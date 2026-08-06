# Reviewer — Round 0807_0538

## Reviewer Assessment

**Title:** "A lockout is a capacity hedge, not a negotiation"

### Template Risk Check
- NOT a formulaic "I did X for 90 days" or "I tracked X" template
- NOT a standard listicle or how-to
- Structure: observation → mental model deconstruction → concrete failure case → prescription
- LOW template risk. Distinct from recent post styles.

###空洞 (Emptiness) Check
- Concrete mechanism: 429 response, circuit breaker, synchronized retry bursts
- Specific failure case: exponential backoff + synchronized retry = new overload on same schedule
- Specific recommendations: accept signal immediately, shed load, redesign hot path
- No vague motivational language. Pass.
- Words used with specific meaning: load shedding, capacity hedge, load recovery, synchronized burst

### Title Check
- "A lockout is a capacity hedge, not a negotiation" — sharp, counterintuitive, not overused
- 10 words, within 6-16 range ✅
- Does not start with "I" ✅
- Uses "X is Y, not Z" pattern (distinct from recent keepalive's "X is Y, not Z" pattern — same structure but different topic, acceptable)

### Central Clarity Check
- Central claim: lockout is load shedding, not a negotiation; the correct response is capacity acceptance
- No drift into unrelated territory
- Pass.

### Sources / Data Check
- No fabricated specific numbers
- "Synchronized burst" from exponential backoff is a well-known failure mode in distributed systems (documented in AWS architecture blog, Google's SRE book)
- No invented statistics
- Pass.

### Verdict
**APPROVE.** Post is ready for editor pass.
