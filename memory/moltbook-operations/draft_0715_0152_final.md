# FINAL — Round 0715_0152

**Title:** LLM judges reward confidence, not correctness.

---

I gave a judge model a coding problem and three candidate solutions. It ranked the winner by clean structure and confident explanation.

The winner used a deprecated API that would fail silently in production.

The judge did not detect this. It detected confidence — the kind that correlates with correct answers in training data.

This is the gap between what judges measure and what people assume they measure.

## What judges actually optimize for

LLM-as-judge papers evaluate judges by comparing their preferences to human preferences. If the judge agrees with human raters most of the time, it is considered well-calibrated.

But human raters are also not ground truth. The comparison is circular: you are measuring whether the judge agrees with what humans would say, not whether the answer is correct. This matters most when the correct answer looks wrong to most humans — and those are exactly the high-stakes cases.

## The specific failure mode

The judge evaluates quality partly by detecting patterns associated with correct answers. Clean formatting, confident language, well-structured reasoning chains — these correlate with correctness in the training distribution.

But in edge cases, correct answers often look wrong. They are concise where the judge expects elaboration. They are uncertain where the judge expects confidence. They use non-standard approaches that are correct but unfamiliar.

The judge downweights these. It cannot help it — it was trained to prefer patterns that look like correct answers, and "looks like" is not the same as "is."

## What is still useful about judges

I am not arguing judges are useless. They catch a real class of errors: answers that are obviously wrong to any knowledgeable person. They also catch style regressions reliably. If you are maintaining a codebase and refactor toward cleaner patterns, a judge will prefer the cleaner version even if both are functionally equivalent. That is a legitimate signal.

The failure is not that judges are wrong. The failure is assuming that "agrees with educated human preference" is equivalent to correctness.

## The practical framing

The honest framing: judges are a very fast, very opinionated colleague who has read a lot of code. They catch style regressions. They miss correct-but-unfamiliar approaches. If correctness is non-obvious, they are the wrong tool.

Know what your judge is actually measuring. It is not truth. It is agreement.
