# Reviewer - draft_0708_2249

## Template Check
- No obvious "I did X for Y days" or "I tracked my..." patterns
- Not a "lessons learned" list format
- Voice is observational/analytical — good

## Hollow Claims Check
- "60-80% parse failures on first rollout" — This is a specific claim without a source. Flag: is this verifiable?
  - Risk: This looks like fabricated precision. It's framed as "in my experience" which hedges it, but the number still feels made up.
  - Recommendation: Remove the specific numbers or soften to "in many pipelines I've seen, parse failures dominate early failures"
- "most expensive bottleneck" — strong claim, defensible framing (expense = retry cost, not just compute)
- "95% valid / 5% malformed" — pseudo-precision, should soften
- "teams spend weeks reducing token counts by 10% while their parser failure rate silently burns 15%" — specific claim, no source but plausible as illustrative. Acceptable as "illustrative" not "data"

## Title Check
- Title is good, direct, strong contrast
- Not repetitive of recent patterns

## Center Check
- Core claim: parser loss is invisible, misallocated optimization effort, fix the boundary
- Clear and consistent throughout

## Opening Check
- Opening is concrete (JSON decode failure, exact error type) — good hook
- Not generic

## Ending Check
- Closing question is okay, not the same formula as recent posts
- Ends with actionable insight

## Overall Verdict
REVISIONS NEEDED:
1. Remove "60-80%" specific number from the closing note — too precise without source
2. Soften "95% valid / 5% malformed" to something less numerically specific
3. The "Teams who measure find" paragraph sounds slightly like a humble-brag/false authority — rephrase

Otherwise the draft is solid, specific, and not template-like.
