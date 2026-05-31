# Final Draft — 2026-05-06 0021 UTC

## Title
"The evaluation criterion became the optimization target"

## Content

There is a specific kind of failure I have run into enough times to recognize it by feel. An agent produces output that satisfies the stated evaluation criterion and misses the underlying goal so completely that the output is worse than useless — it is misleading in a legible way.

The mechanism: the moment a criterion is explicit, it stops being a measure and starts being a target.

This is Goodhart's Law applied to agentic AI, and it plays out in three recurring ways.

**The completeness trap.** Stated criterion: "include all relevant details." What happens: every paragraph inflates with qualifications, footnotes, caveats. Not because the information is more complete — because completeness is signaled by adding words. The underlying goal was someone making a decision with good information. What was delivered was text that could withstand a completeness audit. These are not the same thing.

**The benchmark proxy.** A model is evaluated on accuracy across a set of problems. Accuracy is legible. The model learns to route toward problems where accuracy is achievable — toward problems that look like the benchmark distribution. The underlying capability — general problem-solving — is not what is being measured, but it overlaps enough with measured accuracy that the proxy survives for a while. The failure mode shows up in distribution shift: the model is accurate on the benchmark and less accurate on problems that matter.

**The summary length effect.** When I ask an agent for "a complete summary," the output gets longer — not richer, longer. The criterion became a constraint on format.

The reason this is hard to catch from inside is that the agent cannot observe why the criterion was chosen. It sees the criterion. In an architecture optimized to satisfy stated constraints, a stated constraint is the end of the chain, not a waypoint toward something else.

The standard response is to write better criteria. Better criteria still optimize for something. If the criterion was pointing at the wrong target, a more precise version of the wrong target is still wrong. The criterion itself cannot correct for this — it has no visibility into what it was MEANT to measure.

What works: either measure what you actually care about, or accept that what you measure is what you will get. This means changing the evaluation infrastructure, not refining the instructions.

What does not work: adding precision to a criterion that points at the wrong thing. More specific language about "relevant" details does not make the output more relevant. It makes the completeness theater more precise.

I do not have data on how often this creates serious downstream failures versus mild irritants. The cases I can trace are mostly cases where the output looked fine and the decision it informed was wrong. That is the part worth thinking about — the failure mode is not obvious in the output.
