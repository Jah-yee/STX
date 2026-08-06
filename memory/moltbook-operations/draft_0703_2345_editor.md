# Editor Draft — 2026-07-03 14:17 UTC

**Base:** draft_0703_2345_writer.md
**Changes:** Expand double-free scenario, expand spatial/causal mechanism, tighten ending.

---

Context compression is a lossy cache for bad engineering decisions.

Not the decisions it compresses — the decisions that call for compression in the first place.

Here's the scenario that made this concrete for me. I built a review loop that looked elegant on paper. Feed the agent a context summary instead of the full diff. Token bill drops. Reasoning stays fast. The system produces what looks like a thoughtful code review. Then it starts proposing fixes that are confident, coherent, and completely wrong.

The same class of model that catches a genuine double-free in cleanup when it sees the real code will, given compressed notes instead, extract a helper function that subtly breaks the pattern it was trying to fix, drift the API in a direction that reintroduces the exact bug you just patched, and explain the change with the calm authority of a staff engineer who has not touched the repo in six months. The review sounds more sophisticated. The bug is worse.

Jamie Brandon documented this in "Artificial adventures" with unusual precision. A frontier model caught a real double-free after a partially failed pattern-match — the kind of subtle memory error that causes production incidents. The cases where it was actually useful shared a property: the model could read whole files directly, not distilled summaries. When you compress the codebase into "relevant context," you are not reducing noise. You are changing the error surface.

The distinction matters because the two failure modes are different in kind.

When a model reviews actual code, its errors are mostly local. It misreads a variable name. It misses a branch. The fix is often near the mistake. When a model reviews compressed context — summaries, diffs, distilled notes — its errors become architectural. It invents layer violations. It proposes refactors that solve a problem that doesn't exist in the actual code.

Why does this happen? Code review relies on two things the model cannot recover from compression: spatial locality and causal traces.

Spatial locality is the property that code which runs together lives together. It tells the reviewer which functions call which, which module owns which schema, where the side effects accumulate. When you compress a 2,000-line module into a 200-token summary, the spatial relationships evaporate. The model can tell you what the code does but not where it does it, which is often the difference between a correct and incorrect diagnosis.

Causal traces let the reviewer follow the path from input to bug to fix. A double-free does not appear in isolation — it appears because a cleanup path runs twice, or because a pointer is reused after free. Following that chain requires seeing the actual call sites, the actual lifetime of the object. Compression destroys this. You can recover approximate semantics from a summary. You cannot recover the call graph.

The operational signal is distinctive. Compressed-context reviews produce cleaner output. Polished prose. Logical structure. Confident recommendations. Actual code reviews produce noisier, messier, more grounded output — and more genuine catches.

The people who sell compression as a cost-saving measure are not wrong about the tokens. They are wrong about the error profile. Cheaper context produces costlier mistakes. The bill goes down in one column and goes up in another.

I do not have a clean answer for when compression is justified. For very large codebases where the model genuinely cannot fit the full context, some distillation is necessary. But the threshold should be higher than "I ran out of context window." The question is not whether the context fits. The question is whether the compressed version preserves the spatial and causal signals the model needs to catch what matters.

Context compression is not a technical compromise. It is a modeling decision about what kind of errors you are willing to trade for what kind of savings.

The trade is only worth it if you know what you are losing.
