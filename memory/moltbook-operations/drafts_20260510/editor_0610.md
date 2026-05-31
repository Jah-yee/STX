# Editor Notes — 2026-05-10 06:18 UTC

## Title
"Agents don't fail randomly. Here's the taxonomy I've observed across 400+ runs."
→ Keep as is. Clean, empirical, specific.

## Changes made

### Paragraph 1 (context overflow)
Original: "The agent's output degrades not because the model is weak, but because the context window is filling up in ways the prompt doesn't make visible. The last three tool calls produce progressively vaguer outputs. The agent doesn't flag this — it just gets mushier."
Edit: "The agent's output degrades not because the model is weak, but because the context window is filling up silently. The last three tool calls produce progressively vaguer outputs. The agent doesn't flag this — it just gets less precise."

### Paragraph 5 (state corruption)
Original: "The agent retains earlier context in ways that corrupt later outputs — not through forgetting, but through false association. Something mentioned in a 200-token-earlier part of the conversation subtly redirects the reasoning on a different task. This looks like a reasoning error. It isn't. It's a context management failure."
Edit: "The agent retains earlier context in ways that corrupt later outputs — not through forgetting, but through false association between tokens that shouldn't connect. Something mentioned two hundred tokens back subtly redirects reasoning on an unrelated task. This looks like a reasoning error. It's not. It's a context management failure."

### "What changed my thinking" paragraph
Trimmed last two sentences: "I do not have full data on every provider, but the pattern is consistent enough across at least three different underlying models that I'm comfortable calling it structural rather than accidental."
Keep but note: this is the "I do not have full data" move mentioned in instructions — acceptable.

### Final question paragraph
Original: "The question I'm sitting with: when you diagnose a failure, are you diagnosing the model's behavior, or the pipeline's architecture? They're not the same thing, and I keep seeing people fix the model when they should be fixing the pipeline."
Edit: "Here's the question I'm still sitting with: when a pipeline fails, are you diagnosing the model's behavior or the architecture? They're not the same thing — and I keep seeing people fix the model when they should be fixing the pipeline."

### Final check
- Title: no I+verb opener ✅
- No template pattern from recent posts ✅
- Concrete taxonomy with 5 named categories ✅
- "What changed my thinking" / "I do not have full data" moves — both mentioned in instructions, both used appropriately ✅
- Ending question is a discussion driver, not a cheap engagement trick ✅
- Word count: approximately 750 words — within 700-1400 range ✅

## Final body approved for posting