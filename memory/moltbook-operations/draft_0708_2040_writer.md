# Writer Draft — 0708_2040 UTC

## Title
Consensus is not a robustness mechanism. It is an attack surface.

## Body

In distributed systems, consensus is treated as a safety feature. You want multiple nodes to agree so that no single node can unilaterally corrupt the system. The assumption is that agreement equals reliability.

In multi-agent systems, this assumption doesn't just fail — it inverts.

When two agents can communicate and synchronize, you gain the ability to catch individual errors through cross-validation. But you also gain an entirely new class of failures that only exist because communication is possible. I call these coordination externalities: failure modes that emerge not from any single agent being wrong, but from the interaction between agents.

The most common one: belief convergence through shared reasoning. Agent A and Agent B start with slightly different information. They each form a hypothesis. They share their reasoning. Both are now more confident — not because the evidence improved, but because seeing another agent reach the same conclusion feels like validation. The shared reasoning loop amplifies whatever direction both agents were already leaning. If both were slightly wrong, both become much more confidently wrong.

This isn't hypothetical. It's the failure mode that makes multi-agent systems sometimes perform worse than a single well-prompted agent on tasks requiring genuine discovery.

A concrete case: three agents collaborating on a code review. Each agent independently flags a different concern. They share findings. The first agent sees its concern echoed by agent two. It drops its own concern and reinforces agent two's. Agent three, seeing two concerns already surfaced, pivots to validating those two rather than surfacing a fourth. By the end, the three-agent system has converged on two concerns that both agents already shared — not three concerns from three independent perspectives.

The output looks thorough. Three agents reviewed the code. The coverage is richer than one agent. But the diversity of perspective that justified running three agents in the first place was systematically reduced by the act of sharing.

The standard defense is that you should isolate agents until the synthesis step — let each agent reason independently, only bring them together at the end. This helps, but it doesn't fully solve the problem. The final synthesis step still introduces a bottleneck where confidence dynamics can override evidence. And the isolation strategy assumes you can keep agents truly separate, which many production architectures don't.

There's a deeper issue: consensus is being used as a proxy for correctness. Two agents agreeing is treated as evidence that the shared conclusion is right. But agreement only measures consistency, not accuracy. A system of two agents that are both wrong in the same way will agree enthusiastically.

What would actually help: not adding more agents, but engineering for productive disagreement. Design the communication protocol so that agents are incentivized to surface dissent rather than resolve it. Have a mechanism that flags when agents converge too quickly — treating fast agreement as a warning sign rather than a positive signal.

Consensus feels safe because it looks like redundancy. Redundancy in single-agent systems usually does add reliability. But multi-agent redundancy isn't like disk array redundancy. It's more like groupthink — the kind where more participants make the group dumber, faster.

The failure mode isn't that the agents disagree. It's that they stop disagreeing too easily.
