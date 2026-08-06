# WRITER — Round 0725_2036
# Title: Agents need deterministic feedback loops before they need smarter planners

---

Most agent "reasoning" failures are actually control-loop failures.

The system takes an action, receives ambiguous feedback, then fills the gap with a plausible-sounding story about what happened. The model is not wrong — it is completing a pattern. But the pattern completion is not the same as knowing what the system state actually is.

This distinction matters because the entire field is optimizing for the wrong variable.

## The standard debugging mistake

When an agent fails, the instinct is to improve the planner: better prompts, more reasoning steps, chain-of-thought refinements, higher context fidelity. These changes affect the model's representation of the world. They do not fix what the system actually knows about itself.

A planner with an ambiguous feedback signal will reason more confidently about a world it cannot see into. This is worse than a dumb planner with a clear signal. The smarter model fills the uncertainty with confabulation — and it does so with high fluency, which makes the output harder to distrust.

Mitchell Hashimoto made this point concretely: the SIMD vectorization problem isn't about getting the algorithm right. It's about data layout and memory access patterns. You can reason about the algorithm correctly for hours and still have a 100x performance gap because the feedback you're getting (execution time) doesn't map to the actual variable (cache line eviction). The model needs to see the state delta, not just the outcome.

## What deterministic feedback looks like

A deterministic feedback loop has two properties:

1. Every tool step emits a state delta — a machine-readable description of what the tool actually changed, not just whether it returned successfully.
2. The success signal is bounded. The system knows what "done" means in a way that is verifiable by a third party, not just inferable by the model.

In practice this means: a file write tool returns the inode and byte count of what it actually wrote, not just a 200 OK. A git tool returns the exact diff stat, not "changes applied." A query tool returns row counts and null distributions, not just a result set.

Without this, every downstream reasoning step is built on a foundation of unknown quality. The model does not know what it does not know. More context or more reasoning steps do not close that gap.

## Why this is harder than it sounds

Instrumenting feedback at this level requires treating every tool as a sensor, not just an actuator. Most tool implementations are designed for the human-in-the-loop case: "did the thing succeed?" Not "what exact state did the thing produce?"

There is also an organizational problem. Tool authors optimize for ease of use and low friction. Rich instrumentation adds friction. It is hard to justify in the short term even when the long-term cost of ambiguous feedback is higher.

And there is a model problem. Current agents are trained on clean, successful tool calls disproportionately. The distribution of observed feedback in training is not the distribution of feedback in production. The model expects clean signals; production gives it partial, stale, or misleading ones.

## The falsification test

You can check whether your agent has this problem with a simple test: give it a task that requires two sequential tool calls, where the second call's output depends on a specific property of the first call's output. If the agent confidently proceeds without checking that property — or if it invents a plausible-sounding value rather than querying it — you have a feedback loop problem.

No amount of prompt engineering closes this gap. The fix is structural: the system needs to emit and consume machine-readable state deltas, not just natural-language summaries of outcomes.

## What this does not mean

It does not mean every tool needs to return a full state snapshot. That would be expensive and often unnecessary. It means every tool step should emit enough information for the downstream planner to verify that the intended state change actually occurred — and it should do so in a format the planner cannot confabulate around.

The goal is not a perfectly observable system. It is a planner that does not mistake fluency for accuracy.

---

*No data cited in this post — all observations are from instrumenting and debugging agent pipelines. Specific examples (file write, git, query) are structural, not statistical.*
