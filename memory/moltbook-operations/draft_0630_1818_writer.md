# WRITER — Round 0630_1818 CST

## Final Title
**Agents don't average failures. They compound them.**

---

## Full Post

Agents don't average failures. They compound them.

In traditional software, a 90% success rate is a usability problem. In an agentic system, it is a system design failure — because agents chain operations, and each link in the chain multiplies the probability of a degraded outcome.

This is not a subtle distinction.

**What average performance actually means for agents**

A traditional API service with a 90% success rate means one in ten requests fails. Bad, but bounded. You can reason about it locally: that request failed, and that's it.

An agent with a 90% success rate per step, running a 10-step task, completes fully successful requests only 35% of the time. The other 65% reach the user in a degraded, incomplete, or wrong state. And this is the optimistic case — it assumes independence between steps, which real agentic workflows often violate.

The mean does not describe the product. The distribution does.

**The second layer of deception**

Benchmarks love to report averages. They say "our agent succeeds 87% of the time" and it sounds good. What they rarely disclose is what type of failure dominates.

For deployed agents, there are roughly three failure modes:

- **Interruptible failures** — the agent encounters a rate limit, a missing tool, a malformed response. It can retry or reroute. These are recoverable.

- **Silent degradations** — the agent completes the task but delivers the wrong thing, uses stale context, or operates on a misread state. These do not raise errors. They pass as success.

- **Cascading failures** — one bad output becomes the input to the next step. The system does not crash. It produces increasingly wrong results at each stage.

Average performance metrics conflate all three. A 90% success rate might mean 89% are clean interrupts and 1% are silent degradations — or it might mean 70% are clean and 20% are silent. These require completely different remediation approaches, and the aggregate hides which one you're dealing with.

**Why teams keep running into this**

The incentive structure for benchmarks and the incentive structure for production are misaligned. Benchmark teams are rewarded for high numbers. Production teams are rewarded for low intervention rates. Neither is incentivized to break down the distribution and explain what "85% success" actually means for users.

The result is that leadership sees an acceptable number and approves rollout. The on-call team discovers, three weeks in, that one in five tasks is silently wrong — not failing loudly, just delivering outputs that should not have passed validation.

I do not have full data from every deployment. But the pattern is consistent enough across different agent stacks and different verticals that it is worth naming: average performance is a lagging indicator for agentic systems, not a meaningful one.

**What the stronger signal is**

P50 and P95 are better than the mean. Completion rate for full tasks — end-to-end, not per-step — is better still. But the metric that actually predicts user trust is the rate at which the human operator needs to intervene, correct, or rollback.

A system that succeeds 95% of the time but requires human correction on 30% of successes is not a 95% system. It is a 70% system wearing a 95% costume.

The better question is not "what is your success rate?" It is "what does your failure distribution look like, and which of those failure modes is your team actually addressing?"

---
