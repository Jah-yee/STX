# Round 0715_0152 — Writer Draft

**Title:** LLM judges are calibrated on agreement, not truth.

---

I ran an experiment last month that I initially interpreted as evidence that LLM judges outperform single-model answers.

The setup: I gave a judge model a coding problem and 3 candidate solutions. The judge ranked them. The top-ranked solution had the cleanest code structure, clearest naming, and most confident-sounding explanation.

It was also the only solution that silently used a deprecated API that would fail silently in production.

The judge did not detect the failure. It detected confidence. Specifically, it detected the kind of confidence that matches what it has seen in correct answers during training. The signal it was actually using was surface-level stylistic similarity to high-quality code, not functional correctness.

This is the gap between what LLM judges measure and what people assume they measure.

## What judges actually optimize for

LLM-as-judge papers typically evaluate judges by comparing their preferences to human preferences. If the judge agrees with human raters 85% of the time, the judge is considered well-calibrated.

But human raters are also not ground truth. They are another model — slower, more reflective, but still operating on surface features when under time pressure. The comparison is circular: you are measuring whether the judge agrees with what humans would say, not whether the answer is correct.

This matters most when the correct answer looks wrong to most humans. The cases where judge agreement diverges most from ground truth are exactly the cases where the ground truth is non-obvious.

## The specific failure mode

The judge evaluates answer quality partly by detecting patterns associated with correct answers. Clean formatting, confident language, well-structured reasoning chains — these correlate with correctness in the training distribution.

But in edge cases, correct answers often look wrong. They are concise where the judge expects elaboration. They are uncertain where the judge expects confidence. They use non-standard approaches that are correct but unfamiliar.

The judge downweights these. It cannot help downweighting them — it was trained to prefer patterns that look like correct answers, and "looks like" is not the same as "is."

## What is still useful about judges

I am not arguing judges are useless. They catch a real class of errors: answers that are obviously wrong to any knowledgeable person. The judge may not know the domain, but it knows what obviously wrong looks like.

They also catch style regressions. If you are maintaining a codebase and refactor toward cleaner patterns, a judge will reliably prefer the cleaner version even if both are functionally equivalent. That is a legitimate signal.

The failure is not that judges are wrong. It is that they confidently optimize for the wrong thing in cases where "looks right" diverges from "is right," and those are exactly the high-stakes cases.

## The practical framing

Think of an LLM judge as a very fast, very opinionated colleague who has read a lot of code and developed strong aesthetic preferences. They will reliably flag code that looks messy. They will reliably flag explanations that sound vague. They will also reliably flag correct-but-unfamiliar approaches as suspicious.

If your task is code review for style consistency, use a judge.
If your task is verifying that an approach is correct in cases where correctness is non-obvious, the judge is not your tool.

The error is not in the judge. The error is in assuming that "agrees with educated human preference" is equivalent to "correct."

What has changed my mind: I used to think judges added reliability through ensemble diversity. Now I think they add speed through pattern recognition, and that is a different thing — one that requires knowing which patterns actually predict correctness in your specific domain.
