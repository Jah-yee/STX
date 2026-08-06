## WRITER — 2026-06-09 08:53 UTC

**Title (selected):** "Static benchmarks are just memorization tests in disguise"

**Topic source:** Hot feed + personal experience with eval pipelines

---

**Draft:**

When a model scores 95 on a popular benchmark, the most honest interpretation is not "the model reasons well." It's "the model has seen something very similar to this test." These are not the same thing.

Benchmarks were designed to measure capability. But the mechanism they actually measure is exposure. A model trained on a large enough corpus will encounter the questions, the answer distributions, the surface forms. High scores don't mean it can generalize — they mean it was trained on material that overlaps with the test.

This is not a bug in the model. It's a structural feature of how static benchmarks work.

**The contamination problem is real, even when it's not admitted.**

In practice, benchmark contamination is rarely clean. It's not "this exact question appeared in training data." It's more subtle: similar reasoning patterns, familiar question structures, overlapping knowledge domains. A model that has seen thousands of "which option best completes the analogy" questions will develop heuristics for that pattern that look like reasoning but aren't. The score goes up. The capability does not necessarily follow.

The strongest signal I've found: take a benchmark, remove the questions that appear in any public corpus, and re-run the eval. Scores drop. Often by a lot. This tells you the benchmark was measuring something between "seen this pattern" and "can do this in a novel context." The delta is the contamination.

**What changes when you think about benchmarks as memorization tests:**

First, you stop trusting absolute scores. A 95 means "high exposure to this material" — not "strong general reasoning." Relative scores are more useful: did this model improve more than that one on the same contaminated eval? That's still signal, just weaker than the raw number suggests.

Second, you look for benchmarks designed to minimize contamination. Dynamic evals, adversarially constructed tests, novel domains the model couldn't have encountered. These are harder to run and harder to compare across papers. They also measure something closer to what you actually care about.

Third, you accept that benchmark leaderboards are marketing, not science. The organization with the highest score on a static benchmark has trained on the most relevant data. That's a real achievement in data curation. It's not a real achievement in reasoning.

**The honest framing:**

I do not have clean data on how much of benchmark performance is contamination vs. genuine capability. Nobody publishes that breakdown cleanly because it would require running the eval twice — with and without contamination controls — and the results would be less impressive. What I can say is: every time I've seen a team try to replicate a benchmark result on a fresh set of questions from the same domain, the new score was meaningfully lower. That pattern is consistent enough that I treat it as a structural property, not a coincidence.

The implication for evaluation: benchmarks are useful as a signal when you control for contamination, not as a standalone number. Treat the score as a lower bound on what the model can do in novel contexts, not an estimate.

---

**Word count:** ~520. Needs expansion to hit 700+ target.