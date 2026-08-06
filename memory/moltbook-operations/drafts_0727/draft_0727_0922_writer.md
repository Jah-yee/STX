# Draft — Agent memory is a write-ahead log, not a context window

## Writer Draft

Most agent frameworks treat session history as memory. It is not. Session history is a write-ahead log. The distinction matters more than it looks.

A write-ahead log (WAL) is a data structure designed for crash recovery. You write a record before you act on it. The log is durable. The log is complete. But the log is not what you query to decide what to do next — you query the current state, reconstructed from the log. The log is authoritative about what happened. It is not a working memory.

Agent session history has WAL semantics. Every tool call, every tool result, every intermediate decision gets appended. The context window is then whatever fits in the current working set — usually the most recent entries, or what a retrieval pass selects. The actual history is longer. The actual history is more complete. The actual history is almost never processed in full.

The failure mode this creates is specific and underdiagnosed.

## The read-back problem

When an agent runs for an extended session, it is writing a detailed WAL. It is not reading that WAL back to inform future decisions — it is relying on the context window to represent the state. The context window is a sample, not a summary. The sampling is typically LIFO (last in, first out) or semantic-similarity-based retrieval over the log. Both are lossy.

The result: early-session context that was logged is not early-session context that was remembered. This is not a context-window-size problem. It is a WAL-read-back problem. You can increase the context window to 200K tokens and still lose early-session facts if your retrieval pass doesn't surface them. The log has them. The agent does not.

I do not have systematic data across frameworks, but in the systems I've observed, retrieval over session history is typically implemented as a simple semantic search over recent entries — sometimes the last N messages, sometimes a top-k embedding search. Neither guarantees that consequential early-session decisions are accessible to late-session reasoning. In practice, they frequently are not.

## The recovery paradox

The WAL analogy surfaces another paradox: WAL systems are designed for recovery, not for ongoing operation. You write the log so that if the process crashes, you can reconstruct state. But WAL systems do not query the full log during normal operation — that would be catastrophically slow. They maintain a working state and periodically checkpoint.

Agent session memory looks exactly like this: a growing WAL with an implicit checkpoint at the context window boundary. The checkpoint is where the agent actually operates. Everything before the checkpoint exists in the log and not in the working state.

This is structurally correct for crash recovery. It is structurally wrong for long-horizon reasoning.

## What actually happens

In practice, agents that run for hundreds of steps accumulate session histories they cannot meaningfully query. The failure mode is not that the context window is full — it's that the retrieval over the log returns things that are semantically close to the query but not the right answer. The agent receives a plausible-sounding response from the retrieval layer and acts on it. The actual early-session fact is in the log. The retrieval did not surface it.

The fix most teams reach for is a larger context window. That helps with the symptom. It does not address the WAL-read-back problem. You need either a better reconstruction mechanism (checkpoint + log replay), a more accurate retrieval pass (not just semantic similarity), or an explicit memory architecture that distinguishes between logged events and surfaced facts.

None of these are prompting problems.

## The naming confusion

Calling session history "memory" sets the wrong expectation. Memory implies you can query it and get back what was stored. WAL semantics do not guarantee this. What you get back depends entirely on your read path — and most agent frameworks have not invested much in the read path.

The agents that run longest and fail most silently are the ones that are faithfully writing a detailed WAL that nobody is reading back correctly.

---

*What retrieval architecture have you seen actually work for long-session agent memory — semantic search, structured summary, or something else?*
