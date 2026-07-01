# Anki Deck — Domain 2 (Asset Security)

> Format: `Question :: Answer` (Obsidian_to_Anki compatible). Pruned for exam-yield: atomic, gradeable cards only.

## Data Management Roles

What is the Business/Mission Owner responsible for? :: Owns a business process; balances security requirements against business needs (uses a governance framework like COBIT to align IT/security with business objectives).
What is the Data Owner responsible for? :: Classifying specific data and defining its protection/access — focus is the data itself. (The owner DECIDES.)
Data owner vs data custodian? :: Owner DECIDES (classification, access, protection requirements); custodian DOES the day-to-day technical implementation (backups, patching, access enforcement). A DBA is a custodian.
Data custodian vs data steward? :: Custodian = technical caretaker (backups/patching/access); steward = data QUALITY and content governance on the owner's behalf.

## GDPR Roles

GDPR controller vs processor vs data subject? :: Controller = determines the PURPOSES & MEANS (the why/how); Processor = processes on the controller's behalf per instructions (e.g., a 3rd-party analytics firm); Data Subject = the individual the data is about.
What is a Supervisory Authority (SA) under GDPR? :: The national data-protection regulator that enforces GDPR and receives breach notifications (within 72h, Art 33).

## Cloud & Tool Selection

What is a CASB? :: Cloud Access Security Broker — sits between users and cloud services; enforces security policy on cloud-app user activity, discovers Shadow IT, can add DLP/access control/threat protection.
The 4 pillars of CASB? :: Visibility (Shadow IT discovery), Compliance (policy + report exceptions), Data Security (DLP), Threat Protection.
CASB vs NGFW vs IDS vs NAC? :: CASB = policy/visibility for CLOUD-app user activity; NGFW = network perimeter (DPI/IPS); IDS = detects/alerts (no enforcement); NAC = governs NETWORK access.

## Data Discovery

What is a data discovery tool, and why run it first? :: Software that scans systems/storage to locate sensitive data (PII/PHI/PCI). Run first because you can't protect what you don't know you have — it feeds classification and controls.
How do data discovery tools recognize sensitive data? :: Pattern matching (regex for SSNs/cards), keywords, and classification labels.
The three data discovery approaches? :: Metadata-based, Content-based, Analytics-based (ML/context).
Metadata-based vs content-based discovery? :: Metadata = search the tags/labels ABOUT the data (fast, misses unlabeled); content = scan the data itself via pattern matching (thorough, catches unlabeled, heavier).
Labeling vs content scanning for DLP enforcement? :: Labels = fast metadata-based enforcement (a machine-readable instruction that travels with the data); content scanning = fallback to catch UNLABELED sensitive data.

## DRM vs DLP

DRM vs DLP? :: DRM = usage control of content AFTER distribution (copy/print/forward/expiry) — protection TRAVELS WITH THE FILE; DLP = prevents exfiltration at the egress BOUNDARY ("is data leaving where it shouldn't?").
Which protection follows the file even after it leaves your network? :: DRM (persistent usage rights travel with the file); DLP mostly enforces at the egress boundary.

## Data Classification & Sanitization

Which administrative process assigns controls by sensitivity, and which CIA element? :: Data classification — protects Confidentiality.
What is data remanence? :: Residual recoverable data left on media after deletion — a risk, not a control-assignment process.
Why isn't deleting or formatting a file secure? :: They remove only the pointer/index; the actual bits remain (data remanence) and are recoverable. Use clearing/purging/destruction.
Clearing vs purging vs destruction? :: Clearing = overwrite via normal functions (defeats standard recovery, NOT lab attacks). Purging = secure-erase/degauss/crypto-erase (defeats lab attacks). Destruction = physical (nothing left). Strength: clearing < purging < destruction.
What is NIST SP 800-88, and the two factors choosing the method? :: "Guidelines for Media Sanitization" (source of Clear/Purge/Destroy). Method depends on (1) data confidentiality level and (2) whether the media leaves the org's control.
Sanitization trigger by destination? :: SAME sensitivity level / stays in trusted environment → Clearing; LOWER level or released OUTSIDE the org → Purging; no reuse / EOL / highly sensitive → Destruction.
Why is purging the wrong answer for same-level reuse? :: Overkill — clearing meets the need when data stays at the same sensitivity level. Match the method to where the media goes.
What does degaussing do, and what does it work on? :: A strong magnetic field scrambles platter magnetism (incl. servo tracks → HDD unusable). Works on HDDs and magnetic TAPES; does NOTHING to SSDs (electrical charge, not magnetism).
What is crypto-shredding (cryptographic erase)? :: Encrypt the media, then destroy the key → data instantly unrecoverable. Fast purge method for SSDs/cloud.
Why is overwriting unreliable on SSDs, and the fix? :: Wear-leveling + over-provisioning leave stale copies in spare/remapped cells the OS can't address. Use firmware secure-erase or crypto-erase (degauss is useless); destroy for high assurance.
Why do spare/bad (remapped) sectors cause data remanence? :: The original data stays in the remapped sector the OS no longer addresses — overwriting (clearing) can't reach it, but a lab can recover it.

## Destruction vs Purging Decisions

Decision rule — when to destroy vs purge media? :: Destroy = no reuse + highly sensitive / EOL disposal (max assurance). Purge = reusing/reselling at a lower level or outside the org.
Why is highly classified media usually destroyed rather than purged & reused? :: Verified declassification (cleared labor + proven assurance + spill risk) costs more than cheap replaceable hardware, and residual-data risk is unacceptable at that level.

## Classification Schemes

Government classification levels (high→low)? :: Top Secret (grave damage) > Secret (serious damage) > Confidential (damage) > Sensitive but Unclassified > Unclassified.
Commercial classification levels (high→low)? :: Confidential/Proprietary > Private > Sensitive > Public.
Trap: where does 'Confidential' rank — commercial vs government? :: Commercial = HIGHEST (= Proprietary, trade secrets); Government = LOWEST classified level.
Commercial level for PII (phone/address) causing 'damage but not exceptional'? :: Private — the personal-data tier, just below Confidential. (HIPAA context tempts "Confidential," but non-medical PII + not-exceptional = Private.)

## Classification Process & Criteria

Classification process vs information classification system? :: The PROCESS assigns labels; the SYSTEM is the framework of levels + handling rules. Owner assigns; controls flow from the level.
How do you determine which baseline controls apply to a system? :: By the DATA CLASSIFICATION of the data it handles — higher classification → stronger controls (not by asking a person one step removed).
Commercial vs government classification criteria? :: Commercial = business value, useful lifespan, legal/regulatory, sensitivity. Government = damage to NATIONAL SECURITY.
What is the high water mark principle? :: A system is classified at the HIGHEST level of any data it holds; all controls must meet the most sensitive data's requirements. (Confidential+Secret+TS system = Top Secret.)
Categorization vs Classification? :: Categorization = group by impact level (FIPS 199 Low/Mod/High); Classification = assign a sensitivity level.

## Asset Types & Valuing Data

Is data a tangible or intangible asset, and why? :: Intangible — it has NO physical form. The storage media holding it is tangible; losing the data usually costs more than the hardware.
Three-lens summary of data value? :: What it COST you (create/replace) + what it's WORTH to you (operational/revenue) + what it'd COST if compromised (competitor value, liability, reputation).
How does data value connect to risk assessment? :: "Cost to replace" = replacement cost; "cost if disclosed/lost" = the impact behind SLE/ALE. Valuing the asset is step one of risk assessment.

## Data Retention & Liability

How does a data retention policy reduce liability? :: Less retained data = smaller attack surface and less to subpoena; consistent documented destruction is legally defensible; stays within regulatory min/max. Principle: don't keep what you don't need.
What is a legal hold (litigation hold)? :: When litigation is reasonably anticipated, it SUSPENDS normal retention/destruction — you must STOP destroying relevant data and preserve it.
What is spoliation? :: The intentional/negligent destruction or alteration of evidence relevant to known/anticipated litigation — illegal, severe penalties.
Routine vs post-hold destruction — liability? :: Routine, documented, policy-driven destruction BEFORE litigation REDUCES liability (defensible business practice); destroying AFTER a legal hold attaches INCREASES it (spoliation).
Why do laws set both a MINIMUM and MAXIMUM retention period? :: Minimums require keeping records long enough (e.g., tax); maximums require deleting when no longer needed (e.g., GDPR storage limitation).
What is defensible destruction? :: Destroying data via a documented, consistent, legally-defensible process so it holds up in litigation.

## Data Lifecycle

Typical data lifecycle order? :: Collect/Create → Store → Use → Share → Archive → Destroy.
First step of the data lifecycle? :: Collection/Creation — you can't label, store, or analyze data that doesn't exist yet.
Which phase is scrubbing data (removing outdated/duplicate info)? :: Data Maintenance — ongoing organizing/updating/cleansing to keep data accurate during its useful life.
Technique to identify end-of-life data for disposal? :: Tagging — metadata (creation date, retention period, classification) makes expired data findable so retention policy can dispose of it on schedule.

## Data Tiering

What is data tiering, and the tiers fast→slow? :: Storing data on different storage classes by access frequency/criticality: Hot (RAM/NVMe SSD) → Warm (SSD/fast HDD) → Cold (HDD/cloud IA) → Archive (tape/Glacier). Principle: match cost/speed to use.
Security caveat with cold/archive tiers? :: Cheap/cold ≠ unprotected — still needs encryption & access control; slower retrieval (Glacier hours) affects RTO/availability.

## Data States & Encryption

Default encryption-by-state rule of thumb? :: At rest → AES; In motion/transit → TLS. (DES is obsolete — never pick it over AES.)
Why is 'TLS at rest' or 'VPN at rest' wrong? :: TLS and VPNs protect data IN MOTION (transport), not stored files. At rest needs a cipher like AES.
Best control if backup TAPES are STOLEN, and why not 'keep multiple copies'? :: AES-256 encryption — theft = confidentiality risk; encryption makes the tape unreadable without the key. Multiple copies protect AVAILABILITY, not confidentiality (wrong threat).

## Encryption in Motion

Link vs end-to-end encryption (header visibility)? :: Link = entire packet incl. headers encrypted, but plaintext at EACH hop. End-to-end = headers visible for routing, payload never exposed at intermediate nodes.
What is onion routing? :: Layered encryption (Tor) — each relay peels one layer; provides ANONYMITY since no single node knows both source and destination.

## Privacy — Data Categories & Identifiers

PII vs SPI vs PHI vs PI? :: PII = identifies a person; SPI = Sensitive Personal Info (race/religion/health/biometrics — extra protection); PHI = Protected Health Info (HIPAA); PI = broad "personal information."
Direct vs indirect vs online identifiers? :: Direct = alone identifies (name/SSN/passport); Indirect = re-identifies when combined (ZIP+DOB+gender); Online = IP/cookie/device IDs (personal data under GDPR).
OECD Privacy Guidelines — the 8 principles? :: Collection Limitation, Data Quality, Purpose Specification, Use Limitation, Security Safeguards, Openness, Individual Participation, Accountability.
Why 'you cannot achieve privacy without security'? :: Security controls (encryption, access control) are the foundation that ENABLES privacy.

## Labels & Markings

Security Label vs Security Marking? :: Label = machine-readable classification metadata (for systems/DLP); Marking = human-readable visible banner (e.g., "CONFIDENTIAL", for people).

## Scenarios (Application)

Scenario: A drive that held Secret data is SOLD AS SURPLUS (leaves the org). Minimum sanitization? :: Purge at minimum (destroy if highly sensitive) — once media leaves your control, clearing is insufficient.
Scenario: A workstation processed Top Secret data and is now END OF LIFE (no reuse). What do you do? :: Destroy the drive — no reuse + highly sensitive = maximum assurance.
Scenario: Media reused at the SAME classification level. Cheapest sufficient sanitization? :: Clearing — it stays in the same trusted environment, so overwriting is enough; purging is overkill.
Scenario: An admin "degausses" an SSD to wipe it. What's wrong? :: Degaussing does nothing to SSDs (flash = charge, not magnetism) — data survives. Use secure-erase/crypto-erase or destroy.
Scenario: Courier loses unencrypted backup tapes. Best single control? :: AES-256 encryption — theft = confidentiality risk; encrypted tapes are useless without the key.
Scenario: Hybrid-cloud org can't see/govern user activity across growing SaaS apps. Best tool? :: A CASB — visibility (Shadow IT) + policy enforcement for cloud-app activity.
Scenario: An EU retailer sends customer data to a third-party analytics firm. Under GDPR, that firm is? :: A data processor (processes on the controller's behalf, per instructions).
Scenario: Classify patient PII (phone/address, NOT medical), exposure = damage but not exceptional. Level? :: Private — non-medical PII + not-exceptional = Private (HIPAA tempts "Confidential").
Scenario: A system stores Confidential + Secret + Top Secret data. How is it classified? :: Top Secret — high water mark.
Scenario: Find unlabeled sensitive data scattered across file shares. Which approach? :: Content-based discovery (pattern matching) — metadata/label search misses unlabeled data.
What is the PRIMARY goal of an asset management program? :: To prevent losses — tracking/protecting assets is the means; preventing loss (theft, untracked decommissioning, breaches, wasted licenses) is the business outcome.
Asset management: "accurate inventory / keep systems updated / tag assets" — goal or activity? :: Activities (the HOW). The GOAL is the outcome they serve: prevent losses / protect the organization.

## Scenarios II — Decision Points & Traps

Scenario: A hospital must dispose of failed SSDs holding patient data; degaussing is proposed. Best method? :: Cryptographic erase or physical destruction — degaussing does nothing to flash/SSD (no magnetic state).
Scenario: A batch of archival CD-ROMs holding Confidential records must be sanitized. Best method? :: Physical destruction (shred/incinerate) — optical media can't be overwritten or degaussed.
Scenario: Failed backup TAPES holding Secret data are being returned to the vendor for warranty. Sanitization? :: Degauss or destroy — tape is magnetic, so degaussing works (unlike on SSDs); destroy if reuse isn't needed.
Scenario: Org runs sensitive workloads in a public cloud and can't physically destroy the disks. How to sanitize at decommission? :: Cryptographic erase (crypto-shred) — destroy the keys; you don't control the hardware.
Scenario: A DBA performs backups, patching, and enforces the access list someone else defined. Which data role? :: Custodian — implements controls; the owner DECIDES classification and access.
Scenario: Who decides a dataset's classification level? :: The data owner — classification is a decision/accountability function, not a custodian/administrator task.
Scenario: An employee ensures customer records stay accurate, complete, and consistent. Which role? :: Data steward — responsible for data quality/content on the owner's behalf (not technical caretaking).
Scenario: A SaaS analytics vendor starts using client data to build its OWN product. Under GDPR, its role shifts to? :: Controller — it now determines a new purpose/means; processors only act on the controller's instructions.
Scenario: Litigation is reasonably anticipated and a legal hold is issued. What happens to scheduled destruction? :: Suspend it — preserve all relevant data; destroying it now is spoliation.
Scenario: Records are shredded on the normal schedule one week before a lawsuit is filed but reasonably foreseeable. Problem? :: Likely spoliation — duty to preserve attaches when litigation is reasonably anticipated, not only when filed.
Scenario: An EU company suffers a personal-data breach. Who must be notified, and how fast? :: The supervisory authority within 72 hours (GDPR Art. 33).
Scenario: A dataset has no names but contains ZIP + date of birth + gender. Privacy concern? :: Indirect (quasi-) identifiers — combined they re-identify individuals, so it's still personal data.
Scenario: Logs store only IP addresses, cookie IDs, and device IDs. Is this personal data under GDPR? :: Yes — online identifiers count as personal data.
Scenario: A field records employees' union membership and health conditions. Data category? :: Sensitive Personal Info / special-category data — requires heightened protection.
Scenario: A new system will process Secret data. How are its baseline controls chosen? :: By the data classification it handles — higher classification drives stronger baseline controls.
Scenario: Security must stop staff copying sensitive files to USB drives and printing them. Which DLP? :: Endpoint DLP — it controls local device/port and print actions.
Scenario: Security must block sensitive data from being emailed or uploaded out of the network. Which DLP? :: Network DLP — it inspects traffic at the egress boundary.
Scenario: A contract requires a file to stay non-copyable/non-forwardable even after a partner receives it. DLP or DRM? :: DRM — usage controls travel with the file; DLP mostly stops data at your boundary.
Scenario: Tax law says keep records 7 years; GDPR says don't keep longer than needed. How does the retention policy reconcile this? :: Set a minimum (regulatory floor) AND a maximum (delete when purpose ends) — keep within both bounds.
Scenario: Before launching a classification program, the org doesn't know where its sensitive data lives. First action? :: Run data discovery — you can't classify or protect what you haven't located.
