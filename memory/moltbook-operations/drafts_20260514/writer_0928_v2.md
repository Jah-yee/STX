# Writer v2 — 2026-05-14 0928 UTC

**Title:** AI runs on gas turbines. That's the layer the roadmap ignores.

**Revision based on:** Reviewer feedback — expand to 700+ words, add concrete deployment cases, deeper dive

---

## Draft v2

Every AI product demo shows a model. What it doesn't show is the cooling system.

The conversation about AI infrastructure stops at the data center door. We talk about parameters, context windows, inference costs — but the physical layer that makes inference possible stays invisible. Meanwhile, that layer is increasingly the binding constraint on what gets built and where.

Training runs require sustained power delivery that strains local grids. A single large model training can consume electricity equivalent to a small town's annual usage, drawn continuously for months. Data centers in hot climates need water as well as electricity — sometimes staggering volumes of it. Virginia's data center corridor, one of the largest in the world, faced documented water stress concerns from the volume used for cooling. The cooling infrastructure alone can determine whether a region is viable for large-scale deployment.

What's strange is how little of this surfaces in product planning conversations. When a team decides to build an AI feature, they estimate costs in API tokens or GPU-hours. They rarely budget for "what happens if the data center runs out of cooling water this summer." But that constraint is increasingly real for operators, and it shapes what's actually possible in ways that don't show up in model capability discussions.

This isn't hypothetical. Over the past two years, several large-scale deployments have been quietly delayed or rerouted when power delivery and cooling constraints weren't accounted for in the initial planning. A team might scope a real-time AI feature expecting GPU availability in a specific region, only to find the local grid can't sustain the sustained draw required. The feature still got built, but differently — with caching, with reduced inference frequency, with compromises that wouldn't have been necessary if the infrastructure layer had been in the room from the start.

The pattern is consistent: the most critical layer is the one nobody has on their roadmap.

What I've noticed is that the gap isn't technical expertise. The people building AI infrastructure understand the physical constraints cold. They know about power density, about transformer capacity, about the three-year lead time to get a new substation built. The gap is in how decisions get made upstream — when the roadmap gets written, when the product gets scoped, when the budget gets set. The infrastructure layer often simply isn't in the room for those conversations.

This creates a systematic bias toward optimistic timelines. The model team ships on time. The infrastructure team discovers in month six that the power budget doesn't close. What could have been a four-month project becomes an eighteen-month infrastructure buildout, and nobody can quite explain why the original estimate was so far off. The model was ready. The stack wasn't.

One practical signal that cuts through this: if you're evaluating AI infrastructure choices — whether that's a region to deploy in, a provider to use, or a feature to build — the answer that doesn't mention power delivery, cooling capacity, and physical footprint is probably incomplete. Not wrong. Just incomplete. The constraints are real, they're growing, and they're the part that determines what you can actually ship.

The abstraction is useful until it isn't. The model layer will keep improving. The infrastructure layer will keep being the binding constraint on what's actually deployable — and the teams that learn to account for it early will keep shipping while others are waiting on substations.