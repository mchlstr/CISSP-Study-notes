# Anki Deck — Domain 7 (Security Operations)

> Format: `Question :: Answer` (Obsidian_to_Anki compatible). Pruned for exam-yield: atomic, gradeable cards only.

## Recovery Sites

Cold site? :: Space, power, HVAC, comms only — NO equipment or data. Slowest, cheapest (days–weeks).
Warm site? :: Cold + hardware and connectivity, but STALE data. Hours–days; mid cost.
Hot site? :: Fully equipped + near-real-time data. Fastest (minutes–hours); most expensive.
What is a mirror (redundant) site? :: A full, real-time duplicate of the primary — instant failover, most expensive.
What is a mobile recovery site, and its defining trait? :: A portable data center (container/trailer); defining trait is PORTABILITY, not readiness (can be cold or warm).
What do ALL recovery sites fundamentally depend on? :: POWER and COOLING — the constant; only equipment and data currency vary by tier.
Why locate a recovery site geographically remote? :: So a regional disaster doesn't take out the primary and recovery sites at once.

## DR/BCP Plan Testing

DR test types in order of increasing rigor/disruption? :: Read-through (checklist) → walkthrough (tabletop) → simulation → parallel → full-interruption.
Parallel vs full-interruption test — key difference? :: Parallel = recovery site runs alongside production (no downtime); full-interruption = primary is shut down and operations move to the recovery site (most disruptive, highest risk).
What is a tabletop (walkthrough) test? :: Team talks through the DR plan in a discussion — no systems are activated; finds gaps cheaply.

## Operations & Detection

What is NTP, and why is it security-relevant? :: Network Time Protocol — synchronizes clocks; accurate time underpins log correlation, forensic timelines, and Kerberos/cert validity.
What is SOAR? :: Security Orchestration, Automation, and Response — automates incident-response workflows across multiple security tools.
Cyber Kill Chain stages (Lockheed Martin), in order? :: Recon → Weaponization → Delivery → Exploitation → Installation → Command & Control (C2) → Actions on Objectives.

## Logging, Monitoring & SIEM

What is a SIEM? :: Security Information and Event Management — centrally aggregates and CORRELATES logs from many sources for real-time analysis, alerting, dashboards.
What is circular overwrite (logging), and the risk? :: When a log fills, the OLDEST entries are overwritten — risks losing evidence if logs aren't archived first.
What is log normalization? :: Converting logs from different formats into one common format so they can be correlated.
Why centralize logs (vs leaving on each host)? :: Protects logs from local tampering, enables cross-system correlation, supports retention/analysis.
What governs log retention and disposal? :: Retention policy + legal/regulatory requirements — keep long enough for investigation/compliance, then dispose securely.

## Logging Scenarios (Application)

Scenario: After an incident the relevant logs were already overwritten. What setting caused it, and the fix? :: Circular overwrite — fix with larger logs + central aggregation/archival (ship to SIEM) before rotation.
Scenario: Failed-login alerts are so frequent real attacks get lost. What setting helps? :: Set an appropriate clipping level/threshold so only abnormal counts alert.
Scenario: Correlating an attack across firewall/server/IDS logs fails because times don't line up. Cause? :: Clocks aren't synchronized — deploy NTP.
Scenario: You need one tool to collect, correlate, and alert on logs enterprise-wide in real time. What is it? :: A SIEM.

## Investigations & Forensics

First step at an investigation scene? :: Secure the scene — protect from contamination/alteration before collecting evidence.
What is Locard's Exchange Principle? :: Every contact leaves a trace — a perpetrator brings something to and takes something from the scene.
What does MOM stand for (investigations)? :: Motive, Opportunity, Means.
Order of volatility (forensics)? :: Collect MOST volatile first — CPU/RAM/live data (lost on power-off), then disk, then archives/backups.
What is chain of custody? :: A documented record of who handled evidence, when, where, how — proves integrity, keeps it admissible.
Evidence types — real vs direct vs documentary? :: Real = tangible objects (the actual drive); Direct = testimony from a witness's own senses; Documentary = documents/copies.
What is the Best Evidence Rule? :: The ORIGINAL document is preferred over copies when proving content.
Five qualities of good evidence? :: Authentic, Accurate, Complete, Convincing, Admissible.
Three criteria that make evidence ADMISSIBLE? :: Relevant, Reliable (competent), and legally Permissible (obtained lawfully).
The four types of investigations? :: Criminal, Civil, Regulatory, Administrative.
Burden of proof — criminal vs civil? :: Criminal = "beyond a reasonable doubt" (highest); Civil = "preponderance of the evidence" (>50%).
Regulatory vs administrative investigation? :: Regulatory = government agency, legal/regulatory compliance; Administrative = internal/operational (HR/policy), lowest burden.

## Forensics Scenarios (Application)

Scenario: A compromised server is still running. What do you collect FIRST? :: Volatile/live evidence (RAM, processes, network connections) — order of volatility; lost on shutdown.
Scenario: A defense attorney claims evidence "could have been altered." What defeats this? :: Chain of custody — documented controlled handling from collection to court.
Scenario: You must prove a contract's contents; you have the original and a photocopy. Which? :: The original — Best Evidence Rule.
Scenario: An employee is investigated internally for a policy violation (not a crime). Type and burden? :: Administrative — lowest burden of proof.
Scenario: A prosecutor must convict a hacker. What standard must evidence meet? :: Beyond a reasonable doubt (criminal — highest burden).

## Incident Response

Incident response phases, in order? :: Preparation → Detection → Response → Mitigation (Containment) → Reporting → Recovery → Remediation → Lessons Learned.
Event vs incident? :: Event = any observable occurrence; incident = an event that NEGATIVELY affects security. Every incident is an event; not every event is an incident.
What is Containment/Mitigation, and when does it happen? :: Limiting damage / stopping spread (isolate affected systems) — done BEFORE eradication/recovery.
Recovery vs Remediation? :: Recovery = return to normal operation; Remediation = fix the ROOT CAUSE so it doesn't recur.
Common detection sources for IR? :: SIEM, IDS/IPS, DLP, antivirus/EDR, firewalls, environmental sensors, user reports.

## IR Scenarios (Application)

Scenario: Ransomware is spreading across the LAN. Immediate priority action? :: Containment — isolate affected systems to stop the spread before eradication/recovery.
Scenario: A failed login appears in logs but nothing was compromised. Event or incident? :: An event — it becomes an incident only if it adversely affects security.
Scenario: After fully recovering, leadership asks "are we done?" Remaining phase? :: Lessons Learned — review and improve so it doesn't recur.
Scenario: Systems are clean and online, but the original vulnerability is still present. Which phase is incomplete? :: Remediation — recovery returned to normal, but the root cause must be fixed.

## Patching

Agent vs agentless vs passive patch detection? :: Agent = installed software reports status; agentless = remote scanning, no agent; passive = infers patch level from network traffic.
How should patches be deployed? :: Through CHANGE MANAGEMENT — test in non-production first, schedule, then deploy. A patch can break functionality.

## Change Management

What identifies "change management" in a scenario? :: An approval gate before production + separation of duties (someone other than the developer deploys).
Regression testing vs change management? :: Regression testing = a test type (did the change break anything?); change management = the controlled approval/deployment PROCESS.
Change management process steps? :: Change request → assess impact → approval → build & test → notification → implement → validation → update baseline.
What is a CAB vs ECAB? :: CAB (Change Advisory Board) reviews/approves NORMAL changes; ECAB (Emergency CAB) fast-tracks urgent emergency changes.
Standard vs normal vs emergency change? :: Standard = pre-approved routine low-risk; normal = full CAB review; emergency = expedited via ECAB.
What is done in change validation? :: Confirm it worked: test new functionality AND run regression testing.
Why update the version/baseline after a change? :: Configuration management — the baseline must reflect the current approved state to stay auditable.

## Patching & Change Scenarios (Application)

Scenario: A critical zero-day patch must go out immediately, outside the normal window. Process/board? :: Emergency change via the ECAB — still documented, just fast-tracked.
Scenario: An admin pushes a patch straight to production and it crashes the app. What was skipped? :: Change management — assess impact + test in non-production first.
Scenario: You want patch status across thousands of endpoints without installing anything. Which method? :: Agentless (remote scanning).
Scenario: After a change, the new feature works but an old one broke. What should have caught it? :: Regression testing (part of validation).

## Failure Modes

Fail-safe vs fail-secure? :: Fail-safe prioritizes LIFE safety (defaults open/unlocked — doors unlock on fire). Fail-secure prioritizes ASSET protection (defaults locked/denied).
What is fail-soft? :: On failure the system continues in a DEGRADED/reduced mode rather than shutting down completely.

## Backups

What is the archive bit? :: A flag set when a file is created/modified, indicating it needs backing up; backup types differ in whether they clear it.
Full backup? :: Backs up ALL data; clears the archive bit. Slowest backup, fastest restore (one set).
Incremental backup? :: Changes since the LAST backup (any type); clears the archive bit. Fastest backup, slowest restore (full + ALL incrementals).
Differential backup? :: Changes since the last FULL backup; does NOT clear the archive bit. Restore = full + the LAST differential only.
Incremental vs differential — backup vs restore speed? :: Incremental = fast backup / slow restore. Differential = slower backup / fast restore.
How are backups validated? :: Periodic TEST RESTORES (a backup is only good if it restores) + checksums.
What is tape rotation (GFS)? :: Grandfather-Father-Son — a scheme for reusing backup tapes balancing retention vs media cost.

## Off-site Data Strategies

Electronic vaulting vs remote journaling vs remote mirroring? :: Vaulting = bulk DB backups transferred off-site periodically; journaling = transaction logs sent off-site (smaller RPO); mirroring = live real-time copy (smallest RPO, most expensive).

## Recovery Time Objectives

What is MTD? :: Maximum Tolerable Downtime — the longest a process can be down before unacceptable harm.
RTO vs RPO? :: RTO = how fast you must RECOVER (time to restore, ≤ MTD); RPO = how much DATA you can afford to LOSE.
RPO drives what choice? :: Backup/replication frequency — a tighter RPO requires more frequent backups.

## High Availability & RAID

RAID 0? :: Striping for performance — NO redundancy (one disk fails = all data lost).
RAID 1? :: Mirroring — exact copy on a second disk; survives one failure (50% overhead).
RAID 5? :: Striping with distributed parity; 3+ disks; survives ONE disk failure.
RAID 6? :: Striping with DOUBLE parity; survives TWO simultaneous disk failures.
Does RAID replace backups? :: No — RAID gives availability/fault tolerance but doesn't protect against deletion, corruption, ransomware, or disaster.
What is clustering (HA)? :: Multiple systems acting as one so that if a node fails, others take over (failover).
Cold vs warm vs hot spare? :: Cold = on the shelf (must install); warm = installed standby (manual switch); hot = live, automatically takes over.

## Recovery Scenarios (Application)

Scenario: Full backup Sunday, differential nightly. Fails Thursday — how many sets to restore? :: Two: Sunday's full + Thursday's (last) differential.
Scenario: Full Sunday, incremental nightly. Fails Thursday — what do you restore? :: Sunday's full + Mon, Tue, Wed, Thu incrementals (full + ALL).
Scenario: Array survives one failed disk and keeps serving data. Which RAID minimum, and why still back up? :: RAID 5 (survives 1 disk); back up anyway — RAID doesn't protect against deletion/corruption/ransomware.
Scenario: The business can lose at most 1 hour of data. Which metric, and what does it drive? :: RPO = 1 hour — drives backup/replication frequency (at least hourly).
Scenario: Fire alarm triggers; door locks release so people exit. What failure mode? :: Fail-safe (life safety over asset protection).

## Log Data Reduction & Clipping

What is a clipping level? :: A predefined THRESHOLD below which events are ignored/not recorded (e.g., log a failed login only after the 3rd attempt). A fixed-rule, NONstatistical way to cut logged data volume.
Reduce stored log volume using a NONstatistical method — which technique? :: Clipping levels (fixed threshold). Sampling also reduces data but is STATISTICAL, so "nonstatistical" rules it out.
Clipping level vs sampling — statistical or not? :: Clipping level = nonstatistical (fixed threshold); sampling = statistical (representative subset).

## CISSP Exam-Outline Gap-Fill

EDR vs XDR vs MDR? :: EDR = Endpoint Detection & Response (detect/respond on endpoints); XDR = Extended (correlates across endpoint + network + cloud + email); MDR = Managed (a vendor runs it for you).
What is UEBA? :: User and Entity Behavior Analytics — baselines normal user/device behavior and flags anomalies (insider threat, compromised accounts).
Threat intelligence — IOC vs TTP? :: IOC = Indicators of Compromise (hashes, IPs, domains — the "what", easy to change); TTP = Tactics, Techniques, Procedures (attacker behavior — the "how", harder to change).
What is threat hunting? :: Proactively searching for threats already inside the environment (hypothesis-driven), instead of waiting for alerts.
What is a duress code (personnel safety)? :: A secret signal that silently indicates coercion (e.g., entering a special PIN under threat) — life safety is the priority.
DRP key components? :: Response, personnel/notification, communications, assessment, restoration, and training/lessons-learned.
Whitelisting/allow-listing vs sandboxing vs honeypot (operations defenses)? :: Allow-listing = only approved programs run (deny by default); sandboxing = run untrusted code isolated; honeypot = decoy to lure/study attackers.

## Recovery-Site Selection Scenarios (Application)

Scenario: Tight budget and the process can tolerate several days of downtime. Which recovery site? :: Cold site — cheapest; only space/power/HVAC, so slowest to bring up.
Scenario: You need operations to continue with essentially zero downtime, sustainable long-term — cost is no concern. Which site? :: Redundant (mirror) site — duplicate running in parallel; near-zero downtime.
Scenario: You can afford pre-installed hardware but will reload data from the last backup; recovery in hours-to-days. Which site? :: Warm site — equipment ready, data stale, mid cost.
Scenario: Two firms agree to host each other's operations after a disaster. Name it and its main weakness. :: Reciprocal agreement — cheap, but capacity/confidentiality issues and may fail if both firms are hit.
Scenario: RTO is a few hours and you need near-real-time data, with budget available. Which site? :: Hot site — equipped and replicated, fastest realistic cutover.

## DR Test & Backup-Type Selection Scenarios (Application)

Scenario: You must validate the DR plan cheaply without activating any systems. Which test? :: Tabletop / walkthrough — discussion only, lowest cost and disruption.
Scenario: You want to confirm the recovery site actually works without disrupting production. Which test? :: Parallel test — recovery site runs alongside production, no downtime.
Scenario: Leadership wants the highest-confidence proof the plan works and accepts real downtime/risk. Which test? :: Full-interruption test — primary shut down, ops moved to recovery site.
Scenario: Goal is to minimize the nightly backup window and storage; restore speed is secondary. Which backup type? :: Incremental — smallest/fastest backup; slow restore (full + all increments).
Scenario: Goal is fast restore from just two sets while keeping backups shorter than a full. Which type? :: Differential — restore = full + last differential only.

## Off-site Data & RAID Selection Scenarios (Application)

Scenario: You need the smallest possible data loss with a live off-site copy. Which strategy? :: Remote mirroring — real-time replication, smallest RPO (most expensive).
Scenario: You want continuous off-site transaction logs with a smaller RPO than periodic bulk transfers. Which strategy? :: Remote journaling — ships transaction logs off-site.
Scenario: The array must keep serving data through TWO simultaneous disk failures. Minimum RAID level? :: RAID 6 — striping with double parity.
Scenario: Only two disks available but you must survive one disk failure. Which RAID? :: RAID 1 — mirroring (survives one failure, 50% overhead).

## Control Selection & Foundational-Principle Scenarios (Application)

Scenario: Management wants to know after the fact WHO accessed a system. Preventive or detective control, and an example? :: Detective — audit logs / log review (and CCTV review); preventive would block access up front.
Scenario: Two vulnerabilities: an internet-facing critical RCE and an internal low-severity bug. Patch which first, and why? :: The internet-facing critical RCE — prioritize by risk (severity x exposure/exploitability), not by count.
Scenario: One employee can both create and approve vendor payments. Which principle is violated? :: Separation of duties — split the steps so no single person controls the whole transaction.
Scenario: A user keeps admin rights "just in case" but the role never needs them. Which principle is violated? :: Least privilege — grant only the access the job requires.
Scenario: You want to surface hidden fraud by forcing staff out of their duties periodically. Which control? :: Mandatory vacation — absence exposes fraud that requires the perpetrator's daily involvement.
Scenario: You rotate staff through different roles periodically to deter and detect fraud. Which control? :: Job rotation — also cross-trains and reduces single points of knowledge.
Scenario: A critical action must require two authorized people acting together. Which control? :: Dual control (two-person integrity) — splitting it forces collusion to abuse.
Scenario: An incident is confirmed and contained. Which phase must complete BEFORE recovery? :: Eradication — remove the malware/root cause first, then restore.
