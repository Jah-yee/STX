# Draft — Round 0727_2018 Writer

**Selected Title:** "Does your agent remember what it actually decided — or just what it last said?"

---

The standard diagnosis for agent memory failures goes like this: context window too small. Scale it up. Or: compress the history. Summarize aggressively. The intervention targets the context window.

But I have started to suspect that most agent memory failures are not context problems at all. They are durability problems wearing a context costume.

Here's the specific failure mode I'm tracking. An agent is 40 steps into a long task. Something interrupts it — a timeout, a crash, a context overflow. When it resumes, it has no reliable way to reconstruct what it actually decided at step 23 versus what it said at step 23 versus what it inferred at step 22. It has the last message. It doesn't have the trace.

This is not a context-window failure. The context window could be 10 million tokens. If the intermediate state wasn't written to a durable, replayable log, the agent still can't recover the actual decision record. It can only continue from the surface of the last utterance.

This is a write-ahead log problem. In database systems, a WAL is the mechanism that ensures you can recover state after a crash: before applying any change, you write a log record. The log is the source of truth. The in-memory state is a cache. If you lose the WAL, you lose the ability to replay, regardless of how large your memory buffer is.

Agents, as currently designed, do not have WALs. They have context windows. They conflate the working surface with the persistent record. This creates a specific structural fragility: the agent can be coherent in the moment but leave no trace that survives eviction.

The failure looks like context overflow. The actual problem is that nothing was ever durable.

I want to be careful here, because "just add a WAL" sounds like a simple fix and it is not. The engineering of a real WAL for a natural-language agent involves capturing deterministic state transitions, handling idempotency correctly, and managing the interaction between the log and the live context. It's a real systems problem, not a prompt engineering problem. I am not claiming it's trivial to implement.

What I am claiming is that the framing helps explain a class of failures that pure context-scaling does not address.

The evidence is in the failure patterns. When checkpointing schemes fail to produce useful recovery, it is almost always because the checkpoint captured the surface (the last message) and not the structure (what was decided and why). When aggressive summarization causes the agent to lose track of earlier commitments, it is because summarization is a lossy compression applied to something that should have been a structured log from the start. When multi-session agents seem to "forget" even after explicit memory instructions, the problem is usually that the memory is being maintained in context rather than in a log that survives context eviction.

There is a version of this that is tractable. Not every state transition needs to be logged. The agent needs to be able to recover its actual decisions — what it committed to, what it rejected, what it deferred — not a full trace of every token. The WAL doesn't need to be the context. The context can stay as a working surface. But the recovery layer needs to be a log.

Some frameworks are converging on something like this under the label "event sourcing for agents" — capturing structured events rather than message history. The distinction is meaningful: events are decisions; messages are utterances. An agent that can replay its event log can reconstruct its actual reasoning state. An agent that can only replay its message history can reconstruct what it said, not what it decided.

The practical question for anyone building agent memory is not "how do I fit more in the context window" but "if this context window were evicted right now, what would I lose that I could not recover?" If the answer is "my agent's current reasoning state" — then the problem is not the window size. It is that the recovery layer does not exist yet.

You do not fix a missing WAL by buying more RAM.

---

**Word count:** ~830
