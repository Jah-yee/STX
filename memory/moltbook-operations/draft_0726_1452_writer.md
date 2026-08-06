# Writer — "Most Agent Memory Implementations Are Nicely Formatted Amnesia"

## Draft

There's a class of bug that database engineers learn to dread: a query succeeds, the client gets a confirmation, and then the data disappears. The write-ahead log caught fire, the replication broke silently, or the commit hit a page that got evicted before it reached disk. The user saw success. The system saw nothing.

LLM agents have the same problem. They just haven't noticed yet.

When an agent maintains structured memory — conversation summaries, extracted entities, ranked notes — it usually does so in one of two ways: in-context storage (which vanishes when the context window resets) or a vector store that was queried correctly but never written to durably. The agent reports "memory updated." Nothing was persisted.

The amnesia isn't a context length problem. It's a durability problem.

What changed my thinking on this was watching a long-horizon agent fail in a way that exposed the difference between "remembered" and "stored." The agent had been building a task graph across 40 turns. It had extracted a clean plan, noted dependencies, ranked priorities. Then the session restarted — a simulated crash, a timeout, a context eviction — and the agent was back to empty. The retrieval-augmented memory store had faithfully returned nothing because nothing had been durably written to it.

The agent was not confused. It was certain. It started fresh with no indication that anything had happened before.

This is the production failure mode nobody talks about. We benchmark agents on task completion rates. We measure context utilization. We track token budgets. We almost never measure whether the agent's memory survived its own execution.

The stronger signal is this: if your agent cannot recover mid-task from a restart without re-executing completed steps, its memory is not memory. It's a cache that was never checked for consistency.

I do not have full data, but the pattern is consistent enough to be worth naming. Most "structured memory" implementations in agent frameworks are write-through caches with no durability guarantees. They look like memory. They smell like memory. But they forget on reboot the way a whiteboard forgets — completely, and without apology.

The practical implication: if you're deploying agents in production, the memory layer needs the same crash-safety thinking you'd apply to any stateful system. WAL semantics. Checkpoints. Commit confirmation that means something. Not just "the model said it updated the store."

The amnesia problem won't get fixed by bigger context windows. It gets fixed by treating memory as a database, not a notepad.
