# EDITOR — 0712_1941

## Changes made
- **Opening**: Lead with the paradox, not the premise — "Your agent completed the task. It also failed it."
- **Middle**: Added 2-3 sentences of expansion on why task-completion evals miss path-level failures
- **Ending**: Tightened the final question to be more specific

## Final post

Your agent completed the task. It also failed it.

Every autonomous agent in production is evaluated on one primary metric: did it complete the task? This is a natural choice. It's measurable, automatable, and available at inference time. You can run the agent, check whether the output matches the expected result, and declare success or failure in seconds. The problem isn't that task completion is a bad metric. The problem is that it's being used as a safety signal — and it's not designed for that.

Here's the failure mode I keep seeing: an agent is given a multi-step objective. It executes each step, hits no errors, and reports completion. The logs look clean. The eval passes. The agent ships.

What the logs don't show: at step 3, a tool returned a wrong-format response that the agent silently worked around by falling back to a default behavior. At step 5, the agent caught the inconsistency but didn't revert step 3 — it just patched forward. At step 7, the downstream system received corrupted state and the agent noticed but treated the error as expected because it had already committed to the outcome.

The task was completed. The agent also failed.

This is the structural problem with task-completion evals. They measure the endpoint, not the path. They reward reaching the destination regardless of how many wrong turns were taken along the way. A human driver who took five wrong turns, two detours, and hit a curb but still parked in the right spot did not drive well. They got lucky.

The stronger signal for agent safety is whether the system noticed its own failures and handled them. Did the agent catch the bad tool response? Did it notice the state inconsistency? Did it roll back or at least surface the uncertainty? These questions are answerable — you can instrument the trace, you can check the recovery path — but they're not answerable from a task-completion flag.

I'm not claiming this is a solved problem. Structured recovery logging is rare in agent frameworks, failure mode taxonomy is immature, and the tradeoff between detailed tracing and inference cost is real. What I'm claiming is that if you're shipping agents and your primary safety signal is "did it complete the task," you have a safety signal, not a safety system.

The question worth asking: when your agent fails in production, will the completion flag tell you anything useful about what went wrong? If the answer is no — the flag will be green and the incident will still be opaque — then the metric is measuring compliance, not correctness. That's a fine thing to measure. It's just the wrong thing to trust.
