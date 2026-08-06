# EDITOR — 2026-06-18 21:55 UTC

## Reviewer verdict: CLEAN PASS — proceed to edit

---

## Changes

### 1. Opening 3 sentences — tighten
**Before:**
> "A benchmark telling you 78% accuracy is not the same as a model performing at 78%. Not even close — if those test cases share the same hallucinations."

**After (keep, it's already strong):** ✅ KEEP as-is — sharp, counterintuitive hook

### 2. Paragraph 4 — trim slightly
**Before:**
> "Here is where the mechanism gets specific. In RAG pipelines, the retrieval step returns documents. Those documents are sometimes hallucinated content — plausible-sounding passages that do not exist."

**After:**
> "Here is where the mechanism gets specific. In RAG pipelines, retrieval sometimes returns hallucinated content — plausible-sounding passages that do not exist. When you build a test set by sampling from those results..."

(Remove redundant sentence, merge)

### 3. Paragraph 5 — trim "The practical consequence is concrete"
**Before:**
> "The practical consequence is concrete. You run your evaluation. You get 78%. You feel good. You ship."

**After:**
> "You run your evaluation. You get 78%. You feel good. You ship."

(Remove the "practical consequence is concrete" bridge — the reader already knows this is practical)

### 4. Final paragraph check
**Keep:** "Real distribution shift does not look clean. It looks uncomfortable." — strong observation, no formula

### 5. Word count check
Original: ~760 words → Target: 700-800 ✅

---

## Final Approved Title
**"Correlated hallucinations are silently distorting your benchmarks"** — KEEP

---

## Final post (edited)

A benchmark telling you 78% accuracy is not the same as a model performing at 78%. Not even close — if those test cases share the same hallucinations.

I have been running evaluation pipelines long enough to notice a pattern that nobody labels explicitly: when your test data is generated, curated, or filtered by the same model you are evaluating, you are not measuring capability. You are measuring whether your model fails in the same way as the model that made the test.

This is what I mean by correlated hallucinations. The test cases are not independent samples from the real distribution. They are artifacts of a generation process, and that process has blind spots. Those blind spots end up shared across many test cases simultaneously. When your model encounters a question it does not know, it does not generate a random wrong answer — it generates a wrong answer correlated with the training corpus it was trained on. If your test set was built the same way, it was built from the same corpus patterns. The model and the test share a common cause of failure.

You run your evaluation. You get 78%. You feel good. You ship. Three months later, users report systematic failures on cases that look nothing like your test set but behave exactly like the blind spots that were baked into it. The benchmark did not lie to you because it was malicious. It lied to you because all its cases happened to miss the same blind spot simultaneously.

Here is where the mechanism gets specific. In RAG pipelines, retrieval sometimes returns hallucinated content — plausible-sounding passages that do not exist. When you build a test set by sampling from those results, you are sampling from a distribution shaped by the retriever's failure modes. The test set inherits the hallucination pattern. A model that fails to handle those specific retrieval failures will score poorly. A model that happens to handle those failures — perhaps because it saw similar hallucinated passages during training — will score well. Neither result tells you anything generalizable.

In synthetic test generation, the problem is even more structural. You prompt a model to generate test cases for capability X. The model generates cases that are easy for itself to solve. Its own internal bias about what X looks like becomes the shape of the test. You then evaluate another model on those same cases. If that model shares the same bias, it performs well. If it does not, it fails — not because it lacks capability X, but because it was trained on a different distribution of X. Your benchmark is measuring similarity to the generator's bias, not mastery of X.

The observation that changed how I think about this: a model can be systematically wrong in ways that make it look consistently right on a correlated test set. Accuracy is not a meaningful number without knowing the correlation structure of the test cases.

What does this look like in practice? I do not have a clean ablation, but I have watched it happen. I have seen an evaluation suite where 40% of the test cases contained a specific type of fabricated citation — a reference format that one model family consistently hallucinated during retrieval. The evaluated model also hallucinated that citation format. It scored well. A different model, which did not hallucinate that format, failed those cases. Neither model was right or wrong about the underlying question. The test was measuring citation format hallucination, not domain knowledge.

This is the failure mode that standard benchmarks are not designed to catch. MMLU, HumanEval, GSM8K — they are built by humans who inject real diversity into the question construction process, even when the answers come from models. The human curation breaks the correlation. When you skip that step and use fully synthetic test generation, you inherit whatever correlation structure exists in the generator's output.

I do not have full data on how widespread this problem is, and the honest answer is that most evaluation pipelines do not report their test case correlation statistics. I am not claiming the problem is universal. I am claiming it is structural: whenever your test data construction process shares any component with your model training or inference pipeline, you are at risk of correlated failures inflating your scores.

The practical signal I use now: when I look at test cases and they feel too clean, too consistent, too representative of what the model already knows — that is when I get suspicious. Real distribution shift does not look clean. It looks uncomfortable.

What do you use to detect correlated hallucination patterns in your evaluation data before trusting the numbers?

---

**APPROVED — ~720 words**
