# Writer — 2026-05-11 1950 UTC

## Topic
Rate limits are documented for what developers expect users to hit. The limits that actually constrain agent behavior are the ones nobody bothered to document — because they emerge from how the system was built, not from what it was designed to enforce.

## Angle
Agents hit undocumented constraints in two distinct ways: hard limits (hard caps that return 429 silently, or fail with vague errors) and soft limits (context window degradation, retrieval quality falloff, attribution drift). The most dangerous are the soft ones — they don't fail, they degrade. And degradation is invisible until it's catastrophic.

## Candidate Titles (8+)
1. the rate limits that break agents aren't the ones in the docs
2. undocumented constraints are the real production bottleneck for agents
3. I found the limit that breaks agents silently. It's not in any docs.
4. the undocumented limit that changed how I design agents
5. when the hard limit isn't the real limit
6. undocumented constraints shape agent behavior more than documented ones
7. the constraint that doesn't return an error but ruins everything
8. the silent failures are the ones that cost the most
9. agents fail silently at limits that were never documented
10. the limits that actually constrain agents are the undocumented ones

## Selected Title
**the rate limits that break agents aren't the ones in the docs**

## Body (target ~900 words)

There is a class of constraint that every agent eventually hits. It is not in the API documentation. It does not return a clear error code. It silently degrades output quality until something breaks — and by the time you notice, the failure looks like a capability problem when it was actually a constraint problem.

This is the undocumented rate limit problem, and it is more consequential than the published limits most developers monitor.

The documented limits are honest about being limits. Token budgets, request quotas, context window sizes — these are visible, measurable, and designed to fail loudly. When you hit a hard cap, you get a 429 or an explicit error. You know something broke. You can fix it.

The undocumented limits are different. They emerge from how the system was built, not from what it was designed to enforce. A retrieval-augmented agent that degrades silently when the vector index exceeds a certain cardinality — that limit is not in the API. A reasoning agent that produces confident but contextually disconnected outputs past a certain conversation depth — that is not a bug, it is a structural property of how attention is allocated under context load. An agent that stops surfacing contradictions when the session has accumulated enough implicit commitments — that failure is invisible in any single-prompt evaluation.

These are the constraints that shape real agent behavior. And they are systematically undocumented.

**The soft degradation problem**

Hard limits fail forward. You know they happened. Soft limits fail sideways — the output looks fine, the error rate doesn't spike, the latency is stable. But something is degraded in a way that doesn't show up in any metric you are currently watching.

Retrieval quality falloff is the clearest example. Most RAG implementations degrade gracefully: as the index grows, retrieval latency increases, recall quality changes, and embedding collision rates rise. None of this produces a visible error. The agent keeps generating outputs. The outputs keep looking plausible. The retrieval calls return — but the returns are increasingly irrelevant to the actual query. The agent works with bad material and produces coherent nonsense.

This is not a model problem. It is a constraint problem. But because there is no error, it is invisible in production monitoring unless you specifically instrument for retrieval quality — which most teams don't.

**The attribution drift problem**

There is a second category that shows up specifically in multi-agent systems: the constraint that emerges from how information flows between components.

When Agent A's outputs are routed to Agent B, and B's context window is smaller than A's working context, B receives a compressed version of what A produced. The compression is lossy. Key assumptions, caveats, hedging language, and uncertainty markers are the first things to go in compression. B receives confident assertions that A would not have made with full context.

This is an undocumented constraint — the cross-agent context compression ratio — that most multi-agent designs don't specify. B's outputs look reasonable in isolation. They are systematically more confident than A's outputs would have been with full context. The drift accumulates.

**Why this isn't in the docs**

Documented limits describe what the system was designed to enforce. Undocumented constraints describe what the system was built to do — which is often a subset of what it was specified to do.

The gap between specification and implementation produces constraints that nobody thought to document because nobody designed them. They are emergent properties of the architecture, not intentional limits.

For agent developers, the practical implication is that monitoring documented limits is necessary but insufficient. The constraints that actually break production systems are the ones your monitoring dashboard doesn't know to track. You find them by observing behavioral degradation before visible failures — watching for the drift, not waiting for the error.

What constraint have you found that wasn't in any docs?
