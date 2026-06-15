# dena IME Weekly Report Automation

Automated weekly portfolio status report generation using Claude AI and email delivery via Resend.

## Overview

This project automatically:
1. Reads project portfolio data from a local Excel file (`.xlsx`)
2. Sends data to the Claude API for intelligent analysis
3. Generates a structured weekly status report
4. Delivers the report as a formatted HTML email

**Schedule:** Every Monday at 08:00 UTC

## Tech Stack

- **APScheduler** — Scheduled execution
- **openpyxl** — Local Excel file reading
- **anthropic** — Claude API integration
- **resend** — Email delivery
- **python-dotenv** — Environment variable management

## Project Structure

```
dena-report/
├── main.py                                    # Scheduler entry point
├── reader.py                                  # Excel file reader
├── report.py                                  # Claude API integration
├── email_sender.py                            # Resend email delivery
├── data/
│   └── dena_IME_mock_dataset_v2.xlsx         # Local mock data file
├── .env                                       # Environment variables (not in git)
├── requirements.txt                           # Python dependencies
├── README.md                                  # This file
└── dena_report.log                           # Log file (generated)
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

Copy `.env` and fill in your credentials:

```bash
# Anthropic Claude API key
ANTHROPIC_API_KEY=sk-ant-...

# Resend API key
RESEND_API_KEY=re_...

# Email configuration
REPORT_SENDER_EMAIL=reports@dena.example.com
REPORT_RECIPIENT_EMAIL=leadership@dena.example.com

# Data file path
DATA_FILE_PATH=data/dena_IME_mock_dataset_v2.xlsx
```

### 4. Place Excel Data File

Add your Excel file to the `data/` folder:
- File format: `.xlsx`
- Sheet name: `CONSOLIDATED DASHBOARD`
- Columns: A-L (Project ID through Key Risk)
- Data starts: Row 4 (rows 1-3 are headers/titles)
- Stop reading: At first empty Project ID (column A)

Expected columns:
1. Project ID
2. Project Name
3. Funder
4. Budget
5. Spend YTD
6. Budget %
7. HR Utilisation
8. Milestone Status
9. Overall Status
10. Escalation (Yes/No)
11. Next Milestone
12. Key Risk

## Usage

### Test Locally

Run the report immediately without waiting for the scheduler:

```bash
python main.py --now
```

This will:
- Read the Excel file
- Call Claude API for analysis
- Send the email
- Exit

### Deploy (Production)

Start the scheduler (runs indefinitely):

```bash
python main.py
```

The scheduler will wake up every Monday at 08:00 and execute the report.

To run as a background service, use a process manager (PM2, systemd, supervisor, etc.).

### Deploy to Railway

1. Create a new Railway project
2. Connect your Git repository
3. Set environment variables in Railway dashboard:
   - `ANTHROPIC_API_KEY`
   - `RESEND_API_KEY`
   - `REPORT_SENDER_EMAIL`
   - `REPORT_RECIPIENT_EMAIL`
   - `DATA_FILE_PATH`
4. Set start command: `python main.py`
5. Deploy

Railway will keep the process running and handle restarts.

## Logging

All events are logged to both console and `dena_report.log`:
- Report execution start/end
- Data rows read from Excel
- API calls (success/failure)
- Email delivery status
- Error details

## Error Handling

The system handles these failure scenarios gracefully:

| Scenario | Behavior |
|----------|----------|
| Excel file not found | Logs error, sends fallback email with file path |
| Empty portfolio (0 rows) | Aborts, no report sent, logs warning |
| Claude API fails | Logs error, sends fallback email with error details |
| Resend fails | Logs error only (report was generated, just not sent) |

## Report Structure

The Claude-generated report includes:

1. **Executive Summary** — Portfolio health, budget overview, red/amber/green count
2. **Immediate Actions Required** — Only escalation-flagged projects with recommendations
3. **Projects at Risk** — Amber-status projects and what to monitor
4. **On-Track Projects** — Confirmed green projects with upcoming milestones
5. **Budget Overview** — Total spend vs. budget, >90% consumed alerts
6. **Leadership Actions** — Max 3 concrete, actionable recommendations

**Tone:** Professional, concise, decision-oriented for non-technical division heads  
**Length:** Max 700 words  
**Format:** Plain text with clear section headers

## Email Template

The report is delivered as an HTML email with:
- Clean, professional header
- Escalation warning banner (if any red projects)
- Report body in monospace font for readability
- Footer with disclaimer
- Responsive design for mobile

## Security Notes

- ✅ API keys loaded from `.env`, never hardcoded
- ✅ `.env` should be in `.gitignore` (not committed to git)
- ✅ Logs are written to disk for audit trail
- ✅ No sensitive data in email subject lines

## Troubleshooting

### "Data file not found"
- Check `DATA_FILE_PATH` in `.env`
- Ensure the Excel file exists at that path
- Verify the sheet name is exactly `CONSOLIDATED DASHBOARD`

### "Claude API call failed"
- Verify `ANTHROPIC_API_KEY` is correct
- Check rate limits and quota at console.anthropic.com
- Ensure network connectivity

### "Email send failed"
- Verify `RESEND_API_KEY` is correct
- Check sender/recipient email addresses are valid
- Ensure Resend account is active

### "Scheduler not triggering"
- Verify the process is still running: `ps aux | grep main.py`
- Check system time is correct
- Review logs for errors: `tail -f dena_report.log`

## Development

### Local Testing with Mock Data

Create a test Excel file in `data/dena_IME_mock_dataset_v2.xlsx` with sample projects, then run:

```bash
python main.py --now
```

### Modifying the Report Prompt

Edit the `SYSTEM_PROMPT` variable in `report.py` to change the analysis structure, tone, or focus.

### Changing the Schedule

Modify the `CronTrigger` in `main.py`:

```python
# Currently: Every Monday at 08:00
trigger=CronTrigger(day_of_week="mon", hour=8, minute=0)

# Example: Every day at 09:00
trigger=CronTrigger(hour=9, minute=0)

# Example: Every Friday at 17:00
trigger=CronTrigger(day_of_week="fri", hour=17, minute=0)
```

See [APScheduler CronTrigger docs](https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html) for full syntax.

## License

Internal dena project.
