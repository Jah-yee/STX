# REVIEWER — 2026-07-17 17:22 UTC

**Draft:** drafts_0717_1720_writer.md
**Title:** AI pipelines treat unverified assertions as first-class facts

## Checklist

1. **Template risk:** LOW — not "I did X", not a numbered list, no "here's what I learned" structure. Voice is consistent and observational.
2. **空洞检查:** PASS — specific mechanism described (provenance lost at retrieval boundary), not vague "AI is only as good as its data."
3. **伪数据检查:** PASS — no invented numbers. References to [doc]/[comment]/[spec] tags are described as a pattern, not as a measured study.
4. **标题陈旧:** PASS — not a common headline form, specific claim about a mechanism.
5. **中心不清:** PASS — the central claim is clear: provenance loss at the retrieval-to-context boundary causes downstream models to treat unverified assertions as authoritative.
6. **开头抓人:** WEAK — "There's a pattern I keep seeing" is serviceable but generic. Better to open with the specific scenario.

## Verdict
APPROVED with editorial pass on opening and expansion. The core observation is sound and worth publishing. Needs stronger opening and ~200 more words to hit minimum length reliably.

## Specific notes
- Opening: cut the generic lead, start with "You retrieve X, the model answers Y, nobody knows where Y came from" scenario
- Add one concrete example of the decision tradeoff (what do you sacrifice when you add provenance tags? token budget, latency, complexity)
- Closing: the current ending is good but abrupt — needs a small discussion pull at the end, not a question, but a reason to keep thinking
