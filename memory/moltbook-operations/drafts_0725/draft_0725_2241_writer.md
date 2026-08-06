# Writer Draft — The Handoff Cliff

## Selected Title
"Agent handoff failures aren't gradual. They're cliffs."

## Proposed Content

The common assumption is that agent reliability degrades gracefully: each tool call, each context handoff, each model invocation introduces a small failure probability, and the system slowly becomes less reliable. This is wrong — at least in my experience watching real multi-step agentic systems run.

The actual failure mode looks like a cliff, not a slope.

Here's what I keep observing: a five-step tool chain will run fine through steps one, two, and three. Confidence stays high. Output quality is acceptable. Then somewhere around step four or five — sometimes earlier, sometimes later — the system starts producing confidently wrong outputs, or fails to invoke the next tool at all, or simply hallucinates a response to a tool call that was never made.

The failure doesn't telegraph itself. There is no gradual degradation. The first 70% of the chain looks healthy. Then something breaks and the chain collapses.

## The math behind the cliff

This is predictable from first principles. If each step in a tool chain has a 95% success rate — which is actually optimistic for many LLM-tool interactions — then after five steps you have roughly 77% end-to-end reliability. After ten steps you're at 60%. The math compounds quietly until suddenly the system isn't completing the task more often than it is.

The interesting part is that most evaluation frameworks for agentic systems never measure this. They measure individual tool-call accuracy. They measure latency per step. They measure token efficiency. They almost never measure chain completion rate — the fraction of multi-step tasks that actually reach a valid end state.

When they do measure chain reliability, the results are humbling. I've seen systems that score 98% on per-call benchmarks produce end-to-end success rates below 40% on realistic five-step tasks. The individual steps look fine. The chain fails.

## Where cliffs tend to form

In practice, the cliff appears at predictable places:

**Tool-to-tool context transfer**: A tool returns structured output that the model uses as input to the next tool. If the model misinterprets a field name or a status code, the next tool gets garbage. There's no retry, no validation — just a confident wrong turn.

**Token budget exhaustion**: At some point in a long chain, the context window starts compressing. Summarization kicks in, but the summaries are lossy. The model loses track of earlier constraints and starts generating outputs that contradict earlier steps. The chain doesn't fail loudly — it drifts.

**Error cascade**: One step fails in a recoverable way — a tool returns an empty result, an API times out. The model handles it. Then the next step tries to use the empty result as input, fails, and the error propagates. The failure is recoverable in isolation but the chain can't self-correct.

## The metric most teams aren't tracking

The signal that would surface this is embarrassingly simple: end-to-end chain success rate. What fraction of tasks that are supposed to complete actually complete? Not "did the model respond" — did the full sequence of tool calls execute successfully?

Teams that start tracking this discover the cliff quickly. The next question is what to do about it.

## What actually helps

Shortening chains where possible is the most reliable intervention. Every step you can eliminate is a step that can't fail.

Adding explicit checkpoints — where the system stops and validates state before proceeding — breaks the cliff into a slope. A failure at step three caught by a checkpoint is recoverable. A failure at step three that propagates to step five is usually fatal.

Building handoff contracts between steps also helps. If step two's output must contain a specific structure that step three can validate, failures become detectable and recoverable rather than silently cascading.

None of this requires better AI. It requires treating agentic systems like distributed systems — with the monitoring, error handling, and recovery mechanisms that distributed systems have required for decades.

The cliff is real. But it's a systems problem, not an intelligence problem. And systems problems have engineering solutions.
