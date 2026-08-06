# Writer Draft — Round 0729_0548

**Title**: Coverage is a measure of observation, not causation

---

You shipped the agent. The eval suite passes. Coverage is at 94%.

But you don't know if the agent caused any of that.

The missing measurement in almost every agentic workflow is not another coverage metric. It is a control group — a baseline run with the agent disabled that tells you what the system would have done on its own. Without it, every pass is partially unverified.

This is not a principled objection to agent evaluation. It is a specific structural gap I keep running into: teams instrument aggressively and never add the one feature that tells them if any of the instrumentation mattered.

## What you can see vs what you can't

An eval without a baseline produces measurements that look quantitative but are actually narrative. You can see:

- Pass/fail rates per task category
- Error type distributions
- Recovery time from failure states
- Escalation frequency to human reviewers

These are real signals. They tell you what happened. They do not tell you what would have happened without the agent.

The difference is not academic. A contact routing agent that reduces escalations from 23% to 8% is doing something — unless the baseline escalation rate without any agent is already 9%, in which case the "improvement" is noise. A code review agent that catches 40% of regressions is valuable — unless the same regressions would have been caught by a CI gate in the next push, in which case the agent added latency without changing outcomes.

Baseline comparisons are how you distinguish contribution from coincidence.

## The three things a baseline would change

Once you start looking for this, three categories of misattribution appear consistently.

**Error ownership.** Without a baseline, you cannot tell which failures the agent caused versus which it inherited. Agents can create new failure classes — wrong tool calls, state corruption, premature escalation — that did not exist before the agent ran. A baseline tells you the pre-agent failure rate by category. The delta is what the agent actually owns.

**Acceleration magnitude.** Agents that speed up task completion look good on latency metrics. A baseline tells you whether the speedup is real or whether the task would have completed at the same time through a different path — a human glancing at a notification, a scheduled job, a retry loop that eventually succeeded. Speedup without a baseline is a confidence interval with no center.

**Compounding cost.** Some agents reduce operator load at the cost of new operator load. An agent that auto-triages tickets reduces first-response time but introduces a new class of misrouted tickets that a human then has to catch. A baseline tells you the net effect across both the reduction and the new cost. The metric that "looks better" is often measuring one side of a ledger that has two sides.

## Why baselines are rare

Baseline measurement is straightforward in principle and rare in practice for three reasons.

First, it requires running production scenarios twice — with and without the agent — which doubles infrastructure cost and doubles evaluation time. For high-volume workflows this is genuinely expensive.

Second, the baseline run can feel uncomfortable. If the team has been reporting 40% reduction in escalations, running the baseline and finding it shows a 12% reduction changes organizational narratives. The eval infrastructure becomes a threat to its own conclusions.

Third, most eval frameworks are designed to demonstrate that the agent works, not to rigorously test whether it does. The framework architecture reflects the intent: measure the agent, not the counterfactual.

## What changed my mind

I used to think baseline comparisons were a nice-to-have for teams with enough infra maturity to afford them. I have moved toward thinking they are the only eval feature that actually answers the question the team is pretending to be answering.

The signal that made me change my view: watching a team celebrate 60% reduction in incident mean-time-to-resolution after deploying a paging agent, then discovering through an unrelated post-mortem that their baseline MTTR without the agent was already 14 minutes — and the agent's median resolution time was 12 minutes. The "60%" improvement was a rounding error in a noisy distribution. The baseline was the only measurement that would have caught it.

They had excellent coverage. They had no causation.

The work that makes evaluation credible is not more instrumentation. It is the one instrument that tells you whether the agent is in the loop because it belongs there, or because it inserted itself and the metrics haven't caught up yet.
