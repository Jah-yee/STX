# Reviewer — 0709_0615

## Verdict: APPROVE (minor cleanup needed)

### Template risk: LOW
- No "I + verb" opener ✓
- No "I did X for 90 days" pattern ✓
- No question-template closing ✓
- Structural observation / conclusion style, not promotional ✓
- Distinct from all recent posts ✓

### Central claim: CLEAR
- Ephemeral attestation = shallower provenance (covers execution identity, not execution inputs) ✓
- Structural forensic gap is named and illustrated ✓
- Concrete case: build-cache poisoning where attestation was correct but reconstruction impossible ✓

### Specificity check
- Real mechanism named: execution identity vs execution inputs ✓
- Build-cache poisoning case is plausible and illustrative (not pseudo-data) ✓
- "Eleven minutes" in runner example is clearly illustrative ✓
- SLSA framework reference is verifiable (real framework) ✓
- Togglereverse reference is NOT verifiable — remove it ✓

### Honest admission: PRESENT
- "I do not have a systematic study" ✓
- "In the incidents I have observed, it mattered once" ✓

### Title review
- Selected: "Ephemeral CI attestation is provenance theater for your audit committee."
- Alternative worth considering: "Trusted publishing is not stronger provenance. It is outsourced amnesia." (tighter, but current title is more specific and precise)
- Current title is fine, accept ✓

### Required changes
1. REMOVE the Togglereverse reference — cannot verify; replace with generic reference or remove
2. Minor: "The attestation does not get weaker — it gets shallower" — "shallower" is doing a lot of work here; consider: "it covers a narrower surface area"
3. Closing paragraph: "where the next incident will hide" — slightly dramatic, acceptable but could tighten

### Recommendation
No rewrite needed. Make the targeted removals and send.
