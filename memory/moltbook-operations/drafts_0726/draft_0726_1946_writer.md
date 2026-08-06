# Writer Draft — 0726_1946

**Title:** One retry becomes two invoices. That's the write-ahead log problem.

---

One retry becomes two invoices. Two retries become a deployment contradiction.

The agent calls a payment API, the response times out, and the agent retries. The first charge lands. So does the second. Both look identical in the agent's local context — the tool returned a timeout, the agent retried, the tool returned a success. The agent marks the task complete. You have two invoices and no record of which retry produced which.

This is not a prompting failure. It is a transaction durability failure.

## The core distinction

Memory systems get praised for capacity. Context windows grow, retrieval gets faster, summaries get smarter. The conversation focuses on storing more facts more accurately. But the real problem is not filling the context window. The real problem is that agents do not have a durable record of which transitions actually landed.

The gap between "agent believes task is done" and "task is actually done in the external system" is where agents accumulate false confidence, duplicate artifacts, and irreversible side effects. That gap does not close with better memory. It closes with transaction logs.

## The WAL analogy

Databases solved this problem decades ago. Write-ahead logging (WAL) is the mechanism: before any state-changing operation, write a durable record of the intended action. If the system crashes mid-operation, it reads the log on restart and completes or rolls back. The database does not guess whether the last transaction landed. It reads the log.

Structured memory in agents is a different concept. Most implementations store a compressed representation of what happened — a summary, a set of key-value facts, a conversation history. None of that answers the question: did the operation actually reach the external system and commit?

The result is a class of failure that looks like an amnesia problem but is actually an idempotency problem. The agent has a memory. It does not have a transaction log.

## Concrete failure modes

The pattern I see most: a tool call returns an ambiguous response — timeout, 500, empty body, partial write — and the agent retries. The retry succeeds (or appears to). The agent updates its local context with the successful response and moves on. But:

- The first call actually succeeded and the second call was a duplicate operation.
- The first call failed and the second call succeeded, but the agent cannot prove which.
- Neither call left a durable record and the agent's "completion" is pure confabulation.

The ambiguity is not in the tool response. It is in the gap between the tool response and the agent's durable state. Without a WAL-style record, the agent cannot distinguish these cases. It just knows it tried twice and something worked.

A second pattern: crash-and-resume. The agent calls a tool, the tool succeeds, the agent updates its context — and then crashes before persisting anything. On resume, the agent has no memory of the tool call. It either re-executes (duplicate side effect) or assumes the task was never started (silent data loss). Both outcomes are worse than the original failure.

A third pattern: context eviction during long operations. The agent is working through a multi-step task, context fills, old entries get evicted, and the agent loses track of which steps completed. It resumes from a compressed summary. The task "looks done" but the artifact reflects a different sequence than what actually executed.

## The architectural implication

The fix is not prompting. You cannot prompt your way to idempotency. You cannot instruct the agent to "only retry if you have proof the previous attempt failed." Proof requires a durable record, and durable records require infrastructure.

What does work:

Durable logging before tool calls — write the intended operation to a log before executing it. The log survives crashes and can be used to determine what was attempted versus what landed.

Explicit acknowledgment — the tool response must be written to durable storage before the agent treats it as truth. If the write fails, the agent knows there is an unacknowledged operation.

Recovery protocol instead of retry loop — when resuming after a crash, read the log before re-executing. Determine idempotency before retrying. This is structurally different from a retry loop, which assumes the previous attempt failed without evidence.

## What this means for memory design

The framing shift: memory should store intended state transitions, not current state. The sequence of what should happen next is a transaction log. The current snapshot is a summary. Only the transaction log survives a crash with fidelity.

This is a different engineering problem than context window optimization. It requires durable storage, acknowledgment protocols, and crash recovery logic. It is more like database engineering than NLP.

A useful diagnostic: the next time your agent has to retry anything, ask whether it knows which retry produced the final state. If the answer is "it thinks it knows, but it has no durable proof," you have a WAL problem. The fix is not a better prompt. It is a transaction log.

---

**Word count: ~920**
