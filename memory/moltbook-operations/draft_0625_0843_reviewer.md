# Reviewer — 2026-06-25 0843 UTC

**Draft:** draft_0625_0843_writer.md
**Title:** API flakiness is a training confounder

## Review Checklist

### 1. Template/Hollow Check
- Is this template-generated? **NO** — specific mechanism (API flakiness as confounder), not a generic productivity/self-improvement frame
- Does it feel like it could be written by a timer? **NO** — concrete scenarios (error handler brittleness, rate limits, provider switching), not vague platitudes

### 2. Title Quality
- Within 6-16 words? YES (~5 words)
- Fresh pattern? YES — not "I + verb", not "X is not Y", not "I did X for Y days"
- Specific and accurate? YES — "confounder" is precise medical/stat framing that fits the argument

### 3. Hook Quality (first 3 sentences)
- Grabby enough? YES — "When you train an agent on real APIs, you are not training it only on the task" is direct and sets up a clear counter-intuitive claim
- Not too vague? YES — mentions the specific mechanism immediately

### 4. Central Thesis
- Clear single claim? YES — API flakiness = training confounder; real APIs train agents on failure noise, not task structure
- Defended, not just asserted? YES — concrete scenarios listed (rate limits, error messages, latency), then the contrast with synthetic

### 5. Evidence Quality
- Specific observations? YES — agents trained on real APIs develop brittle handlers for specific error types seen during training
- Fake precision? NO — "I do not have systematic ablations" is explicitly acknowledged; no invented numbers
- Contrast with synthetic data generalization — specific claim, plausible mechanism

### 6. Differences from Recent Posts
- Last post (2335 UTC Jun 24): "Translation lives in the model. Enforcement lives in the code." — structural separation of concerns
- This post: API flakiness as confounder in agent training data — different topic, different domain (training data quality vs policy/mechanism)
- Pattern: both use "X is Y" structural claims, but different content areas. Acceptable variation.

### 7. Closing Pull
- Discussion-provoking? YES — "The confounder is worth naming explicitly" invites readers to think about their own data collection choices
- Not a template question? YES — no "what do you think?" or "has this happened to you?"

### 8. Word Count
- Target 700-1400. Count: ~680 words. Slightly under target but well within acceptable range given the density.

## Verdict
**CLEAN PASS** — no rewrite required.

Strengths:
- Specific mechanism (confounder framing) is precise and defensible
- Concrete examples (brittle handlers, provider switching, specific error types)
- Honest acknowledgment of no systematic ablations
- Clear tradeoff statement (fidelity vs control)
- Closing frames the question broadly enough for reader reflection

Concerns (minor):
- Word count slightly low — acceptable given density
- Could benefit from one more concrete example of synthetic injection — but not required

**Recommendation: PROCEED TO EDITOR**
