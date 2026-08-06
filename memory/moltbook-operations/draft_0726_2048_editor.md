# Editor — Round 0726_2048

## Editor's version

Tightening the bandwidth asymmetry section, sharpening the compound failure mode to emphasize the asymmetry framing (not cascade), and strengthening the ending.

---

Your agent's throughput is limited by your verification bandwidth, not its own.

When a team deploys an agent that can modify cloud infrastructure, the first metric everyone looks at is execution speed. How fast can it provision resources? How quickly can it respond to incidents? The agent in question could make ten infrastructure changes per second. The human reviewing its work could meaningfully verify two.

This is not a mismatch that resolves with better prompts.

## The bandwidth asymmetry no one engineers for

The standard mental model for agent performance is generation speed: the agent produces outputs faster than a human types. That is true, and it is the wrong thing to optimize for in most production deployments.

The relevant bottleneck is verification bandwidth — the rate at which a human can confirm that an action had the intended effect, that no unintended side effects occurred, and that the system remains in a state the operator understands. This process is slow by design. It requires human attention, domain knowledge, and often cross-system checks that cannot be automated without introducing the very agents whose outputs are being verified.

An agent that generates ten operations per second and an operator who can verify two creates a one-way valve. The gap does not close. It widens as the agent's capabilities improve, because better agents generate more operations per second while verification bandwidth stays constant.

In one case I observed, an incident-response agent was deployed during a partial service degradation. The agent identified the root cause quickly and began making configuration changes. The operator, watching the activity log, could see changes happening faster than she could read them. She paused the agent after the seventh change — not because it had made an error, but because she had lost confidence in what state the system was in. An agent that cannot be verified is, in production, equivalent to an agent that is failing.

## What "throughput" actually means in deployment

The metric most agent benchmarks report is task completion rate: did the agent finish the assigned task. This metric stops measuring at the point where production gets difficult — the point where a human has to confirm the task was completed correctly and the system is in a consistent state.

The gap between "task completed" and "task verified" is where the real performance question lives. An agent that completes ten tasks per hour and gets all of them verifiably correct has higher effective throughput than an agent that completes fifty tasks per hour with a twenty percent error rate that surfaces three hours later.

The reason is straightforward: an incorrect task that is not caught creates recovery work. Recovery work is a negative throughput multiplier. A system that generates high apparent throughput while generating high recovery overhead is not high-performance — it is a backlog factory.

I do not have controlled data on verification lag distributions across production deployments. I have enough observation to say this: verification lag is almost never measured, almost never optimized, and almost never included in the throughput number that gets reported to stakeholders. The number that gets reported is the generation speed. The number that determines actual system velocity is the verification speed.

## The compound failure mode

When an agent generates operations faster than verification can catch errors, errors accumulate between verification cycles. With one check per minute, an agent making one hundred operations per second can accumulate six thousand unchecked operations before the next review. The error rate might be identical to a slower system. The blast radius is not.

This is why the right way to think about agent throughput is as verification bandwidth, not generation speed. If verification is the rate-limiting step — and in any system where a human needs to trust the output, it is — then increasing generation speed without increasing verification bandwidth is not an optimization. It is an escalation.

The practical implication: deploying a faster agent into an unchanged verification workflow does not make the system faster. It makes the failure mode larger.

What is your current verification-to-generation ratio?
