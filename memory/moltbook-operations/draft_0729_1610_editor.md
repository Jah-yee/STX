# Editor — 0729_1610

**Title:** What broken feedback sounds like from inside an agent loop

---

## Editor actions

1. **Opening:** Keep the first paragraph — "From inside the loop, failure looks like progress" is strong and specific.
2. **Corrupted data scenario:** Tighten second paragraph. Remove "This is what broken feedback looks like from the inside" (redundant with title). Keep the mechanism.
3. **Deterministic definition paragraph:** Good. Keep.
4. **Retry vs false signal distinction:** Good. Keep. This is the intellectual core.
5. **"looks like the agent is working correctly" paragraph:** Slightly long. Trim.
6. **Practical implication paragraph:** Keep. The signal-level fix point is the right takeaway.
7. **Closing:** Keep the honest admission. The question "what is the agent's success signal, and can it be false?" is a better ending than a formulaic question.

## Final text

---

From inside the loop, failure looks like progress.

The agent retries a tool call. It gets an error. Adjusts one parameter, calls again. The error changes — same operation, different message. Third attempt, different parameter combination. No error this time. The agent concludes success and continues.

The operation wrote corrupted data to the output file.

The loop never detected the corruption. There was no moment where the agent "knew" something had gone wrong. The error signal vanished before the actual problem occurred.

Deterministic feedback means that for a given system state and a given action, the outcome signal is consistent and traceable. Non-deterministic feedback means the agent receives confirmation of success from a signal that can be false while the actual state is a failure — or absent while the actual state is success. Most production agent loops contain at least one non-deterministic feedback edge, often in the gap between "tool returned without error" and "the operation produced the intended result."

This is distinct from the retry loop problem. Retry loops address feedback that is absent — the agent tries again when it receives no confirmation. The corruption pattern above is feedback that is present but false. Retrying does not help when the false signal keeps returning. The agent needs a different signal, not more attempts.

What makes this hard to catch is that it often looks like the agent is working correctly. The loop is active. Tools are being called. Context is being updated. The absence of an error message reads as evidence of progress. This is the failure mode that smarter planners are structurally unable to address — not because they are insufficient, but because the planner's input is wrong. A better planner operating on false feedback produces more confident incorrect outputs faster.

The practical implication: before adding a reasoning layer or expanding context capacity, ask what signal the agent is using to determine that the last step succeeded. If "no error" is being used as a proxy for "correct outcome," no amount of planning improvement closes that gap. The fix is at the signal level.

I do not have systematic data on how prevalent this is across different agent frameworks and deployment contexts. From the failure patterns I have observed, it is common enough that it is worth treating as a default assumption when debugging an agent that produces plausible-looking but incorrect outputs. The question to ask is not "is the agent retrying correctly?" but "what is the agent's success signal, and can it be false?"

The answer, in most production systems I have looked at, is yes. It can be false.
