import logging
import os
from datetime import datetime
from resend import Emails

logger = logging.getLogger(__name__)


def check_escalations(projects: list[dict]) -> tuple[bool, int]:
    """
    Check if any projects have escalation flags.

    Args:
        projects: List of project dicts

    Returns:
        Tuple of (has_escalations, count)
    """
    escalation_count = sum(
        1 for p in projects
        if p.get("escalation") and p.get("escalation", "").lower() == "yes"
    )
    return escalation_count > 0, escalation_count


def build_html_email(report_text: str, projects: list[dict], report_date: str) -> str:
    """
    Build HTML email template with report content.

    Args:
        report_text: Plain text report from Claude
        projects: List of project dicts (for escalation check)
        report_date: Date string (Monday of report week)

    Returns:
        HTML email body
    """
    has_escalations, esc_count = check_escalations(projects)

    escalation_banner = ""
    if has_escalations:
        escalation_banner = f"""
        <div style="background-color: #dc2626; color: white; padding: 16px; margin-bottom: 24px; border-radius: 4px; font-weight: bold;">
            ⚠ ACTION REQUIRED: {esc_count} project(s) require immediate escalation
        </div>
        """

    # Escape report text for HTML and preserve line breaks
    escaped_report = report_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    escaped_report = escaped_report.replace("\n", "<br>")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            .header {{
                border-bottom: 3px solid #1f2937;
                padding-bottom: 16px;
                margin-bottom: 24px;
            }}
            .header h1 {{
                margin: 0;
                font-size: 24px;
                color: #1f2937;
            }}
            .subheader {{
                font-size: 14px;
                color: #6b7280;
                margin-top: 8px;
            }}
            .content {{
                background-color: #f9fafb;
                padding: 20px;
                border-radius: 6px;
                font-family: "Monaco", "Courier New", monospace;
                font-size: 13px;
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
            .footer {{
                margin-top: 24px;
                padding-top: 16px;
                border-top: 1px solid #e5e7eb;
                font-size: 12px;
                color: #9ca3af;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>IME Division — Weekly Portfolio Report</h1>
            <div class="subheader">Week of {report_date} • AI-generated draft — human review required</div>
        </div>

        {escalation_banner}

        <div class="content">
{escaped_report}
        </div>

        <div class="footer">
            Auto-generated report. Review before distributing.
        </div>
    </body>
    </html>
    """
    return html


def send_email(
    report_text: str,
    projects: list[dict],
    sender_email: str,
    recipient_email: str,
    api_key: str
) -> bool:
    """
    Send formatted HTML email via Resend.

    Args:
        report_text: Plain text report
        projects: List of project dicts
        sender_email: From email address
        recipient_email: To email address
        api_key: Resend API key

    Returns:
        True if sent successfully, False otherwise
    """
    try:
        os.environ['RESEND_API_KEY'] = api_key
        client = Emails()

        # Get Monday of current week
        today = datetime.now()
        monday = today - __import__('datetime').timedelta(days=today.weekday())
        report_date = monday.strftime("%Y-%m-%d")

        html_body = build_html_email(report_text, projects, report_date)

        response = client.send({
            "from": sender_email,
            "to": recipient_email,
            "subject": f"IME Division Weekly Portfolio Report — {report_date}",
            "html": html_body
        })

        logger.info(f"Email sent successfully. Message ID: {response.id}")
        return True

    except Exception as e:
        logger.error(f"Error sending email via Resend: {e}")
        return False


def send_fallback_email(
    error_message: str,
    sender_email: str,
    recipient_email: str,
    api_key: str
) -> bool:
    """
    Send fallback email when report generation fails.

    Args:
        error_message: Error description
        sender_email: From email address
        recipient_email: To email address
        api_key: Resend API key

    Returns:
        True if sent successfully, False otherwise
    """
    try:
        os.environ['RESEND_API_KEY'] = api_key
        client = Emails()

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px;">
            <h2>IME Division Weekly Portfolio Report — ERROR</h2>
            <p>The automated report could not be generated due to the following error:</p>
            <pre style="background-color: #f3f4f6; padding: 16px; border-radius: 4px; overflow-x: auto;">
{error_message}
            </pre>
            <p>Please check the logs and investigate.</p>
        </body>
        </html>
        """

        response = client.send({
            "from": sender_email,
            "to": recipient_email,
            "subject": "IME Division Weekly Portfolio Report — ERROR",
            "html": html
        })

        logger.info(f"Fallback error email sent. Message ID: {response.id}")
        return True

    except Exception as e:
        logger.error(f"Error sending fallback email: {e}")
        return False
