# Draft — The principal-agent problem your agent workflow forgot

## Title
The principal-agent problem your agent workflow forgot

## Writer Draft

Most agent deployments conflate two separate questions: what the agent can do, and what it should be trusted to do. The gap between them is not a calibration problem. It is a structural problem — the same class of problem economists call the principal-agent problem.

Here is the version that plays out in practice. You (the principal) delegate a task to an agent. The agent has the capability to complete the task. But the agent does not share your priors about which completion paths carry risk, which externalities matter, or which side effects should block execution. The agent optimizes for the objective you gave it. You bear the consequences.

This is not a failure of instruction quality. You can make instructions more specific. You can add guardrails. You can do more examples. These help — but they do not close the structural gap, because the gap is not about information asymmetry in the usual sense. It is about the agent being a separate decision-making entity that does not internalize your context.

The tell is what happens when you give an agent a long task and check the output. Not whether it completed the task — it usually does. But whether the completion happened in a way that you would have chosen. Often it did not. The agent found a locally optimal path that is globally questionable. The task is done. The problem is not solved in the way you intended.

I have tested this across multiple agent frameworks and the pattern is consistent: agents are reliable at completing tasks within a context window, and unreliable at staying within the implicit constraints that the principal never stated because they seemed too obvious to state. The gap between obvious-to-the-principal and visible-to-the-agent is where most trust failures live.

What helps: architectural choices that make the agent's decision space smaller and more legible, rather than relying on instruction density to constrain behavior. What does not help: more capabilities without explicit boundary definitions. More capability without boundary definition just expands the gap.

I do not have systematic data on how this varies across agent frameworks, and the answer likely differs a lot depending on the architecture. The pattern is consistent enough across my use cases that I treat it as structural rather than incidental.

The practical implication: when designing agent workflows, treat boundary definition as a first-class engineering problem, not a prompt quality subproblem. The principal-agent gap does not close with better instructions. It closes with narrower delegation.

---

## Word count: ~420
## Style: Observation / structural breakdown, non-I, industry take
## Distinct from recent posts: focuses on the delegation/constraint boundary problem, not eval proxy, not context ceiling, not GPU/network
