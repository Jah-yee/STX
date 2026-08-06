# Writer — 0728_0924

## Draft

**Title:** Infrastructure models are too slow for machine-speed agents

---

There is a gap in how agent frameworks are designed and how the underlying inference actually behaves. Agents are increasingly structured as rapid-cycling loops: observe, think, act, repeat. The mental model behind them treats inference as something that happens fast enough to not interrupt the loop. For most real deployments, this is not true.

The bottleneck is not context length. The bottleneck is decode latency.

A language model generates tokens sequentially. No matter how you slice it, producing N tokens requires N decode steps. A small 7B model generating 500 tokens of reasoning needs roughly 500 sequential decode steps. Even at aggressive speeds — 50 tokens per second — that's 10 seconds. A 70B model at 15 tokens per second needs 33 seconds for the same output.

Agents do not generate 500 tokens and stop. They generate 500 tokens, read the result, decide what to do next, and generate another chunk. A typical agentic pipeline for a moderate task — read a file, understand it, write a modification, verify the modification — might run 8 to 15 inference calls. At 10 seconds per call, you are at 80 to 150 seconds of cumulative inference time. The task itself might take a human 20 seconds.

This is not a frontier model problem. It affects all model sizes. Smaller models are faster but less capable; they make more mistakes, which means more retry loops, which adds inference calls rather than reducing them. Larger models are smarter per call but slower per call. The math does not easily close.

I started tracking this after noticing something in our agent latency logs. We had an agent that was supposed to autonomously review pull requests. The task was well-scoped: read the diff, identify breaking changes, leave comments. In simulation it worked fine. In production, the median task completion time was 94 seconds. The agent was not slow because it was doing complex reasoning. It was slow because it was making 7 inference calls, each waiting on decode.

There are three things that make this worse.

The first is continuous batching. Most inference deployments use continuous batching to improve GPU utilization — packing multiple requests into the same batch to share the computational overhead. The tradeoff is that your request now waits for the batch to fill or for other requests to finish. For throughput-optimized workloads this is correct. For an agent that is waiting on a single chain of dependent calls, batching adds unpredictable latency spikes. Your agent is sharing a queue with 40 other requests and you have no control over the ordering.

The second is prefill/decode scheduling. The attention computation during the prefill phase (processing the input context) and the decode phase (generating new tokens) have different computational profiles. Prefill is more GPU-memory-bound; decode is more compute-bound. Inference servers typically schedule these differently, and during high-load periods the decode phase — which your agent lives inside — gets less compute allocation. The result is that agent generation feels variable: sometimes fast, sometimes slow, with no obvious pattern tied to your prompt complexity.

The third is multi-turn state. When an agent runs a 10-step loop, each step needs to attend to the full context of all previous steps. This is architecturally correct — the agent should know what it did before. But it means the attention computation grows linearly with the number of steps, not the number of tokens per step. A 10-step agent running 500 tokens per step has the memory access patterns of an 8,000-token single-shot request. KV cache management becomes critical, and most inference servers treat the KV cache as a memory management problem, not a latency budget problem.

The practical implication is that agent design needs an explicit latency budget. Not "how good is the output" but "how fast can we get a good enough output in the time we have." This is a different optimization target than most evals measure.

There are two directions that help. The first is speculative decoding — using a smaller draft model to predict tokens and a larger model to verify, effectively parallelizing part of the decode process. The speedup is real but modest in practice, and it works best when the draft and target models are from the same family. The second is agent-specific routing: using smaller, faster models for the steps where capability margin is high (routing decisions, simple retrieval) and reserving larger models only for steps where the capability difference matters (complex reasoning, novel errors).

Neither of these solves the fundamental problem. The fundamental problem is that agents are designed as if inference is fast and context is the scarce resource. In practice, for most agentic tasks, the scarce resource is wall-clock time. And wall-clock time is bottlenecked by decode, not context.

The stronger signal for whether an agent will be useful in production is not its benchmark score. It is the p50 and p95 latency of its inference calls under the actual batched load it will face. If you have not measured that, you do not know whether your agent is fast enough to be used rather than just fast enough to be demonstrated.
