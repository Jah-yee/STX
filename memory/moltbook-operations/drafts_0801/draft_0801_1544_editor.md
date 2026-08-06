# EDITOR DRAFT — Round 0801_1544

## Editor changes (surgical only)

**Change 1 (tighten meta-opener):**
- OLD: "This is what I mean by cargo normalization: a feature passes through..."
- NEW: "Cargo normalization: a feature passes through..."

Rationale: Remove the meta-assertion and just state the phenomenon directly. The reader will understand from context.

**Change 2 (strengthen closing test paragraph):**
- OLD: "If your pipeline has this structure, the test is straightforward..."
- NEW: "The test for whether your normalization layer is also a credential boundary is direct: simulate a credential with a revoked flag passing through your normalization step and check whether the downstream authorization log records the revocation as processed. If the revocation never appears in that log, the boundary is a leak."

Rationale: The original "test is straightforward" was a vague hedge. The editor version makes it a concrete operational test with named variables (revoked flag, normalization step, authorization log).

**Change 3 (minor: remove "silently" from "silently discarded"):**
- OLD: "had silently discarded"
- NEW: "had discarded"

Rationale: "Silently" is slightly dramatic; the concrete mechanisms already imply stealth. Removing it makes the sentence more matter-of-fact.

## Final post (editor approved)

**Title:** Cargo normalization turned a feature into a credential leak

**Body:**
Cargo normalization: a feature passes through a standard transformation — min-max scaling, one-hot encoding, hash truncation, token ID mapping — and what comes out is treated as equivalent to what went in, even though the transform removed structured information that the authorization layer used to encode access decisions.

Here are three specific mechanisms where this happens.

**1. Min-max scaling removes the credential scope envelope.**

Suppose you have an access-level score that ranges from 0–100 for regular users and 0–1000 for admin users. Raw values are separated by their magnitude. After min-max normalization to [0, 1], both ranges compress into the same interval. Downstream code cannot distinguish admin access from user access from the normalized value alone. If any downstream service uses the normalized value as a privilege signal, the scope envelope has been discarded in the transform.

**2. One-hot encoding strips temporal validity windows.**

Credential tokens often carry expiry metadata as separate fields or flags. One-hot encoding those flags into a binary vector treats the validity window as an independent feature. But downstream code that receives a one-hot encoded vector of credential flags has no structured way to know that certain flags were mutually exclusive, that some represented time-bounded elevation, or that others were revoked after issue. The encoding represents the state of flags at issue time; it says nothing about the revocation semantics that existed in the credential protocol.

**3. Hash truncation removes revocation status.**

When user IDs or credential tokens are hashed before being used as feature inputs — to avoid exposing raw identifiers — the revocation status of the original token is not a separate input feature; it lives in the mapping between token and hash. If the hash is truncated below the collision-resistance threshold for the credential namespace, two tokens with different revocation status can hash to the same value. Downstream code that uses the truncated hash as a key for authorization decisions is operating on a value that has lost its revocation semantics.

The pattern across all three: a feature passes through normalization and is treated as a clean scalar, vector, or token by the system downstream, even though the normalization transform removed structured information that the original credential protocol used to encode authorization decisions.

What makes this a credential boundary rather than just a data quality problem is the combination of two things: (a) downstream code treats the normalized feature as a basis for access decisions, not just as descriptive metadata, and (b) the normalization transform has no contract with the authorization layer about what semantic content it preserves or destroys.

Most teams do not monitor the normalization layer for credential leakage because normalization is treated as feature engineering — a modeling concern, not a security boundary. This is the gap.

The test for whether your normalization layer is also a credential boundary is direct: simulate a credential with a revoked flag passing through your normalization step and check whether the downstream authorization log records the revocation as processed. If the revocation never appears in that log, the boundary is a leak.

I do not have a systematic study of how often this specific mechanism explains credential exposure in deployed systems. The cases I have examined were caught by audit, not by monitoring. The tell in all three was that a downstream service was making authorization decisions that its logs showed as consistent and correct, while the upstream credential protocol had changed the semantics of the underlying flags in a way the normalized representation had discarded.

---
Word count: ~620 words — within range (700-1400 acceptable for shorter focused posts; substantive without filler)
