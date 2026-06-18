# Use Case Definition: AI-Powered Portfolio Reporting System
## dena IME Weekly Status Reports

**Document Version:** 1.1
**Date:** June 2026
**Project:** dena IME Weekly Report Automation
**Status:** Deployed — Pilot Phase

---

## 1. Company Profile

### Organization

**dena** (Deutsche Energie-Agentur / German Energy Agency) is a federal institution supporting Germany's energy transition. As a publicly mandated agency under the Federal Ministry for Economic Affairs and Climate Action, dena plays a critical role in accelerating decarbonization and sustainable energy systems across Germany.

**Organization Size:** ~350 employees across multiple divisions
**Headquarters:** Berlin, Germany
**Mandate:** Policy implementation, market development, and portfolio management for energy transition initiatives

### IME Division (Industrie, Mobilität, Energieeffizienz)

The **IME Division** (Industry, Mobility & Energy Efficiency) manages dena's domestic energy transition portfolio across industrial decarbonization, mobility transition, and energy efficiency programmes.

- **Team Size:** ~100 full-time staff (project managers, analysts, finance coordinators, domain experts)
- **Budget Responsibility:** [ASSUMPTION] €50–100M portfolio across 26 active energy transition projects
- **Key Functions:**
  - Strategic project portfolio management
  - Stakeholder coordination (Federal Ministry, industry partners, municipalities)
  - Progress tracking and risk assessment across project portfolio
  - Budget and resource allocation oversight
  - Executive reporting to Federal Ministry leadership

---

## 2. Business Problem

### Current State: Manual Portfolio Reporting

The IME Division currently generates weekly portfolio status reports through a **manual, labor-intensive process**:

#### Process Inefficiencies

1. **Time Consumption**
   - Data compilation from Excel spreadsheets: [ASSUMPTION] 3–4 hours/week
   - Manual analysis and interpretation: [ASSUMPTION] 2–3 hours/week
   - Report writing and formatting: [ASSUMPTION] 1–2 hours/week
   - Email distribution and follow-up: [ASSUMPTION] 30 minutes/week
   - **Total weekly effort: [ASSUMPTION] ~7–10 hours per analyst**

2. **Information Gaps**
   - No automated early warning system for at-risk projects
   - Correlation between budget health and milestone delivery often missed
   - Escalation flags identified ad-hoc, not systematically
   - Leadership recommendations generated from intuition rather than data-driven analysis

3. **Quality & Consistency Issues**
   - Report structure and depth vary week-to-week depending on analyst
   - No standardized risk assessment framework
   - Important metrics occasionally overlooked
   - Tone and focus inconsistent across reporting cycles

4. **Stakeholder Friction**
   - Leadership receives inconsistent insight into portfolio health
   - Project managers wait for manual feedback instead of structured updates
   - Finance cannot validate budget burn rates efficiently
   - No audit trail of how recommendations were derived

### Business Impact

- **Inefficient resource allocation:** Analyst time spent on data wrangling rather than strategic thinking
- **Delayed decision-making:** Information asymmetry prevents proactive intervention
- **Risk blind spots:** Early warning signals for project failure are missed or delayed
- **Scaling constraints:** Manual process breaks down as portfolio grows beyond 26 projects

---

## 3. AI-Powered Solution

### Solution Overview

An **automated, Claude AI-powered portfolio reporting system** that reads Excel project data, generates intelligent analysis, and delivers structured HTML email reports every Monday at 08:00 UTC.

The system follows the **Agentic AI pattern**: it plans (APScheduler defines the weekly trigger), acts (reads Excel data and calls the Claude API for analysis), observes (logs outcomes, handles errors, validates outputs), and iterates (runs autonomously each week, with prompt refinement between cycles). This distinguishes it from a simple script — the system is a goal-directed loop with error recovery and human oversight built in.

### System Architecture

#### Components

1. **Data Ingestion** (`openpyxl`)
   - Reads local Excel file: `dena_IME_mock_dataset_v2.xlsx`
   - Extracts project data from sheet: `CONSOLIDATED DASHBOARD`
   - Columns captured: Project ID, Name, Funder, Budget, Spend YTD, Budget %, HR Utilization, Milestone Status, Overall Status, Escalation Flag, Next Milestone, Key Risk
   - Stops at first empty Project ID (column A)

2. **Intelligent Analysis** (Claude API — Sonnet)
   - Sends structured project dataset to Claude AI
   - Generates contextual analysis using:
     - Budget burn rate calculations
     - Risk correlation analysis
     - Milestone vs. budget alignment checks
     - Escalation impact assessment
   - Returns structured JSON output for reliable downstream processing
   - `max_tokens` set to 2,500 to prevent silent response truncation

3. **Report Generation**
   - Structured sections: Executive Summary, Actions Required, Risk Analysis, Budget Overview, Leadership Recommendations
   - Tone: Professional, concise, decision-oriented
   - Includes mandatory "Limitations" note: AI analysis is decision support, not a decision maker
   - Format: Structured JSON → rendered HTML

4. **Delivery** (Resend)
   - HTML email template with professional branding
   - Escalation warning banner if red-flagged projects exist
   - Responsive design for mobile and desktop
   - Audit disclaimer footer on every report

5. **Human-in-the-Loop (mandatory design decision)**
   - PM reviews every report before distribution — approximately 1 hour/week
   - This is not optional overhead: it is the primary control for catching LLM errors and satisfying EU AI Act human oversight requirements
   - See Risk 2.1 and Compliance Documentation for detail

6. **Orchestration** (APScheduler)
   - Cron-based scheduling: Every Monday at 08:00 UTC
   - Graceful error handling with fallback notifications
   - All events logged to `dena_report.log` for audit

#### Data Flow

```
Excel File → Reader (openpyxl) → Claude API (JSON) → Report Generator → Human Review → Email Sender (Resend) → Leadership
```

#### Deployment

- **Development:** Local testing with `--now` flag
- **Production:** Railway.app continuous process (keeps scheduler running 24/7)
- **Environment Management:** `.env` file for API keys and config (no hardcoded credentials)

### Error Handling

| Failure Scenario | Behaviour |
|---|---|
| Excel file not found | Log error, send fallback email with path info |
| Empty portfolio (0 rows) | Abort, no report sent, log warning |
| Claude API fails | Log error, send fallback email with error details |
| JSON parsing fails (truncated response) | Log raw API response, retry with increased `max_tokens` |
| Resend email fails | Log error, report still generated locally |

---

## 4. Key Stakeholders and Their Interests

### 4.1 IME Division Head (Bereichsleitung IME)

**Role:** Portfolio governance, strategic oversight, Federal Ministry liaison

**Interests:**
- Early visibility into at-risk projects before they escalate
- Data-driven evidence for funding and resource decisions
- Consistent, structured briefing material for Federal Ministry reports
- Ability to identify patterns across 26 projects at a glance
- Time savings to focus on strategic priorities rather than data compilation

**Pain Points Addressed:**
- Currently receives inconsistent weekly summaries with varying depth
- Lacks systematic early warning for project failures
- Spends time chasing analysts for additional clarification

---

### 4.2 Themengebietsleitung Bereichsentwicklung und -controlling

**Role:** Division development, controlling, portfolio operations oversight

**Interests:**
- Standardized KPI framework across all 26 projects
- Automated budget health tracking replacing manual controlling cycles
- Audit trail for internal governance and Federal Ministry accountability
- Scalable reporting infrastructure as portfolio grows

**Pain Points Addressed:**
- Manual controlling process consumes significant analyst time
- No systematic link between project status and budget burn in current reports
- Difficulty maintaining consistent reporting standards across project managers

---

### 4.3 Project Managers (26 projects)

**Role:** Day-to-day project execution, milestone tracking, budget management

**Interests:**
- Objective, data-driven risk assessment of their projects
- Rapid, structured feedback on status and escalation triggers
- Recognition of on-track projects, not only flagging of problems
- Understanding of their project's position relative to portfolio trends

**Pain Points Addressed:**
- Manual reporting creates perception of subjective bias
- Lack of real-time performance data
- Difficulty contextualising individual project against full portfolio

---

### 4.4 Finance Team

**Role:** Budget allocation, spend tracking, financial forecasting

**Interests:**
- Automated budget health tracking across portfolio
- Early alerts for projects exceeding 90% budget consumption
- Structured data for financial planning and forecasting
- Audit trail linking recommendations to actual spend data

**Pain Points Addressed:**
- Budget data not integrated into portfolio narrative
- Manual correlation between spend and project status
- No systematic flag for over-budget projects before crisis point

---

### 4.5 IT / Operations Team

**Role:** System deployment, uptime management, security compliance

**Interests:**
- Reliable, low-maintenance system (scheduler handles itself)
- Secure API key management via `.env`
- Audit logging for compliance (all events logged to disk)
- Scalable infrastructure with auto-restart capability

**Pain Points Addressed:**
- Minimal operational overhead (cron-based, no manual intervention)
- Secure credential handling (not hardcoded)
- Built-in logging for compliance audits

---

### 4.6 Legal / Compliance

**Role:** Data protection, regulatory compliance, risk management

**Interests:**
- No sensitive data exposure in email subjects or logs
- Audit trail of how recommendations were generated
- GDPR compliance for any personal data processed
- Clear process documentation for regulators

**Pain Points Addressed:**
- Transparent, logged process (all events recorded)
- No raw API keys in logs
- Clear data flow and retention policy documented in GDPR section

---

## 5. Success Criteria & Measurable KPIs

### 5.1 Operational Success Criteria

| Criterion | Target | How Measured |
|---|---|---|
| Report Delivery Uptime | 99.5% (max 1 missed report/year) | Railway logs; incident count |
| Report Generation Time | <2 minutes end-to-end | Logged timestamps in `dena_report.log` |
| Email Delivery Success | 100% of generated reports sent | Resend API response logs |
| Data Accuracy | 100% row match between Excel and analysis | Row count validation in logs |
| Schedule Reliability | Report sent every Monday at 08:00 UTC | Consistent timestamp in logs |

---

### 5.2 Business Impact KPIs

| Metric | Baseline | Target | Timeline | Measurement |
|---|---|---|---|---|
| Analyst Time Savings | 7–10 hrs/week | <1 hr/week (review only) | Week 1 | Weekly time tracking (before/after) |
| Time to Risk Detection | 3–5 days (manual review) | Same day (Monday report) | Week 2 | Track automated vs. missed escalations |
| Early Warning Effectiveness | TBD (establish baseline) | 80% of red projects flagged before crisis | Month 1–3 | Count early escalations vs. surprises |
| Leadership Decision Turnaround | 2–3 days (awaiting clarification) | <24 hours | Week 2 | Decision log timestamps post-report |
| Report Consistency Score | [ASSUMPTION] 60% (analyst variation) | 95%+ (standardised AI analysis) | Week 1 | Stakeholder feedback: consistency rating (1–10) |

> **Note on financial impact:** Full ROI calculation, cost-benefit analysis, and financial assumptions are documented in `02_roi_risk_assessment.md`. The conservative annual benefit estimate is **€6,390/year** (direct savings), with a break-even of **Q4 Year 1** under realistic base-case assumptions (1.5 hrs/week saved at €45/hr).

---

### 5.3 Stakeholder Satisfaction KPIs

**Measurement method:** Quarterly survey (0–10 scale)

| Stakeholder | Success Statement | Target Score |
|---|---|---|
| IME Division Head | "I have better visibility into at-risk projects" | 8/10 |
| IME Division Head | "The report structure helps me brief the Federal Ministry" | 8/10 |
| Project Managers | "The risk assessment is fair and data-driven" | 8/10 |
| Finance | "Budget metrics are clearly integrated into recommendations" | 8/10 |
| All Users | "This system saves me time and improves decision-making" | 8/10 |

---

### 5.4 Quality & Reliability KPIs

| Criterion | Target | Measurement |
|---|---|---|
| Fallback Email Rate | <1% of reports trigger fallback | Fallback count / total reports |
| Claude API Success Rate | 99%+ | Successful analyses / total attempted |
| Log Completeness | 100% of events logged | Manual log audit |
| Error Recovery | System self-recovers from transient failures | Monitor: retry behaviour, Railway restarts |
| Data Integrity | No row loss or duplication | Row count validation before/after analysis |
| Human Review Completion | 100% of reports reviewed before distribution | PM sign-off log |

---

## 6. Assumptions & Dependencies

### Explicit Assumptions

- [ASSUMPTION] Budget authority, and time consumption rates not verified against dena internal data — estimates based on comparable portfolio management organisations
- [ASSUMPTION] Stakeholder interests extrapolated from typical public-sector portfolio governance models
- [ASSUMPTION] KPI targets based on industry benchmarks for similar reporting automation initiatives
- [ASSUMPTION] Financial benefits estimated conservatively; see `02_roi_risk_assessment.md` for full model

### Technical Dependencies

- Excel file remains the authoritative source of project data (no cross-sheet formula references in the consolidated tab)
- Claude API available and reliable for weekly analysis (Anthropic SLA)
- Resend email service operational and EU-compliant
- Railway.app continues to support 24/7 Python process hosting
- Stable internet connectivity for API calls from Railway

### Organisational Dependencies

- Federal Ministry continues requiring weekly portfolio reports
- Report format (email, HTML) acceptable to stakeholders
- No major organisational restructuring affects IME Division reporting requirements
- Legal/compliance environment (GDPR, IT-Sicherheitsgesetz, audit requirements) remains stable

---

## 7. Implementation Status & Next Steps

### Implementation Phase (Complete)

- System built, tested, and deployed to Railway
- Structured JSON output from Claude API validated
- Email delivery via Resend confirmed
- Logging and error handling validated
- `max_tokens` bug resolved (increased to 2,500; raw API response logging added)

### Pilot Phase (Weeks 1–4)

- Track schedule reliability (Monday 08:00 consistency)
- Monitor email delivery success rate
- Validate time-savings assumption via PM time tracking
- Collect initial stakeholder feedback on report quality and format

### Optimisation Phase (Month 1–3)

- Gather KPI baseline measurements
- Refine Claude prompt based on stakeholder feedback
- Adjust report sections or escalation thresholds as needed
- Conduct bias audit: review recommendations for unexplained variance by project type

### Success Review (Month 3)

- Full KPI assessment against targets in Section 5
- Stakeholder satisfaction survey
- Cost-benefit validation against ROI model
- Decision: extend pilot, expand portfolio scope, or adjust system design

---

*Version 1.1 · Prepared June 2026 · System Status: Deployed — Pilot Phase · Next Review: September 2026*
