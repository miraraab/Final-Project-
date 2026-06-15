# Strategic Deployment Plan
## dena IME Weekly Portfolio Reporting System

**Document Version:** 1.0  
**Date:** June 2026  
**Planning Horizon:** June 2026 – December 2026 (7-month roadmap)  
**Vision:** Operationalize AI-powered portfolio reporting as dena's core decision-support tool; evaluate external commercialisation in Year 2  
**Target Audience:** dena Executive Leadership, Steering Committee, IME Division

---

## PART 1: THREE-PHASE DEPLOYMENT ROADMAP

### 1.1 Phase 1: Proof of Concept (POC) — COMPLETED

**Timeline:** [ASSUMPTION] April–May 2026 (8 weeks)  
**Status:** ✅ COMPLETE

#### **Scope: What Was Proven**

| Objective | Evidence | Status |
|---|---|---|
| **Technical Feasibility** | System runs stably; Claude API integrates successfully | ✅ Proven |
| **Data Integration** | Excel reader correctly extracts 26 projects; data schema validated | ✅ Proven |
| **Report Quality** | AI-generated reports are coherent, structured, actionable | ✅ Proven (subject to bias audit) |
| **Scheduling** | APScheduler triggers reports reliably every Monday 08:00 | ✅ Proven |
| **Email Delivery** | Resend successfully delivers to 10+ internal recipients | ✅ Proven |
| **Cost Feasibility** | Claude API costs ~€0.14/report; total operating cost <€4K/year | ✅ Proven |
| **Time Savings Potential** | Manual portfolio report takes 7-10 hours; AI version generated in <2 minutes | ✅ Proven |
| **Compliance Readiness** | EU AI Act (Limited-Risk), GDPR, IT Security Act frameworks documented | ✅ Proven (gaps identified for remediation) |

#### **Key Learnings**

1. ✅ **Claude Sonnet is accurate enough** for portfolio analysis (no major hallucinations in test runs; minor issues manageable with prompt refinement)
2. ✅ **Internal stakeholder enthusiasm** is high (Division Head, PMs see immediate value)
3. ⚠️ **Data quality issues exist** in Excel file (inconsistent formatting, incomplete entries in "Key Risk" column) — mitigation needed before pilot
4. ⚠️ **GDPR compliance gaps** identified (third-party agreements, transparency notices) — must remediate before Pilot
5. ✅ **Automation is reliable** (no critical outages; single-vendor risk noted but acceptable with mitigation)
6. ⚠️ **User training needed** — end-users need education on AI system limitations and how to interpret recommendations

#### **Transition Criteria (POC → Pilot)**

- ✅ All technical components functional and documented
- ✅ Cost model validated
- ⚠️ GDPR gaps remediated (Anthropic DPA finalized, privacy notices distributed) — **BEFORE PILOT LAUNCH**
- ⚠️ Data quality controls implemented in Excel workflow
- ⚠️ Training materials drafted

**Phase 1 Investment:** [ASSUMPTION] €4,290 (development, setup, testing)

---

### 1.2 Phase 2: Pilot (Internal Beta) — 60 DAYS

**Timeline:** July 1 – August 31, 2026 (9 weeks)  
**Budget:** [ASSUMPTION] €8,000 (dedicated PM time, compliance work, training, monitoring)  
**Success Criteria:** Pilot greenlight (Yes/No) for Phase 3 based on metrics below

#### **Scope: Who & What**

**Pilot User Group:**
- **Core Users:** 10 project managers (self-selected volunteers representing different project types/geographies)
- **Leadership:** IME Division Head, Finance lead (readers of report)
- **Operations:** IT staff (system monitoring)
- **Observers:** dena Compliance Officer, EU AI Act assessor

**Pilot Duration:** Weekly reports generated and delivered for 9 consecutive weeks (9 reports total)

**Pilot Objectives:**
1. Validate accuracy of recommendations against actual project status
2. Measure time savings in portfolio review process
3. Assess user satisfaction and adoption readiness
4. Identify system issues/edge cases in real-world use
5. Verify GDPR/compliance controls are effective
6. Build internal case study for full rollout communication

---

#### **Phase 2 Milestone Table**

| Week | Milestone | Owner | Status | Success Criteria |
|---|---|---|---|---|
| **W1 (Jun 30-Jul 6)** | Compliance Remediation Complete | Legal + DPO | ⏳ Planned | DPA signed, privacy notices sent, logs configured |
| **W1 (Jun 30-Jul 6)** | Data Quality Review & Cleanup | PM + IT | ⏳ Planned | Excel file validated; duplicate/incomplete entries resolved |
| **W1 (Jun 30-Jul 6)** | User Training Materials Ready | Tech Lead | ⏳ Planned | Slideshow, user guide, FAQ, video tutorial available |
| **W2 (Jul 7-13)** | Kick-off Meeting with Pilot Group | Sponsor | ⏳ Planned | 10 PMs + leadership present; expectations aligned |
| **W2 (Jul 7-13)** | Report #1 Generated & Delivered | System | ✅ Automated | Report sent; recipients confirm delivery |
| **W3-W9 (Jul 14-Aug 31)** | Weekly Reports Delivered (8 reports) | System | ⏳ Ongoing | Each report generated, delivered, logged |
| **W3-W9 (Jul 14-Aug 31)** | Weekly Stakeholder Debrief | Sponsor | ⏳ Ongoing | Collect feedback, identify issues, iterate prompt if needed |
| **W4, W6, W8 (Bi-weekly)** | Accuracy Spot-Check | QA + PMs | ⏳ Planned | Manual validation of 5% of recommendations per report |
| **W9 (Aug 25-31)** | Pilot Evaluation Meeting | Sponsor | ⏳ Planned | Analyze metrics, make go/no-go decision for Phase 3 |
| **W9 (Aug 25-31)** | Final Report & Recommendation | Sponsor | ⏳ Planned | Document learnings, recommend next steps |

---

#### **Phase 2 Success Metrics**

| Metric | Target | Measurement Method | Go-to-Phase-3 Threshold |
|---|---|---|---|
| **Adoption Rate** | >75% pilot group actively uses report | Weekly survey: "Did you read the report?" | >70% minimum |
| **Time Savings Validation** | PMs save ≥3 hours/week on portfolio review | Pre/post time tracking (5 volunteer PMs) | Demonstrate 50%+ time reduction |
| **Report Accuracy** | ≥90% of recommendations align with PM assessment | Spot-check: compare AI flags to actual project status | ≥80% minimum |
| **User Satisfaction** | >7/10 average rating on usefulness | Post-report survey (weekly, 9 responses) | >6/10 minimum |
| **Zero Compliance Incidents** | No GDPR breaches, data leaks, or major security issues | Incident log review; DPO sign-off | Zero critical incidents |
| **System Uptime** | 99%+ (1 report max may be delayed) | Automated monitoring; log review | 95%+ minimum |
| **Decision Impact** | ≥5 documented decisions influenced by AI analysis | Tracking form: "Did you act on this recommendation?" | Evidence of influence |
| **Stakeholder Feedback** | No major concerns from executives, legal, or IT | Feedback form (end of pilot) | Majority support for Phase 3 |

---

#### **Phase 2 Go/No-Go Decision Criteria**

**GREENLIGHT for Phase 3 IF:**
- ✅ Adoption rate >70% (shows users engaged)
- ✅ Time savings demonstrated (≥50% reduction)
- ✅ Accuracy ≥80% (recommendations are reliable)
- ✅ User satisfaction >6/10 (acceptable, not requiring redesign)
- ✅ Zero critical incidents (no data breaches, major outages)
- ✅ Uptime ≥95% (reliable system)
- ✅ Executive + Compliance sign-off

**NO-GO / PAUSE IF:**
- ❌ Adoption <50% (suggests user skepticism)
- ❌ Accuracy <70% (recommendations unreliable; need prompt refinement or manual oversight)
- ❌ Critical compliance breach (GDPR violation, audit finding)
- ❌ System outages >5% (unreliable infrastructure)
- ❌ Executive concern about AI quality/bias

**NO-GO / TERMINATE IF:**
- ❌ Data breach occurs
- ❌ Major regulatory finding (AI Act violation)
- ❌ User satisfaction <4/10 (system rejected)

---

#### **Phase 2 Investment & Resource Allocation**

| Cost Category | Estimate | Notes |
|---|---|---|
| **Compliance Remediation** | €2,000 | DPA finalization, privacy notices, audit setup |
| **Data Quality Cleanup** | €1,000 | Manual review + validation of 26 projects |
| **User Training** | €1,500 | Materials, delivery, support |
| **System Monitoring & Support** | €2,000 | Dedicated PM to monitor, respond to issues |
| **Evaluation & Reporting** | €1,000 | Go/no-go assessment, final report |
| **Contingency (10%)** | €500 | Buffer for unknowns |
| | | |
| **TOTAL PHASE 2 COST** | **€8,000** | |

---

### 1.3 Phase 3: Full Deployment — Month 4–6

**Timeline:** September 2026 – November 2026 (12 weeks)  
**Budget:** [ASSUMPTION] €12,000 (rollout, training at scale, transition to operations)  
**Milestone Count:** 12 milestones

#### **Phase 3 Scope: Expansion & Operationalization**

**Expansion:**
- From 10-person pilot → all 26 project managers + full leadership team (~50 internal stakeholders)
- Weekly reports become official organizational product (not beta)
- Handoff to dena IT Operations (system maintenance, future enhancements)

**Rollout Strategy:**
- **Wave 1 (Sep 1-14):** Kick-off + training for all teams
- **Wave 2 (Sep 15-30):** Stabilization + feedback collection
- **Wave 3 (Oct 1-31):** Full-scale operations + optimization
- **Wave 4 (Nov 1-30):** Transition to IT Ops + strategy planning for Year 2

---

#### **Phase 3 Milestone Table**

| Week | Milestone | Owner | Deliverable |
|---|---|---|---|
| **W1-2 (Sep 1-14)** | Pilot-to-Production Prep | Tech Lead | Infrastructure scaling checklist, runbook |
| **W1-2 (Sep 1-14)** | All-Hands Training | Sponsor | 3x training sessions (50 participants); post-training quiz |
| **W1-2 (Sep 1-14)** | User Documentation Finalized | Tech Lead | PDF guide + video tutorials + FAQ portal |
| **W3 (Sep 15-21)** | Go-Live | System Ops | First official production report sent; monitoring active |
| **W3-4 (Sep 15-28)** | Daily Stand-ups | Sponsor | 15-min daily check-in on system health + feedback |
| **W4 (Sep 22-28)** | Week 1 Feedback & Adjustments | Tech Lead | Collect feedback; minor prompt tweaks if needed |
| **W5-8 (Sep 29-Oct 26)** | Steady-State Operations | IT Ops | Weekly reports delivered; support tickets handled <24hr |
| **W8 (Oct 20-26)** | Month 1 Retrospective | Sponsor | Assess performance against targets; plan optimizations |
| **W9-12 (Oct 27-Nov 23)** | Optimization Phase | Tech Lead | Prompt refinement, additional features, performance tuning |
| **W12 (Nov 17-23)** | IT Operations Handover | Tech Lead + IT | Knowledge transfer, runbook review, on-call setup |
| **W13 (Nov 24-30)** | Year-2 Planning Kickoff | Sponsor | Scope Q1 2027 enhancements; assign product owner |
| **W13 (Nov 24-30)** | Full Deployment Complete | Sponsor | System fully operational; IT Ops owns; Phase 3 closed |

---

#### **Phase 3 Success Criteria**

| Criterion | Target | Go-Live Requirement |
|---|---|---|
| **Adoption at Scale** | >80% of IME staff use weekly report | Required before Nov 1 |
| **Operational Efficiency** | Portfolio review time reduced by 75% organization-wide | Measured by Oct 31 |
| **User Satisfaction** | >8/10 average rating | Sustained through November |
| **System Reliability** | 99.5%+ uptime (max 1 missed report in 3 months) | Maintained throughout Phase 3 |
| **Executive Enablement** | Division Head makes ≥10 documented decisions using AI insights | Tracked monthly |
| **Compliance Maturity** | All GDPR/AI Act obligations met; audit-ready | By Sep 30 |
| **IT Operations Ready** | IT team can manage system independently; on-call support in place | By Nov 30 |

---

#### **Phase 3 Investment & Resource Allocation**

| Cost Category | Estimate |
|---|---|
| **Infrastructure Scaling** | €1,500 (Railway upgrade if needed) |
| **Training at Scale** | €3,000 (materials, facilitators, sessions) |
| **Change Management & Support** | €4,000 (dedicated PM for 12 weeks) |
| **Documentation & Knowledge Transfer** | €2,000 (runbooks, video, IT ops training) |
| **Contingency (10%)** | €1,500 |
| | |
| **TOTAL PHASE 3 COST** | **€12,000** |

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

**Total Investment:** €4,290 (POC) + €8,000 (Pilot) + €12,000 (Deployment) = **€24,290**

**Timeline to Full Operationalization:** 7 months (June 2026 → November 2026)

---

## PART 2: GO-TO-MARKET STRATEGY

### 2.1 Market Definition & Opportunity

#### **Primary Market: Internal (dena IME Division)**

**Current State:**
- Portfolio of 26 energy transition projects
- ~50 stakeholders (PMs, finance, leadership)
- Manual weekly reporting process (7-10 hours/week analyst time)
- No data-driven early warning system

**Market Size:** Internal (1 division), but potential to expand to other dena divisions (Climate Change, International Markets, etc.)

**Entry Strategy:** Full deployment as internal tool by Q4 2026. Prove ROI internally first (cost savings, decision quality, user adoption).

---

#### **Secondary Market: External (Potential, Year 2+)**

**Target Customer Segments:**

1. **German Federal Agencies (Ministries)**
   - Bundesministerium für Wirtschaft und Klimaschutz (Federal Ministry for Economic Affairs & Climate)
   - Bundesministerium für Umwelt, Naturschutz und Nukleare Sicherheit (Federal Ministry for Environment)
   - Other agencies with large project portfolios
   - Market Size: [ASSUMPTION] 5-10 potential agencies
   - Entry: Custom deployment or SaaS model

2. **Energy Sector Private Companies**
   - Utility companies with renewable energy portfolios (e.g., EON, RWE)
   - Grid operators (Bundesnetzagentur, TSO)
   - Private investment firms in energy transition space
   - Market Size: [ASSUMPTION] 20-30 potential customers
   - Entry: SaaS model or white-label licensing

3. **European Counterpart Agencies**
   - ADEME (France's energy agency)
   - IRENA member states
   - European Commission (Directorate-General for Energy)
   - Market Size: [ASSUMPTION] 10-15 potential customers
   - Entry: EU-funded projects or licensing agreement

---

#### **Market Attractiveness**

| Segment | TAM | Entry Difficulty | Strategic Fit | Year 2 Priority |
|---|---|---|---|---|
| **Internal (dena)** | 1 division, 50 users | Easy | High | 🔴 NOW |
| **Other dena divisions** | 4-5 divisions, 200+ users | Medium | High | 🟡 Q1 2027 |
| **German federal agencies** | 5-10 agencies, 1000+ users | High | Medium | 🟡 Q2 2027+ |
| **Energy utilities** | 20-30 companies, 5000+ users | High | Medium | 🟡 Q2 2027+ |
| **European agencies** | 10-15 agencies, 2000+ users | Very High (regulatory) | Low-Medium | 🟡 2028+ |

---

### 2.2 Commercialisation Model

#### **Three Scenarios**

**Scenario A: Internal Tool Only (Conservative)**
- System remains proprietary to dena
- No external commercialisation
- Long-term: Sunk cost (€25K+ investment)
- Benefit: Competitive advantage for dena; strategic asset
- **Timeline:** Indefinite

**Scenario B: Licensing / White-Label Model (Moderate)**
- License system to other German agencies on per-seat or annual basis
- dena provides training + ongoing support
- Partner agency customizes for their context
- Revenue model: €500-2000 per customer/year
- **Timeline:** Pilot in Q1 2027; first customer Q2 2027

**Scenario C: SaaS Platform (Aggressive)**
- Build multi-tenant SaaS platform (one system serves many customers)
- Offer as subscription (€100-500/month per agency)
- Dena becomes platform provider/vendor
- Requires: Significant re-architecture, compliance work (data isolation, security)
- Revenue model: €15K-100K+ annually per customer
- **Timeline:** Platform development Q1-Q3 2027; launch Q4 2027

---

#### **Recommended Model: Hybrid (B + C)**

**Year 1 (2026):** Internal tool only. Focus on operational excellence, user adoption, case study.

**Year 2 (2027):**
- **Phase 2a:** Licensing to 1-2 pilot federal agencies (Scenario B)
  - Outcome: €10-20K revenue; validate market demand
- **Phase 2b:** Begin SaaS platform development (Scenario C)
  - Outcome: Multi-tenant architecture; prepare for scale

**Year 3 (2028):**
- Launch SaaS platform commercially
- Expand to 5-10 agency/utility customers
- Outcome: €50-200K annual recurring revenue (ARR)

**Rationale:**
- ✅ Validate ROI internally first (reduces risk of external pitch)
- ✅ Licensing is low-risk entry to external market (quick win)
- ✅ SaaS is long-term monetisation (requires investment, but scalable)
- ✅ Aligns with dena's mission (energy transition tools serving broader ecosystem)
- ✅ Builds organizational capability (product development, customer support)

---

#### **Pricing Model (if Commercialised)**

**Scenario B: Licensing Model**

```
Annual License Fee:
- Base fee: €2,000/year (system access, updates, 12 training hours)
- Per-user fee: €50/user/year (for >20 users)
- Custom integration: €500-1,000 (one-time, connects to partner's Excel/systems)
- Support: €100/hour (optional, beyond included support)

Example: 50-user agency
- Base: €2,000 + (50 users × €50) = €4,500/year
- 3-year contract = €13,500 total
```

**Scenario C: SaaS Model**

```
Monthly Subscription:
- Starter: €99/month (up to 10 projects, basic reporting, email support)
- Pro: €299/month (up to 50 projects, advanced analytics, API access)
- Enterprise: €999/month (unlimited projects, custom features, dedicated support)

Example: 30-project organization
- Pro tier: €299/month × 12 = €3,588/year
- Annual discount (10%): €3,230/year
```

---

### 2.3 Go-to-Market Phasing

| Phase | Timeline | Activity | Revenue | Success Metric |
|---|---|---|---|---|
| **Phase 0: Internal Scaling** | Jun-Nov 2026 | Full deployment to dena IME (50 users) | €0 (cost center) | 80%+ adoption; €25K ROI proven |
| **Phase 1: Internal Expansion** | Dec 2026-Q1 2027 | Expand to other dena divisions (200+ users) | €0 (internal cost allocation possible) | 50%+ other divisions adopt |
| **Phase 2a: Licensing Pilot** | Q1-Q2 2027 | License to 1-2 federal agencies; validate market | €10-20K | Signing first customer; deployment success |
| **Phase 2b: SaaS Development** | Q1-Q3 2027 | Build multi-tenant platform; prepare launch | €0 (R&D investment) | Platform architecture complete; beta testing |
| **Phase 3: SaaS Launch** | Q4 2027 | Commercial SaaS launch to market | €10-50K (first 2-3 customers) | 3-5 paying customers by end 2027 |
| **Phase 4: Scale** | 2028+ | Growth to 20-50 customers | €100K+ ARR | Positive unit economics; expansion to Europe |

---

## PART 3: STAKEHOLDER COMMUNICATION MAP

### 3.1 Executive Leadership (CFO, CIO, Division Head)

**What They Care About:** ROI, risk mitigation, strategic advantage, board visibility

**Key Messages:**

| Message | Evidence | Frequency |
|---|---|---|
| **"We save €25K+ per year on analyst time"** | Cost-benefit analysis (Part A of ROI doc) | Quarterly business review |
| **"We reduce project failure risk with early warnings"** | DPIA + risk assessment (Parts B&C) | Bi-weekly during pilot |
| **"We maintain GDPR and AI Act compliance"** | Compliance documentation (Part 4) | Monthly + audit cycles |
| **"We position dena as AI/innovation leader in energy"** | Media positioning + awards potential | Annual strategy meeting |
| **"We have 2-3 year option to monetize externally"** | Go-to-market plan (Part 2 of this doc) | Year-1 planning |

**Communication Cadence:**
- **Monthly:** One-slide status update (metrics, blockers, spend)
- **Quarterly:** Executive review meeting (30 min) with business review
- **Annual:** Strategy session (2 hours) re: Year 2 expansion plans

**Format:** PowerPoint slides, Excel dashboards, brief emails (not long documents)

---

### 3.2 Legal & Compliance (DPO, CISO, Compliance Officer)

**What They Care About:** Risk, liability, regulatory compliance, audit readiness

**Key Messages:**

| Message | Evidence | Frequency |
|---|---|---|
| **"System is Limited-Risk under EU AI Act"** | Compliance doc Part 1 (risk classification) | Pre-launch + annual review |
| **"All GDPR obligations met with documented DPAs"** | Compliance doc Part 4 (GDPR + third-party agreements) | Pre-launch + quarterly checks |
| **"Data transfers to US are protected by SCCs + supplementary measures"** | DPIA Part 3 (Schrems II mitigations) | Quarterly; annual Schrems II review |
| **"Audit trail is complete; incident response plan is in place"** | Logging system + incident response procedure | On-demand; annual compliance audit |
| **"No high-risk decision-making; humans always decide"** | System architecture doc | Pre-launch + when challenged |

**Communication Cadence:**
- **Pre-Launch:** Compliance review meeting (1 hour) with DPO, CISO, Legal
- **Quarterly:** Compliance check-in (30 min) on GDPR/AI Act obligations
- **Annual:** Full audit readiness review (2 hours) with external auditors if needed

**Format:** Compliance matrices, audit checklists, certificate-of-compliance letters

---

### 3.3 IT Operations & Infrastructure Team

**What They Care About:** Uptime, security, cost, scalability, handoff readiness

**Key Messages:**

| Message | Evidence | Frequency |
|---|---|---|
| **"System is production-ready and operationally stable"** | Phase 2 metrics (99%+ uptime, zero incidents) | Pre-launch + monthly updates |
| **"We've eliminated vendor risk with fallback processes"** | Risk assessment Part B (vendor lock-in mitigation) | Quarterly review |
| **"Infrastructure cost is minimal (€5/month Railway)"** | ROI doc Part A (cost structure) | Annual budget planning |
| **"Handoff documentation is complete; on-call support is feasible"** | Runbooks, dashboards, training materials | Pre-handoff + post-handoff |
| **"Security controls are configured; log retention is defined"** | GDPR doc Part 1 (data inventory + logs) | Quarterly security review |

**Communication Cadence:**
- **Pre-Launch:** Technical readiness review (2 hours) with IT Ops, Security, Infrastructure
- **Monthly (during Pilot):** Operational health check (15 min) on uptime/errors
- **Phase 3 Handoff:** Knowledge transfer series (4x 1-hour sessions) on system architecture, monitoring, troubleshooting

**Format:** Architecture diagrams, runbooks, dashboards (Grafana/CloudWatch), configuration checklists

---

### 3.4 End-Users (Project Managers, Finance, Leadership)

**What They Care About:** Time savings, ease of use, decision quality, lack of surprise

**Key Messages:**

| Message | Evidence | Frequency |
|---|---|---|
| **"This saves you 3+ hours per week on portfolio review"** | Time-tracking study from Pilot (Phase 2 metrics) | Kick-off training |
| **"Reports are written in plain English; easy to understand"** | Sample report output with explanations | Training + reference guide |
| **"We explain how the AI works; nothing is a black box"** | System Card / transparency materials (Compliance doc) | Training + FAQ |
| **"You remain in control; AI advises, you decide"** | System architecture + human oversight flow | Training + kickoff |
| **"Privacy is protected; your project data stays within dena"** | Privacy notice (Compliance doc Appendix A) | Initial notification + FAQ |
| **"Support is available; we'll help you troubleshoot"** | Support contact info + response SLA (24 hours) | Training + email footer |

**Communication Cadence:**
- **Pre-Launch:** Training session (90 min) + Q&A; repeat 2-3x to accommodate schedules
- **Weekly (during Pilot + Phase 3):** "Ask the Experts" office hours (30 min) for questions
- **Monthly:** Newsletter with tips, highlights, upcoming features

**Format:** Slides, recorded videos, user guides (PDF + web), FAQs, email newsletters, office hours

---

### 3.5 Communication Plan Timeline

| Phase | Stakeholder | Message | Format | Owner | Frequency |
|---|---|---|---|---|---|
| **POC (Complete)** | All | "System is proven; moving to Pilot" | Email + meeting | Sponsor | One-time |
| **Pilot (Jul-Aug)** | Exec | Monthly status; risk updates | Slides + email | Sponsor | Monthly |
| **Pilot (Jul-Aug)** | Legal/Compliance | GDPR gaps remediated; audit-ready | Memo + checklist | DPO | Pre-Pilot + monthly |
| **Pilot (Jul-Aug)** | IT Ops | System health; escalations | Dashboard + email | Tech Lead | Weekly |
| **Pilot (Jul-Aug)** | Pilot PMs | "Here's what we're learning; feedback?" | Email + meeting | PM | Weekly |
| **Pre-Phase-3 (Late Aug)** | All | "Pilot succeeded; launching org-wide" | Email + all-hands | Sponsor | One-time |
| **Phase 3 (Sep-Nov)** | All users | Training + onboarding | Classes + videos | Training lead | Staggered (Wave 1-3) |
| **Phase 3 (Sep-Nov)** | Exec | Adoption metrics + ROI validation | Dashboard + slides | Sponsor | Monthly |
| **Phase 3 (Sep-Nov)** | IT Ops | Handoff readiness; runbook reviews | Meetings + docs | Tech Lead | Bi-weekly (final 4 weeks) |
| **Post-Phase-3 (Dec)** | All | "System is live; here's the handbook" | Email + portal | IT Ops | One-time |

---

## PART 4: SUCCESS METRICS PER PHASE

### 4.1 Phase 2 (Pilot) Success Metrics & Go/No-Go Criteria

#### **Quantitative Metrics**

| Metric | Target | Go/No-Go Threshold | Measurement |
|---|---|---|---|
| **Adoption Rate** | >75% | >70% required | Survey: "Did you read the report?" (weekly) |
| **Time Savings** | 3+ hrs/week per reviewer | 2+ hrs/week | Pre/post time logging (sample of 5 PMs) |
| **Report Accuracy** | ≥90% recommendations align with actual status | ≥80% | Spot-check by QA (5% of recommendations) |
| **User Satisfaction** | >7.5/10 | >6/10 | Post-report survey (Likert 1-10) |
| **System Uptime** | 99.5% (max 1 report delayed) | 95% | Automated monitoring + logs |
| **Report Timeliness** | 100% delivered by 08:30 Mon | 95% on-time | Timestamp in logs |
| **Escalation Accuracy** | 100% Red flags are genuine crises | ≥90% | Retrospective: was flag accurate? |
| **Cost per Report** | <€1 | <€2 | API usage + hosting cost ÷ 9 reports |

#### **Qualitative Metrics**

| Metric | Target | Assessment Method | Go/No-Go Threshold |
|---|---|---|---|
| **User Confidence** | PMs express confidence in recommendations | Semi-structured interviews (5 pilots) | No major concerns about bias/accuracy |
| **Executive Perception** | Division Head sees value in system | Executive feedback form | Positive sentiment ("valuable tool") |
| **Compliance Maturity** | All GDPR/AI Act gaps remediated | DPO sign-off + audit readiness checklist | Zero critical compliance gaps remain |
| **IT Readiness** | Operations team can manage system | Knowledge transfer assessment | IT lead confirms readiness to operate |
| **Data Quality** | Excel data is clean, consistent | Data validation audit | No missing/inconsistent fields block analysis |

---

#### **Decision Matrix: Greenlight vs. No-Go**

```
GREENLIGHT (Proceed to Phase 3) IF:
  ✅ Adoption ≥70% AND
  ✅ Accuracy ≥80% AND
  ✅ Uptime ≥95% AND
  ✅ Satisfaction ≥6/10 AND
  ✅ Zero critical compliance incidents AND
  ✅ Executive approval obtained

CONDITIONAL GREENLIGHT (Proceed with caveats) IF:
  ✅ Adoption ≥60% (marginal) → Plan additional training in Phase 3
  ✅ Accuracy 75-79% (concerning) → Refine Claude prompt before Phase 3
  ✅ Uptime 90-94% (low) → Investigate + patch infrastructure issues
  ⚠️ Satisfaction 5-6/10 (poor) → Redesign user experience; gather feedback
  ⚠️ One low-level compliance issue found → Fix before Phase 3 launch

NO-GO (Pause & Iterate) IF:
  ❌ Adoption <50% (users don't trust system)
     → Action: Hold stakeholder interviews; identify barriers; redesign training
  ❌ Accuracy <75% (recommendations unreliable)
     → Action: Claude prompt overhaul; human review layer added
  ❌ Uptime <90% (system unstable)
     → Action: Infrastructure audit; migrate to more reliable hosting if needed
  ❌ Satisfaction <5/10 (system rejected)
     → Action: Redesign; reconsider architecture
  ❌ Critical compliance breach found
     → Action: Halt; legal/DPO assessment; remediate before restart

TERMINATE (Project Killed) IF:
  ❌ Data breach occurs (GDPR violation)
  ❌ Major regulatory finding (AI Act non-compliance)
  ❌ Executive decision to cease (political/strategic)
```

---

### 4.2 Phase 3 (Full Deployment) Success Metrics

| Metric | Target | Timeline | Success Threshold |
|---|---|---|---|
| **Adoption at Scale** | >80% of 50+ staff use report weekly | Measure Nov 30 | >75% minimum |
| **Organizational Time Savings** | 300+ hours/year saved across org | Annualize from Phase 3 monthly data | Minimum 200 hours |
| **Executive Decision Impact** | ≥10 documented decisions influenced by AI | Track through Q4 | Qualitative + quantitative evidence |
| **Portfolio Risk Detection** | System flags ≥3 at-risk projects before crisis | Retrospective validation by Q1 2027 | Evidence of early intervention |
| **System Reliability** | 99.5%+ uptime (1 report max delayed) | Measure Sep-Nov | 99% minimum |
| **User Satisfaction** | >8/10 average rating | Monthly survey (Sep-Nov avg) | >7/10 minimum |
| **IT Operations Readiness** | IT team independently manages system | Post-handoff (by Nov 30) | IT lead certifies readiness |
| **Compliance Maturity** | Full compliance + audit-ready | DPO sign-off by Sep 30 | Zero open compliance gaps |
| **Cost per Report** | <€1/report | Operating cost ÷ 52 annual reports | <€2/report |

---

### 4.3 Year 2 Strategy Evaluation (January 2027)

**Decision Point:** After Phase 3 completion, decide on Year 2 direction (internal only vs. external expansion).

**Evaluation Criteria:**

| Question | Evidence for "Yes, Expand Externally" | Evidence for "No, Stay Internal" |
|---|---|---|
| **Is system working well internally?** | >80% adoption; >8/10 satisfaction; 99%+ uptime | <80% adoption; <7/10 satisfaction; uptime issues |
| **Is there external demand?** | ≥2 inbound inquiries from agencies/utilities | Zero external inquiries |
| **Can dena support it?** | Dedicated product/sales resource identified | No internal resources available |
| **Is there budget?** | €50K+ allocated for licensing/SaaS dev | No budget allocated |
| **Is leadership aligned?** | CIO/CFO approve Year 2 expansion plan | Leadership prefers internal-only |
| **Are compliance frameworks adequate?** | EU AI Act + GDPR mature; no blockers for external | Compliance framework under-developed for external use |

**Decision:**
- ✅ **EXPAND:** If ≥4/6 criteria met → Pursue Scenario B (licensing) + Scenario C (SaaS platform) development
- ⚠️ **CONDITIONAL:** If 3/6 criteria met → Expand to other dena divisions first; reassess external in 2028
- ❌ **STAY INTERNAL:** If <3/6 criteria met → Continue internal-only; system remains cost center

---

## PART 5: COMMERCIALISATION MODEL (RECOMMENDED)

### 5.1 Recommended Path: Hybrid Licensing + SaaS

**Short Version:**
1. **Year 1 (2026):** Internal tool only. Perfect internal execution; build case study.
2. **Year 2 (2027):** License to 1-2 federal agencies (validate demand; generate €10-20K revenue). Simultaneously develop SaaS platform.
3. **Year 3 (2028):** Launch SaaS commercially; scale to 5-10 customers; target €100K+ ARR.

---

### 5.2 Why This Model?

#### **Advantages**

| Advantage | Rationale |
|---|---|
| **Low Risk** | Licensing is low-risk; SaaS platform can be built in parallel without disrupting internal tool. |
| **Validates Demand** | Licensing pilot with federal agencies tests market appetite before major SaaS investment. |
| **Revenue in Year 2** | Quick win: €10-20K licensing revenue demonstrates monetisation without waiting for SaaS. |
| **Strategic Alignment** | Aligns with dena's mission (advancing energy transition ecosystem); not purely profit-driven. |
| **Builds Competency** | dena learns product management + customer support via licensing; prepares for SaaS. |
| **Scalability Path** | SaaS is inherently more scalable; licensing can be bridge to long-term platform. |

#### **Risks Mitigated**

| Risk | Mitigation |
|---|---|
| **"Market doesn't want this"** | Licensing pilot reveals demand; fail fast if no market. |
| **"Building SaaS is hard"** | Year 2 pilot validates product-market fit; reduces risk of wasted SaaS investment. |
| **"dena doesn't have product skills"** | Licensing requires minimal product ops; time to hire/train for SaaS. |
| **"Regulatory hurdles in external market"** | Licensing stays within Germany initially (simpler); SaaS can target EU with appropriate DPA/scoping. |

---

### 5.3 Licensing Path (Year 2-3)

#### **Target Customer: Federal Agency (e.g., Bundesministerium für Umwelt)**

**Fit:**
- Manages large infrastructure portfolio (similar to dena)
- Uses Excel for tracking (same format as dena)
- Under budget pressure (interested in efficiency)
- Compliant with German IT security standards (less friction)

**Value Proposition:**
- "Reduce portfolio reporting time by 75%; improve decision quality with AI-powered risk assessment."
- "Leverage dena's proven system; benefit from ongoing updates."
- "Fully compliant with GDPR and AI Act; pre-audited."

**Deal Structure:**
- Annual license: €2,000 + (€50 × # users)
- 1-year contract (auto-renew)
- Included: system access, 12 hours training, monthly support
- 3-year contract discount: 15%

**Customer Onboarding (8 weeks):**
- Week 1: Environment setup; data migration from partner's Excel
- Week 2-3: Customization (adjust column names, analysis focus)
- Week 4: User training (2x half-day sessions)
- Week 5-8: Pilot (4 reports delivered; feedback loop)

**Revenue Model:**
```
Year 2 (Pilot):
- 1 customer (federal agency, 40 users)
- €2,000 + (€50 × 40) = €4,000/year
- 2 more inbound pilots in discussion = potential €12,000 total if all sign

Year 3 (Growth):
- 5 customers (mix of agencies + utilities)
- Average €3,500 per customer
- Total: €17,500 licensing revenue
- Plus: €5,000 custom integration services
- Total: €22,500 Year 3 licensing revenue
```

**Why Licensing Works:**
- ✅ Low operational overhead (dena maintains 1 system; partners deploy copies)
- ✅ Proven in German gov/defense sector (common model)
- ✅ Lower regulatory risk than SaaS (data stays in partner's infrastructure)
- ✅ Achieves revenue without major product investment

---

### 5.4 SaaS Path (Year 3+)

#### **SaaS Vision: Multi-tenant Portfolio Intelligence Platform**

**Product:**
- Web-based (no Excel needed)
- Multi-tenant (separate data isolation for each customer)
- Advanced features: custom alerts, benchmarking vs. peers, API integrations, mobile app
- Roadmap: Predictive analytics, project scheduling, team collaboration

**Market:**
- Energy utilities (EON, RWE, Vattenfall) with 50-200 projects each
- Government agencies across EU
- Private equity / infrastructure funds
- TAM: [ASSUMPTION] €50M+ globally (energy sector alone)

**Pricing:**
```
Starter: €99/month (up to 10 projects)
Pro: €299/month (up to 50 projects; advanced analytics)
Enterprise: €999/month (unlimited; custom features; dedicated support)

Example: Utility company with 100 projects
- Enterprise tier: €999/month × 12 = €11,988/year
- 20-customer cohort = €240K ARR

Growth trajectory:
- Year 1 (2028): 3-5 customers; €50-80K ARR
- Year 2 (2029): 15-20 customers; €250-400K ARR
- Year 3 (2030): 50+ customers; €1M+ ARR
```

**Go-to-Market:**
- Sales: Freemium (Starter tier free for 14 days) + direct sales for Enterprise
- Channels: Energy trade shows, LinkedIn, industry analyst relations
- Partnerships: Cloud platforms (AWS, Azure); consulting firms (McKinsey, PWC)

**Why SaaS is Worth It:**
- ✅ Highly scalable (one system serves 100+ customers)
- ✅ Recurring revenue model (more valuable to investors/acquirers)
- ✅ Network effects (benchmarking improves as user base grows)
- ✅ Higher margins (cloud-native cost structure)
- ❌ Higher risk (requires significant investment, longer payback)

---

### 5.5 Commercialisation Timeline & Milestones

```
INTERNAL TOOL (2026)
↓
Deploy to dena IME
Build case study
Measure ROI
Validate user demand
↓
LICENSING PILOT (2027 Q1-Q2)
↓
License to 1-2 federal agencies
Achieve €10-20K revenue
Learn customer needs
↓
PARALLELIZATION (2027 Q2-Q4)
↓
Continue licensing (3-5 customers)      ← Generate €15-25K revenue
Develop SaaS platform architecture      ← Build for launch in 2028
Hire Product + Customer Success team    ← Scale operations
↓
SaaAS LAUNCH (2028 Q1)
↓
Release MVP (basic features)
Acquire first 3-5 customers
Target: €50-80K ARR
↓
SCALE (2028-2029+)
↓
Expand features (advanced analytics, APIs, mobile)
Reach 50+ customers
Target: €1M+ ARR
↓
EXIT / IPO / ACQUISITION (2030+)
↓
Potential acquirer: McKinsey, Accenture, SAP, energy utilities
Valuation: [ASSUMPTION] €50-100M (SaaS multiple of 5-10x ARR)
```

---

### 5.6 Decision Framework: Internal Only vs. Commercialise

**Year-End 2026 Decision Point (December 2026):**

| Question | Internal Only | Pursue Licensing | Pursue SaaS |
|---|---|---|---|
| **Is internal tool successful?** | Required | Required | Required |
| **Executive appetite for growth?** | No | Yes | Yes |
| **Resource availability?** | N/A | 1-2 FTE product/sales | 3-5 FTE product/sales/eng |
| **Budget available?** | N/A | €50K | €200K+ |
| **Risk tolerance** | Low | Medium | High |
| **Timeline to revenue** | N/A | 6 months (licensing) | 12-18 months (SaaS) |
| **Timeline to profitability** | Sunk cost (~€25K investment) | 1-2 years | 3-5 years |

**Decision Recommendation:**
- **If 2026 goes well + external inquiries received:** Pursue licensing in 2027 (low risk, quick revenue)
- **If licensing succeeds + executive supports growth:** Begin SaaS development in 2028 (hedge bets with licensing)
- **If 2026 underperforms internally:** Shelve external plans; internal tool only until 2029+

---

## PART 6: SUMMARY & NEXT STEPS

### 6.1 Phasing Overview

| Phase | Duration | Status | Investment | Key Outcome |
|---|---|---|---|---|
| **Phase 1: POC** | Apr-May 2026 | ✅ Complete | €4,290 | Proof technical/cost feasibility |
| **Phase 2: Pilot** | Jul-Aug 2026 | ⏳ Planned | €8,000 | Go/no-go decision for Phase 3 |
| **Phase 3: Full Deploy** | Sep-Nov 2026 | ⏳ Planned | €12,000 | System fully operational; 80%+ adoption |
| **Year 2: Strategic Review** | Dec 2026-Jan 2027 | ⏳ Planned | €0 (decision point) | Decide: internal only or commercialise |

**Total Year 1 Investment:** €24,290 (POC + Pilot + Deployment)  
**Expected Year 1 ROI:** €25K-30K (time savings + risk mitigation)  
**Payback Period:** 10-12 months

---

### 6.2 Critical Path & Dependencies

```
CRITICAL PATH (blocks Phase 3 if delayed):

┌─ Compliance Remediation (Jun 30)
│  ├─ Anthropic DPA ← blocking
│  ├─ Privacy Notices ← blocking
│  └─ Log Retention Policy ← blocking
│
├─ Phase 2 Evaluation (Aug 31)
│  ├─ Adoption metrics >70% ← blocking
│  ├─ Accuracy ≥80% ← blocking
│  └─ Executive approval ← blocking
│
└─ Phase 3 Deployment (Sep 1)
   ├─ Training materials ready ← blocking
   ├─ IT Ops onboarded ← blocking
   └─ Full user rollout ← blocking

All items must be complete before Phase 3 launch (Sep 1).
Slack: 2 weeks (if any item slips past deadline, Phase 3 delays 1 week per item).
```

---

### 6.3 Governance & Decision Authority

| Decision | Owner | Approval Authority | Timeline |
|---|---|---|---|
| **Proceed from Phase 1→2** | Sponsor | CIO + Division Head | June 30, 2026 |
| **Proceed from Phase 2→3** | Sponsor | Steering Committee (CFO, CIO, Compliance) | August 31, 2026 |
| **Year 2 Strategy (Internal vs. External)** | CIO + Strategy Lead | Executive Board | January 2027 |
| **SaaS Platform Investment** (if approved) | CFO | Executive Board + Board of Directors | Q2 2027 |

---

### 6.4 Next Immediate Actions (June 2026)

**By June 20, 2026:**
- [ ] Compliance review meeting (DPO, Legal, CISO) — finalize remediation plan
- [ ] Data quality audit — identify/fix Excel issues
- [ ] Pilot user selection — recruit 10 volunteer PMs

**By June 30, 2026:**
- [ ] Anthropic DPA signed
- [ ] Privacy notices drafted and distributed
- [ ] Training materials drafted (first cut)
- [ ] Phase 2 kickoff meeting scheduled (July 7)

**By July 7, 2026:**
- [ ] Pilot begins (report #1 generated and delivered)
- [ ] Weekly stakeholder debriefs start
- [ ] Feedback collection process in place

---

## CONCLUSION

The dena IME Weekly Portfolio Reporting System has a clear, phased path to operational success:

**2026 Goal:** Full internal operationalization (50+ users, 99%+ uptime, 80%+ adoption)

**2027-2028 Goal:** Validate commercial potential (license to 1-2 federal agencies; develop SaaS platform)

**2030+ Goal:** Establish dena as provider of AI-driven portfolio intelligence for energy sector (€1M+ ARR potential)

**Key Success Factors:**
1. ✅ Flawless Phase 2 execution (metrics, compliance, user feedback)
2. ✅ Strong Phase 3 rollout (training, adoption, IT handoff)
3. ✅ Executive commitment to growth agenda (resources, budget, vision)
4. ✅ Customer demand validation (external inquiries in 2026-2027)
5. ✅ Regulatory environment remains favorable (no major GDPR/AI Act changes)

**Investment Required:** €24K (Phase 1-3); €50K+ additional (Year 2 external expansion)

**Expected Returns:** €25K/year internal (time savings); €50-100K+/year external (licensing + SaaS, Years 2-3+)

---

**Document Prepared:** June 15, 2026  
**Next Review:** July 31, 2026 (post-Pilot evaluation)  
**Approvers:** CIO, CFO, Division Head, Compliance Officer  
**Strategic Owner:** [ASSUMPTION] dena Chief Innovation Officer or equivalent
