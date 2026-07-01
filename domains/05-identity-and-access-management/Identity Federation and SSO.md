# Identity Federation and SSO

## Overview

SSO lets a user authenticate once and reach many systems; federation extends that trust *across organizational boundaries* so one login works at partner services too. The trade-off is concentration of risk — convenience and fewer passwords, but the SSO account becomes a single high-value target. The exam leans hard on telling the standards apart: SAML (XML, enterprise web SSO), OAuth (authorization/delegation), and OIDC (authentication built on OAuth).

## Key Concepts

### Single Sign-On (SSO)
- User authenticates once, gains access to multiple systems
- Reduces password fatigue and helpdesk calls
- Risk: single point of compromise (if SSO account is breached, all access is lost)

### Federation Standards
| Standard | Purpose | Notes |
|----------|---------|-------|
| **SAML** (Security Assertion Markup Language) | Web SSO between organizations | XML-based; enterprise standard |
| **OAuth 2.0** | Authorization delegation | Grants access to resources without sharing credentials |
| **OpenID Connect (OIDC)** | Authentication layer on OAuth 2.0 | Identity verification; returns ID token |
| **Kerberos** | LAN SSO | Ticket-based; single realm or cross-realm trusts |
| **WS-Federation** | Web services federation | Microsoft ecosystem (ADFS) |

### SAML Components
- **Identity Provider (IdP)** - authenticates the user (e.g., corporate AD)
- **Service Provider (SP)** - the application/service being accessed
- **Assertion** - XML document with authentication/authorization data
- Flow: User -> SP -> IdP (authenticate) -> SP (with assertion) -> Access

**The four SAML building blocks (exam list):**
- **Assertions** - the identity/attribute/authorization statements (XML).
- **Protocol** - request/response rules for asking for and returning assertions.
- **Bindings** - how SAML messages map onto a transport (e.g., HTTP POST, HTTP Redirect).
- **Profiles** - combinations of assertions/protocol/bindings for a specific use case (e.g., Web Browser SSO).

### OAuth 2.0 vs. OpenID Connect
- **OAuth 2.0** = authorization only ("this app can access your photos")
- **OIDC** = authentication + authorization ("verify who you are AND what you can access")
- OAuth issues **access tokens**; OIDC adds **ID tokens**
- **Standards/maintainers (exam trap):** **OAuth 2.0** is described in **RFC 6749** and is maintained by the **IETF**. **OIDC** is *built on* OAuth 2.0 (RFC 6749) but is maintained by the **OpenID Foundation** (not IETF). So a system that lets users authenticate via a third party *without the site seeing/storing credentials*, "uses technologies in RFC 6749 but is **not** maintained by IETF" → **OIDC** (the not-IETF clue rules out plain OAuth).

### OIDC Components and Flows

**Components:**
- **Relying Party (RP)** = the web application that authenticates the user via the IdP (trap — RP is the *web app* doing the authentication, NOT the authorization server)
- **Identity Provider (IdP)** = the OIDC server that holds identity and issues tokens
- **Authorization Server** = part of the IdP that issues tokens
- **Resource Owner** = the end user who owns the protected resources
- **End User** = the human authenticating

**OIDC Flow Types:**

| Flow | How it works | When to use |
|---|---|---|
| **Authorization Code Flow** | RP receives a code from IdP, then exchanges it directly with IdP for the ID token (server-to-server). **Most secure.** | Confidential clients (server-side apps) — trigger phrase: "RP provided an auth code and must use it to directly request the ID token" |
| **Implicit Flow** | Token returned directly in URL fragment. No code exchange. **Deprecated for security reasons.** | Legacy SPAs (use PKCE instead now) |
| **Hybrid Flow** | Combines code + token in one flow — RP gets some tokens directly + a code to exchange | Mixed scenarios |
| **Client Credentials Flow** | Service-to-service, no user involved | Machine-to-machine auth |

**Trigger phrase mapping:**
- "RP gets a code, exchanges it for ID token" → **Authorization Code Flow**
- "Token returned directly, deprecated" → **Implicit Flow**

### Virtual Directory vs Meta-Directory

These are easily confused with regular directory services. Common trap:

| Type | What it does |
|---|---|
| **Directory Service** | The actual identity store (AD, LDAP, NDS) |
| **Meta-Directory** | Aggregates multiple directories into one logical view (data-pull approach, periodic sync) |
| **Virtual Directory** | Same role as meta-directory but **real-time view** (queries on demand, no data sync) |

**Trigger phrase:** "Virtual directory plays the same role in IAM as ___" → **Meta-directory** (NOT directory service)

### Synchronous vs Asynchronous Tokens

| Token Type | How it works | Examples |
|---|---|---|
| **Synchronous time-based** | Server and token share time; token displays current OTP | TOTP, Google Authenticator |
| **Synchronous counter-based** | Server and token share a counter; press to advance | HOTP, RSA SecurID counter mode |
| **Asynchronous nonce-based / challenge-response** | Server sends challenge; token computes response using nonce | Smart card challenge-response |

**Trigger phrase:** "Challenge/response scheme to authenticate" → **Asynchronous nonce-based** (NOT synchronous — challenge-response is async by definition)

### Virtual Password

A **virtual password** = passphrase converted into the **length and format required by a specific system or application**.

- NOT a hash (that's a different concept)
- NOT an encryption key
- It's the system-specific representation of the user's passphrase

**Trigger phrase:** "Passphrase converted to a length/format" or "derived from a passphrase" → **Virtual Password**

### Kerberos vs. SESAME
- **Kerberos** = **symmetric** encryption only (+ timestamps); KDC is a single point of failure.
- **SESAME** = a Kerberos successor that adds **asymmetric (public-key)** crypto on top of symmetric, and uses a **PAC (Privilege Attribute Certificate)** to carry the user's identity and access rights. Trap pairing: "symmetric + asymmetric / uses a PAC" = **SESAME**, not Kerberos.

### Linked vs. Synced vs. Federated Identity
- **Linked** - the same person's separate accounts in different systems are *associated* (no data moved).
- **Synced** - identity data is *copied/synchronized* between systems (e.g., on-prem AD → cloud).
- **Federated** - a *trust relationship* lets one login work across domains, with **no credential copying** (the SP trusts the IdP's assertion).

### Federation Trust Models
- **Cross-certification** - each organization certifies the other (peer-to-peer)
- **Third-party trust** - trusted third party (bridge CA) manages trust
- **Federation** - trust agreements between IdPs and SPs

## Exam Tips

- **SAML** = enterprise SSO, XML-based, most comprehensive
- **OAuth** = authorization (not authentication)
- **OIDC** = authentication (built on top of OAuth)
- SSO increases convenience but also increases risk (single point of failure)
- Kerberos requires **time synchronization** between all systems

## Diagrams

### Kerberos Authentication — Sequence

```mermaid
sequenceDiagram
    participant C as Client
    participant AS as AS (in KDC)
    participant TGS as TGS (in KDC)
    participant S as Service
    C->>AS: 1. Authenticate (logon)
    AS-->>C: 2. TGT (Ticket Granting Ticket)
    C->>TGS: 3. Present TGT, request service
    TGS-->>C: 4. Service Ticket
    C->>S: 5. Present Service Ticket
    S-->>C: 6. Access granted
    Note over AS,TGS: KDC = single point of failure · symmetric only · needs time sync (NTP)
```

**Takeaway:** AS issues TGT → TGS issues service ticket → service grants access. Symmetric only; KDC is the SPOF.

### OAuth 2.0 Authorization Code Flow — Sequence

```mermaid
sequenceDiagram
    participant U as User
    participant App as Client App
    participant Auth as Authorization Server
    participant API as Resource Server
    U->>App: Use app (wants my data on service Y)
    App->>Auth: Redirect — request authorization
    U->>Auth: Consent / approve
    Auth-->>App: Authorization CODE
    App->>Auth: Exchange code (+ secret) for ACCESS TOKEN
    Auth-->>App: Access token
    App->>API: Call API with access token
    API-->>App: Protected resource
    Note over U,API: OAuth = AUTHORIZATION (delegated access), not authentication
```

**Takeaway:** OAuth = delegated authorization (code → token → access). OIDC adds authentication on top.

### SAML Web SSO — Sequence

```mermaid
sequenceDiagram
    participant U as User (browser)
    participant SP as Service Provider (app)
    participant IdP as Identity Provider
    U->>SP: Request a resource
    SP-->>U: Redirect to IdP (SAML auth request)
    U->>IdP: Authenticate (login)
    IdP-->>U: SAML assertion (signed XML)
    U->>SP: Present assertion
    SP-->>U: Access granted (trusts the IdP)
```

**Takeaway:** SP trusts the IdP's signed XML assertion — one login works across federated services.

### Active Directory + Kerberos — End-to-End Flow

The whole story: build the company → onboard a user → log in → access a resource.
Watch where **authentication** (Kerberos) ends and **authorization** (the resource) begins.

---

#### 1️⃣ Setup & Onboarding — where authorization is *defined*

```mermaid
flowchart TD
    A[Install Active Directory on a server] --> B[That server becomes a Domain Controller]
    B --> C[Create the domain: company.com]
    C --> D[Join every employee PC to the domain<br/>PCs now ask the DC for all logins]
    C --> E[Create GROUPS<br/>Finance, Engineering, HR, VPN-Users]
    E --> F[Set permissions ACL on resources<br/>Finance share = Finance group only]

    G[Onboard Alice] --> H[Create user account in AD on the DC]
    H --> I[Set her password]
    I --> J[Add her to groups: Engineering, VPN-Users<br/>THIS step is her authorization]
```

> Her access is decided here, by **which groups she's in** — before she ever logs in.

---

#### 2️⃣ Login + Resource Access — the Kerberos ticket flow

```mermaid
sequenceDiagram
    participant U as Alice's PC
    participant KDC as Domain Controller / KDC
    participant FS as Finance File Server

    Note over U,KDC: LOGIN = Authentication
    U->>KDC: 1. I'm michaela + proof of password [to AS]
    KDC-->>U: 2. TGT wristband — sealed by KDC,<br/>carries her groups inside

    Note over U,KDC: ACCESS A RESOURCE
    U->>KDC: 3. Here's my TGT — give me a ticket<br/>for the Finance server [to TGS]
    KDC-->>U: 4. Service Ticket — sealed for the file server,<br/>also carries her groups

    U->>FS: 5. Present the Service Ticket
    Note over FS: 6. Seal valid → AUTHENTICATED<br/>reads groups: Engineering, VPN-Users
    Note over FS: 7. AUTHORIZATION happens HERE:<br/>check groups vs the folder's ACL
    FS-->>U: 8. Finance needs 'Finance' group → DENY
```

> Kerberos **proved who she is** and **carried her groups**. It did NOT decide access.

---

#### 3️⃣ The Authorization Decision — done BY the resource

```mermaid
flowchart TD
    A[User presents service ticket to the resource] --> B{Seal valid?<br/>signed by the KDC}
    B -- No --> X[Reject — authentication fails]
    B -- Yes --> C[AUTHENTICATED<br/>read user's groups from the ticket]
    C --> D{Are the user's groups<br/>in the resource's ACL?}
    D -- Yes --> E[✅ ALLOW access]
    D -- No --> F[⛔ DENY access]
```

---

#### Who does what

| Step | Who | Job |
|---|---|---|
| Prove who you are | **Kerberos / KDC** | **Authentication** |
| Carry your group memberships | **Kerberos ticket** | delivers identity + groups |
| Decide allow/deny | **The resource + its ACL** | **Authorization** |

- **Authentication** = "who are you?" → Kerberos (AS issues the TGT, TGS issues service tickets).
- **Authorization** = "are your groups on my list?" → the **resource** checks the groups (delivered in the ticket) against **its own ACL**.

> **Why Golden/Silver tickets are deadly:** they forge the **groups inside the ticket**. The resource *trusts* those groups and never re-checks them → forge `Domain Admins` and every resource authorizes you. You were attacking exactly this handoff.

**CISSP-depth:** Kerberos = authentication + SSO via AS→TGS tickets; authorization is enforced **at the resource** against an **ACL** using the user's **group memberships**. The crypto/PAC internals are below exam level — the *handoff* is the testable idea.

## Related Topics

- [Authentication Methods](Authentication%20Methods.md)
- [Authorization and Accountability](Authorization%20and%20Accountability.md) - Kerberos, RADIUS
- [Identity Management](Identity%20Management.md) - federation extends identity across boundaries
- [Domain 4 - Communication and Network Security](../04-communication-and-network-security/00%20Domain%204%20-%20Communication%20and%20Network%20Security.md) - protocols used
