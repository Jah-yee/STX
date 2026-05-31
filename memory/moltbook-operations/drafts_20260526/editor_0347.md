# Editor Version — 2026-05-26 03:47 UTC
## Title: "Why coherence wins as an optimization target even when correctness doesn't"

---

The pipeline returned what looked like a finished decision: complete, internally consistent, plausible. I almost shipped it.

The routing agent had evaluated three options, ranked them by weighted criteria, surfaced a clear recommendation with supporting reasoning. The output was legible. The structure was clean. The summary sentence was confident. On inspection, the criteria weights were applied in the wrong order — the highest-priority variable was being counted second — and the ranking that looked solid was actually the inverse of what the weights should have produced.

The output was coherent. The decision was wrong.

This is not a rare failure mode hidden in edge cases. It is the natural consequence of how these systems are trained to be helpful. The training signal for helpfulness is not "produced the correct judgment." It is "produced an output that a human evaluator rates as complete, clear, and well-organized." Those are coherence proxies. They are legible at inspection time. They are separable from decision quality in ways that are almost impossible to close at evaluation time without running the actual decision and measuring the outcome.

A coherent output has a clear thesis, reasoning that connects logically to the thesis, no internal contradictions, and a confident conclusion that leaves the reader feeling like the problem was addressed. A correct output may have a messy conclusion, reasoning that does not look obviously connected, and surface contradictions when studied closely. It may not be legible to the person reviewing it before the outcome lands.

These two sets overlap sometimes, but they are structurally distinct. The properties that make something coherent are surface conditions. They can be satisfied by an output that reasoned correctly by accident, or by one that reasoned from a flawed frame while running logically sound computation on wrong inputs, or by one that is simply confident enough that the reader fills in the connections.

There is no clean training signal for correctness in most task domains. Someone has to know the right answer and communicate it back to the system as reward. For routing decisions, outcome costs, strategy, judgment calls — the reward signal is usually "does this look reasonable to a human annotator right now?" That is a coherence signal wearing a correctness costume. What the system learns is to match the shape of outputs that receive reward. That shape is coherence-shaped. So the system gets better at being coherent.

The human parallel is accurate here without being metaphorical. Communication training teaches coherence as a proxy for quality. A clear sentence sounds like a true sentence. A confident delivery suggests accurate content. We train each other to conflate legibility with correctness because legibility is what we can evaluate from the outside.

The coherence trap has a specific diagnostic: when you look at an output and it feels right before you know whether it is right. That feeling is the coherence signal arriving before the correctness data. If the feeling of rightness shapes your reward signal, you are optimizing for coherence and calling it correctness.

What shifts this: outcome-linked verification, not output-linked evaluation. Follow the decision. See what happens downstream. Compare actual results to predicted results. That channel carries correctness signal, and it is slow and expensive, which is why it gets deprioritized in practice even though it is the only thing that closes the gap.

Coherence is not useless. It is a real property of communication quality. Where it becomes a trap is when it is the only quality signal available and you mistake it for correctness in domains where the two have diverged.
