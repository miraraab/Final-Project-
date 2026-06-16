# EU AI Act Compliance Documentation
## dena IME Weekly Portfolio Reporting System

**Document Version:** 1.1
**Date:** June 2026
**Regulation:** EU Artificial Intelligence Act (EU 2024/1689)
**Compliance Assessment Date:** June 15, 2026
**System Name:** dena IME Weekly Report Automation
**Provider/Deployer:** dena (Deutsche Energie-Agentur) — see Section 1.3 for role classification
**Authority Having Jurisdiction:** Germany / Federal Ministry for Economic Affairs and Climate Action

---

## Part 1: Risk Classification

### 1.1 System Overview for Classification

**System Name:** dena IME Weekly Portfolio Reporting System
**Purpose:** Automated weekly analysis of portfolio data from 26 public energy transition projects; generation of structured management reports with risk flags.

**Key Characteristics:**
- Analyses Excel data (Project ID, Name, Budget, Spend, Milestones, Status, Escalation flags, Risk assessments)
- Uses Claude Sonnet (general-purpose AI model) via Anthropic API
- Generates structured JSON report with sections: Executive Summary, Projects at Risk, Actions Required, Budget Overview, Leadership Recommendations
- Flags projects as Red (immediate action needed), Amber (monitor), or Green (on track)
- Delivers report via HTML email to dena IME leadership and project managers
- **Human decision-making:** No autonomous decisions. All recommendations are advisory. Humans review report and make all final decisions about project funding, scope, and status.

**Data Subjects:**
- No processing of personal data about natural persons in the primary data flow (project metadata only: budget figures, timeline data, performance metrics)
- Email addresses of internal IME staff used for report distribution (see GDPR Documentation for treatment)

**Scope:** Internal organisational tool. Not exposed to public. Used only by dena IME staff.

---

### 1.2 Provider vs. Deployer Role Classification

> **Why this distinction matters:** The EU AI Act assigns different obligations to AI system *providers* (who develop and place systems on the market or into service) and *deployers* (who use systems developed by others in a professional context). Anthropic is the provider of Claude Sonnet as a general-purpose AI model. dena's role depends on the degree of integration and customisation it performs.

**Assessment:**

dena is classified as a **provider** of the dena IME Weekly Report Automation system because:

1. dena develops and operates the full system (reader, orchestration, scheduling, email delivery) — not merely using an off-the-shelf AI product
2. dena defines the system prompt, output structure, and integration logic — materially shaping AI behaviour
3. dena places the system into service within its own organisation for a specific intended purpose
4. Anthropic remains the provider of Claude Sonnet as the underlying general-purpose AI model, with its own separate obligations under the EU AI Act (GPAI obligations, Articles 53–55)

**Implication:** As provider of the integrated system, dena bears obligations for risk classification, technical documentation, transparency, and human oversight of the deployed system. Anthropic bears obligations for the underlying GPAI model. These are complementary, not conflicting.

---

### 1.3 Step-by-Step Risk Classification

#### Step 1: Is the System Prohibited?

Prohibited AI systems (Article 5, EU AI Act) include:
- Cognitive behavioural manipulation targeting vulnerable groups
- Social credit scoring
- Real-time biometric identification in public spaces
- Emotion recognition in law enforcement / workplace contexts
- Automated processing leading to unfavourable legal consequences without human intervention

**Analysis:**

The system does not manipulate cognitive behaviour, score individuals, process biometric data, make binding decisions, or create legal consequences for natural persons. All analysis targets organisational project entities, not people.

**Step 1 Conclusion: NOT PROHIBITED.**

---

#### Step 2: Is the System High-Risk (Annex III)?

High-Risk AI systems (Annex III) include: biometric identification, law enforcement, critical infrastructure safety components, migration and border control, administration of justice, employment screening, education, and creditworthiness assessment.

**Annex III Critical Infrastructure — Deeper Assessment:**

Annex III includes: *"AI systems intended to be used as safety components in the management and operation of critical infrastructure."*

**Does the dena IME system qualify?**

**No.** The decisive distinction is between *operational control* of infrastructure and *governance/portfolio management* of infrastructure projects:

| High-Risk (Annex III) | This System |
|---|---|
| SCADA system controlling power grid voltage | Portfolio reporting on energy transition project health |
| Autonomous load balancing in electrical networks | Budget burn rate analysis and milestone tracking |
| Automated turbine shut-off triggers | Weekly management report with advisory recommendations |
| Real-time demand-response algorithms | Monday 08:00 email to IME leadership |

dena IME manages energy transition project portfolios (funding, planning, policy) — not active power plants, grids, or real-time infrastructure systems. If the system fails completely, no infrastructure is affected; the worst case is a delayed management report.

**Analogy:** A strategic planning dashboard used by a hospital board does not become a "medical device AI" merely because the hospital operates safety-critical equipment. The system advises governance, not operations.

**Regulatory basis:** EU AI Act critical infrastructure language targets *operational* AI systems embedded in infrastructure control loops. Project management, financial dashboards, and planning tools consistently fall below this threshold in EU Commission guidance and comparable national frameworks (including BSI).

**All other Annex III categories:** Not applicable (no biometric processing, no law enforcement use, no employment screening, no creditworthiness assessment, no education context).

**Step 2 Conclusion: NOT HIGH-RISK (Annex III).**

---

#### Step 3: Is the System Limited-Risk?

Limited-Risk systems include AI systems with specific transparency obligations, particularly those interacting with natural persons in potentially consequential ways, and systems built on general-purpose AI models used in a deployment context.

**Assessment:**

The system qualifies as **Limited-Risk** based on:

1. **General-purpose AI model in deployment:** Uses Claude Sonnet (a GPAI model) in an organisational context where outputs inform consequential decisions (project funding, continuation, resource allocation)
2. **Decision support role:** Recommendations influence significant management decisions, warranting transparency obligations toward users
3. **Not minimal-risk:** The system is not a simple spam filter, grammar checker, or video game AI — its outputs feed directly into project governance decisions

**Step 3 Conclusion: LIMITED-RISK.**

---

#### Step 4: Classification Decision Matrix

| Characteristic | Assessment | Implication |
|---|---|---|
| Makes binding individual decisions | No — human decides | Not High-Risk |
| Processes biometric / facial data | No | Not High-Risk |
| Used in law enforcement | No | Not High-Risk |
| Controls critical infrastructure | No — advisory only | Not High-Risk |
| Impacts employment decisions | No — not hiring/firing | Not High-Risk |
| Affects creditworthiness / insurance | No | Not High-Risk |
| Uses general-purpose AI model (GPAI) | Yes — Claude Sonnet | Limited-Risk transparency obligations |
| Provides consequential decision support | Yes — advisory | Limited-Risk transparency obligations |
| Internal-only use | Yes | Lower risk profile |
| Human oversight by design | Yes — mandatory review loop | Mitigates risk |
| Full audit logging | Yes — dena_report.log | Mitigates risk |

---

### 1.4 Final Risk Classification

**FINAL VERDICT: LIMITED-RISK AI SYSTEM**

The system is classified as Limited-Risk under the EU AI Act. It falls outside prohibited (Article 5) and high-risk (Annex III) categories. Applicable obligations arise from the system's use of a general-purpose AI model in a deployment context with consequential decision support.

**Classification is unambiguous.** This is not a borderline case defaulting to a conservative position. The Annex III critical infrastructure exclusion is well-founded: the system advises on project governance, not infrastructure operation. No material doubt exists that would warrant High-Risk treatment.

---

## Part 2: Conformity Assessment Summary

### 2.1 System Description

**System Identifier:** dena IME Weekly Report Automation v1.1
**Provider Organisation:** Deutsche Energie-Agentur (dena)
**Intended Use:** Internal weekly portfolio management reporting for IME Division
**End-Users:** IME Division Head, Themengebietsleitung Bereichsentwicklung und -controlling, project managers, finance team
**Deployment:** Railway.app (cloud), triggered via APScheduler (cron: Monday 08:00 UTC)

**Input Data:**
- Excel file: `dena_IME_mock_dataset_v2.xlsx`, sheet: `CONSOLIDATED DASHBOARD`
- 26 rows (one per project): Project ID, Name, Funder, Budget (€), Spend YTD (€), Budget % Consumed, HR Utilisation (%), Milestone Status, Overall Status, Escalation Flag, Next Milestone, Key Risk

**Processing:**
1. openpyxl reads Excel rows (hardcoded values only — no cross-sheet formula references)
2. Structured data passed to Claude Sonnet API with system prompt
3. Claude returns structured JSON (not free text) for reliable downstream processing
4. JSON rendered as HTML email and delivered via Resend
5. PM conducts mandatory human review before distribution
6. All events logged to `dena_report.log`

**Output:**
- HTML-formatted email report with sections: Executive Summary, Immediate Actions, Projects at Risk, On-Track Projects, Budget Overview, Leadership Actions
- Every report includes mandatory disclaimer: *"This analysis is AI-generated using Claude Sonnet and reviewed by [PM name] before distribution. It is decision support, not a decision."*
- Archive copy stored locally

**No Autonomous Decisions:** The system does not terminate projects, reallocate budgets, escalate issues to third parties, send follow-up communications, trigger funding holds, or change project status in any system. All actions require explicit human decision-making.

---

### 2.2 Applicable Obligations

**Risk Class:** Limited-Risk AI System

> **Note on article references:** Specific article numbers for Limited-Risk obligations in the EU AI Act are subject to ongoing regulatory interpretation and national guidance (as of June 2026). The obligations below are described by content rather than by article number alone to avoid misattribution. Legal counsel should confirm final article mapping before regulatory submission. All references marked `[ASSUMPTION: article mapping]` where specific numbers are cited.

| Obligation | Content Requirement | Compliance Status |
|---|---|---|
| **Transparency — AI Disclosure** | Disclose that AI is involved in analysis; explain what it does and does not do | ✅ Mandatory disclaimer in every report |
| **Transparency — Limitations** | Communicate known limitations of AI output (hallucination risk, data dependency) | ✅ Limitations section in report design |
| **Human Oversight** | Ensure humans can understand, monitor, and override recommendations before consequences | ✅ Mandatory PM review before distribution |
| **Record-Keeping** | Maintain records of AI involvement, outputs, and decisions made | ✅ Full logging in dena_report.log |
| **Technical Documentation** | Maintain technical file documenting system design, data, performance, risk | ⚠️ In progress — outline in Part 3 |
| **Bias & Fairness Testing** | Test for bias in recommendations across project types and characteristics | ⚠️ Quarterly bias audit scheduled from Q3 2026 |
| **GPAI Model Documentation** | Reference provider's (Anthropic's) model documentation for underlying model | ⚠️ To be linked — Anthropic Claude model card |

---

### 2.3 Environmental Compliance (Green Software / SCI)

dena's mandate explicitly includes sustainability. The system is designed with minimal computational footprint:

- **Inference frequency:** 52 API calls per year (weekly batch, not continuous)
- **Token usage per run:** ~2,000 tokens (input + output), well within efficient range
- **Batch processing:** Single weekly run replaces continuous polling or on-demand queries
- **Model selection:** Claude Sonnet chosen for accuracy/efficiency balance; not an unnecessarily large model for the task
- **Carbon impact:** Negligible at 52 runs/year; dena can report near-zero AI-attributable carbon for this system

**SCI approximation (Green Software Foundation framework):**
`SCI = (O + M) per R` where R = one weekly report. Operational energy (O) per inference is minimal; embodied carbon (M) is amortised across millions of Anthropic API users. Per-report carbon footprint is estimated in the gram CO₂e range — orders of magnitude below the manual alternative (analyst workstation hours).

**Conclusion:** System is consistent with dena's sustainability commitments and demonstrates AI deployment can reduce, not increase, organisational carbon footprint through automation of energy-intensive manual work.

---

### 2.4 Conformity Assessment Conclusion

**The dena IME Weekly Report Automation system is a Limited-Risk AI system under the EU AI Act.**

| Assessment Dimension | Result |
|---|---|
| Prohibited (Article 5) | ✅ Not applicable |
| High-Risk (Annex III) | ✅ Not applicable — confirmed by operational vs. governance distinction |
| Risk Classification | **Limited-Risk** |
| Core obligations identified | ✅ Transparency, human oversight, record-keeping, technical documentation |
| Transparency implemented | ✅ Mandatory disclaimer in every report |
| Human oversight implemented | ✅ Mandatory PM review before distribution |
| Record-keeping implemented | ✅ Full logging operational |
| Technical documentation | ⚠️ Outline complete; full file by August 31, 2026 |
| Bias audit | ⚠️ Scheduled Q3 2026 |

**Assessed By:** [ASSUMPTION] dena Compliance Officer + Technical Lead
**Review Cycle:** Annual, or upon material system changes
**Next Review:** Q4 2026

---

## Part 3: Technical Documentation Outline

### 3.1 Regulatory Basis

Article 11 of the EU AI Act `[ASSUMPTION: article mapping]` mandates that providers maintain technical documentation covering system description, development methodology, data governance, performance metrics, human oversight, and post-deployment monitoring. The outline below constitutes the Table of Contents for dena's full technical file.

---

### 3.2 Technical File — Table of Contents

```
DENA IME WEEKLY REPORT AUTOMATION — TECHNICAL DOCUMENTATION FILE
Version 1.1 | Target Completion: August 31, 2026
================================================================

1. EXECUTIVE SUMMARY
   1.1 System Identification (name, version, provider, classification)
   1.2 System Scope (intended use, users, environment)
   1.3 Conformity Summary (risk class, obligations, status)

2. SYSTEM DESCRIPTION & INTENDED PURPOSE
   2.1 Purpose Statement
   2.2 Technical Architecture (Reader → API → Generator → Human Review → Sender)
   2.3 Functional Specifications (input schema, output structure, processing rules)
   2.4 Operational Scope (deployment, access control, geography)

3. DEVELOPMENT & METHODOLOGY
   3.1 AI Model Selection (Claude Sonnet; rationale; alternatives considered)
   3.2 System Prompt Design (full prompt text; engineering rationale; risk mitigations)
   3.3 Agentic Pattern Description (Plan → Act → Observe → Iterate cycle)
   3.4 Development Process (requirements, design, coding, testing phases)
   3.5 Timeline & Milestones

4. MODEL INFORMATION & TRAINING DATA
   4.1 Training Data (Claude Sonnet: general internet corpus — Anthropic documentation)
   4.2 Model Characteristics (architecture, capabilities, knowledge cutoff, limitations)
   4.3 Model Card Reference (link to Anthropic's official Claude Sonnet documentation)
   4.4 No Fine-Tuning (base model used; no custom training by dena)

5. PERFORMANCE METRICS & EVALUATION
   5.1 Validation Approach (weekly human assessment; mock data testing)
   5.2 Performance Results (accuracy, relevance, hallucination rate — target: <1/month)
   5.3 Known Limitations (hallucination risk; Excel data quality dependency; no real-time data)
   5.4 Error Analysis (post-launch incident log; root cause; corrective actions)

6. HUMAN OVERSIGHT & CONTROL
   6.1 Human-in-the-Loop Design (mandatory PM review before distribution)
   6.2 Decision Authority (Division Head + PMs + Finance — not system)
   6.3 Override Capability (any recommendation can be disregarded; no system consequences)
   6.4 User Training (README; stakeholder briefing; annual refresher)
   6.5 Incident Response (error reporting; corrective action; communication protocol)
   6.6 Automation Bias Safeguards (acceptance rate monitoring; >80% triggers review)

7. DATA MANAGEMENT & PROCESSING
   7.1 Input Data Schema (Excel column definitions; validation rules)
   7.2 Data Processing (cleaning; transformation; no cross-sheet formula dependency)
   7.3 Data Retention (log retention period; report archive policy)
   7.4 Data Security (encryption in transit; access control; no PII in primary flow)
   7.5 Data Minimisation (only project metadata; email addresses in distribution list only)

8. RISK ASSESSMENT & MITIGATION
   8.1 Risk Register (reference: 02_roi_risk_assessment.md — 8 risks assessed)
   8.2 Mitigation Strategies (per risk category)
   8.3 Residual Risk Acceptance (approved by management)

9. QUALITY ASSURANCE & TESTING
   9.1 Test Strategy (unit, integration, system, user acceptance)
   9.2 Test Cases (normal operation; edge cases; error scenarios)
   9.3 Test Results (pass/fail; bug log; resolution)
   9.4 Regression Testing (schedule; approach)

10. POST-DEPLOYMENT MONITORING
    10.1 KPI Framework (uptime, accuracy, satisfaction — reference: 01_use_case_definition.md)
    10.2 Monitoring Tools (Railway logs; dena_report.log; Resend delivery logs)
    10.3 Feedback Loop (quarterly stakeholder survey; issue tracking)
    10.4 Continuous Improvement (prompt tuning; model updates; change control)
    10.5 Sunset Plan (review criteria; decommissioning process; data handling)

11. ALGORITHM TRANSPARENCY & EXPLAINABILITY
    11.1 System Logic (data flow pseudocode; risk flagging rules; calculation methods)
    11.2 Claude API Behaviour (system prompt; structured JSON output; known quirks)
    11.3 Explainability for Users (how recommendations trace to input data)
    11.4 Limitations of Explainability (LLM black-box nature; structural transparency as mitigation)

12. COMPLIANCE & REGULATORY ALIGNMENT
    12.1 EU AI Act (obligations per risk class; implementation status)
    12.2 GDPR (reference: 04_gdpr_documentation.md)
    12.3 IT-Sicherheitsgesetz (BSI compliance assessment; audit schedule)
    12.4 Green Software / SCI (environmental impact assessment — see Part 2.3)

13. CHANGE MANAGEMENT & VERSION CONTROL
    13.1 Change Log (version history; approvals)
    13.2 Version Control (repository; branching; code review; deployment process)
    13.3 Rollback Procedures (revert to previous version; fallback to manual process)

14. EXTERNAL DEPENDENCIES
    14.1 Claude API / Anthropic (version; SLA; security certifications; pricing)
    14.2 Resend Email Service (API version; reliability; data handling)
    14.3 Railway Hosting (plan; SLA; data residency)
    14.4 Python Libraries (full dependency list; version pinning; licence compliance)

15. GLOSSARY & REFERENCES
    15.1 Terminology (AI system; GPAI; high-risk; limited-risk; LLM; hallucination; SCI)
    15.2 References (EU AI Act; Anthropic documentation; BSI guidance; related documents)
    15.3 Appendices
        A: Full System Prompt (complete text)
        B: Sample Report Output (anonymised)
        C: Data Schema (Excel column definitions)
        D: GDPR Data Processing Agreements (Anthropic; Resend)
        E: BSI Security Assessment (when available)
        F: Claude Sonnet Model Card (Anthropic reference)
        G: Bias Audit Results (quarterly, from Q3 2026)
        H: User Training Materials
```

---

### 3.3 Documentation Completion Plan

| Section | Owner | Deadline | Status |
|---|---|---|---|
| 1–2 (Overview & Architecture) | Technical Lead | June 30, 2026 | In progress |
| 3–4 (Development & Model) | Technical Lead | July 15, 2026 | Planned |
| 5 (Performance) | QA + User Feedback | August 15, 2026 | Planned |
| 6 (Human Oversight) | Project Sponsor | July 1, 2026 | Planned |
| 7 (Data Management) | IT Security + DPO | July 31, 2026 | Planned |
| 8 (Risk Assessment) | Project Lead | July 15, 2026 | Reference to ROI doc |
| 9 (Testing) | QA Team | July 31, 2026 | Planned |
| 10 (Monitoring) | Operations | August 31, 2026 | Planned |
| 11–15 (Compliance, Dependencies, References) | Compliance Officer | August 31, 2026 | Planned |

**Estimated effort:** [ASSUMPTION] 60–80 hours total
**Target completion:** August 31, 2026

---

### 3.4 Priority Documentation Artefacts

**High-Priority (required for core compliance):**
1. ✅ System Prompt — full text of instructions given to Claude
2. ✅ Data Schema — Excel column definitions and validation rules
3. ⚠️ GDPR Data Processing Agreement with Anthropic — template exists; requires signing
4. ⚠️ Bias Audit Process & Schedule — quarterly, starting Q3 2026
5. ⚠️ User Training Materials — Division Head, PMs, Finance team
6. ⚠️ Incident Response Procedure — error reporting and escalation process

**Medium-Priority (good practice):**
7. Sample Report Output (anonymised real example)
8. Claude Sonnet Model Card reference (Anthropic official documentation)
9. BSI Security Assessment results
10. Performance Metrics Baseline (pre-launch vs. post-launch comparison)

**Lower-Priority (supporting documentation):**
11. Change Log & Version History
12. Full Glossary
13. Sunset & Obsolescence Plan

---

## Part 4: Summary & Compliance Roadmap

### 4.1 Risk Classification Summary

| Dimension | Result | Rationale |
|---|---|---|
| **Final Risk Class** | **Limited-Risk** | GPAI model in deployment; consequential decision support; no autonomous decisions; internal use |
| Prohibited (Article 5) | Not applicable | No manipulation, social scoring, biometric processing, or autonomous legal consequences |
| High-Risk (Annex III) | Not applicable | Governance/advisory tool, not operational infrastructure control; no employment, biometric, or justice context |
| Annex III (Critical Infrastructure) | Excluded | System advises on project portfolios; does not operate, control, or manage infrastructure systems |

---

### 4.2 Compliance Roadmap (2026–2027)

**Phase 1: Classification & Documentation (June 2026)** — In Progress
- [x] Risk classification assessment (this document)
- [x] Provider/deployer role defined
- [x] Applicable obligations identified
- [x] Technical documentation outline complete
- [ ] Compliance activities scheduled

**Phase 2: Implementation & Documentation (July–August 2026)**
- [ ] Full technical file (Sections 1–15) completed
- [ ] Transparency disclosures implemented in all reports (by July 1)
- [ ] Formal human oversight process documented and operational (by June 30)
- [ ] GDPR DPA with Anthropic and Resend signed
- [ ] Audit logging confirmed operational

**Phase 3: Monitoring & Testing (September–December 2026)**
- [ ] First bias audit conducted (Q3)
- [ ] Performance metrics baseline established
- [ ] Stakeholder satisfaction survey completed
- [ ] Error recovery procedures tested
- [ ] Incident log reviewed

**Phase 4: Compliance Validation (January 2027)**
- [ ] Full technical file reviewed and signed off by Compliance Officer
- [ ] Internal compliance audit completed
- [ ] External audit readiness confirmed
- [ ] Annual risk reclassification review

---

### 4.3 Ongoing Compliance Obligations Summary

| Obligation | Requirement | Implementation | Schedule |
|---|---|---|---|
| AI Disclosure | Disclose AI involvement in every report | ✅ Mandatory disclaimer in report footer | Operational from launch |
| Capability & Limitations | Communicate what AI can and cannot assess | ✅ Limitations section in report design | Operational from launch |
| Human Oversight | Humans review and can override all recommendations | ✅ Mandatory PM review before distribution | Operational from launch |
| Record-Keeping | Maintain logs of AI outputs and post-report decisions | ✅ dena_report.log operational | Operational from launch |
| Technical Documentation | Complete technical file per Article 11 structure | ⚠️ Outline complete; full file in progress | August 31, 2026 |
| Bias Testing | Quarterly bias audit across project characteristics | ⚠️ Scheduled Q3 2026 | From Q3 2026 |
| GPAI Model Documentation | Reference Anthropic's Claude Sonnet model card | ⚠️ To be linked | July 2026 |

---

### 4.4 Assumptions & Caveats

- **[ASSUMPTION] EU AI Act article mapping:** Specific article numbers cited in this document are based on available guidance as of June 2026. The EU AI Act's implementing regulations and national guidance are still developing. Legal counsel should confirm final article mapping before any regulatory submission. Content-level obligations are well-established; precise article attribution may require revision.
- **[ASSUMPTION] Annex III exclusion:** Based on current EU Commission guidance distinguishing operational control from governance advisory tools. If future regulatory guidance narrows this distinction or dena's system scope changes to include real-time operational elements, reclassification to High-Risk must be triggered immediately.
- **[ASSUMPTION] Vendor compliance:** Assumes Anthropic, Resend, and Railway maintain current security certifications. Vendor compliance status is reviewed quarterly per the risk governance schedule.

---

## Conclusion

The **dena IME Weekly Portfolio Reporting System is a Limited-Risk AI system** under the EU AI Act.

The classification is unambiguous: the system advises on project governance, does not control infrastructure, processes no biometric data, makes no binding decisions, and is used only by internal dena staff. The use of Claude Sonnet (a general-purpose AI model) in a consequential decision-support role generates transparency and oversight obligations — all of which are implemented or scheduled.

**Key compliance actions (2026):**
1. Complete technical documentation file — by August 31, 2026
2. Transparency disclosures in all reports — operational from launch
3. Formal human oversight process documented — by June 30, 2026
4. GDPR DPAs signed with Anthropic and Resend — by July 2026
5. Quarterly bias audits — from Q3 2026
6. Annual reclassification review — January 2027

**Expected compliance status:** Fully compliant with EU AI Act Limited-Risk obligations by September 2026.

---

*Version 1.1 · Prepared June 15, 2026 · Next Review: Q4 2026 or upon material system changes · Escalation: dena CISO / Compliance Officer*