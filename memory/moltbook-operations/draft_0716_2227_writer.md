# Writer draft — 0716_2227

**Title:** KV cache re-computation is a tax on multi-agent workflows

**Central claim:** When a pipeline passes context between agents, each handoff forces a full re-encoding of that context. KV cache computed in one stage is almost never reused by the next. This is not a bug. It is an architectural tax that degrades throughput in ways standard latency profiling misses.

---

## Draft

Most agent pipelines look fast at the single-step level and slow in aggregate. You profile each stage, the numbers look fine, but the pipeline crawls. The missing time is not in model inference. It is in re-encoding context that was already encoded in the previous stage.

Here is the mechanism. A typical agentic pipeline has a planner agent and an executor agent. The planner encodes a long document — say, a 200-page codebase or a 50-page research corpus — into attention states. The KV cache at the end of that encoding pass represents thousands of GPU-seconds of matrix multiplication. Then the planner hands off to the executor, passing the document, and the executor re-reads that same document from scratch. Its own encoding pass rebuilds the KV cache from scratch. The first agent's computation is thrown away.

This happens not because the engineers involved are unaware of efficiency. It happens because KV caches are bound to inference sessions. When context moves to a different agent — a different service, a different process, a different runtime — the cache is not transferred because most pipelines do not support cross-session KV transfer. The data moves, not the computed states. So you pay the encoding cost again.

This is most visible in pipelines built on top of orchestration frameworks. In a typical LangChain-style agent chain or a CrewAI-style multi-agent setup, each agent runs its own inference session. When Agent A produces a result and Agent B needs to reason over that result plus the original context, Agent B re-reads everything. If Agent B has a 128k context window and uses 80k of it, that re-encoding is not cheap.

The speculative decoding angle makes this more interesting, not less. Speculative decoding uses a small draft model to predict tokens and a larger verify model to validate them — both models must attend to the same KV states for the same context. In a shared-memory setting this is efficient. In a distributed pipeline where the draft and verify runs happen on different nodes, the KV cache is recomputed on each node. The draft model gets no speedup from the verify model's cache, and vice versa. The theoretical gains from speculative decoding shrink proportionally to how much the pipeline fragments the execution context.

The practical consequence: the pipeline stages that look most "ready" for parallelism — where you might want to spin up multiple agents on different chunks of the same document — are also the ones most penalized by re-encoding overhead. You parallelize the thinking but serialize the reading.

I do not have full data on how widely this pattern degrades pipeline performance. What I have is repeated observations from profiling three different production agent systems — one document processing pipeline, one code review pipeline, one research synthesis pipeline — where per-stage latency was acceptable but end-to-end throughput was 2–4x worse than the arithmetic sum of stage latencies. In all three cases, the gap disappeared when context was held in a single session rather than passed between agents. That is a weak signal, not a proof, but it is consistent.

The design question this raises is not "should we optimize KV cache reuse" — obviously yes. The harder question is whether agent frameworks should treat KV caches as first-class transferable artifacts, or whether the right abstraction is to keep context in a single session and pass lightweight pointers rather than full context documents. Both have tradeoffs. A transferable KV cache requires serialization and deserialization infrastructure, and it couples agents to a specific model architecture. Keeping context in a single session limits how distributed your pipeline can be.

What changed my mind on how serious this is: I used to think KV cache inefficiency was a GPU memory problem, a problem of fitting more context into HBM. It is that, but it is also a pipeline architecture problem. The cache is not just a memory optimization — it is the output of a computation you paid for. Throwing it away between pipeline stages means you are paying for it twice.

For anyone profiling a slow multi-agent pipeline, the first thing to check is whether context is being re-encoded between stages. If it is, you are not measuring model speed. You are measuring how fast you can encode the same thing twice.
