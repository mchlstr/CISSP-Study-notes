# Anki Deck — Domain 3 (Security Architecture & Engineering)

> Format: `Question :: Answer` (Obsidian_to_Anki compatible). Pruned for exam-yield: atomic, gradeable cards only.

## Environmental & Maturity

Which CIA element does HVAC (temperature/humidity control) protect? :: Availability — keeps equipment running.
List the 5 CMMI maturity levels in order. :: 1 Initial → 2 Repeatable/Managed → 3 Defined → 4 Quantitatively Managed → 5 Optimizing.
CMM/CMMI vs RMM (trap)? :: CMM/CMMI rate PROCESS maturity (Domain 3); RMM rates RISK-management maturity (Domain 1).

## Cryptography — Core

What is a MAC (Message Authentication Code), and does it give confidentiality? :: A value proving integrity + authenticity (from the holder of a shared secret key). NO confidentiality.
Three meanings of 'MAC' in CISSP? :: Message Authentication Code (crypto); Mandatory Access Control (labels/clearances); Media Access Control (Layer 2 address).
In TLS, what provides confidentiality vs integrity vs key-exchange? :: Confidentiality = AES (symmetric); integrity/authenticity = MAC/HMAC; authentication + key exchange = asymmetric (RSA/ECDHE) + certificates.
Why does TLS use hybrid crypto? :: Asymmetric is secure but slow → used to authenticate and exchange a session key; symmetric (AES) is fast → encrypts the bulk data.
Is TLS a cipher or a protocol? :: A protocol — it USES ciphers like AES. Successor to SSL, the S in HTTPS.
What is BitLocker / FileVault? :: Full-disk encryption (AES) — BitLocker = Windows (often TPM), FileVault = macOS. Protect data at rest.
Which data state is hardest to protect, and why? :: Data in use — the key must be PLAINTEXT in RAM to be used (can't wrap it while in use), exposed to memory dumps / cold-boot.

## Asset Lifecycle & Obsolescence

EOL vs EOS — which is the security-critical date? :: EOS (End of Support) — vendor stops issuing patches, so vulnerabilities go unfixed. EOL = stops selling. Retire before EOS.
Manufacturer product lifecycle order (first→last)? :: General Availability → End of Sale → End of Life (EOL) → End of Support (EOS).
Why are legacy/unsupported systems a security risk? :: Past EOS they get no patches → a growing unpatchable attack surface.

## Tangible vs Intangible Asset Inventory

How do you inventory tangible vs intangible assets? :: Tangible → asset tags + network discovery + CMDB (barcode it). Intangible → data-discovery + classification + registers (must discover & document).
Why is intangible asset inventory harder? :: No physical form to tag or scan — you must DISCOVER, CLASSIFY, and DOCUMENT it.

## Security Models & Frameworks

Bell-LaPadula — focus and rules? :: Confidentiality — 'no read up / no write down'.
Biba — focus and rules? :: Integrity — 'no read down / no write up'.
What is the Lipner implementation? :: Combines Bell-LaPadula (confidentiality) + Biba (integrity) to enforce both.
Zachman vs SABSA vs TOGAF? :: Zachman = matrix/taxonomy (what/how/where/who/when/why); SABSA = risk/business-driven SECURITY architecture; TOGAF = general EA method (ADM).
What does 'fail securely' / fail-safe mean? :: On failure, default to a SECURE/denied state (don't fail open).
What is Zero Trust? :: 'Never trust, always verify' — no implicit trust from network location; supersedes trust-but-verify.
What is 'secure defaults'? :: Ship/configure systems in the most secure state out of the box; loosening is opt-in.
Cloud shared responsibility — the split? :: Provider secures OF the cloud (infrastructure); customer secures IN the cloud (data/config/access). Shifts across IaaS→PaaS→SaaS.
FISMA vs FedRAMP? :: FISMA = US law requiring federal agencies to secure info systems (via NIST RMF); FedRAMP = standardized security authorization for cloud services sold to government.
ISO 27001 vs 27002? :: 27001 = the certifiable ISMS (management system); 27002 = the catalog of security controls.

## Security Evaluation Criteria

TCSEC (Orange Book) — what is it? :: Old US DoD standard; confidentiality-only; evaluates a single standalone system; superseded by Common Criteria.
TCSEC vs ITSEC — key difference? :: TCSEC = US, confidentiality only, BUNDLES functionality + assurance into one rating. ITSEC = European, full CIA, networked, SEPARATES functionality from assurance.
What is Common Criteria (CC)? :: The international evaluation standard, ISO/IEC 15408, that superseded TCSEC/ITSEC; assigns an EAL.
Common Criteria — what are PP, TOE, ST? :: PP (Protection Profile) = the security needs the CUSTOMER wants; TOE (Target of Evaluation) = the product being evaluated; ST (Security Target) = what the VENDOR claims the TOE does.
What is an EAL? :: Evaluation Assurance Level — the CC rating, EAL1 (functionally tested) → EAL7 (formally verified design & tested).
Certification vs Accreditation? :: Certification = the TECHNICAL evaluation against a standard; Accreditation = MANAGEMENT's formal authorization to operate (accepts residual risk).

## System Architecture & Trusted Computing

What is the TCB (Trusted Computing Base)? :: The totality of protection mechanisms (hardware + software + firmware) that enforce the security policy — everything you must trust.
Reference Monitor — what it is + 3 required properties? :: The abstract concept that mediates ALL subject→object access. Must be: always invoked (non-bypassable), tamperproof, and small enough to be verifiable.
Reference Monitor vs Security Kernel? :: Reference monitor = the abstract CONCEPT (mediate all access); security kernel = the actual IMPLEMENTATION (HW/firmware/SW) of it.
Subject vs Object (access control)? :: Subject = active entity requesting access (user/process); Object = passive resource being accessed (file/record/device).
Ring Protection Model — Ring 0 vs Ring 3? :: Ring 0 = kernel (most privileged); Ring 3 = user programs (least privileged). Rings 1–2 = OS components/drivers. Lower ring # = more privilege.
Problem state vs supervisor state (= user vs kernel mode)? :: Problem/user = restricted instruction set (apps); supervisor/kernel = full privilege (OS kernel).
What is process isolation? :: Each process runs in its own protected memory space so it can't read or corrupt another's — prevents leakage/tampering.
Primary vs secondary storage vs virtual memory? :: Primary = RAM (fast, volatile); secondary = disk (persistent); virtual memory = using disk paging to extend RAM.
What is firmware (TCB relevance)? :: Software on non-volatile chips (BIOS/UEFI, device microcode) that boots/controls hardware — a TCB component that must be trusted.

## System Vulnerabilities & Threats

What is a Single Point of Failure (SPOF) and its fix? :: A component whose failure takes down the whole system; fix = redundancy / fault tolerance (failover, clustering).
What is TOCTOU, and how do you mitigate it? :: Time-Of-Check to Time-Of-Use — a race condition where state changes between check and use; mitigate by locking the resource and re-validating at the moment of use.
What are emanations, and the countermeasure? :: Unintended electromagnetic signals leaking from devices that can reconstruct data; countered by TEMPEST (shielding/Faraday cage, white noise, control zones).
Covert storage vs covert timing channel? :: Storage = communicate by writing/reading a shared resource; timing = communicate by modulating the timing/use of resources.
Aggregation vs Inference (DB attacks)? :: Aggregation = COMBINE accessible facts to build a secret; Inference = DEDUCE a secret from accessible clues.
What is polyinstantiation, and what does it defend against? :: Keeping multiple versions of data at different classification levels (lower-cleared users see a cover value) — defends against inference.

## Mobile Security

Authentication vs Authorization? :: Authentication = verifying WHO you are; Authorization = enforcing WHAT you're allowed to do.
Core mobile device security controls? :: MDM enforcing encryption, screen lock, remote wipe, app control — plus policy + training.

## Cloud & Virtualization

List the 5 essential cloud characteristics (NIST). :: On-Demand Self-Service, Broad Network Access, Resource Pooling, Rapid Elasticity, Measured Service.
IaaS vs PaaS vs SaaS — what the CUSTOMER manages? :: IaaS = OS + apps + data; PaaS = apps + data; SaaS = only your data/config. Customer's burden shrinks IaaS→SaaS.
Cloud deployment models? :: Public (shared/open), Private (single org), Community (orgs with a common concern), Hybrid (mix).
Type 1 vs Type 2 hypervisor? :: Type 1 = bare-metal (runs on hardware, more secure); Type 2 = hosted (runs on a host OS).
Containers vs VMs — isolation and weight? :: Containers share the HOST OS KERNEL (lightweight, weaker isolation); VMs run a FULL guest OS each (heavier, stronger isolation).
What is serverless (FaaS)? :: Running event-driven functions without managing servers — the provider handles provisioning/scaling.
Cloud roles + GDPR mapping? :: Cloud Consumer = CONTROLLER (accountable); Cloud Provider = PROCESSOR; Cloud Broker = intermediary; Cloud Auditor = independent assessment.
What is a VM escape? :: Code breaking out of a guest VM to the hypervisor/host — the key virtualization isolation risk (protect the hypervisor as TCB).
Why does a cloud SLA matter for security? :: It contractually defines the provider's measurable commitments (uptime, RTO/RPO, breach notification) — your main lever since you don't own their infrastructure.

## Cryptography — Services & Terminology

What are the four cryptographic services? :: Confidentiality (encryption), Integrity (hashing), Authenticity (proof of source), Non-repudiation (digital signatures).
What is non-repudiation, and what provides it? :: The sender can't deny sending — provided by digital signatures (private key only the signer holds).
What is Kerckhoffs's principle? :: A cryptosystem must be secure even if everything except the KEY is public — security rests on the key, not on hiding the algorithm.
What is key clustering? :: A weakness where two DIFFERENT keys produce the SAME ciphertext from the same plaintext.
What is work factor? :: The time/effort/resources required to break a cryptosystem — higher = stronger.
What is an IV / nonce, and the rule? :: A random/unique value so identical plaintexts encrypt to different ciphertexts; must NOT be reused.
Confusion vs diffusion? :: Confusion = hide the key↔ciphertext relationship (substitution); Diffusion = spread one plaintext bit across many ciphertext bits (transposition/permutation).
What is the avalanche effect? :: A 1-bit input change flips ~half the output bits — a property of strong ciphers/hashes.
Steganography vs cryptography? :: Steganography HIDES that a message exists; cryptography SCRAMBLES the message (existence obvious, content not).

## Cryptography — Hashing

Is hashing one-way or two-way, and what does it provide? :: One-way (can't reverse); provides integrity — a fixed-length fingerprint that changes if the data changes.
MD5 and SHA-1 — status and sizes? :: Both deprecated/broken (collisions). MD5 = 128-bit, SHA-1 = 160-bit. Don't use for security.
SHA-2 vs SHA-3? :: SHA-2 (SHA-256/512) = current widely-used standard; SHA-3 = newer alternative family (different internal design).
Why does salting matter for password hashing? :: A unique random salt per password defeats precomputed (rainbow-table) attacks and makes identical passwords hash differently.

## Cryptography — Symmetric

What is symmetric encryption (and its challenge)? :: One SHARED secret key for encrypt + decrypt — fast, good for bulk data; key distribution is the challenge.
Block vs stream cipher? :: Block = fixed-size blocks (e.g., 128-bit); Stream = bit/byte-by-byte (keystream XORed with data), good for real-time.
DES vs 3DES — status? :: DES = 56-bit key, broken/obsolete. 3DES = DES applied 3×, a stopgap, now NIST-deprecated (disallowed after 2023).
What is AES (Rijndael)? :: The global symmetric block-cipher standard; 128-bit blocks; 128/192/256-bit keys; replaced DES/3DES.
What is RC4? :: A symmetric STREAM cipher — fast but insecure (biases); deprecated (used in WEP/early TLS).
What were the 5 AES-competition finalists? :: MARS, RC6, Rijndael (WINNER → AES), Serpent, Twofish — all considered secure.
Is RC6 secure / should it be discontinued? :: Secure (an AES finalist) — do NOT discontinue it. It's just rarely used in practice.
Secure/modern symmetric ciphers (keep)? :: AES, CAST-256/CAST-128, Twofish, Serpent, Blowfish, RC6.
Weak/legacy symmetric ciphers (avoid)? :: DES (56-bit), 3DES (deprecated), RC4 (broken stream), SKIPJACK (80-bit, NSA/Clipper).
What is SKIPJACK? :: An NSA block cipher (Clipper chip), 80-bit key — old, weak, tied to key escrow. Not secure today.
What is CAST-256? :: A modern symmetric block cipher (256-bit), AES candidate — considered secure.
Exam tactic — "most secure symmetric algorithm"? :: Eliminate legacy/broken (DES, 3DES, RC4, SKIPJACK); pick the modern survivor (AES, CAST-256, Twofish). Don't assume old/NSA = strong.
Exam tactic — "which to discontinue"? :: Pick the OLD/broken ones (DES family, RC4, SKIPJACK) — don't flag an unfamiliar-but-modern cipher (e.g., RC6) just because you haven't heard of it.
Block mode ECB — why avoid it? :: Each block encrypted independently → identical plaintext blocks give identical ciphertext (leaks patterns).
Which block mode propagates errors between blocks, and why? :: CBC — each block is XORed with the previous ciphertext block, so a corrupted block affects the next. "Chaining" = error propagation.
Which modes don't propagate errors between blocks? :: Stream/counter modes — OFB, CTR, GCM (a bit error affects only the matching bit).
Which block modes provide BOTH confidentiality AND authenticity? :: GCM and CCM. ECB/CBC/OFB/CTR = confidentiality only.
What is AES's maximum key length? :: 256 bits. Valid sizes: 128/192/256 (NOT 512).
Symmetric key count for n users? :: n(n-1)/2 shared keys (one per pair of users). 6 users = 6×5/2 = 15.
Asymmetric key count for n users? :: 2n keys — each user has ONE key PAIR (public + private). 6 users = 12. (Contrast: symmetric = n(n-1)/2 = 15 for 6 users.)
What is the only cryptosystem proven unbreakable? :: The one-time pad — IF the key is truly random, as long as the message, used once, kept secret. All others (incl. AES) are theoretically attackable.

## Cryptography — Asymmetric & Signatures

What is asymmetric encryption? :: A key PAIR (public + private); what one encrypts only the other decrypts. Solves key distribution; slower → used for key exchange/signatures.
RSA is based on which hard problem? :: Integer factoring (factoring the product of two large primes).
Diffie-Hellman, ECC, ElGamal, DSA are based on which hard problem? :: The discrete logarithm problem.
Is Diffie-Hellman symmetric or asymmetric? :: ASYMMETRIC (discrete-log family). The ONLY "symmetric" thing about it is the shared key it PRODUCES — the algorithm itself is asymmetric.
What is Diffie-Hellman used for? :: Key EXCHANGE — an asymmetric method to agree a shared SYMMETRIC key over an insecure channel without pre-sharing it. It does NOT encrypt the data itself (AES does that afterward).
Why does the symmetric key count (n(n-1)/2) matter? :: It scales badly (many users → huge number of shared keys to distribute) — this key-distribution problem is WHY asymmetric crypto / Diffie-Hellman exists.
What is ECC? :: Asymmetric crypto giving equivalent security with much SMALLER keys — efficient for mobile/low-power.
ECC vs RSA — key length for equivalent strength? :: ECC keys are far shorter — ~256-bit ECC ≈ 3072-bit RSA. Same security, smaller key.
What is a digital signature, and what does it provide? :: Sign a message's hash with your PRIVATE key; verify with your PUBLIC key → integrity + authenticity + non-repudiation (not confidentiality).
What is a digital certificate? :: A CA-signed binding of a public key to an identity (X.509) — lets you trust a public key belongs to that party.

## Cryptography — Classical Ciphers

Substitution vs transposition? :: Substitution REPLACES symbols (gives confusion); transposition REORDERS symbols (gives diffusion). Modern ciphers use both.
Monoalphabetic vs polyalphabetic substitution? :: Mono = one fixed substitution alphabet (broken by frequency analysis); poly = multiple alphabets (e.g., Vigenère), resisting it.

## PKI & Certificates

What is X.509? :: The standard format for digital certificates (subject, public key, issuer, validity, serial, CA signature).
What is certificate revocation? :: Invalidating a cert before expiry (e.g., key compromise) so it's no longer trusted.
CRL vs OCSP? :: CRL = downloaded list of revoked certs (can be stale); OCSP = real-time per-certificate status check (current).
What is certificate pinning? :: Hard-coding a specific expected cert/public key in the client, so a fraudulent-but-valid cert is rejected (defeats some MITM).
What is PKI? :: Public Key Infrastructure — the CAs, RAs, certs, CRLs, policies that create/manage/distribute/revoke certificates.
CA vs RA? :: CA issues/signs certs (root of trust); RA verifies the requester's identity before issuance (doesn't issue).
Why keep the root CA offline (use intermediate CAs)? :: To protect the root of trust — if the root key is compromised the whole PKI fails, so day-to-day issuance is delegated to intermediates.

## Key Management

Key-distribution methods? :: Diffie-Hellman (negotiate a shared secret), out-of-band (separate channel), hybrid (asymmetric to exchange a symmetric key).
TPM vs HSM? :: TPM = a chip on a single device (per-machine, e.g., backs BitLocker); HSM = a dedicated enterprise appliance for bulk key operations.
What is key rotation? :: Periodically replacing keys to limit exposure and reduce how much data one key protects.
What is crypto-shredding? :: Destroying the encryption key so the encrypted data becomes permanently unrecoverable — a fast way to "destroy" data.
Split knowledge vs dual control? :: Split knowledge = the SECRET is divided among people (no one knows it all); dual control = an ACTION requires two people together.
What is key escrow? :: A trusted third party holds a copy of keys so data can be recovered or accessed under authorized conditions.

## Cryptanalytic & Implementation Attacks

Brute-force attack, and the defense? :: Try every possible key; defeated by large key length (high work factor).
Ciphertext-only attack? :: Attacker has ONLY ciphertext — the hardest scenario for the attacker.
Known vs chosen plaintext attack? :: Known = attacker is GIVEN existing plaintext/ciphertext pairs; Chosen = attacker actively PICKS plaintexts to encrypt.
What is a man-in-the-middle (MITM) attack, and the defense? :: Attacker secretly relays/alters communication between two parties; defeated by authentication (certificates).
What is a replay attack, and the defense? :: Capture valid (often auth) data and resend it later; defeated by nonces, timestamps, session keys, challenge-response.
What is a pass-the-hash attack? :: Stealing a password HASH and using it directly to authenticate — no need to crack the password.
What is a side-channel attack? :: Attacking the IMPLEMENTATION via physical leakage — timing, power consumption, electromagnetic — not the math.
What are rainbow tables, and the defense? :: Precomputed hash→password lookup tables; defeated by salting.
What is a birthday attack? :: Exploiting hash COLLISION probability (two inputs → same hash); why hash output length must be large.

## Physical Security — Controls

#1 priority in physical security? :: Safety of PEOPLE — life safety always overrides asset protection.
Functional order of physical controls? :: Deter → Delay → Detect → Assess → Respond.
What is CPTED? :: Crime Prevention Through Environmental Design — layout, lighting, landscaping, natural surveillance to deter crime.
What is a mantrap? :: A two-door entry where the first must close before the second opens — prevents tailgating/piggybacking.

## Physical Security — Power

UPS vs generator? :: UPS = battery, short-term, rides through outages / allows safe shutdown; generator = fuel-powered, long-term backup (UPS bridges until it starts).
Power anomalies — momentary vs prolonged? :: Low: sag (momentary) / brownout (prolonged). High: spike (momentary) / surge (prolonged). Loss: fault (momentary) / blackout (prolonged).

## Physical Security — HVAC

Why control humidity in a data center? :: Too LOW → static/ESD damages components; too HIGH → condensation/corrosion.
What is positive pressure (air quality)? :: Room pressure higher than outside so air (and contaminants/smoke) flows OUT, not in.

## Fire Detection & Suppression

Ionization vs photoelectric smoke detector? :: Ionization = fast FLAMING fires; photoelectric = slow SMOLDERING fires.
What does suppression remove (fire triangle)? :: Fire needs heat + fuel + oxygen (+ reaction); suppression removes one (water=heat, gas/CO2=oxygen/reaction).
Wet vs dry pipe sprinkler? :: Wet = pipes always hold water, discharge immediately (leak risk). Dry = pipes hold pressurized air, water fills only when a head opens (for cold areas).
Pre-action sprinkler (and why for data centers)? :: Requires BOTH a detector trip AND a head to open before water flows (double-knock) — minimizes accidental discharge.
Why use clean-agent gas (FM-200/INERGEN) suppression? :: Suppresses fire without water damage to electronics; but watch human safety (oxygen displacement).
CO2 suppression — benefit and danger? :: Displaces oxygen to smother fire — very effective but DANGEROUS to people (asphyxiation); unoccupied spaces only.

## Malware

Virus vs worm? :: Virus needs a host file + user action to spread; worm self-propagates across networks automatically.
What is a Trojan? :: Malware disguised as legitimate software; the user runs it willingly, but it carries a hidden payload.
What is a logic bomb? :: Malicious code that lies dormant and triggers when a CONDITION is met (a date, an event).
What is a rootkit? :: Malware embedded deep (often kernel-level) to hide itself and keep privileged, persistent access.
What is ransomware? :: Malware that encrypts/locks the victim's data and demands payment for the key.
What is a botnet? :: A network of compromised hosts ("bots") controlled via command-and-control (C2) — used for DDoS, spam.
What is a polymorphic virus? :: Malware that mutates its code/signature each infection to evade signature-based detection.
What is a salami attack? :: Stealing tiny amounts repeatedly (fractions of a cent) that add up while staying unnoticed.
What is a zero-day? :: An attack exploiting an unknown/unpatched vulnerability — no signature or fix exists yet.
Signature-based vs heuristic malware detection? :: Signature = matches KNOWN patterns (misses zero-day); heuristic = analyzes behavior to catch UNKNOWN malware (more false positives).
How does application allow-listing prevent malware? :: Only approved programs may run — anything not on the list (incl. new malware) is blocked by default.

## Scenarios (Application)

Scenario: Enforce a security baseline on 500 DOMAIN-JOINED Windows PCs and keep it enforced over time. Best tool? :: Group Policy (GPO) — centralized enforcement that auto-reapplies and corrects drift.
Scenario: The Windows laptops are NOT domain-joined. How do you push the baseline? :: Intune/MDM — GPO needs Active Directory.
Scenario: A user reports the website now shows an attacker's message. Which CIA element, and likely attack? :: Integrity — web defacement, often via SQL injection or stolen admin access.
Scenario: Verify in REAL TIME whether one certificate has been revoked. CRL or OCSP? :: OCSP — real-time per-cert status (a CRL can be stale).
Scenario: No single employee should be able to recover the master key alone. Which controls? :: Split knowledge (each holds part) + dual control (two people required to act).
Scenario: A pen tester recovers a password using a precomputed hash-lookup table. Attack and defense? :: Rainbow table attack — defense is salting.
Scenario: Malware spread across the whole network overnight with no one clicking anything. Virus or worm? :: A worm — it self-propagates without user action.
Scenario: AV keeps missing malware because it changes its code each infection. Type and detection? :: Polymorphic malware — needs heuristic/behavior-based detection.
Scenario: You want to stop ANY unapproved program (incl. unknown malware) from executing on endpoints. Best control? :: Application allow-listing (deny-by-default).

## High-Yield Discriminators

Quantitative risk: you add a countermeasure — which factor changes? :: ARO (Annualized Rate of Occurrence) — the control reduces how OFTEN the risk happens per year. (It may also lower EF, but ARO is the primary change.)
Which provides inherent NON-REPUDIATION: HMAC, ECDSA, MD5, SHA-1? :: ECDSA (a digital SIGNATURE with a private key only the signer holds). HMAC uses a SHARED secret → no non-repudiation. MD5/SHA-1 = just hashes.
Which crypto mode best supports PARALLELIZED encryption/decryption? :: Galois/Counter Mode (GCM) — counter-based, independent blocks parallelize (and it adds authentication). CBC/CFB chain sequentially.
Attack against algorithms lacking TEMPORAL (time) protections? :: Replay attack — capture a valid message and resend it. Defenses: timestamps, nonces, ephemeral session keys, challenge-response.
Verifying a server's digital certificate — what do you check? :: (1) CA's signature authentic, (2) not expired, (3) not revoked (CRL/OCSP). You do NOT separately "verify the sender's public key is valid" — the CA signature already vouches for it.
Anonymization method that CANNOT be reversed (GDPR-safe)? :: Randomized masking done correctly = irreversible. Pseudonymization, encryption, tokenization are all REVERSIBLE.
Community vs Public vs Private vs Hybrid cloud? :: Community = multiple orgs with a COMMON concern. Public = open to anyone. Private = one org. Hybrid = mix. "SaaS shared with another organization" = community.
Dual-core single-processor: how many threads run AT ANY GIVEN INSTANT? :: Two (one per core). More threads can exist, but cores limit simultaneous execution.
Scoping vs tailoring? :: Scoping = REMOVING controls from a baseline that don't apply. Tailoring = adjusting/customizing the baseline (incl. compensating controls).

## CISSP Exam-Outline Gap-Fill

Clark-Wilson model — focus and mechanism? :: Integrity — enforces well-formed transactions + separation of duties; subjects access data ONLY through authorized programs (the access triple: subject → program → object), never directly.
Brewer-Nash (Chinese Wall) model — purpose? :: Prevents CONFLICTS OF INTEREST — access is dynamically restricted based on what you've ALREADY accessed (a consultant who saw Bank A's data is blocked from competitor Bank B's).
Bell-LaPadula — the two named properties? :: Simple Security Property = NO READ UP; Star (*) Property = NO WRITE DOWN. (Confidentiality.)
Biba — the two named properties? :: Simple Integrity = NO READ DOWN; Star (*) Integrity = NO WRITE UP. (Integrity.)
Defense in depth (design principle)? :: Layering multiple independent controls so no single failure breaks security (perimeter → network → host → app → data).
What is privacy by design? :: Building privacy into systems from the start and by default — not bolting it on later.
What is ICS/SCADA, and the security concern? :: Industrial Control Systems / Supervisory Control And Data Acquisition — run physical infrastructure (power/water/manufacturing); legacy, fragile, often unpatchable → isolate and segment (allowlist, no direct internet).
IoT security concerns and the control? :: Internet-of-Things devices have weak defaults, rare patching, large attack surface → put them on their own segmented network, change defaults, monitor.
What is an embedded system (security)? :: A computer built into a larger device (medical/automotive/appliance) with fixed function; hard to patch → secure by isolation and secure-by-design.
What are Spectre and Meltdown? :: CPU speculative-execution vulnerabilities that leak memory across boundaries; mitigated by OS/firmware microcode updates.

## Scenarios — Crypto Selection

You need strong, fast, standard encryption for bulk data at rest on company laptops. Best choice? :: AES-256 — symmetric, fast, the global standard for data at rest.
You must encrypt a real-time voice/video stream with minimal latency. Block or stream cipher? :: Stream cipher — encrypts bit/byte-by-byte, suited to continuous real-time data.
You need one cipher mode that gives BOTH confidentiality AND authenticity. Pick it. :: GCM (or CCM) — authenticated encryption; ECB/CBC/CTR give confidentiality only.
A developer wants to encrypt many records with a block cipher but identical records keep producing identical ciphertext. What's wrong, what to use? :: They're using ECB — switch to CBC or GCM so patterns don't leak.
You only need to confirm a downloaded file wasn't altered. Symmetric, asymmetric, or hashing? :: Hashing (SHA-256) — integrity only, no key needed.
You must let a recipient prove the sender cannot deny authoring a message. Which mechanism? :: Digital signature — sign with the sender's private key (non-repudiation).
Two parties must agree a shared symmetric key over an insecure channel without pre-sharing one. Method? :: Diffie-Hellman key exchange — asymmetric agreement of a symmetric key.
A low-power IoT/mobile device needs asymmetric crypto with the smallest possible keys. Choose. :: ECC — equivalent strength at far shorter key lengths than RSA.
You must store user passwords so a stolen database can't be reversed and rainbow tables fail. How? :: Salted one-way hash (per-password salt) — never reversible encryption.
You're told to discontinue the weakest cipher from: AES, RC6, DES, Twofish. Which? :: DES — 56-bit, broken; the others are modern/secure (don't flag unfamiliar-but-modern RC6).

## Scenarios — Security Models

You must stop low-integrity data from corrupting high-integrity records. Which model? :: Biba — integrity, no read down / no write up.
You must keep highly classified data from leaking to lower clearances. Which model? :: Bell-LaPadula — confidentiality, no read up / no write down.
A consultant who viewed Bank A's files must be blocked from Bank A's competitors. Which model? :: Brewer-Nash (Chinese Wall) — dynamically prevents conflicts of interest.
You need commercial integrity via well-formed transactions and separation of duties, with users touching data only through approved programs. Model? :: Clark-Wilson — the access triple (subject → program → object).

## Scenarios — Key Management & PKI

You must wipe cloud-hosted data fast without physically destroying shared disks. Technique? :: Crypto-shredding — destroy the encryption key so the data is unrecoverable.
You need per-machine hardware key storage to back full-disk encryption on each laptop. TPM or HSM? :: TPM — a chip on a single device; HSM is the enterprise appliance for bulk key operations.
A datacenter needs high-throughput, tamper-resistant key operations for many servers. TPM or HSM? :: HSM — dedicated enterprise appliance for bulk key handling.
You want to limit how much data a single key ever protects. Practice? :: Key rotation — periodically replace keys to cap exposure.
A valid-but-fraudulent CA-issued certificate is enabling MITM on your app. Defense? :: Certificate pinning — hard-code the expected cert/key so others are rejected.
Your root CA key compromise would collapse the whole PKI. How do you reduce that risk? :: Keep the root CA offline and issue day-to-day certs from intermediate CAs.

## Scenarios — Physical, Fire & Environmental

A datacenter needs fire suppression that avoids water damage AND accidental discharge. Choose. :: Pre-action sprinkler — needs both a detector trip and an open head before water flows.
An occupied server room needs suppression that won't damage electronics. Choose. :: Clean-agent gas (FM-200/INERGEN) — suppresses without water; mind oxygen displacement.
An UNoccupied vault needs the most effective gas suppression and asphyxiation risk is acceptable. Choose. :: CO2 — smothers fire by displacing oxygen; people-only-absent spaces.
Sprinkler pipes run through an unheated area that freezes. Which sprinkler type? :: Dry pipe — pipes hold pressurized air, water enters only on activation.
You must stop tailgating/piggybacking at a secure entrance. Control? :: Mantrap — first door must close before the second opens.
Adversaries are reconstructing data from a device's electromagnetic emanations. Countermeasure? :: TEMPEST — shielding/Faraday cage, white noise, control zones.

## Scenarios — Cloud, Virtualization & Design Principles

You must maximize tenant isolation between two untrusted workloads. Containers or VMs? :: VMs — full guest OS each gives stronger isolation than kernel-sharing containers.
The top isolation risk in your virtualized host is code breaking out of a guest. Name it + the asset to protect. :: VM escape — protect the hypervisor as part of the TCB.
A system must default to a denied/safe state if a control fails. Which design principle? :: Fail securely (fail-safe) — never fail open.
Products must ship locked down, with loosening as an opt-in. Which principle? :: Secure defaults.
Access must never be granted from network location alone, always re-verified. Principle? :: Zero Trust — never trust, always verify.
