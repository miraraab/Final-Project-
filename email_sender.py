import logging
import os
import base64
from datetime import datetime
from resend import Emails
from chart_agent import generate_portfolio_charts
from data_validator import build_validation_banner_html

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


def build_summary_html(summary: dict) -> str:
    """Build executive summary section from JSON."""
    headline = summary.get('headline', 'Portfolio analysis in progress')
    red = summary.get('red', 0)
    amber = summary.get('amber', 0)
    green = summary.get('green', 0)
    total_budget = summary.get('total_budget_eur', 0)
    spend_confirmed = summary.get('spend_confirmed', False)

    status_badge = f"<span style='color: #dc2626; font-weight: 600;'>{red} Red</span> · <span style='color: #f59e0b; font-weight: 600;'>{amber} Amber</span> · <span style='color: #16a34a; font-weight: 600;'>{green} Green</span>"

    budget_note = "" if spend_confirmed else "<em>(Spend figures pending final confirmation)</em>"

    return f"""
    <div style="background-color: #eff6ff; border-left: 4px solid #3b82f6; padding: 16px; margin-bottom: 16px; border-radius: 4px;">
        <h2 style="margin: 0 0 12px 0; color: #1f2937; font-size: 16px; font-weight: 600;">
            📊 Executive Summary
        </h2>
        <div style="color: #374151; font-size: 14px; line-height: 1.6;">
            <p><strong>{headline}</strong></p>
            <p>Portfolio status: {status_badge}</p>
            <p>Total budget: €{total_budget:,.0f} {budget_note}</p>
        </div>
    </div>
    """


def build_actions_html(actions: list) -> str:
    """Build immediate actions section from JSON."""
    if not actions:
        return ""

    items = ""
    for action in actions:
        project_id = action.get('project_id', '')
        project_name = action.get('project_name', '')
        issue = action.get('issue', '')
        act = action.get('action', '')
        owner = action.get('owner', '')
        deadline = action.get('deadline', '')

        items += f"""
        <div style="background-color: white; border: 1px solid #fee2e2; border-radius: 4px; padding: 12px; margin-bottom: 10px;">
            <p style="margin: 0 0 6px 0; font-weight: 600; color: #991b1b;">{project_id}: {project_name}</p>
            <p style="margin: 0 0 6px 0; color: #374151;"><strong>Issue:</strong> {issue}</p>
            <p style="margin: 0 0 6px 0; color: #374151;"><strong>Action:</strong> {act}</p>
            <p style="margin: 0; color: #6b7280; font-size: 13px;"><strong>Owner:</strong> {owner} | <strong>Deadline:</strong> {deadline}</p>
        </div>
        """

    return f"""
    <div style="background-color: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; margin-bottom: 16px; border-radius: 4px;">
        <h2 style="margin: 0 0 12px 0; color: #991b1b; font-size: 16px; font-weight: 600;">
            ⚠️ Immediate Actions Required
        </h2>
        {items}
    </div>
    """


def build_amber_html(amber: list) -> str:
    """Build projects at risk section from JSON."""
    if not amber:
        return ""

    items = ""
    for project in amber:
        project_id = project.get('project_id', '')
        project_name = project.get('project_name', '')
        watch_point = project.get('watch_point', '')

        items += f"""
        <div style="padding: 8px 0; border-bottom: 1px solid #fef3c7; color: #374151; font-size: 13px;">
            <strong>{project_id}: {project_name}</strong><br>
            <em style="color: #6b7280;">Watch:</em> {watch_point}
        </div>
        """

    return f"""
    <div style="background-color: #fffbeb; border-left: 4px solid #f59e0b; padding: 16px; margin-bottom: 16px; border-radius: 4px;">
        <h2 style="margin: 0 0 12px 0; color: #92400e; font-size: 16px; font-weight: 600;">
            🟠 Projects at Risk
        </h2>
        <div style="color: #374151; font-size: 14px;">
            {items}
        </div>
    </div>
    """


def build_green_html(green: list) -> str:
    """Build on-track projects section from JSON."""
    if not green:
        return ""

    items = ""
    for project in green:
        project_id = project.get('project_id', '')
        project_name = project.get('project_name', '')
        milestone = project.get('milestone', '')
        due = project.get('due', '')

        items += f"""
        <div style="padding: 8px 0; border-bottom: 1px solid #dcfce7; color: #374151; font-size: 13px;">
            <strong>{project_id}: {project_name}</strong><br>
            Next milestone: {milestone} ({due})
        </div>
        """

    return f"""
    <div style="background-color: #f0fdf4; border-left: 4px solid #16a34a; padding: 16px; margin-bottom: 16px; border-radius: 4px;">
        <h2 style="margin: 0 0 12px 0; color: #166534; font-size: 16px; font-weight: 600;">
            ✅ On-Track Projects
        </h2>
        <div style="color: #374151; font-size: 14px;">
            {items}
        </div>
    </div>
    """


def build_budget_html(budget_flags: list, total_budget: int) -> str:
    """Build budget overview section from JSON."""
    critical_count = sum(1 for b in budget_flags if b.get('severity') == 'critical')
    warning_count = sum(1 for b in budget_flags if b.get('severity') == 'warning')

    flags_html = ""
    for flag in budget_flags:
        project_id = flag.get('project_id', '')
        remaining = flag.get('remaining_eur', 0)
        severity = flag.get('severity', 'info')

        color = '#dc2626' if severity == 'critical' else '#f59e0b' if severity == 'warning' else '#6b7280'
        badge = '🔴' if severity == 'critical' else '🟠' if severity == 'warning' else '⚪'

        flags_html += f"""
        <div style="padding: 8px; color: {color}; font-size: 13px;">
            {badge} {project_id}: €{remaining:,.0f} remaining
        </div>
        """

    summary = f"<p style='margin: 0 0 8px 0;'><strong>{critical_count}</strong> critical | <strong>{warning_count}</strong> warning</p>"

    return f"""
    <div style="background-color: #f5f3ff; border-left: 4px solid #a855f7; padding: 16px; margin-bottom: 16px; border-radius: 4px;">
        <h2 style="margin: 0 0 12px 0; color: #6b21a8; font-size: 16px; font-weight: 600;">
            💰 Budget Overview
        </h2>
        {summary}
        {flags_html}
    </div>
    """


def build_recommendations_html(actions: list) -> str:
    """Build leadership actions section from JSON."""
    if not actions:
        return ""

    items = ""
    for i, action in enumerate(actions, 1):
        items += f"""
        <div style="margin-bottom: 8px; padding-bottom: 8px; border-bottom: 1px solid #dbeafe; color: #374151; font-size: 14px;">
            <strong>{i}.</strong> {action}
        </div>
        """

    return f"""
    <div style="background-color: #f0f9ff; border-left: 4px solid #0284c7; padding: 16px; margin-bottom: 16px; border-radius: 4px;">
        <h2 style="margin: 0 0 12px 0; color: #0c4a6e; font-size: 16px; font-weight: 600;">
            🎯 Recommended Leadership Actions
        </h2>
        <div style="color: #374151;">
            {items}
        </div>
    </div>
    """


def build_html_email(report_json: dict, projects: list[dict], report_date: str, charts: dict = None, validation: dict = None) -> str:
    """
    Build HTML email template from structured JSON report.

    Args:
        report_json: Structured JSON report from Claude
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

    # Build sections from JSON
    summary_html = build_summary_html(report_json.get('summary', {}))
    actions_html = build_actions_html(report_json.get('immediate_actions', []))
    amber_html = build_amber_html(report_json.get('amber_projects', []))
    green_html = build_green_html(report_json.get('green_milestones', []))
    budget_html = build_budget_html(
        report_json.get('budget_flags', []),
        report_json.get('summary', {}).get('total_budget_eur', 0)
    )
    recommendations_html = build_recommendations_html(report_json.get('leadership_actions', []))

    # Build validation HTML
    validation_html = build_validation_banner_html(validation) if validation else ""

    # Build charts HTML with cid references (for email attachments)
    charts_html = ""
    if charts and charts.get("risk_chart_b64"):
        charts_html = f"""
    <div style="margin-bottom: 24px;">
      <h2 style="color: #003087; font-size: 16px; font-weight: 600; margin-bottom: 16px;">📈 Portfolio Dashboard</h2>
      <table width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td width="40%" style="padding-right: 12px; vertical-align: top;">
            <img src="cid:risk_chart" width="100%" style="max-width: 280px; display: block;" alt="Risk Status"/>
          </td>
          <td width="60%" style="vertical-align: top;">
            <img src="cid:budget_chart" width="100%" style="display: block;" alt="Budget Utilization"/>
          </td>
        </tr>
      </table>
    </div>
    """

    sections_html = summary_html + validation_html + charts_html + actions_html + amber_html + green_html + budget_html + recommendations_html

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
    api_key: str,
    charts: dict = None,
    validation: dict = None
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

        # Ensure validation is a dict, not a string
        if isinstance(validation, str):
            logger.warning(f"Validation was a string: {validation[:100]}, converting to empty dict")
            validation = {}

        logger.debug(f"Validation type: {type(validation)}, keys: {list(validation.keys()) if isinstance(validation, dict) else 'N/A'}")

        try:
            html_body = build_html_email(report_text, projects, report_date, charts=charts, validation=validation)
        except Exception as e:
            logger.error(f"Error building HTML email: {e}", exc_info=True)
            raise

        # Build email payload with optional attachments
        email_payload = {
            "from": sender_email,
            "to": recipient_email,
            "subject": f"IME Division Weekly Portfolio Report — {report_date}",
            "html": html_body
        }

        # Add chart attachments if available
        if charts and charts.get("risk_chart_b64"):
            try:
                risk_bytes = base64.b64decode(charts["risk_chart_b64"])
                budget_bytes = base64.b64decode(charts["budget_chart_b64"])

                email_payload["attachments"] = [
                    {
                        "filename": "risk_chart.png",
                        "content": list(risk_bytes),
                        "content_id": "risk_chart"
                    },
                    {
                        "filename": "budget_chart.png",
                        "content": list(budget_bytes),
                        "content_id": "budget_chart"
                    }
                ]
                logger.info("Chart attachments added to email")
            except Exception as e:
                logger.warning(f"Error adding chart attachments: {e}")

        response = client.send(email_payload)

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
