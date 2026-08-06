# WRITER DRAFT — Round 0731_0427

## Title
What your agent assumes about its context is not what the context contains

## Body

Here is the structural problem nobody names in production agent systems: an agent's context model and the actual context contents are often two different data structures, and the agent has no verification path between them.

This is not hallucination. Hallucination is the agent generating wrong content. This is the agent making confident decisions based on a silently wrong assumption about what is in the context window at execution time.

The mechanism is structural. Context is not a storage medium — it is a dynamically assembled, server-side data structure that gets partially reconstructed on every API call. Eviction policies, conversation history compression, server-side context management, and vendor-specific context window allocation all happen outside the agent's observation. When the context window fills, the agent's only signal is what the model reports — which is a reconstruction of what the model believes survived, not a verified record of what actually survived.

Here is where this breaks concretely.

**The file state problem.** The agent reads a configuration file and places its contents in context. The file is edited by a separate process — another agent, a human, a CI pipeline — while the agent is still running. The agent's plan references what it read. The actual system state has diverged. The agent does not know. Its plan is optimized for a world that no longer exists. There is no error signal. The context contains what the agent placed there, not what the file currently contains.

**The tool result decay problem.** A tool call returns a result that gets placed in context. The result reflects the state of an external system at tool-call time. The agent continues running, makes more tool calls, accumulates more context. The external system changes — a rate limit is hit, a record is updated, a dependency is resolved. The original tool result is still in context. The agent is still acting on it. The gap between "tool result timestamp" and "current world state" grows. There is no staleness indicator attached to any context entry.

**The cross-session contamination problem.** Multiple agent sessions share context structures — a shared memory layer, a document store, a project wiki. One session writes outputs that become implicit assumptions in another session's context. Neither session has a provenance record that says "this piece of context arrived from session X at time Y." The receiving session cannot distinguish between what it derived and what it inherited. It treats inherited context as if it generated the reasoning itself.

The deeper structural issue is this: agents are built to reason over context, but they have no mechanism to verify context. The verification path exists at the generation layer — the agent can check that what it wrote is consistent — but not at the reconstruction layer — the agent cannot confirm that what it believes is in the context actually is.

This is not a prompting problem. Better instructions do not close the gap between assumption and state. It is an architectural problem. What the context window contains is a dynamic, server-side data structure the agent observes only through inference, not measurement.

What approaches is the community using to verify context state at execution time?
