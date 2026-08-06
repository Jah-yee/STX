# EDITOR — Round 0730_2341

## Changes

1. **"First: request arrival sparsity" section** — removed redundant sentence: "The cost of waiting a few hundred milliseconds is usually less than the cost of running the same workload with no batching." Already implied by batching framing above. Keeps the section tight.

No other changes required.

---

# FINAL POST — Round 0730_2341

**Title:** Inference cost is a scheduler problem, not a model problem

---

When an inference bill comes in high, the instinct is to reach for a smaller model. Sometimes that helps. Often it doesn't — and the reason why has almost nothing to do with the model.

The dominant cost driver in most inference deployments is not model capability. It is scheduling inefficiency: how requests arrive, how they are batched, how long a GPU sits idle while waiting for the next unit of work.

## What the GPU is actually doing

A GPU running an LLM inference call spends a fraction of its time doing useful matrix multiplication. The rest is waiting — for the next request to arrive, for KV cache entries to be retrieved, for memory bandwidth to free up after the previous request's output generation completed.

This waiting is not a property of the model. It is a property of how work is dispatched to the model.

Consider two deployment patterns for the same 70B model. In Pattern A, requests arrive independently and are dispatched to the GPU as soon as they arrive. In Pattern B, requests are collected into batches of 16–32 before being dispatched, with a short wait window to accumulate candidates. Pattern B typically achieves 3–8× higher throughput per GPU-hour. The model did not change. The scheduler did.

This is not a marginal effect. In production systems handling thousands of inference requests per hour, the gap between naive and batch-optimized dispatch can represent the difference between profitable and unprofitable operation at scale.

## Three specific scheduling failures that drive up inference cost

**First: request arrival sparsity.** When requests arrive at irregular intervals, a GPU handling them individually spends significant time in low-utilization states between arrivals. The fix is request queuing with a bounded wait window — accumulate a small batch, dispatch together.

**Second: KV cache thrashing.** Modern LLMs maintain a key-value cache across the context window. When requests with non-overlapping contexts are dispatched to the same GPU in rapid sequence, the cache is evicted and rebuilt for each request. This is invisible in per-request latency metrics — each request completes quickly — but shows up clearly in aggregate GPU memory bandwidth utilization. The model is doing redundant computation that a smarter scheduler could avoid.

**Third: output generation blocking.** Generating a long output sequence occupies the GPU for hundreds of milliseconds while the model produces tokens one at a time. A naive scheduler dispatches this request and waits. A better scheduler uses the blocking time to run inference on other requests whose prefill phase has already completed, overlapping I/O and compute. This is standard pipeline parallelism, but it requires scheduling logic that most out-of-the-box inference servers do not implement by default.

## The model improvement trap

There is a common failure mode in teams that react to high inference costs by switching to smaller models: the smaller model runs faster per token, but if the scheduling infrastructure is the actual bottleneck, the improvement is smaller than expected — sometimes negligible.

The reason is that scheduling inefficiencies affect all model sizes roughly proportionally. A batch that waits 200ms for the previous request to finish wastes the same 200ms regardless of whether the GPU is running a 7B or a 405B model. The per-token cost may drop, but the per-request overhead does not.

The implication is not that model size doesn't matter for cost. It does. But before switching models, it is worth measuring how much of the inference budget is actually being spent on computation versus being lost to scheduling overhead. If the latter is large, optimizing the scheduler will outperform a model switch at a fraction of the effort.

## A test you can run

If you have access to your inference infrastructure's metrics, pull GPU utilization and request inter-arrival time for a typical hour. If you see GPU utilization below 60% during periods of normal load, scheduling inefficiency is likely a significant cost driver. The question is not whether your model is the right size. It is whether your scheduler is giving the GPU enough work to do.

I do not have a systematic study of how often scheduling explains inference cost versus model selection. But in the production systems I have looked at closely, the answer has been "more often than the team expected."
