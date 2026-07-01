# Anki Deck — Domain 6 (Security Assessment & Testing)

> Format: `Question :: Answer` (Obsidian_to_Anki compatible). Pruned for exam-yield: atomic, gradeable cards only.

## Verification & Validation

Verification vs Validation? :: Verification = "did we build it RIGHT?" (meets spec); Validation = "did we build the RIGHT thing?" (meets user needs).

## Levels & Methods of Testing

The four levels of testing (small→large)? :: Unit (individual components in isolation) → Interface (connections between components) → Integration (combined components together) → System (complete integrated system end-to-end).
Manual vs automated testing? :: Manual = a human tests (flexible, good for logic/judgment); automated = tools run tests (fast, repeatable, scalable).
Static vs dynamic testing? :: Static = analyze code WITHOUT running it (code review, SAST); dynamic = test the program while it RUNS (DAST).
What is fuzz testing, and mutation vs generation? :: Sending malformed/random input to find crashes/flaws. Mutation = randomly MODIFY existing valid inputs; Generation = CREATE inputs from scratch per the format/spec.

## Access to Code & Test-Case Techniques

White-box vs black-box vs gray-box testing? :: White-box = FULL knowledge of internals/source; black-box = NO internal knowledge (outside, like an attacker); gray-box = PARTIAL knowledge.
Positive vs negative testing? :: Positive = verify it works with VALID inputs; negative = verify it handles INVALID/unexpected inputs gracefully.
What is misuse (abuse-case) testing? :: Testing how the system behaves when deliberately misused/attacked (attacker's-eye-view cases).
Boundary value analysis vs equivalence partitioning? :: BVA tests the EDGES of input ranges (min/max/just in/out — where bugs cluster); equivalence partitioning tests ONE representative per equivalent class (efficiency).

## Operational Testing

Real User Monitoring (RUM) vs synthetic monitoring? :: RUM = passively observes ACTUAL user traffic; synthetic = runs SCRIPTED/simulated transactions to test performance proactively.
What is regression testing? :: Re-testing after a change to confirm existing functionality still works (the change didn't break anything).

## Assessors & SOC Reports

Test vs assessment vs audit? :: Test = checks one control/mechanism works; Assessment = broad review of multiple controls (often internal, advisory); Audit = formal evaluation against a standard by an INDEPENDENT party, producing attestation.
Internal vs external vs third-party assessors? :: Internal = the org's own staff (least independent); external = engaged outsiders; third-party = independent (SOC audits/attestation).
SOC 1 vs SOC 2 vs SOC 3? :: SOC 1 = controls over clients' FINANCIAL reporting; SOC 2 = Trust Services Criteria (security/availability/integrity/confidentiality/privacy), restricted/NDA audience; SOC 3 = a PUBLIC general-use summary of SOC 2.
SOC 2 Type 1 vs Type 2? :: Type 1 = control DESIGN at a point in time; Type 2 = control EFFECTIVENESS over a period (6–12 months) — more rigorous/valuable.
Who oversees the audit function at the top? :: The audit committee (of the board) — independent oversight of audits and controls.

## Assessment Scenarios (Application)

Scenario: A client needs assurance about a SaaS provider's control EFFECTIVENESS over the past year. Which report? :: SOC 2 Type 2 (effectiveness over a period). Type 1 only covers design at a point in time.
Scenario: A provider wants a publicly shareable assurance doc for marketing. Which report? :: SOC 3 (public summary). SOC 1/2 are restricted.
Scenario: Auditors evaluate a vendor's impact on YOUR financial statements. Which report? :: SOC 1 (financial-reporting controls).
Scenario: A tester is given source code and full internals. Which approach? :: White-box testing.
Scenario: Test how an app handles inputs at the exact min and max allowed. Technique? :: Boundary value analysis.
Scenario: A review reads source code for flaws WITHOUT running the app. Static or dynamic? :: Static (code review / SAST).
Scenario: You re-run the old test suite after a patch to ensure nothing broke. Which testing? :: Regression testing.
Scenario: You want truly independent assurance of a third party's controls. Which assessor? :: A third-party/external auditor (independence).

## Vulnerability Assessment & Penetration Testing

Vulnerability assessment vs penetration test? :: VA = identifies/LISTS vulnerabilities (no exploitation); pentest = actively EXPLOITS them to demonstrate real impact.
Phases of a penetration test? :: Reconnaissance → Enumeration → Vulnerability Analysis → Execution (exploitation) → Document Findings.
Internal vs external test perspective? :: Internal = on the inside (simulates an insider/compromised host); external = from outside the perimeter (simulates an internet attacker).
Blind vs double-blind test? :: Blind = tester has limited info but the TARGET is informed; Double-blind = tester has limited info AND defenders are NOT informed (also tests detection/response).
Pentest knowledge levels? :: Zero knowledge = black-box; Partial = gray-box; Full = white-box.
Credentialed vs uncredentialed scan? :: Credentialed (authenticated, logged in) = deeper, finds missing patches/config; uncredentialed = outsider's view, less depth.
What is banner grabbing / fingerprinting? :: Reading service banners/responses to identify the OS, software, and version running (to find applicable vulnerabilities).
CVE vs CVSS vs SCAP? :: CVE = the catalog/IDs of known vulns (the "which"); CVSS = the severity score (0–10); SCAP = the protocol/standard automating and combining them.
False positive vs false negative — which is worse? :: False negative — a real vuln/attack goes UNDETECTED (dangerous). A false positive only wastes investigation time.

## VA/Pentest Scenarios (Application)

Scenario: Management wants proof a vulnerability could actually be exploited to reach sensitive data — not just a list. VA or pentest? :: Penetration test (exploits to demonstrate real impact).
Scenario: You want to test whether the SOC detects and responds, so defenders aren't told. Approach? :: Double-blind test.
Scenario: A scan with valid login credentials finds far more issues than without. Why? :: Credentialed scans see inside the host (patch level, config) → deeper, more accurate.
Scenario: A scanner reports a critical vuln, but the system isn't actually affected. What is this? :: A false positive.
Scenario: You need a single number to prioritize which vuln to patch first. What do you use? :: The CVSS score (0–10); identify the vuln by its CVE.

## Security Tool Purposes (know the PRIMARY job)

Which tool's PRIMARY purpose is a network VULNERABILITY scan? :: Nessus (also OpenVAS, Qualys, Nexpose) — checks hosts against a database of known weaknesses, produces a risk-rated report.
What is Nmap's PRIMARY purpose? :: Port scanning / network mapping — host discovery, open ports, service & OS fingerprinting. (It CAN run NSE vuln scripts, but that's a bolt-on.)
What is Metasploit's PRIMARY purpose? :: Exploitation framework — exploits vulnerabilities to prove access (pops a shell); does not primarily scan for them.
What is lsof used for? :: "List open files" — a local Linux/Unix host diagnostic (which process holds which file/socket); NOT a network scanner. Common distractor.
Exam tactic: "vulnerability scan" vs "port scan / network map" vs "exploit/gain access" — pick? :: "vulnerability scan" → Nessus/OpenVAS/Qualys; "port scan/map/discovery" → Nmap; "exploit/gain access" → Metasploit.

## Decision-Point Scenarios (Application)

A SaaS customer wants public assurance your security controls are designed AND operating effectively over time. Which report? :: SOC 2 Type II — design and operating effectiveness over a period; restricted-use but the correct scope (SOC 3 is public but only a summary, no detail).
A regulator demands assurance that is truly independent of your internal influence. Internal, external, or third-party? :: Third-party — independence is the deciding factor; internal staff lack it.
You have full source code and want to analyze it for flaws before deployment without executing it. SAST or DAST? :: SAST (static) — reads the source/binary at rest, no running instance needed.
You can only test the live, running application as a black box with no source. SAST or DAST? :: DAST (dynamic) — exercises the running app from the outside, finds runtime/config flaws SAST misses.
Leadership wants the deepest pre-deployment view: combine source analysis AND runtime testing. What gives best coverage? :: Use SAST and DAST together — each catches what the other misses (and IAST hybridizes them).
A tester gets network diagrams and a low-priv account but not source code. Which box type? :: Gray-box — partial knowledge, between full-internals (white) and zero-knowledge (black).
You want the engagement to mimic a real external attacker with no inside information. Which box type? :: Black-box — zero knowledge, attacker's outside view.
The system passed all build-to-spec checks but users say it doesn't solve their problem. Verification or validation failure? :: Validation failure — it was built right (verification) but isn't the right thing (validation = meets user needs).
You need a formal, standards-based evaluation by an independent party that yields an attestation. Test, assessment, or audit? :: Audit — formal, independent, against a standard, produces attestation (assessment is broader/advisory; test checks one control).
A scanner reported "no vulnerabilities" but the host was later breached through an unpatched flaw. What did the scan produce? :: A false negative — a real vuln went undetected (the dangerous error type).
Repeated false positives are flooding analysts; you raise the alert threshold so minor events don't trigger. What is this threshold called? :: A clipping level — only deviations beyond it are logged/alerted (filters noise, but set too high it hides real events).
A SOC 2 engagement must judge controls only as designed at a single point in time (pre-launch). Type I or II? :: Type I — design at a point in time; Type II requires an operating period (6–12 months).
You want to verify the app rejects malformed and unexpected input gracefully, not just valid input. Which testing? :: Negative testing (often via fuzzing) — confirms graceful handling of invalid/unexpected inputs.
Test results show 60% of code paths were never executed during testing. What metric flags this, and what's the concern? :: Code (test) coverage — low coverage means untested paths may hide defects; raise coverage on critical paths.
You must proactively detect performance problems before any real user hits them. RUM or synthetic monitoring? :: Synthetic — scripted transactions run continuously even with no live users; RUM only sees actual traffic after the fact.
Management wants documented attacker-perspective cases showing how the system behaves when deliberately abused. Which testing? :: Misuse/abuse-case testing — models intentional misuse, complementing normal use-case testing.
You want the same depth as an authenticated scan but the audit scope says simulate an outside attacker with no login. Which scan? :: Uncredentialed (unauthenticated) scan — accepts less depth to preserve the external attacker perspective.
The board needs a body that independently oversees the audit function and remediation. Who? :: The audit committee of the board — independent governance over audits and controls.
