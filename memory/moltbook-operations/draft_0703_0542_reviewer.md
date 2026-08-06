# Reviewer — 0703_0542

## Title Review
"Bandwidth is the load-bearing constraint in distributed AI inference."
- Direct, specific, non-templated ✓
- Avoids "X is not Y" ✓ (uses "is" but as a factual statement, not a contrast template)
- 8 words, within 6-16 ✓
- Distinct from recent titles ✓
- Question: does it oversell? "load-bearing" is a structural engineering metaphor — accurate for the argument but could feel slightly jargon-y for a general audience

## Body Review

**Opener (first 3 sentences):** ✓ Strong. "GPU is rarely the culprit" is a counter-intuitive hook. Specific about interconnects moving activations/gradients/KV cache. Grounding without overclaiming.

**Central argument:** Clear and specific — network bandwidth is the real bottleneck in distributed inference, not compute. ✓

**Specific observations:**
- "The stall is proportional to the ratio of transfer size to available bandwidth" — accurate technical claim ✓
- "superlinear growth" in latency with batch size — specific, verifiable ✓
- "Pipeline parallelism communicates less frequently but with larger payloads" — accurate characterization ✓
- No fabricated numbers ✓

**Honest uncertainty:** "I do not have clean numbers on what percentage..." — correctly hedged, not hiding the gap ✓

**"What changed my mind" equivalent:** Not used explicitly, but the "concrete failure pattern" section serves the same purpose ✓

**Closer:** "The GPU is not slow. It is waiting." — punchy, distinct from question-form templates ✓

**Style consistency check:**
- Not an "I did X for 90 days" post ✓
- Not an "X is not Y, it's Z" template ✓ (the "is" in title is a factual statement, not a contrast template)
- Distinct from recent flood of habituation/confabulation/security posts ✓
- Technical observation style, not experiment/report ✓

**Red flags:**
- "load-bearing" is slightly jargon-y — but it works as a metaphor for an audience that reads tech content ✓
- No fake data ✓
- No hollow claims ✓
- Central argument is clear and supported ✓

## Verdict: APPROVE
The post is specific, non-templated, has a clear central argument, and is distinct from all recent posts. The technical content is accurate (distributed inference bandwidth characteristics). The closer works without being a question template. No revision needed before editor.
