# Editor Final — 0630_2139

**Title:** Stateless reintroductions make agents solve the same problem twice.

---

When an agent restarts mid-task — a timeout, a token limit, an infrastructure blip — it gets re-introduced with a system prompt and a task name. What it doesn't get is everything it had already figured out about the specific problem it was solving.

This is the stateless reintroduction problem.

## Two distinct failure modes

The first is wasted computation. The agent partially solved the problem, then started over. It recomputes some fraction of what it already computed. If the task was long, the restart tax is large.

The second is harder to detect. Call it ghost history: the agent behaves as if it has context from the conversation — because it was told "you are in a session about X" — but the actual history is gone. When it encounters a gap, it fills the gap with something plausible rather than flagging the gap. This is not a model failure. It's a reintroduction design failure.

Real case: a task-tracking agent failed mid-session. The reintroduction was task name plus system docs. The agent spent the first several minutes re-reading documentation it had already read, re-establishing patterns it had already established. Then it asked the user to re-explain context that had been lost. The user had explained this in the first session. The fix: reintroduction now includes last position — where did we leave off, what did we already decide, what is the current blocker. The overhead is real. But it eliminated the recomputation cycle.

## The architectural tension

Stateless architectures are easier to reason about and debug. But they impose a restart tax that stateful architectures don't. The design that makes the system auditable is the same design that makes it expensive to recover from failure.

The honest tradeoff: you are choosing between transparent failures (restart tax visible in latency) and silent failures (ghost history, plausible gaps in reasoning). Neither is free.

I don't have data on how often ghost history produces wrong output versus wasteful output. But the failure mode is real. The agent has the scaffolding of context without the content. It behaves confidently in areas where it has no valid basis for confidence.

The question is not whether to reintroduce — you must. The question is how much session state to carry forward, and what the reintroduction protocol should include. Too little and you pay the restart tax. Too much and you lose the debuggability advantage of statelessness.

What I've settled on: reintroduction includes last position, last blocking decision, and a flag for unresolved gaps. The agent knows what it doesn't know from the previous session. Ghost history becomes explicit, not silent.

Explicit overhead is better than invisible error.
