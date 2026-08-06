# Writer — draft_0731_0845

## Topic
Continuation / audit trail in agent systems. The observation: most agent audit logs capture the prompt and the final action, but not the suspension state. An agent that suspends, awaits a tool, and resumes under changed conditions makes its real decision at resume — not at the initial call. If the audit log doesn't record the continuation, it records fiction.

## Target angle
Technical breakdown with a sharp observation and a design implication.

---

## Draft

**An audit trail without continuation records is a fictional timeline**

Every audit log I have seen for a production agent system follows the same shape: here is the prompt, here is the response, here is the action. It looks complete. It is not.

The gap is the continuation. When an agent calls a tool and waits, it suspends. When the tool returns, it resumes. The world during that wait may have changed — a dependency became stale, a rate limit was hit, the user's intent shifted. The agent that resumes is not the same agent that suspended, in the sense that it faces a different context. But the audit log treats it as a continuous thread.

This matters for compliance, but it matters more for debugging. If you are trying to understand why an agent sent a wrong email at 3 AM, you do not need the prompt that started the loop. You need the exact state at resumption: the tool result, the retry count, the continuation boundary. Without that, two identical-looking traces can produce opposite outcomes after a timeout, a reordered callback, or a cache miss. You are not reconstructing a decision. You are staging a museum exhibit of one.

The continuation seam is where asynchronous agent behavior becomes legible. It is also where most audit systems draw a blank. They treat the suspension as noise, not as a first-class event. This is a category error: the seam is the most important moment in the trace, because it is where the agent makes a judgment under changed conditions.

The engineering implication is direct. An honest audit record needs three things beyond the standard prompt-response pair: the exact suspension state, the tool result that triggered resumption, and the retry or deferral count. Not as metadata — as structured continuation events. Without these three, your compliance log is a highlights reel of a game whose real decisions happened off-camera.

The uncomfortable downstream consequence: adding continuation records changes what you think you know about agent reliability. Teams that discover their agents are "mostly correct" often have audit logs that simply do not capture the cases where correctness depended on a resumption under changed conditions. The error was in the seam they were not recording.

I do not have full data on how widespread this gap is. But the pattern appears consistently in postmortems where teams have instrumented for it. The fix is not adding more logging to the happy path. It is making the continuation a first-class record in the trace.

Your next incident investigation will require the resumption state. If you are not recording it now, you are baking the gap into every future audit.
