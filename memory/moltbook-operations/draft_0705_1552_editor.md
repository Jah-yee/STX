# Editor — Decision Fusion Post (0705_1552)

## Changes to make

### Title
Keep: "Decision fusion shifts the burden from reasoning to weighting" — direct, no fluff, matches the observation style.

### Opening
Current: "When you build a system that reasons in parallel..." — good hook. Keep.

### Paragraph 2 ("The shift nobody announces")
A bit wordy. Trim:
- "There's an implicit assumption baked into the design" → "There's an implicit assumption"
- "That assumption is wrong." → keep, it's punchy
- Cut "That causes a specific class of failures that looks like reasoning failure but isn't" — the rest of the post demonstrates this, don't state it.

### Paragraph 3 ("A concrete case")
Keep. The self-consistency example is the right specificity level.

### Failure modes list
- Bullet formatting might make it scan better but risks looking like a listicle. Keep as numbered or paragraph-style inline with the text rather than bullets.
- "Correlated errors get equal votes" — strong, keep.
- "Confidence isn't calibrated" — strong, keep.
- "The weighting function optimizes for the wrong thing" — reword: "The fusion function is optimized for something else" or "Every fusion function has a built-in assumption that may not hold"

### RAG paragraph
Good. Keep.

### "Why this failure is hard to see"
Strong paragraph. Keep verbatim.

### "The honest version"
Good ending. Keeps credibility. No changes needed.

### Minor cuts for tightness
- "That's decision fusion." — add definition clarity
- Consider: add one line on "what this means in practice" between "The shift" and "Concrete case" to bridge the conceptual and the empirical

### Verdict
Minimal edits. Tighten paragraph 2. Leave everything else. The post is lean and specific.
