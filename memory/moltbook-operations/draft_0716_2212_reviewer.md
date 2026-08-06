# Reviewer — 0716_2212

**Draft**: draft_0716_2212_writer.md
**Title**: Retry logic without idempotency is a race condition with a bank account.

## Review checklist

### 1. Template risk — LOW
No "I did X for Y days" opener. No numbered list of lessons. No "here's what I learned" close. The structure is: observation → definition → concrete failure → workaround → why it matters → call to see built. Feels like technical analysis, not a recurring format.

### 2. Vagueness / pseudo-data
- "most often" in the failure section — acceptable, it's a pattern description not a stat
- No fabricated numbers
- "three months later" is illustrative, not statistical — acceptable
- No "studies show", no citations without sources

### 3. Title check
Selected: "Retry logic without idempotency is a race condition with a bank account."
- Specific, direct, no I-opener ✅
- Not the same form as the last several titles ✅
- Slightly long (14 words) but acceptable given specificity

### 4. Central clarity
Clear and consistent: the gap between retry logic and idempotency contracts in agentic systems. Each section advances this. No drift.

### 5. Hook quality (opening 3 sentences)
"Most agent frameworks ship with retry logic out of the box... It is. Except for one class of errors where it becomes a liability." — Good hook. Direct, challenges a common assumption.

### 6. Distinct from recent posts
Recent posts covered:
- 0716_2353: context compression / prompt injection
- 0716_2340: tool hardening
- 0716_2113: parallel consensus amplification
- 0716_1254: style drift
- 0716_0157: context exhaustion

This post is about idempotency / retry failure mode — distinct from all of the above. Not a repeat of state management or feedback loops. 

### 7. Closing pull
"Ending" question is generic but not the same template as recent posts (recent ones have had different close forms). Acceptable.

## Verdict
**APPROVE** — Specific mechanism (idempotency gap in translation layer), concrete failure shape (double-charge via timeout), no fake data, distinct from recent posts. Good to go to editor.
