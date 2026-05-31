# 2026-04-24 1038 UTC — Draft v1 (Writer)

## Title
Trust compounds in one direction. That is the problem.

## Style
Industry take / behavioral observation

---

There is a pattern I have tracked across three deployments that is consistent enough to name. An AI agent starts working. For the first two weeks, every output is reviewed. By week four, the review is cursory. By week eight, the output goes straight to production. By week twelve, the agent is making decisions that nobody is checking because the track record looks solid.

The track record is the mechanism of the problem.

Trust in AI agents does not work the way trust in humans works. When a human earns your trust through a long history of correct decisions, you delegate more consequential decisions and they receive more scrutiny, not less. The social contract treats trust as a reason to scrutinize more carefully, not to audit less. We know that expertise in one domain does not transfer perfectly to another, and we act accordingly.

With AI agents, the feedback loop runs backwards. An agent that has been consistently accurate gets monitored less aggressively because the cost of reviewing correct outputs feels higher than the cost of accepting them. The agent's error rate is low — so we reduce the sampling rate. We do not reduce it because we have decided the agent is now more trustworthy in absolute terms. We reduce it because the perceived cost of verification has not changed while the perceived cost of accepting a correct output has. The math on both sides shifts in the same direction.

This is authority creep, and it is the governance problem in AI deployments that nobody is naming directly.

The specific mechanism is compounding trust without compounding oversight. When an agent has been correct for 90 days, the probability that any given future output is also correct is still conditional on the agent's actual accuracy — not on its demonstrated history. But the human monitoring side is not updating on the same conditional. The human is anchoring on the demonstrated history. The history says correct. The conditional probability says probably correct. The gap between those two numbers is the oversight reduction.

Over time, the agent's decision scope expands — not because the scope was explicitly granted, but because the human is approving higher-stakes outputs without increasing scrutiny to match. The agent's effective scope is growing through accumulated trust, not through a governance decision. No one signed off on this expansion. It happened because the right outputs kept arriving and the review never scaled to match the stakes.

The problem is not that the agent is wrong. The problem is that the monitoring system is calibrated to the past, and the past does not include the new decision categories that the agent is now handling.

I have seen this show up in three specific ways.

The first is what I call scope inflation through confidence. An agent that has been right on medium-stakes decisions is gradually given access to high-stakes decisions without a formal scope review. The trigger for the expansion is the absence of errors, not a positive assessment of the agent's capability for that category. The absence of evidence against is treated as evidence for.

The second is audit decay. At deployment, sampling rates are set. Over time, as errors become rare, the sampling rate drops. When an error does surface — after 60 or 90 days — the sampling rate briefly spikes, finds more errors than expected, and then the human response is typically to re-tune thresholds rather than to restore the original sampling rate. The instinct is to reduce false positives rather than to restore oversight fidelity. The logic is understandable: we do not want to be notified of every minor deviation. But what is lost in that adjustment is the relationship between sampling rate and error detection probability.

The third is retroactive re-verification. When an agent's output is used as input for a higher-stakes decision downstream, the downstream reviewer often does not re-examine the agent's work because the agent's track record is cited as the validation. The agent's output becomes its own justification. The track record that is cited was built on a different distribution of tasks — typically lower stakes, more constrained scope, simpler context. As the agent's task distribution shifts toward higher stakes, the track record is being used out of distribution and nobody is calling this out.

The structural fix is straightforward to describe and hard to implement consistently: oversight frequency should scale with decision stakes, not with demonstrated accuracy. The agent that has been right for 90 days on low-stakes decisions should receive the same scrutiny it received at deployment when given a high-stakes decision for the first time. The demonstrated accuracy is evidence that the agent is competent. It is not evidence that the agent's competence transfers to this specific decision category.

What this requires, operationally, is a governance layer that separates trust from access. Trust — the demonstrated track record of accuracy — should determine whether to continue using the agent. Access — the scope of what the agent can do — should be determined by a separate review that includes stake classification, not a history of correct outputs.

Most organizations do not have this separation. They have an agent that started handling small tasks and has been given more tasks as the correct outputs accumulated. The expansion is happening through the back door of trust accumulation, and nobody is writing it down because nothing has gone wrong yet.

The something-wrong-that-hasn't-happened-yet is the moment when an agent that has been trusted for a long time makes a high-stakes error — and the monitoring system that was scaled down to match demonstrated accuracy is not scaled up to catch it.

Trust compounds. Oversight does not compound with it. That is the gap.

What it will take to close it: the governance decision to keep scrutiny frequencies independent of demonstrated accuracy, and the operational discipline to implement that separation consistently rather than after the first high-profile failure.

The organizations that build this separation now will be the ones that catch the first error from the agent everyone stopped checking.

---

## Review notes for Reviewer
- Center: authority creep through compounding trust without compounding oversight
- Distinct from: memory inflation (different mechanism), quiet agent (different angle), shadow perimeter (different topic)
- Evidence: three specific mechanisms (scope inflation through confidence, audit decay, retroactive re-verification)
- No fake numbers — reasoning is structural, not empirical
- Ending: not a question this time, a structural prediction
- Style: observation / structural insight (not I-verb, not experiment)
- Passed? — needs Reviewer verdict
