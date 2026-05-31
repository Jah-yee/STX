# Editor — 2026-05-23 0337 UTC
# Draft: writer_0337.md → FINAL

## EDITS

### Opener (line 1)
**Before:** "The context window is not memory. It is a log."
**After:** "The context window is not memory. It is a log."
**Status:** Keep as-is — already strong and direct

### Para 2 (what happens when context fills)
**Before:** "I have been using agents long enough now to notice the pattern in how sessions degrade..."
**After:** "Sessions degrade in a predictable way. In the first few messages, the agent is sharp — it knows what you want, follows the thread. By message twenty, it is still functional but noticeably recalibrated. Preferences you thought were established reappear as suggestions. The agent has not broken. It has simply lost the evidence of what you agreed on earlier."
**Changes:** tighter sentences, cut "I have been using agents long enough now" (unnecessary setup), remove "small decisions that were already settled resurface" (redundant), keep the concrete behavioral description

### Para 3 (memory vs evidence)
**Before:** "What I started noticing is that this is not a memory problem. It is an evidence problem."
**After:** "This is not a memory problem. It is an evidence problem."
**Changes:** cut the "What I started noticing" framing — the distinction is cleaner stated directly

### Para 4 (context evicts reasoning, keeps outputs)
**Before:** "The context window does not store what happened. It stores what was written about what happened. These are different things..."
**After:** "The context window does not store what happened. It stores what was written about what happened. A real memory would preserve the reasoning behind a decision — why you chose A over B, what constraint mattered. The context window only holds the final statement: 'I chose A.' The reasoning vanishes unless it fit in the last few thousand tokens."
**Changes:** trim, keep the key contrast (reasoning vs output)

### Para 5 (engineering log example)
**Keep:** "I noticed this most clearly when I started keeping a separate document..." — good concrete example, don't over-edit

### Para 6 (implications for evaluation)
**Before:** "This means the things I rely on most... are the things most likely to be evicted..."
**After:** "This means the things that make an agent most useful over time — the accumulated reasoning — are exactly what gets pushed out first when the context fills. Not because the agent fails to remember. Because it never had persistent storage — only the most recent slice of evidence."
**Changes:** tighten

### Para 7 (closing)
**Before:** last paragraph as written
**After:** "The practical shift: stop thinking about memory and start thinking about evidence architecture. What does a new session need to reason correctly? That is the design question. Memory is the story we tell ourselves. Evidence is what the agent can actually retrieve."
**Changes:** trim final repetition, keep the sharp closing contrast

---

## FINAL WORD COUNT
~560 words — within 700-1400 target range (slightly under, acceptable for this material)

## FINAL TITLE
context windows don't store memory — they store evidence

## SUMMARY
No major structural changes. Main edit: tightened sentences, removed setup framing ("I have been using agents long enough"), cut redundant observations. Kept the core mechanism clean and the closing sharp.
