import json
import logging
from anthropic import Anthropic

logger = logging.getLogger(__name__)


def _repair_json(text: str) -> str:
    """Repair common JSON issues like unterminated strings."""
    result = []
    in_string = False
    escape_next = False
    i = 0

    while i < len(text):
        char = text[i]

        if escape_next:
            result.append(char)
            escape_next = False
            i += 1
            continue

        if char == '\\' and in_string:
            result.append(char)
            escape_next = True
            i += 1
            continue

        if char == '"':
            in_string = not in_string
            result.append(char)
            i += 1
            continue

        # If we're in a string and encounter newline, replace with space
        if in_string and char in '\n\r':
            result.append(' ')
            i += 1
            continue

        result.append(char)
        i += 1

    return ''.join(result)


def format_portfolio_data(projects: list[dict]) -> str:
    """Format project list into structured text for validation."""
    if not projects:
        return "No project data available."

    lines = ["PORTFOLIO DATA FOR VALIDATION:\n"]
    for i, project in enumerate(projects, 1):
        lines.append(f"Project {i}:")
        for key, value in project.items():
            lines.append(f"  {key}: {value}")
        lines.append("")

    return "\n".join(lines)


def validate_portfolio_data(projects: list[dict], api_key: str) -> dict:
    """
    Run AI-powered data quality check on project portfolio.

    Args:
        projects: List of project dicts
        api_key: Anthropic API key

    Returns:
        Validation result dict with passed status, warnings, anomalies, etc.
    """
    client = Anthropic(api_key=api_key)
    portfolio_text = format_portfolio_data(projects)

    system_prompt = """You are a data quality analyst. Return ONLY compact JSON, no markdown, no preamble, no markdown code fences.
Respond with exactly this single-line structure (no newlines inside strings):
{"passed": bool, "project_count": int, "status_distribution": {"green": int, "amber": int, "red": int, "unknown": int}, "warnings": [], "anomalies": [], "data_completeness_pct": float, "summary": "one sentence"}

Check for completeness, plausibility, status validity, and anomalies.
passed = true only if data_completeness_pct >= 80 and no high-severity issues."""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1500,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": f"Analyze this portfolio data for quality issues:\n\n{portfolio_text}"
                }
            ]
        )

        response_text = message.content[0].text.strip()
        logger.info("Data validation response received from Claude")

        # Remove markdown code fences if present
        if response_text.startswith("```"):
            response_text = response_text.split("\n", 1)[1]
        if response_text.endswith("```"):
            response_text = response_text.rsplit("\n", 1)[0]

        response_text = response_text.strip()

        try:
            validation = json.loads(response_text)
            logger.info(f"Data validation result: passed={validation.get('passed')}")
            return validation
        except json.JSONDecodeError as e:
            logger.warning(f"JSON parsing failed for validation: {e}, attempting repair...")
            # Try to fix common JSON issues
            fixed = _repair_json(response_text)
            try:
                validation = json.loads(fixed)
                logger.info(f"Data validation result after repair: passed={validation.get('passed')}")
                return validation
            except Exception as e2:
                logger.error(f"JSON repair failed: {e2}")
                return {
                    "passed": False,
                    "warnings": [],
                    "anomalies": [],
                    "summary": f"Validation error: Could not parse response",
                    "data_completeness_pct": 0,
                    "project_count": 0,
                    "status_distribution": {"green": 0, "amber": 0, "red": 0, "unknown": 0}
                }

    except Exception as e:
        logger.error(f"Data validation failed: {e}")
        return {
            "passed": False,
            "warnings": [],
            "anomalies": [],
            "summary": f"Validation failed: {str(e)}",
            "data_completeness_pct": 0,
            "project_count": 0,
            "status_distribution": {"green": 0, "amber": 0, "red": 0, "unknown": 0}
        }


def build_validation_banner_html(validation: dict) -> str:
    """
    Build HTML banner for data validation results.

    Args:
        validation: Validation result dict from validate_portfolio_data()

    Returns:
        HTML banner string, or empty string if no validation data
    """
    if not validation or not isinstance(validation, dict):
        return ""

    passed = validation.get("passed", False)
    completeness = validation.get("data_completeness_pct", 0)
    project_count = validation.get("project_count", 0)
    warnings = validation.get("warnings", [])
    anomalies = validation.get("anomalies", [])
    summary = validation.get("summary", "")

    # Ensure warnings and anomalies are lists of dicts
    if not isinstance(warnings, list):
        warnings = []
    if not isinstance(anomalies, list):
        anomalies = []

    # Filter out non-dict items
    warnings = [w for w in warnings if isinstance(w, dict)]
    anomalies = [a for a in anomalies if isinstance(a, dict)]

    # Filter for high-severity issues
    high_severity_warnings = [w for w in warnings if w.get("severity") == "high"]
    high_severity_anomalies = [a for a in anomalies if a.get("severity") == "high"]
    all_high_severity = high_severity_warnings + high_severity_anomalies

    # Case 1: Passed with no high-severity issues
    if passed and not all_high_severity:
        return f"""
    <div style="background-color: #dcfce7; border-left: 4px solid #16a34a; padding: 16px; margin-bottom: 16px; border-radius: 4px;">
        <h2 style="margin: 0 0 8px 0; color: #166534; font-size: 14px; font-weight: 600;">
            ✅ Data Quality Check Passed
        </h2>
        <p style="margin: 0; color: #166534; font-size: 13px;">
            {completeness:.0f}% complete • {project_count} projects validated
        </p>
    </div>
    """

    # Case 2: Passed but with warnings/anomalies
    if passed and (warnings or anomalies):
        issues_html = ""

        for warning in warnings:
            severity_badge = "🟡" if warning.get("severity") == "medium" else "🔴"
            issues_html += f"""
        <div style="padding: 6px 0; color: #374151; font-size: 13px;">
            {severity_badge} <strong>{warning.get('project_id', 'Unknown')}</strong> —
            {warning.get('field', 'field')}: {warning.get('issue', 'issue')}
        </div>
        """

        for anomaly in anomalies:
            severity_badge = "🟡" if anomaly.get("severity") == "medium" else "🔴"
            issues_html += f"""
        <div style="padding: 6px 0; color: #374151; font-size: 13px;">
            {severity_badge} <strong>{anomaly.get('project_id', 'Unknown')}</strong> —
            {anomaly.get('description', 'anomaly')}
        </div>
        """

        return f"""
    <div style="background-color: #fffbeb; border-left: 4px solid #f59e0b; padding: 16px; margin-bottom: 16px; border-radius: 4px;">
        <h2 style="margin: 0 0 12px 0; color: #92400e; font-size: 14px; font-weight: 600;">
            ⚠️ Data Quality Warnings
        </h2>
        <p style="margin: 0 0 8px 0; color: #92400e; font-size: 13px; font-weight: 500;">
            {completeness:.0f}% complete • {project_count} projects • {len(warnings) + len(anomalies)} issue(s)
        </p>
        <div style="color: #92400e; font-size: 13px;">
            {issues_html}
        </div>
    </div>
    """

    # Case 3: Failed validation
    issues_html = ""
    for issue in all_high_severity[:5]:  # Show max 5 issues
        issues_html += f"""
    <div style="padding: 6px 0; color: #7c2d12; font-size: 13px;">
        🔴 <strong>{issue.get('project_id') or issue.get('description', 'Unknown')}</strong> —
        {issue.get('issue') or issue.get('description', 'High severity issue')}
    </div>
    """

    return f"""
    <div style="background-color: #fef2f2; border-left: 4px solid #dc2626; padding: 16px; margin-bottom: 16px; border-radius: 4px;">
        <h2 style="margin: 0 0 12px 0; color: #991b1b; font-size: 14px; font-weight: 600;">
            ⚠️ Data Quality Issues Detected
        </h2>
        <p style="margin: 0 0 8px 0; color: #991b1b; font-size: 13px;">
            {summary}
        </p>
        <p style="margin: 0 0 8px 0; color: #991b1b; font-size: 12px; font-weight: 500;">
            <em>Review and correct before distributing to leadership</em>
        </p>
        <div style="color: #991b1b; font-size: 13px;">
            {issues_html}
        </div>
    </div>
    """


if __name__ == "__main__":
    import json as json_module

    # Test with 5 mock projects including 2 intentional errors
    mock_projects = [
        {
            "project_id": "TEST-001",
            "project_name": "Test Project 1",
            "budget": 100000,
            "spend_ytd": 75000,
            "budget_pct": 0.75,
            "overall_status": "Green",
            "escalation": "No",
            "hr_utilisation": 0.65,
            "milestone_status": "On track"
        },
        {
            "project_id": "TEST-002",
            "project_name": "Test Project 2 (OVERSPEND ERROR)",
            "budget": 100000,
            "spend_ytd": 120000,  # ← ERROR: spend > budget
            "budget_pct": 1.20,
            "overall_status": "Red",
            "escalation": "Yes",
            "hr_utilisation": 0.80,
            "milestone_status": "Overdue"
        },
        {
            "project_id": "TEST-003",
            "project_name": "Test Project 3",
            "budget": 150000,
            "spend_ytd": 45000,
            "budget_pct": 0.30,
            "overall_status": "Amber",
            "escalation": "No",
            "hr_utilisation": 0.55,
            "milestone_status": "At risk"
        },
        {
            "project_id": "TEST-004",
            "project_name": "Test Project 4 (MISSING STATUS ERROR)",
            "budget": 80000,
            "spend_ytd": 20000,
            "budget_pct": 0.25,
            # ← ERROR: overall_status missing
            "escalation": "No",
            "hr_utilisation": 0.40,
            "milestone_status": "Planning"
        },
        {
            "project_id": "TEST-005",
            "project_name": "Test Project 5",
            "budget": 200000,
            "spend_ytd": 160000,
            "budget_pct": 0.80,
            "overall_status": "Green",
            "escalation": "No",
            "hr_utilisation": 0.70,
            "milestone_status": "On track"
        },
    ]

    print("=" * 80)
    print("Data Validator Test")
    print("=" * 80)
    print(f"\nTest projects: {len(mock_projects)}")
    print("Intentional errors:")
    print("  - TEST-002: spend_ytd (120000) > budget (100000)")
    print("  - TEST-004: missing overall_status field")

    # Load environment variables
    import os
    from dotenv import load_dotenv
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("\n❌ ANTHROPIC_API_KEY not found in environment")
    else:
        validation = validate_portfolio_data(mock_projects, api_key)

        print("\n" + "=" * 80)
        print("Validation Result:")
        print("=" * 80)
        print(json_module.dumps(validation, indent=2, ensure_ascii=False))

        print("\n" + "=" * 80)
        print("HTML Banner Preview:")
        print("=" * 80)
        banner = build_validation_banner_html(validation)
        if banner:
            print(banner[:500] + "..." if len(banner) > 500 else banner)
        else:
            print("(No banner generated)")

        print("\n" + "=" * 80)
