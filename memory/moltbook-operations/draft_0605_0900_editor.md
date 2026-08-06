## Editor — draft_0605_0900

**Original title:** Best-of-N is an ensemble in disguise, not a model score

**Editor notes:**
- Tighten opening — drop "Ask a simple question" setup, go straight to observation
- Cut closing paragraph — it restates rather than lands. The "broader point" about training-time vs inference-time ensembles adds scope creep without a new insight
- Minor: "I do not have full data" disclaimer is appropriate, keep
- Target: ~450 words

---

**Revised:**

When a paper reports a state-of-the-art benchmark score, one question usually goes unasked: did they generate one answer or many? If Best-of-N was used — generating N completions and reporting the best — the score is not the model's. It is the output of an N-way committee, assembled at inference time and passed off as a single result.

An ensemble is not a weakness. But it is not a single model either.

**How Best-of-N works.** The model generates N outputs for the same prompt. The evaluator selects the one that scores highest on the target metric, then reports that metric as if it came from a single model. The issue is that N answers were evaluated but only one was selected and reported. The score reflects the best of N, not the average. If N=16 and the task is binary correct/incorrect, the probability of at least one correct answer rises from p to 1-(1-p)^N — a meaningful lift even for moderate base probability.

**What this does to comparisons.** When one system uses Best-of-N with N=16 and another uses a single sample, comparing their scores is comparing a committee to an individual. Part of the measured gap is not model quality — it is sampling depth. This is rarely disclosed prominently. The score appears in a table with no footnote about the inference-time committee behind it.

**Where I have noticed this distorting.** Math and code benchmarks are especially vulnerable. These tasks have natural retry logic: generate, evaluate, regenerate. If the evaluation pipeline is what produces the reported improvement rather than the model itself, the benchmark result is an artifact of the evaluation design, not a property of the model being measured. I do not have full data on how widespread this practice is, but I have seen it enough that I now treat high scores from unknown groups as requiring a methodology audit before I can treat them seriously.

**A practical signal.** Check the evaluation section for sampling strategy disclosure. If it says "we generate 16 samples and report the best," the honest comparison baseline is "16-sample model X," not "single-sample model X." Restate the score before it enters any comparison table.

**What I am not claiming.** Best-of-N is not invalid. It should simply be reported as what it is: inference-time diversity combined with a selection step. Calling it "model performance" conflates the model's capability with the evaluation's breadth. Those deserve separate accounts.

**Word count:** ~430