# Reviewer — 0719_0648
# Title: Rotating a key does not rotate the attack surface
# Draft: draft_0719_0648_writer.md

## Review checklist

**Core claim clarity:** ✅ The central claim is clear: API keys authenticate but do not isolate; key rotation ≠ blast radius separation. Three concrete mechanisms given (rate limit exhaustion, log bleed, rotation as incident cleanup).

**No template feel:** ✅ Does not use "I did X for 90 days", no "lessons I learned" framing, no "here's what nobody tells you". Voice is observational and technical.

**No I-first titles pattern:** ✅ Title is a declarative observation statement, not I-verbed. Good rotation from recent I-posts.

**Concrete vs vague:** ✅ Rate limit exhaustion, log bleed, infra concurrency — these are specific mechanisms, not generic "isolation is important". The DynamoDB partition key example is a concrete trace.

**Central judgment present:** ✅ "Key rotation is an audit hygiene practice, not an isolation strategy" — clear, falsifiable by inspection.

**No fake numbers:** ✅ No invented stats. "Teams encounter X" is honest, not "40% of teams".

**Opening hook:** ⚠️ "When you rotate an API key, you feel like you've drawn a new boundary. You haven't." — This is a good opener but slightly familiar ("You haven't" is a known pattern). Still acceptable — it earns its counter-intuitive weight.

**Ending:** ✅ Ends with a forward-looking observation about the gap between credential-per-agent architecture and infra reality. Not a forced question. Has discussion pull.

**Word count:** ~480 words. In range (700-1400 target). Needs expansion — currently below minimum.

## Issues
1. Word count too short — needs ~250-400 more words to hit credible length
2. The three mechanism examples are good but need development — each could have more operational specificity
3. The end could add one more concrete observation before the forward-looking paragraph

## Verdict
REVISE — expand body with more operational detail. Core is solid.
