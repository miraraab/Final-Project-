from dotenv import load_dotenv
from pathlib import Path
import json
from langsmith import Client, traceable, evaluate
import anthropic
from target_function import generate_project_summary

# Load .env from project root
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

# Initialize clients at module level
ls_client = Client()
anthropic_client = anthropic.Anthropic()


@traceable
def report_quality_evaluator(inputs: dict, outputs: dict, reference_outputs: dict) -> dict:
    """
    LLM-as-judge evaluator that scores the generated report on 3 criteria:
    - completeness: mentions key points from expected_summary_contains
    - risk_clarity: risk status clearly communicated
    - professional_tone: appropriate for executive reporting in German energy sector
    """
    try:
        # Extract key fields for evaluation context
        project_name = inputs.get("project_name", "Unknown")
        risk_flag = inputs.get("risk_flag", "No")
        generated_report = outputs.get("report_section", "")
        expected_points = reference_outputs.get("expected_summary_contains", [])

        # Build evaluation prompt
        eval_prompt = f"""You are an expert evaluator for corporate portfolio reporting.
Score the generated project status report on 3 criteria (each 1-5 scale).

PROJECT CONTEXT:
- Project Name: {project_name}
- Risk Flag: {risk_flag}
- Expected to mention: {', '.join(expected_points)}

GENERATED REPORT:
{generated_report}

SCORING CRITERIA:
1. Completeness (1-5): Does the report address all expected points? (project name, risk/status, budget, milestone, lead name)
2. Risk Clarity (1-5): Is the risk level ({risk_flag}) and escalation status clearly communicated? 1=not mentioned, 5=prominently flagged
3. Professional Tone (1-5): Is language appropriate for executive reporting in German energy sector? 1=informal, 5=excellent

RESPONSE FORMAT:
Return ONLY valid JSON, no markdown, no preamble. No code blocks.

{{
  "completeness": <int 1-5>,
  "risk_clarity": <int 1-5>,
  "professional_tone": <int 1-5>,
  "reasoning": "<one sentence per criterion, semicolon-separated>"
}}
"""

        # Call Claude Sonnet 4.6 for evaluation
        message = anthropic_client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=300,
            messages=[
                {"role": "user", "content": eval_prompt}
            ]
        )

        response_text = message.content[0].text.strip()

        # Parse JSON response (handle potential markdown code blocks)
        if response_text.startswith("```"):
            # Extract JSON from code block
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]
            response_text = response_text.strip()

        eval_result = json.loads(response_text)

        # Calculate average score
        scores = [
            eval_result.get("completeness", 0),
            eval_result.get("risk_clarity", 0),
            eval_result.get("professional_tone", 0),
        ]
        average_score = sum(scores) / len(scores) if scores else 0

        # Store detailed scores for later aggregation
        return {
            "key": "report_quality",
            "score": round(average_score, 2),
            "comment": f"C:{eval_result.get('completeness')}/5 RC:{eval_result.get('risk_clarity')}/5 PT:{eval_result.get('professional_tone')}/5",
        }

    except Exception as e:
        return {
            "key": "report_quality",
            "score": 0,
            "comment": f"EVAL ERROR: {str(e)}",
        }


if __name__ == "__main__":
    print("=" * 80)
    print("LangSmith Evaluation: dena IME Portfolio Report Generation")
    print("=" * 80)
    print("\nStarting evaluation run...")
    print("Dataset: dena-ime-portfolio-reports")
    print("Target function: generate_project_summary")
    print("Evaluator: report_quality_evaluator (LLM-as-judge)")
    print("Max concurrency: 2")
    print("\nThis may take a few minutes...\n")

    # Run evaluation
    results = evaluate(
        generate_project_summary,
        data="dena-ime-portfolio-reports",
        evaluators=[report_quality_evaluator],
        experiment_prefix="claude-sonnet-portfolio-eval-v1",
        max_concurrency=2,
    )

    print("\n" + "=" * 80)
    print("EVALUATION RESULTS")
    print("=" * 80)

    # Extract and aggregate results using to_pandas()
    all_scores = []

    try:
        df = results.to_pandas()
        print(f"\nDataFrame columns: {df.columns.tolist()}")

        print("\nPer-Example Scores:")
        print("-" * 80)

        for i, row in df.iterrows():
            # Extract project name from the dataframe column
            project_name = row.get("inputs.project_name", "Unknown")
            score = 0

            # Extract score from feedback
            feedback_col = row.get("feedback.report_quality")
            if feedback_col is not None:
                if isinstance(feedback_col, dict):
                    score = feedback_col.get("score", 0)
                elif isinstance(feedback_col, (int, float)):
                    score = feedback_col

            all_scores.append(score)

            print(f"\n{i+1}. {project_name}")
            print(f"   Overall Score: {score}/5")

    except Exception as e:
        print(f"Error extracting results: {e}")
        print("Falling back to direct iteration...")

    # Calculate and print aggregated results
    print("\n" + "=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)

    if all_scores:
        mean_score = sum(all_scores) / len(all_scores)
        print(f"\nTotal Examples Evaluated: {len(all_scores)}")
        print(f"Mean Overall Score: {mean_score:.2f}/5")
        print(f"Min Score: {min(all_scores)}/5")
        print(f"Max Score: {max(all_scores)}/5")
    else:
        print("\nNo results to aggregate.")

    # Print LangSmith experiment URL
    print("\n" + "=" * 80)
    print("LANGSMITH EXPERIMENT")
    print("=" * 80)
    print(f"\nExperiment Name: {results.experiment_name}")
    print(f"Experiment URL: {results.url}")

    print("\n" + "=" * 80)
    print("Evaluation complete!")
    print("=" * 80)
