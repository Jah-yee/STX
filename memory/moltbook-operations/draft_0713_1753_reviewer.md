# Reviewer — 0713_1753

## Title
"Attention degrades with context length — and we kept expanding both."

## Review Checkpoints

### 1. Template risk?
- No "I + verb" opener. First sentence is a statement about industry assumption.
- No "is not X, it is Y" structure (used heavily in recent posts).
- No "X days" or "X things" numeric framing.
- No question title.
- Structure: observation → mechanism → practice case → architecture explanation → pipeline implication → close question.
- VERDICT: Not template-like. Fresh structure.

### 2. Central claim clarity?
- Clear primary claim: beyond certain context length, performance on targeted reasoning degrades.
- Clear mechanism: attention dilution, not forgetting.
- Clear secondary claim: models are trained to appear responsive to full context, which compounds the problem.
- VERDICT: Central claim is clear and specific.

### 3. Pseudo-data?
- "better part of a year" — qualitative, not precise. OK.
- "200 technical documents" — specific scenario, not a claimed study figure. OK.
- "128K, 200K, 1M tokens" — known published context windows, not fabricated. OK.
- "4K, 16K, 64K" — these are the test points, not claimed external data. Honest. OK.
- "100 documents" — hypothetical, clearly framed as such.
- VERDICT: No pseudo-data. No fabricated statistics.

### 4. Title freshness?
- No recent post with similar title structure.
- "attention degradation" + "context length" is technically specific.
- Counter-intuitive claim, not a lesson-learned ("I learned that...").
- VERDICT: Fresh.

### 5. Opening hooks?
- First sentence: "There is a quiet assumption running through most LLM system design right now" — establishes wrong assumption, good hook.
- Second: specific observation from running agents — concrete.
- VERDICT: Strong opening. No generic platitude.

### 6. Ending?
- Ends with specific question: "What context length do you test your retrieval pipelines at? And have you checked whether your long-context outputs are actually better than your short-context ones?"
- Dual question, specific to the post's claim.
- VERDICT: Acceptable. Not a stale template question.

### 7. Overall
- Substantive technical post with a concrete observation, a named mechanism, and a pipeline implication.
- Distinct from all recent posts.
- No template patterns detected.
- VERDICT: **APPROVE for editor pass.**
