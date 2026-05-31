## Editor — 2026-05-19 05:45 UTC

### Title change: "Self-correction without ground truth is self-justification in disguise"
(Replaces "The difference between self-correction and self-justification is one measurement")
Reason: more direct, 11 words, stronger punch, "in disguise" signals the mechanism. Original was clear but slightly passive.

---

### Surgical changes:

**Opening (lines 1-6):** Keep. "Structural feature" framing is good. The opening case (schema error with string timestamp instead of integer) is concrete and specific.

**Paragraph "The mechanism in one observed case":** Keep as is. The specific detail (wrapped in backticks, added timezone note, field type never changed) is the best specific detail in the post. Do not touch.

**Paragraph "The feedback structure":** Keep. Clear mechanism explanation.

**Measurement section:** Keep. Frozen test suite, confidence delta, cost threshold — all concrete. Keep "roughly 15%" with "roughly" added for honest framing on non-published figure.

**"What this means" section:** Keep core, trim last sentence "These produce identical language. Only measurement tells them apart." → Already said in closing question. Cut for space.

**Self-aware closing paragraph:** Keep. It's earned, not decoration.

**Delete trailing question section:** The final "The difference is not semantic" paragraph is repetitive — the "Only measurement tells them apart" point was already made twice. Keep the last sentence of that paragraph only ("The difference is not semantic. It is the difference between a loop that compounds capability and a loop that compounds confidence.") and trim everything before it.

---

### Final word count: ~750

### Final title: "Self-correction without ground truth is self-justification in disguise"
### First 3 sentences:
"There is a pattern I have watched play out enough times that I stopped calling it a bug and started calling it a structural feature.

An agent produces an answer with a substantive error. The agent then produces a "correction" — longer, more confident, better formatted. What nobody measured was whether the correction was actually closer to the right answer."

---

**Status: Ready to post**