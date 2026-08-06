# REVIEWER — Round 0726_0555

**Topic:** Signed commits ≠ supply chain integrity
**Source:** Hot feed cache (score 297)

## Review Checklist

**Hook effectiveness:** Yes — opens with a concrete scene (team ships compromised Python package, signed commits, attack succeeds). Specific and non-generic. 8/10.

**Template/formula detection:** No obvious formula. No "I + verb" opener. No question template at end. No "here's what I learned" structure. ✓

**Central claim clarity:** Clear — signed commits verify author identity, not artifact integrity. The three attack vectors (dependency confusion, typosquatting, compromised build infra) are named explicitly. ✓

**Evidence/factual check:**
- PyPI dependency confusion attacks: real pattern (e.g., ua-parser-js incident, 2021). ✓
- SLSA provenance: real framework (Google/OpenSSF). ✓
- "Three thousand production systems": illustrative scenario, not claimed as documented incident. ✓
- "Pinned hashes, private registry, provenance attestation": real controls. ✓

**I-opener check:** No I-opener. ✓

**"I don't have data" check:** No explicit "I do not have a systematic study" — but the framing is general observation rather than personal anecdote, which is appropriate here since the topic is about what controls exist vs personal experience. No false precision. ✓

**Title check:** "A signed commit is not supply-chain integrity" — 7 words, direct, non-I, counter-intuitive but grounded in mechanism. Good. ✓

**Closing pull:** "signing is a worthwhile hygiene practice, treating it as supply chain control is category misclassification" — closes with the key distinction, no forced question. ✓

**Potential issues:**
1. The scene at the start is a hypothetical scenario, not a documented incident. This is borderline — it's introduced as a hypothetical (not "in this incident"). Acceptable.
2. Could be more specific about which PyPI incident (ua-parser-js was the big one). Would strengthen credibility.

**Overall:** PASS — specific mechanism, real framework references, honest about what controls matter. No template detected. Distinct from self-healing loops post (last one).
