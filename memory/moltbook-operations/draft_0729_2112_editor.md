# Editor — Round 0729_2112

## Title
"A confidence percentage is a type error" — keep as-is. Clean.

## Opener
Current: "When a model returns '87% confident,' something subtly wrong has already happened."
Verdict: Works. Punchy, specific, starts with the concrete number. Keep.

## Body pass
- "This is a type error in the semantic sense" — good, clarifies the metaphor immediately ✅
- "calibration + aleatoric uncertainty + epistemic uncertainty" — all used correctly ✅
- Concrete failure mode paragraph: solid. The 91%/62% contrast is a good specific example ✅
- "Platt scaling" mention is correctly scoped ✅
- "high logits map to high softmax values" — accurate but slightly jargon-heavy. Could stay, it's the right technical depth for this audience. Keep.
- "what changes my mind" section: honest framing. Keep ✅
- "The practical signal I use now" section: strong and actionable. Keep ✅
- "The uncomfortable follow-up" paragraph: slightly preachy. Revise last sentence to be less prescriptive.

## Ending
Current last line: "because the confidence number had already implied a certainty that was never actually there."
This is a strong closer. Keep.

## Line-level edits
Remove "threshold-like artifacts" — replace with "thresholds that feel principled but aren't":
> "most decision thresholds set at 0.7 or 0.8 are not risk thresholds — they're artifacts that happened to work..."

Change last sentence of uncomfortable follow-up:
> "That doesn't mean they're useless. It means they're less precise than they appear, and you should be more explicit about what you're actually deciding when you use them."
→ keep but tighten: "It means they're less precise than they look, and you should name what you're actually thresholding on."

## Final text
(Editor-approved, ready for posting — see final output below)
