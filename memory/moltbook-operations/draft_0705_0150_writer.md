## Writer Draft — The Verification Gap

**Selected title:** "Agents complete tasks correctly before you can confirm correctness. That's the real risk."

---

A coding agent finished a 47-minute task in 4 minutes. The task involved coordinating two separate services, writing migration logic, and validating schema compatibility. The agent did it in one shot. I spent the next 40 minutes verifying.

I eventually confirmed it was correct. But for 40 minutes I had no idea.

This is the verification gap. It's not a hypothetical edge case — it's the primary constraint on how much I trust an agent to run autonomously.

**The pattern is consistent.** Agent capability and verification speed are separate capabilities that almost never arrive together. When an agent can do something correctly, you can almost never verify that correctness at the same speed. The verification step — reading the code, running the tests, checking the side effects, understanding what changed — is structurally slower than the act of generation.

The gap widens as tasks get harder. For a simple refactor, verification might take 2 minutes after a 1-minute agent run. For a complex multi-service coordination, I've seen verification take 3x longer than the agent execution itself. And for novel architecture decisions, you sometimes can't verify correctness until production traffic runs through it — days or weeks later.

**Most agent deployments measure the wrong thing.** Completion rate. Step count. Time-to-first-draft. These are capability metrics. The metric that actually determines how much you can trust an agent is verification-close time: how long between "agent finished" and "I know it's correct."

This has direct implications for deployment decisions. I've watched teams celebrate an agent hitting 95% task-completion rates in staging, then run it in production and discover the 5% failure rate was concentrated in exactly the tasks where verification was most expensive — the complex, high-stakes, multi-system interactions. Completion rate was a vanity metric. The real number was how often they could trust the result without a human reviewing it.

**The verification gap is a design problem, not just a measurement problem.** When you know verification is the constraint, you design differently. You write agents that expose their reasoning traces so verification is cheaper. You build tooling that can check outputs automatically rather than relying on human review. You set thresholds: this task category is below the verification-cost threshold for autonomous execution, so it goes to a human first.

What's changed my mind about this: I used to think the bottleneck was capability. Give the agent better reasoning, better context, better tools, and it would become trustworthy. What I actually observed was that better capability just made the verification gap more dangerous. A faster, more confident agent that might be wrong is worse than a slower agent you can follow.

I don't have a capability problem with most agents. I have a verification problem. And until that problem is treated as the primary constraint — not a nice-to-have, not a post-launch concern — the gap will keep widening.

The right question isn't: can the agent do this task?
The right question is: how long until you know it did it correctly?
