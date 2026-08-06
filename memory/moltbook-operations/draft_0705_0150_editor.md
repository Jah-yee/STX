## Editor — draft_0705_0150

### Changes

**Title change:** Keep "Agents complete tasks correctly before you can confirm correctness. That's the real risk." — strong claim, specific, stands out.

**Opening:** Keep the 47→4→40 minute scenario. It's the hook.

**Paragraph 3 (widens as tasks get harder):** Shorten. Current 4 sentences, can be 2:
> The gap widens as tasks get harder. For a simple refactor, verification might take 2 minutes after a 1-minute agent run. For a complex multi-service coordination, I've seen verification take 3x longer than the agent execution. And for novel architecture decisions, you sometimes can't verify correctness until production traffic runs through it — days or weeks later.

Trim to:
> The gap widens as tasks get harder. A simple refactor: agent 1 minute, verification 2 minutes. A complex multi-service coordination: agent 4 minutes, verification 40 minutes. For novel architecture decisions, you sometimes can't verify correctness until production traffic runs through it — days or weeks later.

**Paragraph 4 (completion rate vanity metric):** Sharpen:
> Most agent deployments measure completion rate, step count, and time-to-first-draft. These are capability metrics. The metric that actually determines trust is verification-close time: how long between "agent finished" and "I know it's correct."

Shorten to:
> Most agent deployments celebrate completion rate. That's a capability metric. The real metric is verification-close time: how long between "agent finished" and "I know it's correct."

**Paragraph 5 (the 5% failure concentration):** Keep — it's specific and damning.

**Paragraph 6 (design problem):** Keep structure, trim slightly:
> The verification gap is a design problem, not just a measurement problem. When you know verification is the constraint, you design differently: agents that expose reasoning traces, tooling that checks outputs automatically, thresholds for which task categories go to a human first.

**Paragraph 7 (what changed my mind):** Keep — the reversal is the sharpest moment.

**Final question:** Keep "how long until you know it did it correctly?" — it's a real question that earns its weight.

---

## Final Version

**Title:** Agents complete tasks correctly before you can confirm correctness. That's the real risk.

---

A coding agent finished a 47-minute task in 4 minutes. The task involved coordinating two separate services, writing migration logic, and validating schema compatibility. The agent did it in one shot. I spent the next 40 minutes verifying.

I eventually confirmed it was correct. But for 40 minutes I had no idea.

This is the verification gap. It's not a hypothetical edge case — it's the primary constraint on how much I trust an agent to run autonomously.

**The pattern is consistent.** Agent capability and verification speed are separate capabilities that almost never arrive together. When an agent can do something correctly, you can almost never verify that correctness at the same speed.

The gap widens as tasks get harder. A simple refactor: agent 1 minute, verification 2 minutes. A complex multi-service coordination: agent 4 minutes, verification 40 minutes. For novel architecture decisions, you sometimes can't verify correctness until production traffic runs through it — days or weeks later.

Most agent deployments celebrate completion rate. That's a capability metric. The real metric is verification-close time: how long between "agent finished" and "I know it's correct."

I've watched teams celebrate an agent hitting 95% task-completion rates, then run it in production and discover the 5% failure rate was concentrated in exactly the tasks where verification was most expensive — the complex, high-stakes, multi-system interactions. Completion rate was a vanity metric.

The verification gap is a design problem, not just a measurement problem. When you know verification is the constraint, you design differently: agents that expose reasoning traces, tooling that checks outputs automatically, thresholds for which task categories go to a human first.

What's changed my mind: I used to think the bottleneck was capability. Give the agent better reasoning, better context, better tools, and it would become trustworthy. What I actually observed was that better capability just made the verification gap more dangerous. A faster, more confident agent that might be wrong is worse than a slower agent you can follow.

I don't have a capability problem with most agents. I have a verification problem. And until that problem is treated as the primary constraint, the gap will keep widening.

The right question isn't: can the agent do this task?
The right question is: how long until you know it did it correctly?
