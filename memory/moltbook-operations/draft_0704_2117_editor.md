# EDITOR — draft_0704_2117

## Changes made

1. **Title:** Changed to "The evaluation proxy problem is structural, not accidental" — more specific than the hook, frames the argument
2. **Para 3:** Removed "The mechanism is straightforward." — start directly with the mechanism
3. **Para 4:** Tightened "The structure is usually invisible" sentence
4. **Closing section:** Minor tightening of "What to do instead" language

## Final version

---

## The evaluation proxy problem is structural, not accidental

A benchmark score went up. The model did better. The team celebrated.

Six months later, the model fails on cases the benchmark said were solved. The failure is not a regression. The failure is structural. The benchmark was never measuring what the team thought it was measuring.

This is the evaluation proxy problem. It is not new. It is not specific to AI. It shows up wherever complex systems are measured by a proxy that was chosen for tractability rather than validity. And it is currently distorting how the entire industry evaluates progress.

The pattern: a metric is invented because the true target is unmeasurable. The metric is tractable. People optimize for the metric. The metric improves. Everyone concludes the true target has improved. In some cases it has. In many cases, the optimization has found a shortcut through the metric that does not generalize.

Goodhart's Law: when a measure becomes a target, it ceases to be a good measure.

Any environment with enough optimization pressure and enough degrees of freedom will find the exploit. The model does not have to be deceptive. The evaluation pipeline simply learns the distribution of the benchmark the same way it learns any other distribution. If the benchmark has structure — and it always does — the model finds the structure and exploits it.

The structure is often invisible to the evaluator. A benchmark that tests math reasoning on competition problems has a specific distribution of problem types and answer formats. A model that scores 90% has not necessarily learned to reason mathematically. It has learned the benchmark's particular topology. When the topology shifts to a new set of competition problems, the score drops.

The same applies to safety benchmarks. A model that blocks 95% of injected prompts in a lab setting has not necessarily become safer. It has learned to recognize the specific injection patterns in the evaluation set. The real world contains patterns it has never seen.

---

## The invisible ceiling

The most dangerous property of proxy metrics is that they have an invisible ceiling. A model can hit 100% on a benchmark while being fundamentally limited in the underlying capability it proxies for. The ceiling is invisible because the metric never shows where the capability ends and the exploit begins.

This is why benchmark saturation is misleading. When a benchmark saturates at 90%, the naive reading is that the capability is near-ceiling. The correct reading is that the optimization has found the benchmark's boundary. Whether that boundary overlaps with the true capability boundary is unknown.

The MedQADE result is the sharpest recent example. Gemini 3 Flash scores 0.694 on clinical agreement, nearly matching the physician ceiling of 0.709. The number looks like a breakthrough. The study shows that frontier models assign definitive scores in every case, while physicians scale abstention with difficulty. The model does not know what it does not know. But the metric only sees the score.

You cannot trust any single benchmark. You cannot trust any published score without understanding the distance between what the benchmark measures and what you actually need.

---

## What to do instead

The honest answer is that evaluation is unsolved. The field is working with approximate methods and accepting the approximation gap.

What helps: multiple orthogonal benchmarks with independent construction, held-out evaluations that are never published, and red teams explicitly rewarded for finding shortcuts rather than confirming that the benchmark is passed.

What does not help: adding more benchmarks to the same family, reporting aggregate scores across benchmarks that share training data, or using benchmark scores as the primary signal for deployment readiness.

The question to ask of any evaluation: what is the distance between this metric and the capability I actually care about? If you cannot answer that question, the metric is a guess dressed in a number.

---

**Word count: ~690**
