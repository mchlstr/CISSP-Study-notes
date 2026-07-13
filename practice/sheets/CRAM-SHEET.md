# CISSP Cram Sheet — Last-Mile Memorize

High-density "memorize this exactly" sheet — each line is a tested fact, not a discussion. Best used for last-mile review in the final weeks before the exam.

---

## OOP Concepts — DIRECT MAPPINGS (D8)

> Question text → answer (general CISSP doctrine).

- "Data structure + operations grouped into one entity" → **Encapsulation**
- "Hiding internal complexity / exposing simple interface" → **Abstraction**
- "Restrict external access to internal implementation" → **Information Hiding**
- "Redefine internal components without affecting other parts of the system" → **Modularity**
- "Delay binding / delay implementation decisions until late / late binding" → **Deferred Commitment**
- "Map object-oriented analysis/design to real-world business needs" → **Naturalness**
- "Use the same object in different contexts" → **Reusability**
- "How strongly the elements within a module relate" → **Cohesion** (high cohesion = good)
- "How dependent modules are on each other" → **Coupling** (low coupling = good)
- "Same interface, different implementations" → **Polymorphism**
- "Child inherits properties from parent" → **Inheritance**

---

## ACID Properties — DIRECT MAPPINGS (D8)

- "All-or-nothing" → **Atomicity**
- "DB moves from one valid state to another" → **Consistency**
- "Parallel transactions are separated; one's effects don't corrupt another" → **Isolation** (NOT atomicity)
- "Committed transactions persist even after crash" → **Durability**

---

## SDLC Methodologies (D8)

- **Waterfall** = strict sequential linear phases
- **V-Model** = sequential with parallel testing at each phase
- **Agile** = iterative + self-organizing teams
- **Scrum** = specific Agile flavor with sprints + ceremonies (subset of Agile)
- **Sprint** = fixed-duration dev interval (typically 2 weeks) within Scrum
- **Spiral** = risk-driven iterations with risk analysis each cycle
- **RAD** = Rapid Application Development — prototyping focus; allows reset at clearly defined points
- **Extreme Programming (XP)** = pair programming + frequent releases
- **Kanban** = continuous flow, no fixed iterations
- **DevOps** = dev + ops merged
- **DevSecOps** = dev + ops + security embedded throughout

**For "best approach for cross-team communication and collaboration":** answer is typically **DevSecOps** (modern), not co-location (dated).

---

## CMM / CMMI Levels (D8, D3)

1. **Initial** — chaotic, ad hoc, undocumented
2. **Repeatable** (CMM) / **Managed** (CMMI) — basic processes established, can repeat past successes
3. **Defined** — processes documented and standardized
4. **Managed** (CMM) / **Quantitatively Managed** (CMMI) — **planned, performed, measured, controlled** ← memorize this exact phrase
5. **Optimizing** — continuous improvement

**Key trap:** "planned, performed, measured, controlled" = Level 4 Managed (NOT Defined Level 3, definitely NOT Initial Level 1). If a test marks this as Initial, that is a test error — Initial is by definition ad hoc.

---

## Hashing Algorithms — Output Sizes (D3)

| Algorithm | Output | Notes |
|---|---|---|
| **MD5** | 128 bits | Broken, don't use |
| **SHA-1** | **160 bits** | Deprecated |
| **SHA-256** | 256 bits | Current standard |
| **SHA-512** | 512 bits | |
| **SHA-3** | variable | Newer family |

**Trap:** "Which algorithm produces a 160-bit hash?" → **SHA** (specifically SHA-1). NOT AES (AES is symmetric encryption, not a hash). NOT MD5 (128).

---

## Block Cipher Internals (D3)

- Block ciphers use **S-boxes** (Substitution boxes) for mathematical functions, substitution, and permutations on message bits
- NOT initialization vectors (those are used to initialize the cipher in some modes)
- NOT digital certificates
- NOT keystream generators (those are for stream ciphers)

---

## Covert Channels (D3)

- **Covert Storage Channel** = one process communicates to another by writing/reading a shared storage resource
- **Covert Timing Channel** = one process communicates by **modulating the use of system resources** (the receiver observes timing variations)

**Trap:** "Modulating the use of the system's resources" → **Covert Timing Channel** (NOT covert storage, NOT maintenance hook, NOT TOC/TOU)

---

## Disaster Severity Classifications (D1)

1. **Nondisaster** = service disruption, little impact
2. **Disaster** = entire facility unusable for a day or more
3. **Catastrophe** = **destroys the original facility** + requires both **short- AND long-term** recovery planning

**Trap:** "Cripples a business, destroys the original facility, requires short- and long-term recovery" → **Catastrophe** (NOT Disaster)

---

## Law / Regulation / Policy / Standard / Procedure (D1)

- **Law** = system of rules created by government **or society**, recognized as binding, enforced by specific authority
- **Regulation** = written rules with **force of law**, issued by executive body / government agency
- **Policy** = organizational high-level directive
- **Standard** = mandatory specification (e.g., PCI-DSS within an org)
- **Procedure** = step-by-step instructions
- **Guideline** = recommendation (not mandatory)

**Trap:** "System of rules created by either government or a society, recognized as binding, enforced by specific authority" → **Law** (NOT Standard)

---

## Evidence (D7) — Admissibility

Three required criteria: **Relevance + Reliability + Legality** (NOT accuracy, NOT truthfulness)

Evidence types:
- **Best evidence** = original document
- **Documentary evidence** = any written
- **Parol evidence rule** = verbal modifications inadmissible when contradicting written contract
- **Testimonial** = witness statements
- **Direct vs Circumstantial**

---

## Risk Approaches for Senior Management (D1)

Effective ways to express risk in executive summary: **Cost / Income / Market** approach
**NOT effective:** Technical approach (execs don't speak technical)

---

## Smart Card Types (D5) — REVERSED-PAIR TRAP

- **Combi card** = ONE chip with dual interface (contact AND contactless from a single chip)
- **Hybrid card** = TWO separate chips (one contact + one contactless)

**Trap:** the question reverses this in the wrong options. Memorize exactly which is which.

---

## Authentication Token Types (D5)

- **Synchronous time-based** = TOTP (Google Authenticator); server and token share time
- **Synchronous counter-based** = HOTP; server and token share a counter
- **Asynchronous nonce-based** = **challenge/response** (server sends challenge, token computes response using a nonce)

**Trap:** "Challenge/response scheme to authenticate" → **Asynchronous nonce-based** (NOT synchronous — challenge-response is async)

---

## OIDC (D5)

- **Relying Party (RP)** = the web application itself (the app that needs the user authenticated)
- **Identity Provider (IdP)** = third-party server that authenticates the user — this is the component the RP *uses* to authenticate
- **Authorization Server** = part of the IdP that issues tokens (don't confuse with the IdP itself)
- **End User / Resource Owner** = the human

**Trap:** "What component does a web app USE to authenticate an end user?" → **IdP** (NOT Authorization Server, NOT Relying Party — RP is the app itself)

**Flows:**
- **Authorization Code Flow** = RP receives a code, exchanges it for an ID token directly with IdP (most secure, server-to-server)
- **Implicit Flow** = token returned directly in URL (deprecated, less secure)
- **Hybrid Flow** = combines code + token in one flow
- **Client Credentials Flow** = service-to-service, no user

---

## IPSec vs TLS vs HTTPS (D5)

- **IPSec** = protects **IP traffic** (Layer 3) — VPNs, site-to-site
- **TLS** = protects transport-layer connections (Layer 4-5)
- **HTTPS** = HTTP over TLS — protects web traffic specifically
- **HAIPE** = High Assurance Internet Protocol Encryptor (US govt IPSec-based device for classified networks)

**Trap:** "Technology developed specifically to protect IP traffic" → **IPSec** (NOT TLS — TLS protects transport, not IP)

---

## VPN IPSec Modes (D5)

- **Transport mode** = host-to-host, only payload encrypted (original IP header preserved)
- **Tunnel mode** = gateway-to-gateway or VPN, **entire packet encrypted** (new IP header added)

**Trap:** "VPN using IPSec" → **Tunnel mode** (VPNs almost always use tunnel mode)

---

## Virtual / Meta Directory (D5)

- **Directory service** = the actual directory (e.g., AD, LDAP)
- **Meta-directory** = aggregates multiple directories into one logical view (data-pull approach, periodic sync)
- **Virtual directory** = same role as meta-directory but real-time view (no data sync, just queries on demand)

**Trap:** "Virtual directory plays same role as ___" → **Meta-directory** (NOT just "directory service")

---

## Virtual Password (D5)

- **Virtual password** = passphrase converted into the **length and format required by a specific system or application** (NOT a hash, NOT an encryption key)
- "Derived from a passphrase" → Virtual password

---

## Network Standards (D4)

- **H.323** = international standard for **audio/video over packet-based networks** (NOT SIP — SIP is a competing standard but H.323 is THE international one)
- **SIP** = Session Initiation Protocol, also for VoIP/video
- **SONET** = **physical layer fiber-optic** transmission standard
- **T-carriers** = copper-based digital transmission (T1, T3 etc.)
- **ATM** = WAN tech using **53-byte fixed cells**, low delay (good for time-sensitive)
- **Frame Relay** = packet-switched WAN tech
- **X.25** = legacy packet-switched WAN
- **FDDI** = fiber-distributed data interface

---

## Baseband vs Broadband (D4) — REVERSED-PAIR TRAP

- **Baseband** = uses **entire** communication channel for its transmission (single channel, full bandwidth, limited distance)
- **Broadband** = **divides** the communication channel into multiple independent channels (multiplexed)

**Trap:** the wrong options swap which uses entire vs which divides. Memorize: BAS=entire, BROAD=divides.

---

## OSI Layer Device Mapping (D4)

| Layer | OSI Layer Name | Devices |
|---|---|---|
| 1 | Physical | Hub, repeater, cables |
| 2 | Data Link | Bridge, Switch (some L3) |
| 3 | Network | Router |
| 4 | Transport | (Firewalls in some classifications) |
| 7 | Application | **Gateway** |

**Trap:** "Operates at the application layer" → **Gateway** (NOT switch/router/bridge)

---

## Wi-Fi Encryption Algorithms (D4)

- **WEP** uses **RC4** (broken)
- **WPA** uses RC4 with TKIP (transitional)
- **WPA2** uses AES with CCMP
- **WPA3** uses AES with SAE (Simultaneous Authentication of Equals — replaces PSK)

**Trap:** "WEP uses which algorithm?" → **RC4** (NOT DES, NOT AES, NOT SHA-256)

---

## Spread Spectrum Technologies (D4)

- **FHSS** (Frequency Hopping Spread Spectrum) = spread spectrum
- **DSSS** (Direct Sequence Spread Spectrum) = spread spectrum
- **OFDM** (Orthogonal Frequency Division Multiplexing) = NOT pure spread spectrum (multi-carrier modulation)
- **WPA2** = encryption protocol, NOT a spread spectrum technology

**Trap:** "Which are NOT spread spectrum?" → **OFDM and WPA2** (NOT FHSS/DSSS)

---

## CIS Controls Categorization (D8, D1)

- **CIS Controls** uses **Basic / Foundational / Organizational** categorization (legacy 20 controls)
- Newer CIS v8 uses **Implementation Groups (IG1, IG2, IG3)**
- **NOT COBIT** — COBIT is governance framework
- **NOT NIST RMF** — NIST RMF uses categorize/select/implement/assess/authorize/monitor steps
- **NOT ISO 27000**

---

## AI Approaches (D8)

- **Symbolic AI** = rule-based, expert systems, logic-driven
- **Non-symbolic** (or sub-symbolic) AI = neural networks, machine learning, data-driven
- NOT "signature-based vs anomaly-based" (that's IDS classification)
- NOT "heuristic vs behavioral" (that's antivirus classification)

---

## GOTS / COTS / Custom Software (D8)

- **GOTS** = Government-Off-The-Shelf (made for a specific government org, custom or customized)
- **COTS** = Commercial-Off-The-Shelf (generic, sold to many)
- **Custom** = built specifically for one organization

**Trap:** "Software made specifically for an organization and is custom (or at least customized)" → **GOTS** (when org = govt). Third-party = the developer, not the category.

---

## Password Generator (D8)

A password generator is an **automated system that creates long-stringed passwords difficult to remember**. NOT a teaching tool, NOT a dictionary attack, NOT a list of questions.

---

## Incident Response Phases (D7)

**Preparation → Detection → Response → Eradication → Recovery → Lessons Learned**

- **Containment of damage happens during the RESPONSE phase**
- Eradication = remove the threat
- Recovery = restore systems

---

## DR Site Types (D7)

- **Cold site** = empty building with power/HVAC; takes weeks to bring up
- **Warm site** = some equipment, partial readiness; days
- **Hot site** = fully equipped, near-real-time; can be activated in hours
- **Redundant site** = duplicate operational site running in parallel; essentially zero downtime + sustainable long-term
- **Rolling hot site** = mobile hot site (truck/trailer)
- **Mobile site** = portable
- **Reciprocal agreement** = use another company's facility
- **Subscription service** = paid service with shared facility

**Hot vs Redundant — when each is the answer:**
- "Minimal downtime, fast activation" → **Hot site** (general CISSP default for "minimal downtime")
- "Zero downtime, always running in parallel, most expensive" → **Redundant / Mirror site**
- Both are defensible; Hot is the more commonly tested CBK answer for "minimal downtime" framing

---

## Runbook vs Playbook (D7)

- **Playbook** = procedures for **specific incident types** (ransomware playbook, phishing playbook)
- **Runbook** = operational procedures (more general)

**Trap:** "Collection of procedures the IR team follows for specific types of incidents" → **Playbook**

---

## Insider Threat (D7)

**Employees cause the MOST computer crime losses** — not hackers, not contractors, not management.

---

## BIA Scope (D7)

**BIA prevents NOTHING** — it analyzes business impact (diagnostic). Don't pick BIA for "prevents disasters."

**Trap:** "Cannot prevent disasters" → BIA is a valid answer because BIA doesn't prevent (it identifies).

---

## DLP Types (D2)

- **Network DLP** = monitors traffic crossing network boundaries; prevents sensitive data from traveling from internal to external network (email, web upload, etc.)
- **Endpoint DLP** = installed on user devices; prevents users from **copying data to non-networked devices and external media** (USB sticks, external drives) + printing/screenshots
- **Storage DLP** = scans data at rest in repositories

**Trap:** if the question scopes specifically to "endpoint DLP," the answer is the USB/external-media one (not the network-egress one).

---

## Evidence Admissibility (D1, D7)

Three required criteria for evidence to be legally admissible:
- **Relevance** — pertinent to the case
- **Reliability** — technically sound, reproducible, intact chain of custody (NOT "accuracy" — accuracy is subjective)
- **Legality** — collected lawfully

**Trap:** Accuracy is NOT one of the admissibility criteria. Reliability is the technical concept; accuracy is subjective. Don't pick accuracy.

---

## CISSP "Test" Definition (D6)

CISSP's precise definition of a "test": **a procedure that records some set of properties or behaviors in a system being tested and compares them against predetermined standards.**

Contrast:
- **Test** = records properties + compares to standards
- **Assessment / Audit** = broader event of significant importance, against external standards
- **Vulnerability assessment** = identifies vulnerabilities
- **Penetration test** = determines weaknesses by exploitation

**Trap:** the test definition is the *precise / technical* one (record + compare). The "important event" framing is closer to assessment.

---

## Internal Pentest Disadvantage (D6)

Primary disadvantage of internal pentest team: **limited exposure to other approaches** to both securing and exploiting information systems. (Familiarity-bias is real but secondary — the structural issue is the team only sees their own org's techniques.)

---

## UL Gate Classes (D3, Physical Security)

UL classifies vehicular access gates as **Class I / II / III / IV (Roman numerals)**:
- Class I — Residential
- Class II — Commercial / General Access
- Class III — Industrial / Limited Access
- Class IV — Restricted Access (airports, prisons)

**Trap:** "Class B Commercial" uses a letter — that's the made-up one. All real UL gate classes use Roman numerals.

---

## Data Retention Policy (D2)

Considerations: **what type / how long / where stored**. **Cost is NOT a primary consideration** in retention policy (it's relevant for storage decisions but not the policy itself).

---

## NFC (D5)

**Near Field Communications** = short-range RF (a few centimeters) at **13.56 MHz** base frequency.

---

## Media Library Responsibility (D7)

The **media librarian** is responsible for the security and protection of media in a formal media library (NOT CISO/CIO who have organizational responsibility, NOT data owner).

---

## Network Scanning Purpose (D6)

**Network scanning identifies unauthorized hosts connected to the network**. Different from **vulnerability scanning** (which identifies potential vulnerabilities on a target host).

---

## High-Yield Facts

### Privacy & Compliance Laws (D1/D2)
- "financial institution + privacy notice" → **GLBA**
- "student education records" → **FERPA** (rights transfer parent→student at **18**)
- "online + under 13 + parental consent" → **COPPA** (PG-13=COPPA, 18=FERPA)
- HIPAA covered entities → **providers, plans, clearinghouses** (health/fitness app = NOT covered)
- "clearinghouse" → middleman that translates health data nonstandard ↔ standard (billing/claims)
- "breach notification + business associates + bigger penalties + EHR" → **HITECH** (HIPAA=original rules)
- "telecom must cooperate with wiretaps" → **CALEA** ("Carriers Assist Law Enforcement Agencies")
- "federal agency PII records" → **Privacy Act (1974)**
- **POPIA**=South Africa, **PIPL**=China, **PIPEDA**=Canada (all "GDPR-style")
- GDPR uniform because it's a **Regulation** (direct effect) not a Directive; EU is NOT a federation
- US breach laws → **no single federal law; 50 state laws; triggered by where customers RESIDE** (+ sector federal laws)
- **PCI DSS** = contractual (not law); enforced via card brands → **acquiring bank**; "may choose to pursue investigation" → **the bank**; merchant pays a **PFI**
- **SOX** = US law, public companies, internal controls over financial reporting, CEO/CFO certify (≠ **SOC** = vendor audit report)

### Quantitative Risk (D1)
- **SLE = AV × EF**; **ALE = SLE × ARO**; **EF = SLE ÷ AV**; **ARO = 1 ÷ years**
- ARO: 10yr=**0.1**, 100yr=**0.01**, 200yr=**0.005** (count zeros in years = decimal places; classic 10× trap)
- "rebuild/restore" → **replacement cost** (not purchase/original cost = historical price paid)
- Control cost > ALE → **accept** (formal, documented, senior-mgmt decision); insurance = **transfer**
- **Threat agent** (hacker) exploits **vulnerability** (missing patch) to realize **threat** (SQLi) → **impact** (defacement=integrity). Vulnerability ≠ threat. "malicious attacker" with no method listed = the **threat**
- tangible/intangible describes **assets & losses only** (not threats/vulns)

### BCP & BIA (D1)
- BCP order: **Scope&Planning → BIA → Continuity Planning → Approval&Implementation** (documentation is in Approval&Implementation, NOT Scope&Planning)
- Scope&Planning 4 activities: org analysis, BCP team, resource assessment, legal/regulatory review
- "ideal person to **approve** BCP" → **CEO** (most senior; CIO/CISO too narrow, COO runner-up)
- BCP **planning team** (builders) = business leaders + IT + support depts (+ senior mgmt liaison); **CEO is NOT on the team** (approves, doesn't build)
- **Initial** BCP training → **everyone** (org-wide awareness); "initial" = entry tier, not "first group"
- **Emergency Response Guidelines** = concise immediate-steps doc (procedures + notification/contact list + escalation)
- "loss of customer confidence" → **qualitative** impact (quantitative = $/numbers)

### Governance / Ethics / Metrics (D1)
- "assess processes used to **manage risk**" → **RMM** (Risk Maturity Model); CMM/SW-CMM = software/process maturity
- "**information security controls**, worldwide" → **ISO 27002** (27001 = the ISMS you certify against)
- **COBIT** = ISACA IT governance framework; **NIST RMF (800-37)** = Prepare/Categorize/Select/Implement/Assess/Authorize/Monitor
- (ISC)² Code of Ethics canons (priority order): **Society → Honorably → Service to principals → Profession**; CISSP bound by (ISC)² code + employer code; **RFC 1087** = non-binding advisory
- **KPI** = performance vs target (present) / **KGI** = goal achieved (outcome) / **KRI** = risk early-warning (forward); target present (95% aim) → **KPI**, not just a metric
- **NDA** → administrative control protecting confidentiality

### Threat Modeling & CIA (D1)
- **STRIDE**: Spoofing(Auth), Tampering(Integrity), Repudiation(Non-repud), Info Disclosure(Confidentiality), DoS(Availability), Elevation of Privilege(Authorization)
- info in **HTML comment** → **Information Disclosure** (the "I")
- **Reduction analysis** = decompose system into 5 elements (trust boundaries, data flows, input points, privileged ops, controls) via **DFD** (≠ data modeling)
- CIA quick-map: keylogger/sniffing → **Confidentiality**; load balancer/RAID/failover → **Availability**; defacement → **Integrity**

### Supply Chain & Ops (D1/D7/D3)
- "modified by **third party before delivery**" → **supply chain** / **interdiction** (defend with tamper-evident packaging + chain of custody)
- vendor security standard → "**handle our data the way we would**" (not just "comply with laws"; never "eliminate all risk")
- develop→review→approve→**different employee deploys** → **change management** (approval gate + separation of duties)
- **HVAC** → Availability control (+ attack surface: 2013 Target breach via HVAC vendor)
- **NTP** → time sync underpins log correlation, forensics, cert/Kerberos validity

### NIST 800-53 Control Selection (D1)
- **800-53** = catalog of **security AND privacy** controls (federal + widely adopted); controls in **families**; used with the **RMF**, always start from a **baseline**
- "which controls **apply to my org** / are appropriate/applicable" → **scoping** (eliminate the controls that don't apply, e.g. drop physical-datacenter controls for cloud-only)
- **tailoring** = the **broader** baseline customization = **scoping + compensating controls + org-specific parameter values** (e.g. setting password length)
- **scoping is a SUBSET of tailoring**: scoping = remove what doesn't apply; tailoring = full customization
- distractors (NOT control-selection): **bounds checking** = coding control vs **buffer overflow** (D8); **data stewardship** = data-governance role, day-to-day quality on owner's behalf (D2)

### Data Management Roles (D2)
- "select/apply **COBIT** to **balance security controls against business requirements**" → **business / mission owner** (owns a business unit/process; aligns IT-security with business via governance framework)
- "classify & protect **specific data** / assign classification / define access" → **data owner** (too narrow for the COBIT-balancing answer)
- "day-to-day **data quality** & management on the owner's behalf" → **data steward** (operational data-governance role)
- "processes data **on behalf of the controller**, follows instructions" → **data processor** (GDPR; sets no governance strategy)
- "day-to-day implementation (backups/patching/access enforcement)" → **data custodian** (owner decides, custodian does)
- DBA / sysadmin (backups, access enforcement, patching) → **data CUSTODIAN** (owner decides / custodian does; not owner, not steward)
- **COBIT discriminator**: "balance security vs business + COBIT" → **business owner**; "classify & protect the data" → **data owner**

### CASB & Security Tool Selection (D2/D7)
- "apply **security policies to user activity** in **cloud services** + report **exceptions** + visibility across a **growing number** of cloud services / **Shadow IT**" → **CASB** (Cloud Access Security Broker) — policy enforcement + visibility point **between users and cloud apps** (SaaS/IaaS); can add DLP/access control/threat protection
- **NGFW** = **network perimeter** protection (DPI, app awareness, IPS) — NOT cloud-SaaS user-activity governance
- **IDS** = detects/**alerts** on attacks — does NOT enforce cloud policies or manage cloud-app access
- **SOAR** = automates incident-response **workflows** across tools — a response-automation layer, NOT a cloud-policy/visibility broker
- CASB 4 pillars → **Visibility (Shadow IT) / Compliance / Data Security (DLP) / Threat Protection** (V-C-D-T)

### Data Classification & Sanitization (D2)
- "administrative process that assigns the appropriate **level of security controls** to **sensitive information** (by sensitivity)" → **data classification** (administrative control; protects **confidentiality**; tiers e.g. Public→Confidential / Unclassified→Top Secret)
- **Remanence** = residual **recoverable data left after deletion** — a *risk/problem*, NOT a control-assignment process
- **Transmitting / data in transit** = a data *state* (in motion), NOT a classification process
- **Clearing** = a *sanitization* method (**overwriting** so data isn't recoverable by standard tools) — removes data, doesn't classify it
- Sanitization strength: **clearing < purging < destruction**
- same sensitivity level reuse → **clearing**
- lower level / released outside → **purging**
- no reuse → **destruction**
- erasing = standard delete (not secure); sanitization = umbrella term
- **MECHANISM ladder** (how deep you scrub remnants): **delete = pointer/index entry only** (bits remain = remanence, undelete recovers) → **clearing = LOGICAL OVERWRITE** via normal system functions (defeats standard/"keyboard" recovery, NOT lab) → **purging = PHYSICAL-level** (multiple overwrites / firmware secure-erase / degauss; defeats lab/advanced) → **destruction = obliterate** (shred/crush/incinerate/pulverize)
- **Degaussing** scrambles ALL platter magnetism incl. factory **SERVO TRACKS** (head's lane-markings) → **permanently DESTROYS the HDD** (one-way; can't be reused) — magnetic only (HDD/tape)
- **Degaussing USELESS on SSD/flash** — they store **electrical charge**, not magnetism (gotcha: "degauss an SSD" → data intact)
- **SSD** → overwriting **unreliable** (wear-leveling hides data in spare cells) → use **built-in secure-erase or crypto-erase**, or destroy
- **Crypto-shred** (cryptographic erase) = **destroy the key** on an encrypted drive → data instantly unrecoverable; fast purge for SSDs/cloud
- **Bad sector/block** = a **faulty area the drive stops using**; **spare sector** = hidden **reserve** the firmware **REMAPS** the data to when a sector goes bad (theater reserve-seat: you move, but what's on the broken seat stays)
- Remapped (bad) sectors **still hold the original data** the OS no longer addresses → **overwriting can't reach it** = **remanence**, **lab-recoverable** (both HDD & SSD; defeats simple clearing)
- **HDD remaps occasionally** (on actual failure / G-list) vs **SSD remaps CONSTANTLY** (wear-leveling, every write) + **large over-provisioning (~7–28%)** → **SSD remanence WORSE** (multiple stale copies scattered in cells/spares)
- → **SSD needs firmware secure-erase or crypto-erase, NOT overwrite** (overwrite misses remapped/spare cells; degauss useless); **HDD** overwrite mostly works but misses remapped sectors → degauss/destroy to purge
- **Process vs scheme:** data classification = the **process** (assigns labels); information classification **system** = the **framework of levels + handling rules** it uses. **Owner assigns; controls flow from the level**
- **which baseline controls apply to a system** → based on the **DATA CLASSIFICATION it stores/handles** (classification → control level); **'business owner' = trap** (helps classify, but the criterion is the classification); **custodian implements**; **same-controls-for-all = wrong** (ignores classification). NB: org-level "which controls apply to my org" = **scoping** (different question)
- **Gov/military levels (high→low):** Top Secret > Secret > Confidential > Sensitive but Unclassified (SBU) > Unclassified
- **Commercial/private levels (high→low):** Confidential/Proprietary > Private > Sensitive > Public
- Commercial order high→low: **Proprietary/Confidential > Private > Sensitive > Public**; trap: 'Confidential' = HIGHEST in commercial but LOWEST classified in government; 'Sensitive' sounds high but is LOW in commercial
- Mixed-classification SYSTEM → classified at the HIGHEST level present = **high water mark** (TS+Secret+Confidential → Top Secret); one TS file makes the whole system + all users require TS clearance/controls
- **Gov disclosure-impact map:** Top Secret = **grave/exceptionally grave** damage; Secret = **serious** damage; Confidential = **damage** to national security ("grave"→TS, "serious"→Secret, plain "damage"→Confidential)
- Commercial damage map: Confidential=exceptional/grave, **Private=damage-not-exceptional + PII/personal info about individuals**, Sensitive=some, Public=none; PII (phone/address) + 'damage not exceptional' → PRIVATE (HIPAA context tempts Confidential — trap)
- **Commercial classification CRITERIA** (factors that drive the decision): **value/worth** (worth of the data to the org), **useful lifespan/age** (data loses value over time, may be declassified), **legal/regulatory** (HIPAA/PCI/GDPR), **sensitivity/criticality, usefulness**
- **Government/military criterion** = **impact to national security** (maps to TS=grave, Secret=serious, Confidential=damage) — this is the GOV criterion, NOT commercial
- **"NOT a common COMMERCIAL criterion?"** (lifespan / data value / national security / legal) → **impact to national security** (it's the GOVERNMENT criterion; value/lifespan/legal are all core commercial criteria). Hook: Commercial = **business value/lifespan/legal-regulatory**; Government = **damage to national security**
- spare/bad sectors + SSD over-provisioning common issue → **may not be cleared → data remanence** (NOT "not addressable" — that overstates; bad sectors were addressable pre-remap)
- **data/information = INTANGIBLE asset** (no physical form, **NOT** because of value); **storage media = tangible**; **"data value" = a classification criterion, not an asset type** (value ≠ intangibility — tangible assets have value too)
- **What determines the VALUE of data?** four buckets: **COST** (create/replace/maintain — replace cost often huge/impossible) + **UTILITY** (operational value/revenue/usefulness/timeliness — stale data worth less) + **EXPOSURE** (competitor value/liability if disclosed/reputation) + **LEGAL/IP** (regulatory, intellectual property)
- **Three-lens hook:** data value = what it **COST** you (create/replace) + what it's **WORTH** to you (operational/revenue/usefulness) + what it'd **COST if compromised** (competitor/liability/reputation)
- **Flow:** higher value → higher classification → stronger controls. Risk tie-in: **"cost to replace" = replacement cost**; **"cost if disclosed/lost" = impact behind SLE/ALE**; valuing the asset is **step one of risk assessment**
- **high-quality media cost-effective** → **VALUE OF DATA far exceeds media cost** (small premium negligible vs data value/liability); **"less likely to fail" is TRUE but NOT the cost-effectiveness reason** (it's a media property); "easier to encrypt" / "improves integrity" = false. Secondary real-world note (NOT the exam reason): durable media can also be sanitized & reused, amortizing cost
- **high-quality media = high ENDURANCE** (SSD **TBW/DWPD** = rewrite cycles) + **reliability** (**MTBF**) + **enterprise build** (power-loss protection, 24/7-rated, longer warranty); **endurance matters MOST for sanitize-and-reuse** (each **clearing = a rewrite**); examples → **enterprise HDD / high-TBW SSD / LTO tape / M-DISC** (vs consumer HDD / QLC SSD / old tape / CD-DVD-R)
- EOL workstations + trade secrets → **destruction** (no reuse + highly sensitive = max assurance); 'sanitizing' too general (umbrella); reuse/resale → purge instead
- classified tapes: degauss-and-reuse NOT allowed → **data REMANENCE** concern → destroy (not 'permanence' = wordplay; degaussing DOES work on tapes — they're magnetic; bit-rot = irrelevant)
- downgrading classified system (TS→Secret) for reuse → concern = **sanitization cost may exceed new-equipment cost** (rigorous purging is expensive; reuse-vs-replace flips at high classification). Runner-up distractor = TS/Secret commingle/remanence.
- **WHY declassification > hardware cost:** paying for **CLEARED LABOR + VERIFIED ASSURANCE + RISK of a classified spill**, not the wipe (hardware cheap, trust expensive); classified media usually **kept-at-level-for-life or destroyed, rarely downgraded**
- **Cost picture (illustrative):** commercial sanitize = **pennies–tens of $/drive** (destruction often CHEAPER than purging); classified verified-downgrade = **$400–1,600+/device cleared labor** (rivals/exceeds hardware) + **spill-risk tail** → **destroy+rebuy wins**; pay for **ASSURANCE not the wipe**
- **GOV vs COMMERCIAL same wipe** — gov costs more b/c **MANDATED assurance**: cleared labor + prescribed standards (NSA/DoD/NIST 800-88) + verification/sign-off + near-**ZERO** acceptable residual risk (national-security downside). Commercial = cost-benefit/accept residual risk (cheap); gov = comply regardless of cost (expensive/destroy)
- **purge vs destroy cost gap = NOT equipment** (degausser ≈ shredder ~$5k–50k) but **VERIFICATION + SPEED**: destruction self-evident (no verification, seconds/drive); purging must be **PROVEN** (verification cost) + overwrite takes time → destruction's assurance is **free**, purging **buys** it

### Data Retention & Liability (D2)
- "how does a **retention policy reduce liability**?" → **less to breach** (smaller attack surface — destroyed data can't be stolen) + **less to subpoena** in **e-discovery** (legitimately destroyed data doesn't exist to produce) + **defensible/consistent destruction** + stays within **regulatory min/max retention**. Principle: **don't keep what you don't need**
- **Legal hold** (litigation hold) → **SUSPENDS** the retention/destruction schedule the moment litigation is **reasonably anticipated**; you must STOP destroying relevant data and preserve it (overrides routine destruction)
- **Spoliation** = destroying/altering/concealing evidence relevant to **known or anticipated litigation** → **illegal**, severe penalties (sanctions, adverse inference, default judgment)
- Trap: **routine** pre-litigation destruction **reduces** liability; destruction **after** a legal hold **increases** it (= spoliation)
- Laws set **both MIN and MAX** retention → keep long enough (e.g., tax records) AND delete when no longer needed (e.g., **GDPR storage limitation**); avoids fines either way

### Data Lifecycle (D2)
- "**first step** of the data lifecycle" → **collect/create** (you can't label, store, or analyze data that doesn't exist yet)
- order → **Collect/Create → Store → Use → Share → Archive → Destroy**
- distractors NOT the first step: **labeling/classification** comes after collection; **policy** = governing framework around the whole lifecycle (not a step); **analysis** = part of **Use** (later)
- identify **END-OF-LIFE** data for disposal → **TAGGING** (metadata: creation date/retention/classification makes expired data findable → retention policy disposes). NOT **rotation** (media/key cycle) / **DRM** (usage control) / **DLP** (exfiltration)
- **SCRUBBING** data (remove outdated/duplicate/unneeded info) → **data MAINTENANCE** phase. Trap: 'data remanence' is NOT a lifecycle phase (residual leftover data = a risk). 'Scrub data' = cleanse (quality) / sanitize (PII) / integrity-scrub (bit rot)

### Security Baselines & the Absolutes Trap (D1)
- "**why use a security baseline?**" → it's a **good starting point that can be tailored** to the org — a pre-defined **minimum set of controls** you then **scope** (remove non-applicable) and **tailor** (customize). **Saves designing controls from scratch**. Chain: **baseline → scoping + tailoring → fitted to org**
- **Absolutes-are-usually-wrong pattern:** answer choices with **all / always / never / prevents / ensures / eliminates / guarantees** are typically **WRONG** — security = risk reduction, not certainty; the **measured/realistic** option wins
- Why the baseline-question distractors failed (all absolutes): "applies to **all** circumstances" (no baseline fits every case — that's why you tailor); "**preventing** liability" (compliance ≠ immunity); "**ensures** always secure" (nothing guarantees always-secure). Right answer = "**starting point that can be tailored**"
- **scoping vs tailoring TELL:** "match the **SPECIFIC SYSTEMS**" → **SCOPING** (system-driven applicability; match controls + assessment procedures to the system; keep relevant, drop the rest); "align with **ORG mission/needs**" → **TAILORING** (broader umbrella; scoping is part of it). Distractors: **asset mgmt** = inventory; **compliance** = regulatory. (Alice Q: matches controls/procedures to specific systems → scoping)

### Data Discovery (D2)
- **Sensitive data scanning / data discovery tool** = scans systems/storage/DBs/files to **find WHERE sensitive data lives** (PII/PHI/PCI) via **pattern matching** (regex SSNs/credit cards) + keywords + classification labels
- Principle: **"can't protect what you don't know you have"** — surfaces unknown/forgotten data (e.g., SSNs on a random share)
- **First step → feeds classification: find → classify → protect**; commonly a feature of **DLP and CASB** platforms
- Parallels the **CASB Visibility pillar** (shadow apps) and **EDR/Defender** device discovery — same "find the unknown" idea aimed at **sensitive DATA**
- **3 discovery approaches = metadata-based / content-based / analytics-based**
- **"Asset metadata search" = metadata-based** (searches labels/attributes about the data; **fast, misses unlabeled**)
- **"Sensitive data scanning" = content-based** (pattern matching of the data itself; **thorough, heavier**); analytics-based = ML/context/behavior

### In-Memory Databases (D8/D2)
- **In-memory / memory-resident DB** = data stored primarily in **RAM** (Redis, SAP HANA, Memcached) for speed; **volatile** — lost on power-off unless persisted (snapshots/WAL/replication)
- **Risk** = data is **data in use** — sits **unencrypted in RAM**, exposed via **cold-boot attack** (RAM retains data briefly after power-off) or **memory dump**; **disk/at-rest encryption doesn't help** — need encryption-in-use/memory protection
- **Persistence** (solves volatility) = **snapshots/savepoints** (full copy to disk; SAP HANA savepoints / Redis RDB) + **transaction/WAL logs** (replay on top of snapshot → near-zero loss) + **replication** (mirror to other nodes = HA) (+ **battery-backed RAM/NVDIMM**)
- **Danger only when persistence is OFF**: Redis as a **pure cache with no persistence loses ALL data on restart** — fine if rebuildable cache, **catastrophic as system of record**
- Durability ties to **RPO** — how much data you can afford to lose sets snapshot/log frequency

### Data Tiering (D2)
- **Data tiering** = match **storage speed/cost to access frequency**: **Hot** (RAM/NVMe SSD) → **Warm** (SSD/fast HDD) → **Cold** (HDD / cloud IA) → **Archive** (tape/Glacier)
- Driving principle = **cost-vs-performance proportionality** (don't pay for fast media for rarely-accessed data); often automated via lifecycle policies
- **Cold/cheap ≠ unprotected** — archived data still needs encryption + access control; colder tiers = **slower retrieval** (Glacier hours) → affects **RTO**

### AES & TLS (D3)
- **AES** = **symmetric block cipher**, **128-bit blocks**, **128/192/256-bit keys**, based on **Rijndael**; the global symmetric standard (replaced DES/3DES); fast; data at rest AND in transit; no practical break
- **TLS** = a **protocol** (not a cipher) securing data **in transit**, successor to SSL, the **S in HTTPS**; provides **confidentiality + integrity + authentication**
- **Relationship (hybrid):** TLS handshake uses **asymmetric (RSA/ECDHE)** to authenticate + exchange the session key → then switches to **symmetric AES** for **bulk** encryption. Asymmetric to **set up** (secure but slow), symmetric/AES to **do the work** (fast)
- **Trap:** "Is TLS a cipher?" → **No, it's a protocol that USES ciphers like AES**

### MAC in TLS + 3 meanings (D3)
- **MAC in TLS** = **Message Authentication Code** = a value appended to each message giving **integrity + authenticity** via **HMAC** (e.g., HMAC-SHA256) — sender computes over message+shared key, receiver recomputes & compares; mismatch → rejected. **NOT confidentiality (AES does that)**; MAC sits **alongside** the encryption
- **Full TLS split:** confidentiality = **AES** / integrity+authenticity = **MAC/HMAC** / authentication+key exchange = **asymmetric (RSA/ECDHE) + certificates**
- **3 meanings of MAC** (context decides): **Message Authentication Code** (crypto integrity, TLS) / **Mandatory Access Control** (labels/clearances model, D5) / **Media Access Control** (Layer 2 MAC address, D4)

### Encryption by Data State (D2/D3)
- **At rest → AES** (symmetric cipher; actually encrypts stored files on disk/file server)
- **In motion/transit → TLS** (transport protocol; secures data on the wire)
- **"TLS at rest" and "VPN at rest" are WRONG** — both protect data *in motion* (transport), neither encrypts stored files
- **"DES at rest" is WRONG** — DES is obsolete/broken (56-bit); never pick it over AES
- EXAM Q "best encryption for proprietary data on a file server + in motion?" → **AES at rest, TLS in motion**

### Labeling & DLP (D2)
- **Labeling lets DLP identify sensitive data by its classification label** (**metadata-based** detection — read the tag, no deep content scan) and **auto-enforce policy** (**block/quarantine/encrypt/alert**) **across all 3 states** (at rest / in transit / in use)
- A **label = machine-readable instruction that travels WITH the data** → every system knows how to handle it → classification + labeling is what makes **automated DLP enforcement** possible
- **Metadata-based = fast** (reliable when labeled correctly); **content scan = fallback** for **UNLABELED** sensitive data (regex/pattern matching catches what has no label)

### CIS Benchmark vs PCI DSS (D1/D3)
- **"harden a SPECIFIC OS"** (e.g., a **Win11 box processing credit cards**) → **CIS BENCHMARK** = the **OS hardening baseline** (the HOW: vendor-neutral, consensus, settings-level config, **L1/L2 profiles**, **maps to PCI DSS**)
- **PCI DSS = the compliance OBLIGATION** (the WHAT), **NOT a host config baseline** — the credit-card detail is a **distractor** pulling toward PCI DSS; PCI DSS even points you to CIS to do the hardening
- **Microsoft Win11 baseline** = the **vendor's own** → solid **runner-up** (CIS is independent + tiered + more recognized for compliance); **NSA baseline** = **high-security/government, often overly restrictive** for a commercial card system
- **CIS Benchmarks ≠ CIS Controls** — Benchmarks = OS/app secure-config hardening guides; **CIS Controls = a prioritized list of ~18 controls** (see "CIS Controls Categorization" above). Don't conflate.

### GDPR Roles (D1/D2)
- **Data Controller** = determines the **purposes & means** of processing (the **WHY/HOW**) — e.g., the org that collects the data and decides why/how it's used
- **Data Processor** = processes data **on behalf of** the controller, per instructions — e.g., a **3rd-party analytics firm** you send data to → **processor**
- **Data Subject** = the **individual** the data is about
- **"Owner" is NOT a GDPR term** — GDPR uses **controller / processor / data subject**; "owner" is a data-governance role (don't conflate vocabularies)
- **Tell:** "send to a 3rd party to process/analyze **on your behalf**" → **processor**; "decides **why & how**" → **controller**

### Reputational Impact (D1/D2)
- "greatest **REPUTATIONAL** impact to **data at rest**?" → **DATA BREACH** (it **publicly exposes** the data → known to customers/regulators/media → loss of **customer confidence** = **qualitative** impact)
- distractors are **causes or internal issues**, not the public outcome: **improper classification** = internal control weakness (may lead to a breach, not visible itself); **decryption** = technical concern (only matters if it causes exposure); **intentional insider threat** = a **CAUSE/threat actor**, not the impact — damage comes from the **BREACH** it produces (threat-vs-impact)
- Hook: reputational damage = **public exposure** → only the **breach** is the public, reputation-damaging **OUTCOME**

### Breach Notification + Encryption Safe Harbor (D1)
- **Regulator vs Individuals = different thresholds.** **GDPR Art 33** = notify the **REGULATOR** within **72h** UNLESS *"unlikely to result in a risk"* (risk-based, not automatic). **GDPR Art 34** = notify **AFFECTED INDIVIDUALS** only if **HIGH risk** → **encrypted/unintelligible data is EXEMPT**
- **US state encryption safe harbor** → breached data **encrypted + keys NOT compromised** = notification **generally not required**
- **NOT a blanket "report everything regardless of impact"** — risk thresholds + encryption exemptions exist; **BUT tightening** (SEC cyber-incident rule, EU **DORA/NIS2**, sector rules push broader/stricter disclosure); *"unlikely to result in a risk"* = a defensible **judgment call** → orgs often **over-report** to be safe
- Encryption is only a safe harbor if **STRONG + current + keys safe** (weak cipher / stolen key voids it). **NET:** encryption can **prevent a breach from being reportable** (esp. to individuals) — not an automatic universal pass; jurisdiction/sector-specific

### Planned Obsolescence & EOL/EOS (D3/D7)
- **Planned obsolescence** = product **deliberately designed with a limited lifespan** → wears out / outdated / loses vendor support → **forces replacement/upgrade**
- **Security risk:** drives products to **EOL/EOS** → once support ends, **no more security patches** → newly found vulns **never fixed**
- **EOL** (End of Life) = vendor stops **selling/producing**; **EOS** (End of Support) = vendor stops **patching** → **EOS is the security-critical date** (watch: EOS can also = End of Sale)
- **Legacy/unsupported** systems = a growing **unpatchable attack surface** (e.g., EOL Windows still in production)
- **Fix:** manage the **asset lifecycle** — track EOL/EOS dates and **retire/replace BEFORE support ends**

### Asset Retention & Lifecycle (D2/D3)
- **Manufacturer lifecycle order:** General Availability → End of Sale → End of Life (EOL) → **End of Support (EOS = LAST event, security-critical, no more patches)**
- **Asset retention** = manage how long hardware/software/data is kept (lifecycle discipline); **risks** = EOL/EOS unpatchable + bigger attack surface + lost documentation/orphaned assets; **asset-side cousin of data retention**

### Enforcing Windows Baselines — GPO (D1/D3)
- enforce/verify a **Windows security baseline across many PCs** (settings set AND kept set) → **Group Policy (GPO)** — centralized + **auto-refresh corrects DRIFT** (reapplies the baseline, resets changed settings back); both applies AND continuously enforces
- **startup scripts** = apply only at **startup**, no continuous refresh / no drift correction (weaker)
- **spot-check / periodic review with data owner** = **manual / governance**, NOT technical enforcement
- Trigger: "enforce + auto-correct a Windows baseline across many PCs" → **GPO**
- GPO PREREQUISITE = domain-joined (AD); exam implies it. Non-domain fallback = **Intune/MDM** (NOT startup scripts — central scripts also need AD). Domain-joined→GPO; Azure AD/cloud/remote→Intune

### DRM vs DLP (D2)
- **DRM** = **usage control of content AFTER distribution** — copy/print/forward/edit/screenshot/expiry; the protection **TRAVELS WITH THE FILE** (persistent rights — still applies after the file leaves your network). *"What can you DO with this file?"* Enterprise version = **IRM** (Microsoft Purview / Azure RMS)
- **DLP** = **exfiltration prevention at the boundary** — detect/block sensitive data LEAVING where it shouldn't (egress/network/endpoint/storage monitoring). *"Is sensitive data LEAVING?"*
- **Tell:** "follows the file / enforces rights wherever it goes" → **DRM/IRM** (persistent); "blocks sensitive data at the boundary/egress" → **DLP**

### Stolen vs Lost Media (D2)
- backup **tapes STOLEN** → **AES-256 encryption** (theft = **confidentiality** risk; encryption makes stolen media **unreadable** without the key)
- **"keep multiple copies" = availability, NOT confidentiality** → trap; doesn't stop a thief reading the stolen tape (also "replace tapes w/ HDD" = drives get stolen too; "security labels" = thief ignores them)
- rule: **STOLEN → encryption**; **LOST/destroyed → backups/copies**

### NIST SP 800-88 (D2)
- **NIST SP 800-88 = "Guidelines for Media Sanitization"** — authoritative US standard; **SOURCE of the Clear / Purge / Destroy** framework
- **Clear** = logical overwrite (standard recovery) < **Purge** = secure-erase/degauss/crypto-erase (lab recovery) < **Destroy** = physical (nothing left)
- **Choose method by 2 factors:** (1) **data sensitivity / security categorization** + (2) **does the media leave org control** → higher sensitivity + leaving control → **purge or destroy**
- **Media-type aware** (degauss useless on flash/SSD → secure-erase/crypto-erase); **verify + document** the sanitization

### Protocol & Crypto Quick-Ref (D3/D4)
- **Telnet** = insecure (port 23) → use **SSH**; **ISDN** = legacy (BRI/PRI); **UDP** = fast/unreliable (connectionless)
- **BitLocker** (Windows) / **FileVault** (macOS) = full-disk encryption (FDE) via **AES**
- **AES** / **Serpent** (AES finalist) / **IDEA** (early PGP, old) = symmetric block ciphers
- **TLS** = transport security (SSL successor); **IPsec** = network-layer IP (**AH** = integrity + **ESP** = encryption); **VPN** = encrypted tunnel (often IPsec/TLS)

### Hardest Place to Protect a Key (D3)
- Hardest place to protect an encryption key → **IN MEMORY** (must be plaintext to use = **data in use**; cold-boot / memory-dump / malware).
- **Disk** = encrypt at rest (key wrapping / TPM / HSM); **network** = encrypt in transit (TLS / IPsec); **memory can't be wrapped while in use** → hardest.

### Tangible vs Intangible Inventory (D2/D3)
- **Tangible inventory** (hardware/media/facilities) = **asset tags** (barcode/RFID) + **automated network discovery** + **CMDB** — physical/visible, easy to tag & scan.
- **Intangible inventory** (data/IP/licenses/goodwill/processes) = **data discovery** + **classification** + **documentation/registers** (IP registers, license/entitlement tracking) — **can't barcode data**, must discover & record.
- Both serve **"you can't protect what you don't know you have"** — tangible you find physically/on the network; intangible you discover & document.
- Centralizing: tangible → **CMDB**; intangible → category registries (**data catalog**/RoPA for data, **SAM/license** tools for software, **IP/contract registers** for legal), unified via ITAM/data-governance/GRC. No single 'intangible CMDB'.

---

## Pre-exam Last-Mile Checklist

- [ ] OOP terms cold (encapsulation/abstraction/modularity/naturalness/reusability/cohesion/coupling)
- [ ] ACID cold (atomicity/consistency/isolation/durability)
- [ ] SDLC methodologies cold (Scrum vs Agile vs Spiral vs RAD)
- [ ] CMM levels exact phrasing (Level 4 = "planned, performed, measured, controlled")
- [ ] Hashing sizes (MD5=128, SHA-1=160, SHA-256=256)
- [ ] Smart cards (Combi=1 chip dual / Hybrid=2 chips)
- [ ] Baseband vs Broadband (entire vs divided)
- [ ] WEP=RC4 / WPA3=SAE
- [ ] H.323 international audio/video / SONET fiber physical
- [ ] OSI device-layer mapping with Gateway=L7
- [ ] Disaster < Catastrophe terminology
- [ ] Law definition (rules by govt OR society, binding, enforced)
- [ ] Evidence admissibility = Relevance + Reliability + Legality
- [ ] Async tokens = challenge/response
- [ ] OIDC RP = web app, Auth Code flow most secure
- [ ] IPSec for IP / TLS for transport / HTTPS for web
- [ ] DevSecOps for cross-team collab
- [ ] CIS Controls = Basic/Foundational/Organizational

## Related

- [reading-patterns](reading-patterns.md) — the 4 cross-domain reading patterns
- [OOP Concepts](../../domains/08-software-development-security/OOP%20Concepts.md) — D8 deep dive
- [ACID Properties](../../domains/08-software-development-security/ACID%20Properties.md) — D8 deep dive
- [Development Methodologies](../../domains/08-software-development-security/Development%20Methodologies.md) — D8 deep dive
- [Disaster Classifications](../../domains/01-security-and-risk-management/Disaster%20Classifications.md) — D1 deep dive
- [Smart Card Types](../../domains/05-identity-and-access-management/Smart%20Card%20Types.md) — D5 deep dive

