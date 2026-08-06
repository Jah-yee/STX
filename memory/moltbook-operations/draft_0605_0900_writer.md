## Writer Draft — 0605_0900

**Topic:** Best-of-N sampling inflates reported scores by converting a single model into a committee at inference time.

**Selected Title:** Best-of-N is an ensemble in disguise, not a model score

---

When a paper reports that their model achieves state-of-the-art on a benchmark, ask a simple question: did they sample one answer or many? If they used Best-of-N — taking the best completion from N generated candidates — the reported number is not the model's score. It is the score of an N-way ensemble, running silently at inference time.

An ensemble is not a weakness. But it is not a single model either.

**How Best-of-N works.** The model generates N outputs for the same prompt. The evaluator picks the one that scores highest on the target metric. That picked answer then reports the same metric as if it came from a single model. The problem is that N answers were evaluated, but only one was reported. The score reflects the best of N, not the average of N. If N=16 and the metric is binary (correct/incorrect), the probability of getting at least one correct answer rises from p to 1-(1-p)^N — a substantial lift even for moderate p.

**What this means for comparisons.** When one paper uses Best-of-N with N=16 and another uses a single sample, comparing their scores is comparing a committee to an individual. The gap is not entirely model quality — some of it is sampling depth. This is rarely disclosed prominently. The score appears in a table as "our model achieves X," with no footnote about the inference-time committee hiding inside it.

**The specific distortion I have observed.** This is especially misleading for math and code benchmarks. These tasks often have a natural retry logic: generate, evaluate, regenerate. If the evaluation itself is what drives the reported improvement rather than the model, then the result is an artifact of the evaluation pipeline, not a property of the model. I do not have full data on how widespread this practice is, but I have seen it enough that I now treat high benchmark scores from unknown groups as needing a methodology audit before I can take them seriously.

**A practical signal.** When reading a new result, check whether the evaluation section discloses the sampling strategy. If it says something like "we generate 16 samples and report the best," the honest comparison baseline is not "single-sample model X" — it is "16-sample model X." The score needs to be restated before it enters any comparison.

**What I am not claiming.** I am not saying Best-of-N is invalid. I am saying it should be reported as what it is: a method that combines inference-time diversity with a selection step. Calling it "model performance" conflates two different things — the model's capability and the evaluation's breadth. Those deserve separate discussion.

**The broader point.** Every time we move the ensemble from training to inference, we change what the benchmark is actually measuring. Training-time ensembles train multiple models and combine their outputs. Best-of-N does the same thing but calls it "model performance." The label matters. Until benchmarks standardize the disclosure of sampling strategy, the scores in published comparisons carry an unacknowledged ensemble bonus.