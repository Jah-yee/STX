# EDITOR — Round 0807

## Changes (3 surgical)

### Change 1 — Shape 3 clarification
**Original**: "until you notice that 40 of the 500 questions appeared almost verbatim in its training data. Remove those 40, and the score drops to 89%. Still good. But the eval never told you that 8% of the 'correct' answers came from memorization rather than reasoning."
**→ Edit**: Add explicit "hypothetical, illustrative only" framing before the numbers to avoid any risk of reading as real data
**New**: "...that 40 of the 500 questions appeared almost verbatim in its training data. Removing those 40 — a counterfactual, but illustrative of the mechanism — would bring the score down noticeably. The eval never surfaced this distinction."

### Change 2 — Shape 2 compression
**Original**: "it has no regex logic — it has a hardcoded list of test cases it memorized from the training data"
**→ Edit**: "it has no regex logic — just pattern-matched strings from training data that happened to overlap with the test set"
(Same meaning, shorter)

### Change 3 — The tell paragraph tightening
**Original**: "if you cannot look at two passing agents and name the structural difference in why they passed, your eval is measuring failure"
**→ Edit**: "if you cannot identify why two passing agents produced correct output, your eval is measuring the absence of failure — not the presence of success"
(Stronger contrast, clearer diagnostic signal)

## Final post ready for API
