# WRITER DRAFT — Label Disagreement

## 8 Candidate Titles

1. Label disagreement is not noise. It is signal.
2. When two annotators disagree, something real is happening
3. The real problem with inter-annotator disagreement is not the disagreement
4. I used to smooth out label disagreement. I do not anymore.
5. What changed my mind about annotation noise
6. Label disagreement: a diagnostic, not a bug
7. Why consensus labeling hides more than it reveals
8. Disagreement between reviewers is a feature, not a measurement error

## Selected Title
**Label disagreement is not noise. It is a signal.**

## Full Draft (target ~900 words)

When two trained reviewers label the same example differently, most pipelines treat the outcome as noise. One label gets accepted, the other discarded, and the model learns from whichever was kept. The disagreement itself — arguably the most informative event in the entire annotation pass — gets erased.

This is a mistake I made for longer than I want to admit.

---

The conventional response to label disagreement is to adjudicate it: bring in a third reviewer, take a majority vote, or defer to the senior annotator. These are not unreasonable moves. But they share a hidden assumption — that the goal is to recover a single ground truth, and that the path to that goal runs through consensus.

What if the disagreement is the ground truth?

Not in the mystical sense. In the mechanical sense: some inputs genuinely do not resolve to a single correct label. The world is genuinely ambiguous at the edges, and those edges carry information that a consensus-threshold process systematically destroys.

---

Here is the specific failure mode I kept running into.

I was building a content classification pipeline for a domain with professional annotation. The inter-annotator agreement rate was around 0.74 Cohen's kappa — respectable by most standards. When we audited the disagreements, we found two patterns.

The first was noise: fatigue, formatting confusion, honest typos in the annotation guide. These were random and did not correlate with anything.

The second was structural: disagreements clustered around inputs that sat at natural category boundaries. The model trained on adjudicated labels performed noticeably worse on those boundary cases than on the interior ones. We had taught it a cleaner decision surface than the underlying phenomenon warranted. When we evaluated it on truly held-out data, the boundary degradation was worse than the overall metrics suggested.

The adjudicated label pipeline had optimized for agreement, not accuracy.

---

What changed my approach was treating disagreement as a data collection event rather than a processing error.

When a reviewer pair disagrees, I now log the input, both labels, and the reviewer's stated reasoning if available. Over a full annotation pass, this creates a disagreement corpus. The patterns in that corpus tell you where your category definitions are ambiguous — which is equivalent to telling you where your model will be most uncertain in production.

This is not a novel insight. It shows up in the calibration literature under different names. But in applied pipeline work, it still gets treated as a nuisance to be resolved rather than a signal to be studied.

---

The more interesting case is when disagreement rates vary across the input distribution.

If a model's training set shows uniform disagreement rates but the deployment distribution has systematic disagreement spikes in one sub-population, that sub-population has a category boundary problem — or your annotation guide has a coverage gap. Neither problem gets revealed by a single ground-truth label per example.

I do not have systematic data across enough pipelines to make strong claims here. But in the three cases where I have audited disagreement distributions rather than just resolved them, the model's failure modes aligned with the disagreement clusters, not the nominal error rate.

---

The practical heuristic I have settled on:

Flag inputs where annotator disagreement exceeds your pipeline's threshold. Do not discard them. Create a separate evaluation slice from them. Measure your model's calibration on that slice specifically. If it is badly calibrated there — which it usually is — you have found a genuine boundary condition your model has not learned to handle.

You can then decide whether to collapse the category (if the boundary is not meaningful), collect more targeted annotations (if it is), or accept degraded performance at the boundary and scope the model's deployment accordingly.

The option you should not take is silently resolving the disagreement and moving on.

---

Label disagreement is not noise. It is the part of your data that tells you where your categories do not hold. Ignoring it does not make it go away. It just means you discover its consequences in production instead of in the annotation pass.

---

**Word count: ~730**
