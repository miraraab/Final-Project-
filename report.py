import logging
from anthropic import Anthropic

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a senior project controlling analyst for dena (Deutsche Energie-Agentur),
a German federal energy agency managing 25+ publicly funded projects.

Analyse the project portfolio data and generate a structured weekly division
status report for IME Division Leadership.

Report structure:
1. Executive Summary (3-5 sentences): portfolio health, total budget consumed,
   red/amber/green count, key message.
2. Immediate Actions Required: ONLY escalation-flagged projects.
   For each: name, issue (1 sentence), recommended action with owner and deadline.
3. Projects at Risk (Amber): brief note per project, what to watch.
4. On-Track Projects (Green): confirm status, flag milestones due in next 14 days.
5. Budget Overview: total spend vs budget, any projects >90% consumed,
   forecast overruns.
6. Recommended Leadership Actions: max 3 bullet points, concrete and actionable.

Tone: professional, concise, decision-oriented. Written for a non-technical
division head. Max 700 words. Plain text with clear section headers."""


def format_portfolio_data(projects: list[dict]) -> str:
    """
    Format project list into structured text for Claude analysis.

    Args:
        projects: List of project dicts

    Returns:
        Formatted text representation of portfolio
    """
    if not projects:
        return "No project data available."

    lines = ["PROJECT PORTFOLIO DATA:\n"]
    for i, project in enumerate(projects, 1):
        lines.append(f"Project {i}:")
        for key, value in project.items():
            lines.append(f"  {key}: {value}")
        lines.append("")

    return "\n".join(lines)


def generate_report(projects: list[dict], api_key: str) -> str:
    """
    Call Claude API to generate analysis report from project data.

    Args:
        projects: List of project dicts
        api_key: Anthropic API key

    Returns:
        Report text from Claude, or error message if API call fails
    """
    client = Anthropic(api_key=api_key)
    portfolio_text = format_portfolio_data(projects)

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2048,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": f"Please analyze this portfolio and provide the weekly status report:\n\n{portfolio_text}"
                }
            ]
        )

        report = message.content[0].text
        logger.info("Report generated successfully from Claude API")
        return report

    except Exception as e:
        logger.error(f"Error calling Claude API: {e}")
        return None
