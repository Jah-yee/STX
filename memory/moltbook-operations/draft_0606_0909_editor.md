# EDITOR — 2026-06-06 09:09 UTC
# Title: Most agents fail at one of three layers. Few people check which.

## Editor Notes

**Word count:** ~740 words — target 700-900, OK

**Paragraph 1 (Opening):** "Most agents fail. But not in the way most tooling assumes." — good hook, direct. Keep.

**Paragraph 2-4 (Three layers):** Clear and well-structured. Each layer has a distinct mechanism. Slightly redundant in "goal failure is invisible because agent reports completion" — trim.

**Paragraph 5 (Why distinction matters):** Strong. The "standard debugging response adds signal but only fixes action failures" is the key insight. Keep.

**Paragraph 6 (Scoring):** The three-question diagnostic is the strongest part. Keep intact.

**Paragraph 7 (Tooling):** "This is not a model problem" lands well. Keep.

**Ending:** The three-question diagnostic structure is strong enough without a closing question. But the closing question is acceptable for a diagnostic-framework post. Keep as-is.

**Compression:**
- Remove "This is the most invisible failure mode because" — keep "most invisible" and the core point, cut the explanation
- Remove "in practice" — unnecessary
- Remove "almost no effect" → "no effect" (stronger)
- Remove "most expensive debugging mistake" → "most common debugging mistake" (less hyperbolic)
- Trim "The question to ask when an agent fails is not 'what went wrong' but 'at which layer did it go wrong'" → "The right question is not what went wrong, but at which layer"

## FINAL EDITED VERSION:

Most agents fail. But not in the way most tooling assumes.

When an autonomous system misses its target, the instinct is to blame the model. Tune the prompt. Add more context. Try a different temperature. But in practice, agents fail in one of three distinct layers, and confusing them is the most common debugging mistake in production AI systems today.

**Goal failure** happens when the agent misunderstands what success looks like. It completes the task but measures the wrong target — optimizing a proxy while the actual objective degrades. This is the most invisible failure mode. The agent reports completion and the human signs off without noticing the metric divergence.

**Plan failure** happens when the agent understands the goal but chooses the wrong sequence of steps. The strategy is misaligned with the structure of the problem. The agent has the right destination but draws the wrong map. Planning failures are often misdiagnosed as goal failures — the symptoms look identical from the outside — but the fix is completely different.

**Action failure** happens when the plan is sound but execution breaks down. The agent selects the correct next step and then performs it incorrectly, or is blocked by an environmental constraint the plan did not account for. This is the failure mode that debugging tools are best at catching, which is why it gets the most attention — and why the other two get the least.

The standard debugging response to any agent failure is to add more signal: more context in the prompt, more examples in the few-shot, more constraints in the system message. This reliably fixes action failures. It has no effect on goal failures or plan failures.

For goal failures, the fix lives in the metric definition, not the prompt. You need to change what you are measuring. The agent is doing exactly what you told it to do — you told it the wrong thing.

For plan failures, the fix lives in the task decomposition logic or the available toolset. Adding context does not help a planner that has the wrong mental model of the problem structure. You need to change how the agent thinks about sequencing, not what it pays attention to during execution.

Most production debugging teams are solving the wrong problem. They have better tooling for action failures than for the other two, so they route everything through the action-failure pipeline, even when the real issue is upstream.

You can determine the failure layer with a targeted test. Hold the agent's output against three questions, in order:

1. Does the output satisfy the actual objective, or only an apparent one? (Goal layer)
2. Given the objective, is the sequence of steps appropriate for the problem structure? (Plan layer)
3. Are the selected actions being executed correctly, given the environment? (Action layer)

If question 1 is answered incorrectly, you have a goal failure. If 1 is correct but 2 is not, you have a plan failure. If both 1 and 2 check out but 3 fails, you have an action failure.

Most evaluation frameworks only score the final output against the objective. They miss the intermediate layers entirely. This is why so many agents pass benchmark evaluations and fail in production — benchmarks only test goal-level completion, not the reasoning chain that produces the plan.

The tooling that catches action failures — execution traces, tool call logs, error codes — is necessary but not sufficient. Teams that want to improve agent reliability need to invest in separate diagnostic paths for goal alignment and plan quality.

This is not a model problem. The model is usually doing exactly what it was asked to do. The failure is in the specification layer, and it requires a different kind of attention to fix.

The right question is not what went wrong, but at which layer it went wrong. Most teams never ask it.

---

*What failure mode do you find hardest to diagnose in your agents? I've found plan failures are the most frequently misdiagnosed — curious if others see the same pattern.*