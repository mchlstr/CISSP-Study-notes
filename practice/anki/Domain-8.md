# Anki Deck — Domain 8 (Software Development Security)

> Format: `Question :: Answer` (Obsidian_to_Anki compatible). Pruned for exam-yield: atomic, gradeable cards only.

## Secure Coding Controls

What is bounds checking, and what does it prevent? :: Verifying input stays within allocated memory limits BEFORE writing — prevents buffer overflows.
Where must input validation always be performed, and why? :: Server-side — client-side validation is UX only and CAN be bypassed (the attacker controls the client).
Allow-list vs deny-list input validation — which is preferred? :: Allow-list (define what IS permitted, reject the rest) — safer; deny-list always misses something.

## Web Application Vulnerabilities

What is XSS, and who is the target? :: Cross-Site Scripting — injecting malicious script that runs in the victim's BROWSER (the CLIENT). Steals sessions, keystrokes, redirects.
The three types of XSS (and which is most dangerous vs most common)? :: Stored/Persistent (saved on server, hits all viewers — most DANGEROUS), Reflected (crafted link echoed back — most COMMON), DOM-based (client-side only, never hits server).
What is CSRF, and who is the target? :: Cross-Site Request Forgery — tricks the victim's browser into sending a FORGED authenticated request; targets the SERVER (acts as the logged-in user).
XSS vs CSRF — key difference? :: XSS targets the CLIENT (runs script in the user's browser); CSRF targets the SERVER (forges an authenticated request riding the user's session). Opposite targets.
What is SQL injection, and its primary defense? :: Injecting SQL via unsanitized input so attacker commands run on the DB (data theft/modification). Defense = parameterized queries (prepared statements) + input validation.

## Secure SDLC

What does "bake in security" mean (and why)? :: Build security into every SDLC phase from the start — defects found in requirements/design cost far less to fix than ones found in production.
SLC vs SDLC? :: SLC = the whole SYSTEM life cycle (incl. hardware/operations/disposal); SDLC = the SOFTWARE development life cycle specifically.
SDLC phases? :: Plan (+ mgmt approval) → Requirements → Architecture & Design → Development → Testing → Certification → Deployment/Accreditation → Operations → Disposal.

## Development Methodologies

Waterfall vs Agile? :: Waterfall = sequential/rigid (good for fixed requirements); Agile = iterative SPRINTS with frequent feedback (good for changing requirements).
What is the Spiral model? :: A RISK-driven iterative model — each loop repeats plan/design/build/evaluate and includes an explicit risk-analysis and prototyping step before proceeding.
Waterfall vs Spiral vs Agile — defining trait of each? :: Waterfall = sequential phases; Spiral = risk-driven iterations with prototypes; Agile = lightweight, feedback-driven sprints.
Cohesion vs coupling (which is desirable)? :: Cohesion = how focused a module is on one task (HIGH is good); coupling = how dependent modules are on each other (LOW is good).
What is a Scrum Master? :: The facilitator in Scrum/Agile who removes impediments and keeps the process running (not a traditional boss).
DevOps vs DevSecOps? :: DevOps = Dev + QA + Ops merged for continuous delivery; DevSecOps = DevOps with SECURITY integrated throughout the pipeline ("shift left", automated into CI/CD).
What is a canary deployment? :: Releasing a change to a SMALL subset of users/servers first to catch problems before a full rollout.
Certification vs accreditation (software deployment)? :: Certification = the TECHNICAL evaluation that the system meets requirements; Accreditation = MANAGEMENT's formal authorization to deploy/operate (accepts the risk).

## APIs, Obfuscation & Acquisition

REST vs SOAP? :: REST = lightweight, typically JSON, stateless (web/mobile-friendly); SOAP = XML-based, rigid/standardized, with built-in WS-Security.
What is code obfuscation? :: Making code hard to read/reverse-engineer while keeping it functional (protects logic/IP).
What must you do when ACQUIRING third-party software? :: Assess the vendor's security and put security requirements in contracts/SLAs — you inherit their risk.

## Software Vulnerabilities

What is a buffer overflow? :: Writing more data than a buffer holds, overwriting adjacent memory — can crash or let an attacker run code / modify memory. Prevented by bounds checking.
What is a backdoor / trapdoor? :: Hidden code that bypasses normal authentication for covert access (sometimes a leftover dev/maintenance hook).
What is object/memory reuse? :: Residual data left in memory or a reused object that a new process can read — an information leak (clear/zeroize on release).
What is the citizen-developer risk? :: Non-professional employees building apps with low-code/no-code tools — fast, but often bypasses security review, testing, and governance.
What is SCM (software configuration management)? :: Tracking/controlling versions and changes to code and artifacts (version control, baselines) so builds are known and reproducible.

## Software Dev Scenarios (Application)

Scenario: Team wants to ship fast with changing requirements and short feedback loops. Which methodology? :: Agile (iterative sprints) — Waterfall suits fixed requirements.
Scenario: Security keeps getting bolted on at the end, causing rework. What fixes this? :: DevSecOps — integrate security throughout the pipeline.
Scenario: You release a new version to 5% of servers first to limit blast radius. What is this? :: A canary deployment.
Scenario: A developer left hidden code that logs in bypassing authentication. What is this? :: A backdoor/trapdoor.
Scenario: A finance employee builds a critical app in a low-code tool with no security review. Concern? :: Citizen-developer risk — skips governance, testing, controls.
Scenario: An app leaks another user's data left in reused memory. What weakness? :: Object/memory reuse.

## Database Concepts

Relational DB terms — row, column, cell? :: Row = tuple/record; column = attribute; cell (row×column intersection) = a field.
Primary key vs foreign key? :: Primary key uniquely identifies a row in ITS table (no null/duplicate); foreign key references a primary key in ANOTHER table (links tables, referential integrity).
What is concurrency control / database locking for? :: Managing simultaneous access so transactions don't corrupt data or read inconsistent values (one transaction locks a record so others wait) — supports isolation.

## ACID Properties

What does ACID stand for? :: Atomicity, Consistency, Isolation, Durability — properties guaranteeing reliable transactions.
Atomicity? :: All-or-nothing — a transaction fully completes or fully rolls back (no partial changes).
Consistency? :: A transaction moves the DB from one VALID state to another (all rules/constraints satisfied).
Isolation? :: Concurrent transactions don't interfere — each behaves as if running alone.
Durability? :: Once committed, data PERSISTS even through a crash/power loss.

## In-Memory Databases

What is an in-memory database, examples, and its data state? :: A DB storing data primarily in RAM for speed (Redis, SAP HANA) = data IN USE.
Main security risk of an in-memory database? :: Sensitive data sits unencrypted in RAM — exposed via memory dumps, cold-boot attacks, or malware reading process memory. Disk/at-rest encryption does NOT cover it.
How do in-memory databases avoid losing data on power loss, and the DR tie? :: Persistence — snapshots to disk + transaction/WAL logs + replication. Snapshot frequency ties to RPO. Danger: a cache with persistence disabled loses all data on restart.

## Database Scenarios (Application)

Scenario: Two users update the same record at once and one update is lost. Which ACID property/mechanism? :: Isolation — enforced via concurrency control/locks.
Scenario: A transfer debits one account but crashes before crediting the other. Which ACID property prevents a half-done transfer? :: Atomicity (all-or-nothing rollback).
Scenario: Ensure every order row references a real customer. What feature enforces this? :: A foreign key (referential integrity).

## Database & Language Discriminators

What is ODBC? :: Open Database Connectivity — a standard API that lets application code retrieve data from a database regardless of the DBMS. JDBC is the Java equivalent.
Compiled vs interpreted languages (examples)? :: Compiled (translated ahead of time): C, C++, Fortran, Java (to bytecode). Interpreted (executed line-by-line at runtime): VBScript, JavaScript, Python, Perl, PHP.
Distributed database model? :: Data stored across multiple databases but LOGICALLY connected — the user sees a single entity though it spans many interconnected parts over a network. (Hierarchical/relational describe structure, not physical distribution.)

## CISSP Exam-Outline Gap-Fill

What is the OWASP Top 10? :: The most critical WEB-application security risks. Key entries: Injection (SQLi), Broken Access Control, Identification/Authentication failures, Cryptographic failures, Security Misconfiguration, XSS, Vulnerable/outdated components, SSRF.
COTS vs GOTS vs open-source software? :: COTS = Commercial off-the-shelf; GOTS = Government off-the-shelf (custom for a gov org); open-source = inspectable but YOU own vetting/patching. All carry third-party/supply-chain risk.
What is software supply chain risk, and mitigations? :: Risk from third-party code/dependencies/build pipeline (e.g., a poisoned library or update — SolarWinds). Mitigate with SBOM, dependency scanning, code signing, vendor assessment.
What is CI/CD, and its security concern? :: Continuous Integration / Continuous Delivery — an automated build/test/deploy pipeline that can push to production fast; secure it with automated security tests, secrets management, and signed artifacts.
What is mobile code (applets/ActiveX), and the control? :: Code downloaded and executed in the browser (Java applets, ActiveX, JavaScript); run it in a sandbox with restricted privileges — legacy mobile code is a common attack vector.
Software security maturity — CMM vs SAMM/BSIMM? :: CMM/CMMI = general process maturity; SAMM (OWASP) and BSIMM = software-ASSURANCE/security maturity models specifically.
Security concern with acquired SaaS/managed services in development? :: You inherit the provider's security — assess them, use contracts/SLAs, and retain responsibility for your data (shared responsibility).

## Methodology Selection Scenarios (Application)

A high-risk project needs explicit risk analysis and a prototype evaluated before each iteration proceeds. Best methodology? :: Spiral — risk-driven iterations with prototyping at each loop.
Requirements are fully known, stable, and the customer wants a fixed plan with formal sign-off per phase. Best methodology? :: Waterfall — sequential and rigid; suits fixed, well-defined requirements.
You need a working prototype in front of users very quickly to refine the design through their feedback. Best methodology? :: RAD (Rapid Application Development) — speed via rapid prototyping over heavy planning.
The exam asks the best methodology for a "complex, changing environment." Pick the umbrella term, not the framework. :: Agile — choose the umbrella (Agile) over the subset (Scrum).
Teams want continuous flow with work-in-progress limits and no fixed-length sprints. Best fit? :: Kanban — continuous flow with WIP limits (Scrum uses fixed sprints).
Management wants to compare two vendors' software-process maturity, and one is "documented and standardized org-wide." Which CMMI level? :: Level 3 — Defined (documented, standardized processes).

## Vulnerability-from-Symptom Scenarios (Application)

A user's session cookie is stolen after they view a comment another user posted on the site. Vulnerability? :: Stored (persistent) XSS — malicious script saved server-side runs in every viewer's browser.
A logged-in user clicks an emailed link and their account silently changes its email address. Vulnerability and defense? :: CSRF — defend with anti-CSRF tokens (and SameSite cookies).
Entering `' OR 1=1 --` in a login field returns all rows. Vulnerability and best defense? :: SQL injection — defend with parameterized queries / prepared statements.
An app crashes and runs attacker code after a long input overruns a fixed-size field. Vulnerability and defense? :: Buffer overflow — defend with bounds/length checking (input validation).
The fix proposed for a SQLi flaw is "filter out single quotes on the client side." Why is this wrong? :: Client-side filtering is bypassable and deny-list-based — use server-side parameterized queries instead.

## Database Confidentiality Scenarios (Application)

A user with access to many unclassified records can deduce a classified fact from them. What problem, and the control? :: Aggregation enabling inference — control with polyinstantiation or restricting/aggregating access.
The DB shows a low-clearance user a fake "cover story" row while high-clearance users see the real one. What technique? :: Polyinstantiation — multiple rows with the same key at different classification levels to defeat inference.
A user reasons from data they CAN see to sensitive data they cannot. Name the threat. :: Inference — deducing protected information from accessible data.

## Secure-Coding & Acquisition Scenarios (Application)

To stop tampered software from running, the team wants assurance the binary is unaltered and from a trusted source. Control? :: Code signing — digital signature proves integrity and origin.
You're acquiring a closed-source product and fear the vendor may go bankrupt and orphan it. What arrangement protects you? :: Software escrow — a third party holds the source code, released if the vendor fails.
Before integrating an open-source library, what do you need to manage its components and known vulnerabilities? :: An SBOM plus dependency scanning — track components and patch known CVEs (you own the vetting).
A public REST API must limit abuse and verify callers without sessions. Two key controls? :: Authentication tokens (OAuth/API keys) plus rate limiting / throttling.
