# D4 Protocol Quick-Reference

## Overview

Focused cram-style note on the specific D4 protocol/standard items that are commonly tested and were not well-covered in existing notes. Complements [Network Protocols](Network%20Protocols.md), [WAN Technologies and Protocols](WAN%20Technologies%20and%20Protocols.md), [OSI and TCP-IP Models](OSI%20and%20TCP-IP%20Models.md), and [Network Devices and Components](Network%20Devices%20and%20Components.md).

## Baseband vs Broadband — REVERSED-PAIR TRAP

| Type | How it uses the channel | Distance | Channels |
|---|---|---|---|
| **Baseband** | **Uses the entire communication channel** for its transmission | Limited (single segment) | Single channel, full bandwidth |
| **Broadband** | **Divides the communication channel** into multiple independent channels | Longer | Multiplexed, multiple channels |

**Trap:** The wrong options swap which uses "entire" vs which "divides." Memorize:
- **BASE**band = uses entire channel as the **BASE** (one path)
- **BROAD**band = **BROAD**-cast across multiple sub-channels

## H.323

- **International standard** for **audio and video calls over packet-based networks**
- Developed by ITU-T (ITU Telecommunication Standardization Sector)
- Suite of protocols, not a single protocol
- Used in early VoIP and video conferencing
- **SIP (Session Initiation Protocol)** is a competing/successor standard but **H.323 is THE international standard** per CISSP framing
- **Trigger phrase:** "international standard that deals with audio and video calls over packet-based networks" → **H.323**

## SONET (Synchronous Optical Network)

- **Physical-layer standard for transmitting data over fiber-optic lines** (this is the trigger phrase)
- Ring topology with self-healing failover
- Carries multiple T-circuits and ATM over fiber
- High bandwidth (OC-3 = 155 Mbps, OC-192 = 10 Gbps, etc.)
- North American standard; SDH is the international equivalent
- **Trigger phrase:** "physical layer standard for transmitting data over fiber-optic lines" → **SONET**

## ATM (Asynchronous Transfer Mode)

- WAN technology using **53-byte fixed-size cells**
- Low delay (good for time-sensitive applications like voice/video)
- Cell structure: 48 bytes payload + 5 bytes header = 53 bytes
- Connection-oriented (virtual circuits)
- **Trigger phrase:** "53-byte cells" / "low delay" / "time-sensitive applications" → **ATM**

## FDDI

- Fiber Distributed Data Interface
- 100 Mbps over fiber
- Dual ring topology (counter-rotating) for redundancy
- Token-passing access method
- Mostly legacy / historical

## QoS Bit Rate Services

For ATM and similar circuit services:

| Service | Description |
|---|---|
| **CBR** (Constant Bit Rate) | **Consistent throughput** for time-sensitive apps (voice, video) — guaranteed bandwidth |
| **VBR** (Variable Bit Rate) | Variable bandwidth, suitable for bursty traffic |
| **ABR** (Available Bit Rate) | Uses whatever bandwidth is available; minimum guaranteed |
| **UBR** (Unspecified Bit Rate) | Best-effort, no guarantee |

**Trigger phrase:** "consistent data throughput for time-sensitive applications" → **CBR (Constant Bit Rate)**

## DSL Service Types

| Service | Upstream vs Downstream |
|---|---|
| **ADSL** (Asymmetric) | Different speeds — usually higher download than upload (residential) |
| **SDSL** (Symmetric) | **Same speed upstream AND downstream** (business) |
| **VDSL** (Very high speed) | Asymmetric, very fast |
| **BRI ISDN** | Basic Rate Interface — 2B+D channels, legacy |
| **BISDN** | Broadband ISDN, supports higher speeds |

**Trigger phrase:** "DSL where traffic flows at the same speed upstream and downstream" → **Symmetric service** (SDSL)

## NFC (Near Field Communications)

- Short-range RF (a few centimeters)
- Base frequency **13.56 MHz**
- Used for contactless payments, smart cards, device pairing
- Distinct from Bluetooth (longer range, different band) and Wi-Fi
- **Trigger phrase:** "few centimeters" + "13.56 MHz" → **NFC**

## OSI Layer → Device Mapping

| Layer | OSI Name | Devices that operate here |
|---|---|---|
| 1 | Physical | **Hub**, Repeater, Cables, NIC (some) |
| 2 | Data Link | **Bridge**, **Switch** (basic L2 switches) |
| 3 | Network | **Router**, L3 Switch |
| 4 | Transport | (Firewalls in some classifications, esp. stateful) |
| 5-6 | Session / Presentation | (typically software, not dedicated devices) |
| 7 | Application | **Gateway**, Proxy, Application Firewall |

**Trigger phrase:** "Operates at the application layer of the OSI model" → **Gateway**

## Wi-Fi Encryption Algorithms

- **WEP** uses **RC4** (broken, deprecated)
- **WPA** uses RC4 + TKIP (transitional, also weak)
- **WPA2** uses **AES with CCMP**
- **WPA3** uses AES with **SAE** (Simultaneous Authentication of Equals — replaces PSK)

**Trigger phrase:** "WEP uses which algorithm?" → **RC4**

## Spread Spectrum

- **Spread spectrum technologies:** FHSS (Frequency Hopping), DSSS (Direct Sequence)
- **NOT spread spectrum:** OFDM (multi-carrier modulation), WPA2 (encryption protocol)

**Trigger phrase:** "Are NOT spread spectrum?" → **OFDM and WPA2**

## VPN IPSec Modes (cross-referenced from D5)

- **Transport mode** = host-to-host, only payload encrypted
- **Tunnel mode** = gateway-to-gateway / VPN, **entire packet encrypted**
- VPNs almost always use **Tunnel mode**

## Block Ciphers Internal Mechanism

- Block ciphers use **S-boxes** (Substitution boxes) for mathematical functions, substitution, and permutations on message bits
- NOT initialization vectors (those initialize the cipher in certain modes)
- NOT digital certificates
- NOT keystream generators (those are for stream ciphers)

**Trigger phrase:** "Used to perform mathematical functions, substitution, and permutations on message bits" → **S-boxes**

## ARP / RARP / DHCP

| Protocol | Function |
|---|---|
| **ARP** (Address Resolution Protocol) | **Translates IP → MAC** (asks "who has this IP?") |
| **RARP** (Reverse ARP) | Translates MAC → IP (legacy; replaced by DHCP) |
| **DHCP** | Assigns IP addresses dynamically (DORA handshake) |

**Trigger phrase:** "Translates IP address into MAC address" → **ARP**

## Related Topics

- [Network Protocols](Network%20Protocols.md) — broader protocol coverage
- [WAN Technologies and Protocols](WAN%20Technologies%20and%20Protocols.md) — WAN-specific
- [OSI and TCP-IP Models](OSI%20and%20TCP-IP%20Models.md) — layer reference
- [Network Devices and Components](Network%20Devices%20and%20Components.md) — device deep-dive
- [Wireless Security](Wireless%20Security.md) — WEP/WPA detail
- [CRAM-SHEET](../../practice/sheets/CRAM-SHEET.md)
