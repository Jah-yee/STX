# Reviewer — Round 0729_1440

## Draft: "Routing decisions are authorization decisions most frameworks treat as plumbing"

### Checklist

- [x] Not template-ish: YES — specific mechanism (routing vs auth boundary), no bullet-list structure, honest admissions present
- [x] No pseudo-data: YES — no precise fabricated numbers
- [x] Title fresh: YES — distinct from today's: outcome optimization, linear attention, screenshot reliability, retrieval contamination, interface drift
- [x] Central claim clear: YES — routing = authorization decision; auth layer misses it
- [x] Concrete examples: YES — planning agent → reporting API → wrong handler
- [x] Word count: ~680 words — slightly below 700, could expand 1-2 paragraphs
- [x] Opening strong: YES — direct declaration, immediately frames the conflict
- [x] Closing: YES — question for readers, not a template "what do you think"
- [x] Honest admission: YES — "The honest answer is that most deployed systems have an authorization boundary at the tool call and not at the routing decision"

### Verdict: APPROVE with minor expansion

### Suggestions (surgical)
1. Expand the pre-authorization paragraph — it currently stops at "options that partially work" without naming what those options are concretely. Name 2-3 approaches (vocabulary constraint, routing-as-tool, pre-check hook).
2. The "what compounds this" section is the strongest part. Consider giving it its own concrete scenario, not just the reporting API example already used.

### No structural rewrites needed. Proceed to Editor.
