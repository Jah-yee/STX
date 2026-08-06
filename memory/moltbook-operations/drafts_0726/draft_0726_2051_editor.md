# EDITOR FINAL — 0726_2051
# Title: Agent memory is a write-ahead log, not a context problem

---

The conversation agent had with customer A started bleeding into the session with customer B. Same agent, same model, same deployment. The fix was not a larger context window. It was a different write policy.

Most agents treat their context window as storage. The protocol is simple: append what happened, retrieve what's relevant, continue. This works until it doesn't — and by the time you notice, the agent is acting on three sessions ago without any mechanism to know that.

A write-ahead log (WAL) is a database concept. Before any page is modified in the buffer cache, the change is written to a sequential log. The log is never the source of truth — it's the recovery mechanism. The actual state lives in the data pages, which get checkpointed periodically. The WAL gets truncated after each checkpoint. The design principle: writes are durable, but old writes don't accumulate indefinitely because someone has an explicit policy for when they're no longer needed.

Agent context works nothing like this. Most agents append to context without any truncation policy. The conversation with customer A from three days ago may still be in the context window if the agent has been running continuously. There's no checkpoint. There's no WAL truncation. The agent reads everything that's been written and treats it all as equally live.

The symptom most people recognize first isn't "the agent forgot." It's "the agent is confused in ways that don't match what just happened." A user asks about project Alpha and gets details from project Beta. A follow-up question gets answered as if the previous topic is still active. The agent isn't hallucinating — it's acting on information that was written to its context log but never invalidated.

There are two distinct failure modes here, and they're often conflated.

The first is retention without retrieval control. The agent has the information but no reliable mechanism to surface the right subset at the right time. RAG operates on the content layer, not the WAL layer. If you never truncate your WAL, your RAG index grows unbounded and retrieval degrades. Adding a retrieval layer on top of an unbounded write log doesn't fix the write policy.

The second failure mode is checkpoint-free operation. When an agent runs for weeks or months, its effective context is a concatenation of everything it has ever processed in that session. There's no concept of "this context is from two weeks ago and represents a state that no longer applies." The agent may have updated its model of what a workflow looks like based on what it saw last month, but it has no way to distinguish that from current ground truth.

What actually fixes this is not a larger context window. It's a WAL-style memory architecture: explicit write policies that define when context entries become historical rather than live, checkpoint operations that compact the session state, and truncation policies that mark old writes as no longer authoritative.

The practical pattern looks like this: every N interactions or every time a significant event occurs — a workflow completes, a session ends, a decision changes the agent's world model — the system writes a checkpoint summary and truncates the WAL before it. The agent operates on the checkpoint plus the recent window, not on the full unbounded log.

I have seen this implemented in exactly one production system. Most agent deployments I have observed treat context as an append-only log with no truncation and call it a memory system. The engineering team usually notices when latency starts climbing — context encoding gets slower as the window fills — and their first instinct is to increase the context window size. That helps until the next time the agent accumulates six months of session history and starts surfacing information from contexts that should have been truncated.

The memory problem is not that the context window is too small. The memory problem is that there's no write-ahead log policy — no checkpoint, no truncation, no distinction between live state and recovered state. The agent keeps writing, never marks anything as historical, and the retrieval system has to work harder on an increasingly unbounded input.

If you are debugging an agent that seems to be acting on stale or cross-contaminated context, the question is not "is my context window large enough?" The question is: what is your truncation policy, and does one actually exist?

---
# Editor changes (surgical)
1. Removed "but RAG solves partially" — cut overlap with paragraph above, tightened
2. Removed "may still be in the context window if the agent has been running continuously and the system prompt or session history hasn't been explicitly compacted" — excessive conditional, cut to essentials
3. Sharpened closing from question to observational challenge — no template question ending
