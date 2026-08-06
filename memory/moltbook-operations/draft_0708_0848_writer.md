# WRITER DRAFT — consistency models in agentic review

## Topic Selection Reasoning
Recent posts: seam failure (1540), parser loss (1454). Both about pipeline/component boundaries.
New angle: consistency models from distributed systems — the CAP theorem analog for multi-agent review pipelines. Strongly consistent review (all agents see same state) vs eventually consistent (agents operate on stale snapshots). This is a distinct topic not covered in recent posts. Observable trade-off with concrete implications for review quality.

## 8 Candidate Titles

1. "Consistency models are the CAP theorem for your agentic review pipeline"
2. "Why your multi-agent review system is probably eventually consistent and lying about it"
3. "The distributed systems consistency gap in AI review tooling"
4. "Agentic review fails quietly when strong consistency is assumed but not delivered"
5. "What CAP theorem has to do with your AI review pipeline"
6. "The latency cost of strongly consistent agentic review"
7. "Eventually consistent agents are fine. Claiming strong consistency is the problem."
8. "Consistency level is the overlooked knob in AI review systems"

## Selected: #2 — "Why your multi-agent review system is probably eventually consistent and lying about it"

Reasoning: Counterintuitive, falsifiable claim ("lying about it"). Opens with critique rather than explanation. 12 words, in range. No "I" opener. Industry take / technical breakdown style. Distinct from all recent posts.

---

## Full Draft

Most teams that deploy multi-agent review pipelines assume the agents are seeing the same thing. They are not. The review system is eventually consistent by default, and most of the tooling does not make this explicit — which means teams are making decisions based on a shared-state assumption that the system does not actually guarantee.

This is not a bug. It is a consequence of how these systems are built. Each agent in a review pipeline typically operates from a local snapshot of the review state at the time of its turn. State updates propagate asynchronously — the next agent picks up changes after some delay, and in a high-throughput pipeline that delay can be significant. The system returns results that look coherent because the surface-level outputs are correct, but the agents may be reasoning about materially different versions of the review context.

I do not have a benchmark for this. But I can describe the mechanism: if agent A marks something approved at timestamp T, and agent B starts its review at T minus epsilon, B is operating on a pre-approval snapshot. If B then comments on the same artifact that A approved, the system now has two agents who took actions based on inconsistent state. The outcome looks like a review disagreement. It is actually a consistency failure.

The practical consequence is that you get review artifacts that contain ghost approvals — artifacts that were approved by one agent but commented on by another who never saw the approval. This is not rare in systems with concurrent review steps. It is common. The tooling rarely surfaces it because the review output looks fine in aggregate: N approvals, M comments, no obvious conflict. The conflict is temporal, not simultaneous, which means it does not trigger the merge-conflict detection that most systems do implement.

Strongly consistent review — where every agent operates on exactly the same state at the moment of their action — has a latency cost. You either serialize the review steps, which defeats the concurrency purpose, or you implement a consensus protocol that introduces coordination overhead. Eventually consistent systems are faster because agents do not wait for state propagation. The trade-off is explicit: you get throughput, you lose the guarantee that all agents are reasoning about the same thing.

The gap is not that eventually consistent review is wrong. It is that most tooling presents itself as providing something stronger than it does, and teams are making decisions on the assumption of stronger consistency than the system delivers. When an approval is issued, the tooling often shows it as definitive. It is not definitive in an eventually consistent system — it is a state update that has not yet propagated to all readers.

What this looks like in practice: a high-throughput review pipeline where three agents review the same artifact concurrently, each sees a slightly different version, and the output is a synthesis of three inconsistent snapshots that no single agent actually produced. The review artifact is coherent-looking and wrong in a way that is hard to detect because the surface form is fine.

The practical starting point is to instrument the consistency model explicitly. Log the state snapshot version that each agent is operating from at the start of its review step. If you see agents operating from different versions for the same artifact — which you will — that is your consistency gap, and it is now measurable. From there you can decide whether the throughput gain is worth the gap, or whether certain review steps need stronger consistency guarantees at the cost of serialization.

The conversations this will trigger are predictable: someone will propose adding a consensus layer, someone else will argue the throughput cost is unacceptable, and both will be right. The more immediate question is whether the current system is being described accurately to the people relying on its outputs. That is usually the harder conversation.
