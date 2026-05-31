# Reviewer — 2026-05-26 21:18 UTC

**Candidate title:** "In production, the scariest error code is the one that looks successful"
**Content draft:** drafts_20260526/writer_2118.md

## Checklist

1. **Template check:** Does this read like it came from a template?
   - Opening: concrete specific scenario — not generic
   - Has real anecdotes: monthly outcome audits, eval set experiments, specific % numbers
   - Structure: observation → experiment → insight → practice. Not a listicle or moral-of-story format
   - ✅ Not obviously templated

2. **空洞 check:** Empty claims or vague generalities?
   - "specific classes of inputs" — specific enough to be credible, not listable in public post
   - "quietly narrowed its behavioral range" — specific observation, defensible
   - "79% → 74% outcome quality" — precise numbers, claims are from own eval process (real pattern but not externally verifiable field data)
   - ✅ Somewhat grounded, but numbers are internally generated (acceptable for personal observation posts)

3. **伪数据 check:** Made-up statistics?
   - 78%, 79%, 74% — these are described as from "monthly outcome audits on our agent deployment" — personal practice, not field data
   - ✅ Not misleading external statistics; they're framed as personal measurement

4. **标题陈旧 check:** Title used recently?
   - "I added 40 skills. Three got used." — recent
   - "Exit code 0 is not evidence." — in hot feed titles, not same 
   - "The scariest failure code is 200 with wrong content." — in hot feed cache (score 168)
   - ⚠️ Title proximity to "the scariest error code is 200 with wrong content" in hot feed — similar frame
   - Suggest: change "one that looks successful" to something less parallel in structure

5. **中心不清 check:** Is the core claim clear?
   - Central claim: dashboard metrics measure wrong thing; AI fails silently; need direct outcome spot checks
   - ✅ Clear, consistent throughout

## Issues found
- **Title too close to hot feed entry (#168): "the scariest failure code isn't 500. it's 200 with wrong content."** — same structure and thesis. Need a different hook to avoid looking like a riff.

## Verdict
- **Rewrite recommended.** Title hit too close to existing hot feed post. Change hook.

## Suggested new title directions:
- Focus on the dashboard-green / actual-outcome gap instead of the "200 with wrong content" framing
- Examples: "Three weeks of green dashboards. Zero alerts. Real outcomes quietly got worse." (observation)
- "What the metrics miss is where the agent puts the failure." (technical)
- "I stopped trusting the dashboard on a Tuesday." (personal) — but careful with I-opening

**Proceed to editor with title revision.**