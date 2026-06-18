import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import io
import base64
import logging

logger = logging.getLogger(__name__)


def generate_portfolio_charts(projects: list[dict]) -> dict:
    """
    Generate two charts from project portfolio data.

    Args:
        projects: List of project dicts with keys:
                 - overall_status: str ("Green", "Amber", "Red")
                 - project_name: str
                 - budget: float or None
                 - spend_ytd: float or None

    Returns:
        Dict with keys:
        - "risk_chart_b64": base64-encoded PNG string (or None on error)
        - "budget_chart_b64": base64-encoded PNG string (or None on error)
    """
    risk_chart_b64 = None
    budget_chart_b64 = None

    try:
        logger.info(f"Generating risk status chart for {len(projects)} projects")
        risk_chart_b64 = _generate_risk_status_chart(projects)
        logger.info("Risk status chart generated successfully")
    except Exception as e:
        logger.error(f"Error generating risk status chart: {e}", exc_info=True)

    try:
        logger.info(f"Generating budget utilization chart for {len(projects)} projects")
        budget_chart_b64 = _generate_budget_utilization_chart(projects)
        logger.info("Budget utilization chart generated successfully")
    except Exception as e:
        logger.error(f"Error generating budget utilization chart: {e}", exc_info=True)

    return {
        "risk_chart_b64": risk_chart_b64,
        "budget_chart_b64": budget_chart_b64,
    }


def _generate_risk_status_chart(projects: list[dict]) -> str:
    """Generate donut chart for portfolio risk status distribution."""
    # Count projects by status (case-insensitive)
    status_counts = {"Green": 0, "Amber": 0, "Red": 0}

    logger.info(f"Processing {len(projects)} projects for risk chart")

    for i, project in enumerate(projects):
        status = project.get("overall_status")
        if status is None:
            logger.debug(f"Project {i}: overall_status is None")
            continue
        status_str = str(status).lower().strip()
        logger.debug(f"Project {i}: overall_status='{status}' -> '{status_str}'")
        if status_str == "green":
            status_counts["Green"] += 1
        elif status_str == "amber":
            status_counts["Amber"] += 1
        elif status_str == "red":
            status_counts["Red"] += 1

    logger.info(f"Risk chart counts: {status_counts}")

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(5, 5), dpi=150)
    fig.patch.set_facecolor('white')

    # Data and colors
    sizes = [status_counts["Green"], status_counts["Amber"], status_counts["Red"]]
    labels = ["Green", "Amber", "Red"]
    colors = ["#2ECC71", "#F39C12", "#E74C3C"]

    # Create donut chart
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct="%1.0f%%",
        startangle=90,
        wedgeprops=dict(width=0.5, edgecolor="white", linewidth=2),
        textprops={"color": "black", "fontsize": 10},
    )

    # Add center text with total count (total number of projects passed in)
    total_projects = len(projects)
    ax.text(
        0, 0,
        str(total_projects),
        ha="center", va="center",
        fontsize=24, fontweight="bold",
        color="#003087",
    )

    # Title
    ax.set_title(
        "Portfolio Risk Status",
        fontsize=14,
        fontweight="bold",
        color="#003087",
        pad=20,
    )

    # Clean style
    ax.axis("off")

    # Save to buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight", facecolor="white")
    buffer.seek(0)
    plt.close(fig)

    # Encode to base64
    chart_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return chart_b64


def _generate_budget_utilization_chart(projects: list[dict]) -> str:
    """Generate horizontal bar chart for budget utilization by project."""
    # Filter projects with valid budget and spend data
    budget_data = []

    for project in projects:
        budget = project.get("budget")
        spend_ytd = project.get("spend_ytd")

        # Convert to float, handling both None and string values
        try:
            if budget is None or spend_ytd is None:
                continue
            budget = float(budget)
            spend_ytd = float(spend_ytd)

            if budget > 0:
                pct = (spend_ytd / budget) * 100
                project_name = project.get("project_name", "Unknown")
                # Truncate project name to 28 chars
                if len(project_name) > 28:
                    project_name = project_name[:25] + "..."
                budget_data.append({
                    "name": project_name,
                    "pct": pct,
                    "spend": spend_ytd,
                    "budget": budget,
                })
        except (ValueError, TypeError):
            # Skip projects with invalid budget/spend data
            continue

    # Sort by percentage descending
    budget_data.sort(key=lambda x: x["pct"], reverse=True)

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 8), dpi=150)
    fig.patch.set_facecolor('white')

    # Prepare data for bar chart
    names = [item["name"] for item in budget_data]
    percentages = [item["pct"] for item in budget_data]

    # Determine colors based on percentage
    colors = []
    for pct in percentages:
        if pct > 90:
            colors.append("#E74C3C")  # Red
        elif pct > 75:
            colors.append("#F39C12")  # Amber
        else:
            colors.append("#2ECC71")  # Green

    # Create horizontal bar chart
    bars = ax.barh(names, percentages, color=colors, edgecolor="black", linewidth=0.5)

    # Add vertical dashed line at 100%
    ax.axvline(x=100, color="#003087", linestyle="--", linewidth=2, alpha=0.7)

    # Add value labels at end of bars
    for i, (bar, pct) in enumerate(zip(bars, percentages)):
        label_x = pct + 2
        ax.text(label_x, i, f"{pct:.1f}%", va="center", fontsize=9, fontweight="bold")

    # Styling
    ax.set_xlabel("Budget Utilization (%)", fontsize=11, fontweight="bold", color="#003087")
    ax.set_title(
        "Budget Utilization by Project",
        fontsize=14,
        fontweight="bold",
        color="#003087",
        pad=20,
    )
    ax.set_xlim(0, max(max(percentages) + 15, 120))

    # Clean style
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#CCCCCC")
    ax.spines["bottom"].set_color("#CCCCCC")
    ax.grid(axis="x", alpha=0.3, linestyle=":", linewidth=0.5)

    # Tight layout
    plt.tight_layout()

    # Save to buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight", facecolor="white")
    buffer.seek(0)
    plt.close(fig)

    # Encode to base64
    chart_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return chart_b64


if __name__ == "__main__":
    # Test with 5 mock projects using exact key names
    mock_projects = [
        {
            "overall_status": "Green",
            "project_name": "Industrial Energy Efficiency Programme",
            "budget": 320000,
            "spend_ytd": 285000,
        },
        {
            "overall_status": "Red",
            "project_name": "Hydrogen Readiness SME Network",
            "budget": 540000,
            "spend_ytd": 198000,
        },
        {
            "overall_status": "Amber",
            "project_name": "District Heating Transition Initiative",
            "budget": 450000,
            "spend_ytd": 380000,
        },
        {
            "overall_status": "Green",
            "project_name": "EV Fleet Transition Public Sector",
            "budget": 600000,
            "spend_ytd": 120000,
        },
        {
            "overall_status": "Green",
            "project_name": "Carbon Neutrality Roadmap Development",
            "budget": 250000,
            "spend_ytd": 240000,
        },
    ]

    print("=" * 80)
    print("Chart Generation Test")
    print("=" * 80)

    # Debug: show all unique overall_status values
    unique_statuses = set()
    status_values = []
    for project in mock_projects:
        status = project.get("overall_status")
        status_values.append(status)
        if status is not None:
            unique_statuses.add(str(status).lower().strip())

    print(f"\nTotal projects: {len(mock_projects)}")
    print(f"All status values found: {status_values}")
    print(f"Unique status values (normalized): {sorted(unique_statuses)}")

    # Generate charts
    charts = generate_portfolio_charts(mock_projects)

    # Save test PNG files
    if charts["risk_chart_b64"]:
        risk_png = base64.b64decode(charts["risk_chart_b64"])
        with open("test_risk.png", "wb") as f:
            f.write(risk_png)
        print("\n✓ Risk status chart saved as test_risk.png")
    else:
        print("\n✗ Risk status chart generation failed")

    if charts["budget_chart_b64"]:
        budget_png = base64.b64decode(charts["budget_chart_b64"])
        with open("test_budget.png", "wb") as f:
            f.write(budget_png)
        print("✓ Budget utilization chart saved as test_budget.png")
    else:
        print("✗ Budget utilization chart generation failed")

    print(f"\nChart sizes:")
    print(f"Risk chart: {len(charts['risk_chart_b64']) if charts['risk_chart_b64'] else 'N/A'} bytes (base64)")
    print(f"Budget chart: {len(charts['budget_chart_b64']) if charts['budget_chart_b64'] else 'N/A'} bytes (base64)")
    print("=" * 80)
