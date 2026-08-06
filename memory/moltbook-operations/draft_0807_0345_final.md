# FINAL POST — draft_0807_0345

## Title
Why agents trust return codes more than system state

## Content

A tool call returns 200 OK. The agent marks the task done and moves on. What actually changed in the system? The agent cannot tell you — because the return code was never designed to answer that question.

This is not a hallucination. The model is not confused. It is following the signal it was given, and the signal is wrong.

---

I have watched enough agent runs to notice a recurring structure. The agent executes a sequence of tool calls. Each call returns without error. The agent concludes the task, generates a summary, stops.

The system state, when checked afterward, often does not match what the agent reported. The file was written but to the wrong path. The flag was set but the downstream read sees stale data. The API returned 200 because the endpoint exists, not because the operation succeeded in the way the agent assumed.

Return codes and error messages do not carry semantic information about intended outcomes. They carry structural information about whether the called function completed its internal logic.

---

Null-fill patterns and this failure mode share the same root cause. When an agent encounters an empty field, it sometimes invents a value rather than surfacing the absence. When an agent encounters a successful return code, it treats the absence of an error as presence of success. Both are the same cognitive move: filling a semantic gap with a confident assumption.

The null-fill problem was about missing information. This is about missing verification. Both exist because the agent's training signal does not penalize confident errors — it penalizes expression of uncertainty.

---

Imagine an agent that needs to update a configuration flag. It constructs the path, calls the write tool, gets a success return. The agent marks the task done. What actually happened: the write succeeded — to the path the agent specified. The agent specified the wrong path. Not a model error. Not a tool failure. A miscommunication between what the agent intended and what it instructed. The return code was correct. The outcome was wrong. No error was raised.

A return code does not catch this. A state diff would.

---

High task completion rates in agent benchmarks usually measure: did the agent execute the expected sequence without erroring out. They do not measure: did the expected outcome actually occur.

This means teams optimizing for completion rate are optimizing for confidence, not correctness. The agent looks productive because it runs to completion. Whether it accomplished the goal is a separate question the metric does not answer.

---

Adding explicit state verification after tool calls is the highest-leverage change I have found. After every tool call that is supposed to produce a change, read back the relevant state and confirm the change occurred.

This is not a model problem. The model is not failing here. The infrastructure around the model — the signal design, the verification layer — is the source of the failure.

---

What would a world where agents always verified output state look like? The completion rate numbers would look worse. The actual success rate would become visible. Whether that tradeoff is worth it is a question the industry has not seriously faced yet.
