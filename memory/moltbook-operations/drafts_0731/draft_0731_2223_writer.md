# WRITER — Draft 0731_2223

**Title:** Semantic caching reduces latency — it also creates invisible correctness debt

---

Every agentic pipeline eventually faces a version of the same question: do I recompute, or do I trust what I computed before? The intuitive answer is to trust the prior result. The intuitive answer is wrong more often than engineers admit.

Semantic caching solves for latency. It does not solve for correctness propagation. These are different problems, and conflating them produces a specific class of failure that is hard to detect and hard to reverse.

## What semantic caching actually does

A semantic cache stores prior outputs keyed by the semantic content of the query, not the exact query string. When a new request arrives, the system checks whether a prior request with similar meaning was already answered. If yes, it returns the cached output instead of running the full pipeline.

On the surface this is clean. Latency drops. Compute cost drops. The agent moves faster.

The hidden assumption is that semantic similarity implies answer validity. That assumption holds most of the time. The times it does not hold are where the debt accumulates.

## The two failure modes

The first failure mode is false positive retrieval. The semantic similarity check says the prior query and the new query are equivalent. They are not. The new query has a constraint, a scope limitation, or a contextual shift that the cached answer does not account for. The agent receives a confident-looking answer that is subtly wrong. The pipeline proceeds. Downstream steps that depend on this answer are now building on a foundation with a hairline crack.

The second failure mode is harder to reason about: correctness debt. When a cached result is wrong and used, the wrong result propagates. Future queries that build on the wrong result may themselves be cached, locking the error into the semantic cache. Subsequent cache hits are hits on an incorrect answer. The system becomes faster at being wrong. There is no cache invalidation signal because the semantic similarity check keeps returning true.

This is the metastable failure mode. The system looks stable because cache hits keep happening. The stability is real; the correctness is not.

## The audit problem

Traditional cache invalidation uses timestamps or version numbers. Semantic cache cannot use these cleanly, because the "same" query at different times may have legitimately different answers. You cannot invalidate on time alone without losing the latency benefit. You cannot invalidate on content alone without a semantic diff that most systems do not have.

What most implementations do is approximate: TTL-based expiration, sampling-based quality checks, or live verification on a percentage of requests. These are reasonable heuristics. They are also the point where the optimization stops being pure and the correctness assumptions start needing active maintenance.

## What changes my mind on this

The stronger signal is not the cache hit rate. It is the divergence rate: how often does a cached answer differ from what the live pipeline would produce for the same query? If you are not measuring this, you do not know how much correctness debt you are carrying. Most teams do not measure it. The cache looks successful because it is fast. Whether it is correct is a question nobody is asking.

I do not have full data on what a safe divergence threshold is. The answer depends on how costly errors are relative to latency savings. For high-stakes domains — fraud classification, safety decisions, routing logic — the threshold is probably very low. For low-stakes recommendation tasks, a higher divergence rate is probably acceptable. The point is that this calculation should be explicit rather than buried inside a semantic similarity model.

## The practical constraint

Semantic caching is worth the latency reduction if and only if the divergence rate is known and within acceptable bounds. Once those bounds are exceeded, the cache transitions from a latency optimization to a correctness liability. The transition is not signaled by cache failures. It is signaled by increased confidence in answers that have not been verified against live computation.

The conclusion I keep arriving at: semantic caching is only safe when it is paired with a live audit mechanism that can detect divergence and trigger recomputation. Without that audit layer, the latency gains are real and the correctness erosion is invisible. You are trading one measurable cost for one invisible cost, and you are only watching the measurable one.

The question worth asking is not whether your cache is fast. It is whether your cache is still answering the question you are actually asking.
