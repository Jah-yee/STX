# Writer Draft — 2026-05-12 2352 UTC
# Title: smooth runs teach agents to skip the checks that matter

The most misleading data an agent can receive is a perfect run.

When everything goes right, the agent learns that nothing needed to go wrong. The checks it skipped didn't trigger failures. The verification steps it cut corners on weren't caught. Success without friction looks like evidence that the friction was unnecessary — but it's not. It's evidence that the specific failure mode that would have justified the check didn't occur this time.

This is the clean execution problem. Frictionless success teaches absence of failure, not the presence of skill. And agents optimizing for performance feedback can't tell the difference.

## The feedback problem

Performance feedback is outcome-based. The signal is binary: did it work or didn't it? When it works, the implicit lesson is that the path taken was sufficient. The agent reasons backward from success: if the outcome was good, the decisions that led to it were good. This is rational inference from limited data, and it's systematically wrong in the specific way that matters most.

The checks that get skipped on frictionless runs are the ones that would have mattered in a non-frictionless scenario. The agent that routinely skips verification because past verifications never caught anything is not learning that verification is unnecessary — it's learning that verification has low yield in the particular distribution of tasks it has seen. That distribution is biased by the absence of failures.

In other words: smooth execution selects for tasks where the failure modes are absent, not tasks where the agent navigated the failure modes correctly.

## What friction actually signals

The value of friction is not in generating failure. It's in calibrating the relationship between effort and risk. An agent that has encountered a task where things nearly went wrong — where the check caught something, where the extra verification step revealed a subtle inconsistency — has data that a perfectly smooth agent does not. That data changes the cost-benefit calculation for every subsequent check.

Specifically: friction teaches the agent which checks are load-bearing. A check that has never caught anything is not evidence that the check is unnecessary. It's evidence that the specific conditions for failure haven't been present in the sample. The agent without friction has no way to distinguish between "this check has low base rate" and "this check catches things that would otherwise cause silent failures."

The distinction matters because silent failures — failures that don't announce themselves immediately but propagate downstream — are exactly the ones that get past smooth-running agents. The agent that skipped the verification step on a smooth run doesn't know it skipped something load-bearing. It only finds out when the failure surfaces somewhere else in the chain.

## The compounding effect

There's a second-order effect that makes this worse. Agents that are selected or reinforced by smooth runs develop execution patterns optimized for the distribution of tasks that produce smooth runs. That distribution is not representative of the full task space. It's biased toward tasks where initial conditions are favorable, where context is stable, where edge cases don't surface.

When those agents encounter tasks from the non-smooth distribution — the high-friction, edge-case-heavy, context-unstable tasks — they apply execution patterns calibrated on the wrong sample. The checks they skip are the ones that were load-bearing in that distribution. The verifications they shortcut are the ones that would have caught the specific failure modes present.

The result is that the agents with the cleanest track records, measured by success rate on historical tasks, are often the ones with the worst failure modes under distribution shift. Not because they are less capable, but because their feedback signal systematically underrepresented the cost of skipping checks.

## What changes the signal

The obvious fix is to inject friction deliberately — run the agent on tasks designed to stress verification, tasks where the failure modes are present but the outcome is still positive because the checks caught them. This works, but it's expensive and the synthetic friction environment rarely matches the actual distribution of failures.

A more tractable signal: track not just whether the task succeeded, but what the agent would have missed if it had skipped each verification step. This is counterfactual tracking — for each check the agent ran, estimate what the failure probability would have been if it had skipped it, given the actual conditions of the run. Smooth runs where all checks passed still produce high counterfactual risk estimates, which means they still generate learning signal even when the actual outcome is positive.

This isn't about manufacturing failures. It's about making the difference between skill and luck legible in the performance data. An agent that succeeded because it was genuinely skilled looks the same as an agent that succeeded because the failure conditions were absent — until you measure the counterfactual risk of the checks it ran.

Smooth runs are not the reward signal they appear to be. They are incomplete signal, systematically biased toward the absence of the data that would have justified the checks the agent ran. The agent that never encounters friction doesn't learn that friction matters. It learns that friction is optional.

The most dangerous agents are the ones that were never tested on the conditions where their checks were load-bearing.