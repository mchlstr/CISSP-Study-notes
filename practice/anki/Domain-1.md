# Anki Deck — Domain 1 (Security & Risk Management)

> Format: `Question :: Answer` (Obsidian_to_Anki compatible). Pruned for exam-yield: atomic, gradeable cards only.

## Privacy & Compliance Laws

What does GLBA require, and its trigger phrase? :: Financial institutions must give a privacy notice (opt-out of info sharing) + safeguard customer financial data. Trigger: "financial institution + privacy notice."
What does FERPA protect, and what happens at 18? :: Privacy of student education records (schools getting federal funds); rights TRANSFER from parents to the student at 18 / entering college.
What does COPPA require, and the age? :: Verifiable parental consent before collecting data on children UNDER 13.
COPPA/FERPA age mnemonic? :: PG-13 = COPPA (under 13); 18 = FERPA (transfer age).
HIPAA — three covered entities? :: Healthcare providers, health plans, healthcare clearinghouses (+ their business associates). A fitness app is NOT automatically covered.
HIPAA vs HITECH? :: HIPAA = original rules; HITECH (2009) = added Breach Notification Rule, direct liability for business associates, bigger penalties, EHR push.
What does CALEA require? :: Telecom carriers/equipment makers must build in capability to cooperate with lawful (warranted) wiretaps.
What does the Privacy Act of 1974 govern? :: How US FEDERAL government agencies handle PII in their records.
PIPL vs PIPEDA? :: PIPL = China's privacy law; PIPEDA = Canada's. Don't confuse them.
Why is GDPR uniform EU-wide (Regulation vs Directive)? :: It's a Regulation (applies directly); a Directive must be implemented separately by each member state.
GDPR default digital consent age? :: 16 by default; members may lower to 13.
US breach notification — based on HQ or residents? :: Where the affected INDIVIDUALS reside (not the company's HQ). No single federal law — all 50 states + sector laws.
GDPR Art 33 vs Art 34 — who is notified, when? :: Art 33 = the REGULATOR within 72h (unless unlikely to risk). Art 34 = AFFECTED INDIVIDUALS, only if HIGH risk; encrypted/unintelligible data is exempt.
Does encryption exempt you from breach notification? :: Often yes (GDPR Art 34 / US state safe harbor) — IF encryption is strong and keys aren't compromised.
Is PCI DSS a law, and who writes vs enforces it? :: Not a law — a contractual standard. PCI SSC writes it; card brands enforce it via the acquiring bank.
SOX — who and what? :: US PUBLICLY TRADED companies; internal controls over financial reporting, with CEO/CFO personal certification.
SOX vs SOC? :: SOX = law for public companies; SOC = an audit report on a vendor.

## Quantitative Risk

SLE formula and meaning? :: SLE = AV × EF — the dollar loss from ONE occurrence. (EF = % of asset value lost per event.)
ALE formula? :: ALE = SLE × ARO — dollars of loss per year.
ARO, and the classic exam trap? :: Annualized Rate of Occurrence = 1 ÷ (years between events). Trap = 10× error: a 100-year event = 0.01, NOT 0.1. Count the zeros.
ARO must match what? :: The SPECIFIC asset AND event in the scenario — a tornado hitting MY building once per 200 years = 0.005, regardless of regional hazard rate.
Worked example — rebuild $10M, typical damage $5M, once per 200 years, ALE? :: AV=$10M, SLE=$5M, EF=0.5, ARO=0.005 → ALE = $25,000/year.
Asset valuation — when REPLACEMENT cost? :: When the scenario emphasizes recovery/rebuilding/restoring (cost to rebuild today). Other methods: original/purchase (what was paid), depreciation (book value), opportunity (next-best forgone).
The four risk treatment options? :: Mitigate (reduce via control), Transfer (e.g., insurance), Avoid (stop the activity), Accept (knowingly retain). "Reject/ignore" = always wrong (negligence).
Cost-benefit rule for accepting a risk? :: If the cost of the control > ALE (potential loss) → ACCEPT the risk.
What makes risk acceptance valid (vs negligence)? :: A formal, documented decision by senior management with authority. Ignoring an un-assessed risk = negligence.
Order the risk components chain. :: Threat agent → exploits vulnerability → realizes threat → against asset → causing impact → = risk (likelihood × impact).
Threat vs threat agent? :: Threat = the potential danger (what could happen); threat agent = the entity that carries it out (e.g., a hacker).
Is a missing patch a threat or a vulnerability? :: A vulnerability (a weakness) — NOT a threat.
When a scenario names an attacker but gives no exploit method, what role does the attacker fill? :: The threat — with no separate method specified, the threat agent stands in as the threat.

## BCP & BIA

BCP phase order? :: Project Scope & Planning → BIA → Continuity Planning → Approval & Implementation (documentation + approval happen here).
The 4 activities of BCP Scope & Planning? :: (1) Structured analysis of the org, (2) create the BCP team (mgmt approval), (3) assess available resources, (4) analyze the legal/regulatory landscape.
Who should APPROVE the BCP, vs who DEVELOPS it? :: Approve = CEO/senior mgmt (broadest authority). Develop = business function leaders + IT + support (with a senior liaison). Verb cue: "approve" → CEO; "develop/team" → business+IT+support.
In BCP training, what does "initial" mean? :: The entry-level TIER (broad, org-wide awareness) — NOT "the first group of people." Role-specific training comes after.
What are Emergency Response Guidelines, and what do they contain? :: A concise, quickly-accessible doc of disaster-onset steps: (1) immediate response (evacuation/safety/containment), (2) who to notify, (3) escalation to response teams.
BIA — quantitative vs qualitative impact? :: Quantitative = numbers/$ (lost revenue, fines, replacement cost). Qualitative = intangibles (reputation, customer confidence, goodwill). "Loss of customer confidence" = qualitative.
Which data-at-rest risk causes the greatest REPUTATIONAL impact, and why? :: A data breach — it publicly exposes data, destroying customer confidence. (Insider threat = a cause; the public BREACH is the reputational outcome.)

## Governance, Frameworks, Ethics & Metrics

CMM/SW-CMM vs RMM? :: CMM/SW-CMM = process/software maturity (5 levels); RMM = risk-management maturity. Match the model to the thing measured.
What is COBIT? :: ISACA's IT governance & management framework — aligns IT goals with business objectives.
ISO 27001 vs 27002? :: 27001 = the ISMS you certify against; 27002 = the internationally-accepted catalog of security controls.
NIST RMF (SP 800-37) steps? :: Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor (7 steps).
What is a security baseline? :: A documented minimum mandatory level of security/config all systems of a type must meet — a starting point you then scope and tailor.
(ISC)² Code of Ethics canon order? :: 1 Society, 2 Honorably, 3 Service to principals, 4 Profession — applied in priority order (earlier canon wins on conflict).
Which codes of ethics bind a CISSP? :: The (ISC)² Code PLUS the employer's code. (RFC 1087 is an old advisory, not binding; a federal code binds only federal employees.)
KPI vs KGI vs KRI? :: KPI = current performance vs target (present); KGI = whether the end goal was achieved (outcome); KRI = risk exposure / early warning (forward-looking).
Metric vs KPI? :: A metric is a raw measurement; a KPI is a metric tied to a defined target (a measurement with a 95% aim = a KPI).
What is an NDA (and control type)? :: Non-Disclosure Agreement — an administrative control protecting confidentiality; signed at onboarding and by vendors.
Due care vs due diligence? :: Due care = taking the prudent, reasonable action to protect the org (doing the right thing); due diligence = the ongoing investigation/research that informs it. Diligence = investigate; care = act.
Rule hierarchy — which are mandatory vs discretionary? :: Policy, Standard, Procedure, and Baseline are mandatory; Guideline is the only one that is a recommendation (discretionary).
Standard vs guideline vs procedure? :: Standard = mandatory specification (the what); Procedure = mandatory step-by-step instructions (the how); Guideline = optional recommendation.

## Threat Modeling & CIA Mappings

STRIDE + CIA mapping? :: Spoofing(Authentication), Tampering(Integrity), Repudiation(Non-repudiation), Information Disclosure(Confidentiality), Denial of Service(Availability), Elevation of Privilege(Authorization).
What is reduction analysis, and what 5 elements does it find? :: Decomposing a system (via a Data Flow Diagram) to find the attack surface: trust boundaries, data flows, input points, privileged operations, security controls.
General CIA mapping by attack type? :: Confidentiality = unauthorized DISCLOSURE (sniffing, keylogger — defend with encryption); Integrity = unauthorized MODIFICATION (defacement); Availability = DISRUPTION (DoS — defend with load balancing/clustering/RAID).
What is PASTA? :: Process for Attack Simulation and Threat Analysis — a risk-centric, 7-stage attacker-simulation threat model.
What is DREAD? :: A threat-scoring model — Damage, Reproducibility, Exploitability, Affected users, Discoverability.

## Controls & Risk Frameworks

Three control categories (how implemented)? :: Administrative (policies/training), Technical/Logical (firewall/encryption), Physical (locks/guards).
Seven control functions (what they do)? :: Directive, Deterrent, Preventive, Detective, Corrective, Recovery, Compensating.
What is a compensating control? :: An alternative used when the primary control isn't feasible (e.g., encrypt stored card data you can't remove).
Functional vs assurance requirement? :: Functional = does the control DO what it should; Assurance = confidence/evidence that it works correctly.
Risk frameworks — ISO 31000 vs COSO vs ISACA Risk IT? :: ISO 31000 = international risk-management standard (broad); COSO = enterprise risk + internal controls (financial/governance); ISACA Risk IT = IT-risk (COBIT family).

## NIST 800-53 — Control Selection

What is NIST SP 800-53? :: A catalog of security AND privacy controls (US federal, widely adopted), organized into families; used with the RMF from a control baseline.
Scoping vs tailoring? :: Scoping = REMOVE controls from a baseline that don't apply ('specific systems'). Tailoring = the BROADER customization (scoping + compensating controls + org-specific parameter values; 'organization's mission/needs'). Scoping is a subset of tailoring.
Setting an org-specific password length on a baseline control is which? :: Tailoring (assigning org-specific parameter values) — scoping only removes non-applicable controls.
Exam trap — answers with 'all / always / never / prevents / ensures / eliminates'? :: Usually WRONG — absolutes overreach. Pick the measured, realistic option.

## Baselines & Benchmarks

PCI DSS vs CIS Benchmark? :: PCI DSS = the compliance requirement (the WHAT); CIS Benchmark = an OS-specific, vendor-neutral hardening baseline with specific settings (the HOW).
CIS Benchmarks vs CIS Controls? :: Benchmarks = OS/app secure-configuration hardening guides; Controls = a prioritized list of ~18 security controls.
Most effective way to enforce a Windows baseline across many PCs, and the requirement? :: Group Policy (GPO) — centralized enforcement that auto-reapplies and corrects drift. Requires devices be DOMAIN-JOINED (Active Directory).
If Windows PCs are NOT domain-joined, how do you enforce the baseline? :: Intune/MDM (cloud-pushed) — GPO and centralized startup scripts both need AD.

## Import/Export Controls & Transborder Data

ITAR vs EAR? :: ITAR = US State Dept, defense/military items & technical data (US persons only). EAR = US Commerce Dept, dual-use commercial items (incl. some crypto).
What is the Wassenaar Arrangement? :: An international multilateral export-control pact for arms + dual-use tech (incl. cryptography).
What is transborder data flow (security concern)? :: Moving data across national borders subjects it to different countries' laws (e.g., GDPR restricts personal-data transfers out of the EU). Satisfy each jurisdiction (adequacy/SCCs/BCRs).

## Awareness, Governance & Accountability

Awareness vs training vs education? :: Awareness = change behavior/attention (the 'what', all staff); Training = teach a job skill (the 'how', role-based); Education = deeper conceptual understanding (the 'why').
Responsibility vs accountability — which can be delegated? :: Responsibility (who DOES the task) can be delegated; accountability (who ANSWERS for the outcome, ultimately senior mgmt) CANNOT.
Corporate vs security governance? :: Corporate governance = directing/controlling the whole org for stakeholders; security governance = the subset aligning the security program with business objectives.
Primary focus of a security program? :: Enable the business and increase value — security supports business objectives, not the reverse.

## Intellectual Property

The four IP types + key facts? :: Trade Secret (secret business info, no expiry while secret, NDA, no registration); Patent (inventions, ~20 yrs, novel/useful/non-obvious, public disclosure); Copyright (original works incl. software, life+70 yrs, automatic); Trademark (brand names/logos, renewable indefinitely).
Trade secret vs patent — the trade-off? :: Trade secret = kept secret, protected forever IF secret. Patent = public disclosure in exchange for a ~20-year monopoly, then public.
Trademark symbols ® vs ™ vs ©? :: ® = registered (USPTO-approved); ™ = unregistered/claimed (before approval); © = copyright.

## Supply Chain

What is interdiction (supply chain), and the defense? :: A third party intercepts hardware in transit and implants a backdoor before delivery — it arrives compromised. Defend with tamper-evident packaging, chain-of-custody, integrity verification on receipt, buying direct.
Best security standard to require of a vendor handling your data? :: That the vendor handle your data the same way YOUR organization would — not merely "comply with all laws," never "eliminate all risk."

## BCM, Plan Types & Testing

What is the #1 priority in any BCM/DR/emergency decision? :: Safety of PEOPLE — life safety overrides all asset/business concerns. (BCM goal order: people → minimize damage → business survival.)
BCP vs DRP? :: BCP = keep the whole BUSINESS running (strategic); DRP = restore IT SYSTEMS after failure (tactical). DRP is a subset of BCP.
How do RTO, WRT, and MTD relate? :: RTO (restore systems) + WRT (verify data & resume work) must be ≤ MTD (maximum tolerable downtime).
In what order are processes restored after a disaster? :: Most CRITICAL functions first, using dependency charts to respect prerequisites (per the BIA).

## BCP/DR Plan Testing Types

BCP/DR test types, least → most disruptive? :: Read-through/checklist (review docs, lowest cost) → Walkthrough/tabletop (discuss/role-play) → Simulation (practice a scenario) → Parallel (recovery brought up alongside live production) → Full-interruption (production taken DOWN and failed over).
Parallel vs full-interruption test? :: Parallel = recovery runs alongside live production (no downtime risk); full-interruption = production is taken DOWN and failed over (highest risk/realism).
Simplest / lowest-risk DR test? :: Read-through / checklist (or tabletop) — discussion-based, no systems touched.

## BCM/Testing Scenarios (Application)

Scenario: A flood threatens the data center and staff. FIRST priority? :: Safety of people — before minimizing damage or saving the business.
Scenario: You must test DR realistically but cannot risk any production downtime. Which test? :: A parallel test (recovery alongside production, no outage).
Scenario: MTD is 8h; restoring systems takes 5h (RTO) and verifying/resuming takes 4h (WRT). Problem? :: RTO + WRT = 9h > 8h MTD — recovery doesn't meet the MTD; speed up recovery or reduce WRT.
Scenario: After a disaster, what guides the restore order? :: Restore the most critical functions first, per the BIA and dependency charts.

## Scenarios & Application

A vendor breach exposes your customer data; you had a signed DPA holding the vendor liable for damages. What risk-response did the DPA represent? :: Risk transfer — contractual liability shifts financial impact, but accountability for the data stays with you.
A control to mitigate a risk costs $40k/year; the ALE is $15k. What should you do? :: Accept the risk — the control costs more than the expected annual loss, so spending on it isn't justified.
A risk remains after you deploy all planned controls. The board signs a formal statement choosing to live with it. What is this called, and is it valid? :: Risk acceptance of residual risk — valid because it's a documented decision by senior management with authority.
You stop offering a product line entirely because its data-handling risk is unacceptable. Which risk response? :: Risk avoidance — eliminating the activity removes the risk rather than reducing it.
A server fails once every 25 years; rebuild cost is $200k and a failure destroys half its value. What is the ALE? :: SLE = $200k × 0.5 = $100k; ARO = 1/25 = 0.04; ALE = $100k × 0.04 = $4,000/year.
Your firm researches a target before acquiring it, reviewing its security posture and liabilities. Due care or due diligence? :: Due diligence — the ongoing investigation that gathers facts. Acting on those facts prudently would be due care.
After acquiring the firm, you promptly remediate the security gaps you found. Due care or due diligence? :: Due care — taking the prudent, reasonable action a careful organization would take.
A breach happens despite reasonable safeguards being in place and maintained. What legal concept shields the org from negligence claims? :: Due care (the prudent-person rule) — doing what a reasonable org would do, even if it isn't perfect.
The CISO delegates patching to the ops team, but a missed patch causes a breach. Who is ultimately accountable? :: Senior management — accountability cannot be delegated; only the responsibility (the task) was.
Who has the authority to formally approve and sign off on the BCP? :: Senior management / the CEO — they hold the broadest organizational authority and own the residual risk.
Leadership asks for the financial justification of a risk in an executive summary. Which approaches communicate it best? :: Cost, income, or market approaches — a technical approach fails because executives don't think in technical terms.
A developer writes secret code that only their company knows; they choose not to file for protection. Which IP protection applies and for how long? :: Trade secret — protected indefinitely as long as it stays secret; no registration needed.
You want a 20-year exclusive right but must publicly disclose how your invention works. Which IP type? :: Patent — the disclosure-for-monopoly trade-off; after ~20 years it becomes public.
Software source code is automatically protected the moment it's written in fixed form. Which IP type? :: Copyright — protection is automatic on creation (life + 70 years for individual authors).
You can't remove stored cardholder data a legacy app requires, so you encrypt it instead of tokenizing. What kind of control is the encryption? :: A compensating control — an alternative used when the primary control isn't feasible.
A guard dog and warning signs are deployed mainly to discourage intruders from trying. Which control function? :: Deterrent — it discourages the attempt (a fence that physically stops entry would be preventive).
A SIEM alert tells you an intrusion already occurred. Which control function did the SIEM serve? :: Detective — it identifies an event after it happens, not before.
Two (ISC)² ethics canons conflict: protecting society vs. serving your employer. Which wins? :: Protect society, the common good, and the infrastructure — Canon I outranks service to principals (Canon III).
A vendor offers to "comply with all applicable laws" with your data. Is that the standard you should require? :: No — require the vendor to protect your data the way your own organization would; legal compliance alone is a floor, not the bar.
You need to test DR realistically but cannot tolerate any production outage. Which test type? :: Parallel test — recovery systems run alongside live production with no downtime risk.
A disaster destroys the original facility and demands both short- and long-term recovery. Which severity classification? :: Catastrophe — destruction of the original facility plus dual-horizon recovery, beyond a Disaster.
You set a longer minimum password length on a baseline control to fit org policy. Scoping or tailoring? :: Tailoring — assigning org-specific parameter values; scoping only removes controls that don't apply.
A baseline includes physical data-center controls, but you're cloud-only. Removing them is what? :: Scoping — eliminating baseline controls that don't apply to your specific systems.
Hardware arrives with an implanted backdoor after being intercepted in transit. What supply-chain attack is this, and a key defense? :: Interdiction — defend with tamper-evident packaging, chain-of-custody, and integrity verification on receipt.
A metric reports patch compliance against a 95% target for the board. Is that a metric or a KPI? :: A KPI — a measurement tied to a defined target; a raw number with no target is just a metric.
