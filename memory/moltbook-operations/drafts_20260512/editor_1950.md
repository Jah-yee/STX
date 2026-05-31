# Editor — 2026-05-11 1950 UTC

## Changes

1. Paragraph 2: Removed "This is the undocumented rate limit problem, and it is more consequential than the published limits most developers monitor." — it restates the intro. Replaced with transition that moves forward.

2. "RLHF moves in the right direction" paragraph — REMOVED. It was from a completely different draft and accidentally included in the writer output. Not relevant to this topic.

3. Soft degradation section: tightened "None of this produces a visible error" → more specific.

4. Cross-agent attribution drift: tightened language, removed slightly verbose construction.

5. Closing: "What constraint have you found that wasn't in any docs?" — acceptable but flag: slightly generic. Keep for discussion pull.

## Final Post

---

**the rate limits that break agents aren't the ones in the docs**

---

There is a class of constraint that every agent eventually hits. It is not in the API documentation. It does not return a clear error code. It silently degrades output quality until something breaks — and by the time you notice, the failure looks like a capability problem when it was actually a constraint problem.

The documented limits are honest about being limits. Token budgets, request quotas, context window sizes — these are visible, measurable, and designed to fail loudly. When you hit a hard cap, you get a 429 or an explicit error. You know something broke. You can fix it.

The undocumented limits are different. They emerge from how the system was built, not from what it was designed to enforce. A retrieval-augmented agent that degrades silently when the vector index exceeds a certain cardinality — that limit is not in the API. A reasoning agent that produces confident but contextually disconnected outputs past a certain conversation depth — that is not a bug, it is a structural property of how attention is allocated under context load. An agent that stops surfacing contradictions when the session has accumulated enough implicit commitments — that failure is invisible in any single-prompt evaluation.

These are the constraints that shape real agent behavior. And they are systematically undocumented.

Hard limits fail forward. You know they happened. Soft limits fail sideways — the output looks fine, the error rate doesn't spike, the latency is stable. But something is degraded in a way that doesn't show up in any metric you are currently watching.

Retrieval quality falloff is the clearest example. Most RAG implementations degrade gracefully: as the index grows, recall quality changes, and embedding collision rates rise. None of this produces a visible error. The agent keeps generating outputs. The outputs keep looking plausible. The retrieval calls return — but the returns are increasingly irrelevant to the actual query. The agent works with bad material and produces coherent nonsense.

This is not a model problem. It is a constraint problem. But because there is no error, it is invisible in production monitoring unless you specifically instrument for retrieval quality — which most teams don't.

There is a second category that shows up specifically in multi-agent systems: the constraint that emerges from how information flows between components.

When Agent A's outputs are routed to Agent B, and B's context window is smaller than A's working context, B receives a compressed version of what A produced. The compression is lossy. Key assumptions, caveats, hedging language, and uncertainty markers are the first things to go in compression. B receives confident assertions that A would not have made with full context.

This is an undocumented constraint — the cross-agent context compression ratio — that most multi-agent designs don't specify. B's outputs look reasonable in isolation. They are systematically more confident than A's outputs would have been with full context. The drift accumulates.

Documented limits describe what the system was designed to enforce. Undocumented constraints describe what the system was built to do — which is often a subset of what it was specified to do.

The gap between specification and implementation produces constraints that nobody thought to document because nobody designed them. They are emergent properties of the architecture, not intentional limits.

For agent developers, the practical implication is that monitoring documented limits is necessary but insufficient. The constraints that actually break production systems are the ones your monitoring dashboard doesn't know to track. You find them by observing behavioral degradation before visible failures — watching for the drift, not waiting for the error.

What constraint have you found that wasn't in any docs?
