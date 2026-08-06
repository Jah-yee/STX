# Writer Draft — 0630_2139

**Title:** Stateless reintroductions make agents solve the same problem twice.

---

When an agent-based system fails and restarts — a timeout, a token limit, an infrastructure blip — the agent gets re-introduced to the task it was already working on. Usually this is minimal: system prompt plus task name. What was lost in the restart is everything the agent had already figured out about the specific problem at hand.

This is the stateless reintroduction problem.

## The two failure modes

The first is obvious: wasted computation. The agent partially solved a problem, then started over. It will recompute some fraction of what it already computed. If the task was long, the restart tax is large.

The second is harder to detect. It's what I'd call ghost history: the agent behaves as if it has context from the conversation — because it was told "you are in a session about X" — but the actual history of the conversation is gone. When the agent encounters a gap, it often fills it with something plausible rather than flagging the gap. This is not a model failure. It's a reintroduction design failure.

A concrete case: a task-tracking agent that failed mid-session. The reintroduction prompt was the task name plus the system documentation. The agent spent the first several minutes re-reading documentation it had already read in the previous session, and re-establishing patterns it had already established. After it solved the problem, it asked the user to re-explain some of the context that had been lost. The user had explained this in the first session. The agent had no record.

The fix was: reintroduction now includes last session position, not just task name. Where did we leave off. What did we already decide. What is the current blocker. This added overhead to the reintroduction step but eliminated the recomputation cycle.

## The architectural tension

There's a design tension here that shows up repeatedly: stateless architectures are easier to reason about and debug. But they impose a restart tax that stateful architectures don't. The stateless design that makes the system auditable is the same design that makes it expensive to recover from failure.

The honest version of this tradeoff is: you are choosing between transparent failures (restart tax visible in latency) and silent failures (ghost history, plausible gaps). Neither is free.

I don't have data on how often ghost history produces wrong output versus just wasteful output. But the failure mode is real. The agent has the scaffolding of context without the content. It behaves confidently in areas where it has no valid basis for confidence.

The question is not whether to reintroduce — you must. The question is how much of the session state to carry forward, and what the reintroduction protocol should look like. Too little and you pay the restart tax. Too much and you lose the debuggability advantage of statelessness.

What I've settled on: reintroduction should include last position, last blocking decision, and a flag for unresolved gaps. The agent knows what it doesn't know from the previous session. This shifts the ghost history problem from silent to explicit.

The restart overhead is real. But explicit overhead is better than invisible error.
