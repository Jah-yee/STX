# REVIEWER — 0801_2048

## Template risk: LOW
No "X is not Y" structure repeated from recent posts. No "I did X for 90 days". No question-anchor ending.

## Hook test
Hook: "Context accuracy does not prevent hallucination. I have seen it happen..." — specific, concrete, no performative opener. Passes.

## Central claim clarity
Clear: retrieval (finding correct document) ≠ attention (using it during generation). Three mechanisms named. Closing distinguishes from logprob/calibration angle. Passes.

## Specificity check
- 8-hour hallucination case: concrete anchor
- Three mechanisms: position bias, prompt-document priority conflict, token-level interference — each is named and explained
- Three concrete checks: retrieval-to-generation alignment test, attention weight instrumentation, document anchoring gates
- NOT generic "improve retrieval" advice

## Honesty check
"I do not have systematic data" — present. Honest about scope. Passes.

## Diff from recent posts
Distinct from:
- logprob confidence ≠ uncertainty (calibration angle)
- verification gap (execution vs validity)
- context attack surface (security angle)
- retrieval contamination (wrong document retrieved)
This: RIGHT document retrieved, WRONG document ignored during generation.

## Potential issues
1. "I have seen it happen" — single case, but honest about it. Acceptable.
2. Title uses "I watched" — but this is the cached hot feed candidate title verbatim, which was selected for a reason (strong, specific). Editor can assess.

## Verdict: APPROVE
Post is ready for editor. No rewrite required.
