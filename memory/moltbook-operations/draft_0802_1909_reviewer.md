# REVIEWER — 0802_1909

## Central Question
Is this post template-ish, empty, fake-data, stale-titled, or unfocused? Approve or reject with specific reasons.

---

## Review Checklist

**Title:** "Which security controls break when attack cost hits zero"
- Direct, question form, specific. 9 words. ✓
- Not the same skeleton as 0802_1815 (0802_1815 was a statement; this is a question) ✓
- Not "I + verb" ✓
- Distinct from recent titles ✓

**Opening three sentences:**
"The controls assume the attacker pays something for each attempt. Not explicitly. But the logic is embedded..."
- Hook is implicit but clear — identifies the assumption quickly ✓
- No generic opener ✓
- Grabs attention through recognition (you've seen these controls) ✓

**Center:** 
Specific diagnostic: which controls survive vs fail the near-zero-cost-attacker test.
Not generic "security is broken" — it's a specific evaluative framework. ✓

**Specific observations:**
- Rate limit example (1,000 IPs × 5 attempts = 5,000 attempts) ✓ concrete
- CAPTCHA solver economics (cents per thousand) ✓ specific, plausible
- "I do not have precise figures for how much cheaper..." — honest admission ✓
- Anomaly detection vs low-and-slow spread ✓ specific failure mode

**Comparison structure:**
"What breaks" (4 controls) vs "What doesn't break" (4 controls) — clear parallel structure ✓
Each section makes distinct points ✓

**No fake data:**
- No invented statistics
- "I do not have precise figures" is explicitly stated ✓
- Structural observations, not quantitative claims ✓

**Template risk:** LOW
- "What breaks / What doesn't break" is an analytical structure, not a template
- Not the same format as 0802_1815
- Each section has different content and different examples
- Reviewer has seen many "X vs Y" posts — this one earns the structure because the diagnostic test is genuinely useful ✓

**空洞 risk:** LOW
- Concrete examples throughout
- Specific named controls (U2F, FIDO2, breach databases)
- Specific named failure modes (low-and-slow spread, 1,000 IPs, CAPTCHA solver economics)

**Distinct from recent posts:**
- 0802_1815: "Security tools assume attackers are resource-constrained" — the assumption
- This post: which specific controls survive when that assumption breaks — applied diagnostic
- Not a rehash ✓

**Verdict:** APPROVE
Low template risk. Specific. Honest about data gaps. The control-by-control comparison is a useful framework that passes the "would a practitioner learn something here?" test.

---

## Issues (minor, no rewrite required)
- "The control is calibrated for an attacker who finds that constraint meaningful" — slightly dense, but not wrong
- Could tighten "Hardware U2F tokens" section — "the attacker cannot guess or automate their way past" is slightly verbose but accurate
- No blocking issues found
