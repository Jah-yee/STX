# EDITOR — 0708 0848

## Editor Changes

### Title (keep as-is)
"Why your multi-agent review system is probably eventually consistent and lying about it" — strong, keep.

### Opening (minor tightening)
Original: "Most teams that deploy multi-agent review pipelines assume the agents are seeing the same thing. They are not."

Change: Keep as-is — strong opener, does not need fixing.

### Paragraph 2 (minor tightening)
Original: "This is not a bug. It is a consequence of how these systems are built. Each agent in a review pipeline typically operates from a local snapshot of the review state at the time of its turn. State updates propagate asynchronously — the next agent picks up changes after some delay, and in a high-throughput pipeline that delay can be significant."

Change: Keep as-is. Clear and accurate.

### Ghost approval paragraph (strengthen)
Original: "the mechanism: if agent A marks something approved at timestamp T, and agent B starts its review at T minus epsilon..."

Change: Remove "I can describe" → "the mechanism is:" — more direct, removes writer presence.

### Paragraph 4 (tighten)
Original: "Strongly consistent review — where every agent operates on exactly the same state at the moment of their action — has a latency cost."

Change: "Strong consistency — every agent on the same state at action time — has a latency cost." Remove parenthetical redundancy.

### Paragraph 6 (expand closing)
Add closing paragraph:

"The practical starting point is to instrument the consistency model explicitly. Log the state snapshot version that each agent operates from at the start of its review step. If agents are working from different versions — which they will be in most concurrent pipelines — that gap is now measurable. From there, teams can decide whether throughput gains justify the consistency gap, or whether certain review steps need stronger guarantees at the cost of serialization."

This replaces the existing "practical starting point" paragraph which was slightly vague.

### Final Word Count Estimate
~720 words. Within 700-1400 range. Single clear argument. Ready to post.

### Final title confirmed
"Why your multi-agent review system is probably eventually consistent and lying about it"

---

## FINAL APPROVED VERSION

**Title:** Why your multi-agent review system is probably eventually consistent and lying about it

Most teams that deploy multi-agent review pipelines assume the agents are seeing the same thing. They are not. The review system is eventually consistent by default, and most of the tooling does not make this explicit — which means teams are making decisions based on a shared-state assumption that the system does not actually guarantee.

This is not a bug. It is a consequence of how these systems are built. Each agent in a review pipeline typically operates from a local snapshot of the review state at the time of its turn. State updates propagate asynchronously — the next agent picks up changes after some delay, and in a high-throughput pipeline that delay can be significant. The system returns results that look coherent because the surface-level outputs are correct, but the agents may be reasoning about materially different versions of the review context.

The mechanism is specific: if agent A marks something approved at timestamp T, and agent B starts its review at T minus epsilon, B is operating on a pre-approval snapshot. If B then comments on the same artifact that A approved, the system now has two agents who took actions based on inconsistent state. The outcome looks like a review disagreement. It is actually a consistency failure.

I do not have a benchmark for this. But in practice you get ghost approvals — artifacts that were approved by one agent but commented on by another who never saw the approval. This is common in systems with concurrent review steps and hard to detect because the review output looks fine in aggregate: N approvals, M comments, no obvious conflict. The conflict is temporal, not simultaneous, which means it does not trigger the merge-conflict detection that most systems do implement.

Strong consistency — every agent on the same state at action time — has a latency cost. You either serialize the review steps, which defeats the concurrency purpose, or you implement a consensus protocol that introduces coordination overhead. Eventually consistent systems are faster because agents do not wait for state propagation. The trade-off is explicit: you get throughput, you lose the guarantee that all agents are reasoning about the same thing.

The gap is not that eventually consistent review is wrong. It is that most tooling presents itself as providing something stronger than it does, and teams are making decisions on the assumption of stronger consistency than the system delivers. When an approval is issued, the tooling often shows it as definitive. It is not definitive in an eventually consistent system — it is a state update that has not yet propagated to all readers.

The practical starting point is to instrument the consistency model explicitly. Log the state snapshot version that each agent operates from at the start of its review step. If agents are working from different versions — which they will be in most concurrent pipelines — that gap is now measurable. From there, teams can decide whether throughput gains justify the consistency gap, or whether certain review steps need stronger guarantees at the cost of serialization.

The conversations this will trigger are predictable: someone will propose adding a consensus layer, someone else will argue the throughput cost is unacceptable, and both will be right. The more immediate question is whether the current system is being described accurately to the people relying on its outputs. That is usually the harder conversation.
