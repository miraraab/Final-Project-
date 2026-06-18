from dotenv import load_dotenv
from pathlib import Path
from langsmith import traceable
import anthropic

# Load .env from project root
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

# Initialize Anthropic client at module level
client = anthropic.Anthropic()


@traceable
def generate_project_summary(inputs: dict) -> dict:
    """
    Generate a concise project status summary for weekly leadership reporting.
    Calls Claude Sonnet 4.6 with project portfolio data.
    """
    try:
        # Extract all fields from inputs
        project_id = inputs.get("project_id", "N/A")
        project_name = inputs.get("project_name", "Unknown Project")
        status = inputs.get("status", "Unknown")
        risk_flag = inputs.get("risk_flag", "No")
        project_lead = inputs.get("project_lead", "Unassigned")
        budget_total = inputs.get("budget_total", 0)
        budget_spent_ytd = inputs.get("budget_spent_ytd", 0)
        monthly_status_text = inputs.get("monthly_status_text", "No update")
        next_milestone = inputs.get("next_milestone", "Not defined")
        next_milestone_due = inputs.get("next_milestone_due", "N/A")
        next_milestone_status = inputs.get("next_milestone_status", "Unknown")

        # Calculate budget utilization percentage
        try:
            budget_used_pct = round((budget_spent_ytd / budget_total) * 100, 1) if budget_total > 0 else 0
        except ZeroDivisionError:
            budget_used_pct = 0

        # Build user prompt with all input fields
        user_prompt = f"""
Project Portfolio Data:
- Project ID: {project_id}
- Project Name: {project_name}
- Project Lead: {project_lead}
- Current Status: {status}
- Escalation Flag: {risk_flag}
- Budget Total: €{budget_total:,.0f}
- Budget Spent YTD: €{budget_spent_ytd:,.0f}
- Budget Utilization: {budget_used_pct}%
- Monthly Status: {monthly_status_text}
- Next Milestone: {next_milestone}
- Milestone Due Date: {next_milestone_due}
- Milestone Status: {next_milestone_status}

Please generate a concise project status summary for weekly leadership reporting.
"""

        # Call Claude Sonnet 4.6
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=500,
            system=(
                "You are an AI reporting assistant for the dena IME Division "
                "(Industrie, Mobilität, Energieeffizienz). Generate a concise "
                "project status summary for weekly leadership reporting. "
                "Structure: 1) Status & Risk, 2) Budget, 3) Next Milestone, "
                "4) Project Lead Note. Be precise, flag risks clearly, "
                "use professional German energy sector language. Max 150 words."
            ),
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )

        # Extract response text
        report_section = message.content[0].text

        return {"report_section": report_section}

    except Exception as e:
        return {"report_section": f"ERROR: {str(e)}"}


if __name__ == "__main__":
    # Test the function with a hardcoded example
    test_input = {
        "project_id": "IME-001",
        "project_name": "Industrial Energy Efficiency Programme",
        "status": "Red",
        "risk_flag": "Yes",
        "project_lead": "Dr. A. Müller",
        "budget_total": 320000,
        "budget_spent_ytd": 285000,
        "monthly_status_text": "Final report 80% complete. Budget nearly exhausted, extension request pending.",
        "next_milestone": "Final report submission",
        "next_milestone_due": "2026-06-30",
        "next_milestone_status": "Overdue",
    }

    print("=" * 80)
    print("Testing generate_project_summary()")
    print("=" * 80)
    print(f"\nInput Project: {test_input['project_name']}")
    print(f"Project Lead: {test_input['project_lead']}")
    print(f"Status: {test_input['status']}")

    result = generate_project_summary(test_input)

    print("\n" + "=" * 80)
    print("Generated Report Section:")
    print("=" * 80)
    print(result["report_section"])
    print("\n" + "=" * 80)
