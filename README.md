# dena IME Weekly Report Automation

AI-powered weekly portfolio status report generation with data quality validation, LangSmith evaluation, relevant news aggregation, and formatted email delivery.

## Overview

This system automatically:
1. **Reads** project portfolio data from Excel (25 projects)
2. **Validates** data quality using Claude AI (detects overspends, missing fields, inconsistencies)
3. **Generates** structured portfolio report via Claude API
4. **Creates** visual charts (risk status donut, budget utilization bars)
5. **Fetches** relevant energy sector news from NewsAPI (last 7 days, scored by relevance)
6. **Delivers** complete email with charts, validation banner, and news
7. **Evaluates** report quality using LangSmith (for continuous improvement)

**Schedule:** Every Monday at 08:00 UTC (or manually via `--now`)

## Tech Stack

- **APScheduler** — Scheduled execution
- **openpyxl** — Excel file reading
- **anthropic** — Claude API integration (report generation, data validation)
- **requests** — NewsAPI news fetching
- **resend** — Email delivery with attachments
- **langsmith** — LLM evaluation framework
- **matplotlib** — Chart generation
- **python-dotenv** — Environment variable management

## Project Structure

```
dena-report/
├── main.py                              # Pipeline orchestration & scheduler
├── reader.py                            # Excel reader (filters totals rows)
├── report.py                            # Claude report generation
├── data_validator.py                    # AI-powered data quality checks
├── chart_agent.py                       # Portfolio charts (risk, budget)
├── news_fetcher.py                      # Energy sector news aggregation
├── email_sender.py                      # Resend email with charts
├── requirements.txt                     # Dependencies
├── .env                                 # Environment variables (not in git)
├── data/
│   └── dena_IME_mock_dataset_v2.xlsx   # Portfolio data (25 projects)
├── langsmith_eval/
│   ├── dataset.py                       # LangSmith dataset creation
│   ├── target_function.py               # Report generation for eval
│   ├── run_eval.py                      # Evaluation runner
│   ├── evaluation_summary.md            # Eval results & recommendations
│   └── requirements_eval.txt            # Eval dependencies
├── README.md                            # This file
└── dena_report.log                      # Runtime logs (generated)
```

## Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create `.env` with these variables:

```bash
# Anthropic Claude API
ANTHROPIC_API_KEY=sk-ant-...

# Resend Email Service
RESEND_API_KEY=re_...

# Email Configuration
REPORT_SENDER_EMAIL=reports@dena.example.com
REPORT_RECIPIENT_EMAIL=leadership@dena.example.com

# Data File Path
DATA_FILE_PATH=data/dena_IME_mock_dataset_v2.xlsx

# NewsAPI for Energy Sector News
NEWS_API_KEY=... (get from https://newsapi.org/)

# LangSmith Evaluation (optional, for quality monitoring)
LANGCHAIN_API_KEY=lsv2_...
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://eu.api.smith.langchain.com
LANGCHAIN_PROJECT=dena-ime-portfolio-eval
```

### 4. Excel Data Format

Place Excel file in `data/dena_IME_mock_dataset_v2.xlsx`:

**Sheet:** `CONSOLIDATED DASHBOARD`

**Columns (A-L):**
1. Project ID
2. Project Name
3. Funder
4. Budget
5. Spend YTD
6. Budget %
7. HR Utilisation
8. Milestone Status
9. Overall Status (Green/Amber/Red)
10. Escalation (Yes/No)
11. Next Milestone
12. Key Risk

**Data rows:** Start at row 4 (rows 1-3 are titles/headers)  
**Stop at:** First empty Project ID  
**Note:** Totals rows are automatically filtered out

## Usage

### Test Locally (Run Report Now)

```bash
python main.py --now
```

This executes the full pipeline:
- ✓ Read 25 projects
- ✓ Validate data quality (AI checks)
- ✓ Generate report via Claude
- ✓ Create charts (risk & budget)
- ✓ Fetch news articles (scored by relevance)
- ✓ Send email with all components
- Exit

### Deploy (Production)

```bash
python main.py
```

Scheduler runs indefinitely, triggers every Monday at 08:00 UTC.

Use a process manager (PM2, systemd, supervisor) to run as background service.

### Deploy to Railway

1. Create Railway project
2. Connect Git repo
3. Set environment variables in Railway dashboard
4. Set start command: `python main.py`
5. Deploy

## Email Contents

The complete email includes:

| Component | Source | Purpose |
|-----------|--------|---------|
| **Escalation Banner** | project data | Warns if any Red projects need immediate action |
| **Data Quality Check** | Claude AI validator | Shows data completeness % and any issues |
| **Portfolio Dashboard** | chart_agent.py | Donut chart (Green/Amber/Red) + budget bar chart |
| **Executive Summary** | Claude report | Portfolio health, budget overview, red/amber/green count |
| **Immediate Actions** | Claude report | Only escalation-flagged projects with recommendations |
| **Projects at Risk** | Claude report | Amber-status projects and monitoring points |
| **On-Track Projects** | Claude report | Green projects with upcoming milestones |
| **Budget Overview** | Claude report | Total spend vs. budget, >90% utilization alerts |
| **Leadership Actions** | Claude report | Max 3 concrete, actionable recommendations |
| **Relevant News** | NewsAPI + scoring | Last 7 days energy sector articles, sorted by relevance (★ score) |

**Length:** ~2000 words  
**Format:** HTML with responsive design  
**Attachments:** 2 PNG charts (risk_chart.png, budget_chart.png)

## Pipeline Steps

```
Step 1: Read Data
  └─ Load 26 rows, filter totals row → 25 projects

Step 1b: Data Validation
  └─ Claude AI checks completeness, plausibility, status validity
  └─ Report: % complete, warnings, anomalies

Step 2: Generate Report
  └─ Claude analyzes portfolio, generates structured JSON
  └─ Extracts: summary, actions, risks, milestones, budget flags

Step 2b: Generate Charts
  └─ Risk status donut (Green/Amber/Red distribution)
  └─ Budget utilization bars (sorted by %, color-coded)
  └─ Saved as PNG, encoded to base64 for email

Step 2c: Fetch News
  └─ NewsAPI searches 6 keywords (Energiewende, Wasserstoff, etc.)
  └─ Scores by relevance (counts German energy keywords)
  └─ Max 10 articles, sorted by score descending

Step 3: Send Email
  └─ Build HTML from all components
  └─ Attach PNG charts with cid: references
  └─ Resend via Resend API
  └─ Log success/failure
```

## Data Quality Validation

The data validator (Claude AI) checks for:

- **Completeness:** Missing project_id, project_name, budget, spend_ytd, overall_status
- **Plausibility:** Overspend (spend > budget), negative values, budget_pct consistency
- **Status validity:** Overall_status in [Green, Amber, Red], escalation flag consistency
- **Anomalies:** Budget outliers (>3x average), utilization >150% or <10%, zero spend with advanced milestones

Returns:
- `passed`: true if ≥80% completeness and no high-severity issues
- `data_completeness_pct`: 0-100
- `warnings`: List of issues with severity (low/medium/high)
- `anomalies`: List of suspicious patterns

## News Fetching

NewsAPI integration fetches German-language articles from last 7 days:

**Search keywords:**
- Energiewende
- Energieeffizienz
- Wärmepumpe Gebäudesanierung
- Elektromobilität
- dena Deutsche Energie-Agentur
- Wasserstoff Energie

**Relevance scoring:**
Counts matches of energy sector keywords in title + description:
- energiewende, wasserstoff, photovoltaik, elektromobilität, wärmepumpe, etc.

**Display:**
- Sorted by score (highest first)
- Shows relevance badge (★ 0-18)
- Includes source, publication date, description (120 chars max)
- Clickable links to full articles

## LangSmith Evaluation

For continuous improvement, reports can be evaluated using LangSmith:

```bash
cd langsmith_eval
python dataset.py          # Create evaluation dataset (12 projects)
python target_function.py  # Test report generation
python run_eval.py         # Run evaluation suite
```

See `langsmith_eval/evaluation_summary.md` for latest results.

## Logging

All events logged to console and `dena_report.log`:
- Report execution start/end
- Data validation results
- Chart generation
- News fetch count
- API calls (status, tokens, latency)
- Email delivery status
- Errors with full traceback

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Excel file not found | Logs error, sends fallback email |
| Data validation fails | Continues with warnings (doesn't block) |
| Claude API fails | Logs error, sends fallback email |
| Chart generation fails | Continues without charts (graceful degrade) |
| News fetch fails | Continues without news section (graceful degrade) |
| Email send fails | Logs error only (report was generated) |

## Troubleshooting

### "Data validation failed — proceeding with warnings"
- Check data in Excel for completeness
- Verify all projects have overall_status (Green/Amber/Red)
- Check for budget values >3x average (might be outliers)

### "No news articles fetched"
- Verify `NEWS_API_KEY` is correct
- Check NewsAPI account status at newsapi.org
- Ensure network connectivity

### "Charts not attached to email"
- Check that chart generation logged "...generated successfully"
- Verify matplotlib can write to `/tmp` or local directory
- Check email log for base64 encoding errors

### "Scheduler not triggering"
- Verify process is running: `ps aux | grep main.py`
- Check system time and timezone
- Review `dena_report.log` for errors

## Development

### Modifying the Report Prompt

Edit `SYSTEM_PROMPT` in `report.py` to change analysis structure, tone, or focus.

### Changing the Schedule

Modify `CronTrigger` in `main.py`:

```python
# Current: Every Monday at 08:00
trigger=CronTrigger(day_of_week="mon", hour=8, minute=0)

# Every day at 09:00
trigger=CronTrigger(hour=9, minute=0)

# Every Friday at 17:00
trigger=CronTrigger(day_of_week="fri", hour=17, minute=0)
```

See [APScheduler CronTrigger docs](https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html).

### Testing Individual Modules

```bash
# Test data validation
python data_validator.py

# Test chart generation
python chart_agent.py

# Test news fetching
python news_fetcher.py

# Test report generation
python report.py
```

## Performance

**Typical run time:** 50-60 seconds
- Data read: ~1s
- Data validation (Claude): ~17s
- Report generation (Claude): ~31s
- Chart generation: ~1s
- News fetching: ~1s
- Email send: ~1s

**Email size:** ~2-3 MB (charts as PNG attachments)

## Security Notes

- ✅ All API keys in `.env`, never hardcoded
- ✅ `.env` in `.gitignore` (not committed)
- ✅ Logs written to disk for audit trail
- ✅ No sensitive data in email subjects
- ✅ Charts attached securely (no public URLs)
- ✅ News links open in new browser tab (security policy)

## License

Internal dena project. All rights reserved.
