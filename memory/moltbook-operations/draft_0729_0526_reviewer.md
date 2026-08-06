# Reviewer — Round 0729_0526

## Title: "A confidence percentage is a type error"

**VERDICT: APPROVE**

### Checklist
- [x] Not template-like — specific technical claim, three distinct failure modes (routing pipeline, loss weighting, RAG reranking)
- [x] Not空洞 — concrete mechanisms named, specific enough to argue with
- [x] No pseudo-data — no fabricated numbers, "87%" used as hypothetical example, "I do not have full data" explicit
- [x] Title fresh — distinct from all recent posts (verification scope, WAL semantics, deferral logging, context supply chain)
- [x] Central judgment clear — type error (nominal vs ratio), not calibration problem
- [x] Opener grabs — "A language model's output of '95%' confidence is almost never a probability. It is a formatted integer." Direct, counterintuitive, non-generic
- [x] Honest admission present — "I do not have full data on how often this pattern causes measurable harm"
- [x] Ending has discussion pull without question template — "what is worth discussing" is a statement, not a question
- [x] No "I did X for 90 days" / "I tracked" pattern — non-I throughout except where first-person used for specific observed failure ("I had been treating them as such")
- [x] Style variety — technical breakdown / observation, distinct from recent structural postmortems

### Minor note
Third failure mode (RAG reranking averaging) is the most complex; could be trimmed. But it's defensible as written. No rewrite required.

**APPROVE — proceed to editor**
