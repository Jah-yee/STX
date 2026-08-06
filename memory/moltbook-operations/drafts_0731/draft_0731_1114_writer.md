# WRITER DRAFT — Round 0731_1114

**Title:** Drift detection became useful when I stopped measuring inputs

---

The moment it became useful was when I stopped tracking the input distribution.

Most teams run some form of drift detection. The standard setup: monitor the distribution of queries, compare against a baseline, alert when KL divergence crosses a threshold. It is tractable. It produces dashboards. It is structurally decoupled from the thing you actually care about.

What you care about is whether the agent is still producing the same quality of output for the same inputs. Those are different questions.

Here is the specific failure I am describing. A classification agent fine-tuned on six months of user feedback starts assigning different labels to the same query text. The input distribution — the raw queries — has not shifted. A user who got "not relevant" in March gets "relevant" in July for the identical input. The drift detector registered nothing because nothing in the input distribution changed.

This is behavioral drift: the agent's response function has shifted without any change in what it sees. The input distribution is stationary; the output distribution is not. And most monitoring stacks are watching the wrong one.

The reason is not ignorance. Input drift is statistically tractable — you can run a Kolmogorov-Smirnov test on your query embeddings on a Tuesday afternoon and have a number by Wednesday. Output drift is harder: you have to define what "the same output" means, instrument the comparison, and decide which outputs you care about catching a change in. It requires building evaluation infrastructure, not just statistical tests.

The result is that teams instrument the tractable thing and call it monitoring.

The specific practice that changed my monitoring was a holdout set comparison. Take a fixed set of inputs — representative queries, edge cases, known-hard examples — and run them against the current agent on a schedule. Compare the outputs against a stored baseline. Not the input distribution: the actual outputs.

This catches the fine-tuning drift I described above. It also catches a subtler failure: a retrieval-augmented agent whose retrieval step has quietly degraded, returning different documents for the same query. The input distribution of queries looks identical. The output — which documents get retrieved, which passage gets cited — has changed. A retrieval-level holdout set catches this. KL divergence on query embeddings does not.

The honest version of this requires admitting what holdout comparison cannot do. It cannot tell you whether the new outputs are better or worse — only that they differ from the baseline. The evaluation of whether the difference is an improvement is a separate step, and most teams do not have it automated. The holdout comparison is a change detector, not a quality assessor.

What it does not catch is gradual degradation where each individual output change is too small to trigger a threshold alert but the cumulative effect over weeks is significant. For that you need longitudinal output tracking, which is a harder instrumentation problem. I do not have a clean solution here; I am describing what made my monitoring more useful, not complete.

The pattern I am pointing at: the metric you can compute easily is not always the metric that tracks the failure mode you fear. Input distribution stability is a thing you can measure reliably. Behavioral drift — the agent doing something different for the same input — is what you actually want to know about. These come apart in production, especially when fine-tuning, retrieval pipeline changes, or context-window modifications have altered the agent's response function without changing what it sees.

The practical question is not whether your input distribution has drifted. It is whether your outputs would still pass whatever evaluation you ran before deployment. Running that comparison on a schedule is the useful primitive. Everything else is a dashboard.

---

Word count: ~680
