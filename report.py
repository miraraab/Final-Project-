import logging
import json
import re
from anthropic import Anthropic

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a senior project controlling analyst for dena (Deutsche Energie-Agentur).
Respond with ONLY valid, properly-formatted JSON. NO preamble, NO markdown, NO explanation, NO text before or after the JSON.

CRITICAL REQUIREMENTS:
- Return ONLY the JSON object, nothing else. Start with { and end with }
- ALL string values must be on ONE LINE with NO actual newlines (use spaces instead)
- Keep all string values under 100 characters
- Ensure proper JSON escaping: use \\\\ for backslashes, \\" for quotes
- Arrays must be compact (ok to have on multiple lines structurally, but each string value is one line)

Return this exact JSON structure (adjust values to match data):
{
  "summary": {
    "total_projects": 25,
    "red": 5,
    "amber": 6,
    "green": 14,
    "total_budget_eur": 8000000,
    "spend_confirmed": true,
    "headline": "One sentence summary max 150 chars. Use \\\\n for visual breaks if needed."
  },
  "immediate_actions": [
    {
      "project_id": "IME-XXX",
      "project_name": "Full project name",
      "issue": "One sentence issue description",
      "action": "Recommended action to take",
      "owner": "Role or name of responsible person",
      "deadline": "Date or timeframe"
    }
  ],
  "amber_projects": [
    {
      "project_id": "IME-XXX",
      "project_name": "Full project name",
      "watch_point": "Specific point to monitor"
    }
  ],
  "green_milestones": [
    {
      "project_id": "IME-XXX",
      "project_name": "Full project name",
      "milestone": "Milestone name",
      "due": "Date or timeframe"
    }
  ],
  "budget_flags": [
    {
      "project_id": "IME-XXX",
      "remaining_eur": 50000,
      "severity": "critical"
    }
  ],
  "leadership_actions": [
    "Concrete action one as complete sentence.",
    "Concrete action two as complete sentence."
  ]
}

Analysis rules:
- immediate_actions: ONLY escalation-flagged (column J = Yes) projects
- amber_projects: ONLY amber-status (column I = Amber) projects
- green_milestones: ONLY green-status (column I = Green) projects with upcoming milestones
- budget_flags: ONLY projects with >90% budget consumed
- leadership_actions: max 3 concrete, actionable items
- All budget values as integers (euros)
- String values must not contain actual newlines — use spaces or \\n escape sequences

ABSOLUTELY CRITICAL: Return ONLY the JSON object. Begin with { and end with }. Nothing else."""


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


def generate_report(projects: list[dict], api_key: str) -> dict:
    """
    Call Claude API to generate structured JSON analysis report from project data.

    Args:
        projects: List of project dicts
        api_key: Anthropic API key

    Returns:
        Parsed JSON report dict, or None if API call/parsing fails
    """
    client = Anthropic(api_key=api_key)
    portfolio_text = format_portfolio_data(projects)

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=3000,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": f"Analyze this portfolio and respond ONLY with the JSON object:\n\n{portfolio_text}"
                }
            ]
        )

        response_text = message.content[0].text.strip()
        logger.info("Raw response from Claude received")

        # Remove markdown code fences if present
        if response_text.startswith("```"):
            response_text = response_text.split("\n", 1)[1]
        if response_text.endswith("```"):
            response_text = response_text.rsplit("\n", 1)[0]

        response_text = response_text.strip()

        try:
            report = json.loads(response_text)
            logger.info("Report JSON parsed successfully from Claude API")
            return report
        except json.JSONDecodeError as e:
            logger.warning(f"JSON parsing failed: {e}")
            # Fix: preserve JSON structure but fix string newlines
            # Replace newlines that appear inside string values (between quotes) with spaces
            fixed = _fix_json_string_newlines(response_text)
            try:
                report = json.loads(fixed)
                logger.info("Report JSON parsed after fixing string newlines")
                return report
            except Exception as e2:
                logger.error(f"JSON repair failed: {e2}")
                logger.error(f"Raw response preview: {response_text[:300]}")
                raise Exception(f"Claude response was not valid JSON: {e}")

    except Exception as e:
        logger.error(f"Error generating report: {e}")
        return None


def _fix_json_string_newlines(text: str) -> str:
    """Replace newlines inside JSON string values with spaces, preserving structure."""
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
