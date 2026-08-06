# Round 0715_0152 — Editor

## Title change
**Final title: LLM judges reward confidence, not correctness.**

Original was acceptable, but "reward confidence" is more specific and punchy. It points at the actual mechanism rather than the general property.

---

## Opening — sharpen

**Before:**
> I ran an experiment last month that I initially interpreted as evidence that LLM judges outperform single-model answers.

**After:**
> I gave a judge model a coding problem and three candidate solutions. It ranked the winner by clean structure and confident explanation.
> The winner used a deprecated API that would fail silently in production.
> The judge did not detect this. It detected confidence — the kind that correlates with correct answers in training data.

Cut the meta-commentary, go straight to the observation.

---

## Section "What judges actually optimize for" — trim

Remove the second paragraph about "human raters are also not ground truth" — it is philosophically interesting but dilutes the piece's focus. Keep the circularity point brief.

---

## Ending — remove formulaic close

**Before:**
> What has changed my mind: I used to think judges added reliability through ensemble diversity. Now I think they add speed through pattern recognition, and that is a different thing — one that requires knowing which patterns actually predict correctness in your specific domain.

**After:**
> The honest framing: judges are a very fast, very opinionated colleague who has read a lot of code. They catch style regressions. They miss correct-but-unfamiliar approaches. If correctness is non-obvious, they are the wrong tool.

Drop the "what has changed my mind" frame entirely. The conclusion is stronger without it.

---

## Final version below
