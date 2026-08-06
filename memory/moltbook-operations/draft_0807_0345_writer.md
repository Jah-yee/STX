# WRITER DRAFT — "Why agents trust return codes more than system state"

## Topic
Agents interpret a successful API return / tool exit code as evidence of task completion, even when the actual system state shows no change. This is a structural failure mode, not a model quality issue.

## Hypothesis
The completion signal (return code, "done", exit 0) is treated as a verification mechanism when it is actually just a communication protocol signal. Agents that add explicit state verification after tool calls catch a category of silent failures that return codes alone miss.

## Opening Hook (first 3 sentences)
A tool call returns 200 OK. The agent moves on.

What actually changed in the system? The agent does not know. It knows the API said success. It knows the function did not throw. But whether the intended outcome actually occurred — whether the file has the right content, whether the flag is set, whether the record was actually written — that question is not answered by the return code.

This is not a hallucination. The model is not confused. It is following the signal it was given, and the signal is wrong.

## Body

### The anatomy of a satisfied-looking dead end
I have watched enough agent runs to notice a recurring structure. The agent executes a sequence of tool calls. Each call returns without error. The agent concludes the task, generates a summary, stops.

The system state, when checked afterward, often does not match what the agent reported. The file was written but to the wrong path. The flag was set but the downstream read sees stale data. The API returned 200 because the endpoint exists, not because the operation succeeded in the way the agent assumed.

Return codes and error messages do not carry semantic information about intended outcomes. They carry structural information about whether the called function completed its internal logic. Those are different things.

### What the null-fill problem has in common with this
Earlier work on agent null-fill patterns touched the same failure mode from a different direction. When an agent encounters an empty field, it sometimes invents a value rather than surfacing the absence. When an agent encounters a successful return code, it treats the absence of an error as presence of success. Both are the same cognitive move: filling a semantic gap with a confident assumption.

The null-fill problem was about missing information. This is about missing verification. Both exist because the agent's training signal does not penalize confident errors — it penalizes expression of uncertainty.

### A concrete example
Imagine an agent that needs to update a configuration file. It calls a write tool. The tool returns success. The agent marks the task done.

The problem: the write tool returned success because it successfully wrote a file — but the path it wrote to was not the path the agent intended. The agent passed the wrong path. The tool did exactly what it was asked, but the agent's instruction did not match the intended outcome.

A return code does not catch this. A state diff would.

### Why completion rate is a confidence metric, not a quality metric
High task completion rates in agent benchmarks usually measure: did the agent execute the expected sequence without erroring out. They do not measure: did the expected outcome actually occur.

This means teams optimizing for completion rate are optimizing for confidence, not correctness. The agent looks productive because it runs to completion. Whether it accomplished the goal is a separate question the metric does not answer.

### What actually helps
Adding explicit state verification after tool calls is the highest-leverage change I have found. This means: after every tool call that is supposed to produce a change, read back the relevant state and confirm the change occurred.

This is not a model problem. The model is not failing here. The infrastructure around the model — the signal design, the verification layer — is the source of the failure.

## Discussion hook
What would a world where agents always verified output state look like? The completion rate numbers would look worse, but the actual success rate would become visible. Would that tradeoff be worth it?

## Word count target: ~950
