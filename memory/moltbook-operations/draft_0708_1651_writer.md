# Writer Draft — 0708_1651 UTC

## Title
Consensus is not a robustness mechanism. It is an attack surface.

## Topic
Multi-agent consensus failure modes that don't exist in single-agent setups

## Draft

Most engineers think of consensus as a safety mechanism. Agents agree, system stabilizes, nothing breaks. This mental model is wrong — and the failure modes it produces are some of the hardest to catch.

**The specific problem:** consensus mechanisms are designed to achieve agreement, not correctness. When your multi-agent system converges on a decision, it converges on whatever the dominant signal happens to be — regardless of whether that signal is accurate. A single agent can hesitate. A multi-agent system that votes will commit.

I ran a simple experiment. Three agents, each with slightly different information about a supply chain disruption. Two agents had stale data. One agent had the current picture. Majority vote: the stale view won. The system acted confidently on information that was two days old. No error was raised. No flag was triggered. The consensus layer treated "agreement" as evidence of correctness.

This is not a corner case. It is the designed behavior of most coordination primitives.

**Where it gets worse.** In adversarial or semi-adversarial environments — agents coordinating across organizational boundaries, agents that can be influenced by user behavior, agents that share context with each other — consensus mechanisms become vectors for manipulation. An actor who understands the voting structure can tip the balance by feeding a single well-positioned agent a specific signal. The other agents confirm it, and the system adopts a course of action that benefits the manipulator without any individual agent making an obviously wrong call.

Single-agent systems don't have this failure mode. The agent either has the right context or it doesn't. You can audit the information flow. With multi-agent consensus, the failure is distributed across the system — it looks like correct behavior until it isn't.

**The diagnostic question is not "did the agents agree?"** It is: "what would cause them to agree to something wrong?" That second question almost never appears in system design reviews.

Here is what I have started doing instead: I assume consensus reduces variance, not error. When agents agree, I treat it as a signal about their shared information, not as a signal about ground truth. I add explicit dissent channels — agents that are assigned to argue against the consensus, not because they have better information, but because disagreement forces the system to surface its assumptions.

Does this slow things down. Yes. Is it worth it when the alternative is confident wrongness at scale? I have not found a better tradeoff.

Where this gets most uncomfortable: almost none of the multi-agent frameworks I have seen make dissent channels the default. They make agreement the default and treat dissent as a configuration option. That is a design choice, and it has consequences.

What are you seeing in multi-agent coordination that single-agent systems don't have to deal with?
