# WRITER — draft_0618_0821

## Topic
Multi-agent job-shop scheduling: why joint training doesn't always beat modular training, and what the coordination gap reveals about when to pay for complexity.

## Thesis
Joint training in multi-agent scheduling has a hidden failure mode: when the environment has a single dominant bottleneck, the coordination you paid for during training becomes pure overhead. Modular training is sufficient — and sometimes better — in severely constrained environments.

## Candidate Titles (8)
1. When coordination becomes overhead: what joint training gets wrong about bottlenecks
2. Joint training is not a universal win for multi-agent scheduling
3. The coordination gap: why modular agents sometimes beat joint ones
4. Slack is not a given — coordination breaks when the bottleneck dominates
5. Why your multi-agent scheduler is over-engineered for its own environment
6. Most joint training gains disappear when the floor is tight enough
7. Coordination is a luxury of slack. In a bottleneck, it is just overhead.
8. The coordination gap: when joint training underperforms dispatching rules

## Selected Title
**"The coordination gap: why modular agents sometimes beat joint ones"** — clean, non-I, question-adjacent observation form.

## Opening Hook (3 sentences)
The assumption that joint training always beats modular training in multi-agent systems is a trap built on averaged environments.

The coordination gap — the performance delta between jointly trained and modularly trained agents — is not constant. It disappears precisely when the environment's resource constraints are tight enough that there is no room to maneuver.

This matters for anyone building agentic pipelines: the most sophisticated coordination logic collapses into noise when the bottleneck owns the schedule.

## Body

### The Setup
In job-shop scheduling with both production and transport resources, there are two ways to train your agents. Joint training means all scheduling agents learn together, sharing gradients and updating simultaneously. Modular training means each agent learns independently, with integration happening only at inference time via fixed rules or a lightweight coordinator.

The intuition favors joint training. If agents can see each other's decisions during training, they should learn to anticipate and complement each other. The coordination learned in training should transfer to better performance at runtime.

The data says otherwise — under specific conditions.

### The Coordination Gap
The gap between joint and modular training varies. When resource slack is high, joint training consistently outperforms modular baselines and dispatching rules. The agents find non-trivial complementarities that a fixed coordinator cannot discover on its own.

But in severe bottleneck environments — when transport constraints or processing times create a single dominant constraint that gates the entire schedule — the gap narrows. In some cases, modular training matches or exceeds joint training.

Why? Because when the bottleneck dominates, there is no room for the kind of inter-agent maneuvering that joint training optimizes for. The dominant constraint sets the schedule. No amount of coordination can reorder what the bottleneck has already sequenced. The sophisticated interplay between agents that joint training learned is simply never activated.

This is a structural result, not a statistical one. It does not depend on the specific learning rates or network architectures. It is a consequence of the environment having too little slack for coordination to matter.

### The Implication for Agentic Pipelines
Most agentic workflow research is done in environments with generous resource margins. We build pipelines that assume the agents will have room to negotiate, to reroute, to dynamically reallocate. Then we deploy those pipelines into production environments that are tight — constrained by rate limits, API quotas, physical dependencies, or business rules that do not bend.

In those tight environments, the coordination overhead we trained for is not just unused. It is a liability. Every inference cycle spent computing coordination signals that the environment will ignore is a cycle not spent on the bottleneck's actual needs.

This is the coordination gap at the agentic level: the mismatch between the sophistication of the trained coordination and the actual slack available in the deployment environment.

### What to Do About It
Before investing in joint training, characterize the slack profile of your target environment. If you are deploying into a dominated bottleneck — a single tight constraint that gates the entire workflow — modular training with a simple coordinator is likely sufficient. Save the gradient-sharing complexity for environments with genuine coordination opportunities.

If you cannot measure the slack profile directly, err toward modularity. A modular system that underperforms due to insufficient coordination is easier to debug and iterate on than a joint system whose complexity is structurally misaligned with its deployment environment.

The goal is not to maximize coordination sophistication. It is to match coordination complexity to environmental slack.

### The Honest Boundary
I do not have systematic data on what fraction of real production environments are slack-free enough to invalidate joint training gains. This varies enormously by domain. A GPU cluster scheduling jobs has different slack profiles than a logistics network routing deliveries. The point is not that joint training is useless — it is that the gains are conditional, and the conditions are not always present in production.

Before assuming joint training will transfer, ask: what does the deployment environment's constraint profile actually look like?

---

## Style
Industry take / systems observation. Not a literature review. Single clear argument.

## Word Count Estimate
~720 words.
