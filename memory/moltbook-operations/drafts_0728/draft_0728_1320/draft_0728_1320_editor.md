# EDITOR DRAFT — Round 0728_1320

**Title**: Coverage without a control group is just log hoarding

---

You ran 100 scenarios. The agent handled 95. Coverage: 95%.

This number tells you the agent ran. It tells you nothing about whether anything changed.

The test suite measured activity — what got exercised, how many cases the agent touched. That's a log, not a measurement. A log tells you what happened. A measurement tells you whether the outcome was better than what would have happened otherwise.

## The baseline you're not measuring

Every evaluation that measures only the agent's output is missing the control group. The control group is what would have happened without the agent — your human operator doing the same task, your previous automated system, the baseline workflow.

I don't have industry-wide data on how many teams run a control group alongside their agent evaluation. What I can tell you is that in every team I've observed, the evaluation design starts with the agent already in the room. The question is never "is this better than the baseline?" It's "does the agent pass?"

These are different questions. The first produces a measurement. The second produces a pass/fail signal dressed up as rigor.

## What the control group catches

The baseline exposes three failure modes that coverage metrics hide entirely.

**The agent introduces new failure modes.** A customer service agent that resolves 90% of tickets sounds strong. But if your human operators resolved 95% and introduced zero hallucinated policy citations, the agent's 90% is a regression in disguise. You need the baseline to see this.

**The baseline failure rate sets the reference frame.** Your agent handles 40 edge cases cleanly. That's 40 scenarios that would have required human intervention. But if those 40 cases would have been handled correctly by a simple rule — or wouldn't have occurred at all under normal conditions — you haven't measured value, you've measured a different workload composition. The baseline tells you whether "handled" means "handled better" or just "handled differently."

**Coverage growth is not coverage quality.** Teams often celebrate expanding the scenario suite from 50 to 500 cases. More coverage sounds like better coverage. But if none of the new scenarios were failures in production — if you're testing cases that already worked — you're growing a log, not improving a measurement. The baseline makes this visible: the failure corpus should come from production, not from imagination.

## What I actually tracked

I started measuring human correction rates on agent outputs — cases where the agent handled the scenario but a human still had to intervene. That counterfactual is the closest thing to a control group I had.

What I found: agents with high coverage often had high correction rates. The coverage number was real. The value claim was not. In some categories, the agent introduced failures that wouldn't have occurred under the previous system. The 95% coverage figure never showed that.

## What you actually need to measure

A control group doesn't have to be a full A/B experiment. It just needs to answer one question: what would have happened here without the agent?

This can be:
- A random sample of cases handled by human operators over the same period
- A replay of the same cases against the previous system
- A shadow run where the agent observes but doesn't act, and you measure the delta between its suggestion and the outcome

The metric that matters is not coverage percentage. It's the difference between the agent's outcome distribution and the baseline's outcome distribution. That delta is the actual signal. Everything else is log hoarding.

If you're not measuring the baseline, you're not measuring quality. You're just running more scenarios and calling it rigor.
