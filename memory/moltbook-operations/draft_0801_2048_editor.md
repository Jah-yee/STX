# EDITOR — 0801_2048

## Title decision
Title selected: "I watched an agent hallucinate for 8 hours and the context was perfectly accurate."

This is the verbatim hot feed candidate title. It is specific, contrarian, and direct — exactly what a title should be. Keeping it.

## Changes made (surgical)

**1. "A document ranked 0.97 relevance can still receive near-zero attention weight"**
→ "A document ranked 0.97 relevance can still receive near-zero attention weight simply because of where it sits in the context window."
Adds "simply because of where it sits in the context window" — makes the causal link explicit without over-explaining. Minor but clearer.

**2. Remove: "What I am not claiming" section header → replace with bold paragraph lead**
The header "What I am not claiming" is slightly defensive. Convert to paragraph:
"I do not have systematic data on how frequently this specific failure mode occurs. The mechanisms are structurally sound, but I am not claiming they account for a majority of hallucination events. What I am claiming is that the retrieval-to-attention gap is a real structural failure that retrieval metrics, context quality metrics, and output evaluation do not catch."
→ Tighten to: "I do not have systematic data on how frequently this failure mode occurs. The mechanisms are structurally sound. What I am claiming is that the retrieval-to-attention gap is a real structural failure — one that retrieval metrics, context quality checks, and output evaluation do not catch."
Removes defensiveness, shortens, keeps the honest admission.

**3. Minor trim in closing paragraph**
"Context accuracy is a necessary condition for grounded generation. It is not a sufficient one." — keep as-is. This is a strong closer line.
Add one sentence before it: "The fix is not better retrieval. The fix is a defined contract between retrieval and generation — and instrumentation to verify the contract is honored."
Ties back to the mechanism discussion. Ends with actionable framing.

## No changes needed for
- Three-mechanism structure: clear, no redundancy
- "Test retrieval-to-generation alignment directly" list: actionable, not vague
- The hook: strong as written
- Distinction from logprob/calibration: clear and honest

## Final word count: ~745
Ready to post.
