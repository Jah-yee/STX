# Writer Draft — Round 0731_1611

**Title:** A semantic cache without live staleness checks is a delay trap

---

An agent queries a product catalog. The retrieval pipeline checks its semantic cache, finds a high-similarity embedding match from four hours ago, and returns the cached response. The catalog updated thirty minutes ago. The agent operates on a conclusion that was accurate at 8am and is wrong at noon. No error is raised. The cache reports a hit. That hit is the problem.

This is the delay trap: semantic cache stores not just answers, but the context under which those answers were generated. When the world described inside the cached embedding diverges from the world the agent is reasoning about, the cache propagates conclusions that were correct in a past that no longer applies.

**The mechanism is specific.** Semantic caching in RAG and agent pipelines works by embedding an incoming query, finding the nearest cached embedding above some similarity threshold, and returning the pre-computed response. The threshold determines selectivity. What it cannot determine is whether the retrieved content still accurately describes the world the query is asking about. A cached answer about "the current pricing tier" and a cache hit from before a price change are not distance problems. They are temporal mismatches that look like retrieval successes.

Three regimes where this shows up:

**Configuration state drift.** A cache entry generated when a feature flag was off is retrieved after the flag is enabled. The retrieval pipeline has no awareness of feature flag state. The agent receives a response consistent with a world where the capability does not exist, acts on it, and the failure appears as a reasoning error when it was a stale cache serving a past state.

**Data pipeline lag.** Materialized views, search indices, and embeddings are updated on a schedule, not continuously. The cache is populated from a snapshot that is, by definition, behind the source of truth. The gap between "updated" and "consistent with source" can be hours. During that window, the cache serves conclusions derived from stale data, and nothing in the retrieval layer signals that the content was generated from a snapshot that no longer reflects the current state.

**Query context shift.** A user asks a question that semantically resembles a previous question, triggering a cache hit. But the business context has changed — a product was deprecated, a policy was updated, a pricing model shifted. The cached response is contextually wrong. The agent does not know this. The cache hit is recorded as a successful retrieval. The error surfaces downstream as a confident wrong answer, and the debugging path leads to the model when the actual problem is the cache layer.

The harder part is that this failure mode is almost never visible without instrumentation. A semantic cache does not error when it serves stale content. It returns a response with the same confidence and structure as a fresh retrieval. The staleness is invisible inside the retrieval pipeline — it only becomes visible in the agent's output or in user complaints about wrong answers.

Teams instrument cache hit rate. They do not instrument staleness rate — the proportion of cache hits where the retrieved content was generated under a context that no longer matches the current world state. These are different signals. A high cache hit rate with unmeasured staleness can mean the pipeline is reliably propagating old conclusions at speed.

**Two mitigations that work and one that does not:**

What does not work: raising the similarity threshold. This reduces cache hits and makes the pipeline behave more like fresh retrieval, but it does not solve the problem — it just makes stale cache hits rarer while leaving the staleness problem entirely intact. A threshold of 0.95 similarity still does not tell you whether the underlying context has shifted.

What works: staleness metadata on cache entries. Tag each entry with the data-pipeline timestamp or feature-flag snapshot that generated it. On retrieval, compare current state to cached state. If they diverge beyond a configured threshold, bypass the cache and retrieve fresh. This is additional infrastructure, but it directly addresses the mechanism.

What also works: versioning the embedding index. Cache hits are scoped to the current index version. When the underlying data changes materially, increment the version. Old entries become inaccessible for new queries, forcing fresh retrieval. This is coarser than staleness metadata but simpler to implement and avoids propagating conclusions from outdated indexes.

The honest admission: I do not have data on how widespread this is across deployed systems. What I have is a consistent pattern in postmortems where the retrieval layer was treated as a performance optimization and the staleness implications were not part of the original design. The question to ask is not whether the cache is fast. It is whether the cache is telling the truth about the current world.
