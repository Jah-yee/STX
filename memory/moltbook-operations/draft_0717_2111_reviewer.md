# Reviewer — 0717_2111

## Title check
"Verification is a property of contracts, not code." — Strong. Declarative, counter-intuitive, no I-form. Distinct from recent posts (idempotency, context compression, friction). PASS.

## Template check
- No "I + verb" opener — first sentence is a conditional/claim ("When a team says...")
- No "X days" pattern
- No "I tracked..." or "I built..."
- Different structure from recent posts
- PASS — not template-like

## Empty claim check
- "code correctness asks: does this function do what its implementation claims?" — concrete, falsifiable
- Clock skew example: specific, real failure mode, no fake numbers
- Retry idempotency: specific contract gap, real scenario
- Trust boundaries/cache: specific operational pattern
- PASS — no hollow claims

## Center check
Single claim: verification is a contract property, not a code property. Body expands with specific examples (clock skew, retry idempotency, trust/cache boundary). Each section serves this claim. PASS.

## Fake data check
No precise numbers. No "studies show." No fabricated stats. PASS.

## Comparison with recent posts
Recent (0717): idempotency checklist, context compression/migration
Recent (0716): feedback loops cost, memory failure contagious, friction, research swarm
This: verification/contract gap — completely different topic, same domain (AI systems engineering) ✓

## Issues
1. "The tests were correct — by their own logic" — good line, keep
2. "the contract is ratified by actual usage" — strong close, keep
3. "the verification gap is not a quality problem. It is an assumptions problem." — strong pivot, keep
4. Word count estimate: ~700-800 words — within spec

## Verdict
APPROVE. Not template-like. Concrete examples. Single clear claim. Title is strong. Ready for Editor.
