# Symmetric Encryption - Detail

## Overview

One shared key for both encryption and decryption. Fast, but requires a pre-shared key and doesn't scale for many users.

### Key Math
Number of keys for n users: `n(n-1)/2` (symmetric) vs. `2n` (asymmetric).

## Cryptographic Properties We Want
- **Confusion** — relationship between plaintext and ciphertext is as random as possible
- **Diffusion** — plaintext is spread throughout ciphertext
- **Substitution** — replace characters (provides confusion)
- **Permutation / Transposition** — rearrange characters (provides diffusion)

## DES - Data Encryption Standard (broken)

- Algorithm is DEA (Data Encryption Algorithm); standard is DES
- Symmetric, **64-bit block cipher**, 56-bit key, 16 rounds, Feistel cipher
- No longer secure

### DES Modes

| Mode | Uses IV | Chaining | Notes |
|------|---------|----------|-------|
| **ECB** (Electronic Codebook) | No | No | Same plaintext → same ciphertext (weak) |
| **CBC** (Cipher Block Chaining) | Yes | Yes (XOR with prev block) | Errors propagate |
| **CFB** (Cipher Feedback) | Yes | Yes (stream) | Stream version of CBC; errors propagate |
| **OFB** (Output Feedback) | Yes | Uses sub-key (not previous ciphertext) | Errors don't propagate |
| **CTR** (Counter) | Yes | Predictable feedback (counter) | Parallelizable |

## 3DES (Triple DES)

Encrypt with DES three times, with three modes:

| Mode | Keys | Effective strength | Status |
|------|------|-------------------|--------|
| **K1** | 3 unique keys | 112 bits | Still secure (until 2030) |
| **K2** | 2 unique keys | 80 bits | Not secure |
| **K3** | 1 key (same 3×) | Equivalent to DES | Not secure |

## IDEA - International Data Encryption Algorithm
- Symmetric, 128-bit key, 64-bit block
- Still considered secure; **older** algorithm
- Used in **early PGP**
- **Patented** → pay to use → not widely adopted

## AES - Advanced Encryption Standard (Rijndael)

Won the AES competition. Now the dominant symmetric cipher because it's **open source, fast, and secure**.

The **5 AES-competition finalists** (all considered secure): **MARS, RC6, Rijndael (WINNER → AES), Serpent, Twofish**. Exam tip: don't flag an unfamiliar-but-modern finalist (e.g., RC6) as "discontinue" just because you haven't heard of it — discontinue the *old/short-key* ones (DES, 3DES, RC4, SKIPJACK).

- **Symmetric block cipher**, **128-bit block size**, key sizes **128 / 192 / 256 bits**; based on **Rijndael**.
- The **global symmetric standard** — replaced DES/3DES.
- Used for data **at rest AND in transit** (e.g., disk/file encryption, plus the bulk-encryption cipher inside [TLS](MAC%20HMAC%20SSL%20and%20TLS.md) — see hybrid crypto).
- **No practical break** exists.

### How AES Works (high-level)

Operates on a 4×4 matrix of bytes, through multiple rounds:
1. **Initial round** — AddRoundKey (XOR bytes with round-key bytes)
2. **Main rounds** (repeat):
   - **SubBytes** — each byte replaced via lookup table
   - **ShiftRows** — rows shifted left by 0/1/2/3 positions
   - **MixColumns** — columns XOR-mixed
   - **AddRoundKey**
3. **Final round** — SubBytes, ShiftRows, AddRoundKey (no MixColumns)

### Round Counts by Key Size
| Key size | Rounds |
|----------|--------|
| 128-bit | 10 |
| 192-bit | 12 |
| 256-bit | 14 |

## Full-Disk Encryption Tools (use AES)

These are products, not ciphers — they apply **AES** to protect **data at rest**:
- **BitLocker** — Microsoft Windows full-disk encryption; AES, often bound to a **TPM** for key storage/integrity.
- **FileVault** — Apple macOS full-disk encryption; AES.

## Blowfish and Twofish

Both symmetric, public domain, Feistel-based.
- **Blowfish** — 64-bit blocks; original, now weak
- **Twofish** — 128-bit blocks, 128/192/256-bit keys; same designer's successor; AES finalist

## Serpent

- Symmetric block cipher; **128-bit block**, 128/192/256-bit keys.
- **AES-competition finalist** — runner-up to Rijndael. Considered **more conservative/secure** (more rounds) but **slower than AES**, which is why Rijndael won.

## RC4 / RC5 / RC6

- **RC4** — stream cipher; 40-2048-bit variable key; used in WEP, WPA, SSL, TLS (legacy). **Broken** — avoid.
- **RC5** — symmetric block; 32/64/128-bit blocks; 0-2040-bit keys; Feistel; still secure with large enough parameters
- **RC6** — AES finalist based on RC5; 128-bit blocks, 128/192/256-bit keys; secure but not widely used

## CAST

- **CAST-128 / CAST-256** — modern symmetric block ciphers; CAST-256 has a 256-bit key and was an AES candidate. **Considered secure** — keep, don't discontinue.

## The Feistel Cipher

Underlying structure of DES, Blowfish, Twofish, RC5, RC6.

1. Split the block into left and right halves
2. For each round:
   - XOR the left side with a sub-key
   - Swap left and right halves
3. Repeat with different sub-keys
4. Many rounds in practice

The right side never changes directly in a round (used in the XOR op but not modified). Decryption just reverses the key order.

## Exam Tips

- AES is the workhorse — open, fast, secure
- 3DES K1 (3 keys) is the only still-secure mode
- AES rounds: 10/12/14 for 128/192/256-bit keys
- RC4 is broken
- IDEA is secure but patented
- Feistel structure underpins many symmetric ciphers

## Related Topics

- [Cryptography](Cryptography.md)
- [Asymmetric Encryption Detail](Asymmetric%20Encryption%20Detail.md)
- [Hashing Detail](Hashing%20Detail.md)
- [Cryptographic Attacks](Cryptographic%20Attacks.md)
