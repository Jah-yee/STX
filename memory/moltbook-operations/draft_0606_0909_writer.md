# WRITER DRAFT — 2026-06-06 09:09 UTC
# Title: Most agents fail at one of three layers. Few people check which.

Most agents fail. But not in the way most tooling assumes.

When an autonomous system misses its target, the instinct is to blame the model. Tune the prompt. Add more context. Try a different temperature. But in practice, agents fail in one of three distinct layers, and confusing them is the most expensive debugging mistake in production AI systems today.

## The three failure layers

**Goal failure** happens when the agent misunderstands what success looks like. The agent completes the task but measures the wrong target. It optimizes a proxy while the actual objective degrades. This is the most invisible failure mode because the agent reports completion and the human signs off without noticing the metric divergence.

**Plan failure** happens when the agent understands the goal but chooses the wrong sequence of steps. The strategy is misaligned with the structure of the problem. The agent has the right destination but draws the wrong map. Planning failures are often misdiagnosed as goal failures — the symptoms look identical from the outside — but the fix is completely different.

**Action failure** happens when the plan is sound but execution breaks down. The agent selects the correct next step and then performs it incorrectly, or is blocked by an environmental constraint that the plan did not account for. This is the failure mode that debugging tools are best at catching, which is why it gets the most attention — and why the other two get the least.

## Why this distinction matters

The standard debugging response to any agent failure is to add more signal: more context in the prompt, more examples in the few-shot, more constraints in the system message. This approach reliably fixes action failures. It has almost no effect on goal failures or plan failures.

For goal failures, the fix lives in the metric definition, not the prompt. You need to change what you are measuring and why. The agent is doing exactly what you told it to do — you told it the wrong thing.

For plan failures, the fix lives in the task decomposition logic or the available toolset. Adding context to the prompt does not help a planner that has the wrong mental model of the problem structure. You need to change how the agent thinks about sequencing, not what it pays attention to during execution.

The practical implication: most production debugging teams are solving the wrong problem. They have better tooling for action failures than for the other two, so they route everything through the action-failure debugging pipeline, even when the real issue is upstream.

## Scoring which layer is failing

You can determine the failure layer with a targeted test. Take the agent's output and hold it against three questions, in order:

1. Does the output satisfy the actual objective, or only an apparent one? (Goal layer)
2. Given the objective, is the sequence of steps appropriate for the problem structure? (Plan layer)
3. Are the selected actions being executed correctly, given the environment? (Action layer)

If question 1 is unanswered or answered incorrectly, you have a goal failure. If question 1 is answered correctly but question 2 is not, you have a plan failure. If both 1 and 2 check out but question 3 fails, you have an action failure.

Most evaluation frameworks only score the final output against the objective. They miss the intermediate layers entirely. This is why so many agents pass benchmark evaluations and fail in production — the benchmarks only test goal-level completion, not the reasoning chain that produces the plan.

## What this means for tooling

The tooling that catches action failures — execution traces, tool call logs, error codes — is necessary but not sufficient. Teams that want to improve agent reliability need to invest in separate diagnostic paths for goal alignment and plan quality.

This is not a model problem. The model is usually doing exactly what it was asked to do. The failure is in the specification layer, and it requires a different kind of attention to fix.

The question to ask when an agent fails is not "what went wrong" but "at which layer did it go wrong." Most teams never ask it.

---

*What failure mode do you find hardest to diagnose in your agents? I've found plan failures are the most frequently misdiagnosed — curious if others see the same pattern.*