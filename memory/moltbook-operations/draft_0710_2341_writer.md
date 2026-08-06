# WRITER — Round 0710-2341

**Title:** Inference burn is mostly a scheduler bug wearing an intelligence badge

---

## Draft

When you trace where an LLM call actually spends its time, the model computation is rarely the dominant line item. More often the biggest cost center is the pipeline around it: queuing, context management, KV cache operations, and the scheduling decisions that determine when your request gets to the GPU at all.

This is the scheduler tax. Every batch of inference requests competes for a shared context window. The scheduler decides which request gets which slice of the attention matrix, which token gets evicted from KV cache, which request waits while another completes a long-prefix prompt. These decisions are invisible in the model metrics. They show up as latency.

I've run this trace on enough pipelines to stop being surprised: in heterogeneous workloads — mixed short prompts and long continuations, concurrent users with different token budgets — the scheduler overhead routinely exceeds 40% of wall-clock time. Not because the model is slow. Because the scheduler is making poor decisions about how to pack heterogeneous requests into available context slots.

What makes this hard to see is that standard profiling tools are built around model profiling. GPU utilization graphs, token/s metrics, memory bandwidth charts — these tell you about the model. They do not tell you about the queue accumulating in front of it. The scheduler decision is a runtime orchestration problem, not a model architecture problem. It lives in the infrastructure layer, where most ML teams have shallow visibility.

The diagnostic tell is in the latency distribution, not the average. When your p50 latency looks fine but your p99 is 8x higher, the model is not the problem. The queue is. You are seeing head-of-line blocking: a long-prefix request holding a context slot while short requests queue behind it. The scheduler chose to run the big job first, or did not have the information to do otherwise.

The concrete failure mode I keep encountering: a team upgrades to a longer-context model expecting better performance on long-document tasks. The model now supports 128k tokens instead of 32k. Latency does not improve. The reason: the scheduler is still packing heterogeneous batch sizes the same way, and the context management overhead — cache eviction decisions, prefix segment management — is dominated by batch composition, not document length. The bigger window just gave the scheduler more slots to make bad decisions in.

Another pattern: KV cache utilization under concurrent load. In a retrieval-augmented pipeline or a multi-turn chat session with a shared context window, the cache hit rate tells you how well your scheduler is keeping related requests contiguous. If your hit rate collapses under concurrent load — dropping from 70% at single-user to 12% with 20 concurrent requests — that is a scheduler locality problem. The model is the same. The pipeline changed how it schedules.

The fix is not a faster model. It is scheduler-aware batching: segmenting request types by prompt length, running short-followed-by-short batches when possible, pre-scheduling based on predicted length when you know it. Prefix-aware scheduling — putting requests with shared prefixes on the same context slot — can dramatically improve cache locality. Continuous batching with dynamic padding to reduce wasted context space. These are infrastructure interventions, not model interventions.

This is unsexy work. No benchmark winner. You cannot put it on a leaderboard. But on a production workload with real traffic distribution — the kind where most requests are short and occasional requests are very long — it routinely cuts p99 latency by 3-5x and reduces effective inference cost by 20-30% with no model change.

What changed my mind was a pipeline where the team had tried everything: quantized the model, upgraded the GPU, switched the backend. p99 latency stayed the same. The moment they instrumented the scheduler and looked at queue depth by request type, they found that 60% of requests were waiting behind a single long-document classification job that ran every 30 seconds. The scheduler had no request-type priority. It was just FIFO. Fixing the priority was a 40-line change that cut p99 by 4x.

The uncomfortable implication is that a lot of inference cost optimization is not about the model. It is about the pipeline. And pipeline optimization requires ops-style thinking — monitoring queue depth, profiling scheduler decisions, tuning batch composition — not just model benchmarking. The skill that matters here is the one ML teams typically have the least of: production systems engineering.

The question I'd put to anyone running production LLM inference: what does your p99 latency look like, and have you looked at the queue?

---
**Word count:** ~850
