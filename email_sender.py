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


def parse_report_sections(report_text: str) -> dict:
    """
    Parse report text into structured sections.

    Args:
        report_text: Plain text report from Claude

    Returns:
        Dict with section keys and HTML content
    """
    sections = {}
    current_section = "executive_summary"
    current_content = []

    section_mapping = {
        "Executive Summary": "executive_summary",
        "Immediate Actions Required": "actions",
        "Projects at Risk": "at_risk",
        "On-Track Projects": "on_track",
        "Budget Overview": "budget",
        "Recommended Leadership Actions": "recommendations"
    }

    for line in report_text.split("\n"):
        # Check if line is a section header
        is_header = False
        for header_text, section_key in section_mapping.items():
            if line.strip().startswith(header_text):
                if current_content:
                    sections[current_section] = "\n".join(current_content).strip()
                    current_content = []
                current_section = section_key
                is_header = True
                break

        if not is_header:
            current_content.append(line)

    if current_content:
        sections[current_section] = "\n".join(current_content).strip()

    return sections


def format_section(section_key: str, content: str) -> str:
    """Format a report section as HTML."""

    section_styles = {
        "executive_summary": {
            "title": "📊 Executive Summary",
            "bg": "#eff6ff",
            "border": "#3b82f6",
            "icon": "📊"
        },
        "actions": {
            "title": "⚠️ Immediate Actions Required",
            "bg": "#fef2f2",
            "border": "#dc2626",
            "icon": "⚠️"
        },
        "at_risk": {
            "title": "🟠 Projects at Risk",
            "bg": "#fffbeb",
            "border": "#f59e0b",
            "icon": "🟠"
        },
        "on_track": {
            "title": "✅ On-Track Projects",
            "bg": "#f0fdf4",
            "border": "#16a34a",
            "icon": "✅"
        },
        "budget": {
            "title": "💰 Budget Overview",
            "bg": "#f5f3ff",
            "border": "#a855f7",
            "icon": "💰"
        },
        "recommendations": {
            "title": "🎯 Recommended Leadership Actions",
            "bg": "#f0f9ff",
            "border": "#0284c7",
            "icon": "🎯"
        }
    }

    style = section_styles.get(section_key, section_styles["executive_summary"])

    # Escape HTML in content
    escaped = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    escaped = escaped.replace("\n\n", "</p><p>").replace("\n", "<br>")

    return f"""
    <div style="background-color: {style['bg']}; border-left: 4px solid {style['border']}; padding: 16px; margin-bottom: 16px; border-radius: 4px;">
        <h2 style="margin: 0 0 12px 0; color: #1f2937; font-size: 16px; font-weight: 600;">
            {style['icon']} {style['title']}
        </h2>
        <div style="color: #374151; font-size: 14px; line-height: 1.6;">
            <p>{escaped}</p>
        </div>
    </div>
    """


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
        <div style="background-color: #7c2d12; color: white; padding: 16px; margin-bottom: 24px; border-radius: 6px; font-weight: 600; font-size: 15px;">
            🚨 URGENT: {esc_count} project(s) require immediate escalation — see details below
        </div>
        """

    sections = parse_report_sections(report_text)
    sections_html = ""
    for section_key in ["executive_summary", "actions", "at_risk", "on_track", "budget", "recommendations"]:
        if section_key in sections:
            sections_html += format_section(section_key, sections[section_key])

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {{ margin: 0; padding: 0; }}
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.6;
                color: #1f2937;
                background-color: #f9fafb;
                padding: 0;
            }}
            .wrapper {{
                max-width: 700px;
                margin: 0 auto;
                background-color: white;
            }}
            .header {{
                background: linear-gradient(135deg, #1f2937 0%, #374151 100%);
                color: white;
                padding: 32px 24px;
                text-align: center;
                border-bottom: 4px solid #3b82f6;
            }}
            .header h1 {{
                font-size: 28px;
                font-weight: 700;
                margin-bottom: 8px;
                letter-spacing: -0.5px;
            }}
            .header p {{
                font-size: 13px;
                opacity: 0.9;
            }}
            .content {{
                padding: 32px 24px;
            }}
            .footer {{
                background-color: #f3f4f6;
                padding: 20px 24px;
                border-top: 1px solid #e5e7eb;
                font-size: 12px;
                color: #6b7280;
                text-align: center;
            }}
            h2 {{
                font-size: 16px;
                font-weight: 600;
                margin-bottom: 12px;
            }}
            p {{
                margin-bottom: 12px;
                font-size: 14px;
            }}
            @media (max-width: 600px) {{
                .header h1 {{ font-size: 22px; }}
                .content {{ padding: 20px 16px; }}
                .header {{ padding: 24px 16px; }}
            }}
        </style>
    </head>
    <body>
        <div class="wrapper">
            <div class="header">
                <h1>IME Division</h1>
                <p>Weekly Portfolio Report • Week of {report_date}</p>
            </div>

            <div class="content">
                {escalation_banner}
                {sections_html}
            </div>

            <div class="footer">
                <p><strong>AI-generated draft</strong> — review before distributing to leadership</p>
                <p style="margin-top: 8px;">Generated for dena IME Division | {report_date}</p>
            </div>
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
