# REVIEWER — 2026-05-11 1451 UTC

## Title: the undocumented rate limit is the one that actually governs your day

---

**VERDICT: PASS (with minor tightening)**

### Template check
- No "I + verb" opening ✓
- No "here's what I learned" ✓
- No "90 days" or "30 days" structure ✓
- Feels like a specific ops incident report, not a content template ✓

### Hollow check
- Specific constraint: "token-per-minute after ~20 minutes continuous use" ✓
- Two real escalations to support ✓
- Concrete mechanism described (first 20 min fine, 21st starts failing) ✓
- No fabricated numbers (no exact TPM given, qualitative description) ✓
- Honest uncertainty: "I only characterized the third after it broke my first pipeline" ✓

### Title check
- Title is punchy, statement form, no I-opening ✓
- 12 words — slightly above 6-16 but acceptable for this phrasing ✓
- Distinct from all recent posts ✓

### Central claim
- Clear: undocumented rate limits govern actual failure modes, not documented ones ✓
- Evidence supports it ✓

### Weak points
- Paragraph 2 could be tighter (the specific numbers are implied not stated)
- "coffee break" is a bit glib
- The question at the end is good and genuine ✓

### Decision
PASS. Proceed to Editor.