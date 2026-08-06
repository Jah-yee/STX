# REVIEWER Notes — Round 0421 UTC
# Title: Browser agents don't read pages. They read your edited version of the page.

## Review Checklist

**Templated / repetitive?** NO — structure is original (anti-intuition declaration + mechanism + tooling audit question), not matching any recent title skeleton. Not an I-opening. Not a question. Not a failure comparison.

**Hollow / no real content?** NO — mechanism is specific: Servo June 30 update (--userscripts=, --host-file=), structural distinction from prompt injection, tooling layer audit question. No vague claims.

**Fake data?** NO — no fabricated numbers. No specific statistics without sourcing. "I do not have data on how many production agentic browsers run with some form of document mutation layer" is an honest admission, not a dodge.

**Title stale?** NO — distinct from all recent titles. Different topic, different mechanism, different framing.

**Center clear?** YES — the semantic proxy bug is structurally distinct from prompt injection; the tooling layer is the attack surface; the question to ask is about document mutability, not prompt security.

## ISSUE: Word count
Draft is ~390 words. Guideline is 700-1400 words. Need to expand middle sections.

## ISSUE: Ending
Ending "If the answer involves a shim..." is a bit abrupt. Tighten and strengthen.

## Verdict: REVISE (expand + tighten ending)
Do not rewrite from scratch. Expand these sections:
1. What the mechanism looks like in practice (one concrete scenario)
2. Why the prompt injection framing is a category error (deeper distinction)
3. The tooling ecosystem context (why this is common in production stacks)
4. Tighten ending to have more discussion pull
