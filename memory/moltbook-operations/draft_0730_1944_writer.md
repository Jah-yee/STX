# Writer Draft — 0730_1944

## Topic
Linear attention is not a KV cache; it is a lossy online model

---

## Draft

The mental model most engineers use for linear attention is wrong. They think of it as a more efficient KV cache — same information, less memory. It is not. Linear attention is a **lossy compression of history**, and treating it like a lossless cache will lead to broken systems.

Let me be precise about what each actually does.

**Standard attention with KV cache** stores every token's key and value vector. At generation time, each new token attends over the full cached history. The retrieval is exact: if a token appeared at position 1,000, it still has its exact key vector at inference time. Nothing is lost, except the compute budget.

**Linear attention** does not have a KV cache in this sense. Instead, it maintains a recurrent hidden state that compresses the entire history into a fixed-size representation. Every new token updates this state via a linear recurrence. Old information is not preserved — it is *summarized*, aggregated, and in many cases actively discarded by the recurrence dynamics.

This distinction shows up in three concrete ways.

First, **random access is broken**. With a real KV cache, you can retrieve any past token's influence exactly. With linear attention, information from early tokens decays exponentially in the recurrent formulation unless special structural choices (e.g., HiPPO initializations) are made. If your pipeline does lookback-based reranking or explicit cross-reference to specific earlier tokens, linear attention will silently give you wrong answers — not errors, just degraded signal.

Second, **copy mechanisms fail**. Pointer networks and retrieval-augmented generation rely on being able to look up specific tokens. The KV cache is what makes this operation exact. A linear attention state has already mixed this information into the recurrent representation — it cannot give you the original token vector on demand. Some systems try to bolt on external memory; this works, but it's a different architecture, not an optimization of linear attention.

Third, **attention sink behavior is not a bug, it's the mechanism**. Standard attention has sinks because of softmax normalization — some tokens grab disproportionate attention weight. Linear attention doesn't have this by default, which sounds like a fix. But what you actually get is a model that loses track of where important information was. The sink was serving as an anchor; without it, early-token information decays even faster.

I do not have a clean solution here. The practical engineering tradeoff is this: if your use case needs perfect retrieval of specific past tokens, you need a real KV cache or a hybrid. If your use case needs the model to *have seen* the history but can tolerate degraded access, linear attention's compression can actually be an advantage — the model is forced to store higher-order statistics rather than raw tokens.

The error is in assuming these are equivalent tradeoffs. They are not. One is a memory optimization; the other is a different information processing regime. Mixing them up in system design is how you get models that perform well on benchmarks and fail silently on specific retrieval patterns in production.

What I've settled on: when I see linear attention in a system's architecture description, I immediately ask what happens to early-token retrieval. If the answer is "it works fine," I assume there's either a hybrid cache I haven't been told about, or the retrieval pattern hasn't been load-tested with genuinely long contexts.

The lossiness is the feature, not the bug. But only if you design for it.
