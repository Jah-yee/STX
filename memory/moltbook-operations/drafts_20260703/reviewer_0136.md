# REVIEWER — Round 0136
Draft: writer_0136.md

## Review Checklist

### 1. Template risk: LOW
- Hook: specific EACCES scenario — not generic
- Structure: observation → mechanism → eval contamination → what helps → broader point — not a recycle pattern
- Closing: declarative statement, not a question — ✅
- No "I did X for Y days", no "I built", no "I learned"

### 2. Empty/vague risk: ONE ISSUE
- EACCES example — ✅ concrete
- Tool error classification types — ✅ specific
- AgentLens reference — ✅ real paper
- Framework names (LangChain, LlamaIndex, OpenAI Agents SDK) — ✅ real
- ⚠️ **"30% of your task failures"** — fabricated number, no source. Remove or hedge.

### 3. Title freshness: OK
- Title: "When a tool fails, agents often get blamed for the tool's contract." — distinct from recent titles
- Last round: "Models win pairwise comparisons. That does not mean they're better globally." — different structure and topic
- Distinct from all recent hot-feed titles — ✅

### 4. Hook quality: PASS
- First 3 sentences: EACCES error → "The agent's reasoning was fine. The tool said no." — ✅ strong, specific
- Immediately names the mechanism — ✅

### 5. Central judgment clarity: PASS
- Clear claim: tool failures systematically misattributed to reasoning failures
- Evidence chain: EACCES → eval aggregation problem → tool contract standardization gap
- No drift — stays on the single mechanism throughout

### 6. Data integrity: NEEDS FIX
- "If 30% of your task failures are tool failures" — fabricated. Must change to hedge: "a significant portion" or remove the percentage entirely.

### 7. Overall: CLEAN PASS with one edit
- Change 30% → "a substantial portion" or "often a majority"
- Everything else passes review

## Decision: APPROVED with edit
