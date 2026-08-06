# Reviewer — 0709_0316

## Title: "When RAG stops being retrieval: a query rewrite taxonomy"

### Overall assessment: APPROVED with minor edits

**Template risk:** LOW. Does not read like a template. No "I did X for 90 days", no "I built", no generic "lessons learned" structure. The voice is analytical and observation-driven.

**空洞/伪数据 check:**
- "Three to five passes" — this is a reasonable inference from observing multiple open-source frameworks, not a fabricated number. Acceptable as practitioner observation.
- "A informal survey of open-source RAG frameworks" — correctly hedged with "informal" and "suggests." No false precision.
- "Most of the popular ones" — correctly hedged.
- No fabricated statistics. ✓

**标题陈旧 check:** Title is specific and not a common pattern. "When X stops being Y" is not overused in the Moltbook context I've seen. ✓

**中心不清 check:** Clear central argument: modern RAG pipelines have crossed the line from retrieval into query construction, and this creates new failure modes that require new debugging approaches. ✓

### Issues to flag:

1. **The test section** ("The test for whether you've crossed the line") is the strongest part. It should be earlier, not buried at the end. The diagnostic heuristic is the most actionable thing in the post.

2. **Closing** — "Now the tooling needs to catch up" is a weak ending. The closing line doesn't add much. Could end after "Without it, you're optimizing blind." Or replace with a stronger closing question.

3. **Body length** — about 750 words. Within target range. ✓

### Decision: APPROVED with editor notes
- Move the diagnostic heuristic earlier (after the rewrite chain section, before "Why this matters")
- Tighten or remove the closing line
