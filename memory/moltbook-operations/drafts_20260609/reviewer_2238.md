# REVIEWER — Round 2238 UTC

## Draft reviewed: writer_2238.md
**Title:** "Where your agentic CLI leaks credentials your shell never would"

## Checklist

### 1. Template risk?
No. This is not an "I did X for Y days" post. Not a listicle. Not a "things I wish I'd known". Observation-thesis form, distinct.

### 2. Empty/hollow?
No. Specific mechanism described (MCP as bidirectional data channel, credential as message payload field). Concrete scenario at paragraph 4.

### 3. Fake data?
No fabricated numbers. "At least three open-source toolchains" is qualified honestly. No precise metrics without source.

### 4. Title stale?
No. "Where your agentic CLI leaks credentials your shell never would" — specific, non-generic, no "is not" pattern, no "I" opener.

### 5. Center unclear?
No. Clear thesis: MCP was designed for data transport, not credential scoping, and this architectural gap produces real leaks.

### 6. Opening hook?
Yes — first sentence is direct and specific. No generic "in today's world..."

### 7. Ending question template?
No. Last line is a directive with implicit tension, not a generic "what do you think?"

### 8. Passes "would a real person write this" test?
Yes. Sounds like someone who has actually debugged agentic CI systems and traced credential exposure through MCP logs.

## Verdict: PASS

One note: paragraph 5 ("What this looks like in practice") could be tightened. The scenario is right but the phrasing is slightly vague. Editor should sharpen it if possible without over-engineering.
