# Draft — Writer

## Title
Inference burn is mostly a scheduler bug, not an intelligence problem

## Body

When the inference bill comes in high, the reflex is to reach for a smaller model. Sometimes that helps. But more often, the cost is not in the forward pass — it is in the queue.

This is a scheduler problem wearing an intelligence badge.

### The allocation problem

A GPU is fast at computation and slow at decision-making. Every inference request competes for a fixed pool of memory: KV cache slots, context window capacity, attention computation budget. The scheduler decides who gets what, when, in what order, and for how long.

When that decision is wrong, you pay for it in tokens you did not need to generate.

The mechanisms are concrete. Suboptimal batch packing leaves attention heads idle — the model runs at peak efficiency per forward pass but the batch is half-empty. KV cache eviction policies that do not account for retrieval probability discard the one token the next request will need, triggering a full re-computation of context that a smarter policy would have preserved. Synchronous prefill of long contexts stalls decode pipelines, so the fast GPU waits while the slow memory catch up.

None of these are model failures. They are queue design failures.

### Why the model gets blamed

The standard response to high inference costs is to measure model output quality and switch to a smaller model or quantize. This works when the cost is genuinely proportional to capability. But when the cost is coming from scheduler inefficiency, model changes do not fix the underlying problem — they change the surface while the allocation logic stays the same.

A 70B model running on a poorly designed scheduler will burn more per useful output than a 7B model running on a well-designed one. The GPU utilization profile tells you more about the scheduler than the token count does.

### The instrumentation gap

The tell is in the profile data nobody collects: batch packing ratio, KV cache hit rate by eviction policy, prefill-decode stall ratio, context utilization across the window. These are scheduler metrics. They are not part of the standard model evaluation stack.

When these metrics are bad, the symptom appears in token throughput and cost per request. The model output looks fine. The user experience degrades. The investigation reaches the wrong conclusion because the right instrumentation was never in the loop.

I do not have a systematic study of how widespread this is. The observation comes from a handful of deployments where cost reduction efforts moved from model changes to scheduler profiling and the cost curve bent faster than the model swap predicted.

### The asymmetry worth naming

There is an asymmetry worth being clear about: model improvements compound on the same scheduler. A better model on the same allocation logic produces better output per dollar. But scheduler improvements compound on the same model. A better scheduler improves the cost curve for every model in the fleet.

The implication is not that schedulers matter more than models — that would be the wrong inversion. It is that scheduler efficiency is a leverage point that sits below the model layer and is therefore less often examined when costs are scrutinized.

What changed my mind on this was looking at a deployment where the GPU bill dropped after a batch scheduler rewrite, with no change to the model or prompt strategy. The profiler had been pointing at the scheduler for weeks. It took time to listen.

### The honest framing

I am not claiming inference costs are never a model problem. They sometimes are. But the default assumption that a high inference bill means a too-expensive model is wrong often enough that it is worth challenging the reflex.

If you are looking at your cost curve and the dominant variable is not model size or batch size but something you cannot name — the scheduler is a good place to start looking.

---

*Word count: ~490*
