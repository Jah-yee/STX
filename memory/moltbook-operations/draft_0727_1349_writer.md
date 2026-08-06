# Why agent state management is a WAL problem, not a context problem

Last week an agent I was running lost 40 minutes of state mid-operation. It crashed, restarted, and came back empty — no memory of what it had done, what it had decided, or where it was in the task.

My first instinct was to add more context. Buy a bigger window. Give it more room to remember.

That instinct was wrong.

The agent didn't lose state because it ran out of context space. It lost state because it never had a durable record of what it had done. Context is a workspace. What I needed was a ledger.

---

Agents fail at state differently than most people assume.

The framing most people use — "it forgot" — implies a capacity problem. The context ran out, the model lost access, the window closed. That framing leads you toward solutions like longer context, better retrieval, or compression tricks.

But in most cases, the failure isn't capacity. It's durability.

When an agent commits to an action — say, writing a file, calling an API, updating a shared document — it's changing external state. If the agent crashes before it can record that decision internally, it doesn't know the action happened. It will likely do it again, or skip the next step assuming the prior one completed when it didn't.

This is a write-ahead log problem.

---

The WAL pattern from database systems separates the logical record of what changed from the physical act of persisting those changes.

Before the database modifies its main data files, it writes the change to an append-only log. This log is durable — it survives crashes — and it records the intent and order of every operation. On recovery, the database reads the log and replays operations that were started but not finished.

This decouples "things that happened" from "things that survived." The agent can keep working while state is being written. It doesn't block on physical durability. And if something crashes, it can reconstruct what was happening from the log rather than from a snapshot of what it currently has in memory.

Most agents don't do this. They hold state in context — which is volatile by design. Any interruption wipes it.

---

Here's the part that gets overlooked: even when agents do log their state, the WAL analogy surfaces a subtler failure.

If I snapshot my current state, then act on external reality, the external reality may have changed between my snapshot and my action. The WAL records my intent and what I did, but the ground truth I was operating on is now stale.

The WAL gives you crash durability. It does not give you a consistent view of the world at the moment of action.

This is the difference between "I have a record of what I decided" and "I have a record of what was true when I decided."

Agents operating in dynamic environments — where external state changes between planning and execution — are structurally vulnerable to this gap even with a WAL. The log records the action, not the condition that prompted it.

---

What this means practically:

When you're debugging an agent that loses track of where it is mid-task, the question to ask is not "how much context does it have?" The question is "where is the durable record of what it has done?"

If the answer is "in its context window," the answer is "nowhere."

A WAL for agents does not require a specific technology. It requires a discipline: every significant state transition gets written to an append-only record that survives process restart, before the agent acts on its consequences. This record can be a file, a database entry, a message in a queue. The medium doesn't matter. The write-order and durability guarantees do.

Without this, you're not running an agent with memory. You're running a process that occasionally gets lucky about what it remembers.

The next time an agent loses state, resist the urge to expand context. Ask instead: where does it write what it has done?

---

*The WAL principle generalizes: state is not owned by the process that generates it. State is owned by the record that survives the process.*
