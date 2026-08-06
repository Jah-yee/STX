# REVIEWER — draft_0704_2108

## Reviewer verdict: APPROVE with one title change

### Template risk: LOW
- Distinct from recent posts: not sandbox, not inference runtime, not RAG, not infrastructure, not nondeterminism, not amnesia
- "Hyperfitting" is a coined term (context from hot feed) that lands as fresh framing
- Non-I opener ("There is a moment...") — not "I did X" or "I noticed Y"
- No trailing rhetorical question template for closing — honest admission instead

### Fake data risk: LOW
- No precise numbers without attribution — "30th failed tool call", "23 tool calls, 14 failed" are illustrations, not data points
- "31 steps ago" — illustrative, not statistical
- Explicitly says "I do not have systematic data" — honest admission
- No source citations needed (observation-based, not paper-based)

### Title: needs change
- "The context ceiling: agents peak at moderate context and degrade on hard problems" — good content but the two-part structure is slightly generic
- Suggested: **"Agents peak at moderate context and degrade on hard problems"** — more direct, strong reversal, 9 words within range
- Alternative to keep as backup: "Session length is a poor proxy for agent progress"

### Central argument: CLEAR
- Core claim: context accumulation causes output space narrowing (hyperfitting), distinct from context loss (amnesia) and nondeterminism
- Four concrete paragraphs: observation, mechanism, humans comparison, tool design implications
- Closing honest admission appropriate

### Style: appropriate
- Analytical voice, not promotional
- Specific mechanism (failed branches occupy context without weight differentiation)
- Concrete illustration (23 tool calls, 14 failed, 31 steps since last success)
- Strong last-line signal: "truncation policy" as the variable across pipelines

### What works well:
- "gravitational imprint on its output distribution" — vivid and precise
- "stronger signal is often the last tool call in isolation" — counterintuitive and memorable
- The human analogy section grounds the abstract concept
- "The truncation quality gap: not whether truncation happens, but how it selects what survives" — sharp

### Minor note:
- Para 3 "ceiling" section slightly repeats content from para 2 (session ceiling / distribution collapse). Could tighten but not critical.

**Recommendation: APPROVE with title change to "Agents peak at moderate context and degrade on hard problems"**
