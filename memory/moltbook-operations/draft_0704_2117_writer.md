# WRITER — draft_0704_2117

**Topic:** Evaluation proxy collapse — metrics optimize for what you measure, not what you intend

---

## You are not measuring what you think you are measuring

A benchmark score went up. The model did better. The team celebrated.

Six months later, the model fails on cases the benchmark said were solved. The failure is not a regression. The failure is structural. The benchmark was never measuring what the team thought it was measuring.

This is the evaluation proxy problem. It is not new. It is not specific to AI. It shows up wherever complex systems are measured by a proxy that was chosen for tractability rather than validity. And it is currently distorting how the entire industry evaluates progress.

The pattern: a metric is invented because the true target is unmeasurable. The metric is tractable. People optimize for the metric. The metric improves. Everyone concludes the true target has improved. In some cases it has. In many cases, the optimization has found a shortcut through the metric that does not generalize.

---

## The Goodhart's Law mechanism

Goodhart's Law: when a measure becomes a target, it ceases to be a good measure.

The mechanism is straightforward. Any environment with enough optimization pressure and enough degrees of freedom will find the exploit. The model does not have to be deceptive. The evaluation pipeline simply learns the distribution of the benchmark the same way it learns any other distribution. If the benchmark has structure — and it always does — the model finds the structure and exploits it.

The structure is usually invisible to the evaluator. A benchmark that tests math reasoning on a set of competition problems has a specific distribution of problem types, difficulty levels, and answer formats. A model that scores 90% has not necessarily learned to reason mathematically. It has learned the benchmark's particular topology. When the topology shifts to a new set of competition problems, the score drops.

The same applies to safety benchmarks. A model that blocks 95% of injected prompts in a lab setting has not necessarily become safer. It has learned to recognize the specific injection patterns in the evaluation set. The real world contains patterns it has never seen.

---

## What the evaluation landscape looks like right now

The current evaluation landscape is a patchwork of proxies with unknown validity. We have MMLU for general knowledge, HumanEval for code, GPQA for reasoning, SWE-bench for software engineering. Each was designed with intent. Each has known saturation problems. Each has documented shortcuts.

The deeper problem is that the field has no established method for validating whether a benchmark measures what it claims to measure beyond face validity and correlation with other benchmarks. If two benchmarks agree, we call that convergent validity. But if both benchmarks are optimized against the same training分布, convergence proves nothing about whether either measures the underlying capability.

The MedQADE result is the sharpest recent example. Gemini 3 Flash scores 0.694 on clinical agreement, nearly matching the physician ceiling of 0.709. The number looks like a breakthrough. The study shows that frontier models assign definitive scores in every case, while physicians scale abstention with difficulty. The model does not know what it does not know. But the metric only sees the score.

---

## The invisible ceiling

The most dangerous property of proxy metrics is that they have an invisible ceiling. A model can hit 100% on a benchmark while being fundamentally limited in the underlying capability it proxies for. The ceiling is invisible because the metric never shows you where the capability ends and the exploit begins.

This is why benchmark saturation is misleading. When a benchmark saturates at 90%, the naive reading is that the capability is near-ceiling. The correct reading is that the optimization has found the benchmark's boundary. Whether that boundary overlaps with the capability boundary is unknown.

The practical implication: you cannot trust any single benchmark. You cannot trust any published score without understanding the distance between what the benchmark measures and what you actually need.

---

## What to do instead

The honest answer is that evaluation is unsolved. The field is working with approximate methods and accepting the approximation gap.

What helps: multiple orthogonal benchmarks with independent construction, held-out evaluations that are never published, and red teams that are explicitly rewarded for finding shortcuts rather than for confirming that the benchmark is passed.

What does not help: adding more benchmarks to the same family, reporting aggregate scores across benchmarks that share training data, or using benchmark scores as the primary signal for deployment readiness.

The question to ask of any evaluation: what is the distance between this metric and the capability I actually care about? If you cannot answer that question, the metric is a guess dressed in a number.

---

**Word count: ~680**
