# Use Case Definition: AI-Powered Portfolio Reporting System
## dena IME Weekly Status Reports

**Document Version:** 1.0  
**Date:** June 2026  
**Project:** dena IME Weekly Report Automation  
**Status:** Implementation Complete

---

## 1. Company Profile

### Organization
**dena** (Deutsche Energie-Agentur / German Energy Agency) is a federal institution supporting Germany's energy transition. As a publicly mandated agency under the Federal Ministry for Economic Affairs and Climate Action, dena plays a critical role in accelerating decarbonization and sustainable energy systems across Germany.

**Organization Size:** ~350 employees across multiple divisions  
**Headquarters:** Berlin, Germany  
**Mandate:** Policy implementation, market development, and portfolio management for energy transition initiatives

### IME Division (International and Emerging Markets)
The **IME Division** (International & Emerging Markets) manages dena's international energy transition portfolio and emerging market expansion projects.

- **Team Size:** [ASSUMPTION] ~30-40 full-time staff (project managers, analysts, finance coordinators)
- **Budget Responsibility:** [ASSUMPTION] €50-100M portfolio across 26 active energy transition projects
- **Key Functions:**
  - Strategic project portfolio management
  - Stakeholder coordination (government, international partners, private sector)
  - Progress tracking and risk assessment
  - Budget and resource allocation oversight
  - Executive reporting to Federal Ministry leadership

---

## 2. Business Problem

### Current State: Manual Portfolio Reporting
The IME Division currently generates weekly portfolio status reports through a **manual, labor-intensive process**:

#### Process Inefficiencies
1. **Time Consumption**
   - Data compilation from Excel spreadsheets: [ASSUMPTION] 3-4 hours/week
   - Manual analysis and interpretation: [ASSUMPTION] 2-3 hours/week
   - Report writing and formatting: [ASSUMPTION] 1-2 hours/week
   - Email distribution and follow-up: [ASSUMPTION] 30 minutes/week
   - **Total weekly effort:** [ASSUMPTION] ~7-10 hours per analyst

2. **Information Gaps**
   - No automated early warning system for at-risk projects
   - Correlation between budget health and milestone delivery often missed
   - Escalation flags identified ad-hoc, not systematically
   - Leadership recommendations generated from intuition rather than data-driven analysis

3. **Quality & Consistency Issues**
   - Report structure and depth vary week-to-week
   - No standardized risk assessment framework
   - Important metrics occasionally overlooked
   - Tone and focus inconsistent across reports

4. **Stakeholder Friction**
   - Leadership receives inconsistent insight into portfolio health
   - Project managers wait for manual feedback instead of real-time dashboards
   - Finance can't validate budget burn rates efficiently
   - No audit trail of how recommendations were derived

### Business Impact
- **Inefficient resource allocation:** Analyst time spent on data wrangling vs. strategic thinking
- **Delayed decision-making:** Information asymmetry prevents proactive intervention
- **Risk blind spots:** Early warning signals for project failure missed
- **Scaling constraints:** Manual process breaks down as portfolio grows beyond 26 projects

---

## 3. AI-Powered Solution Proposed

### Solution Overview
An **automated, Claude AI-powered portfolio reporting system** that reads Excel project data, generates intelligent analysis, and delivers structured HTML email reports every Monday at 08:00 UTC.

### System Architecture

#### Components
1. **Data Ingestion** (openpyxl)
   - Reads local Excel file: `dena_IME_mock_dataset_v2.xlsx`
   - Extracts project data from sheet: `CONSOLIDATED DASHBOARD`
   - Columns captured: Project ID, Name, Funder, Budget, Spend YTD, Budget %, HR Utilization, Milestone Status, Overall Status, Escalation Flag, Next Milestone, Key Risk
   - Stops at first empty Project ID (column A)

2. **Intelligent Analysis** (Claude API)
   - Sends structured project dataset to Claude AI
   - Generates contextual analysis using:
     - Budget burn rate calculations
     - Risk correlation analysis
     - Milestone vs. budget alignment checks
     - Escalation impact assessment
   - Produces recommendations grounded in data patterns

3. **Report Generation**
   - Structured sections (Executive Summary, Actions Required, Risk Analysis, Budget Overview, Leadership Recommendations)
   - Tone: Professional, concise, decision-oriented
   - Length: Max 700 words
   - Format: Plain text with clear headers

4. **Delivery** (Resend)
   - HTML email template with professional branding
   - Escalation warning banner (if red-flagged projects exist)
   - Responsive design for mobile/desktop
   - Monospace font for data readability
   - Audit disclaimer footer

5. **Orchestration** (APScheduler)
   - Cron-based scheduling: Every Monday at 08:00 UTC
   - Configurable for other frequencies if needed
   - Graceful error handling with fallback notifications

#### Data Flow
```
Excel File → Reader → Claude API → Report Generator → Email Sender → Leadership
```

#### Deployment
- **Development:** Local testing with `--now` flag
- **Production:** Railway.app continuous process (keeps scheduler running 24/7)
- **Environment Management:** `.env` file for API keys and config

### Error Handling
| Failure Scenario | Behavior |
|---|---|
| Excel file not found | Log error, send fallback email with path info |
| Empty portfolio (0 rows) | Abort, no report sent, log warning |
| Claude API fails | Log error, send fallback email with error details |
| Resend email fails | Log error, report still generated locally |

---

## 4. Key Stakeholders and Their Interests

### 4.1 IME Division Head
**Role:** Portfolio governance, strategic oversight, Federal Ministry liaison

**Interests:**
- ✅ Early visibility into at-risk projects before they escalate
- ✅ Data-driven evidence for funding decisions
- ✅ Consistent, structured briefing for Federal Ministry reports
- ✅ Ability to identify patterns across 26 projects at a glance
- ✅ Time savings to focus on strategic priorities

**Pain Points (Addressed by Solution):**
- Currently receives inconsistent weekly summaries
- Lacks early warning system for project failures
- Spends time chasing analysts for additional analysis

---

### 4.2 Project Managers (26 projects)
**Role:** Day-to-day project execution, milestone tracking, budget management

**Interests:**
- ✅ Objective, fair risk assessment of their projects
- ✅ Rapid feedback on status and escalation triggers
- ✅ Data-driven recommendations, not subjective criticism
- ✅ Recognition of on-track projects and wins
- ✅ Understanding of budget burn rate trends

**Pain Points (Addressed by Solution):**
- Manual reporting creates perception of bias
- Lack of real-time performance data
- Difficulty contextualizing their project against portfolio trends

---

### 4.3 Finance Team
**Role:** Budget allocation, spend tracking, financial forecasting

**Interests:**
- ✅ Automated budget health tracking across portfolio
- ✅ Early alerts for >90% budget consumption
- ✅ Structured data for financial planning and forecasting
- ✅ Audit trail linking recommendations to actual spend data
- ✅ Validation that analysis includes financial metrics

**Pain Points (Addressed by Solution):**
- Budget data not integrated into portfolio narrative
- Manual correlation between spend and project status difficult
- No systematic flag for over-budget projects

---

### 4.4 IT / Operations Team
**Role:** System deployment, uptime management, security compliance

**Interests:**
- ✅ Reliable, low-maintenance system (scheduler handles itself)
- ✅ Clear API key management and `.env` security
- ✅ Audit logging for compliance (all events logged to disk)
- ✅ Scalable infrastructure (Railway handles auto-restart)
- ✅ No sensitive data in logs or email subjects

**Pain Points (Addressed by Solution):**
- Minimal operational overhead (cron-based, not manual intervention)
- Secure credential handling (not hardcoded)
- Built-in logging for compliance audits

---

### 4.5 Legal / Compliance
**Role:** Data protection, regulatory compliance, risk management

**Interests:**
- ✅ No sensitive data exposure in email subjects or logs
- ✅ Audit trail of who generated recommendations
- ✅ Compliance with German data protection (GDPR) requirements
- ✅ Clear process documentation for regulators
- ✅ Error logging for accountability

**Pain Points (Addressed by Solution):**
- Transparent, logged process (all events recorded)
- No raw API keys in logs
- Clear data flow and retention policy

---

## 5. Success Criteria & Measurable KPIs

### 5.1 Operational Success Criteria

| Criterion | Target | How Measured |
|-----------|--------|--------------|
| **Report Delivery Uptime** | 99.5% (1 missed report/year max) | Monitoring Railway logs; incident count |
| **Report Generation Time** | <2 minutes end-to-end | Logged timestamps in dena_report.log |
| **Email Delivery Success** | 100% of generated reports sent | Resend API response logs |
| **Data Accuracy** | 100% row match between Excel and analysis | Row count validation in logs |
| **Schedule Reliability** | Report sent every Monday at 08:00 UTC | Consistent timestamp in logs |

### 5.2 Business Impact KPIs

| Metric | Baseline | Target | Timeline | Measurement |
|--------|----------|--------|----------|-------------|
| **Analyst Time Savings** | 7-10 hours/week | <1 hour/week (email review only) | Week 1 | Weekly time tracking (before/after) |
| **Time to Risk Detection** | 3-5 days (manual review) | Same day (automated Monday report) | Week 2 | Track project escalations: automated vs. missed |
| **Early Warning Effectiveness** | TBD (baseline) | 80% of "red" projects flagged before crisis | Month 1-3 | Count projects with early escalation vs. surprises |
| **Leadership Decision Turnaround** | 2-3 days (awaiting analyst clarification) | <24 hours (report-driven decisions) | Week 2 | Track decision logs post-report delivery |
| **Report Consistency Score** | 60% (analyst-to-analyst variation) | 95%+ (standardized AI analysis) | Week 1 | Stakeholder feedback: consistency rating (1-10) |
| **Data-Driven Recommendations** | [ASSUMPTION] 40% of actions rooted in data | 90%+ recommendations traceable to metrics | Month 1 | Audit trail: link recommendations → data points |

### 5.3 Stakeholder Satisfaction KPIs

**Measurement Method:** Quarterly survey (0-10 scale, "Strongly Disagree" to "Strongly Agree")

| Stakeholder | Success Statement | Target Score | Baseline |
|-------------|------------------|--------------|----------|
| **IME Division Head** | "I have better visibility into at-risk projects" | 8/10 | TBD |
| **IME Division Head** | "The report structure helps me brief the Federal Ministry" | 8/10 | TBD |
| **Project Managers** | "The risk assessment is fair and data-driven" | 8/10 | TBD |
| **Finance** | "Budget metrics are clearly integrated into recommendations" | 8/10 | TBD |
| **All Users** | "Overall, this system saves me time and improves decision-making" | 8/10 | TBD |

### 5.4 Quality & Reliability KPIs

| Criterion | Target | Measurement |
|-----------|--------|-------------|
| **Fallback Email Delivery** | <1% of reports generate fallbacks | Fallback count / total reports |
| **Claude API Success Rate** | 99%+ (rate limit/error handling) | Successful analyses / total attempted |
| **Log Completeness** | 100% of events logged (start, success, failure, email sent) | Manual log audit |
| **Error Recovery** | System self-recovers from transient failures | Monitor: API retry behavior, Railway restarts |
| **Data Integrity** | No row loss or duplication between Excel read and analysis | Row count validation before/after |

### 5.5 Financial Impact (Optional)

| Benefit | Estimated Value | Calculation |
|---------|-----------------|-------------|
| **Analyst Time Savings** | [ASSUMPTION] €15,000/year | 6-9 hrs/week × 50 weeks × €30/hr |
| **Faster Decision-Making** | [ASSUMPTION] €50,000-100,000/year | Reduce project crisis costs via early warnings (assumes 1-2 prevented escalations) |
| **Scalability Headroom** | [ASSUMPTION] €200,000+/year | Enable portfolio growth from 26 to 50+ projects without proportional staffing increase |

---

## 6. Assumptions & Dependencies

### Explicit Assumptions (Marked Throughout)
- [ASSUMPTION] Team size, budget authority, and time consumption rates (not verified with dena)
- [ASSUMPTION] Stakeholder interests extrapolated from typical portfolio governance models
- [ASSUMPTION] KPI targets based on industry benchmarks for similar automation initiatives
- [ASSUMPTION] Financial benefits estimated conservatively

### Technical Assumptions
- Excel file remains the authoritative source of project data
- Claude API is available and reliable for weekly analysis
- Resend email service remains operational and compliant
- Railway.app continues to support 24/7 Python process hosting
- System has stable internet connectivity for API calls

### Organizational Assumptions
- Federal Ministry will continue requiring weekly portfolio reports
- Report format (email, HTML) is acceptable to stakeholders
- No major organizational restructuring affects IME Division reporting requirements
- Legal/compliance environment (GDPR, audit requirements) remains stable

---

## 7. Next Steps & Success Handoff

### Implementation Phase (Complete)
- ✅ System built, tested, and deployed to Railway
- ✅ First reports generated and delivered
- ✅ Logging and error handling validated

### Monitoring Phase (Week 1-2)
- Track schedule reliability (Monday 08:00 consistency)
- Monitor email delivery success rate
- Collect initial stakeholder feedback
- Validate data accuracy (row counts, metrics)

### Optimization Phase (Month 1-3)
- Gather KPI baseline measurements
- Refine Claude prompt based on stakeholder feedback
- Adjust report sections if needed
- Fine-tune schedule or escalation thresholds

### Success Measurement (Month 3)
- Conduct full KPI assessment
- Stakeholder satisfaction survey
- Cost-benefit validation
- Recommendation for portfolio expansion or process changes

---

**Document Prepared:** June 2026  
**System Status:** Operational  
**Next Review Date:** September 2026 (post Month-3 KPI assessment)
