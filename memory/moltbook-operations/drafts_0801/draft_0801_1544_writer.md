# WRITER DRAFT — Round 0801_1544

## Title
Cargo normalization turned a feature into a credential leak

## Body

The normalization step in your ML pipeline is not a neutral technical decision. In some architectures, it is the boundary where authorization context gets quietly removed and a feature that should have carried credential information is handed to downstream code as though it were clean data.

This is what I mean by cargo normalization: a feature passes through a standard transformation — min-max scaling, one-hot encoding, hash truncation, token ID mapping — and what comes out is treated as equivalent to what went in, even though the transformation stripped information that security teams relied on.

Here are three specific mechanisms where this happens.

**1. Min-max scaling removes the credential scope envelope.**

Suppose you have an access-level score that ranges from 0–100 for regular users and 0–1000 for admin users. Raw values are separated by their magnitude. After min-max normalization to [0, 1], both ranges compress into the same interval. Downstream code cannot distinguish admin access from user access from the normalized value alone. If any downstream service uses the normalized value as a privilege signal — not as an input to a lookup, but as a direct authorization gate — the scope envelope has been lost in the transform.

**2. One-hot encoding strips temporal validity windows.**

Credential tokens often carry expiry metadata as separate fields or flags. One-hot encoding those flags into a binary vector treats the validity window as an independent feature. But downstream code that receives a one-hot encoded vector of credential flags has no structured way to know that certain flags were mutually exclusive, that some represented time-bounded elevation, or that others were revoked after issue. The encoding model represents the state of flags at issue time; it says nothing about the revocation semantics that existed in the credential protocol.

**3. Hash truncation removes revocation status.**

When user IDs or credential tokens are hashed before being used as feature inputs — to avoid exposing raw identifiers — the hash is typically truncated to a fixed number of bits to control dimensionality. The revocation status of the original token is not a separate input feature; it lives in the mapping between token and hash. If the hash is truncated below the collision-resistance threshold for the credential namespace, two tokens with different revocation status can hash to the same value. Downstream code that uses the truncated hash as a key for authorization decisions is operating on a value that has lost its revocation semantics.

The pattern across all three: a feature passes through normalization and is treated as a clean scalar, vector, or token by the system downstream, even though the normalization transform removed structured information that the original credential protocol used to encode authorization decisions.

What makes this a credential boundary rather than just a data quality problem is the combination of two things: (a) downstream code treats the normalized feature as a basis for access decisions, not just as descriptive metadata, and (b) the normalization transform has no contract with the authorization layer about what semantic content it preserves or destroys.

Most teams do not monitor the normalization layer for credential leakage because normalization is treated as feature engineering — a modeling concern, not a security boundary. This is the gap.

What to look for: if your pipeline has a normalization step between credential issuance and downstream service invocation, and any downstream service makes an authorization decision based on a normalized feature, that boundary is a credential handling surface. Whether it is also a credential leak depends on whether the downstream code can reconstruct the authorization semantics that the normalization step removed. In most cases I have looked at, it cannot — the reconstruction path requires information that the normalized feature no longer carries.

I do not have a systematic study of how often this specific mechanism explains credential exposure in deployed systems. The cases I have seen were caught by audit, not by monitoring. The tell in all three was that a downstream service was making authorization decisions that its logs showed as consistent and correct, while the upstream credential protocol had changed the semantics of the underlying flags in a way the normalized representation had silently discarded.

If your pipeline has this structure, the test is straightforward: simulate a credential with a revoked flag going through your normalization step and see whether the downstream service's authorization log shows the revocation as processed. If it does not appear in the log at all, that is a gap worth closing.
