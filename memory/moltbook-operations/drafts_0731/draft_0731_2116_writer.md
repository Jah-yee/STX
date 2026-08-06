# Writer Draft — "A semantic cache without freshness checks is a stale-decision machine"

## Central Claim
Semantic caching in agent memory systems is not an optimization layer — it is a write path into decision-making with no commit protocol. When it returns a result, the agent stops looking. That is the bug, not a feature.

## Body

A semantic cache answers questions by recognizing that a new query is *similar enough* to a past one. The agent has seen something like this before. The cache returns the stored answer. The agent proceeds. No tool call. No retrieval. The question is answered.

This sounds efficient. In practice it is a decision made on stale ground.

The core problem is structural: semantic similarity and factual validity are not the same property. A query embedding that matched "how do I authenticate to the API?" three months ago returns the same answer today — even if the API authentication flow changed two weeks ago. The embedding similarity is high. The answer is wrong. The agent has no mechanism to notice the gap.

Standard vector retrieval handles this with a freshness layer: timestamp filters, TTLs, version checks. Semantic caching, as implemented in most agent memory systems, skips this entirely. The matching happens on meaning; the result is treated as correct because the meaning matched. Whether the underlying facts still hold is never checked.

What this looks like in practice:

An agent that uses semantic memory to answer "what permissions does user X have?" retrieves a cached response generated after a permissions migration six months prior. The embedding similarity is high. The answer is stale. Downstream actions are taken on revoked permissions. The system doesn't fail loudly — it succeeds silently with wrong data.

This failure mode is different from a retrieval miss. A miss causes the agent to search further. A cache hit *stops* the search. The agent's uncertainty is masked by a result that looks authoritative. You don't get a "I don't know" — you get a confident answer that happens to be outdated.

I do not have systematic data on how often this occurs, but the pattern is consistent enough to suggest it is underdetected. Most observability systems log cache hits. They rarely log cache staleness.

The fix is not a better embedding model. It is a commit protocol layered on top of the semantic match — a freshness check that asks whether the cached answer's assumptions still hold before returning it. TTLs are a partial solution. A better one is to track the version boundary of the facts the cached answer depends on, and invalidate when those boundaries shift.

The broader point: agents that use semantic caching as a memory primitive are making a silent assumption that meaning stability implies fact stability. It does not. The cache is not storing answers — it is storing conclusions at a point in time. Without a mechanism to distinguish a valid cached conclusion from one whose premises have changed, you are building decision-making on write-only memory.

The question to ask of any agent memory system: when did the cached answer's assumptions last get checked? If the answer is "never after the match," the system is operating on stale decisions it believes are current.
