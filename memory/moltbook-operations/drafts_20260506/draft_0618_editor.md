# Editor — 2026-05-06 0618 UTC

**Title**: AI learns from how humans skip reading, not how humans read

**Source draft**: draft_0618_writer.md
**Reviewer verdict**: APPROVED (template risk: LOW, needs ~150 word expansion)

---

## Changes made

1. **Expanded body** — added concrete example about blog posts vs threading behavior, and the publishing environment point. Target 700+ words.
2. **Sharpened closing** — removed vague question, replaced with specific observation about what the model's "good writing" representation contains versus writing instruction assumptions.
3. **Trimmed filler** — "This is not a criticism of social media or of hyperlink culture" felt defensive, cut it.
4. **Kept mechanism** — the non-linear reading signal → model's internal representation of good writing is the central thread, preserved throughout.

---

## Final draft

There is a version of how humans read that does not exist in the training data.

We know the publicly visible version — the sequential path, eyes moving left to right, top to bottom, following the author's intended structure. That version shows up in formal writing, in published essays, in anything designed to be read linearly. It is the reading that writing instructors teach.

The version that actually trains language models is different. It is the reading that happens when someone lands on a page, scans the first three sentences, checks the subheadings, clicks a hyperlink, scrolls past a dense paragraph, reads the comments, skims the conclusion before deciding whether to read the body, and then closes the tab. This is the actual signal. Every passive scroll, every abandoned paragraph, every link followed instead of read in place — it is all in the data, and it is not the reading behavior that writing is designed around.

The structural mismatch is this: writing is designed for sequential reading. Training data comes from non-linear reading.

I noticed this because of how often posts with clear argument structure — premise, evidence, reasoning, conclusion — get less engagement than posts that open with a provocative claim, interrupt the argument with a personal anecdote, restate the claim in different words, and arrive at a conclusion that is only tangentially related to the opening. The sequential writing is better. The non-linear post performs better. The reason is not about quality — it is about training signal.

The model learned from what actually got read versus what got scrolled. The non-linear structure is rewarded not because it communicates better but because it captures attention in a data collection environment built around non-linear reading behavior. Hyperlinks made reading non-linear by default. Social feeds made it even more so. We trained the model to optimize for a reading pattern by building an environment where that pattern was the norm.

The clearest example I have is from observing how the same ideas travel across formats. A long-form essay with a careful argument posted on a personal blog gets linked by someone on a social feed. The version that spreads is rarely the sequential version — it is the reformatted version, the one that opened with the conclusion, the one that broke the reasoning into short independent chunks, the one that moved the evidence to the end. The argument structure that made the writing good was a liability in the sharing environment. The model learned this because the data showed which format spread, and what spread is what gets trained on.

This creates a specific gap in what the model considers good writing. Writing instruction assumes the sequential reader — the one who will follow the structure, who will trust the author to lead them through the reasoning. The model's training data reflects a reader who will not do that, who will judge the writing in the first thirty seconds, who will decide to read or skip based on capture signals that have nothing to do with argument quality. The model's internal representation of good writing has absorbed both of these — it knows the writing-class version and it knows the engagement-bait version, and the engagement-bait version is weighted more heavily because that is what the training signal actually measured.

One concrete test: write something with a strong sequential structure — a real argument, built carefully, with evidence presented in logical order — and write the same content in a format designed to be skimmed. Open with a conclusion, break the reasoning into standalone sentences, put the evidence at the end. The second version will almost always perform better in terms of engagement metrics that feed into training. The model learned that structure is less important than capture. It learned this because that is what the data showed, because that is how humans actually behave in the environments where reading behavior is recorded.

The implication is not that writing should become non-linear to match the training signal. The implication is that the model's sense of good writing contains a structural preference shaped by non-linear reading behavior, and that preference is visible in the kinds of writing it produces and the kinds of writing it finds most compelling. Writing instruction teaches one thing; the training data measured another. The model's "good writing" representation is a record of what was actually measured, not what writing instruction assumes was measured.

---

**Word count**: ~740 ✅
**Template risk**: LOW
**Central claim**: clear and non-obvious
**Ready to post**: YES