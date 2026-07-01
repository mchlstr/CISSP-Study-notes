# Business Continuity Planning

## Overview

BCP ensures that critical business functions continue during and after a disaster. It is a **management-level** responsibility, not just an IT function.

> **Why this matters:** In studies of orgs that suffered major data loss, **43% never reopened** and another **29% closed within 2 years**. That's >70% dead. Given enough time, every organization has a disaster. BCP is not optional.

## BCP Sub-Plans

The BCP is an umbrella. Under it:
- **COOP** (Continuity of Operations) — keeping core day-to-day functions running (payroll, HR, customer support)
- **Crisis Communication Plan** — defines who can speak to press/internal/external. Everyone else is silent.
- **Critical Infrastructure Protection Plan** — protecting the highest-value assets
- **Cyber Incident Response Plan** — online assets (often rolled into DRP)
- **ISCP** (Information System Contingency Plan)
- **Occupant Emergency Plan** — life safety / evacuation
- **DRP** (Disaster Recovery Plan) — IT-specific tactical recovery

## Key Concepts

### BCP vs. DRP
- **BCP** (Business Continuity Plan) - keeping the business running (proactive, strategic)
- **DRP** (Disaster Recovery Plan) - restoring IT systems after failure (reactive, tactical)
- BCP is the umbrella; DRP falls under it

### BCP Process (ISC2 approach)
1. **Project scope and planning** - get management support, define scope
2. **Business Impact Analysis (BIA)** - identify critical functions and impact of disruption
3. **Continuity planning** - develop recovery strategies
4. **Approval and implementation** - get management sign-off, implement

#### Project Scope & Planning — the 4 activities
This phase contains exactly **four** activities:
1. **Structured analysis of the organization** — identify critical business units and processes
2. **Creation of the BCP team** — with management approval
3. **Assessment of available resources** — people, budget, time
4. **Analysis of the legal & regulatory landscape** — what compliance obligations apply

> **Exam trap:** Plan **documentation is NOT part of Scope & Planning.** Documentation happens later, in the **Approval & Implementation** phase (alongside final approval). If a question asks which activity is *not* in Scope & Planning, "documenting the plan" is the answer.

### Business Impact Analysis (BIA)
The BIA identifies:
- **Critical business functions** and their dependencies
- **Maximum Tolerable Downtime (MTD)** — also called MAD, MTO, MAO, MTPD
- **Recovery Time Objective (RTO)** - how fast to restore hardware (must be ≤ MTD)
- **Work Recovery Time (WRT)** - time to restore software/data/configs after hardware is back
- **Recovery Point Objective (RPO)** - how much data loss is acceptable
- **Mean Time Between Failures (MTBF)** - reliability measure (average time between failures)
- **Mean Time To Repair (MTTR)** - average repair time
- **Minimum Operating Requirements (MOR)** - lowest spec a system can run on in a degraded state

### The Golden Equation
```
MTD ≥ RTO + WRT
```
If RTO + WRT > MTD, your plan doesn't work. You need faster hardware provisioning (pre-built standby systems, hot/warm sites) or faster software restore.

### Key Metrics Relationship
```
RPO <-------- disaster --------> RTO ----> WRT ----> back online
(data loss)                    (hardware)  (software)
            must all fit within MTD
```

### Worked Example
- MTD = 3 hours (business decision)
- RTO = 2 hours (procure + rack server)
- WRT = 2 hours (restore OS, apps, data, configs)
- 2 + 2 = 4 hours > 3 hour MTD → **plan fails**
- Fix: keep a pre-built standby → RTO drops to 30 min. 0.5 + 2 = 2.5 < 3 ✓

### Recovery Strategies
| Site Type | Description | Cost | Recovery Time |
|-----------|-------------|------|---------------|
| **Hot Site** | Fully equipped, ready to go | Highest | Minutes to hours |
| **Warm Site** | Partially equipped, needs some setup | Medium | Hours to days |
| **Cold Site** | Empty facility, power/network only | Lowest | Days to weeks |
| **Cloud/Mobile** | Cloud-based or portable recovery | Varies | Varies |

### Testing Types (least to most disruptive)
1. **Checklist/Desk Check** - review the plan on paper
2. **Structured Walk-through/Tabletop** - team discusses scenarios
3. **Simulation** - practice a scenario (no actual failover)
4. **Parallel** - activate recovery site alongside primary (primary stays running)
5. **Full Interruption** - shut down primary, switch to recovery (most disruptive, most realistic)

## NIST SP 800-34 BCP Process

1. **Project initiation** — get senior management buy-in, identify stakeholders
2. **Scope the project** — in-scope and out-of-scope must both be explicit
3. **Business Impact Analysis** — identify and prioritize critical systems/functions
4. **Preventative controls** — what prevents the disaster entirely
5. **Recovery strategies** — hot/warm/cold sites, cloud, etc.
6. **Design & develop plans** — the actual procedures, runbooks, playbooks
7. **Implement, train, test** — awareness training + tabletop + simulation + parallel + full interruption
8. **Maintain** — review annually OR when systems/infrastructure change OR when senior leadership changes (75%+ rule: if most of leadership changes, redo the plan so they sign off and know it)

## Roles: Who Approves vs. Who Builds

**Senior management OWNS and APPROVES the plan — they do not build it.** Their role is to sponsor, fund, approve, and provide a liaison to the working team. They are not the hands-on builders.

### Who approves the BCP
Approval should come from the **highest-ranking executive possible**. When asked for the *ideal* approver and options include CIO / CEO / CISO / COO → answer **CEO** (most senior, broadest authority across the whole enterprise).
- **CIO / CISO** are too narrow (IT / security only) — a BCP is enterprise-wide.
- **COO** is the runner-up (broad operational authority) if CEO isn't an option.

### Who builds the BCP (the planning team)
The working planning team is made of the people who actually **develop** the plan:
- **Core business function leaders** (the units that must keep running)
- **IT staff**
- **Support departments** (facilities, HR, legal, comms)
- Plus a **senior management liaison** (sponsor link, not a builder)

> **Watch the verb.** "**Approve** the plan / ideal person to approve" → **CEO / senior management.** "**Develop** the plan / part of the planning team" → **business + IT + support.** The **CEO is NOT on the working planning team** — the CEO approves, doesn't build.

## BCP Training Tiers

**Initial training = organization-wide awareness for EVERYONE.** So all staff know the plan exists and the basic actions to take.

- **"Initial"** here means the **entry-level *tier* of training** (broad-and-shallow) — **not** "the first group of people." Everyone gets it.
- **Role-specific detailed training comes AFTER**, and only for those with specific continuity roles (narrow-and-deep).

> **Analogy:** Everyone learns where the fire exit is (initial, org-wide). Only fire wardens get warden training (role-specific, later).

## Emergency Response Guidelines

A **concise document** (part of the BCP/DRP) listing the **immediate steps at disaster onset**. Must be **quickly accessible** so no one is hunting for information mid-crisis. It contains:
1. **Immediate response procedures** — evacuation, safety, containment
2. **Who to notify** — the contact / notification list: internal leads **and** external emergency services / vendors
3. **Escalation** — handoff to the response teams

> Contacts are baked in deliberately so nobody has to hunt for phone numbers during a crisis.

## Crisis Communication Warning

Only authorized spokespeople talk to press. **BP oil spill counter-example:** the CEO publicly complained he'd had to cancel his vacation while 7 people were dead and tens of thousands lost jobs. PR nightmare. Media-train your spokespeople; lock everyone else out.

## Exam Tips

- BCP is a **management responsibility**, not just IT
- BIA is the first analytical step - do this before choosing recovery strategies
- MTD ≥ RTO + WRT
- RPO = data loss tolerance; RTO = downtime tolerance; WRT = software/data restore time
- Hot site = fastest recovery, highest cost
- Full interruption test = most thorough but riskiest
- BCP is strategic / enterprise-wide; DRP is tactical / IT-focused
- Senior management must sign off — and must re-sign if leadership turns over
- Scope & Planning = 4 activities (org analysis, team creation, resource assessment, legal/regulatory). **Documentation is NOT here** — it's in Approval & Implementation
- Ideal BCP approver = **CEO** (most senior); CIO/CISO too narrow, COO is runner-up
- "**Approve**" → CEO/senior mgmt; "**develop / part of team**" → business + IT + support (CEO not on the team)
- **Initial** BCP training = org-wide awareness for **everyone**; role-specific detail comes after

## Diagrams

### BCP/DR Test Escalation — least → most disruptive

```mermaid
flowchart LR
    A["Read-through / Checklist"] --> B["Walkthrough / Tabletop"] --> C["Simulation"] --> D["Parallel (no downtime)"] --> E["Full-Interruption (production DOWN)"]
```

**Takeaway:** Read-through → Walkthrough → Simulation → Parallel (no downtime) → Full-interruption (production down, riskiest).

## Related Topics

- [Risk Management](Risk%20Management.md) - BCP addresses the risk of business disruption
- [Domain 7 - Security Operations](../07-security-operations/00%20Domain%207%20-%20Security%20Operations.md) - DRP and operational recovery
- [Security Governance](Security%20Governance.md) - management oversight of BCP
