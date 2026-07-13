# 🎭 CISSP Fun Memory Hooks

For the conceptual brain: a *character* + a *picture* + one *hook*. Lock the hook, don't dig past it.
Tell the assistant "make X fun" and it gets added here.

---

## 🔐 The 4 Security Models — The Cast

```
🕵️  BELL-LaPADULA = THE SPY        → keeps SECRETS   (Confidentiality)
🛡️  BIBA          = THE BOUNCER    → keeps data CLEAN (Integrity)
🏦  CLARK-WILSON  = THE BANK TELLER→ no touching the vault directly
🧱  BREWER-NASH   = THE LAWYER     → "Chinese Wall," no conflicts
```

### 🕵️ Bell-LaPadula — *"Loose lips sink ships"* (Confidentiality)
```
   TOP SECRET 🔒
       ▲  ✋ NO READ UP    (can't peek at secrets above you)
   SECRET 🕵️ ← you
       ✋ NO WRITE DOWN  (can't leak secrets to those below)
       ▼
   PUBLIC 📰
```

### 🛡️ Biba — *the exact mirror* (Integrity)
```
   CEO REPORT ✅ (clean)
       ▲  ✋ NO WRITE UP   (intern can't corrupt the good stuff)
   INTERN 🛡️ ← you
       ✋ NO READ DOWN   (don't trust gossip from below)
       ▼
   RANDOM BLOG 🗑️ (garbage)
```
> 🔑 **B-I-ba has an "I" → Integrity.** Bell → Confidentiality.
> Bell blocks read↑/write↓ · Biba blocks write↑/read↓ (mirror).

### 🏦 Clark-Wilson — *"Use the teller, not the vault"* (Integrity)
```
   🙋 YOU ──✗──▶ 💰 VAULT            ❌ never touch data directly
   🙋 YOU ──▶ 🏦 TELLER/APP ──▶ 💰 VAULT   ✅ only through the program
```
Access triple: subject → **program** → object, + separation of duties.

### 🧱 Brewer-Nash — *"Pick a side, the wall goes up"* (Conflict of Interest)
```
   👩‍💼 opens → 🏦 BANK A ✅
                 │ 🧱 WALL slams up
                 ▼
              🏦 BANK B 🚫  (A's competitor — blocked)
```
Dynamic: what you touched *already* decides what's blocked *next*.

**Snap decision:** secrets leaking → 🕵️ Bell · data corrupted → 🛡️ Biba · banks/transactions/SoD → 🏦 Clark-Wilson · competitors → 🧱 Brewer-Nash.

---

## 🔑 Symmetric vs Asymmetric vs Diffie-Hellman

```
👯 SYMMETRIC (AES)   = IDENTICAL TWINS sharing ONE key.
                       Super fast — but how do you hand the key to your
                       twin across town without a thief grabbing it? 😬
                       (= the key-distribution problem)

📫 ASYMMETRIC (RSA)  = a MAILBOX. Anyone can drop mail in the slot
                       (PUBLIC key); only YOU hold the key to open it
                       (PRIVATE key). Secure, but slow. 🐢

🏭 DIFFIE-HELLMAN    = a FACTORY (asymmetric) that builds a CHAIR
                       (a symmetric key). The factory ≠ the chair!
                       DH is asymmetric; the KEY it makes is symmetric.
```

> 🔑 **DH is ASYMMETRIC.** The only "symmetric" thing is the chair (key) it produces.

### 🎉 The HTTPS handshake = a nightclub
```
🚪 ASYMMETRIC = the BOUNCER (slow, careful):
     1. Checks the club's ID (certificate) — "are you the real bank?"
     2. Hands you a secret WRISTBAND 🎟️ (Diffie-Hellman key exchange)
                      │
                      ▼
🔊 SYMMETRIC = the PARTY inside (AES, fast):
     3. Everyone with the wristband dances = all your data, encrypted fast
```
**Why both?** Asymmetric is the slow careful bouncer (verify + hand out the key);
symmetric is the fast party (encrypt everything). = a **hybrid cryptosystem**.

---

## 💾 Backups — Incremental vs Differential (the one you always miss)

```
📦 FULL          = the WHOLE moving truck. Slow to pack, ONE trip to restore.

📸 INCREMENTAL   = daily SNAPSHOTS of only what changed since the LAST backup.
                   Quick to make 🟢 ... but to restore you replay EVERY
                   snapshot in order 🔴 (full + Mon + Tue + Wed + ...). Painful.

📈 DIFFERENTIAL  = grows fatter each day = everything since the last FULL.
                   Slower to make 🟡 ... but restore = full + just the LATEST one 🟢.
```

> 🔑 **In**cremental = **In**dividual little changes, fast backup / slow restore, **clears** the archive bit.
> **Diff**erential = **Diff** from the last FULL, slow backup / fast restore, **keeps** the archive bit.
> Mnemonic: *"Incremental is lazy to make, painful to restore. Differential is the opposite."*

| | Backup speed | Restore | Archive bit |
|---|---|---|---|
| Full 📦 | slowest | fastest (1 set) | cleared |
| Incremental 📸 | fastest | slowest (full + ALL) | cleared |
| Differential 📈 | medium | fast (full + last) | NOT cleared |

---

## 🚦 Access Control Models — who decides?

```
🙋 DAC  = "MY file, MY rules"  → the OWNER decides who gets in (flexible; your home PC)
🪖 MAC  = THE ARMY            → the SYSTEM enforces clearance LABELS, you get no say (rigid)
👔 RBAC = THE JOB BADGE       → access by your ROLE (new hire inherits the role's rights)
🏷️ ABAC = THE SMART BOUNCER   → checks ATTRIBUTES: "managers, from the office, 9–5"
```
> 🔑 DAC = **D**iscretion (owner) · MAC = **M**andatory (military labels) · RBAC = **R**ole · ABAC = **A**ttributes.
> "Owner decides" → DAC · "labels/clearance, can't override" → MAC · "by job title" → RBAC · "if/then conditions" → ABAC.

---

## 👁️ Biometric Errors — FAR vs FRR

```
👤 FRR (Type 1) = FALSE REJECT → locks OUT the real you 😤   (annoying, but SAFE)
🦹 FAR (Type 2) = FALSE ACCEPT → lets the IMPOSTOR IN 😱     (DANGEROUS!)

      error %                CER = where the lines cross
        │  FRR ＼      ／ FAR        → LOWER CER = BETTER scanner
        │       ＼  ／
        │        ✕  ← CER
        │       ／  ＼
        └──────────────── sensitivity →
```
> 🔑 **Type 2 = Too bad** (the impostor got in — the dangerous one). **Lower CER = more accurate.**

---

## 🪜 THE BEST-ANSWER LADDER  (your #1 point-leak — read before every test)

When 2+ answers look correct, the wrong ones are usually **TRUE**. Don't pick the most *technically correct* — **climb the ladder and pick the HIGHEST rung that applies:**

```
   🪜  1. 🧍 LIFE / SAFETY           ← always wins, full stop
       2. 🏢 PROTECT THE ORG / risk
       3. 📜 GOVERNANCE / approval / policy
       4. 🌱 ROOT CAUSE (fix the WHY, not the symptom)
       5. 🛡️ PREVENT  >  detect  >  correct
       6. ⌨️ technical / tactical / "do it now"  ← YOUR instinct grabs here — RESIST
```
> 🔑 The exam pays the **manager** (top of the ladder), not the **technician** (bottom).
> Your technician brain dives for rung 6. Force yourself UP the ladder first.

### 🧭 What "think like a manager" REALLY means (re-label it in your head)

It is **not** a non-technical business boss, and **not** a line manager. It is the **risk-aware security leader / advisor — a CISO mindset, the risk owner.** Technically **literate** (understands the concepts across all domains) but deliberately reasoning *one level up* from the technical fix:

- **Risk & business impact** — "what does this mean for the *organization*?", not "what's the most elegant fix?"
- **Governance & process** — policy, approval, due care/diligence, *before* jumping to execution.
- **Root cause** over symptom.
- **People, legal, compliance** — not only the machine.
- **Cost-effectiveness** — never spend more protecting an asset than it is worth.

> 🔑 Re-label "manager" as **"the person accountable for the organization's RISK."** You are not lowering your intelligence to a manager's level — you are *raising your vantage point* from deep-and-narrow (technician) to broad-and-risk-aware (risk owner). That shift is the register the whole exam speaks.
> Note: CISSP expects technical *literacy* (breadth), NOT technical *depth* (hands-on mastery). You are over-qualified on the axis it ignores and under-practised on the axis it tests.

---

## 🍕 Cloud Service Models — the Pizza

```
🏠 On-prem  = make pizza from scratch (you own EVERYTHING)
📦 IaaS     = take-and-bake (provider: kitchen+oven; YOU: cook it = OS, apps, data)
🚚 PaaS     = delivery (provider: up to the runtime; YOU: apps + data)
🍽️ SaaS     = dine out (provider: everything; YOU: just your data/account)
```
> 🔑 Your burden SHRINKS from IaaS → SaaS. "Who patches the OS?" IaaS = you; PaaS/SaaS = provider.

---

## 🏢 VLAN vs Subnet (you thought they were the same — almost everyone does)

They're glued together in practice, but they live on **different layers**:

```
   🏢 SUBNET (Layer 3 = IP address range — "which neighborhood")
        10.0.10.0/24        |        10.0.20.0/24

   🚪 VLAN (Layer 2 = the switch's virtual ROOMS — "which room")
   ┌── VLAN 10 room ──┐
   │                  ├── 🛣️ ROUTER  ← the ONLY door between rooms
   └── VLAN 20 room ──┘
```

- **VLAN** = the **room the SWITCH puts you in** (L2 broadcast domain). You can only shout to people in *your* room.
- **Subnet** = your **IP neighborhood / ZIP code** (L3 address range).
> 🔑 They usually map 1-to-1, but to talk *between* them you **always need a router**.
> "Hardware segmentation needing a routing function" = **VLAN** (not subnet).
> Why they feel identical: admins configure them together (VLAN 10 ↔ subnet 10.0.10.0/24). Different *mechanism*, same *boundary*.

---

## 🥚 RAID — how many drive deaths can it survive?

```
🥚  RAID 0  = STRIPING, all eggs one basket → 1 drive dies = ALL DATA GONE. (speed only, ZERO protection)
👯  RAID 1  = MIRROR → exact twin copy; survives 1 death (half your space is the twin)
🅿️  RAID 5  = stripe + 1 PARITY → needs 3+ drives, survives 1 death (parity rebuilds it)
🅿️🅿️ RAID 6 = stripe + 2 PARITY → survives 2 deaths at once
👯🅿️ RAID 10 = mirror + stripe → speed AND redundancy (needs 4)
```
> 🔑 RAID **5 → survives 1**, RAID **6 → survives 2**, RAID **0 → survives 0** (zero = zero protection).
> RAID is NOT a backup — it won't save you from deletion/ransomware/disaster.

---

## 🏠 DR Sites + ⏱️ RTO / RPO / MTD

```
🥶 COLD site = empty room (power + HVAC only, no gear/data) → cheap, days–weeks
🌤️ WARM site = room + hardware, but STALE data → hours–days
🔥 HOT site  = fully live + current data → minutes, 💸💸💸
```
```
            💥 DISASTER strikes
   last backup ←── RPO ──┤            RPO = how much DATA you can lose (look BACKWARD)
                         ├── RTO ──→  RTO = how fast you RESTORE (look FORWARD)
                         ├──────── MTD ────────→  max downtime before the business dies
```
**Acronym key:** RPO = Recovery Point Objective · RTO = Recovery Time Objective · MTD = Maximum Tolerable Downtime · WRT = Work Recovery Time.
> 🔑 **RPO looks BACK** (data loss → drives backup frequency). **RTO looks FORWARD** (recovery time).
> **RTO + WRT must be ≤ MTD.** Tighter RPO = back up more often.

---

## 📡 OSI 7 Layers — "Please Do Not Throw Sausage Pizza Away"

```
7 Application  📱  the app you see (HTTP, DNS, SSH)        Please
6 Presentation 🎁  encrypt / format / compress (TLS, JPEG)  Do
5 Session      🤝  start & stop the conversation            Not
4 Transport    📦  TCP/UDP, PORTS, segments                 Throw
3 Network      🗺️  IP, ROUTERS, packets                     Sausage
2 Data Link    🔗  MAC, SWITCHES, frames                    Pizza
1 Physical     🔌  bits & cables                            Away
```
> 🔑 Firewalls deepen as you go up: packet filter (L3) < circuit proxy (L5) < app proxy (L7).
> Switch = L2 (MAC) · Router = L3 (IP) · Gateway = L7.

---

## 🎟️ Kerberos — the festival with a ticket booth

```
🎪 KDC (Key Distribution Center) = the ticket booth — holds the AS + the TGS

  1. 🪪 Show ID at the gate = AS (Authentication Service)
        → get a WRISTBAND 🎟️ = TGT (Ticket-Granting Ticket)
  2. 🎢 Show wristband to the ride attendant = TGS (Ticket-Granting Service)
        → get a RIDE TICKET 🎫 = Service Ticket
  3. 🎠 Give the ride ticket to the ride operator (the service/server) → you're IN
```
**Acronym key:** KDC = Key Distribution Center · AS = Authentication Service · TGT = Ticket-Granting Ticket · TGS = Ticket-Granting Service.
> ⏰ Everyone's watch must MATCH (time sync via NTP = Network Time Protocol) or your ticket "expires" → locked out.
> 💥 The booth (KDC) is the SINGLE POINT OF FAILURE.
> Crypto: **symmetric only** (SESAME is the cousin that adds asymmetric).

---

## 🚪 Fail-SAFE vs Fail-SECURE (power dies — what do the doors do?)

```
   ⚡ failure / fire alarm →
   FAIL-SAFE   = doors UNLOCK 🧍  → save PEOPLE  (life safety first)
   FAIL-SECURE = doors LOCK   🔒  → save ASSETS  (protect data/property)
```
> 🔑 **SAFE = people Safe** (unlock & escape). **SECURE = assets Secured** (lock down).
> Life at stake → fail-safe. Data at stake → fail-secure.

---

## 🧮 Risk Math — the formula trap

```
   SLE = AV × EF        💥 one hit  = asset value × % lost
   ALE = SLE × ARO      📅 per year = one-hit × times-per-year
```
> ⚠️ **ARO trap:** a "100-year event" = **0.01**, NOT 0.1. Count the zeros!
> 💡 **If a control costs MORE than the ALE → ACCEPT the risk** (don't overspend to protect).
> "Reject/ignore the risk" = always WRONG (that's negligence).

---

## 🛡️ IPsec — the armored convoy for IP packets

```
   AH (Authentication Header)          = a TAMPER-PROOF SEAL only → integrity + auth, NO encryption 👁️
   ESP (Encapsulating Security Payload)= a LOCKED ARMORED BOX     → encryption + integrity 🔒
   IKE / ISAKMP = the crew that SETS UP the secret keys (Security Associations / SAs)
                  → this is what lets one host run MANY VPNs at once
```
**Acronym key:** AH = Authentication Header · ESP = Encapsulating Security Payload · IKE = Internet Key Exchange · ISAKMP = Internet Security Association and Key Management Protocol · SA = Security Association · VPN = Virtual Private Network.
> 🔑 **AH = seal (no secrecy). ESP = locked box (secrecy).** ISAKMP/IKE = key setup → enables multiple VPNs.

---

## ✂️ Clipping Level — trim the noise, keep the peaks

A **fixed threshold** below which events are ignored; only events that **exceed** it get recorded or alerted. **Nonstatistical** (a fixed rule, e.g. "alert after the 5th failure") — *not* a statistical sample.

```
events
  │            ╱╲         ╱╲   ← PEAKS rise above the line → recorded / alerted
──┼───────────────────────────  ← the CLIPPING LEVEL (threshold)
  │  ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿  ← routine baseline noise → "clipped off", ignored
  └─────────────────────────── time
```

**Where it's used** (all for the same reason — separate routine noise from notable events):
- **Audit logging** — only record events past the threshold → less log volume.
- **Failed-login / account lockout** — ignore 1–2 fat-fingers, lock/alert after N (the "N" *is* the clipping level).
- **IDS / SIEM alerting** — only alert when a count crosses the threshold → fights alert fatigue.
- **Violation / anomaly tracking** — flag a user only once violations exceed a baseline.

**Why "clipping"?** From signal processing — "clipping" = cutting a signal off at a set level. Here you **clip away the baseline noise below the line**, keeping only what pokes above it. The "level" = where you set the scissors.
> 🔑 Clipping level = the threshold that **trims off routine activity**, so only events **above** it are recorded/alerted. Nonstatistical (fixed rule) vs sampling (statistical).



