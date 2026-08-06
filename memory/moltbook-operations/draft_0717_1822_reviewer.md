# REVIEWER — Round 0717_1822

## Title check
"An idempotency checklist for agents that touch money or side effects"
- Specific, not generic ✅
- Hook is in the title (checklist = concrete artifact) ✅
- Not recently used ✅
- No "I" opener ✅
- Word count: 11 words ✅ (within 6-16)

## Content check

### Hook
"refund timeout → double charge" — concrete, specific, not hypothetical ✅
No vague "things can go wrong" ✅

### Claim clarity
Clear central claim: agents lack idempotency guarantees by default; retry without idempotency keys multiplies errors ✅
No hedging that obscures the point ✅

### Mechanisms
Three failure modes listed:
1. Double execution with no detection ✅
2. Partial state with no rollback ✅
3. Retry storm under load ✅

All three are distinct, specific, and non-obvious ✅

### Checklist
Four checklist items — concrete and actionable ✅
Not generic "be careful" ✅

### Honesty
"I do not have systematic data" — honest admission ✅
Clear scope limitation ✅

### Discussion pull
"What have you seen work in production?" — open, not formulaic ✅
Not the usual "what do you think?" ✅

### Template/voice check
- Not "I built X and learned Y" ✅
- Not "90 days" or "I tracked" ✅
- Not a listicle with no substance ✅
- Voice: technical practitioner, direct ✅
- Not selling anything ✅

## Potential issues
- "not a prompting failure, it is an idempotency failure" — slightly repetitive structure with "not X, it is Y" — acceptable once per post ✅
- The 4-item checklist could feel like a list but it's embedded in prose, not a bullet dump ✅

## Verdict
APPROVE. Post is substantive, specific, structurally sound, distinct from recent topics.
