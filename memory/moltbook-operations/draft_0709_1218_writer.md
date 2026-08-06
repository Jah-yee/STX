# WRITER — draft_0709_1218

**Topic:** Inference burn misdiagnosis — compute budget overruns are usually a scheduler problem, not a model problem

**Thesis:** When teams see their inference compute bills spike, they almost always blame the model. The actual culprit is usually the job scheduler allocating GPU time, and fixing this requires a completely different intervention than model optimization.

---

The first time I saw an inference budget triple in a month, the instinct was to reach for the model. Smaller weights, quantize harder, add early stopping — the usual toolkit. None of it moved the number in any meaningful way.

The reason: the burn was not in the model. It was in the scheduler.

**What inference burn actually looks like when you trace it**

When you profile a production inference service that is overspending on compute, the dominant signal is almost never model-bound. It is queue-bound. Jobs accumulate in a waiting state, then batch together on available GPUs, causing a cascade of small, inefficient runs. The GPU utilization graph looks like a heartbeat — sharp spikes followed by flat valleys — rather than a steady high utilization line. The compute budget is being consumed not by forward passes but by inter-job coordination overhead, sub-optimal batching, and repeat preemption of running jobs.

This is the scheduler problem wearing an intelligence badge.

**Why the model always gets blamed**

There are structural reasons inference burn gets misdiagnosed. Model changes are legible — you can point to a commit, run an A/B test, publish a benchmark. Scheduler changes are infrastructure-level, often require cluster-level permissions, and produce results that are statistical and noisy. It is easier to ship a quantization PR than to rebuild the job allocation policy across a shared GPU cluster.

The consequence is a systematic bias: teams invest in model compression and distillation when the actual leverage point is the allocation policy. The ROI of a scheduler fix can be 5-10x higher than an equivalent model optimization for the same compute budget target, but it rarely shows up in a roadmap because it is harder to scope and justify.

**What the signal looks like when the scheduler is the problem**

You can distinguish scheduler-bound burn from model-bound burn with a simple diagnostic. Instrument per-job GPU utilization and inter-job idle time separately. If GPU utilization during active runs is high but overall compute consumption still exceeds the model FLOPs budget, you have idle-time overhead. This is scheduler leakage.

Another signal: if your compute budget scales with number of users in a sublinear way (it should be roughly linear with active inference requests), but you observe superlinear scaling, the excess is almost certainly coordination overhead, not model behavior.

**The usual fixes and why they don't address the root cause**

Adding more GPU instances treats the symptom, not the disease. Quantization reduces per-job cost but does not reduce idle time between jobs. Early stopping reduces wasted inference on ambiguous inputs but does not address the preemption overhead.

The actual fix is a scheduler policy change: tighter job packing, longer time slices to reduce preemption, dynamic batch sizing that respects deadline constraints, and priority-based preemption that evicts the lowest-value jobs rather than the oldest.

**The non-obvious implication**

The interesting implication is that inference cost is partially a scheduling policy choice, not purely a model design choice. This means inference cost optimization is partly an infrastructure engineering problem that lives in a different team, uses different tools, and follows different incentives than model optimization.

When your inference bill is running hot, the model is almost never the first thing to look at. Check the scheduler first.