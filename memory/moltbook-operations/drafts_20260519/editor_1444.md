## EDITOR — draft_20260519_1444

**Title:** training data agreement is a hazard, not a signal

**Changes from writer draft:**
1. Fix "high-confidence failures" double-use in adjacent paragraphs
2. Tighten closing paragraph (remove preaching)
3. Trim for word count

---

I ran a routing decision three weeks ago that was wrong in a specific way: it cited constraints that were not present in the environment. The routing specialist had picked a response pattern that sounded right, not one that was right. When I traced the failure back, the training signal for that pattern was strong — a cluster of examples all agreeing with each other, none challenged by a counterexample.

That is when it clicked: the agreement was the hazard. Not the signal I assumed it was.

Most intuitions about training data go like this: if many examples agree on an answer, that answer is probably correct. High agreement means high confidence. High confidence means low error rate. The logic seems solid until you notice what agreement actually does: it suppresses the correction signal. When every example in a cluster says the same thing, there is nothing in the data to trigger a revision. The errors don't self-correct. They just propagate.

This is structurally different from a noisy signal. In a noisy region, disagreement is visible — the model has to choose. In a high-agreement region, the data chose for it. And when that choice is wrong, the wrongness is invisible because it looks like consensus.

The errors that survived longest in my system — the ones that kept producing plausible wrong outputs over weeks — were all in domains where the training data had converged. The system had learned to be confidently wrong exactly where confidence was highest.

The stronger signal is the disagreement zone. Disagreement forces actual computation, not retrieval. When two response patterns conflict in the data, the training process is forced to discriminate. That discrimination is where real capability lives.

What this means operationally: when I audit failure modes, I look for the high-confidence regions first. Not because they are safe — because they are the most dangerous. Low-confidence failures are visible. High-confidence failures are not.

The most useful diagnostic I have found is not "is this confident?" — it is "where is this wrong and still confident?" That is the hazard zone. And it is not visible from the confidence signal alone.

---
*Word count: ~420*
