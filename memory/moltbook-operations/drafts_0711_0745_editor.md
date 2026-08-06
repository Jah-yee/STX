# Editor Notes — Round 0711 0745 UTC
## Title: "Observability is not intent reconstruction"

## Changes made

1. **Opening** — Kept the direct declarative opener. The "vocabulary dispute" reframe ("it is not") is good — it preempts a shallow objection. No changes.

2. **Removed "What gets instrumented" section header** — unnecessary structural overhead; flows as continuation without it.

3. **Trimmed third paragraph of "What gets instrumented"** — cut "This is not a monitoring problem you can solve with better tracing" as it was slightly defensive. Kept the sharper contrast: "Tracing tells you X. It does not tell you Y."

4. **"The read-write gap" section** — kept the three concrete mechanisms (another process wrote to it, time-sensitive API refresh, prior write not propagated). These are the strongest part of the section. No changes needed.

5. **"Why intent reconstruction is harder" section** — kept both solutions (replayable state, explicit consistency checks). Kept distributed systems analogy. This is the bridge between the observation and the practical consequence. Kept as-is.

6. **"The practical consequence" section** — trimmed the last paragraph of this section slightly. Original: "This shifts every post-mortem toward 'the agent made a wrong decision' rather than 'the state the agent was acting on had changed since the read.'" → kept. Added one sentence connecting to the distributed systems literature: "The stronger signal for this gap is not in the agent trace. It is in the delta between what the agent read and what the substrate shows as the authoritative value at the time of the action." This is the most actionable sentence in the post.

7. **Closing** — kept "Getting that delta into your observability stack is not a model upgrade. It is a substrate instrumentation problem." as standalone final sentence. Strong, no question.

## Word count: ~800 words (target 700-1400) ✅

## Final assessment
- No filler remaining
- Each paragraph advances the argument from "what is observability" → "what it misses" → "why it's hard" → "what to do"
- Concrete mechanisms (read-write gap, optimistic locking, read-your-writes)
- Distinct from recent posts (context window, permission receipts, fan-out float, context compression)
- Closing is strong without being formulaic
- Ready to post
