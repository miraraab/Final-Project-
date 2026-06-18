import logging
import sys
from datetime import datetime
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import os

# Load env vars and set RESEND_API_KEY BEFORE importing email_sender
load_dotenv()
resend_api_key = os.getenv("RESEND_API_KEY")
if resend_api_key:
    os.environ['RESEND_API_KEY'] = resend_api_key

from reader import read_excel_data
from report import generate_report
from email_sender import send_email, send_fallback_email
from chart_agent import generate_portfolio_charts
from data_validator import validate_portfolio_data
from news_fetcher import fetch_energy_news, build_news_html

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("dena_report.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def run_report():
    """
    Execute the full report pipeline: read → analyze → email.
    """
    logger.info("=" * 60)
    logger.info("Starting weekly portfolio report generation")
    start_time = datetime.now()

    # Load environment variables
    load_dotenv()

    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    resend_api_key = os.getenv("RESEND_API_KEY")
    news_api_key = os.getenv("NEWS_API_KEY")
    recipient_email = os.getenv("REPORT_RECIPIENT_EMAIL")
    sender_email = os.getenv("REPORT_SENDER_EMAIL")
    data_file_path = os.getenv("DATA_FILE_PATH", "data/dena_IME_mock_dataset_v2.xlsx")

    # Validate required environment variables
    if not all([anthropic_api_key, resend_api_key, recipient_email, sender_email]):
        error_msg = "Missing required environment variables"
        logger.error(error_msg)
        return

    # Step 1: Read Excel data
    logger.info(f"Reading data from {data_file_path}")
    projects = read_excel_data(data_file_path)

    if not projects:
        error_msg = f"Data file not found: {data_file_path}"
        logger.error(error_msg)
        send_fallback_email(error_msg, sender_email, recipient_email, resend_api_key)
        return

    logger.info(f"Read {len(projects)} projects from portfolio")

    # Step 1b: Run data quality check
    logger.info("Running AI data quality check")
    validation = validate_portfolio_data(projects, anthropic_api_key)
    logger.info(f"Data validation: {validation.get('summary', 'no summary')}")
    if not validation.get('passed'):
        logger.warning("Data quality check failed — proceeding with warnings")

    # Step 2: Generate report via Claude
    logger.info("Calling Claude API for report generation")
    report = generate_report(projects, anthropic_api_key)

    if not report:
        error_msg = "Claude API call failed. Check API key and rate limits."
        logger.error(error_msg)
        send_fallback_email(error_msg, sender_email, recipient_email, resend_api_key)
        return

    # Step 2b: Generate charts
    logger.info("Generating portfolio charts")
    charts = generate_portfolio_charts(projects)

    # Step 2c: Fetch energy sector news
    logger.info("Fetching energy sector news")
    news_articles = fetch_energy_news(news_api_key) if news_api_key else []
    news_html = build_news_html(news_articles)
    logger.info(f"Fetched {len(news_articles)} news articles")

    # Step 3: Send email
    logger.info("Sending report email")
    email_sent = send_email(
        report, projects, sender_email, recipient_email, resend_api_key,
        charts=charts, validation=validation, news_html=news_html
    )

    if not email_sent:
        logger.warning("Email send failed, but report was generated successfully")
    else:
        logger.info("Email sent successfully")

    elapsed = (datetime.now() - start_time).total_seconds()
    logger.info(f"Report generation completed in {elapsed:.1f}s")
    logger.info("=" * 60)


def main():
    """
    Initialize scheduler or run report immediately based on CLI flag.
    """
    load_dotenv()

    if len(sys.argv) > 1 and sys.argv[1] == "--now":
        logger.info("Running report immediately (--now flag)")
        run_report()
        return

    # Set up scheduler
    scheduler = BackgroundScheduler()

    # Schedule for every Monday at 08:00
    scheduler.add_job(
        run_report,
        trigger=CronTrigger(day_of_week="mon", hour=8, minute=0),
        id="weekly_report",
        name="Weekly Portfolio Report",
        replace_existing=True
    )

    logger.info("Scheduler initialized")
    logger.info("Weekly report scheduled for: Every Monday at 08:00")

    try:
        scheduler.start()
        logger.info("Scheduler started (blocking)")
        # Keep the scheduler running
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        logger.info("Shutting down scheduler")
        scheduler.shutdown()


if __name__ == "__main__":
    main()
