# Anki Deck — Domain 5 (Identity & Access Management)

> Format: `Question :: Answer` (Obsidian_to_Anki compatible). Pruned for exam-yield: atomic, gradeable cards only.

## Identity Protocols & Federation

What is SAML? :: Security Assertion Markup Language — an XML-based standard for exchanging authentication ASSERTIONS; the backbone of web SSO/federation (IdP asserts identity to a service provider).
OAuth vs OpenID Connect? :: OAuth = AUTHORIZATION (delegated access — "let app X use my data"); OIDC = AUTHENTICATION layer built on OAuth 2.0 (adds an ID token proving WHO you are). Authz vs authn.
What is SPML? :: Service Provisioning Markup Language — XML standard for automating account provisioning/deprovisioning across systems.
Linked vs synced vs federated identity? :: Linked = identities in separate systems associated; Synced = identity data copied/synchronized (e.g., on-prem → cloud); Federated = a TRUST relationship lets one login work across domains (no credential copying).
Identity Provider (IdP) vs Service Provider / Relying Party? :: IdP authenticates the user and issues assertions/tokens; SP/RP trusts the IdP and consumes the assertion to grant access.
In the cloud, who is ACCOUNTABLE vs RESPONSIBLE for data? :: Cloud Consumer = accountable (data owner/controller); Cloud Provider = responsible for executing per the agreement (processor).

## Access Control Principles

What is separation of duties? :: Splitting a critical task across people so no one can complete it alone — prevents fraud.
Need-to-know vs least privilege? :: Need-to-know limits access to specific DATA (even if cleared for the level); least privilege limits PERMISSIONS/rights overall.

## Access Control Services (IAAA)

The four access control services (IAAA)? :: Identification (claim an identity), Authentication (prove it), Authorization (what you may do), Accountability (logging/audit to trace actions).
Identification vs authentication? :: Identification = CLAIMING an identity (username); Authentication = PROVING it (password/token/biometric).
Authentication vs authorization? :: Authentication = verifying WHO you are; Authorization = determining WHAT you're allowed to do.

## Authentication Factors

The three authentication factor types? :: Type 1 = something you KNOW (password/PIN); Type 2 = something you HAVE (token/smart card); Type 3 = something you ARE (biometric).
What makes authentication "multifactor"? :: Factors from DIFFERENT types (password + token). Two passwords = still single-factor.
Hard token vs soft token? :: Hard = a physical device generating codes; Soft = a software app (e.g., on a phone).
Synchronous vs asynchronous tokens? :: Synchronous = time- or counter-based codes (TOTP/HOTP); Asynchronous = challenge-response (server sends a challenge, token computes the response).
Smart card vs memory card? :: Smart card has a PROCESSOR (can process/protect data); memory card only STORES data (less secure).

## Biometrics

Physiological vs behavioral biometrics? :: Physiological = physical traits (fingerprint, iris, retina, hand geometry, face); Behavioral = how you do things (voice, signature, keystroke, gait).
Iris vs retina scan? :: Iris = pattern of the colored ring (non-invasive, stable); Retina = blood-vessel pattern at the back of the eye (very accurate but invasive, reveals health info).
FRR vs FAR — which is more dangerous? :: FRR (Type 1) = legit user wrongly REJECTED (usability hit). FAR (Type 2) = impostor wrongly ACCEPTED — the DANGEROUS one (security failure).
What is the Crossover Error Rate (CER)? :: The point where FRR = FAR — the key accuracy metric; LOWER CER = more accurate biometric. Also called Equal Error Rate (EER).

## Authorization Models

DAC vs MAC? :: DAC = the data OWNER decides access at their discretion (identity/ACL-based, flexible); MAC = the SYSTEM enforces access via labels + clearances (mandatory, rigid, military/high-security).
What is RBAC? :: Role-Based Access Control — access granted by JOB ROLE; great for high turnover. Non-discretionary.
What is Rule-Based Access Control? :: Access decided by rules/conditions applied to everyone (firewall ACLs, time-of-day restrictions).
What is ABAC? :: Attribute-Based Access Control — access decided by ATTRIBUTES of user/resource/action/environment; fine-grained and dynamic.
What does "non-discretionary" access control include? :: Models where a central authority/system (not the data owner) sets access — MAC and RBAC.
What is just-in-time (JIT) access? :: Granting elevated access only for the moment it's needed, then revoking it — reduces standing privilege.

## Sessions

What is session hijacking, and the defenses? :: An attacker takes over a valid session (steals the token/cookie) to impersonate the user; defended by encryption, secure tokens, and timeouts.

## Access Control Scenarios (Application)

Scenario: A biometric is tuned so few impostors get in, but legitimate users are often rejected. Which error rate rose? :: FRR (Type 1) — false rejection; the sensitivity was set too high, hurting usability.
Scenario: Comparing two fingerprint readers for accuracy. Which metric? :: The LOWER Crossover Error Rate (CER).
Scenario: A military system enforces access by clearance + labels, users CANNOT override. Which model? :: MAC.
Scenario: High-turnover company wants access tied to job function for easy on/offboarding. Which model? :: RBAC.
Scenario: Login uses a password + a code from a phone app. MFA? :: Yes — know (password) + have (soft token) = two factor types.
Scenario: Login uses a password + a security question. MFA? :: No — both are "something you know" (Type 1). Single-factor.
Scenario: An admin can approve payments OR create vendors, but not both. Which principle? :: Separation of duties.
Scenario: A cleared employee is denied a project file they don't work on. Which principle? :: Need-to-know.

## SSO & Federation

What is SSO — main benefit vs main risk? :: One credential set accesses many systems. Benefit = convenience/fewer passwords; Risk = one compromised credential = access to everything ("keys to the kingdom") — mitigate with MFA.
Kerberos — encryption type and what is the KDC? :: SYMMETRIC encryption + timestamps only (no asymmetric). The KDC (Key Distribution Center) = the trusted server containing the Authentication Service (AS) and Ticket Granting Service (TGS).
What is a TGT (Ticket Granting Ticket)? :: Issued by the AS after logon; the client presents it to the TGS to request SERVICE tickets (so it doesn't re-enter the password). A service ticket proves access to a specific service.
Kerberos authentication flow? :: Client → AS (authenticate, get TGT) → TGS (present TGT, get service ticket) → Service (present service ticket, get access).
Kerberos's two main weaknesses? :: (1) The KDC is a single point of failure; (2) it requires time synchronization — timestamped tickets fail or open replay windows if clocks skew.
Kerberos vs SESAME (crypto)? :: Kerberos = symmetric only; SESAME = symmetric + ASYMMETRIC (public-key), uses a PAC (Privilege Attribute Certificate).
What is Federated Identity Management (FIM)? :: Sharing identity across organizations/domains via a TRUST relationship between IdP and SP, so one login works across them.
What are the SAML components? :: Assertions (identity/attribute statements, in XML), Protocol (request/response rules), Bindings (transport, e.g., HTTP), Profiles (use-case combinations).
What is WS-Federation? :: A Microsoft-led federation standard for sharing identity/trust across security domains (alternative to SAML federation).

## SSO/Federation Scenarios (Application)

Scenario: Kerberos logins fail across the domain after a server's clock drifted. Cause? :: Time synchronization — clock skew beyond tolerance breaks Kerberos timestamps. Fix NTP.
Scenario: If one authentication server goes down, all SSO logins fail. Which Kerberos weakness? :: The KDC is a single point of failure — needs redundancy.
Scenario: You need users to log in once and reach partner companies' apps via trust. Concept/standard? :: Federated identity (FIM), typically via SAML assertions between IdP and SP.

## Identity Lifecycle & Provisioning

What is the JML lifecycle? :: Joiner-Mover-Leaver — provision on hire (joiner), adjust on role change (mover), revoke promptly on termination (leaver).
Provisioning vs deprovisioning? :: Provisioning = create the account + grant access (least privilege); deprovisioning = revoke/disable when no longer needed.
What is identity proofing (registration)? :: Verifying a person is who they claim BEFORE issuing credentials (checking ID documents) — the enrollment step.
What is privilege creep, and the counter? :: Accumulating access over time (especially after role changes) beyond what's needed — countered by access reviews/recertification.
What is an access review / recertification? :: Periodically re-verifying each user's access is still appropriate; managers attest or revoke — catches privilege creep and orphaned accounts.
What is an orphaned account? :: An active account with no valid owner (e.g., a departed employee not deprovisioned) — a major attack vector.

## Account Types & Credentials

Privileged vs service vs shared account? :: Privileged = elevated rights (admin/root, protect with PAM/MFA); Service = non-human, used by an app (often over-privileged/rarely rotated); Shared = used by multiple people (breaks ACCOUNTABILITY — avoid).
What is PAM (Privileged Access Management)? :: Controls for privileged accounts — credential vaulting, session monitoring/recording, just-in-time elevation, credential rotation.
Good password policy elements? :: Sufficient length, no reuse (history), lockout after failed attempts; NIST favors length + breached-password checks over forced periodic changes.
What is FIDO2 / a passkey? :: Passwordless, phishing-resistant authentication using public-key crypto (the device holds the private key) — no shared secret to steal.
What is certificate-based authentication? :: Authenticating with a digital certificate (the private key proves identity) instead of a password.

## Access Control Mechanisms

What is an access control matrix? :: A table mapping subjects (rows) to objects (columns) with the allowed actions in each cell.
ACL vs capability table? :: ACL = per-OBJECT (for this file, who can access it — a column of the matrix); capability table = per-SUBJECT (for this user, what it can access — a row).
What is implicit deny? :: The default rule that any access not explicitly allowed is denied (deny by default).
What is access aggregation? :: Gathering enough individual access rights/info to gain more than intended (relates to authorization creep and inference).

## Directory & Federation Services

What is a directory service (LDAP/X.500)? :: A centralized database of identities/resources queried via LDAP — the backbone of authn/authz (e.g., Active Directory).
What is Active Directory? :: Microsoft's directory service (LDAP + Kerberos) for centralized authentication, authorization, and policy (GPO) in a domain.
What is IDaaS? :: Identity as a Service — cloud-delivered identity management (SSO, MFA, provisioning), e.g., Okta, Azure AD/Entra.

## IAM Scenarios (Application)

Scenario: A user changed departments twice and now has access from all three roles. Problem and fix? :: Privilege/authorization creep — fix with regular access reviews/recertification and role-based access tied to the current job.
Scenario: A departed contractor's account is still active and was used in a breach. Failure? :: Orphaned account — deprovisioning (leaver process) failed.
Scenario: Several admins share one "root" login, so changes can't be traced. Principle violated and fix? :: Accountability — eliminate shared accounts; give unique privileged accounts with PAM + logging.
Scenario: Secure domain-admin credentials, record privileged sessions, grant elevation only when needed. Solution? :: PAM with just-in-time elevation.
Scenario: You want phishing-resistant authentication with no shared secret to steal. Technology? :: FIDO2 / passkeys (public-key based).
Scenario: "For this file, who can read or write it?" — ACL or capability table? :: An ACL (object-focused).

## Domain 5 Decision Scenarios (Application)

A bank wants access decided centrally by data classification and clearance, not by data owners. Which model? :: MAC — system-enforced labels/clearances, non-discretionary.
Access must depend on user location, device, and time-of-day, evaluated per request. Which model? :: ABAC — policy over multiple attributes/environment, dynamic.
A file's owner personally chooses who may read it. Which model? :: DAC — owner sets access at their discretion (ACL-based).
A firewall permits a service only between 09:00-17:00 for everyone. Which model? :: Rule-Based Access Control — conditions applied uniformly, not per role.
A hospital wants nurses and doctors to inherit access from their job, not individual grants. Which model? :: RBAC — access tied to role, eases onboarding/turnover.
A third-party app needs to post to your calendar on your behalf without logging you in. Standard? :: OAuth 2.0 — delegated authorization, not authentication.
You need a web app to confirm WHO the user is (identity), built on OAuth. Standard? :: OpenID Connect (OIDC) — authentication layer adding an ID token.
Enterprise browser-based SSO to internal SaaS using XML assertions between IdP and SP. Standard? :: SAML.
A vault door must almost never admit an impostor, even if staff get rejected more often. Tune biometric how? :: Raise the threshold/sensitivity — accept higher FRR to drive FAR down.
A high-traffic lobby turnstile frustrates staff with frequent rejections. Tune biometric how? :: Lower the threshold/sensitivity — accept higher FAR to reduce FRR (usability).
Two biometric devices: A has CER 2%, B has CER 4%. Pick which? :: A — lower CER (EER) means more accurate.
A terminated employee's access should be cut at what point? :: Immediately at termination (leaver) — disable before or at notice, ideally before they're told.
After a role change a user keeps old-role access. Defect and fix? :: Privilege creep — access recertification plus role-based access tied to the current job.
Who attests during access recertification? :: The user's manager/data owner — re-verifies each grant is still appropriate, revoking the rest.
You want admins to hold no standing elevated rights, requesting them only when needed. Approach? :: Just-in-time (JIT) access via PAM — eliminates standing privilege.
A service account is over-privileged and its password never changes. PAM controls to apply? :: Least privilege plus credential vaulting and automatic rotation.
A sensitive transfer should force the user to re-authenticate mid-session. Concept? :: Step-up (adaptive) authentication for the high-risk action.
SSO means one stolen password reaches every app. Primary mitigation? :: Require MFA on the SSO/IdP login.
A client presents its TGT to the TGS to obtain a service ticket without re-entering its password. Normal Kerberos behavior? :: Yes — the TGT lets the TGS issue service tickets; that's SSO by design.
You must verify a new hire is really who they claim before issuing credentials. Step? :: Identity proofing (registration/enrollment).
An access decision needs only stored data, no processing on the card itself. Card type? :: Memory card — stores data only (no processor).
A token computes a response to a server-sent challenge. Token type? :: Asynchronous (challenge-response) token.
In a cloud deployment, who is accountable for the data vs responsible for processing it? :: Consumer accountable (data owner/controller); provider responsible (processor).
A real-time, unified view across several directories without copying data. Service? :: Virtual directory (not a meta-directory, which syncs copies).
