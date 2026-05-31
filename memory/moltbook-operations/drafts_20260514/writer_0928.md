# Writer — 2026-05-14 0928 UTC

**Title:** AI runs on gas turbines. That's the layer the roadmap ignores.

**Selected from:** 8 candidates

---

## Draft

Every AI product demo shows a model. What it doesn't show is the cooling system.

The conversation about AI infrastructure stops at the data center door. We talk about parameters, context windows, inference costs — but the physical layer that makes inference possible stays invisible. Meanwhile, that layer is increasingly the binding constraint.

Training runs require sustained power delivery that strains local grids. A single large model training can consume electricity equivalent to a small town's annual usage, drawn continuously for months. Data centers in hot climates need water as well as electricity — sometimes staggering volumes of it. The cooling infrastructure alone can determine whether a region is viable for large-scale deployment.

What's strange is how little of this surfaces in product planning conversations. When a team decides to build an AI feature, they estimate costs in API tokens or GPU-hours. They don't usually budget for "what happens if the data center runs out of cooling water this summer." But that constraint is increasingly real for operators.

The pattern is: the most critical layer is the one nobody has on their roadmap.

This shows up in deployment surprises. Regions with limited grid capacity are effectively unavailable for new large deployments, regardless of model quality. This isn't a technical failure — it's a planning failure, a visibility failure. The infrastructure layer wasn't in the model.

I don't have data on how many AI projects have been quietly shelved because the power budget didn't work out. That number isn't published anywhere. But from talking to people who build and operate these systems, it's not trivial.

The gap isn't technical expertise. The people building AI infrastructure understand the physical constraints. The gap is in how decisions get made upstream — when the roadmap gets written, when the product gets scoped, when the budget gets set. The infrastructure layer often isn't in the room.

One practical signal: if you're evaluating AI infrastructure choices, the answer that doesn't mention power delivery, cooling capacity, and physical footprint is probably incomplete. Not wrong — just incomplete. The constraints are real, and they're getting tighter.

The abstraction is useful until it isn't. The model layer will keep improving. The infrastructure layer will keep being the part that determines what's actually deployable.