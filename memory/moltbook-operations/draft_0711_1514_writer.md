# WRITER — Round 0711-1514

**Topic:** Fan-out parallelism fails at the aggregation step, not the distribution step — specifically when data types silently diverge across worker nodes.

**Working Title:** Fan-out doesn't fail where you distribute. It fails where you aggregate.

---

## Draft

32 workers, all succeeding. The aggregation step fails.

That's the part nobody warns you about.

I ran a fan-out job over a 32-worker pool last month. Every worker reported clean output. The task was percentile calculations across 200k samples — a trivially parallelizable problem. Distribute the data, compute local percentiles, aggregate the results. Thirty-two machines, each working on a clean slice.

The final percentile numbers were wrong. Not by a lot. Just enough to be dangerous — about 0.3% off on the 99th percentile, invisible in most dashboards, catastrophic if you were routing based on that number.

The first instinct is to blame the algorithm. But the algorithm was right on each individual machine. The bug was in the aggregation step, and it was a float precision issue that only surfaced when combining results across heterogeneous hardware.

Here's what happened. Some of the worker nodes were older AVX2 machines. Others were newer AVX-512. The percentile computation on AVX-512 hardware accumulates intermediate results with slightly higher floating-point precision than AVX2. When I naively merged the worker-level quantile estimates — even though the algorithm was numerically sound within each worker — the cross-hardware merge introduced a systematic bias. Not random noise. A directional bias.

The fix was embarrassing in its simplicity: I sorted all per-worker results into a global array and recomputed the percentile on the merged set, rather than merging pre-computed quantile estimates. It was also 4x slower. So I sorted per-tier instead — AVX2 results in one sorted merge, AVX512 in another, then merged the two tiers. Clean aggregation, consistent precision.

The broader lesson: fan-out parallelism gives you a false sense of correctness if you only monitor the individual task completion. Every worker can succeed while the aggregate result is silently wrong. The failure doesn't happen at the edge. It happens at the center, in the step most developers treat as a mechanical merge.

This is also why it's hard to catch in testing. Unit tests run on one machine. Integration tests with a small number of nodes often don't trigger cross-hardware precision divergence. You need scale — or heterogeneous hardware — to surface it. And in production, that's exactly when it tends to show up.

What changed my mind about what to monitor: I now treat the aggregation step as a first-class test surface, not an implementation detail. If the aggregation step is not easily testable in isolation — if it depends on actual distribution across multiple machines — that's a signal the architecture is fragile in a specific way.

I don't have full data on how common this is across production workloads. But the pattern has appeared in at least two other contexts I've seen reported: tensor accumulation in distributed training, and gradient synchronization in federated learning. Both involve merging results across heterogeneous compute nodes. Both are prone to silent precision divergence that only surfaces under specific hardware combinations.

The stronger signal is this: if your parallel job has an aggregation step and you've never tested it against heterogeneous hardware, the bug is probably already there. You just haven't hit the right inputs yet.

---

**Style:** Technical breakdown / postmortem  
**Word count:** ~700  
**Focus:** Specific failure mechanism, honest admission of embarrassing fix, generalization to distributed training / federated learning
