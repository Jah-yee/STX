# EDITOR — Round 0735

## Changes (surgical, 3 total)

1. **Opening**: "Both are wrong" → "Both miss the point" — sharper, more specific
2. **Ambiguity failures para**: "use your best judgment" — add quotes correctly; tighten "A prompt that says 'if confidence below X, re-query with Y context' does" — remove trailing "does" (dangling)
3. **Closing para**: Remove "The retry graph is the architecture. The prompt is just the instruction set for the path that's currently active." — this line is good but slightly abstract for a closing beat; replace with the more direct: "The retry graph is the architecture. The prompt is just the guide for the path that worked the last time."

---

## Final Version

---

When an agentic system fails in production, the first instinct is to rewrite the prompt. The second instinct is to try a better model. Both miss the point.

The more useful question is: what happens after the failure?

Not whether the failure occurred — all systems fail. But what the system does when it does. That decision tree — that graph of retry paths and fallback behaviors — is the actual differentiator between reliable agentic systems and fragile ones. And it has almost nothing to do with prompt quality.

## The prompt ceiling

Prompts govern what the model does when things go right. They define the happy path. You can write the most precise, well-structured, few-shot-enhanced prompt in existence, and it will not help you when the API returns a 429, when the output schema changes mid-run, when the tool returns an empty result and the model has no instruction for that state.

Prompts are a single-threaded instruction set. They assume the world cooperates. Production does not cooperate.

What actually determines whether the system recovers — whether it retries with backoff, whether it re-asks with reformulated context, whether it falls back to a cached result or escalates to a human — is the retry topology. The graph of paths that exist beyond the happy path.

## Three failure types, three topologies

The retry structures that work depend on what kind of failure you're handling.

**Transient failures** (network timeout, rate limit, service unavailable) respond well to exponential backoff with jitter. The failure isn't about the task — it's about the channel. Retry with delay and you often succeed. A well-structured prompt does nothing for this. The infrastructure does everything.

**State-dependent failures** (tool returned unexpected output, schema mismatch, partial result) require idempotency-aware retry: you need to know what state you're in before retrying, otherwise you compound the error. This is a pipeline design problem. Prompts cannot fix it because the failure happens before the model even processes the output.

**Ambiguity failures** (model output is plausible but wrong, or model asks for confirmation when it should have proceeded) are the most interesting. These are the failures where better prompting actually helps — but only if the prompt explicitly defines the ambiguity resolution policy. A prompt that says "use your best judgment" creates no retry path. A prompt that says "if confidence below X, re-query with Y context" actually does.

## What reliability testing actually measures

Standard agentic benchmarks measure prompt quality. They measure whether a model follows instructions, whether it produces correct outputs, whether it handles edge cases in the prompt. These are all tests of the happy path.

What they don't measure is what the system does when the model produces a confident wrong answer — whether there's a verification loop, a human-in-the-loop checkpoint, or a self-correction path that doesn't require restarting the entire task.

I have not run a controlled study on this. But the pattern is consistent enough across the systems I've observed: teams that achieve reliable agentic behavior invest heavily in retry topology, not prompt engineering. They build explicit state machines for failure recovery. They define idempotency keys. They instrument timeout and fallback paths. They treat the failure graph as a first-class engineering artifact.

Teams that don't achieve reliable behavior tend to iterate on prompts. They add more examples to the few-shot. They rewrite the system instruction. They try a larger model. And the reliability numbers barely move.

## The prompt is not the architecture

Reliable agentic systems are built from the outside in: first you define the failure modes, then you design the retry topology for each, then you write the prompts to guide the model through the paths you've built.

Unreliable systems are built from the inside out: write the prompt, ship it, then debug whatever breaks.

The retry graph is the architecture. The prompt is just the guide for the path that worked the last time.

When your agent fails, ask what the retry path was. If the answer is "it didn't have one," you know where the problem lives.
