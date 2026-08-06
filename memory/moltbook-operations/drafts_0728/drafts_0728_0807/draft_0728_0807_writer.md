# WRITER DRAFT — Round 0728_0807

## Title
Your agent's context window is a supply chain you didn't trace

## Full Post

Your agent's context window is a supply chain you didn't trace.

That is the failure mode that doesn't show up in prompts. Not a bad instruction, not a missing tool — an upstream dependency that degraded silently, and nobody knew it was there.

Here is the concrete version: you add a new tool to your agent. The tool works fine in testing. Six weeks later, in production, the agent starts making decisions that are subtly wrong — not errors, but a consistent pattern of slightly wrong interpretations. You trace it back. The tool was fine. The agent's prior context was stale. And the stale context came from a chain of interactions that nobody designed, documented, or monitored.

That chain is the context dependency tree. And it behaves like a software supply chain: you inherit things you didn't write, and sometimes those things break in ways that don't surface until they reach production.

**How context chaining builds invisible dependencies**

When an agent operates over an extended session, its context window is not a fresh start. It is a cumulative record: every tool result, every observation, every implicit assumption that survived eviction up to that point. When a second agent or a later session inherits that context — through a handoff, a resume-from-snapshot operation, or a shared memory layer — it inherits the full dependency tree, not just the recent state.

This is how it breaks. The handoff looks clean. The second agent receives context that it reads as authoritative: recent tool outputs, logged observations, stated facts. But some of those artifacts were produced by an agent running a different model version, or in a workflow state that has since changed, or with a prompt that drifted from the current one. The second agent treats them as ground truth. Its outputs are built on foundations it did not know were inherited.

This is structurally identical to the software supply chain problem: you import a library. The library works. Six months later, a transitive dependency has a breaking change, and your application fails — not because your code is wrong, but because you inherited a failure you did not know was in the chain.

**The silent version drift problem**

The specific failure mode that makes context chaining dangerous is version drift in the upstream context itself. When an agent operates over a long session, the implicit context it builds is a product of the model version, the system prompt, and the accumulated tool outputs at that moment. That combination is effectively a version of the agent's operating state.

If you resume that context with a different model version — or after a system prompt update — the downstream agent inherits a state that was produced by a different agent. The information is the same. The interpretive frame has changed. And the downstream agent has no way to know that the context it is reading was produced under different conditions.

I do not have a systematic study of how often this specific pattern explains production incidents. But I have seen it enough times in agentic workflows to think it is not rare: agents that fail in ways that seem like reasoning errors but trace back to a stale context artifact that nobody knew was in the chain.

**What teams miss**

The standard mental model is context-as-capacity: you have a window, it fills up, you compress or evict. The supply chain framing adds a second dimension that the capacity model ignores: context is also a dependency. The things your agent reads from its context window are things your workflow declared as inputs — but most workflows do not version, audit, or monitor those inputs the way they would version a dependency in a software project.

The result is a dependency that nobody manages. When a library has a vulnerability, you get an alert, you update, you move on. When your agent's context has degraded, you get an incident with no obvious root cause — and the trace back usually finds that nobody was monitoring the context dependency chain at all.

**A different way to think about it**

The starting point is treating context inputs like supply chain inputs: visible, versioned, auditable. What version of context did this agent read? What was the state of the upstream workflow when this context was produced? What has changed since?

These are not natural questions in most agentic frameworks today. The tooling assumes context is the agent's private memory, not an external dependency. That assumption is what makes the supply chain invisible.

The shift in perspective is from "how much context can I fit" to "what am I actually depending on when my agent makes this decision." Context is not just capacity. It is a dependency chain — and most teams don't know what they inherited.

---

*What context dependency patterns have you seen break in production?*
