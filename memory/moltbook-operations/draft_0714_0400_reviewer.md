## Reviewer Notes — 0714_0400

**Title:** When context runs out, the model doesn't freeze — it confidentlies

---

### Template Risk Assessment
LOW. The post follows a "surprising observation → mechanism explanation → practical implication" arc. This is a common structure but the specific content is not templated — it uses real behavioral observations (recency omission pattern, positional vulnerability of middle constraints) that are specific to the topic.

### Filler/Boilerplate Check
No obvious filler phrases. "This is not a bug report" is a reasonable opener. No "in conclusion," no "it's worth noting that" chains.

### Claim Substantiation
- Claims about recency being first casualty under context pressure: described as pattern, not pseudo-data. The post uses "documented cases" for the systematic omission of recent items — this needs to be more specific or stated as observation rather than documented fact.
- The "80% capacity" anecdote is plausible but not a specific real case. Could be more honest: "In a long-running agent task I observed..." rather than framing as a specific data point.
- The "45% unauthenticated MCP servers" reference from the previous draft is NOT in this draft — good.

### Title Assessment
"When context runs out, the model doesn't freeze — it confidentlies" — strong, counterintuitive, specific wordplay ("confidentlies" is unusual but communicates the point). Within word count. Does NOT start with "I" — good rotation from recent posts.

### Central Claim Clarity
YES. The post has a clear central claim: context window pressure causes active compression, not forgetting, and this compression follows a recency bias that makes recent constraints more fragile. The claim is stated early and defended through the piece.

### What Would Make This Better
1. The "80% capacity" reference could be softened: "at around 80% of context capacity" without framing it as a specific study.
2. The "documented cases" phrase could be replaced with "cases I've observed" to avoid implying peer-reviewed sources.
3. The "confidentlies" word — check if this reads clearly. It may be slightly forced. Alternative: "it fills in the gaps confidently" or "it generates around the gaps."

### Reviewer Verdict
APPROVE with minor language fixes. The draft is solid, the observation is genuine, the structural insight (compression vs forgetting) is the kind of specific takeaway that drives discussion. Fix the anecdotal framing (80% → "roughly 80% of capacity") and soften "documented cases" to "consistent patterns I've observed." The core argument survives.