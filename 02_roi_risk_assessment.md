# ROI & Risk Assessment
## dena IME — AI Portfolio Reporting System

**Version:** 1.1 · **Date:** June 2026 · **Currency:** EUR (1 USD = 0.92 EUR) · **Horizon:** 12 & 36 months

---

## Executive Summary

The dena IME AI Portfolio Reporting System delivers a **high-return, low-risk investment**. Under the base-case scenario, the system pays for itself in **7 weeks** and generates a Year 1 net benefit of **€24,905** after upfront costs (580% ROI). Even in a downside scenario — where user adoption is low and only 2 hours per week are saved — the system breaks even in Year 2. Total risk score across 8 assessed risks is **75/200 (Low)**. Recommendation: **proceed with full deployment.**

---

## Part A — Return on Investment

### A.1 Upfront Costs (One-Time Investment)

| Cost Category | Hours | Estimate | Basis | Notes |
|---|---|---|---|---|
| Development Time | 40 hrs | €2,600 | [ASSUMPTION] 40 hrs @ €65/hr fully loaded | System design, coding, testing, deployment |
| Setup & Configuration | 8 hrs | €520 | [ASSUMPTION] 8 hrs @ €65/hr | Claude API, Railway, Resend, env config |
| Training & Documentation | 4 hrs | €260 | [ASSUMPTION] 4 hrs @ €65/hr | Stakeholder training, README, documentation |
| Testing & QA | 8 hrs | €520 | [ASSUMPTION] 8 hrs @ €65/hr | Local testing, mock data, error scenarios |
| Contingency (10%) | — | €390 | [ASSUMPTION] 10% buffer | Overruns, rework, troubleshooting |
| **TOTAL UPFRONT COSTS** | **60 hrs** | **€4,290** | One-time investment | |

---

### A.2 Ongoing Costs (Annual)

> **\* Human Review is a mandatory design decision, not optional overhead.** The 1 hr/week PM review loop serves as the primary human-in-the-loop control required under EU AI Act transparency obligations and is essential for catching LLM hallucinations before distribution. See Risk 2.1 and Compliance Documentation.

| Category | Frequency | Annual Vol. | Unit Cost | Annual Cost | Notes |
|---|---|---|---|---|---|
| Claude API (Sonnet) | Weekly | 52 reports | ≈€0.003/report | €0.14 | [ASSUMPTION] ~2,000 tokens/report, Sonnet pricing |
| Railway Hosting | Monthly | 12 months | €4.60/month | €55.20 | [ASSUMPTION] Starter plan; includes process uptime + logging |
| Resend Email API | Per email | 52 emails | Free (≤100/mo) | €0.00 | Free tier covers 52 weekly reports; no overage expected |
| Human Review (QA) * | Weekly | 52 weeks | €65/hr | €3,380 | [DESIGN DECISION] 1 hr/week PM review — mandatory human-in-the-loop |
| Maintenance & Support | Ad-hoc | 4 hrs/year | €65/hr | €260 | [ASSUMPTION] Log review, prompt refinement, minor fixes |
| **TOTAL ANNUAL ONGOING COSTS** | | | | **€3,695** | |

---

### A.3 Business Value (Direct Cost Savings)

| Benefit | Baseline State | After System | Annual Saving | Assumption Basis |
|---|---|---|---|---|
| Portfolio Manager Time | 7–10 hrs/week manual compilation | 1 hr/week review only | **€25,350/yr** | 7.5 hrs × 52 × €65/hr [ASSUMPTION] |
| Leadership Review Time | 2–3 hrs (awaiting clarifications) | <30 min (self-contained report) | **€6,760/yr** | 2 hrs × 52 × €65/hr [ASSUMPTION] |
| Finance Validation Cycles | 4–6 hrs/month manual cross-checking | 1 hr/month (automated validation) | **€780/yr** | 12 hrs × €65/hr [ASSUMPTION] |
| **TOTAL DIRECT ANNUAL SAVINGS** | | | **€32,890/yr** | Conservative (1 FTE scope) |

---

### A.4 Indirect & Strategic Benefits (Unquantified in Base Case)

- **Early Warning System Value: €15,000–50,000/yr [ASSUMPTION]** — System prevents 1–2 project escalations/year (50% success rate assumed). Not included in conservative scenario.
- **Portfolio Scaling Enabler: €200,000+/yr (Year 2+) [ASSUMPTION]** — System enables 50+ projects without additional analyst hire. Avoids €50–70K/yr FTE cost.
- **Audit & Compliance Trail: €5,000–10,000/yr [ASSUMPTION]** — Automatic logging reduces manual documentation burden. Estimated via reduced compliance prep time.
- **Decision Quality Improvement: Not quantified** — Structured AI analysis reduces subjective judgment errors. Measurable via audit trail, not directly attributable to system.

---

### A.5 ROI Scenarios — Four-Case Analysis

> **Methodology note:** Year 1 ROI is calculated as `(Annual Benefit − Annual Costs − Upfront Costs) / Upfront Costs`. This is the honest measure — it deducts the full upfront investment in Year 1. The downside scenario stress-tests the investment under low-adoption conditions.

| Metric | ⚠ Downside | Conservative | Moderate | Optimistic |
|---|---|---|---|---|
| **Assumption** | 2 hrs/week saved; low adoption | 7.5 hrs/week saved; base case | 7.5 hrs + early warning value | Full savings + portfolio scaling |
| Annual Benefit | €6,760 | €32,890 | €37,890 | €147,890 |
| Annual Ongoing Cost | €3,695 | €3,695 | €3,695 | €4,195 |
| Upfront Cost | €4,290 | €4,290 | €4,290 | €4,290 |
| **Year 1 Net (incl. upfront)** | **−€1,225** | **€24,905** | **€29,905** | **€139,405** |
| **Year 1 ROI (on upfront)** | **−29%** | **580%** | **697%** | **3,250%** |
| Year 3 ROI (cumulative) | 297% | 1,741% | 2,091% | 10,261% |
| Break-Even Point | Year 2, Q1 | **7 weeks** | **6 weeks** | **11 days** |
| Cumulative 3-Year Net | €11,495 | **€82,975** | **€97,975** | **€432,345** |

> **Downside scenario interpretation:** If adoption is low (2 hrs/week saved vs. 7.5 hrs baseline), Year 1 returns a small net loss of −€1,225. The system still recoups its investment in Year 2 (cumulative net: +€11,495 by Year 3). This confirms the **investment is robust even under pessimistic conditions**, with no scenario producing a long-term loss.

---

### A.6 Key Assumptions & Sensitivity Analysis

| Assumption | Base Value | Sensitivity Range | Year 1 ROI Impact |
|---|---|---|---|
| PM Loaded Hourly Rate | €65/hr | ±€10/hr | ±€7,800/yr (±187%) |
| Weekly Time Savings (PM) | 7.5 hrs/week | 2–10 hrs/week | ROI: −29% to +1,341% |
| Claude API Cost | €0.003/report | 10× increase | −€1.26/yr (negligible) |
| Human Review Hours/Week | 1 hr/week | 0.5–2 hrs/week | ±€1,690/yr (±40%) |
| Adoption Rate (savings realized) | 100% | 50–100% | ROI: 251–580% Year 1 |

**Conclusion:** ROI is driven primarily by the PM time-savings assumption (7.5 hrs/week). This is the single variable that most affects outcomes and **must be validated in the pilot phase via time-tracking.** API and hosting costs are negligible at current scale and have virtually no sensitivity impact.

---

## Part B — Risk Assessment

Risk Score = Likelihood (1–5) × Impact (1–5). Thresholds: 1–5 Minimal (accept) · 6–12 Low (monitor) · 13–17 Medium (mitigate) · 18–25 High/Critical (escalate).

---

### Risk 1.1 — GDPR Data Protection Violation

| Dimension | Details |
|---|---|
| **Category** | Regulatory |
| **Description** | Excel data may contain personal identifiers (PM names, email addresses). Claude API processes this data; a breach or non-compliant Anthropic data-retention policy may trigger GDPR Article 32 violations. Resend email service may also store email metadata. |
| **Trigger** | Breach of Claude AI infrastructure, or discovery that Anthropic terms permit retention beyond processing period. |
| **Likelihood** | 2/5 — Anthropic maintains strong privacy commitments; no known breaches. GDPR compliance is mature in EU tech industry. |
| **Impact** | 4/5 — GDPR penalties up to €20M or 4% annual revenue. Federal agency reputational damage is severe. |
| **Risk Score** | **2 × 4 = 8 (Low — Monitor)** |
| **Mitigation** | Conduct GDPR DPA audit with Anthropic and Resend before processing real data. Anonymize PM names in reports (use role/ID only). Maintain data processing inventory; annual vendor audit. |

---

### Risk 1.2 — IT Security Act Compliance Gap

| Dimension | Details |
|---|---|
| **Category** | Regulatory |
| **Description** | dena is subject to the German IT-Sicherheitsgesetz. Railway and Anthropic cloud infrastructure may not fully satisfy public-sector security standards for encryption, access control, and data residency. |
| **Trigger** | Federal IT auditor flags compliance gaps; new regulation tightens data residency requirements. |
| **Likelihood** | 2/5 — dena already uses cloud services (reduced from 3/5); precedent exists for federal agency exemptions. Regulators are scrutinizing AI procurement more closely. |
| **Impact** | 4/5 — System shutdown pending security audit; political risk; loss of executive buy-in for AI initiatives. |
| **Risk Score** | **2 × 4 = 8 (Low — Monitor)** |
| **Mitigation** | Obtain BSI compliance assessment before production. Quarterly security audits; vendor certifications (Anthropic SOC 2, Railway ISO). Local audit log of all API calls. Pause production if gap found; notify CISO and Legal. |

---

### Risk 2.1 — Claude API Hallucination / Incorrect Analysis

| Dimension | Details |
|---|---|
| **Category** | Technical |
| **Description** | Claude Sonnet occasionally generates plausible but factually incorrect analysis — inflating risk scores, missing budget signals, or misinterpreting escalation flags. Leadership makes decisions on flawed analysis. |
| **Trigger** | Leadership acts on a report recommendation later proven wrong. Budget signal missed; project fails or is incorrectly flagged. |
| **Likelihood** | 3/5 — Claude Sonnet has high accuracy on structured data, but no LLM is perfect. Risk increases with poor Excel data quality. Estimated 1–2 errors/year at 26-project scale. |
| **Impact** | 4/5 — Wrong decision cascades: delayed intervention may cost €100K+. Trust in system collapses; reversion to manual process. |
| **Risk Score** | **3 × 4 = 12 (Low — Monitor)** |
| **Mitigation** | Human-in-the-Loop (mandatory design decision): PM reviews report every Monday before distribution. Structured system prompt with explicit calculation steps. Track hallucinations; if >2/month, escalate to technical review. Maintain manual process runbook as fallback. |

---

### Risk 2.2 — External API Downtime

| Dimension | Details |
|---|---|
| **Category** | Technical |
| **Description** | Claude API, Resend, or Railway becomes unavailable. System cannot generate or deliver weekly report. Repeated outages erode stakeholder trust. |
| **Trigger** | Any of: Anthropic outage, Resend degradation, Railway crash, or network issue at Monday 08:00 window. |
| **Likelihood** | 2/5 — Major providers typically run at 99.9%+ uptime. Probability of Monday window collision: ~2–3%. |
| **Impact** | 3/5 — One missed report: minimal. More than 2/year: reputation damage, system questioned. |
| **Risk Score** | **2 × 3 = 6 (Minimal — Monitor)** |
| **Mitigation** | APScheduler retry logic (auto-rerun after 1 hour). Commit to SLA: report delivered by Tuesday 17:00 at latest. After 3 failed attempts, alert Division Head and IT. Manual Gmail fallback as last resort. |

---

### Risk 3.1 — AI Bias in Project Risk Assessment

| Dimension | Details |
|---|---|
| **Category** | Ethical |
| **Description** | Claude analysis may encode bias based on funder type, project size, or historical flags — creating self-fulfilling risk assessments. Leadership may unconsciously treat AI recommendations as objective truth. |
| **Trigger** | PM or funder questions fairness of risk assessment. Audit reveals correlation between flags and protected characteristics. |
| **Likelihood** | 2/5 — Claude uses structured financial data (not subjective text) as primary input, reducing bias risk. Increases if system prompt contains implicit priors. |
| **Impact** | 4/5 — Unfair project flagging leads to funding loss, PM morale damage, legal risk, and external media scrutiny of federal AI procurement. |
| **Risk Score** | **2 × 4 = 8 (Low — Monitor)** |
| **Mitigation** | Audit system prompt for implicit bias language. Use only objective quantifiable metrics (budget %, burn rate, milestone status). Quarterly bias audit: analyze historical recommendations by project characteristics. Publish report methodology so PMs understand scoring logic. |

---

### Risk 3.2 — Over-Reliance on AI / Loss of Human Judgment

| Dimension | Details |
|---|---|
| **Category** | Ethical |
| **Description** | Leadership begins to trust AI recommendations uncritically. Complex decisions (project extensions, scope changes) are deferred to system. Institutional knowledge atrophies. If system fails, no fallback decision-making process exists. |
| **Trigger** | Major project termination decision made solely on AI recommendation, against PM pushback, later proven wrong. Or: system halts and no one can generate manual report. |
| **Likelihood** | 3/5 — Automation bias is well-documented. Risk is moderated by dena's strong human governance culture as a federal agency. |
| **Impact** | 3/5 — Poor project decisions, PM morale damage, reputational risk if externally visible. |
| **Risk Score** | **3 × 3 = 9 (Low — Monitor)** |
| **Mitigation** | Frame system as "decision support, not decision maker." Include limitations section in every report. Require Division Head + PM + Finance sign-off for major decisions. Quarterly "decision recovery drill" to keep manual process practiced. Track AI recommendation acceptance rate; flag if >80%. |

---

### Risk 4.1 — Poor User Adoption / Change Resistance

| Dimension | Details |
|---|---|
| **Category** | Operational |
| **Description** | PMs resist structured AI output. Leadership finds new format less satisfying. Stakeholders receive emails they don't trust or read. System technically works but ROI never materializes. |
| **Trigger** | First reports delivered; <50% email open rate; PMs bypass system and continue manual analysis. |
| **Likelihood** | 2/5 — Strong adoption driver: system eliminates 7.5 hrs/week of PM workload. Risk increases if perceived as imposed top-down. |
| **Impact** | 3/5 — ROI assumptions fail. Resources spent on maintenance without benefit. Opportunity cost. |
| **Risk Score** | **2 × 3 = 6 (Minimal — Monitor)** |
| **Mitigation** | Co-design report template with Division Head + PMs before launch. Frame as "your workload reduction tool." Track email open rates and satisfaction surveys (target: >75% satisfaction by Month 2). In Month 1, highlight one concrete insight the system enabled. |

---

### Risk 4.2 — Vendor Lock-In & Sustainability Risk

| Dimension | Details |
|---|---|
| **Category** | Operational |
| **Description** | System depends on Claude API + Railway + Resend. Dramatic price increases or service discontinuation could make system unaffordable or require €10–20K emergency migration. |
| **Trigger** | Anthropic raises Claude API pricing 10×; Railway discontinues Starter plan; Resend acquired and degraded. |
| **Likelihood** | 2/5 — Major cloud providers rarely make dramatic pricing changes. Risk becomes material at Year 5+. |
| **Impact** | 2/5 — Not critical to operations (can revert to manual), but disruptive. Migration effort: €10–20K engineering. |
| **Risk Score** | **2 × 2 = 4 (Minimal — Accept)** |
| **Mitigation** | Build vendor-agnostic API client layer (easy LLM provider swap). Quarterly monitor Claude pricing, Railway roadmap, Resend financials. Identify alternative LLMs (Haiku, Llama) as documented fallbacks. 6-month cash reserve for critical vendors. |

---

### B.9 Risk Summary Dashboard

| ID | Category | Description | Likelihood | Impact | Score | Status |
|---|---|---|---|---|---|---|
| 1.1 | Regulatory | GDPR Data Protection Violation | 2/5 | 4/5 | **8** | Monitor |
| 1.2 | Regulatory | IT Security Act Compliance Gap | 2/5 | 4/5 | **8** | Monitor |
| 2.1 | Technical | Claude API Hallucination / Incorrect Analysis | 3/5 | 4/5 | **12** | Monitor |
| 2.2 | Technical | External API Downtime | 2/5 | 3/5 | **6** | Monitor |
| 3.1 | Ethical | AI Bias in Project Risk Assessment | 2/5 | 4/5 | **8** | Monitor |
| 3.2 | Ethical | Over-Reliance on AI / Loss of Human Judgment | 3/5 | 3/5 | **9** | Monitor |
| 4.1 | Operational | Poor User Adoption / Change Resistance | 2/5 | 3/5 | **6** | Monitor |
| 4.2 | Operational | Vendor Lock-In & Sustainability Risk | 2/5 | 2/5 | **4** | Accept |
| | | | | **Total** | **75/200** | **Low** |

**Total Risk Score: 75/200 (37.5% utilization) — LOW OVERALL RISK PROFILE.** No critical or high-severity risks identified. Largest risks (IT Security compliance, Claude hallucination, over-reliance on AI) are fully manageable via the stated mitigation strategies. **Proceed with deployment.**

---

### B.10 Risk Governance & Monitoring Schedule

| Period | Review Focus | Owner |
|---|---|---|
| Q2 2026 (June) | Post-launch: IT audit compliance, API reliability metrics | Technical Lead + IT Manager |
| Q3 2026 (Sept) | Adoption metrics, hallucination incidence (<1/month target), bias audit | Project Sponsor + PM |
| Q4 2026 (Dec) | Year-end consolidation, vendor sustainability, update mitigations | Steering Committee |
| Q1 2027 (Jan) | Annual refresh, escalate new risks to CISO + Steering Committee | All Risk Owners |

---

## Part C — Investment Conclusion

| Dimension | Assessment |
|---|---|
| **Financial Returns** | Break-even in 7 weeks (conservative). Year 1 ROI: 580%. Cumulative 3-year net benefit: €82,975–€432,345 depending on scenario. Downside scenario still yields positive return by Year 2. |
| **Operational Returns** | 75% reduction in portfolio analyst time (7.5 hrs/week saved). Earlier risk detection. Structured, data-driven decision framework for IME leadership. |
| **Risk Profile** | Total risk score: 75/200 (Low). No critical risks. Largest risks manageable via DPA audit, human review loop, and prompt governance. |
| **Strategic Optionality** | System enables portfolio scaling (26 → 50+ projects) without proportional staffing increase. Foundation for future AI expansion within dena. |
| **Recommendation** | **APPROVE for full production deployment.** Allocate €5K Year 1 budget for operations + mitigation. Assign Risk Steward. Validate time-savings assumption in Month 1 via time-tracking. |

---

*Version 1.1 · Prepared June 2026 · Next Review: Q3 2026 · Steering Committee: 28 June 2026*