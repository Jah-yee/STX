# EDITOR — draft_0618_0821

## Changes

1. **Opening**: Keep first paragraph but tighten. "A trap built on averaged environments" is good but could be sharper.

2. **Paragraph 2**: Keep as-is — strong.

3. **Body Structure**: Keep 4 sections. Compress the "What to Do About It" section — last two sentences are repetitive.

4. **Ending**: The closing question is strong. Add one sentence before it to sharpen the payoff.

## Final Post

---

**The coordination gap: why modular agents sometimes beat joint ones**

The assumption that joint training always beats modular training in multi-agent systems is a trap built on averaged environments.

The coordination gap — the performance delta between jointly trained and modularly trained agents — is not constant. It disappears precisely when the environment's resource constraints are tight enough that there is no room to maneuver.

This matters for anyone building agentic pipelines: the most sophisticated coordination logic collapses into noise when the bottleneck owns the schedule.

---

### The Setup

In job-shop scheduling with both production and transport resources, there are two ways to train your agents. Joint training means all scheduling agents learn together, sharing gradients and updating simultaneously. Modular training means each agent learns independently, with integration happening only at inference time via fixed rules or a lightweight coordinator.

The intuition favors joint training. If agents can see each other's decisions during training, they should learn to anticipate and complement each other. The coordination learned in training should transfer to better performance at runtime.

The data says otherwise — under specific conditions.

---

### The Coordination Gap

The gap between joint and modular training varies. When resource slack is high, joint training consistently outperforms modular baselines and dispatching rules. The agents find non-trivial complementarities that a fixed coordinator cannot discover on its own.

But in severe bottleneck environments — when transport constraints or processing times create a single dominant constraint that gates the entire schedule — the gap narrows. In some cases, modular training matches or exceeds joint training.

Why? Because when the bottleneck dominates, there is no room for the kind of inter-agent maneuvering that joint training optimizes for. The dominant constraint sets the schedule. No amount of coordination can reorder what the bottleneck has already sequenced. The sophisticated interplay between agents that joint training learned is simply never activated.

This is a structural result. It does not depend on specific learning rates or network architectures. It is a consequence of the environment having too little slack for coordination to matter.

---

### The Implication for Agentic Pipelines

Most agentic workflow research is done in environments with generous resource margins. We build pipelines that assume agents will have room to negotiate, reroute, and dynamically reallocate. Then we deploy those pipelines into production environments that are tight — constrained by rate limits, API quotas, physical dependencies, or business rules that do not bend.

In those tight environments, the coordination overhead we trained for is not just unused. It is a liability. Every inference cycle spent computing coordination signals that the environment will ignore is a cycle not spent on the bottleneck's actual needs.

---

### What to Do About It

Before investing in joint training, characterize the slack profile of your target environment. If you are deploying into a dominated bottleneck, modular training with a simple coordinator is likely sufficient. Save the gradient-sharing complexity for environments with genuine coordination opportunities.

If you cannot measure the slack profile directly, err toward modularity. A modular system that underperforms due to insufficient coordination is easier to debug and iterate on than a joint system whose complexity is structurally misaligned with its deployment environment.

Before assuming joint training will transfer, ask: what does the deployment environment's constraint profile actually look like?

---

## Sources

- [An Analysis of the Coordination Gap between Joint and Modular Learning for Job Shop Scheduling with Transportation Resources](https://arxiv.org/abs/2604.24117) — Link, Moritz Hoss, Klarmann, 2026
