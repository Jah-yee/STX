# EDITOR DRAFT — Round 0731_1709

**Title**: What your agent can do is determined by the shape of its context

---

A cache miss is not a slower hit. It is a different execution mode with a different contract.

When your agent calls a retrieval component and gets a cache hit, the system returns a result it already computed. When it gets a miss, it reaches into the underlying source — with higher latency, different failure modes, and different freshness guarantees. Most agents handle both signals identically: they take the result and continue. The branching difference is not observed, not logged as a meaningful event, and not surfaced in any downstream metric.

This is not a performance problem. It is a reasoning problem.

The agent that treats a miss as a hit does not slow down. It operates on a false assumption — specifically, the assumption that the data it received is current. The miss means the data is stale. The agent does not know this. Nothing signals: you just received a compressed snapshot of the world, not its present state. The agent builds on the stale signal, and the failure is invisible because the agent never encounters an error — only a wrong answer that looks identical to a right one.

This is distinct from a retrieval failure. A retrieval failure produces an error signal: null, timeout, permission denied. A cache miss produces a result. The agent has no reason to treat it differently from a hit unless the system explicitly surfaces the distinction, and most systems do not.

Most observability tooling does not close this gap. You can see that a cache hit or miss occurred. You cannot see that the agent's reasoning process was structurally different in each case — that one path involved a live inference against ground truth, and the other involved accepting a compressed snapshot as if it were current. The metric system treats them as equivalent events. The agent does the same.

Now consider a second failure mode that is harder to detect: the shape of the context determines what the agent can do, not just what it knows.

An agent with a flat context window of 128,000 tokens has a different permission structure than an agent with a hierarchical context that enforces grouping — even with the same token budget. The hierarchical structure creates implicit boundaries: documents that share a parent are related; documents that do not are not. A flat context lets the agent scatter related information across any position and treat all positions as equally connected. The agent infers topology from the data it sees, not from explicit structure.

When an agent operates in a mixed-topology environment — querying a flat vector database while also accessing a hierarchical document store — the mismatch becomes a source of systematic failure. The agent may treat flat retrieval results as if they carry hierarchical signals. Or it may miss relationships that exist in the hierarchical store because the retrieval path surfaces individual nodes, not parent-child connections. The agent's implicit map of the context does not match the actual structure, and this drives behavior that looks like reasoning error but is actually structural miscalibration.

The topology misread is harder to detect than the cache miss. The cache miss is observable — you can instrument for it. The topology misread is silent. The agent does not receive a signal saying: you are treating this as flat when it has hidden hierarchy. The agent proceeds, makes different choices than it would with correct topology information, and those choices may coincidentally be correct. The failure mode is invisible from inside the reasoning process.

This matters for context design in a specific way: the geometry of the context is not an engineering detail. It is a permission model. It determines what the agent can reach, what it can infer, what paths are visible, and what paths are invisible to it. When you design a context structure, you are making implicit authorization decisions about which information is reachable from which other information — and those decisions shape the agent's effective capabilities independent of what the model is capable of in the abstract.

If you want to understand what an agent will actually do in production, the first thing to examine is not the model. It is the geometry of the context it operates in.

---

**Word count**: ~680 words
**Editor changes from writer draft**:
1. Added explicit contrast between cache miss and retrieval failure (null/timeout vs result) — sharpens the distinction
2. Expanded topology misread section — added mixed-topology scenario, makes mechanism concrete
3. Strengthened closing — added "authorization decisions" framing, making the permission model claim more specific
4. Removed "This is not a memory problem. It is not a capacity problem." — the triple negation was defensively worded
5. Minor: "does not match the actual structure" → "does not match the actual structure, and this drives behavior that looks like reasoning error but is actually structural miscalibration" — adds the causal link
