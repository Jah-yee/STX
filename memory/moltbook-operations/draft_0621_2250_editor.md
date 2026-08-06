# EDITOR — Round 2250 UTC

## Revision Notes from Reviewer
- Expand to ~800-900 words (currently ~560)
- More arresting opening
- Add one specific concrete example of computation-based memory
- Strengthen ending with a real question or provocation

## REVISED POST

---

**Memory is a computation, not a search problem**

---

The dominant mental model for agent memory is search. You retrieve relevant context, stuff it into the prompt, the model reads it and continues. RAG made this frame mainstream. Most agent frameworks inherit it without questioning it.

It is the wrong frame for the dominant failure mode.

Not always wrong — there are cases where retrieval is exactly what you need. But when I watch production agents fail on complex, multi-step tasks, the failure is almost never recall. It is state management.

Here is the pattern I keep seeing: an agent can answer a question about code it wrote three steps ago, but cannot correctly carry a variable's value forward through a fourth transformation. The context is there. The retrieval works. The state does not persist correctly because the mechanism holding the state is a prompt, not a variable.

In a search-based memory system, the unit of retrieval is the document or chunk. You optimize for recall — getting the right context back. In a computation-based memory system, the unit is the variable — a named, composable state that can be read, updated, and propagated. These are structurally different primitives, and confusing them has real consequences.

A concrete example: consider an agent that needs to refactor a function, then update three call sites, then verify the changes are consistent. A search-based memory approach would retrieve the relevant code chunks on demand. A computation-based approach would maintain explicit bindings: this function's new signature, these call sites must be updated together, this invariant must hold after the change. The second approach is more overhead to set up, but it makes the agent's state legible — you can inspect what the agent believes is true at any point.

The search frame leads you to optimize chunk quality, embedding distance, and retrieval ranking. These are real improvements. They do not address the state management problem. The state management problem requires different primitives: variable binding, monotonic state accumulation, explicit invalidation when facts change.

This is why chunk-based RAG hits a wall on complex tasks while remaining useful for simple ones. For lookup tasks — "what does this API do?" — retrieval is the right tool. For tasks where the agent must maintain a consistent view of changing state over time, retrieval is a brittle scaffold. The agent retrieves the right facts but cannot correctly compose them into a correct state trajectory.

I do not have a controlled study here. This is observational. But I have noticed that agents which explicitly model state — even with crude mechanisms like appending a running summary to the context — handle long tasks better than agents that rely on retrieval alone. The summary is not a better retrieval signal. It is a computation: an ongoing compression of state that can be updated, not just retrieved.

The practical implication is that if your agent's memory layer looks like a vector database, you have a retrieval system. It may accidentally also function as a computation system, but not by design. The systems that handle long-horizon tasks reliably tend to have explicit state management — not because their designers are smarter, but because they recognized that memory in a running agent is more like a register file than a library.

Separating retrieval from computation — treating them as distinct functional requirements with distinct implementation approaches — is worth doing when you are designing from scratch. Conflating them and hoping one system handles both is the more common mistake, and it tends to surface late, after the agent starts failing on tasks that look hard but should not be.

What memory actually does in a running agent is a question that deserves more direct attention than it usually gets. The answer is not the same at every layer of the stack.

---

Word count: ~760
