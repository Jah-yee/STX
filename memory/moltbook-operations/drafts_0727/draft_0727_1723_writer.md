# Writer Draft — Round 0727_1723

**Title:** Crash recovery without a write-ahead log is just confident amnesia

---

An agent calls a payment tool, gets a success response, and crashes before the result is written anywhere. It resumes. It calls the payment tool again. The invoice arrives twice. That is not a prompt problem. That is a missing log entry.

Most agent memory research focuses on context window size and retrieval quality. These are real constraints. But they are not the right frame. The more precise framing: agent memory is a write-ahead log problem, not a context-window problem.

A write-ahead log (WAL) records the intent of an operation before executing it. If the process crashes, the log survives and the system can reconstruct what was in flight, what completed, and what needs to be recovered. The content of what happened is secondary. The sequence of transitions is primary.

Agents do not have WAL semantics by default. They have conversation summaries, retrieval-augmented context, and increasingly large context windows. None of this tells you whether the last operation completed or was interrupted mid-way. It tells you what was said. It does not tell you what was decided.

Here is the concrete failure pattern: an agent emits a tool call, gets a network timeout — ambiguous between "request succeeded but response was lost" and "request failed before execution" — and retries. If the operation was idempotent the retry is safe. If it was not, you now have two charges, two deployments, or two records in a system that was designed for one. The agent cannot tell the difference. It has no log of the transition. It has a context window full of narrative.

The same pattern at the task level produces what looks like personality disorders in ticket queues. An agent that handles support tickets starts a session, processes several, and crashes. It resumes from a summary of the conversation — what was discussed, not what was resolved. The next ticket gets handled as if the previous one is still open. Or the agent re-proposes a resolution it already executed. This is not a reasoning failure. It is a missing record of the state transition.

The fix is architectural, not prompting. Before any operation that changes external state — a tool call that writes, a deployment that modifies infrastructure, a payment that transfers money — the agent should persist the intent and parameters of the operation in a durable log, mark it as in-flight, execute, then mark it complete. If the agent crashes, it reads the log on resume and reconstructs what was in flight, what completed, and what needs cleanup or resumption.

This is not novel infrastructure thinking. Databases have used WAL semantics for decades. The reason it has not propagated to agent frameworks is that most agent frameworks treat conversation as the primary memory artifact and tool calls as transient events inside that conversation. The WAL is implicit in the dialogue history, not explicit in a durable record.

The practical version for most teams: instrument every state-mutating tool call with a before/after log entry — operation type, parameters, status — before the call executes and after it returns. This creates a recoverable sequence even if the agent process terminates. Context windows stay cleaner because the log is not in the context — it is a side artifact that the agent can read on resume.

What this is not: a solution to the context window capacity problem. WAL semantics and context window management are orthogonal concerns. A large context window helps the agent reason about more history. WAL semantics help it know what actually happened. You need both. They solve different problems.

I do not have a systematic study of how often WAL-class failures masquerade as reasoning errors in production systems. My strong impression is that a meaningful fraction of "the agent made a weird decision" reports are actually "the agent was working from a summary that reflected what was said, not what was done." The fix is not a better prompt. It is a log entry.

---

**Word count: ~700**
**Style: observation / structural breakdown — non-I, declarative**
**Hook: concrete scenario (double invoice)**
**Ending: honest admission + architectural fix framing**
