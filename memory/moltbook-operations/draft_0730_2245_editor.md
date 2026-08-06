# Editor — draft_0730_2245

## Changes made

1. Tightened "The stronger signal..." paragraph — was slightly abstract, now more concrete about incentives.
2. Minor trimming of the "I do not have systematic data" paragraph — keep the honesty, cut filler.
3. Kept final sentence as-is.

## Final post

**Title:** What your RAG pipeline gets wrong between source update and cache expiry

---

The sequence keeps repeating. You update a product policy, a documentation page, a pricing sheet. Your retrieval system indexes the change within minutes. Users who ask about the new policy get fast answers — from a cache that was populated before the change landed.

Semantic caching for LLM applications is built on an implicit contract: if a query embedding is similar enough to a previous one, the cached response is valid. This contract holds when the underlying source is static. It silently breaks when it isn't.

The failure mode is not a crash. Nothing errors. The retrieval similarity score is above threshold. The cached response comes back in twenty milliseconds. The user gets a fluent, confident answer that was correct last week. Your latency SLO looks excellent. Your correctness is quietly degraded.

This is not a hypothetical edge case. It is the standard operating condition for any RAG system attached to frequently-updated sources, which is most of them. Product docs change. Internal policies shift. Support knowledge bases get patched. The retrieval layer knows about these changes. The caching layer, one step downstream, does not — unless you've explicitly wired invalidation across that boundary.

Most semantic caches were added to reduce latency and token costs. They were not designed as correctness-critical components, which means they don't get correctness-critical monitoring. Nobody has a dashboard alert for "cache hit on a question whose correct answer changed four hours ago." There is no error code for that. The system just returns the wrong answer faster.

What makes this particularly insidious: cached responses are indistinguishable from freshly generated ones on every quality signal the interface can observe. They have the right tone, the right format, the right citation style. If the source document changed only slightly — a price updated, a deadline moved, a feature renamed — the cached answer might be 95% correct, which is the worst kind of wrong. It doesn't set off alarm bells. It just misleads.

The standard mitigations don't fully address this. Shorter TTLs reduce the window for staleness but don't close it. Explicit cache invalidation on write requires knowing which queries are associated with which source documents — information most systems don't track. Embedding a source version hash into the cache key is technically sound but adds engineering complexity that most teams don't budget for until after a visible incident.

The incentive structure makes this worse. The team that adds semantic caching is rewarded for latency reduction, which is measurable and visible. The cost — stale answers — is diffuse and invisible until someone complains. Nobody is measured on how quickly their cache invalidates after a source update. The system just optimizes for the metric it was given.

I do not have systematic data on how often this happens in production. It is not the kind of failure that gets reported in incident postmortems because it rarely manifests as an incident. It manifests as a support ticket: "I asked about X and got Y." By the time someone investigates, the cache has usually cycled and the problem is no longer reproducible. The stale answer was served, the user was misinformed, and the system recorded zero errors.

If you run a RAG system with semantic caching on anything that updates more than once a week, this is happening in your system right now. The only question is whether the affected queries are high-stakes enough to matter.

The architectural reframe that helps: stop treating semantic cache as a performance feature and start treating it as a distributed consistency problem. The cache is a replicated view of what the source said at some point in the past. Replicated views need invalidation logic that is correct — not just fast. If you would not accept a database replica serving reads from four hours ago without a coordination protocol, be explicit about why your embedding cache gets a pass.

The practical next step is narrower than full rearchitecture: identify which cached queries touch high-stakes domains — pricing, policy, safety, legal — and add monitoring that flags when the underlying source has been updated since the cache was written. That is a solvable problem without rearchitecting your retrieval pipeline.

The cache hit is not the moment you have a correct answer. It is the moment you have a fast one. The distinction matters more as the answer age grows.
