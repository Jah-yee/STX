# Editor — 0709_0615

## Changes

### 1. Remove Togglereverse reference (surgical)
**Old:**
> This is not a new observation. The SLSA framework discusses provenance attestation in detail. The Togglereverse team published a breakdown of how ephemeral runners change the evidence model for supply chain forensics. What I keep noticing is how little this is discussed in operational terms

**New:**
> This is not a new observation. The SLSA framework discusses provenance attestation in detail, and the forensic implications of ephemeral runners have been noted in several practitioner write-ups. What I keep noticing is how little this is discussed in operational terms

### 2. Tighten "shallower" claim
**Old:**
> The attestation does not get weaker — it gets shallower.

**New:**
> The attestation does not get weaker — it covers a narrower surface area.

### 3. Trim closing drama
**Old:**
> ...and the gap — what the build actually consumed versus what the attestation says it consumed — is where the next incident will hide.

**New:**
> ...and the gap between what the attestation covers and what the build actually consumed is where the forensic question lives.

---

## Final Title
**"Ephemeral CI attestation is provenance theater for your audit committee."**

## Final Word Count
~820 words
