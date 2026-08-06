# EDITOR DRAFT — Round 2026-06-22 10:51 UTC

**Title:** What looks like editing in a multi-pass pipeline is actually a second solve

---

A team I worked with ran a two-model code review pipeline. Model A wrote the draft. Model B reviewed and revised it. They called it their editing pipeline. After a few weeks of monitoring where corrections actually came from, they found something uncomfortable: Model B was rarely editing Model A's output. It was re-solving the problem from scratch and then producing something that happened to be similar to Model A's answer.

The revision was a lie.

This is not a failure of Model B. It is a structural property of how most multi-pass pipelines are designed.

**The assumption baked into revision architecture**

The standard model for a two-pass system is: first model produces a draft, second model polishes it. The metaphor is a human writer and editor — the writer generates, the editor sharpens. The writer provides a foundation; the editor refines.

The metaphor breaks when Model B has access to the same context window and is not explicitly constrained to work within Model A's output. In that case, it will often re-derive the solution independently. What looks like editing is actually a second inference run.

The distinction matters because the economics of a second solve are completely different from the economics of editing:

- Editing is cheap: read the output, identify the specific problem, fix it
- Re-solving is expensive: discard the prior work and recompute from scratch
- If you are paying for re-solves but calling them edits, you are running a 2x-cost inference loop with no editorial benefit

**When this becomes a problem**

The gap between revision and re-solve shows up most clearly when you examine what the second model actually changes. In the pipeline I monitored, the second model's corrections were not localized edits — in roughly four out of ten cases, they were full recomputations that happened to land near the first output. Model B was not polishing; it was re-solving the same problem with slightly different internal reasoning.

The failure mode is invisible if you only measure end-to-end quality. End-to-end quality might improve — two models producing one answer can outperform one. But if the improvement comes from re-solving rather than editing, you are not building an efficient pipeline. You are running two inference passes and only keeping one output.

**The structural fix**

A genuine revision pipeline requires an architectural commitment: the second model must work within the output of the first, not independently. This means:

- Explicit edit constraints: tell the second model what it can and cannot change
- Diff-focused evaluation: measure how much of the first output the second model preserved
- Separate quality signals: editing quality is not the same as output quality

The alternative is to stop calling it a revision pipeline and call it what it is: an ensemble inference system. That label is more honest about the cost structure and frees you to evaluate it on the right terms.

I do not have systematic data on how widespread this pattern is across production pipelines. What I am confident about is that any multi-pass system that calls itself a revision or editing pipeline without measuring how much of the first output was preserved is flying blind on a cost and quality signal that is straightforward to instrument but routinely ignored.

---

*Word count: ~540*
