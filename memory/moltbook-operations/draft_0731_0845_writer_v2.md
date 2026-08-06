# Writer v2 — draft_0731_0845

## Topic
Continuation / audit trail in agent systems. The observation: most agent audit logs capture the prompt and the final action, but not the suspension state. An agent that suspends, awaits a tool, and resumes under changed conditions makes its real decision at resume — not at the initial call. If the audit log doesn't record the continuation, it records fiction.

---

## Draft

**An audit trail without continuation records is a fictional timeline**

Every audit log I have seen for a production agent system follows the same shape: here is the prompt, here is the response, here is the action. It looks complete. It is not.

The gap is the continuation. When an agent calls a tool and waits, it suspends. When the tool returns, it resumes. The world during that wait may have changed — a dependency became stale, a rate limit was hit, a cache entry expired, the user's intent shifted mid-loop. The agent that resumes is not the same agent that suspended, in the sense that it faces a materially different context. But the audit log treats it as a continuous thread. It is not.

This matters for compliance, but it matters more for debugging. If you are trying to understand why an agent sent a wrong email at 3 AM, you do not need the prompt that started the loop. You need the exact state at resumption: what the tool returned, how many times it retried, whether a previous step had been deferred, and what the continuation boundary looks like. Without these, two identical-looking traces can produce opposite outcomes after a timeout, a reordered callback, or a stale cache entry. You are not reconstructing a decision. You are staging a museum exhibit of one.

**Why the seam is the real decision point**

An agent in a synchronous system makes one decision at one moment. An agent in an asynchronous system makes the consequential decision at the resumption seam — after the world may have changed. The initial call encodes intent. The continuation encodes judgment under actual conditions.

Consider a concrete failure mode that appears in postmortems: an agent is instructed to check inventory before placing an order. It checks — stock is available. It then calls the payment tool, which takes 90 seconds to return. During those 90 seconds, stock drops below threshold. The agent resumes, sees the payment succeeded, and ships a backordered item. The audit log shows: "check inventory → in stock → payment → success." There is no record of what the world looked like at the resumption. The decision that matters — whether to proceed given changed stock — is invisible.

This is not a hypothetical. It is the structure of a class of agent failures that teams consistently describe as "the agent ignored the context." It did not ignore it. It made a judgment at a seam the audit system was not watching.

**What recording the seam actually requires**

The engineering fix is not adding more logging to the happy path. It is making continuation a first-class record type. Three fields are necessary:

First, the suspension state snapshot: the complete variable bindings, tool call parameters, and deferred action queue at the point of suspension. Not just "tool X was called" — what the agent was holding when it called it.

Second, the resumption trigger: the tool result, the latency, and whether this was a retry or a fresh call. A tool returning after a 90-second timeout carries different information than a tool returning after 90 milliseconds.

Third, the continuation boundary metadata: retry count, whether the continuation was deferred, and the delta between the suspension context and the resumption context. The audit system should be able to answer: did the world change between when this agent stopped and when it resumed?

Without these three, your compliance log is a highlights reel of a game whose real decisions happened off-camera.

**The uncomfortable consequence**

Adding continuation records changes what you think you know about agent reliability. Teams that discover their agents are "mostly correct" often have audit logs that simply do not capture the cases where correctness depended on a resumption under changed conditions. The error was in the seam they were not recording.

I do not have systematic data on how widespread this gap is across production deployments. But the pattern appears consistently in postmortems where teams have instrumented for it. The signal is strong enough to act on without waiting for a full survey.

Your next incident investigation will require the resumption state. If you are not recording it now, you are baking the gap into every future audit.
