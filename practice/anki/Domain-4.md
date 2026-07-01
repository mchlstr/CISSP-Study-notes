# Anki Deck — Domain 4 (Communication & Network Security)

> Format: `Question :: Answer` (Obsidian_to_Anki compatible). Pruned for exam-yield: atomic, gradeable cards only.

## Protocols & Secure Transport

Telnet — secure? port? replacement? :: Insecure (port 23, plaintext incl. credentials); replace with SSH (port 22).
TCP vs UDP? :: TCP = connection-oriented + reliable (handshake, delivery guarantees); UDP = connectionless + fast/unreliable (streaming, VoIP, DNS).
IPsec AH vs ESP? :: ESP = encryption + integrity; AH = integrity/authentication only, NO encryption.
TLS vs IPsec — scope? :: TLS = per-connection transport/app traffic (S in HTTPS); IPsec = ALL IP traffic at the network layer (L3).

## OSI Model

List the 7 OSI layers, L1→L7. :: Physical, Data Link, Network, Transport, Session, Presentation, Application ("Please Do Not Throw Sausage Pizza Away").
OSI vs TCP/IP model? :: OSI = 7-layer reference; TCP/IP = 4 layers (Link, Internet, Transport, Application).
Layer 1 (Physical) — function and devices? :: Transmits raw BITS over the medium; devices = hubs, repeaters (regenerate signals, no addressing).
Layer 2 (Data Link) — function, addressing, devices? :: Node-to-node delivery using FRAMES + MAC addresses; devices = switches, bridges.
Layer 3 (Network) — function, addressing, devices? :: Logical addressing + ROUTING of PACKETS; IP addresses; devices = routers, packet-filtering firewalls. (IPsec operates here.)
Layer 4 (Transport) — function and what identifies a service? :: End-to-end delivery via SEGMENTS using PORTS (e.g., 443=HTTPS); TCP (reliable) or UDP (fast). TLS sits around here.
Layer 5 (Session) — function and firewall type? :: Establishes/manages/tears down sessions; circuit-level proxy maps here (e.g., SOCKS).
Layer 6 (Presentation) — function? :: Data translation/formatting — encryption, compression, code conversion (ASCII, JPEG).
Layer 7 (Application) — function, firewall, protocols? :: Network services to apps/users; application proxy = deepest inspection; protocols = HTTP/HTTPS, DNS, SSH, SNMP, LDAP, DHCP.

## Layer 2/3 Protocols

What does ARP do? :: Address Resolution Protocol — maps an IP address to a MAC address on the local network (Layer 2).
What is ICMP? :: Internet Control Message Protocol — error/diagnostic messages (ping, traceroute); Layer 3.
What is 802.1X? :: Port-based network access control — authenticate a device before granting LAN/WLAN access (EAP + RADIUS).
PAP vs CHAP? :: PAP sends the password in PLAINTEXT (insecure); CHAP uses a hashed challenge-response (no password sent over the wire).
EAP vs PEAP? :: EAP = an authentication framework (many methods); PEAP = EAP wrapped inside a TLS tunnel (more secure).
What is BGP? :: Border Gateway Protocol — the internet's routing protocol between autonomous systems (TCP 179).

## Firewalls

Firewall depth by OSI layer? :: Packet filter (L3, IP/port, stateless) < circuit proxy (L5, validates sessions) < application proxy (L7, inspects content). Higher layer = deeper inspection, more overhead.
Stateless vs stateful firewall? :: Stateless = decides per packet (no memory of the connection); stateful = tracks connection state, allowing legitimate return traffic.
What is an application-layer firewall (proxy)? :: Inspects full application content/protocol at L7 (e.g., WAF) — deepest but slowest.

## Common Ports

FTP ports? :: 20 (data) and 21 (control).
SSH port? :: 22.
Telnet port? :: 23 (insecure).
SMTP port? :: 25.
DNS port? :: 53.
HTTP / HTTPS ports? :: 80 / 443.
DHCP ports? :: 67 (server) and 68 (client).
LDAP port? :: 389 (LDAPS = 636).
SNMP ports? :: 161 (and 162 for traps).
RDP port? :: 3389.
SQL ports? :: 1433 (MS SQL), 1521 (Oracle).

## WAN Technologies

What is Frame Relay? :: A packet-switched WAN technology using virtual circuits (successor to X.25).
What is ATM (networking)? :: Asynchronous Transfer Mode — a WAN technology using fixed 53-byte CELLS for predictable, low-latency transport.
What is MPLS? :: Multiprotocol Label Switching — forwards packets by short LABELS instead of IP lookups; fast, supports QoS.

## Wireless

802.11 standards — bands? :: a (5GHz), b/g (2.4GHz), n (both, MIMO), ac (5GHz, gigabit), ax = Wi-Fi 6 (both bands, high efficiency).
What is WEP, and its status? :: Wired Equivalent Privacy — original Wi-Fi encryption using RC4; badly broken, never use.
Wi-Fi encryption evolution (order)? :: WEP (RC4, broken) → WPA (TKIP) → WPA2 (AES-CCMP) → WPA3 (SAE).
What is WPA3's key feature? :: Uses SAE (Simultaneous Authentication of Equals / "Dragonfly") to resist offline password/dictionary attacks.

## IP Addressing

IPv4 vs IPv6? :: IPv4 = 32-bit, needs NAT, address exhaustion. IPv6 = 128-bit, huge space, built-in IPsec, autoconfiguration, no NAT.
IPv4 private address ranges (RFC 1918)? :: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 — not routable on the public internet.
IPv4 address classes? :: A = 0–127, B = 128–191, C = 192–223, D = 224–239 (multicast), E = 240–255 (experimental).

## Converged Protocols

What is VoIP? :: Voice over IP — phone calls over the data network instead of PSTN.
What is iSCSI? :: SCSI storage commands over IP networks (SAN over standard Ethernet/IP).

## Network Attacks

Phases of a network attack? :: Reconnaissance → Enumeration → Vulnerability Analysis → Exploitation.
Recon vs enumeration? :: Recon = passive/general info gathering; Enumeration = actively probing to list specific resources (users, shares, services).
What is a SYN flood? :: A DoS sending many TCP SYNs without completing the handshake, exhausting the half-open connection table.
What is IP spoofing? :: Forging the source IP in packets to impersonate a host or hide the origin.
DoS vs DDoS? :: DoS = one source overwhelms a target; DDoS = many distributed sources (botnet) flood it — harder to block.
What is ARP poisoning, and what does it enable? :: Forged ARP replies map the attacker's MAC to another IP → MITM/interception on a LAN.

## SDN & Defenses

What is SDN? :: Software-Defined Networking — separates the CONTROL plane (decisions) from the DATA plane (forwarding), centrally managed by software.
SDN northbound vs southbound API? :: Northbound = talks UP to applications/orchestration; Southbound = talks DOWN to network devices.
What does ping vs traceroute do? :: Ping = tests reachability/latency (ICMP echo); traceroute = shows the hop-by-hop path to a destination.
What is network segmentation? :: Dividing a network into isolated zones (VLANs/subnets) so a breach can't freely move laterally.
What is a DMZ? :: A semi-trusted zone (behind/between firewalls) hosting public-facing servers, isolated from the internal LAN.
What is a bastion host? :: A hardened, locked-down system intentionally exposed to an untrusted network — minimal services, heavily monitored.
NAT vs PAT? :: NAT = translates private↔public IPs (often 1-to-1); PAT = many-to-one, distinguishing sessions by PORT.
Whitelist vs blacklist? :: Whitelist = allow only what's permitted (deny by default — safer); blacklist = block known-bad, allow the rest (misses new threats).
Honeypot vs honeynet? :: Honeypot = one decoy system to lure/study attackers; honeynet = a whole decoy network. Any activity on them is inherently suspicious.
Ingress vs egress filtering? :: Ingress = filter INBOUND traffic; Egress = filter OUTBOUND (catches data exfiltration / infected hosts calling out).
What is a sandbox? :: An isolated environment to run/analyze untrusted code safely so malware can't reach the real system.

## IDS / IPS

IDS vs IPS? :: IDS = DETECTS and ALERTS (passive, out-of-band); IPS = DETECTS and BLOCKS (active, in-line).
HIDS vs NIDS? :: HIDS = host-based (one system's logs/files/processes); NIDS = network-based (traffic on a segment).
Signature vs anomaly detection? :: Signature = known patterns (low false positives, misses zero-days); Anomaly = baseline deviation (catches unknown, more false positives).

## Remote Access — VPN & Tunneling

What is a VPN? :: A secure remote connection = TUNNELING + ENCRYPTION over an untrusted network.
What is tunneling (and is it secure alone)? :: Encapsulating one protocol's packets inside another; encryption is SEPARATE — tunneling alone isn't secure.
What is GRE? :: Generic Routing Encapsulation — basic tunneling, NO encryption.
What is L2TP? :: Layer 2 Tunneling Protocol — tunnels but has NO encryption of its own; paired with IPsec (L2TP/IPsec).
What is split tunneling, and the risk? :: Only some traffic goes through the VPN, the rest goes direct — RISK: direct traffic bypasses corporate inspection.
What is IKE (IPsec)? :: Internet Key Exchange — negotiates and establishes the Security Associations (keys/parameters) for IPsec.
What is a Security Association (SA)? :: The negotiated security parameters/keys for a connection; ONE-WAY, so bidirectional traffic needs two SAs.
What is mutual authentication? :: Both parties authenticate each other (not just client→server) — defeats impersonation/MITM.

## Remote Authentication — AAA

RADIUS vs TACACS+? :: RADIUS = UDP, encrypts only the password, combines authn+authz, cross-vendor. TACACS+ = TCP, encrypts the whole payload, separates AAA, Cisco.
What is SNMP used for, and the version note? :: Monitoring/managing network devices; use SNMPv3 (v1/v2 send community strings in cleartext).

## High-Yield Discriminators

802.11 wireless collision method vs Ethernet? :: Wi-Fi (802.11) = CSMA/CA (Collision AVOIDANCE — avoid before sending). Ethernet (802.3) = CSMA/CD (Collision DETECTION — detect after). Wireless can't detect collisions, so it avoids.
What is a VLAN (hardware segmentation needing routing)? :: A switch-created Layer-2 segment; separate VLANs need a ROUTER (L3) to talk to each other. "Hardware-imposed segmentation requiring a routing function for intersegment comms" = VLAN (not subnet).
VLAN vs subnet? :: VLAN = L2 segmentation done at the switch (broadcast domain). Subnet = L3 IP-range division. VLANs usually map to subnets but the segmentation mechanism is the switch.
What is VXLAN? :: Virtual eXtensible LAN — an encapsulation protocol that STRETCHES switch-created VLAN segments across subnets and geographic distances. (SD-WAN = manages WAN connectivity; SDN = central programmable network; VPN = secured tunnel.)
Wi-Fi infrastructure modes: stand-alone / wired-extension / enterprise-extension / bridge? :: Stand-alone = WAP not connected to wired net. Wired extension = ONE WAP extending the wired net. Enterprise extension = ONE SSID across MANY WAPs (single logon anywhere in building). Bridge = connects two networks via two WAPs.
Egress filtering to stop DDoS originating from YOUR network — filter what? :: Outbound traffic whose SOURCE address is OUTSIDE your network range (spoofed). It can't legitimately leave your net, so block it. (Ingress filters block inbound spoofed sources.)
IPSec components — which enables multiple simultaneous VPNs? :: ISAKMP (part of IKE) — manages security associations (SAs); SAs are what let one host run multiple VPNs. ESP = encryption+integrity+anti-replay. AH = integrity/origin auth only (no encryption). SKEME/Oakley = key exchange parts of IKE.
Which protocol reauthenticates throughout a session to detect session hijacking? :: IPSec (continual reauthentication). (LEAP = a weak Cisco wireless EAP method; TLS/SSH authenticate at setup.)
NAC agent types — agent-based / agentless / dissolvable / preadmission? :: Agent-based = installed agent can quarantine + auto-update non-compliant hosts. Agentless = scans (ports/services/vuln) to check authorization+baseline, can't auto-remediate. Dissolvable = temporary agent that runs once then deletes itself. Preadmission = must meet security requirements BEFORE joining the network.
DNS: nslookup gives wrong IP, but after ipconfig /flushdns the bad entry is NOT in displaydns — cause? :: Local DNS cache poisoning (the bad cached record was the problem; flushing cleared it). If it were a modified HOSTS file, the entry WOULD reappear in displaydns (hosts entries are boot-persistent, reloaded after flush).
SQL injection attack — which port does the attacker most likely use? :: 443 (HTTPS) — SQLi is delivered THROUGH the web application, not directly to the DB port. 1433=MS SQL, 1521=Oracle (the DB's own ports, not the attack vector here).

## CISSP Exam-Outline Gap-Fill

Secure vs insecure protocol pairs (always pick the secure one)? :: HTTP→HTTPS, FTP→SFTP/FTPS, Telnet→SSH, SNMPv1/2→SNMPv3, LDAP→LDAPS, POP3/IMAP→ over TLS. Replace each plaintext protocol with its TLS/SSH-protected version.
What is S/MIME? :: Secure/MIME — encrypts and digitally signs EMAIL (confidentiality + integrity + non-repudiation) using PKI certificates.
What is DNSSEC, and what it does NOT provide? :: DNS Security Extensions — adds origin authentication + integrity to DNS via digital signatures (stops cache poisoning/spoofing). Does NOT provide confidentiality.
Cabling — UTP vs STP vs coax vs fiber? :: UTP = unshielded twisted pair (cheap, EMI-prone); STP = shielded (EMI resistant); coax = older, more shielding; fiber = light, fastest, immune to EMI, hardest to tap (most secure).
What is plenum-rated cabling? :: Cable with a fire-resistant, low-smoke jacket required in air-handling (plenum) spaces — a safety/code requirement.
Bluetooth attacks — bluejacking vs bluesnarfing vs bluebugging? :: Bluejacking = sending unsolicited messages; Bluesnarfing = STEALING data; Bluebugging = taking full CONTROL of the device.
NFC vs RFID? :: RFID = radio tags read at a distance (asset tracking/badges); NFC = a very short-range (cm) subset (contactless pay/phones).
What is a CDN (Content Delivery Network)? :: Geographically distributed cache servers serving content from near the user — reduces latency and absorbs DDoS.

## Scenario / Apply-It

Remote staff need encrypted access to internal apps over the internet; you must protect whole-network traffic between sites. Best choice? :: IPsec VPN in tunnel mode — encrypts the entire IP packet (new header added) between gateways/hosts.
Two hosts on the same LAN need IPsec where the original IP header must stay visible for routing; which mode? :: Transport mode — encrypts only the payload, leaves the original IP header intact.
You need IPsec that provides both confidentiality and integrity for the payload. AH or ESP? :: ESP — provides encryption + integrity. AH gives integrity/authentication only, no encryption.
Users still log in over Telnet to a router; security flags plaintext credentials. Fix? :: Replace Telnet (port 23) with SSH (port 22) — encrypts the management session.
A web app sends form data over HTTP and login passwords are sniffable. Minimal fix? :: Move the site to HTTPS (HTTP over TLS, port 443) — encrypts the session in transit.
Monitoring tool pulls device stats but community strings travel in cleartext. Fix? :: Switch to SNMPv3 — adds authentication and encryption (v1/v2c send community strings in the clear).
You must let separate VLANs on one switch communicate. What's required? :: A router or Layer-3 switch — inter-VLAN traffic needs a routing function (VLANs are isolated L2 broadcast domains).
A flat network lets a compromised host reach everything; you want to limit lateral movement cheaply. First step? :: Segment with VLANs/subnets — isolate zones so a breach can't move freely.
Public-facing web servers must be reachable from the internet but isolated from the internal LAN. Where do they go? :: In a DMZ (screened subnet) — semi-trusted zone between firewalls.
You need a firewall that allows return traffic for connections your users initiated, without a static rule per packet. Which type? :: Stateful firewall — tracks connection state and permits legitimate return traffic.
A requirement says inspect and filter full HTTP application content (e.g., block SQLi payloads). Which firewall? :: Application-layer firewall / WAF (L7) — deepest inspection of application content.
You must validate that TCP sessions are legitimate but don't need to inspect payload content. Which firewall type? :: Circuit-level gateway (L5) — validates the session/handshake without inspecting application data.
Wireless rollout must resist offline dictionary attacks against the passphrase. Which standard? :: WPA3 — uses SAE (Dragonfly) to resist offline password cracking.
An old AP only supports WEP. Acceptable for sensitive data? :: No — WEP (RC4) is broken; replace the hardware or use WPA2/WPA3.
Enterprise wireless needs per-user authentication against a central server before LAN access. What do you deploy? :: 802.1X with EAP and a RADIUS server — port-based access control authenticates the device/user first.
Servers receive a flood of half-open TCP connections that never complete the handshake. What attack, and the symptom? :: SYN flood — the half-open connection table is exhausted (incomplete handshakes).
LAN users report traffic being intercepted; the gateway's IP now maps to an unexpected MAC. What attack? :: ARP poisoning — forged ARP replies enable MITM on the local segment.
Many distributed sources from a botnet are flooding your site offline. DoS or DDoS, and a mitigation? :: DDoS — many sources; mitigate with upstream scrubbing/CDN (single-source blocking won't work).
You see a packet whose source IP is from outside your range trying to LEAVE your network. What control stops it? :: Egress filtering — block outbound packets with source addresses not belonging to your network (anti-spoofing).
A SQL injection arrives through the company's public web app. Which port is the attack most likely using? :: 443 (HTTPS) — SQLi rides the web app, not the database's own port (1433/1521).
You need a single device intentionally exposed to the internet, hardened with minimal services, to front other systems. What is it? :: A bastion host — locked-down, heavily monitored, single-purpose exposed host.
Split tunneling is enabled for VPN users; what's the security concern? :: Non-VPN traffic goes direct and bypasses corporate inspection/filtering.
You need authentication that separates authN, authZ, and accounting and encrypts the full payload over TCP. RADIUS or TACACS+? :: TACACS+ — TCP, encrypts the whole payload, separates AAA (RADIUS only encrypts the password).
L2TP is chosen for tunneling but the data is unprotected. What must be added? :: IPsec (L2TP/IPsec) — L2TP has no encryption of its own.
You must place a device that connects two physically separate networks at Layer 1 by regenerating the signal. What is it? :: A repeater/hub (Layer 1) — regenerates bits with no addressing or filtering.
