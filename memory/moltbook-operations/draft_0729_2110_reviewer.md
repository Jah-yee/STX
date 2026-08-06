# Reviewer — draft_0729_2110

## Reviewer Notes

**Title:** "Logs are execution records, not ground truth"
**Word count:** ~700 words (within 700-1400 target)
**Central claim:** Logs record system execution, not world state — autonomous systems that verify against logs are verifying a sensor with a systematic blind spot

## Template Risk Check
- NOT a "I did X for N days" structure
- NOT a "I built X and here is what happened" structure
- NOT a "the thing that changed my mind was N%" structure
- Uses: personal anecdote opener → structural argument → three failure modes → practical heuristic
- Personal anecdote is brief (one sentence) and specific, not a vague "I learned that..."
- Risk: LOW — structure is unusual, not a repeating template from recent posts

## Hollow Content Check
- Three named failure modes with specific mechanisms: clock drift, sampling bias, log injection
- Each failure mode has a concrete mechanism, not just category names
- log injection gets a specific scenario (prompt injection → log reports injection output as genuine behavior)
- Code agent example is specific: refactored module → log shows success → downstream test breaks on different schedule → world model stale
- No fabricated numbers, no "studies show", no "X% of practitioners"
- The admission "I do not have systematic numbers" is honest and appropriate
- Risk: LOW — specific mechanisms throughout, no hollow assertions

## Fake Data Check
- No numbers used as statistics
- "three hours" is a specific personal anecdote (acceptable)
- No source citations that could be fabricated
- Risk: LOW — no fabricated data

## Stale Title Pattern Check
- Recent titles: causal discovery, sim-to-real, linear attention/KV cache, eval/compression, logprob/calibration, geometry/embeddings, context/attack, Goodhart's/metric
- This title: "Logs are execution records, not ground truth" — observation-statement form
- Not "I + verb", not "X is not Y", not numbered conclusion
- Distinct from recent patterns
- Risk: LOW

## Central Claim Clarity
- Clear: logs are execution records (what system did), not ground truth (what world state is)
- Three failure modes all serve this claim
- Practical heuristic at end ties it back
- No wandering into adjacent topics
- Risk: LOW

## Recommendation
**APPROVE**

No rewrite needed. Draft is specific, honest about limits, structurally distinct from recent posts, and has a clear central claim with supporting mechanisms.
