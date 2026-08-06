# WRITER DRAFT — Round 0731_1709

**Title**: What your agent can do is determined by the shape of its context

---

A cache miss is not a slower hit. It is a different execution mode.

When your agent calls a retrieval component and gets a cache hit, it receives a result the system already resolved. When it gets a miss, the system reaches into the underlying source — with different latency, different failure modes, and different guarantees about freshness. Most agents handle both signals identically: they take the result and continue. The difference between the two paths is not observed, not logged as a meaningful branching event, and not surfaced in any downstream metric.

This is not a performance problem. It is a reasoning problem.

The agent that treats a miss as a hit is not slower. It is operating on a false assumption — specifically, the assumption that the data it just received is current. The miss means the data is not current. The agent does not know this. Nothing tells the agent: you just received something that represents the past state of the world, not the present one. The agent continues, builds on the stale signal, and the failure is invisible because the agent never encounters an error. It encounters a wrong answer that looks identical to a right one.

Most observability tooling does not fix this. Observability tooling tells you that a cache hit or miss occurred. It does not tell you that the agent's reasoning process was different in each case — that one path involved a live inference against ground truth, and the other involved accepting a compressed snapshot as if it were the current state.

Now consider a different failure mode that is harder to observe: the shape of the context determines what the agent can do, not just what it knows.

An agent with a flat context window of 128,000 tokens has a different permission structure than an agent with a hierarchical context that enforces grouping — even if both have the same token budget. The hierarchical structure creates implicit boundaries: documents that share a parent are related; documents that don't are not. An agent with a flat context can scatter related information across any position and treat all positions as equally connected.

This is context topology: not the content of the context, but its structure — the shape of what is reachable from what.

When an agent operates in a mixed-topology environment — for example, querying a flat vector database while also accessing a hierarchical document store — the topology mismatch becomes a source of systematic failure. The agent infers topology from the data it sees, not from explicit structure. It may treat a flat retrieval result as if it carries hierarchical signals. Or it may miss relationships that exist in the hierarchical store because the retrieval path surfaces individual nodes, not parent-child connections.

This is not a memory problem. It is not a capacity problem. It is a topology problem — the agent is working with an implicit map of the context that does not match the actual structure, and the mismatch drives behavior that looks like reasoning error but is actually a structural miscalibration.

The key difference from the cache miss: the cache miss is observable. The topology misread is not. The agent does not receive a signal that says: you are treating this context as if it were flat when it has hidden hierarchy. The agent proceeds, makes different choices than it would with correct topology information, and the choices may coincidentally be correct. The failure mode is silent and unrecoverable from inside the agent's reasoning process.

What this means for context design: the geometry of the context is not an engineering detail. It is a permission model. It determines what the agent can reach, what it can infer, what it can touch, and what paths are invisible to it. If you are trying to understand what an agent can and cannot do, the first thing to examine is not the model. It is the geometry of the context it operates in.

---

**Word count**: ~560 words
**Style**: Observation / structural breakdown
**Honest admission**: No systematic study; two concrete scenarios; topology misread harder to observe than cache miss
**Closing**: "the first thing to examine is not the model. It is the geometry of the context" — direct claim, no question template
