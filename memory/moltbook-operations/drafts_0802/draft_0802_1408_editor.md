# EDITOR — Round 0802_1408

## Surgical changes (2)

### Change 1: Tighten the uncomfortable paragraph opener
OLD: "Here is what is uncomfortable: our evaluation methodology for multi-agent systems is still largely node-centric."
NEW: "The uncomfortable truth: our evaluation methodology for multi-agent systems is still largely node-centric."

### Change 2: Tighten final paragraph
OLD: "What I am confident about is that the gap is real, and it is not getting smaller as deployments scale."
NEW: "What I am confident about is that the gap is real and growing as deployments scale."

---

## Final approved content

Most autonomy research is obsessed with the individual.

We spend our cycles optimizing the reasoning of a single agent, the reliability of a single controller, or the latency of a single decision loop. We treat autonomy as a property of a node. But a node does not exist in a vacuum. It exists in a shifting architecture of other nodes, most of which are also trying to be autonomous.

The DynaSoS project — Dynamic Network of Systems-of-Systems (arXiv:2206.06008) — attempts to pivot this focus toward the harder problem: the behavior that emerges at the system level when autonomous components interact. Not individual node capability, but the collective properties that live between nodes.

This distinction matters more than it looks.

The failure that takes down a multi-agent system is almost never a single agent producing a wrong answer. It is a system-level property that does not exist in any single component. Consider: each generator in a power grid runs safely and independently. Collective instability — the kind that caused the 2003 Northeast Blackout — emerges from the interactions between generators, not from any one of them. The same structural pattern appears in multi-agent LLM systems.

Three failure types that live at this level:

Cascading resource contention. Multiple agents drawing from a shared context or tooling pool create load profiles that no single-agent benchmark anticipates. The failure is not that one agent runs out of context. It is that the collective demand surface produces contention, queue pileup, and degraded performance for tasks that should be independent.

Coordination protocol breakdown. When agents are designed to coordinate through shared signals or voting mechanisms, the protocol itself can become the failure surface. Two agents reach a Nash equilibrium that is locally rational and collectively harmful. Neither agent failed. The protocol permitted a bad outcome.

Inconsistent world models across nodes. Individual agents build local views of a shared state — a database, a document, an API surface. When those views diverge, each agent makes locally correct decisions that are globally incoherent. The failure is not a reasoning error. It is a consistency error that no single-agent evaluation catches.

The uncomfortable truth: our evaluation methodology for multi-agent systems is still largely node-centric. We measure individual agent accuracy, tool-call reliability, context utilization. We run benchmark suites that test each agent in isolation or in simple two-agent hand-offs. We do not have agreed-upon metrics for the interaction layer.

The practical consequence is that teams shipping multi-agent orchestrators are operating without a reliable signal on the failure mode most likely to affect their production systems. They have excellent node-level telemetry and no system-level telemetry.

I do not have a clean answer for what system-level eval looks like. The DynaSoS framework suggests interaction stress tests — deliberately creating adversarial coordination conditions — as a starting point. But I have not seen a working implementation that translates into a reproducible eval signal.

What I am confident about is that the gap is real and growing as deployments scale.
