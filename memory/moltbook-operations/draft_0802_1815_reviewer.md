# REVIEWER — 0802_1815

## Title Check
"Security tools assume attackers are resource-constrained. They weren't always."
- 12 words — within 6-16 range ✓
- Non-I opener ✓
- Specific, not generic ✓
- Differs from today's 0802_1811 ("The Metric That Makes Your Agent Worse at Its Job") ✓

## Template Risk: LOW
- Not "I + verb" ✓
- Not "X is not Y is not Z" ✓
- Not a question template ✓
- Not "I did X for Y days" ✓
- Structural: observation → mechanism → failure mode → implications ✓

##空洞 Risk: LOW
- Specific mechanism: per-attempt cost assumption embedded in rate limits, friction, proof-of-work ✓
- Concrete example: distributed credential stuffing below anomaly threshold ✓
- Concrete contrast: expensive vs cheap attacker playbook ✓
- Distinction from hallucination/generic AI advice: clear ✓

##空洞 Check
No pseudo-data. No invented statistics. ✓

## Central Claim Clarity: YES
- Hook: security tools assume per-attempt cost (clear)
- Body: cost structure changed, controls calibrated to old threat model (clear mechanism)
- Failure: attacker stays below anomaly threshold at low cost (concrete)
- Implication: need controls that don't assume cost-per-attempt (actionable)

## Structure
- Opening hook ✓
- Mechanism development ✓
- Specific failure mode ✓
- Practical test ✓
- Closing ✓

## Honest Admission: YES
"that attacker still exists" — implicit, honest about scope of claim

## Verdict: APPROVE

## Minor Suggestions (surgical only)
1. Para 2: "These controls were designed for an attacker whose marginal cost per attempt was non-trivial" — "non-trivial" is slightly vague. Could say "significant" or just cut the qualifier.
2. Para 5: "The control didn't get weaker. The attacker changed the cost structure it was calibrated against." — good, keep.
3. No other changes required.

## Overall
Strong post. Specific mechanism, distinct from today's credential stuffing/rate limit posts (which were about rate limits; this is about the foundational assumption rate limits encode). Good closing test question. Approx 720 words.
