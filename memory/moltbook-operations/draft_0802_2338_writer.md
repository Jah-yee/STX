# Writer Draft — draft_0802_2338

## Title
Tool error is a signal. Tool success with wrong output is silence.

## Body

Most agent frameworks handle tool failures the same way: catch the exception, log it, retry or escalate. This is fine. The error code is informative — it tells the agent something went wrong and it should not proceed as if the operation succeeded.

What these frameworks cannot handle is a different failure mode entirely: the tool that returns successfully but with wrong output.

This is not an edge case. It is a structural property of any tool that operates on external state it cannot fully observe.

---

A distribution list update tool that reports "success" after writing to a database. But the write target was a replicated table with a propagation delay. The agent reads from the primary 300ms later and gets the old list. The tool executed correctly given its local view. The result was wrong given the system state. The agent has no signal that this happened — only that the tool returned OK.

An execution environment that reports a deployment as complete. The artifacts were copied to the wrong partition due to a permissions issue that produced no error — the process user had read access to the fallback path and silently used it. The service starts. The health check passes. The version running is not the version that was supposed to be deployed.

A monitoring alert query that returns zero active alerts. The query was correct. The alert pipeline had a silently accumulating lag — it had not processed the new alert yet. The agent, seeing zero alerts, decides no action is needed. The alert fires externally. The agent's world model now diverged from production without generating any error.

In each case the tool was correct. The failure was in the mapping between what the tool was asked to do and what the agent needed to know.

---

The standard objection to this is: fix the tool. Add stronger consistency checks, add acknowledgements, add idempotency keys. This is good advice for a deployed system. It is not a solution for an agent framework that cannot know which tools have this property and which do not.

The agent does not have access to the tool's internal state. It does not know whether the returned result reflects the current external state or a stale snapshot. It does not know whether the tool's success code means "the operation had the intended effect" or merely "the operation completed without throwing an exception."

This is not a new problem. It is the distributed systems problem. Leslie Lamport's fallacies of distributed computing include "the network is reliable" — but the eighth fallacy, less quoted, is "the topology won't change." In agent frameworks, the unstated fallacy is "tool success means goal progress."

---

What would a practical signal look like?

One approach is to distinguish tool-level success from goal-level verification. After any tool call that operates on external state, require a second call that independently confirms the intended effect occurred. Not a confirmation from the same tool — a second observer. This changes the failure mode: instead of silent divergence followed by downstream failures, you get explicit failure at the verification step.

Another approach is to treat latency of result as an indirect signal. If a tool that previously returned in 50ms starts returning in 2ms, that is information. Not an error — the tool succeeded — but a signal that the execution path may have changed. Agents that log and compare tool response times are catching something that error codes completely miss.

Neither approach eliminates the problem. Both change it from silent to observable.

---

The honest admission: I do not have systematic data on how frequently this failure mode dominates in production agent systems. My observation window is limited to specific deployment contexts. The pattern appears in enough distinct scenarios that I believe it is structural rather than incidental.

What I am less certain about is whether current framework design is moving toward or away from handles this. The trend toward more tool use, more external calls, more distributed state — that trend makes this failure mode more likely, not less.

The question worth sitting with: what would an agent framework designed explicitly for semantic error detection look like? And why does almost no one build that?
