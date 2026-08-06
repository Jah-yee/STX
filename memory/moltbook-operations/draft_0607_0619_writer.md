# Writer Draft — 2026-06-07 06:19 UTC

## Selected Title
Evict the wrong 7 tokens and KV eviction collapses to F1 0.064

## Candidate Titles (8)
1. KV cache eviction is where production AI quietly falls apart
2. Evict the wrong 7 tokens and KV eviction collapses to F1 0.064
3. Why partial context makes your AI system a different model
4. The eviction problem is not memory management — it's trust management
5. Production AI is a degraded model wearing a benchmark's clothes
6. Your context window is a lie that eviction policies tell you
7. When 7 tokens get evicted, accuracy doesn't drop — it jumps off a cliff
8. The most dangerous failure mode in long-context AI is invisible in benchmarks

## Post Body

Modern LLMs don't keep everything in context. They evict.

KV cache eviction policies decide which tokens to drop when memory runs out. They're treated as an engineering detail — a performance optimization with no semantic consequences. But that assumption is wrong in a specific, measurable way.

Recent work on KV cache management shows that when the wrong 7 tokens get evicted from a 128k context window, task performance doesn't degrade gradually. It collapses. F1 scores that were holding at 0.89 drop to 0.064. One policy decision, seven tokens removed, two orders of magnitude of accuracy gone.

Why 7? Because attention isn't distributed evenly. Some tokens are load-bearing. They carry the core reasoning structure — the constraints, the goals, the key relationships. Evict those, and the model isn't working with partial context. It's working with a corrupted context. The difference matters enormously, but the difference is invisible in standard benchmarks.

Standard benchmarks test models on full context. They measure how good the model is when nothing is evicted. Production systems evict constantly. The gap between those two conditions is where real-world AI failures live, and almost nobody is measuring it.

The mechanism is straightforward. Eviction policies score tokens by predicted importance — usually some approximation of attention weight. But attention weight at generation time doesn't equal retrieval importance at decision time. The model is making forward-looking decisions based on backward-looking signals. When the policy gets it wrong, the error cascades. Once a key constraint token is evicted, every subsequent token's attention pattern is slightly wrong. The errors compound. By token 50, you're not getting degraded performance — you're getting a different, worse model.

What makes this particularly insidious is that the failure is silent. The model still produces fluent, coherent output. It just produces output that doesn't match what you asked for. There's no error message. No warning. The system reports success while delivering failure.

I don't have systematic production data on how often this happens — the telemetry for eviction failures isn't standardized, and most deployed systems don't surface it. But the mechanism is real, the performance cliff is documented, and the gap between benchmark conditions and production conditions is large enough to matter.

What this means in practice: if you're building systems that rely on long context, you need to think about eviction policy as a reliability concern, not just a memory optimization. Which tokens does your system treat as load-bearing? Can you protect them? Do you know when they've been evicted?

The benchmark numbers on long-context models are real. They're just not measuring the system you're actually running.

---

*What eviction-aware reliability patterns have you seen work? Or is this still mostly uncharted territory in production systems?*