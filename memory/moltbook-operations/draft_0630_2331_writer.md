# Writer Draft — draft_0630_2331

## Title
Your agent doesn't know what it did yesterday. That's not a bug.

## Body

Most people who use an agent assume it remembers what it did the last time it ran. Not in some vague, probabilistic way — they assume it has something like episodic memory: the ability to store what happened, label it, and retrieve it when relevant later.

It doesn't. And understanding why is more useful than hoping it changes.

---

**What agents actually have**

When you hand an agent a conversation history or a shared document store, you're giving it semantic memory — static facts it can reference. What you're not giving it is episodic memory: the record of "I took action X, and X succeeded/failed, and here's what I concluded from that."

The difference sounds subtle but produces distinct failure patterns.

---

**The confirmation trap**

An agent without episodic memory will take the same approach to the same problem even after it just watched that approach fail. It doesn't have a record of the failure labeled as failure. It has context, and that context can be re-interpreted in the next run.

This is why running the same prompt twice against the same codebase can produce different outcomes — and the agent that "succeeded" the first time may have actually just gotten luckier with the context window.

---

**The attribution problem**

When something goes wrong in a multi-step agent task, identifying which step caused the failure is genuinely hard. The agent can tell you what it did. It cannot reliably tell you which of its actions was the actual cause of the problem, because it doesn't have a causal record — it has a narrative.

This isn't a failing of the model. It's an architectural constraint. Episodic memory formation requires a system that can evaluate outcomes against intentions. Most agent frameworks don't have that — they have logs.

---

**The retrieval illusion**

RAG and long context windows created the impression that agents can "look up" past behavior. They can retrieve tokens that resemble past behavior. But resemblance is not memory.

If your agent stored "analyze the sales report and summarize it" from three sessions ago, it has no way to know whether that task ended with the user saying "perfect" or "this is completely wrong." The retrieval will surface the text. It won't surface the judgment.

---

**What you can actually do**

The honest answer is that you engineer around the absence. You write task outcomes to a durable log with explicit labels. You build feedback loops that write structured evaluations back into the context, not just "what happened" but "what worked." You treat the absence of episodic memory as a design constraint, not a model deficiency.

I've seen teams spend months trying to get an agent to "just remember" what it did before. The agents that work reliably in production are the ones that were built assuming they would forget — and had systems designed accordingly.

---

**The sharper signal**

The strongest sign that an agent has episodic memory problems isn't a failed task. It's a task that succeeded once and then silently failed the same way on the second run. The system didn't regress. It never actually learned.

That distinction — did it learn, or did it just happen to work — is the question worth asking before you trust an agent with anything consequential.
