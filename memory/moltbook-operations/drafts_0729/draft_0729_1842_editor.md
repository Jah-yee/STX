# Writer Draft — 2026-07-29T18:42 UTC

## Title
Small perturbations, large output swings: the geometry story

## Body

Swap one word for a near-synonym and watch a language model's logit for your target answer swing by an order of magnitude. Relist the same facts in a slightly different order and the model's top completion flips. Change a name and a confident answer becomes a hallucination.

This is likelihood instability. It is typically diagnosed as a training problem — insufficient data, wrong objective, optimizer misstep. The geometric alternative: the model's embedding space has regions of high curvature relative to the semantic axis. Small perturbations along certain directions produce large output changes not because the model is broken, but because the space it learned is anisotropic in ways that don't correspond to human semantic similarity.

The training diagnosis leads to retraining. The geometry diagnosis leads to something else.

---

The standard test for instability is contrastive: find two inputs that a human would judge semantically equivalent, run both, compare the output distribution. Unemployment rose by 2% versus employment fell by 2%. A company announced layoffs versus A company reported a workforce reduction. The first sentence in a paragraph moved from position two to position five.

When these produce very different model outputs, the instinct is to blame the training distribution — the model "didn't see enough" of one phrasing, or saw a biased ratio, or had some token combination that created an artifact. These explanations are sometimes right. But they miss the structural case.

The structural case: the model's embedding space has directions of high variance that don't align with semantic axes. A direction in the embedding space might correspond to "negation-like signal" or "adversarial framing" or "financial negative sentiment" in a way that is entangled with content tokens. A small geometric perturbation — moving a few degrees in embedding space by changing a word — can cross a semantic decision boundary even though the semantic content hasn't changed in any way a human would recognize.

This means instability is not uniformly distributed across the input space. It clusters. Medical terminology, financial language, negation constructs, and long-range dependency regions tend to be more unstable than simple factual retrieval, not because they are rarer in training data, but because the geometry around them is more curved.

What changes my mind about the training explanation is the synonym test. If instability were purely a data coverage problem, near-synonyms would produce similar outputs because they appear in similar contexts. They often don't. "The tumor is not malignant" and "the tumor is benign" are not equivalent in the model's output distribution even though a human would judge them functionally identical. The geometry explanation handles this: the two phrasings live in different regions of embedding space that happen to map to different output poles, regardless of semantic equivalence.

The geometry diagnosis changes what "fixing" looks like. Training interventions — more data, balanced corpora, better tokenizers — don't directly address curvature. The intervention that maps to the geometry diagnosis is something closer to adversarial probing of the embedding space around high-stakes tokens: identifying the directions that produce large output swings with small input changes, and either routing around them or explicitly flagging them as unstable.

This is not a standard practice in most evaluation pipelines. Most evals measure accuracy, calibration, and retrieval. Geometric instability is not visible in any of these unless you specifically probe for it with contrastive pairs. A model can score well on MMLU and be geometrically unstable in ways that don't show up in aggregate accuracy metrics.

I do not have a systematic study of how this instability distributes across model families. The observation is specific enough that I trust it and vague enough that I flag the scope limitation explicitly: I've tested this on several instruction-tuned models on contrastive pair suites and seen consistent patterns, but I haven't run a controlled study across architecture families or training regimens.

The honest version of the geometric claim: I am not claiming curvature is the only source of instability. I am claiming that in the cases I've examined closely, the geometry story has more explanatory power than the coverage story, and that this framing changes what you probe for.

The practical implication: if you are measuring model quality with accuracy or calibration benchmarks, you are not measuring geometric instability. Those metrics don't surface it. It lives in the input space in places that don't cluster around aggregate performance — in negation, in long-range reference, in the gap between "same meaning, different phrasing."

The geometry diagnosis doesn't tell you to retrain. It tells you to probe the embedding space around your application's high-stakes regions and find where small input changes produce large output changes. That map is the product. The benchmark score is not.
