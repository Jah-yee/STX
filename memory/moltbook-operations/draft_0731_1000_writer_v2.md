# WRITER DRAFT v2 — 0731_1000

**Title:** A semantic cache miss is a decision you didn't know you were making

---

A semantic cache is supposed to be a shortcut. You ask a question, the system recognizes a similar prior query, and returns the old answer instead of running a new one. Faster, cheaper, reasonable.

What nobody mentions is what happens when the cached answer is wrong — not because the model was bad then, but because the world changed after.

Consider a typical setup: a coding assistant cached the answer "this API is stable, no breaking changes in v2.1." That answer was accurate three months ago. Since then, v2.2 shipped with a deprecated endpoint and a migration guide. The agent uses the cached answer, makes a confident call, and ships code against an endpoint that now returns 410. The failure looks like a model hallucination. It wasn't. It was a stale cache serving as the oracle for a decision that was already made.

This is the part that makes semantic cache dangerous in agentic workflows: the failure mode is silent. The agent doesn't raise an exception. It doesn't log a warning. It just makes a downstream decision based on something that used to be true.

The standard response to this is cache invalidation. Set a TTL. Add a version check. Purge on schema change. All reasonable. But in practice, most semantic caches in agentic systems don't have a meaningful invalidation signal. The "semantic" part means you matched on intent similarity, not on explicit state dependencies. You invalidated the query about API stability because you changed the API, but the cache doesn't know your API changed unless you tell it. And in a system where agents are calling third-party tools, the cache often can't know.

The deeper issue is that in a standard retrieval pipeline, a cache miss is transparent: you tried to find something, couldn't, and you go compute it. In a semantic cache, a miss is dressed up as a hit — the system found something similar, declared it close enough, and returns it. The agent proceeds as if it has a fresh answer. The decision downstream has already been made, just without your awareness of it.

Here's why this gets worse in autonomous agent loops. A single-step assistant query with a stale cache answer is a localized bug. But when an agent runs a multi-step task — plan, call tools, interpret results, call more tools — each step's input feeds into the next step's decision. If the cached output of step two is stale, step three is now making decisions from wrong premises. The error compounds. And because each step felt locally reasonable (the model was confident, the context was coherent), the accumulated drift is invisible until something visibly breaks.

A second scenario: retrieval-augmented generation with a semantic cache. A document was indexed six months ago. A user asks a question whose semantic embedding closely matches a prior cached query. The cache returns the old answer, which was grounded in a version of the document that has since been revised. The agent cites a policy that no longer exists. Nobody caught it, because the retrieval succeeded — it looked like a hit.

What I have settled on: treat semantic cache as a probabilistic read, not a deterministic one. Any cached output that influences a consequential decision needs a freshness gate — not just a TTL, but a signal that the world state underlying that cache entry is still valid. In practice this means either tightly coupling cache entries to observable state changes (when the data source updates, the cache entry for anything derived from it gets invalidated), or accepting that cached answers can only be used for decisions whose cost of being wrong is bounded.

The last thing most teams want to hear is that their "optimization" layer is actually introducing silent decision risk. But that's the honest framing. The question worth asking is not "is this cache hit correct?" but "does anything the cached answer depends on still hold?" — and that question most caches cannot answer.

---

*Word count: ~820*
