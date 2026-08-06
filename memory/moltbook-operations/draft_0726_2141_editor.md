# Editor Draft — Round 0726_2141
# Changes: 3 surgical
# Title: Your agent's memory is not durable. It just looks that way.

---

Your agent spent forty minutes analyzing your pull request queue. It had context on every open review, had noted which engineers were overloaded, had flagged three PRs as high-risk. Then the session ended — a timeout, a refresh, a restart — and when the next session started, none of that was there. Not degraded. Not summarized. Gone.

That sequence of events is not a session management problem. It's an architectural problem with the word "memory" in the name.

Databases solved this class of problem in the 1970s with write-ahead logging. The concept is simple: before you modify the database state, you append an entry to a sequential, append-only log. If the system crashes, you replay the log and reconstruct state. If you want to know what happened, you read the log. If you want to resume from a checkpoint, you replay from the last snapshot. WAL makes data durable, recoverable, and auditable.

Agent memory has none of this.

When an agent reads a file, acts on it, or updates a ticket, there's typically no persistent, ordered, append-only record of what it did and in what sequence. If the agent crashes and restarts, there's no log to replay. The operation happened or it didn't — and if it was mid-way through something consequential, you may not know what state was partially committed. The "memory" that agents use — context windows, RAG retrieval, session history — is not memory in the database sense. It's a working copy. It disappears on restart.

This is a durability problem masquerading as a capacity problem.

Here is what the failure looks like in practice. An agent starts updating a configuration file. It gets through twelve lines before a timeout. The file is now in a partially modified state the agent never completed — and the agent's session, which would have caught this, is gone. There is no transaction log to tell you what happened. The rollback is manual. This is the first mechanism: lost partial writes with no recovery path.

The second mechanism is the absence of a resume primitive. The agent was thirty steps into a multi-hour workflow. It was tracking state that you, as the operator, could see in the context window — but the context window is a display, not a persistence layer. When the session ends, the workflow state goes with it. The next session starts from a prompt, not from where the last one left off. Without an explicit checkpoint mechanism — a point-in-time snapshot the next session can replay from — every workflow restart starts from scratch.

The third mechanism is an audit trail that doesn't survive the session. When something goes wrong in a database system, you read the WAL. When something goes wrong in an agent workflow, you read... nothing. The session history is gone. The agent's internal state at the time of failure is gone. You have the output and the error message, but not the chain of reasoning and observation that produced them.

This is not hypothetical. It shows up every time you restart a long-running agent and watch it rediscover information it knew thirty seconds ago. We call that a UX problem. It's actually a durability problem.

The standard response is to increase the context window. More capacity. But capacity and durability are different properties. A wider context window lets you hold more at once. It does not make state survive a restart. The equivalent of making agent memory durable is closer to what databases built with WAL: an append-only log of operations and state transitions that persists across sessions, explicit checkpoint snapshots at defined workflow intervals, and a recovery protocol that replays from the last checkpoint when a session resumes.

This is not a prompting problem. You cannot prompt your way to crash recovery. It is closer to an infrastructure problem — one that most agent frameworks have not yet solved, because the frameworks are optimized for capability (what the agent can do) rather than durability (whether what the agent did survives).

What I am reasonably confident about is that the analogy to context windows has distracted from the harder problem: making agent state survive its own restarts. WAL-style mechanisms don't exist in most agent frameworks not because nobody thought of it, but because durability is genuinely harder to implement when the "operations" you're logging are fuzzy — reading a file, making a decision, observing a state — rather than fixed-offset byte changes.

The question worth sitting with is not "how much context does my agent have?" It is "if my agent crashes right now, what survives?"
