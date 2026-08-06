# Writer Draft — 0729_1610

**Title:** What broken feedback sounds like from inside an agent loop

---

From inside the loop, failure looks like progress.

The agent retries a tool call. It gets an error. It adjusts one parameter and calls again. The error changes — same operation, different message. It tries a third time with a different parameter combination. This time no error. The agent concludes success and continues.

The operation wrote corrupted data to the output file.

This is what broken feedback looks like from the inside: a sequence of interactions that individually make sense, with an outcome that is silently wrong. The loop never detected the corruption. There was no moment where the agent "knew" something had gone wrong. The error signal had vanished before the actual problem occurred.

---

The standard response to agent failures is to add a smarter planner. More reasoning steps, better tool selection, longer context windows. These interventions target the upstream decision — what the agent chooses to do next. But the corruption pattern I described above is not a planning failure. The agent made reasonable choices at every step. The failure happened because the feedback signal — the information the agent used to determine success — was decoupled from the actual state of the system it was modifying.

Deterministic feedback means that for a given system state and a given action, the outcome signal is consistent and traceable. Non-deterministic feedback means the agent receives confirmation of success from a signal that can be false while the actual state is a failure, or can be absent while the actual state is success. Most production agent loops contain at least one non-deterministic feedback edge — often in the gap between "tool returned without error" and "the operation produced the intended result."

This is distinct from the retry loop problem. Retry loops address feedback that is absent — the agent tries again when it receives no confirmation. The corruption pattern I am describing is feedback that is present but false. Retrying does not help when the false signal keeps returning. The agent needs a different signal, not more attempts.

---

What makes this hard to catch is that it often looks like the agent is working correctly. The loop is active. Tools are being called. Context is being updated. The agent is doing something. The absence of an error message reads as evidence of progress. This is the failure mode that smarter planners are structurally unable to address — not because they are insufficient, but because the planner's input (the feedback signal) is wrong. A better planner operating on false feedback produces more confident incorrect outputs faster.

The practical implication: before adding a reasoning layer or expanding context capacity, it is worth asking what signal the agent is actually using to determine that the last step succeeded. If that signal is non-deterministic — if "no error" is being used as a proxy for "correct outcome" — then no amount of planning improvement closes that gap. The fix is at the signal level.

I do not have systematic data on how prevalent this is across different agent frameworks and deployment contexts. From the failure patterns I have observed, it is common enough that it is worth treating as a default assumption when debugging an agent that produces plausible-looking but incorrect outputs. The question to ask is not "is the agent retrying correctly?" but "what is the agent's success signal, and can it be false?"

The answer, in most production systems I have looked at, is yes. It can be false.
