# Strategic Deployment Plan
## dena IME Weekly Portfolio Reporting System

**Document Version:** 1.1
**Date:** June 2026
**Planning Horizon:** June 2026 – December 2026 (7-month roadmap)
**Vision:** Operationalize AI-powered portfolio reporting as dena's core decision-support tool; evaluate external partnerships and licensing in Year 2
**Target Audience:** dena Executive Leadership, Steering Committee, IME Division (Industrie, Mobilität, Energieeffizienz)

---

## Part 1: Three-Phase Deployment Roadmap

### 1.1 Phase 1: Proof of Concept — COMPLETE

**Timeline:** [ASSUMPTION] April–May 2026 (8 weeks)
**Status:** ✅ Complete

#### Scope: What Was Proven

| Objective | Evidence | Status |
|---|---|---|
| Technical Feasibility | System runs stably; Claude API integrates successfully | ✅ Proven |
| Data Integration | Excel reader correctly extracts 26 projects; data schema validated | ✅ Proven |
| Report Quality | AI-generated reports are coherent, structured, actionable | ✅ Proven (subject to bias audit) |
| Scheduling | APScheduler triggers reports reliably every Monday 08:00 | ✅ Proven |
| Email Delivery | Resend successfully delivers to 10+ internal recipients | ✅ Proven |
| Cost Feasibility | Claude API costs ~€0.14/report; total operating cost <€4K/year | ✅ Proven |
| Time Savings Potential | Manual portfolio report: 7–10 hrs; AI version generated in <2 min | ✅ Proven |
| Compliance Readiness | EU AI Act (Limited-Risk), GDPR, IT Security Act frameworks documented | ✅ Proven (gaps on defined remediation timeline) |

#### Key Learnings

1. **Claude Sonnet accuracy is sufficient** for portfolio analysis — no major hallucinations in test runs; minor issues manageable with prompt refinement
2. **Internal stakeholder enthusiasm is high** — Division Head and PMs see immediate value
3. **System follows the Agentic AI pattern:** it plans (APScheduler defines weekly trigger), acts (reads Excel and calls Claude API), observes (logs outcomes, handles errors), and iterates (runs autonomously each week with prompt refinement between cycles) — this distinguishes it from a simple script and is a key design strength
4. ⚠️ **Data quality issues exist** in Excel file (inconsistent formatting, incomplete "Key Risk" entries) — mitigation required before Pilot
5. ⚠️ **GDPR compliance gaps** identified (third-party agreements, transparency notices) — must remediate before Pilot
6. ⚠️ **User training required** — end-users need education on AI system limitations and how to interpret recommendations

#### Transition Criteria (POC → Pilot)

- ✅ All technical components functional and documented
- ✅ Cost model validated
- ⚠️ GDPR gaps remediated (Anthropic DPA finalised, privacy notices distributed) — **required before Pilot launch**
- ⚠️ Data quality controls implemented in Excel workflow
- ⚠️ Training materials drafted

**Phase 1 Investment:** [ASSUMPTION] €2,970 (development, setup, testing at €45/hr)

---

### 1.2 Phase 2: Pilot (Internal Beta) — 60 Days

**Timeline:** July 1 – August 31, 2026 (9 weeks)
**Budget:** [ASSUMPTION] €8,000 (dedicated PM time, compliance work, training, monitoring)
**Success Criteria:** Go/No-Go decision for Phase 3 based on metrics below

#### Scope: Who & What

**Pilot User Group:**
- 10 project managers (self-selected volunteers representing different project types)
- IME Division Head, Finance lead (report recipients)
- IT staff (system monitoring)
- dena Compliance Officer (observer)

**Pilot Duration:** 9 consecutive weekly reports

**Pilot Objectives:**
1. Validate accuracy of recommendations against actual project status
2. Measure time savings in portfolio review process
3. Assess user satisfaction and adoption readiness
4. Identify edge cases in real-world use
5. Verify GDPR and compliance controls are effective
6. Build internal case study for full rollout communication

---

#### Phase 2 Milestone Table

| Week | Milestone | Owner | Success Criteria |
|---|---|---|---|
| W1 (Jun 30–Jul 6) | Compliance Remediation Complete | Legal + DPO | DPA signed, privacy notices sent, log retention defined |
| W1 (Jun 30–Jul 6) | Data Quality Review & Cleanup | PM + IT | Excel validated; duplicate/incomplete entries resolved |
| W1 (Jun 30–Jul 6) | User Training Materials Ready | Tech Lead | User guide, FAQ, video tutorial available |
| W2 (Jul 7–13) | Kick-off Meeting with Pilot Group | Sponsor | 10 PMs + leadership present; expectations aligned |
| W2 (Jul 7–13) | Report #1 Generated & Delivered | System | Report sent; recipients confirm delivery |
| W3–W9 (Jul 14–Aug 31) | Weekly Reports Delivered (8 reports) | System | Each report generated, delivered, logged |
| W3–W9 (Jul 14–Aug 31) | Weekly Stakeholder Debrief | Sponsor | Feedback collected; issues identified; prompt iterated if needed |
| W4, W6, W8 | Accuracy Spot-Check (bi-weekly) | QA + PMs | Manual validation of 5% of recommendations per report |
| W9 (Aug 25–31) | Pilot Evaluation Meeting | Sponsor | Analyse metrics; make Go/No-Go decision for Phase 3 |
| W9 (Aug 25–31) | Final Report & Recommendation | Sponsor | Document learnings; recommend next steps |

---

#### Phase 2 Success Metrics

| Metric | Target | Go-to-Phase-3 Threshold | Measurement |
|---|---|---|---|
| Adoption Rate | >75% pilot group actively reads report | >70% minimum | Weekly survey |
| Time Savings | PMs save ≥3 hrs/week on portfolio review | ≥2 hrs/week demonstrated | Pre/post time tracking (5 volunteer PMs) |
| Report Accuracy | ≥90% of recommendations align with PM assessment | ≥80% minimum | Spot-check vs. actual project status |
| User Satisfaction | >7/10 average rating | >6/10 minimum | Post-report survey (weekly, 9 responses) |
| Compliance Incidents | Zero critical incidents | Zero required | Incident log; DPO sign-off |
| System Uptime | 99%+ (1 report max delayed) | ≥95% minimum | Automated monitoring + logs |
| Decision Impact | ≥5 documented decisions influenced by AI analysis | Evidence of influence | Tracking form |

---

#### Phase 2 Go/No-Go Decision Criteria

**Greenlight (Proceed to Phase 3) if:**
- Adoption ≥70% AND Accuracy ≥80% AND Uptime ≥95%
- User satisfaction ≥6/10
- Zero critical compliance incidents
- Executive and Compliance Officer approval obtained

**Conditional Greenlight (proceed with caveats) if:**
- Adoption 60–69% → plan additional training in Phase 3
- Accuracy 75–79% → refine Claude prompt before Phase 3 launch
- Uptime 90–94% → investigate and patch infrastructure issues

**No-Go (pause and iterate) if:**
- Adoption <50% → stakeholder interviews; identify barriers; redesign training
- Accuracy <75% → Claude prompt overhaul; additional human review layer
- Uptime <90% → infrastructure audit; evaluate hosting migration
- Satisfaction <5/10 → full redesign required

**Terminate (project ended) if:**
- Data breach occurs (GDPR violation)
- Major regulatory finding (EU AI Act non-compliance)
- Executive decision to cease

---

#### Phase 2 Investment

| Cost Category | Estimate | Notes |
|---|---|---|
| Compliance Remediation | €2,000 | DPA finalisation, privacy notices, audit setup |
| Data Quality Cleanup | €1,000 | Manual review of 26 projects |
| User Training | €1,500 | Materials, delivery, support |
| System Monitoring & Support | €2,000 | Dedicated PM to monitor and respond |
| Evaluation & Reporting | €1,000 | Go/No-Go assessment, final report |
| Contingency (10%) | €500 | Buffer |
| **TOTAL PHASE 2** | **€8,000** | |

---

### 1.3 Phase 3: Full Deployment — Months 4–6

**Timeline:** September – November 2026 (12 weeks)
**Budget:** [ASSUMPTION] €12,000 (rollout, training at scale, IT handover)

#### Scope

From 10-person pilot → all 26 project managers + full IME leadership (~50 internal stakeholders). Weekly reports become official organisational product. System handed over to dena IT Operations for ongoing management.

**Rollout Waves:**
- Wave 1 (Sep 1–14): Kick-off + training for all teams
- Wave 2 (Sep 15–30): Stabilisation + feedback collection
- Wave 3 (Oct 1–31): Full-scale operations + optimisation
- Wave 4 (Nov 1–30): IT Ops handover + Year 2 strategy planning

---

#### Phase 3 Milestone Table

| Week | Milestone | Owner | Deliverable |
|---|---|---|---|
| W1–2 (Sep 1–14) | Pilot-to-Production Prep | Tech Lead | Infrastructure checklist; runbook |
| W1–2 (Sep 1–14) | All-Hands Training | Sponsor | 3× training sessions (50 participants); post-training quiz |
| W1–2 (Sep 1–14) | User Documentation Finalised | Tech Lead | PDF guide + video tutorials + FAQ portal |
| W3 (Sep 15–21) | Go-Live | System Ops | First official production report sent; monitoring active |
| W3–4 (Sep 15–28) | Daily Stand-ups | Sponsor | 15-min daily check-in on system health and feedback |
| W5–8 (Sep 29–Oct 26) | Steady-State Operations | IT Ops | Weekly reports delivered; support tickets handled <24 hrs |
| W8 (Oct 20–26) | Month 1 Retrospective | Sponsor | Performance vs. targets; optimisation plan |
| W9–12 (Oct 27–Nov 23) | Optimisation Phase | Tech Lead | Prompt refinement; performance tuning |
| W12 (Nov 17–23) | IT Operations Handover | Tech Lead + IT | Knowledge transfer; runbook sign-off; on-call setup |
| W13 (Nov 24–30) | Year 2 Planning Kickoff | Sponsor | Scope Q1 2027 enhancements; assign product owner |
| W13 (Nov 24–30) | Full Deployment Complete | Sponsor | System fully operational; IT Ops owns; Phase 3 closed |

---

#### Phase 3 Success Criteria

| Criterion | Target | Minimum |
|---|---|---|
| Adoption at Scale | >80% of IME staff use weekly report | >75% |
| Operational Efficiency | Portfolio review time reduced by 75% org-wide | Measured by Oct 31 |
| User Satisfaction | >8/10 average rating | >7/10 sustained |
| System Reliability | 99.5%+ uptime | 99% minimum |
| Executive Decision Impact | ≥10 documented decisions using AI insights | Tracked monthly |
| Compliance Maturity | All GDPR and AI Act obligations met; audit-ready | By Sep 30 |
| IT Operations Ready | IT team manages system independently | By Nov 30 |

---

#### Phase 3 Investment

| Cost Category | Estimate |
|---|---|
| Infrastructure Scaling | €1,500 |
| Training at Scale | €3,000 |
| Change Management & Support | €4,000 |
| Documentation & Knowledge Transfer | €2,000 |
| Contingency (10%) | €1,500 |
| **TOTAL PHASE 3** | **€12,000** |

---

### 1.4 Overall Timeline Summary

```
PHASE 1 POC          PHASE 2 PILOT        PHASE 3 FULL DEPLOYMENT
(April-May)          (July-Aug)           (Sep-Nov)
✅ COMPLETE          ⏳ PLANNED           ⏳ PLANNED

Apr  May   Jun   Jul   Aug   Sep   Oct   Nov   Dec
|--- POC ---|  |---- PILOT ----|  |------ FULL DEPLOYMENT -----|
                                                        → Year 2 Strategy
```

**Total Phase 1–3 Investment:** €2,970 + €8,000 + €12,000 = **€22,970**

**Note on payback periods:** Two valid payback metrics exist and should not be confused:

- **Operational break-even (ROI doc):** €2,970 upfront investment recouped in **~5.6 months** from direct time savings (€6,390/year, realistic scenario: 1.5 hrs/week at €45/hr). This measures the return on the build investment alone.
- **Full programme break-even (this document):** €22,970 total programme cost (including Pilot and Deployment phases) recouped in approximately **3.6 years** from direct time savings. This is the more conservative and comprehensive measure; business case depends on early-warning benefits or portfolio scaling.

Both are correct; they measure different things. The ROI document provides full scenario analysis.

---

## Part 2: Go-to-Market Strategy

### 2.1 Market Definition

#### Primary Market: Internal (dena IME Division)

26 active energy transition projects, ~50 stakeholders, manual weekly reporting process consuming 7–10 hrs/week of analyst time. Full deployment by Q4 2026. Prove ROI internally before any external expansion.

---

#### Secondary Market: External (Year 2+)

**Target Segments:**

1. **German Federal Agencies**
   - Bundesministerien and associated agencies managing large project portfolios
   - High strategic fit: similar Excel-based workflow, same regulatory environment, shared compliance frameworks
   - [ASSUMPTION] 5–10 potential agencies

2. **Energy Sector Organisations**
   - Utility companies and grid operators with renewable energy portfolios (e.g., E.ON, RWE, Bundesnetzagentur)
   - Private investment firms in energy transition space
   - [ASSUMPTION] 20–30 potential customers

3. **European Counterpart Agencies**
   - ADEME (France), IRENA member states, EU Commission Directorate-General for Energy
   - [ASSUMPTION] 10–15 potential organisations
   - Higher regulatory complexity; viable from 2028+

---

#### Market Attractiveness

| Segment | Entry Difficulty | Strategic Fit | Priority |
|---|---|---|---|
| Internal (dena IME) | Easy | High | 🔴 Now |
| Other dena divisions | Medium | High | 🟡 Q1 2027 |
| German federal agencies | High | Medium | 🟡 Q2 2027+ |
| Energy utilities | High | Medium | 🟡 Q2 2027+ |
| European agencies | Very High | Low–Medium | 🟡 2028+ |

---

### 2.2 Commercialisation Scenarios

**Scenario A: Internal Tool Only (Conservative)**
System remains proprietary to dena. No external commercialisation. Strategic asset providing competitive advantage and cost savings. Total investment: ~€25K sunk cost with ongoing annual return of ~€33K (time savings).

**Scenario B: Licensing / White-Label Model (Moderate)**
License system to other German agencies on per-seat or annual basis. dena provides training and support; partner agency deploys in their own environment. Data never leaves partner's infrastructure. Revenue: €2,000–5,000/customer/year. Timeline: first customer Q2 2027.

**Scenario C: Federated Platform / Partnership Model (Strategic)**
Build a multi-agency shared platform under a federal or EU-funded initiative. Not a commercial SaaS product — rather, a shared-service model consistent with dena's public mandate. Revenue via service fees or EU project funding. Timeline: Q3 2027+. This model is more appropriate for a federal GmbH than a commercial SaaS or investor exit scenario.

> **Note:** A commercial SaaS business model with external investors, IPO, or acquisition is not a realistic path for dena given its status as a federally owned GmbH. Scenarios B and C are designed to be consistent with dena's public mandate and governance constraints.

---

#### Recommended Model: Scenario A → B → C (Sequential)

**Year 1 (2026):** Internal tool only. Operational excellence; build case study; validate ROI.

**Year 2 (2027):** License to 1–2 federal agencies (Scenario B). Validate external demand; generate €10–20K revenue. Simultaneously assess Scenario C feasibility with Federal Ministry.

**Year 3 (2028):** Pursue federated platform model (Scenario C) if ministerial interest confirmed. Expand licensing to 5+ agencies.

---

#### Pricing (Licensing Model)

```
Annual License Fee:
- Base: €2,000/year (system access, updates, 12 training hours)
- Per-user: €50/user/year (for >20 users)
- Custom integration: €500–1,000 one-time
- Support: €100/hour (beyond included support)

Example: 50-user agency
- €2,000 + (50 × €50) = €4,500/year
- 3-year contract: €13,500 total (15% discount applied)
```

---

### 2.3 Go-to-Market Phasing

| Phase | Timeline | Activity | Revenue | Success Metric |
|---|---|---|---|---|
| Phase 0: Internal Scaling | Jun–Nov 2026 | Full deployment to dena IME (50 users) | €0 (cost centre) | 80%+ adoption; €845 Year 1 net benefit (realistic: 1.5 hrs/week saved) |
| Phase 1: Internal Expansion | Dec 2026–Q1 2027 | Expand to other dena divisions | €0 (internal allocation possible) | 50%+ other divisions adopt |
| Phase 2a: Licensing Pilot | Q1–Q2 2027 | License to 1–2 federal agencies | €8–10K | First customer signed; deployment success |
| Phase 2b: Federated Model Assessment | Q2–Q3 2027 | Assess Scenario C with Federal Ministry | €0 (R&D) | Ministry interest confirmed or ruled out |
| Phase 3: Licensing Scale | 2028 | Expand to 5–8 agency/utility customers | €25–40K/year | Positive operating contribution |
| Phase 4: Federated Platform | 2028–2029 | Multi-agency platform (if ministerial mandate) | Service fees / EU funding | Platform operational; 3+ agencies |

---

## Part 3: Stakeholder Communication Map

### 3.1 Executive Leadership (CFO, CIO, Division Head)

**What they care about:** ROI, risk mitigation, strategic positioning, Federal Ministry reporting

| Message | Evidence | Frequency |
|---|---|---|
| "We save €6K+/year on analyst time" | ROI doc — conservative scenario (€845 Year 1 net, realistic: 1.5 hrs/week at €45/hr) | Quarterly business review |
| "We reduce project failure risk with early warnings" | Risk assessment — early warning value quantified | Bi-weekly during pilot |
| "We maintain GDPR and AI Act compliance" | Compliance documentation | Monthly + audit cycles |
| "We position dena as AI/innovation leader in energy transition" | Case study + potential federal partnerships | Annual strategy meeting |
| "We have a clear path to licensing revenue from Year 2" | Go-to-market plan — Scenario B | Year 1 planning |

**Communication cadence:** Monthly one-slide status update → Quarterly executive review (30 min) → Annual strategy session (2 hrs re: Year 2 expansion)

---

### 3.2 Legal & Compliance (DPO, CISO, Compliance Officer)

**What they care about:** Risk, liability, regulatory compliance, audit readiness

| Message | Evidence | Frequency |
|---|---|---|
| "System is Limited-Risk under EU AI Act — classification is unambiguous" | EU AI Act compliance doc Part 1 | Pre-launch + annual review |
| "All GDPR obligations met with documented DPAs" | GDPR doc Part 4 | Pre-launch + quarterly |
| "US transfers protected by SCCs + Schrems II supplementary measures" | GDPR DPIA Part 3 | Quarterly; annual Schrems II review |
| "Full audit trail; incident response plan in place" | Logging system + breach procedure | On-demand; annual audit |
| "No high-risk decisions; humans always decide; Art. 22 exclusion maintained" | System architecture + acceptance rate monitoring | Pre-launch + when challenged |

**Communication cadence:** Pre-launch compliance review (1 hr) → Quarterly check-in (30 min) → Annual audit readiness review

---

### 3.3 IT Operations & Infrastructure Team

**What they care about:** Uptime, security, cost, scalability, handover readiness

| Message | Evidence | Frequency |
|---|---|---|
| "System is production-ready and operationally stable" | Phase 2 metrics (99%+ uptime, zero incidents) | Pre-launch + monthly |
| "Infrastructure cost is minimal (€55/month Railway)" | ROI doc — ongoing cost structure | Annual budget planning |
| "Handover documentation complete; on-call feasible" | Runbooks, dashboards, training materials | Pre-handover + post-handover |
| "Security controls configured; log retention defined" | GDPR doc Part 1 — data inventory + logs | Quarterly security review |
| "Environmental footprint is minimal: 52 API calls/year" | SCI assessment in EU AI Act compliance doc | Annual sustainability report |

**Communication cadence:** Pre-launch technical readiness review (2 hrs) → Monthly health check during Pilot (15 min) → Phase 3 knowledge transfer series (4× 1-hr sessions)

---

### 3.4 End-Users (Project Managers, Finance, Leadership)

**What they care about:** Time savings, ease of use, decision quality, fairness

| Message | Evidence | Frequency |
|---|---|---|
| "This saves you 3+ hours per week on portfolio review" | Time-tracking study from Pilot | Kick-off training |
| "Reports are written in plain language; nothing is a black box" | Sample report + transparency materials | Training + reference guide |
| "You remain in control — AI advises, you decide" | System architecture + human oversight flow | Training + kick-off |
| "Risk assessment is data-driven and objective — no subjective bias" | Bias audit schedule + system prompt design | Training + quarterly update |
| "Your privacy is protected; project data stays within dena" | Privacy notice (GDPR Appendix A) | Initial notification + FAQ |

**Communication cadence:** Pre-launch training (90 min) + Q&A → Weekly "Ask the Experts" office hours during Pilot → Monthly newsletter

---

### 3.5 Communication Plan Timeline

| Phase | Stakeholder | Message | Format | Frequency |
|---|---|---|---|---|
| POC (Complete) | All | "System proven; moving to Pilot" | Email + meeting | One-time |
| Pilot (Jul–Aug) | Exec | Monthly status; risk updates | Slides + email | Monthly |
| Pilot (Jul–Aug) | Legal/Compliance | GDPR gaps remediated; audit-ready | Memo + checklist | Pre-Pilot + monthly |
| Pilot (Jul–Aug) | IT Ops | System health; escalations | Dashboard + email | Weekly |
| Pilot (Jul–Aug) | Pilot PMs | Learnings and feedback requests | Email + meeting | Weekly |
| Pre-Phase-3 (Late Aug) | All | "Pilot succeeded; launching org-wide" | Email + all-hands | One-time |
| Phase 3 (Sep–Nov) | All users | Training + onboarding | Classes + videos | Staggered (Waves 1–3) |
| Phase 3 (Sep–Nov) | Exec | Adoption metrics + ROI validation | Dashboard + slides | Monthly |
| Phase 3 (Sep–Nov) | IT Ops | Handover readiness; runbook reviews | Meetings + docs | Bi-weekly (final 4 weeks) |
| Post-Phase-3 (Dec) | All | "System is live; here is the handbook" | Email + portal | One-time |

---

## Part 4: Success Metrics Per Phase

### 4.1 Phase 2 (Pilot) — Quantitative Metrics

| Metric | Target | Threshold | Measurement |
|---|---|---|---|
| Adoption Rate | >75% | >70% required | Survey: "Did you read the report?" |
| Time Savings | 3+ hrs/week per reviewer | 2+ hrs/week | Pre/post time logging (5 PMs) |
| Report Accuracy | ≥90% alignment with actual status | ≥80% | Spot-check (5% of recommendations) |
| User Satisfaction | >7.5/10 | >6/10 | Post-report Likert survey |
| System Uptime | 99.5% | 95% minimum | Automated monitoring + logs |
| Report Timeliness | 100% by 08:30 Mon | 95% on-time | Timestamp in logs |
| Escalation Accuracy | 100% Red flags are genuine | ≥90% | Retrospective validation |
| Cost per Report | <€1 | <€2 | API + hosting cost ÷ 9 reports |

---

### 4.2 Phase 2 — Qualitative Metrics

| Metric | Target | Assessment |
|---|---|---|
| User Confidence | PMs express confidence in recommendations | Semi-structured interviews (5 pilots) |
| Executive Perception | Division Head sees system as valuable | Executive feedback form |
| Compliance Maturity | All GDPR/AI Act gaps remediated | DPO sign-off + audit checklist |
| IT Readiness | Operations team can manage system | Knowledge transfer assessment |
| Data Quality | Excel data clean and consistent | Data validation audit |

---

### 4.3 Phase 3 (Full Deployment) — Success Metrics

| Metric | Target | Minimum | Timeline |
|---|---|---|---|
| Adoption at Scale | >80% of 50+ staff | >75% | By Nov 30 |
| Organisational Time Savings | 300+ hrs/year across org | 200 hrs minimum | Annualised from Oct data |
| Executive Decision Impact | ≥10 documented decisions using AI insights | Qualitative evidence | Q4 2026 |
| Portfolio Risk Detection | ≥3 at-risk projects flagged before crisis | Retrospective validation | Q1 2027 |
| System Reliability | 99.5%+ uptime | 99% minimum | Sep–Nov average |
| User Satisfaction | >8/10 average | >7/10 | Monthly survey (Sep–Nov) |
| IT Operations Ready | IT team independently manages system | Certified by IT lead | By Nov 30 |
| Compliance Maturity | Full compliance; audit-ready | Zero open gaps | By Sep 30 |

---

### 4.4 Year 2 Strategy Evaluation (January 2027)

**Decision point:** After Phase 3 completion, decide on Year 2 direction.

| Question | Evidence for External Expansion | Evidence for Internal Only |
|---|---|---|
| Is system working internally? | >80% adoption; >8/10 satisfaction; 99%+ uptime | <80% adoption; satisfaction or uptime issues |
| Is there external demand? | ≥2 inbound enquiries from agencies or utilities | Zero external enquiries |
| Can dena support it? | Dedicated resource identified | No internal resource available |
| Is there budget? | €50K+ allocated | No budget |
| Is leadership aligned? | CIO/CFO approve Year 2 expansion | Leadership prefers internal-only |
| Are compliance frameworks adequate? | EU AI Act + GDPR mature; DPAs in place | Framework under-developed for external deployment |

**Decision rule:**
- ≥4/6 criteria met → Pursue Scenario B (licensing) + assess Scenario C (federated platform)
- 3/6 criteria met → Expand to other dena divisions first; reassess external in 2028
- <3/6 criteria met → Internal tool only; system remains cost centre

---

## Part 5: Commercialisation Model

### 5.1 Recommended Path: Sequential A → B → C

**Year 1 (2026):** Internal tool only. Operational excellence; build case study; validate ROI.

**Year 2 (2027):** License to 1–2 federal agencies (Scenario B). Low-risk market entry; generate €10–20K revenue. Simultaneously assess Scenario C (federated model) with Federal Ministry stakeholders.

**Year 3 (2028):** Pursue federated platform model under ministerial mandate or EU-funded initiative if interest confirmed. Expand licensing to 5+ agencies/utilities.

---

### 5.2 Why This Model

| Advantage | Rationale |
|---|---|
| Consistent with dena's mandate | Licensing and federated models align with dena's role as a public-interest agency — not a commercial software vendor |
| Low risk | Licensing requires minimal product investment; fail-fast if no market demand |
| Revenue in Year 2 | €10–20K licensing revenue validates market without waiting for platform development |
| Scalable path | Federated model is inherently scalable without requiring a commercial SaaS business |
| Builds competency | dena develops product and partnership skills via licensing before committing to larger platform |

---

### 5.3 Licensing Model Detail (Scenario B)

**Target customer:** Federal agency managing 20–50 infrastructure or energy transition projects.

**Value proposition:** "Reduce portfolio reporting time by 75%; improve decision quality with AI-powered risk assessment. Fully compliant with GDPR and EU AI Act. Proven at dena."

**Deal structure:**
```
Annual License:
- Base: €2,000/year (system access, updates, 12 hrs training)
- Per-user: €50/user/year (>20 users)
- Custom integration: €500–1,000 one-time
- Extended support: €100/hour

Example: 50-user agency
- €2,000 + (50 × €50) = €4,500/year
- 3-year contract with 15% discount: €11,475 total

Revenue projection:
- Year 2 (1 pilot customer): €4,500
- Year 2 (3 customers, if demand validates): €13,500
- Year 3 (5–8 customers): €22,500–36,000
```

**Customer onboarding (8 weeks):**
1. Weeks 1–2: Environment setup; Excel data migration
2. Weeks 2–3: Customisation (column names, analysis focus, prompt adjustment)
3. Week 4: User training (2× half-day sessions)
4. Weeks 5–8: Pilot (4 reports delivered; feedback loop)

---

### 5.4 Federated Platform Model (Scenario C)

**Vision:** Multi-agency shared portfolio intelligence platform, operated as a federal shared service or under an EU-funded initiative.

**Structure:**
- dena operates platform on behalf of participating agencies
- Each agency's data is isolated; no cross-agency data sharing
- Funded via service fees, federal budget allocation, or EU project funding (e.g., Horizon Europe, LIFE programme)
- Governance: steering committee with Ministry representation

**Why this fits dena better than a commercial SaaS:**
- Consistent with dena's public mandate (not profit-maximisation)
- Avoids commercial conflicts of interest as a federal GmbH
- Eligible for EU co-funding (reduces development cost risk)
- Positions dena as public digital infrastructure provider for the energy transition

**Timeline:**
- Q2 2027: Federal Ministry consultation — assess interest and mandate
- Q3 2027: Feasibility study + platform architecture (if mandate confirmed)
- Q1 2028: Platform pilot with 3 agencies
- 2029+: Full operation

---

### 5.5 Commercialisation Roadmap

```
2026: INTERNAL TOOL
- Deploy to dena IME (50 users)
- Build case study; validate €845 Year 1 net benefit (1.5 hrs/week saved at €45/hr)
- Prove operational reliability

2027 Q1-Q2: LICENSING PILOT
- License to 1-2 federal agencies
- Target: €8–13K revenue
- Learn customer needs and deployment friction

2027 Q2-Q4: PARALLEL TRACKS
- Track A: Expand licensing (3–5 customers; €15–25K)
- Track B: Federal Ministry consultation on Scenario C
- Track C: Hire/assign product resource for platform (if mandate)

2028: FEDERATED PLATFORM (if mandate confirmed)
- Platform pilot: 3 agencies
- Service fee model: €3–5K/agency/year
- EU co-funding application submitted

2029+: PLATFORM SCALE
- 8–15 agencies on platform
- Annual service revenue: €30–75K
- Platform self-sustaining; dena recoups development investment
```

---

### 5.6 Decision Framework: Year-End 2026

| Scenario | Conditions | Next Step |
|---|---|---|
| **Pursue Licensing (B)** | Internal tool successful; ≥1 inbound enquiry; resource available; budget approved | Initiate pilot customer engagement Q1 2027 |
| **Pursue Federated Model (C)** | Ministry stakeholder interest confirmed; EU funding viable | Feasibility study Q2 2027 |
| **Internal Expansion Only** | No external demand; resource constraints; internal tool still maturing | Expand to other dena divisions; reassess 2028 |
| **Internal Tool Only** | System underperforms internally; no demand; no budget | Optimise internal; defer external indefinitely |

---

## Part 6: Summary & Next Steps

### 6.1 Phasing Overview

| Phase | Duration | Status | Investment | Key Outcome |
|---|---|---|---|---|
| Phase 1: POC | Apr–May 2026 | ✅ Complete | €2,970 | Technical and cost feasibility proven |
| Phase 2: Pilot | Jul–Aug 2026 | ⏳ Planned | €8,000 | Go/No-Go decision for Phase 3 |
| Phase 3: Full Deploy | Sep–Nov 2026 | ⏳ Planned | €12,000 | System fully operational; 80%+ adoption |
| Year 2: Strategic Review | Dec 2026–Jan 2027 | ⏳ Planned | €0 (decision point) | Internal only vs. external expansion decision |

**Total Year 1 Investment:** €22,970
**Expected Year 1 Direct Benefit:** €6,390 (time savings — realistic scenario: 1.5 hrs/week at €45/hr)
**Year 1 Net Benefit (after all programme costs):** ~−€17,900 ⚠️ *Business case requires early-warning benefits or portfolio scaling*
**Operational break-even (upfront build cost only):** ~5.6 months (per ROI doc)
**Full programme break-even (all Phase 1–3 costs):** ~3.8 years (direct savings only; faster if ancillary benefits materialize)

---

### 6.2 Critical Path & Dependencies

```
CRITICAL PATH (blocks Phase 3 if delayed):

┌─ Compliance Remediation (Jun 30) — BLOCKING
│  ├─ Anthropic DPA finalised
│  ├─ Privacy Notices distributed to all 26 PMs
│  └─ Log retention policy defined
│
├─ Phase 2 Evaluation (Aug 31) — BLOCKING
│  ├─ Adoption ≥70%
│  ├─ Accuracy ≥80%
│  └─ Executive and Compliance Officer approval
│
└─ Phase 3 Launch (Sep 1) — BLOCKING
   ├─ Training materials ready
   ├─ IT Ops onboarded and certified
   └─ Full user rollout complete

Slack: 2 weeks. Each item slipping past deadline delays
Phase 3 by 1 week per item.
```

---

### 6.3 Governance & Decision Authority

| Decision | Owner | Approval Authority | Timeline |
|---|---|---|---|
| POC → Pilot | Sponsor | CIO + Division Head | June 30, 2026 |
| Pilot → Full Deploy | Sponsor | Steering Committee (CFO, CIO, Compliance) | August 31, 2026 |
| Year 2 Strategy (Internal vs. External) | CIO + Strategy Lead | Executive Leadership | January 2027 |
| Federated Platform Investment (Scenario C) | CFO + CIO | Executive Board + Federal Ministry | Q2 2027 |

---

### 6.4 Next Immediate Actions (June 2026)

**By June 20:**
- [ ] Compliance review meeting (DPO, Legal, CISO) — finalise remediation plan
- [ ] Data quality audit — identify and fix Excel issues
- [ ] Pilot user selection — recruit 10 volunteer PMs

**By June 30:**
- [ ] Anthropic DPA signed
- [ ] Privacy notices drafted and distributed to all 26 PMs
- [ ] Training materials drafted (first cut)
- [ ] Phase 2 kick-off meeting scheduled (July 7)

**By July 7:**
- [ ] Pilot begins (Report #1 generated and delivered)
- [ ] Weekly stakeholder debriefs scheduled
- [ ] Feedback collection process in place

---

## Conclusion

The dena IME Weekly Portfolio Reporting System has a clear, phased path to operational and strategic success.

**2026 Goal:** Full internal operationalisation — 50+ users, 99%+ uptime, 80%+ adoption, €845 Year 1 net benefit validated (or early-warning benefits measured if achievable).

**2027 Goal:** Validate external demand — license to 1–2 federal agencies; initiate Federal Ministry dialogue on federated platform model.

**2028+ Goal:** Establish dena as a shared-service provider of AI-powered portfolio intelligence for the public energy transition ecosystem — consistent with dena's public mandate, funded via service fees and EU project co-funding.

**Key success factors:**
1. Flawless Phase 2 execution — metrics, compliance, user feedback
2. Strong Phase 3 rollout — training, adoption, IT handover
3. Executive commitment to Year 2 growth agenda
4. External demand validation in 2026–2027
5. Regulatory environment remains stable (GDPR, EU AI Act, IT-Sicherheitsgesetz)

**Investment required:** €22,970 (Phases 1–3); €50K+ additional for Year 2 external expansion (licensing + platform assessment)

**Expected returns:** €6,390/year internal (time savings, realistic: 1.5 hrs/week at €45/hr); €25–75K/year external from Year 3 (licensing + platform service fees) — external revenue is critical to justify €22,970 programme investment

---

*Version 1.1 · Prepared June 15, 2026 · Next Review: July 31, 2026 (post-Pilot evaluation) · Approvers: CIO, CFO, Division Head, Compliance Officer*
