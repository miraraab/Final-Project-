# GDPR Documentation
## dena IME Weekly Portfolio Reporting System

**Document Version:** 1.1
**Date:** June 2026
**Regulation:** EU General Data Protection Regulation (GDPR / EU 2016/679)
**Controller:** Deutsche Energie-Agentur (dena), Berlin, Germany
**Division:** Industrie, Mobilität, Energieeffizienz (IME)
**Data Protection Officer (DPO):** [ASSUMPTION] dena appoints DPO as per Article 37(1)(b) (public authority)
**DPO Contact:** [ASSUMPTION] dpo@dena.de
**System:** dena IME Weekly Report Automation
**Assessment Date:** June 15, 2026

---

## Part 1: Data Inventory

### 1.1 Overview of Personal Data Processing

**Processing Activity:** Automated weekly portfolio analysis and report generation for internal management purposes.

**Data Controller:** Deutsche Energie-Agentur (dena), Chausseestraße 128a, 10115 Berlin, Germany
**Processing Purpose:** Portfolio health monitoring, project risk assessment, management decision support
**Data Subjects:** dena employees (report recipients), project managers (data referenced in input)
**Processing Frequency:** Weekly (every Monday at 08:00 UTC)
**Data Retention:** Logs kept for [ASSUMPTION] 12 months; reports archived per organisational record-keeping policy

---

### 1.2 Detailed Data Inventory

#### Category A: Personal Data in Input (Excel File)

| Data Type | Source | Scope | Retention | Necessity | Risk Level |
|---|---|---|---|---|---|
| Employee Names (Project Managers) | Project assignment column | Names of up to 26 PMs linked to project assignments | [ASSUMPTION] 12 months | Necessary to contextualise project performance and accountability | Medium |
| HR Utilisation Data | Column: HR Utilisation (%) | Percentage of team capacity per project (project-level aggregate, not individual) | [ASSUMPTION] 12 months | Necessary for resource constraint and feasibility assessment | Low–Medium |
| Budget Figures | Columns: Budget (€), Spend YTD (€), Budget % | Project budget amounts (organisational financial data, not individual salaries) | [ASSUMPTION] 12 months | Necessary for financial assessment | Low (not personal) |
| Project Risk Data | Column: Key Risk (text field) | Free-text risk descriptions; may reference individual performance or team challenges | [ASSUMPTION] 12 months | Necessary for risk assessment | Medium |

**Analysis:**
- Budget and spend figures are organisational data, not personal data
- PM names linked to projects constitute personal data (identified individuals responsible for projects)
- "Key Risk" field may contain personal references (e.g., "Project at risk due to PM's departure") — flagged for governance control and anonymisation

---

#### Category B: Personal Data in Processing (Claude API)

| Data Element | Processing | Retention | Note |
|---|---|---|---|
| Project names + PM names | Sent to Claude API for analysis | [ASSUMPTION] 30 days per Anthropic SLA | Data crosses to US (Anthropic/AWS) |
| Budget/spend/utilisation metrics | Claude analyses financial patterns | Per SLA | Linked to project name; may indirectly identify PM |
| Risk descriptions (text) | Claude reads and synthesises | Per SLA | May contain personal references; anonymisation required before transmission |
| Report generation metadata | Timestamps, API request IDs logged locally | [ASSUMPTION] 12 months | Audit trail; not sensitive |

**Analysis:**
- Data is transmitted to Anthropic's US-based servers — primary GDPR risk (addressed in DPIA and Part 5)
- Risk descriptions must be reviewed for personal identifiers before transmission
- Batch processing model (52 API calls/year) minimises the volume of personal data transmitted to Anthropic — deliberate design decision to reduce data exposure

---

#### Category C: Personal Data in Output (Email Reports)

| Data Element | Recipients | Retention | Risk |
|---|---|---|---|
| Project names + performance flags | IME Division Head, PMs, Finance (internal only) | [ASSUMPTION] Indefinite (organisational records) | Distribution limited to authorised internal users |
| Aggregated risk assessment | Internal only | [ASSUMPTION] Indefinite | No individual performance scores; project-level only |
| PM names (if mentioned in report) | Internal only | [ASSUMPTION] Indefinite | Report may reference PM names in context |
| Budget details | Internal only | [ASSUMPTION] Indefinite | Organisational financial data; not personal |

**Analysis:**
- Distribution is strictly internal; no external sharing
- No individual performance ratings attached to employees
- Project names may implicitly identify individuals; necessary for decision-making and proportionate

---

#### Category D: Personal Data in System Logs

| Log Type | Data Contained | Retention | Access Control |
|---|---|---|---|
| dena_report.log | Timestamp, success/failure, API metadata, email delivery log | [ASSUMPTION] 12 months | IT staff + DPO only |
| Email delivery logs (Resend) | Recipient email addresses, delivery status, timestamp | [ASSUMPTION] Per Resend retention — to be verified in DPA | Resend (US) + dena IT |
| Claude API call logs | Request timestamp, token count, model used, response length | [ASSUMPTION] 30 days per Anthropic SLA | Anthropic (US) + dena IT |
| Railway hosting logs | Application error messages, system performance data | [ASSUMPTION] Per Railway retention — to be verified in DPA | Railway (US) + dena IT |

**Analysis:**
- Email addresses appear in logs (personal data)
- Logs stored across multiple US-based providers (international transfer risk)
- Retention periods for Resend and Railway logs not yet formally defined — gap identified (GAP-7)

---

### 1.3 Data Inventory Summary

| Category | Data Type | Subjects | Retention | Legal Basis |
|---|---|---|---|---|
| Input | PM names + project data | 26 PMs | 12 months | Art. 6(1)(e) |
| Input | Budget/spend data | N/A (org data) | 12 months | Art. 6(1)(e) |
| Input | Risk descriptions | Indirect (may mention PMs) | 12 months | Art. 6(1)(e) |
| Processing | API request payloads (Anthropic) | Same as input | 30 days (Anthropic SLA) | Art. 6(1)(e) + Art. 44 SCCs |
| Output | Report (names + flags) | ~10 internal recipients | Indefinite | Art. 6(1)(e) |
| Logs | Email addresses + metadata | ~10 recipients + ops staff | 12 months | Art. 6(1)(e) |

---

## Part 2: Legal Basis

### 2.1 Primary Legal Basis: Article 6(1)(e) — Public Task

**Text:** "Processing is necessary for the performance of a task carried out in the public interest or in the exercise of official authority vested in the controller."

| Element | Evidence |
|---|---|
| Public Authority | dena is a federal energy agency operating under German public law |
| Public Interest | Energy transition (Energiewende) is explicitly mandated; portfolio management is core to dena's federal mandate |
| Official Authority | dena exercises official authority in managing energy transition projects on behalf of the Federal Ministry for Economic Affairs and Climate Action |
| Necessity | Portfolio monitoring is necessary to fulfil governance obligations; AI system reduces manual effort while maintaining oversight |
| No Consent Required | Art. 6(1)(e) does not require data subject consent |

**Conclusion:** Art. 6(1)(e) is the correct and primary legal basis. Processing is lawful.

---

### 2.2 Secondary Legal Basis: Article 6(1)(f) — Legitimate Interest (Fallback)

Available as fallback if Art. 6(1)(e) is challenged. dena's legitimate interest (efficient portfolio management, early risk detection, cost reduction) is not overridden by data subjects' interests, given the limited scope of processing and internal-only distribution.

---

### 2.3 Legal Basis by Processing Activity

| Processing Activity | Legal Basis | Justification |
|---|---|---|
| Reading project data from Excel | Art. 6(1)(e) | Necessary for portfolio management |
| Transmitting data to Claude API | Art. 6(1)(e) + Art. 44 (SCCs) | Necessary for analysis; transfer governed by SCCs |
| Generating and emailing reports | Art. 6(1)(e) | Necessary for decision-making and governance |
| Logging system events | Art. 6(1)(e) | Necessary for audit trail and compliance |
| Storing emails in archive | Art. 6(1)(e) | Necessary for organisational record-keeping |

---

### 2.4 Lawfulness Assessment

Processing is lawful under GDPR subject to the following conditions:

1. **Legal Basis Present** — Art. 6(1)(e) clearly applies
2. **Purpose Limitation** — Data used only for portfolio management; not repurposed for individual employee performance evaluation
3. **Data Minimisation** — Only necessary project metadata extracted; no personal financial, health, or sensitive data
4. **Storage Limitation** — Retention periods defined for primary data (12 months); vendor retention to be confirmed via DPA
5. **Transparency** — Privacy notices to be distributed to data subjects (GAP-5)
6. **Third-Country Transfers** — Governed by SCCs with Anthropic, Resend, and Railway (see Part 5)

---

## Part 3: Data Protection Impact Assessment (DPIA)

### 3.1 Scope & Triggers

**DPIA Triggers Present:**
- Systematic transfer to third country without adequacy decision (US — Anthropic, Resend, Railway)
- Automated processing informing significant management decisions (project funding, continuation)
- [ASSUMPTION] Under 5,000 regular data subjects (26 PMs + ~10 recipients); BfDI notification likely not required — to be confirmed

**Highest-Risk Processing Activity:** Transmission of personal data to Anthropic (Claude API) in the United States.

**DPIA Conducted By:** [ASSUMPTION] dena DPO + IT Security + Legal Counsel
**Date:** June 15, 2026

---

### 3.2 Necessity & Proportionality

**Is processing necessary?**
Yes. Portfolio analysis could theoretically be performed manually (7.5 hrs/week), but automated analysis is the chosen means for the public task. The US border crossing is a deliberate efficiency trade-off: Anthropic's Claude Sonnet is selected for accuracy. An on-premises LLM (e.g., Llama) would avoid the transfer but at significantly lower output quality.

**Is processing proportionate?**

| Factor | Assessment |
|---|---|
| Sensitive data? | No — project assignment is routine organisational data; no health, criminal, or biometric data |
| Intrusion on privacy | Low — PMs expect their project assignment to be recorded and discussed internally |
| Safeguards in place | SCCs, data minimisation, access controls, retention limits |
| Alternatives considered | On-premises LLM assessed; rejected on quality grounds; reviewed annually |

**Conclusion:** Processing is necessary and proportionate in relation to the public task.

---

### 3.3 Identified Risks

#### Risk 1 — Inadequate Third-Country Safeguards (US Transfer)

| Dimension | Detail |
|---|---|
| Description | Post-Schrems II, SCCs with US vendors are insufficient standing alone. US government has broad surveillance powers (Executive Order 12333, CLOUD Act). Risk: US government compels Anthropic to disclose data without dena's knowledge. |
| Likelihood | 2/5 — Low. Targeting routine portfolio data of a German public agency is highly unlikely. |
| Impact | 3/5 — Unauthorised disclosure of project data; potential reputational damage; compliance violation. |
| Risk Score | 6/25 (Manageable) |
| Mitigation | Data minimisation before transmission; enhanced DPA with supplementary Schrems II clauses; annual review of US regulatory landscape. |

---

#### Risk 2 — Transparency Gap (Data Subject Awareness)

| Dimension | Detail |
|---|---|
| Description | PMs may not know their project data is transmitted to Anthropic (US) for AI analysis. Art. 14 GDPR requires transparency for data not collected directly from data subjects. |
| Likelihood | 4/5 — High. No notification mechanism currently in place. |
| Impact | 3/5 — Data subject right violation; regulatory risk; erosion of trust. |
| Risk Score | 12/25 (Medium) |
| Mitigation | Privacy Notice (Art. 14) to be distributed to all PMs before next production report (GAP-5). |

---

#### Risk 3 — Sub-Processor Visibility (Anthropic)

| Dimension | Detail |
|---|---|
| Description | Anthropic uses sub-processors (AWS, contractors). dena has no visibility into who can access data. |
| Likelihood | 3/5 — Common practice for cloud vendors. |
| Impact | 3/5 — Loss of control over data; wider exposure surface. |
| Risk Score | 9/25 (Manageable) |
| Mitigation | Enhanced DPA requiring sub-processor list; notification clause for changes; SOC 2 audit reliance. |

---

#### Risk 4 — Retention Ambiguity

| Dimension | Detail |
|---|---|
| Description | Anthropic's retention policy not explicit in current SLA. Risk of data retained beyond 30 days or used for model training. |
| Likelihood | 3/5 — Ambiguous SLA language. |
| Impact | 3/5 — Unauthorised retention violates Art. 5(1)(e) storage limitation. |
| Risk Score | 9/25 (Manageable) |
| Mitigation | DPA must include explicit deletion commitment: "all personal data deleted within 30 days of processing; no retention for model training." |

---

#### Risk 5 — Identifiable Risk Descriptions

| Dimension | Detail |
|---|---|
| Description | Excel "Key Risk" field may contain personal references ("Project at risk due to PM's pending retirement"). Transmitting to Anthropic exposes PMs indirectly. |
| Likelihood | 3/5 — Depends on data entry practices; no governance currently in place. |
| Impact | 3/5 — Exposure of personal opinions or performance issues. |
| Risk Score | 9/25 (Manageable) |
| Mitigation | Data entry governance: instructions prohibiting personal references in Key Risk field. Validation step before API transmission. Auto-scan for personal names. |

---

#### Risk 6 — De Facto Automated Decision-Making (Art. 22 Risk)

| Dimension | Detail |
|---|---|
| Description | Art. 22 does not formally apply (humans make all decisions). However, if the Division Head routinely accepts AI recommendations without independent review, the system de facto becomes an automated decision-maker — and the Art. 22 exclusion would no longer hold. |
| Likelihood | 2/5 — Automation bias is well-documented; risk is real even if formal Art. 22 threshold is not met. |
| Impact | 3/5 — Unfair treatment of PMs or projects; legal risk if bias discovered. |
| Risk Score | 6/25 (Manageable) |
| Mitigation | Mandatory review checklist for Division Head. AI recommendation acceptance rate monitored quarterly; if acceptance rate exceeds 80% without documented independent reasoning, the human oversight process is strengthened. This control ensures Art. 22 exclusion remains valid in practice, not just in design. |

---

### 3.4 Mitigation Summary

| Risk | Initial Score | Mitigation | Residual Score | Acceptable? |
|---|---|---|---|---|
| 1 — US Transfer Safeguards | 6 | Data minimisation + enhanced DPA + annual review | 4 | ✅ Yes |
| 2 — Transparency Gap | 12 | Privacy Notice (Art. 14) distributed before production | 6 | ✅ Yes |
| 3 — Sub-Processor Visibility | 9 | DPA sub-processor list + notification clause | 5 | ✅ Yes |
| 4 — Retention Ambiguity | 9 | Explicit deletion clause in DPA | 5 | ✅ Yes |
| 5 — Identifiable Risk Descriptions | 9 | Data entry governance + pre-transmission validation | 4 | ✅ Yes |
| 6 — De Facto Automation (Art. 22) | 6 | Acceptance rate monitoring + review checklist | 3 | ✅ Yes |

---

### 3.5 DPIA Conclusion

**Overall Risk:** Medium — manageable with identified mitigations.

**Recommendation:** Processing may proceed, subject to implementation of all critical mitigations by June 30, 2026. All residual risks are within acceptable range. No prior consultation with BfDI required at current data subject volume ([ASSUMPTION] — confirm with DPO).

---

## Part 4: Data Subject Rights

### 4.1 Rights Overview

| Right | Article | Applies? | Implementation | SLA |
|---|---|---|---|---|
| Right of Access | 15 | ✅ Yes | Provide copy of personal data and processing information | 30 days |
| Right to Rectification | 16 | ✅ Yes | Correct inaccurate data (e.g., wrong project assignment) | 30 days |
| Right to Erasure | 17 | ⚠️ Limited | Art. 6(1)(e) exemption likely applies for active project records; logs deleted after 12 months | 30 days |
| Right to Restrict Processing | 18 | ✅ Yes | Suspend processing of specific PM's data pending review | 30 days |
| Right to Data Portability | 20 | ❌ Exempt | Art. 20 does not apply to processing under Art. 6(1)(e) | N/A |
| Right to Object | 21 | ⚠️ Limited | PM may object on personal grounds; processing continues unless compelling circumstances | 30 days |
| Rights Re: Automated Decisions | 22 | ❌ Not applicable | Humans make all decisions; AI output is advisory only — Art. 22 exclusion maintained through acceptance rate monitoring | N/A |

**Note on Art. 22:** The Art. 22 exclusion depends on humans genuinely making independent decisions, not rubber-stamping AI recommendations. dena's acceptance rate monitoring (see DPIA Risk 6) ensures this exclusion remains valid in practice.

---

### 4.2 Key Rights in Detail

**Right of Access (Art. 15):**
Request to dpo@dena.de. DPO provides: copy of all personal data held, processing purposes, legal basis, recipients (including Anthropic, Resend, Railway), retention periods, and data subject rights. Note: data already deleted at Anthropic after 30 days cannot be retrieved.

**Right to Rectification (Art. 16):**
PM reports inaccuracy → DPO corrects Excel file → next report includes corrected data. Anthropic data already processed; cannot be retroactively corrected, but next transmission will be correct.

**Right to Erasure (Art. 17):**
Art. 6(1)(e) processing for public task: erasure exemption applies for active project records (audit trail cannot be destroyed). Logs containing email addresses: deleted after 12-month retention period. Archived reports: PM name can be pseudonymised upon request without destroying project record integrity.

**Right to Restrict Processing (Art. 18):**
PM's project data can be temporarily excluded from analysis pending dispute resolution. Cannot "un-send" data already at Anthropic; retroactive deletion request can be submitted to Anthropic via DPA mechanism.

**Right to Object (Art. 21):**
Processing under Art. 6(1)(e) continues unless PM demonstrates compelling personal circumstances (e.g., demonstrated discrimination linked to AI analysis). Objection noted and assessed by DPO within 30 days.

**Right to Data Portability (Art. 20):**
Not applicable under Art. 6(1)(e). dena will explain exemption and offer Art. 15 access as alternative.

---

### 4.3 Rights Infrastructure Gaps

| Right | Process Documented | Responsible Officer | Status |
|---|---|---|---|
| Access (Art. 15) | ❌ | DPO | GAP-6 — template needed |
| Rectification (Art. 16) | ❌ | DPO + IT | GAP-6 |
| Erasure (Art. 17) | ❌ | DPO + Legal | GAP-6 — exemption decision template needed |
| Restrict (Art. 18) | ❌ | DPO + IT | GAP-6 |
| Object (Art. 21) | ❌ | DPO + Legal | GAP-6 |

All gaps addressed under GAP-6 remediation (templates + training by July 31, 2026).

---

## Part 5: Third-Party Transfers & Safeguards

### 5.1 Recipient Overview

| Recipient | Location | Data Sent | Legal Basis | Safeguard | DPA Status |
|---|---|---|---|---|---|
| Anthropic Inc. (Claude API) | USA (AWS) | Project names, PM names, budget/metrics, risk descriptions | Art. 44 + SCCs | DPA + SCCs + data minimisation | ⚠️ Draft — urgent |
| Resend Inc. (Email Service) | USA [ASSUMPTION — verify] | Recipient email addresses, report content | Art. 44 + SCCs | DPA + SCCs | ❌ Not started |
| Railway Inc. (Cloud Hosting) | USA [ASSUMPTION — verify] | Application logs, system data | Art. 44 + SCCs | DPA + SCCs | ❌ Not started |

> **Note on Resend and Railway:** Both are assumed US-based pending verification. Until confirmed otherwise, both are treated as requiring SCCs and supplementary Schrems II measures — the same standard applied to Anthropic. This is the conservative and compliant default.

---

### 5.2 Anthropic — Detailed Assessment

**Legal status:** USA has no EU adequacy decision. Standard Contractual Clauses (SCCs) required, supplemented by technical and organisational measures per EDPB Schrems II guidance.

**Current gaps:**
- DPA retention clause is ambiguous ("up to 30 days" ≠ "deleted within 30 days")
- Sub-processor list (AWS regions, contractors) not provided in current draft
- No audit rights beyond SOC 2 reliance
- No government request notification clause

**Proposed enhanced DPA clauses:**

```
1. RETENTION
   Anthropic shall delete all personal data within 30 days of
   processing completion. No retention for model improvement,
   training, or any other purpose.

2. SUB-PROCESSORS
   Authorised sub-processors: Amazon Web Services (AWS),
   US-East and US-West regions. Any changes require 30 days'
   notice to dena with right to object.

3. GOVERNMENT REQUESTS
   If Anthropic receives legal process for dena data,
   Anthropic shall (to the extent legally permitted)
   notify dena before disclosure.

4. AUDIT RIGHTS
   dena has right to audit compliance via: (a) annual SOC 2
   Type II reports, or (b) on-site audit upon 30 days' notice.

5. DATA SUBJECT COOPERATION
   Anthropic shall cooperate with dena to fulfil data subject
   requests (access, deletion) within 10 business days of notice.
```

**Supplementary Schrems II measures:**

- **Technical:** Anonymise PM names before transmission (Project IDs instead of names); TLS 1.3 encryption in transit; no-copy clauses in DPA
- **Legal:** SCC Module Two (Controller-Processor); supplementary clauses above; annual review of US surveillance law landscape
- **Organisational:** Privacy notices to data subjects; access logs from Anthropic; batch processing (52 calls/year) minimises data exposure volume

---

### 5.3 Resend — Assessment

**Location:** [ASSUMPTION] US-based — to be verified. Treated as US-based pending confirmation.
**Data sent:** Recipient email addresses (~10 internal staff), report HTML content, delivery metadata.
**Volume:** ~52 emails/year.

**Required actions:**
1. Verify location and server regions
2. Request and execute DPA (standard terms + SCCs if US-based)
3. Clarify email retention period (how long are emails stored post-delivery?)
4. Data minimisation: use generic salutation; minimise personal data in email body

---

### 5.4 Railway — Assessment

**Location:** [ASSUMPTION] US-based — to be verified. Treated as US-based pending confirmation.
**Data on Railway:** Application logs (timestamps, error messages, API call metadata). No project content or email body stored on Railway.
**Volume:** ~1–5 MB/week in logs.

**Required actions:**
1. Verify location and certifications (SOC 2, ISO 27001)
2. Request and execute DPA (standard terms + SCCs if US-based)
3. Define log retention: [ASSUMPTION] 90 days; delete after
4. Data minimisation: redact email addresses and project names from Railway logs

---

### 5.5 Transfer Compliance Checklist

| Recipient | Location Verified | DPA Signed | SCCs in Place | Retention Defined | Priority |
|---|---|---|---|---|---|
| Anthropic | ✅ USA | ⚠️ Draft | ⚠️ Proposed | ⚠️ Ambiguous | 🔴 Urgent |
| Resend | ❌ Unknown | ❌ None | ❌ None | ❌ Unknown | 🟡 High |
| Railway | ❌ Unknown | ❌ None | ❌ None | ❌ Unknown | 🟡 High |

---

## Part 6: Compliance Gaps & Remediation

### 6.1 Gap Register

| Gap ID | Description | Severity | Deadline |
|---|---|---|---|
| GAP-1 | No finalised DPA with Anthropic | 🔴 Critical | July 31, 2026 |
| GAP-2 | PM names transmitted to Anthropic without anonymisation | 🔴 Critical | June 30, 2026 |
| GAP-3 | No DPA with Resend; location unverified | 🟡 High | June 30, 2026 |
| GAP-4 | No DPA with Railway; location unverified | 🟡 High | June 30, 2026 |
| GAP-5 | No Privacy Notices distributed to data subjects (PMs) | 🟡 High | June 30, 2026 |
| GAP-6 | No documented data subject rights process or templates | 🟡 High | July 31, 2026 |
| GAP-7 | Log retention periods not formally defined for all services | 🟡 High | June 30, 2026 |
| GAP-8 | No data breach response procedure (Art. 33–34) | 🟡 High | July 31, 2026 |
| GAP-9 | Bias audit not yet scheduled | 🟡 Medium | July 31, 2026 |
| GAP-10 | No governance for Key Risk field data entry | 🟡 Medium | June 30, 2026 |

---

### 6.2 Remediation Roadmap

**Phase 1 — Pre-Production (by June 30, 2026):**
- [ ] GAP-2: Implement PM name anonymisation in code (Project IDs before API transmission)
- [ ] GAP-3: Verify Resend location; initiate DPA
- [ ] GAP-4: Verify Railway location; initiate DPA
- [ ] GAP-5: Draft and distribute Privacy Notices to all 26 PMs
- [ ] GAP-7: Define log retention policy (12 months primary; 90 days debug)
- [ ] GAP-10: Issue data entry governance guidance for Key Risk field

**Phase 2 — At Launch (by July 31, 2026):**
- [ ] GAP-1: Finalise Anthropic DPA with supplementary Schrems II clauses
- [ ] GAP-6: Create data subject rights templates; assign DPO ownership; train staff
- [ ] GAP-8: Draft and test incident response procedure

**Phase 3 — Ongoing:**
- [ ] GAP-9: Quarterly bias audits from Q3 2026
- [ ] Annual: Review SCC adequacy + US surveillance law landscape
- [ ] Annual: Reassess on-premises LLM feasibility as alternative to US transfer

---

## Part 7: Summary & Compliance Statement

### 7.1 GDPR Compliance Status

| Area | Status | Comments |
|---|---|---|
| Legal Basis | ✅ Compliant | Art. 6(1)(e) clearly applies; Art. 6(1)(f) available as secondary |
| Data Inventory | ✅ Compliant | Documented; retention periods defined; minimisation principles applied |
| DPIA | ✅ Compliant (in progress) | Mitigations identified and scheduled; all residual risks acceptable |
| Data Subject Rights | ⚠️ Partial | Rights clearly scoped; process templates not yet documented (GAP-6) |
| Third-Country Transfers | ⚠️ In remediation | Critical DPA gaps identified and on defined timeline (GAP-1, 3, 4) |
| Transparency | ⚠️ In remediation | Privacy notices drafted; distribution scheduled by June 30 (GAP-5) |
| Data Security | ⚠️ In remediation | TLS in place; data minimisation implementation in progress (GAP-2) |
| Incident Response | ⚠️ In remediation | Procedure to be documented by July 31 (GAP-8) |

**Overall Assessment:** System is **pre-production compliant pending completion of identified mitigations.** All critical gaps are on a defined remediation timeline. No gaps are unmitigatable; no processing activities have been identified as fundamentally non-compliant. Full compliance target: **August 31, 2026.**

---

### 7.2 Conditions for Production Approval

The system may proceed to production if and only if the following are in place:

1. ✅ **GAP-2:** PM names anonymised before Anthropic transmission (code change)
2. ✅ **GAP-3:** Resend location verified and DPA initiated
3. ✅ **GAP-4:** Railway location verified and DPA initiated
4. ✅ **GAP-5:** Privacy Notices distributed to all 26 PMs
5. ✅ **GAP-7:** Log retention policy defined and communicated to all vendors
6. ✅ **GAP-10:** Key Risk field governance guidance issued

Conditional post-launch (by July 31, 2026):

7. ⚠️ **GAP-1:** Anthropic DPA finalised with supplementary Schrems II clauses
8. ⚠️ **GAP-6:** Data subject rights templates and training completed
9. ⚠️ **GAP-8:** Incident response procedure documented and tested

---

### 7.3 DPO Statement

> "This GDPR assessment identifies manageable risks with a clear remediation path. The system is pre-production compliant pending implementation of critical mitigations by June 30, 2026, particularly PM name anonymisation and vendor DPA initiation. Ongoing quarterly bias audits and annual Schrems II compliance reviews are required. The system does not trigger Art. 22 automated decision-making obligations, provided that the AI recommendation acceptance rate monitoring control is maintained."

**Prepared By:** [ASSUMPTION] dena DPO + Legal Counsel + IT Security
**Approval Authority:** dena CISO / Compliance Officer
**Next Review:** July 31, 2026, or upon material system changes

---

## Appendices

### Appendix A: Privacy Notice Template (Article 14)

```
DATA PRIVACY NOTICE — dena IME Weekly Portfolio Reporting System

Dear Project Manager,

Pursuant to Article 14 GDPR, we inform you that dena processes
personal data relating to your project assignment in our weekly
AI-powered portfolio reporting system.

CONTROLLER
Deutsche Energie-Agentur (dena), Chausseestraße 128a, 10115 Berlin
Division: Industrie, Mobilität, Energieeffizienz (IME)

DATA PROTECTION OFFICER
dpo@dena.de

PROCESSING PURPOSE
Portfolio health monitoring and management decision support

LEGAL BASIS
Article 6(1)(e) GDPR — public task (energy transition mandate)

PERSONAL DATA PROCESSED
- Your project assignment and project name
- Budget and financial metrics associated with your project
- Risk descriptions that may reference your project or role

RECIPIENTS
- dena IME leadership (Division Head, Finance team) — internal
- Anthropic Inc. (USA) — AI analysis; 30-day retention; deleted after processing
- Resend Inc. (USA) — email delivery
- Railway Inc. (USA) — system hosting and logging

All US recipients are governed by Standard Contractual Clauses
and supplementary Schrems II safeguards.

RETENTION
- Project data: Indefinite (organisational records)
- System logs: 12 months
- Data at Anthropic: Deleted within 30 days of processing

YOUR RIGHTS (contact dpo@dena.de within 30-day response SLA)
- Access: Request a copy of your data (Art. 15)
- Rectification: Correct inaccurate data (Art. 16)
- Erasure: Request deletion after retention expires (Art. 17)
- Restriction: Pause processing pending dispute (Art. 18)
- Object: Raise concerns if privacy is affected (Art. 21)

Note: Data portability (Art. 20) does not apply to processing
under Art. 6(1)(e). Automated decision-making (Art. 22) does
not apply — all decisions are made by human managers.

CONTACT
dpo@dena.de | +49 30 XXXX-XXXX
```

---

### Appendix B: SCC Checklist

- [ ] SCC Module Two (Controller-Processor) selected
- [ ] Supplementary Schrems II clauses added: data minimisation, encryption, sub-processor list, government request notification, audit rights
- [ ] Executed and countersigned by vendor
- [ ] Filed with DPO
- [ ] Annual review scheduled

---

### Appendix C: DPA Checklist (Anthropic, Resend, Railway)

- [ ] Subject matter, duration, nature, and purpose of processing defined
- [ ] Personal data types and data subject categories specified
- [ ] Processor obligations: instructions-only processing, confidentiality, security, timely deletion
- [ ] Sub-processor authorisation: list provided; change notification clause included
- [ ] Data subject rights cooperation mechanism defined
- [ ] Audit rights granted
- [ ] Liability and indemnification clauses included
- [ ] SCC reference included (all three vendors: US-based)
- [ ] Executed and dated

---

### Appendix D: Data Breach Response Procedure (Articles 33–34)

```
IF A PERSONAL DATA BREACH IS DISCOVERED:

1. IMMEDIATE (Within 24 hours)
   - Isolate affected system
   - Document: what data, when discovered, how it occurred
   - Assess scope: number of records, data subjects affected

2. SUPERVISORY AUTHORITY NOTIFICATION (Within 72 hours if required)
   - Contact BfDI (German DPA)
   - Provide: description, risk assessment, mitigation taken
   - Exception: if risk to data subjects is low, notification not required

3. DATA SUBJECT NOTIFICATION (Without undue delay if high risk)
   - Send breach notice to affected PMs and recipients
   - Explain: nature of breach, data affected, likely consequences
   - Advise on protective steps

4. DOCUMENTATION
   - Record in incident log: incident ID, date, summary, outcome
   - Retain evidence for regulatory audit

5. PREVENTION
   - Remediate vulnerability
   - Test fix
   - Update security controls
   - Review and update DPIA if risk profile changes
```

---

*Version 1.1 · Prepared June 15, 2026 · Status: Pre-Production Compliant (Mitigations in Progress) · Full Compliance Target: August 31, 2026 · Next Review: July 31, 2026*
