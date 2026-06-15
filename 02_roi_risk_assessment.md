# ROI & Risk Assessment: dena IME AI Portfolio Reporting System

**Document Version:** 1.0  
**Date:** June 2026  
**Project:** dena IME Weekly Report Automation  
**Currency:** EUR (€) | API costs converted from USD at 1 USD = 0.92 EUR  
**Analysis Horizon:** 12-month and 36-month projections

---

## PART A: ROI CALCULATION

### A.1 Cost Structure

#### Upfront Costs (One-Time)

| Cost Category | Duration | Estimate | Basis | Notes |
|---------------|----------|----------|-------|-------|
| **Development Time** | 40 hours | €2,600 | [ASSUMPTION] 40 hours @ €65/hr fully loaded rate | System design, coding, testing, initial deployment |
| **Setup & Configuration** | 8 hours | €520 | [ASSUMPTION] 8 hours @ €65/hr | Claude API setup, Railway account, Resend integration, env config |
| **Training & Documentation** | 4 hours | €260 | [ASSUMPTION] 4 hours @ €65/hr | Stakeholder training, README, process documentation |
| **Initial Testing & QA** | 8 hours | €520 | [ASSUMPTION] 8 hours @ €65/hr | Local testing, mock data, error scenario validation |
| **Contingency (10%)** | — | €390 | [ASSUMPTION] 10% buffer for unknowns | Overruns, rework, troubleshooting |
| | | | | |
| **TOTAL UPFRONT COSTS** | — | **€4,290** | — | **One-time investment** |

---

#### Ongoing Costs (Annual)

| Cost Category | Unit | Frequency | Annual Volume | Unit Cost | Annual Cost | Notes |
|---------------|------|-----------|----------------|-----------|------------|-------|
| **Claude API (Sonnet)** | Per report | Weekly | 52 reports | [ASSUMPTION] $0.003/report = €0.00276/report | €0.14 | Token usage: ~1,500-2,000 tokens/report, 52 reports/year |
| **Railway Hosting** | Per month | Monthly | 12 months | [ASSUMPTION] $5/month = €4.60/month | €55.20 | Assumes basic "Starter" plan, includes process uptime, logging |
| **Resend Email API** | Usage-based | 52 emails/year | 52 emails | Free (up to 100/month) | €0.00 | Free tier accommodates 52 weekly reports + fallback emails |
| **Manual Review & QA** | PM hours | Weekly | ~1 hour/week | €65/hour | €3,380 | [ASSUMPTION] 1 hr/week stakeholder review + system monitoring |
| **Maintenance & Support** | PM hours | Ad-hoc | [ASSUMPTION] 4 hours/year | €65/hour | €260 | Log review, prompt refinement, minor bug fixes |
| | | | | | |
| **TOTAL ANNUAL ONGOING COSTS** | — | — | — | — | **€3,745.34** | **All services combined** |

---

### A.2 Business Value (Benefits)

#### Direct Cost Savings

| Benefit | Baseline | After System | Weekly Savings | Annual Savings | Assumptions |
|---------|----------|--------------|----------------|---|---|
| **Portfolio Manager Time** | 7-10 hrs/week data compilation & analysis | 1 hr/week email review | 6-9 hours | [ASSUMPTION] 7.5 hours × 52 weeks × €65/hour = **€25,350/year** | Portfolio manager fully loaded cost €65/hr; system eliminates manual data work |
| **Leadership Review Time** | 2-3 hours (awaiting analyst clarification) | <30 minutes (report is self-contained) | 1.5-2.5 hours | [ASSUMPTION] 2 hours × 52 weeks × €65/hour = **€6,760/year** | Leadership fully loaded cost €65/hr; structured report eliminates clarification delays |
| **Finance Validation Cycles** | 4-6 hours/month (cross-checking spend data) | 1 hour/month (automated validation included) | ~12 hours/year | [ASSUMPTION] 12 hours × €65/hour = **€780/year** | Finance staff no longer manually correlates budget data |
| | | | | |
| **TOTAL DIRECT ANNUAL SAVINGS** | — | — | — | **€32,890/year** | Conservative estimate (1 FTE) |

---

#### Indirect / Strategic Benefits

| Benefit | Quantification | Basis | Risk of Realization |
|---------|---|---|---|
| **Early Warning System Value** | [ASSUMPTION] €15,000-50,000/year | Assumes system prevents 1-2 project escalations/year that would have cost €15K-25K each in crisis management + stakeholder remediation. Conservative: assume 50% success rate. | High (depends on Claude analysis quality) |
| **Ability to Scale Portfolio** | [ASSUMPTION] €200,000+/year (future) | System enables 50+ projects without hiring additional analyst. Avoids €50-70K/year salary for new FTE. Realized at Year 2. | High (scaling hypothesis) |
| **Data-Driven Decision Quality** | Not quantified | Structured AI analysis reduces subjective judgment errors, leading to better project steering. Difficult to isolate but measurable via audit trail. | Medium (difficult to measure) |
| **Audit & Compliance Trail** | [ASSUMPTION] €5,000-10,000/year | Automatic logging eliminates manual documentation burden. Valuable for Federal audits. Estimated via reduced compliance prep time. | Medium (depends on audit frequency) |

**Conservative Total (Direct + 25% of Early Warning):** €32,890 + €3,750 = **€36,640/year**

---

### A.3 ROI Calculation

#### Scenario 1: Conservative (Direct Savings Only)

**Annual Benefit:** €32,890  
**Annual Cost:** €3,745  
**Annual Net Benefit:** €29,145  
**Payback Period:** €4,290 / €29,145 = **0.15 years (7 weeks)**

```
Year 1 ROI = (€29,145 / €4,290) × 100 = 679%
Year 2 ROI = (€29,145 × 2 - €4,290) / €4,290 × 100 = 1,260%
Year 3 ROI = (€29,145 × 3 - €4,290) / €4,290 × 100 = 1,841%
```

#### Scenario 2: Moderate (Direct + Early Warning Value)

**Annual Benefit:** €32,890 + €5,000 (25% of early warning) = €37,890  
**Annual Cost:** €3,745  
**Annual Net Benefit:** €34,145  
**Payback Period:** €4,290 / €34,145 = **0.13 years (6 weeks)**

```
Year 1 ROI = (€34,145 / €4,290) × 100 = 796%
Year 2 ROI = (€34,145 × 2 - €4,290) / €4,290 × 100 = 1,491%
Year 3 ROI = (€34,145 × 3 - €4,290) / €4,290 × 100 = 2,286%
```

#### Scenario 3: Optimistic (Direct + Early Warning + Scaling Benefit)

**Annual Benefit:** €32,890 + €15,000 (full early warning) + €100,000 (scaling, partial year) = €147,890  
**Annual Cost:** €3,745 + €500 (infrastructure scaling) = €4,245  
**Annual Net Benefit:** €143,645  
**Payback Period:** €4,290 / €143,645 = **0.03 years (11 days)**

```
Year 1 ROI (partial scaling) = (€80,000 / €4,290) × 100 = 1,865%
Year 2 ROI (full scaling) = (€147,890 / €4,290) × 100 = 3,448%
Year 3 ROI (full scaling, stabilized) = (€147,890 / €4,290) × 100 = 3,448%
```

---

### A.4 Summary ROI Table

| Metric | Conservative | Moderate | Optimistic |
|--------|--------------|----------|-----------|
| **Upfront Cost** | €4,290 | €4,290 | €4,290 |
| **Annual Benefit** | €32,890 | €37,890 | €147,890 |
| **Annual Cost** | €3,745 | €3,745 | €4,245 |
| **Annual Net** | €29,145 | €34,145 | €143,645 |
| **Break-Even** | 7 weeks | 6 weeks | 11 days |
| **Year 1 ROI** | 679% | 796% | 1,865% |
| **Year 2 ROI** | 1,260% | 1,491% | 3,448% |
| **Year 3 ROI** | 1,841% | 2,286% | 3,448% |
| **Cumulative 3-Year Benefit** | €91,225 | €106,225 | €439,625 |

---

### A.5 Break-Even Analysis

#### Payback Period Calculation
```
Break-Even Point = Upfront Costs / Annual Net Benefit
                 = €4,290 / €29,145
                 = 0.147 years
                 = ~7 weeks (Conservative)
                 = ~6 weeks (Moderate)
                 = ~11 days (Optimistic)
```

**Result:** System pays for itself in **less than 2 months** under conservative assumptions. **Investment becomes cash-positive in Q2** if implemented in Q1.

---

### A.6 Financial Assumptions & Sensitivity

#### Key Assumptions (All Marked [ASSUMPTION])

| Assumption | Value | Basis | Sensitivity |
|-----------|-------|-------|-------------|
| Portfolio Manager Loaded Rate | €65/hour | [ASSUMPTION] German public sector salary midpoint (~€42K/year) + benefits (30%) + overhead (20%) | ±€10/hr = ±€7,800/year swing |
| Time Savings Baseline | 7.5 hours/week | [ASSUMPTION] Mid-point of 7-10 hour manual range | ±1 hour/week = ±€3,380/year swing |
| Claude API Cost | $0.003/report = €0.00276 | [ASSUMPTION] Based on Sonnet pricing: ~1,500 tokens @ $0.003/1M | Negligible sensitivity |
| Railway Monthly Cost | $5 = €4.60 | [ASSUMPTION] Starter plan; scales if traffic increases | +$10/month = +€120/year |
| Resend Email Cost | Free (up to 100/month) | [ASSUMPTION] Free tier accommodates 52/year; no overage expected | Scales if >100/month needed |
| Manual QA Hours | 1 hour/week | [ASSUMPTION] PM spot-check + stakeholder review; stabilizes after Month 1 | May decrease to 0.5 hr/week = -€1,690/year |
| Early Warning Value | €5K-15K/year | [ASSUMPTION] Prevent 0.5-1.5 escalations × €10K-15K per incident | High variance; not in conservative scenario |

#### Sensitivity Analysis
```
If time savings decrease by 20% → ROI drops to 543% (Year 1, conservative)
If loaded rate is 10% lower → ROI drops to 611% (Year 1, conservative)
If API costs increase 10x → ROI drops to 672% (negligible impact)
If early warning yields 2 prevented escalations → ROI jumps to 1,205% (Year 1, moderate)
```

**Conclusion:** ROI is robust. Even under pessimistic assumptions (20% lower time savings, 10% lower salary rate), Year 1 ROI exceeds 500%.

---

## PART B: RISK ASSESSMENT MATRIX

### B.1 Risk Framework

**Risk Score = Likelihood (1-5) × Impact (1-5)**

- **Score 1-5:** Minimal risk (accept)
- **Score 6-12:** Low risk (monitor)
- **Score 13-17:** Medium risk (mitigate)
- **Score 18-20:** High risk (active management required)
- **Score 21-25:** Critical risk (escalate to leadership)

---

### B.2 Risk Register

#### **Category 1: REGULATORY RISKS**

---

##### Risk 1.1: GDPR Data Protection Violation

| Dimension | Details |
|-----------|---------|
| **Description** | Excel data contains personal project manager names, email addresses, or indirect personal identifiers. Claude API processes this data; if a data breach occurs or Claude stores data beyond agreed terms, dena may violate GDPR Article 32 (data processor obligations). Resend email service may also store email metadata. |
| **Trigger** | Breach of Claude AI infrastructure, or discovery that Anthropic's terms of service permit data retention beyond processing period. |
| **Likelihood** | 2/5 | Anthropic has strong privacy commitments; Claude API has no known breaches. GDPR compliance is mature in EU tech industry. However, AI providers are still regulatorily tested. |
| **Impact** | 4/5 | GDPR penalties up to €20M or 4% annual revenue (whichever is higher). dena is federal agency; reputational damage severe. Media scrutiny on public sector AI use. |
| **Risk Score** | **2 × 4 = 8 (Low Risk)** | |
| **Mitigation Strategy** | <ul><li>**Preventive:** Conduct GDPR Data Processing Agreement (DPA) audit with Anthropic and Resend before processing real data.</li><li>**Detective:** Anonymize project manager names in report (use ID numbers only).</li><li>**Responsive:** Maintain data processing inventory and annual vendor audit schedule.</li><li>**Escalation:** Flag any vendor policy changes immediately to Legal team.</li></ul> |

---

##### Risk 1.2: Compliance with Federal IT Security Standards (IT-Sicherheitsgesetz)

| Dimension | Details |
|-----------|---------|
| **Description** | dena is a federal agency subject to German IT Security Act (IT-Sicherheitsgesetz). System must meet minimum security standards: encryption in transit, access controls, audit logging, incident response. Railway and Anthropic may not fully meet German public sector requirements. |
| **Trigger** | Federal IT auditor flags compliance gaps, or new regulation tightens data residency requirements. |
| **Likelihood** | 3/5 | dena likely has existing exemptions for cloud AI services (precedent in German gov). However, regulators increasingly scrutinize AI procurement. |
| **Impact** | 4/5 | System could be shut down pending security audit. Reputational damage. Non-compliance fines (not GDPR, but political risk). Loss of executive buy-in for AI initiatives. |
| **Risk Score** | **3 × 4 = 12 (Low Risk)** | |
| **Mitigation Strategy** | <ul><li>**Preventive:** Obtain IT Security Compliance Certificate from Federal IT Office (BSI) before production deployment.</li><li>**Detective:** Quarterly security audit; vendor security certifications (Anthropic SOC 2, Railway ISO compliance).</li><li>**Responsive:** Maintain audit log of all API calls (saved locally, not on Railway only).</li><li>**Escalation:** If audit gap found, pause production reports; notify CISO + Legal.</li></ul> |

---

#### **Category 2: TECHNICAL RISKS**

---

##### Risk 2.1: Claude API Model Hallucination / Incorrect Analysis

| Dimension | Details |
|-----------|---------|
| **Description** | Claude Sonnet occasionally generates plausible-sounding but factually incorrect analysis (hallucination). Examples: inflating risk scores, missing budget burn signals, or misinterpreting escalation flags. Leadership makes decisions based on flawed analysis, leading to poor project steering or missed red flags. |
| **Trigger** | Leadership acts on report recommendation that analysis later proves wrong. Budget burn signal missed; project fails. Project marked high-risk incorrectly; team morale damage. |
| **Likelihood** | 3/5 | Claude Sonnet has strong accuracy on structured data analysis. However, no LLM is perfect. Risk increases if Excel data quality is poor (missing values, inconsistent formats). [ASSUMPTION] 1-2 hallucinations/year likely at 26-project scale. |
| **Impact** | 4/5 | Wrong decision cascades: delayed intervention on at-risk project costs €100K+. Loss of trust in AI system. Leadership reverts to manual process. System is de facto abandoned. |
| **Risk Score** | **3 × 4 = 12 (Low Risk)** | |
| **Mitigation Strategy** | <ul><li>**Preventive:** Use Sonnet (not Haiku) for accuracy. Structure system prompt with explicit calculation steps (e.g., "calculate burn rate as: (Spend YTD / Budget) × 100").</li><li>**Detective:** Human review loop: 1 PM reviews report every Monday before distribution. Spot-check 5% of calculations manually.</li><li>**Responsive:** If error detected, send correction email. Adjust prompt for next week.</li><li>**Escalation:** Track hallucinations; if >2/month, escalate to technical review.</li><li>**Fallback:** Keep manual process runbook documented; can revert if AI fails.</li></ul> |

---

##### Risk 2.2: External API Downtime (Claude, Resend, Railway)

| Dimension | Details |
|-----------|---------|
| **Description** | Claude API becomes unavailable (maintenance, outage, rate limit hit). Resend email service fails. Railway hosting crashes. System cannot generate or deliver weekly report on Monday. Leadership receives no report; decision-making blocked. If outages are frequent, stakeholders lose trust in system. |
| **Trigger** | Any of: Anthropic infrastructure outage, Resend service degradation, Railway data center issue, or network connectivity problem. |
| **Likelihood** | 2/5 | Major cloud providers (Anthropic, Resend, Railway) typically have 99.9%+ uptime. Over 52 weeks, expect ~4 hours of downtime. Monday 08:00 UTC window is ~0.6% of week; probability of collision is low (~2-3%). However, correlated outages possible (e.g., both Anthropic and Railway on AWS). |
| **Impact** | 3/5 | One missed report: minimal (leadership waits 1 week). Two consecutive weeks: noticeable gap. More than 2 missed reports/year: reputation damage, system questioned. Not critical to operations (portfolio doesn't stop if report is late), but erodes user confidence. |
| **Risk Score** | **2 × 3 = 6 (Minimal Risk)** | |
| **Mitigation Strategy** | <ul><li>**Preventive:** Diversify dependencies: use Anthropic + backup LLM (Sonnet as primary, Haiku as fallback). Different email vendor fallback (manual Gmail as last resort).</li><li>**Detective:** APScheduler includes retry logic (automatic rerun after 1 hour if fails). Railway auto-restarts failed processes.</li><li>**Responsive:** If Monday report fails, system auto-retries Tuesday morning. Send manual email if both fail.</li><li>**Escalation:** After 3 failed attempts, send email to Division Head + IT flagging issue.</li><li>**SLA:** Commit to "report delivered by Tuesday 17:00 latest" (not Monday 08:00 hard requirement).</li></ul> |

---

#### **Category 3: ETHICAL RISKS**

---

##### Risk 3.1: AI Bias in Project Risk Assessment

| Dimension | Details |
|-----------|---------|
| **Description** | Claude analysis may encode bias based on: project funder type (large vs. small funder favored), project manager background (perceived competence), or historical project performance (path dependency). System flags same project as "high risk" simply because it was flagged before, creating self-fulfilling prophecy. Project managers from underrepresented backgrounds may be unfairly penalized. Leadership unconsciously over-weighs AI recommendations, treating them as objective truth. |
| **Trigger** | Project manager (or funder) publicly questions fairness of risk assessment. Analysis audit reveals correlation between project flags and protected characteristics (funder nationality, PM gender, etc.). |
| **Likelihood** | 2/5 | Claude is trained to avoid bias and uses structured data (budget, milestones) as input, not subjective judgments. Risk increases if system prompt inadvertently primes bias (e.g., "German projects perform better historically"). Likelihood is low if input data is purely financial. |
| **Impact** | 4/5 | Unfair flagging of project leads to: reduced funding, PM morale damage, team churn, or legal risk if bias can be proven. Broader damage: loss of organizational trust in AI. External criticism ("dena's AI system is biased") reaches media. Federal ministry questions AI procurement practices. |
| **Risk Score** | **2 × 4 = 8 (Low Risk)** | |
| **Mitigation Strategy** | <ul><li>**Preventive:** Audit system prompt for hidden bias language. Use only objective, quantifiable metrics (Budget %, Burn Rate, Milestone Status). Remove any reference to project characteristics beyond financials.</li><li>**Detective:** Quarterly bias audit: analyze historical recommendations by funder, PM gender (if available), project size. Look for statistically unexplained variance.</li><li>**Responsive:** If bias detected, retrain prompt and re-analyze past reports. Communicate to affected stakeholders.</li><li>**Escalation:** If unfair assessment causes tangible harm (funding loss), escalate to Ethics Officer + Legal.</li><li>**Transparency:** Publish report methodology (what metrics drive risk assessment). Let PMs understand scoring logic.</li></ul> |

---

##### Risk 3.2: Over-Reliance on AI (Loss of Human Judgment)

| Dimension | Details |
|-----------|---------|
| **Description** | Leadership begins to trust AI recommendations uncritically, replacing human judgment entirely. PMs feel powerless ("the AI said I'm high-risk; there's nothing I can do"). Complex, context-dependent decisions (e.g., project extensions, scope changes) are deferred to system instead of driven by human expertise. Over time, institutional knowledge atrophies. If system fails, organization has no fallback decision-making process. |
| **Trigger** | Leadership makes major decision (e.g., project termination) based solely on AI recommendation, against PM pushback. Decision later proves wrong. Or: system halts; nobody knows how to generate report manually. |
| **Likelihood** | 3/5 | Human tendency to trust automation (automation bias) is well-documented. Risk increases if leadership is under time pressure and uses AI as shortcut. However, dena has strong human governance culture (federal agency); unlikely to abdicate entirely. |
| **Impact** | 3/5 | Poor project decisions (terminating viable project, over-investing in struggling one). Atrophy of PM capability and morale. System failure becomes catastrophic (no manual fallback). Stakeholder frustration ("we're slaves to the algorithm"). Reputational damage if externally visible. |
| **Risk Score** | **3 × 3 = 9 (Low Risk)** | |
| **Mitigation Strategy** | <ul><li>**Preventive:** Frame system as "decision support, not decision maker." Report design includes "limitations" section explaining what AI can/cannot assess. Explicitly assign human decision authority to Division Head (not system).</li><li>**Detective:** Quarterly review: track which recommendations are accepted vs. rejected. If acceptance rate >80%, flag over-reliance.</li><li>**Responsive:** Conduct "decision recovery drill" quarterly: manually generate report without system. Ensure fallback process is practiced, not theoretical.</li><li>**Escalation:** If major decision made on AI recommendation alone, require Division Head + PM + Finance sign-off before implementation.</li><li>**Training:** Annual refresher for stakeholders: "What this AI system can and cannot do."</li></ul> |

---

#### **Category 4: OPERATIONAL RISKS**

---

##### Risk 4.1: Poor User Adoption / Change Resistance

| Dimension | Details |
|-----------|---------|
| **Description** | Portfolio managers accustomed to manual, flexible reporting process resist structured AI output. Concerns: "the system doesn't capture our nuances," "I can't customize the message," "AI analysis is too generic." Leadership finds new report format less satisfying than old format. Stakeholders view system as additional burden (receiving emails they don't trust). Over time, nobody reads the report; system is ignored despite technical success. |
| **Trigger** | First few reports delivered; stakeholders express dissatisfaction. Adoption metrics show <50% of leadership opens weekly emails. PMs bypass system and still do manual analysis. |
| **Likelihood** | 2/5 | System is designed to *reduce* PM workload (by 7.5 hrs/week), which is a strong adoption driver. However, change resistance is common in government. Risk increases if system is perceived as "imposed from above" rather than co-designed with users. [ASSUMPTION] Adoption success depends heavily on communication and stakeholder involvement during rollout. |
| **Impact** | 3/5 | System technically works but is not used, so ROI never materializes. PM time savings don't happen. Leadership falls back to ad-hoc reporting. Resources spent on system maintenance without benefit. Opportunity cost: could have invested in other initiatives. |
| **Risk Score** | **2 × 3 = 6 (Minimal Risk)** | |
| **Mitigation Strategy** | <ul><li>**Preventive:** Involve stakeholders in system design early (before launch). Co-create report template with Division Head + PMs. Frame as "tool to reduce your workload," not "system to replace you."</li><li>**Detective:** Adoption metrics: track email open rates, stakeholder feedback surveys, manual report requests. Target: >75% stakeholder satisfaction by Month 2.</li><li>**Responsive:** If adoption is low, iterate: survey stakeholders on what's missing, adjust report format, increase one-on-one training.</li><li>**Escalation:** If <50% adoption by Month 3, pause system and conduct deep-dive user research.</li><li>**Quick wins:** In Month 1, highlight one concrete decision that system-generated insight enabled (e.g., "AI flagged project X; manager addressed issue before it escalated").</li></ul> |

---

##### Risk 4.2: Vendor Lock-In & Sustainability Risk

| Dimension | Details |
|-----------|---------|
| **Description** | System depends on Claude API + Railway + Resend. If Anthropic significantly raises API pricing, system becomes unaffordable. If Railway discontinues Starter plan, hosting costs jump. If Resend pivots business model, email service reliability drops. Organization becomes trapped: system is business-critical, but vendor has pricing power. Alternative: migrate to open-source LLM (e.g., Llama), but requires significant re-engineering. No internal expertise to maintain open-source stack long-term. |
| **Trigger** | Anthropic raises Claude API pricing by 10x (unlikely but possible). Railway discontinues free/low-cost tier. Resend acquired and service degraded. Or: organization wants to migrate to on-premise model for cost or security reasons. |
| **Likelihood** | 2/5 | Major cloud providers rarely make dramatic pricing changes (market competition). Claude pricing has been stable. However, AI pricing is evolving rapidly. [ASSUMPTION] Risk is real but not imminent over 3-year horizon. Becomes material risk at Year 5+. |
| **Impact** | 2/5 | If API costs spike, system may become unaffordable (€500/month vs. €55/month now). If hosting fails, downtime occurs. Not critical to operations (can revert to manual), but disruptive. Financial impact: €20K-50K emergency migration costs if re-engineering needed. |
| **Risk Score** | **2 × 2 = 4 (Minimal Risk)** | |
| **Mitigation Strategy** | <ul><li>**Preventive:** Maintain "vendor assessment" process. Quarterly monitor: Claude pricing changes, Railway roadmap, Resend financials / acquisition news. Diversify: identify alternative LLMs (Sonnet, then Haiku, then open-source Llama as fallback).</li><li>**Detective:** Build system to be vendor-agnostic: abstract API client layer (easy to swap LLM provider). Document system architecture for knowledge transfer.</li><li>**Responsive:** If vendor raises prices >50%, trigger evaluation of alternative. Budget for potential migration (€10K-20K engineering effort).</li><li>**Escalation:** If single vendor becomes unaffordable, escalate to CTO + Procurement for vendor negotiation or replacement.</li><li>**Insurance:** Keep 6-month cash reserve for critical vendors (build into annual budget).</li></ul> |

---

### B.3 Risk Summary Dashboard

| Risk ID | Category | Description | Likelihood | Impact | Risk Score | Priority |
|---------|----------|-------------|-----------|--------|------------|----------|
| 1.1 | Regulatory | GDPR Data Protection Violation | 2 | 4 | 8 | Monitor |
| 1.2 | Regulatory | IT Security Act Compliance Gap | 3 | 4 | 12 | Monitor |
| 2.1 | Technical | Claude API Hallucination / Incorrect Analysis | 3 | 4 | 12 | Monitor |
| 2.2 | Technical | External API Downtime | 2 | 3 | 6 | Monitor |
| 3.1 | Ethical | AI Bias in Project Risk Assessment | 2 | 4 | 8 | Monitor |
| 3.2 | Ethical | Over-Reliance on AI / Loss of Human Judgment | 3 | 3 | 9 | Monitor |
| 4.1 | Operational | Poor User Adoption / Change Resistance | 2 | 3 | 6 | Monitor |
| 4.2 | Operational | Vendor Lock-In & Sustainability Risk | 2 | 2 | 4 | Accept |
| | | | | | **TOTAL RISK SCORE** | **75 (Low)** |

---

### B.4 Risk Aggregation & Interpretation

**Total Risk Score Across 8 Risks:** 75/200 possible = **37.5% utilization** = **LOW OVERALL RISK PROFILE**

#### Risk Breakdown by Severity
- **Critical (21-25):** 0 risks
- **High (18-20):** 0 risks
- **Medium (13-17):** 0 risks
- **Low (6-12):** 6 risks (highest: IT Security Compliance, Claude Hallucination, Over-Reliance on AI)
- **Minimal (1-5):** 2 risks

#### Interpretation
The system carries **low systematic risk**. No single risk threatens viability if mitigated appropriately. Risks are primarily:
1. **Regulatory/compliance** (moderate but manageable via DPA + IT audit)
2. **Technical** (low likelihood; mitigated by human review loop)
3. **Ethical** (low if designed carefully; high reputation damage if realized)
4. **Operational** (low adoption risk due to strong value proposition)

**Recommendation:** **Proceed with deployment.** Implement mitigation strategies in parallel with rollout. Assign a Risk Steward (IT Manager or Project Lead) to monitor risks quarterly.

---

### B.5 Risk Monitoring & Governance

#### Quarterly Risk Review Schedule
- **Q2 2026 (June):** Post-launch risk assessment. Verify compliance gap mitigation (IT audit). Track API reliability metrics.
- **Q3 2026 (Sept):** Adoption metrics review. Assess hallucination incidence (target: <1/month). Conduct bias audit.
- **Q4 2026 (Dec):** Year-end risk consolidation. Reassess vendor sustainability. Update mitigation strategies based on real-world experience.
- **Q1 2027 (Jan):** Annual risk refresh. Escalate any newly-identified risks to CISO + Steering Committee.

#### Risk Owner Assignments
| Risk Category | Owner | Escalation Path |
|---|---|---|
| Regulatory (1.1, 1.2) | IT Manager + Legal Counsel | CISO → CTO → CFO |
| Technical (2.1, 2.2) | Technical Lead (System Owner) | CTO → VP Engineering |
| Ethical (3.1, 3.2) | Project Sponsor + Ethics Officer | Ethics Officer → Steering Committee |
| Operational (4.1, 4.2) | Project Sponsor + PM | Division Head → CTO |

---

## PART C: INTEGRATED ROI & RISK CONCLUSION

### Investment Thesis
The system is a **high-return, low-risk investment** for dena:

1. **Financial Returns:** Break-even in 6-7 weeks; Year 1 ROI of 679-796% (conservative scenarios). Cumulative 3-year benefit of €91K-106K.

2. **Operational Returns:** 75% reduction in portfolio analyst time (7.5 hours/week saved). Earlier risk detection. Data-driven decision framework.

3. **Risk Profile:** Total risk score of 75/200 (low). No critical risks. Largest risks (regulatory compliance, model hallucination) are highly manageable via mitigation strategies.

4. **Strategic Optionality:** System enables portfolio scaling (26→50+ projects) without proportional staffing increase. Unlocks future expansion.

### Recommendation
**Approve system for full production deployment.** Allocate €5K budget for Year 1 operations + mitigation (compliance audit, human review process, monitoring tools). Assign Risk Steward. Monitor quarterly per governance plan.

---

**Document Prepared:** June 2026  
**Next Review:** Q3 2026 (September) — Post-launch risk assessment  
**Steering Committee Review Date:** June 28, 2026
