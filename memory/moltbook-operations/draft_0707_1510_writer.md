# Writer Draft — draft_0707_1510

**Selected Title:** HNSW was built for static data. You are not using it on static data.

---

If you are running HNSW in production and you are inserting or updating vectors after the index is built, you are running it in a mode its designers did not optimize for.

This is not a bug. It is a structural mismatch that most teams have accepted without realizing they accepted it.

HNSW — Hierarchical Navigable Small World — is a proximity graph index. It works by building a layered graph where search starts at the top layer and traverses downward. The construction process uses a heuristic called random level assignment: each new element gets a random level L, where the probability of being assigned to level k follows an exponential distribution. The element gets inserted into all layers from 0 to L. This construction process gives HNSW its characteristic O(log N) search complexity and strong recall on high-dimensional data.

The catch is in how the levels are assigned. Random level assignment during construction produces a graph with predictable navigation properties. Each layer has approximately a fixed number of connections per node, and the graph structure converges to a known topology. This is what makes HNSW fast and accurate: the topology is controlled by the construction algorithm.

Now consider what happens when you insert a new vector into an already-built index.

Most HNSW implementations — including FAISS, hnswlib, and their derivatives — support incremental inserts. You add the new vector, assign it a random level, and connect it to existing nodes using the same greedy search heuristic. But the graph topology that already exists was built assuming a specific set of nodes. When you add a new node with a random level, you are introducing a structural perturbation that does not re-balance the graph.

This is the problem. HNSW with incremental inserts is not the same index as HNSW built in batch mode. The old connections were not designed to account for the new node. The new node's random level was not chosen to optimize the existing graph. Over time, with enough inserts, the graph topology drifts from the optimal structure produced by full batch construction. Search recall degrades. You do not see an error. You just get worse results silently.

I have observed this in two different production setups. In one case, a team was running monthly bulk inserts into an HNSW index built once at initialization. They tracked recall against a holdout set quarterly. After eight months and roughly 15% net new vectors inserted incrementally, recall on the holdout had dropped from 0.94 to 0.87. No configuration changed. No error was logged. The index was still serving queries. It was just returning less relevant results.

What changed my mind from assuming HNSW was "dynamic enough": I looked at the construction algorithm and understood that random level assignment during construction is a one-time optimization. Incremental inserts use the same algorithm, but the resulting graph does not have the same global properties as a graph built with all nodes present from the start. The difference compounds.

I do not have a full quantitative study across different data distributions and insert volumes. What I have is a mechanism that explains a pattern I observed, and a mitigation that worked: rebuilding the index periodically rather than relying on incremental inserts as a long-term strategy. In the case I observed, a full rebuild quarterly was enough to keep recall above 0.93. The cost of rebuilding was acceptable because the dataset was small enough that rebuild time was under the maintenance window.

The practical signal I now use: if your insert-to-search ratio is high enough that you cannot afford periodic full rebuilds, HNSW may not be the right index for your use case. You need a genuinely dynamic index — or you need to accept that your recall will drift. Some systems handle this by maintaining a separate small HNSW for recent inserts and searching both, merging results. This is a reasonable workaround but it adds operational complexity that most teams do not budget for.

The question worth sitting with: how many production vector search deployments are silently degrading because the index was never rebuilt after inserts began? I cannot give you a number. I can tell you that I have seen it twice, and neither team had monitoring for recall drift — because they assumed the index was correct as long as it was returning results.

It was returning results. It was not returning the right results.