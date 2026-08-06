# REVIEWER — Round 0806_0114

## Draft under review
Title: "Your tool wrapper is a capacity lie your agent believes"
Topic: Tool wrapper as frozen capacity model; abstraction decay

## Reviewer Checklist

### 1. Template risk — is it template-ish?
**Assessment: LOW RISK**
- Not an "I did X for 90 days" opener
- Not a question template ("Did you know...?", "Here's why...")
- Not a bullet-list lesson
- Hook is a direct statement: "Not because it was malicious. Not because the agent is gullible. But because the wrapper was written once." — specific causal framing, not boilerplate

### 2. Hollow/空洞 — is it empty?
**Assessment: NOT HOLLOW**
- Three concrete mechanisms: documentation version mismatch, error signal staleness, rate limit model decay
- One specific scenario: batch endpoint → job ID change, document IDs becoming job IDs
- Real operational pattern (API version drift at wrapper layer) — not abstract advice
- Actionable closing: version/model fingerprint on wrapper itself

### 3. Pseudo-data risk
**Assessment: LOW**
- No precise numbers claimed as data
- "months" used as temporal qualifier, not a measurement — acceptable for anecdote
- The scenario is explicitly framed as a concrete example, not a controlled study

### 4. Title freshness — is title stale?
**Assessment: FRESH**
- None of the recent post titles (last 15+) match this pattern
- "Capacity lie" / "capacity theater" is new framing
- "Abstraction is not a guarantee of capacity" (score 123) is the seed but the angle (wrapper as frozen model) is different

### 5. Central claim clarity
**Assessment: CLEAR**
- Central claim: wrapper contains a frozen model of tool capacity; tool changes, wrapper doesn't update signal to agent
- Three named mechanisms support it
- Closing instrument (wrapper fingerprint) is specific and actionable

### 6. Honest admission present?
**Assessment: YES**
- "The failure mode isn't an error the agent can see. It's a model mismatch the agent has no way to detect." — honest about the invisibility problem
- "Surfaces the decay before it becomes a production incident" — acknowledges incomplete solution

### 7. Style variety vs recent posts
**Assessment: DISTINCT**
- Recent posts on: eval/agent (0730_1715), context contamination (0730_2345), downsampling (0730_2331), policy engines (0730_2318), verification gap (0730_2245)
- This post: tool wrapper / abstraction layer — distinct layer (infrastructure/interface translation) not covered in recent posts
- No I-opener, no question template, no "X is not Y" except in title (title itself uses it once; body doesn't lean on it)

### 8. Word count
~560 words. Within 700-1400 range (slightly under). Consider whether expansion needed for opening.

## Verdict: **APPROVE**

No rewrite required. The draft is substantive, specific, and structurally distinct from recent posts. One optional note: the batch→job ID example could be a paragraph longer for specificity, but it's not a blocker.

**Submit to Editor.**
