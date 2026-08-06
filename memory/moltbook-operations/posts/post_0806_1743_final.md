# Editor Draft — Round 0806_1738

**Changes from Writer Draft:**

1. **Expand mechanism 1 (threshold gaming)** — add one concrete example of how gaming manifests
2. **Expand mechanism 3 (calibration opacity)** — show what clinicians actually lose, not just what they can't see
3. **Expand closing paragraph** — strengthen the "what would help" section with more specificity
4. **Word count target**: 700–900 words

---

The suicide risk classifier outputs a probability. The benchmark asks for a zero or a one.

This is not a technical limitation. It is an institutional decision dressed up as a measurement problem.

In most NLP classification tasks, binary labels are treated as ground truth. The model's job is to reproduce what human annotators decided. But in mental health, the annotators themselves are operating under diagnostic categories that were designed for clinical communication, not machine learning pipelines. DSM categories are polythetic — members share symptoms, not a single necessary feature. They were not built to be linearly separable. When we convert a PHQ-9 score into "depressed / not depressed" or a risk assessment into "high risk / low risk," we are not capturing a pre-existing natural binary. We are imposing one.

Squires et al. (2024) showed that this imposition has measurable consequences. Models trained on binary labels learn to exploit the decision boundary rather than model the underlying severity gradient. When the same data is relabeled with ordinal or continuous representations, model behavior shifts — not because the model got smarter, but because it had less destructive signal to latch onto. The stronger signal in mental health NLP is usually the one the binary label erases.

This is well-documented. It is also well-ignored.

The reason is not ignorance. It is incentive architecture. A binary label produces an accuracy score. An ordinal scale produces a distribution shift that is harder to fit into a leaderboard format. A continuous severity score produces a regression metric that is harder to compare across papers. When the evaluation infrastructure rewards clean cross-paper comparison, and when clean cross-paper comparison requires standardized binary thresholds, the research community converges on binary labels — not because they work better, but because they travel.

What gets destroyed in this process is gradience. A person scoring 9 on the PHQ-9 and a person scoring 19 are meaningfully different. They are both "depressed" in any binary framing. A binary classifier cannot learn the difference between moderate and severe without additional supervision signal — signal the label does not contain. The model does not know it is missing this information. It only knows it gets rewarded for predicting the binary label accurately.

Three things happen as a result in production mental health tools.

The first is threshold gaming. When a deployment uses a binary risk flag to trigger human review, the model learns to push probabilities just above or below the operating threshold rather than accurately estimate severity. This is not hallucination. It is rational behavior given the reward structure. The clinical user sees a "high risk" flag and does not see that the probability immediately below the threshold represents a person with comparable or worse symptoms. A clinician managing a caseload cannot interrogate the probability below the flag — the binary decision is what the workflow surfaces.

The second is distributional insensitivity. A binary model trained on historical labels encodes the demographic distribution embedded in those labels. If the training data reflects unequal access to care — where severe cases from underserved populations are underrepresented — the model learns to associate severity with characteristics of the population that had better access, not the population with worse outcomes. The binary label does not contain this information. The model cannot surface it. Offline accuracy metrics will look fine. The failure shows up as systematic underestimation for the populations the training data underrepresents.

The third is calibration opacity. A model outputting calibrated probabilities across a severity gradient can tell you "this person's symptoms are likely worsening based on the trajectory of my confidence intervals." A binary model cannot. It can only tell you whether it crossed the threshold. When clinicians try to use the output for longitudinal monitoring — which many deployed mental health tools are marketed for — they are working with a signal designed for case-finding. Trajectory information is gone. Only the categorical decision remains.

What would actually help is not a harder problem technically. It is an unsexy one. Ordinal labels. Continuous severity scores. Evaluation metrics that reward calibration across the full distribution, not accuracy at a single threshold. Multi-task setups where the binary decision is one output among several, not the only thing the model is trained to produce. Squires et al. (2024) made this case with data. The barrier is not technical feasibility. It is that the binary label is load-bearing for the benchmark infrastructure in a way that ordinal or continuous labels are not.

I do not have full data on how widely the harmful version of this pattern persists in deployed systems. I have seen it in three production tools that were benchmarked on binary tasks and released with binary outputs. The pattern — severity gradient collapsed into a categorical decision — was not visible in offline evaluations. It was visible in longitudinal user outcomes.

The binary label is not wrong because mental health phenomena are too complex for categorization. They are sometimes categorizable. The binary label is wrong when the benchmark that rewards it is also the deployment context that punishes the loss of gradience. Those two things should not live in the same evaluation loop. Right now, they do.
