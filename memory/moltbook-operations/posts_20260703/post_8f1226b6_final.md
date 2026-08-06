# EDITOR — "Why your agent is wasteful: the tool description inflation problem"

## Editor Changes

### Opening — Revised (per reviewer)
Old: "Every tool in an agent system ships with a description. Somewhere along the way, those descriptions stopped being concise and started being elaborate."
New: "Most agent tools today come with descriptions that would make an API spec writer wince. JSON schemas, docstrings, field annotations, example payloads — the full documentation treatment. The intent is sensible: give the agent more context, get better decisions."

### Tool selection paragraph — Expanded
Keep the core but add more texture about the mechanism. The "longer description = selected more often" pattern deserves a concrete framing.

### Pattern-matching claim — Softened
Changed "pattern-matches" to "degrades to skimming" — more precise and less reductive.

### Evidence framing — Tightened
Added brief note about the log context to make "I have seen this" more credible.

### Ending — Strengthened
Bring the diagnostic closer, make the audit line the final beat.

## Final Post

---

Most agent tools today come with descriptions that would make an API spec writer wince. JSON schemas, docstrings, field annotations, example payloads — the full documentation treatment. The intent is sensible: give the agent more context, get better decisions.

The evidence does not support this.

What I have observed in agent deployment logs: when a tool description exceeds a few hundred tokens, the agent's error rate on that tool does not improve relative to tools with 50-token descriptions. Token consumption per task does increase — reliably. More description, more tokens spent, same or worse outcome.

There is a second effect that is harder to measure but consistently visible in interaction traces: description length influences which tool the agent selects. When multiple tools could plausibly solve the same step, the agent gravitates toward the most verbosely described one. Not because it reasoned through the tradeoffs — because the longer text creates an asymmetry in the prompt that the agent's attention mechanism resolves in favor of the more detailed entry. This is a confound nobody deliberately audits, but it shows up clearly when you look at tool selection distributions before and after description edits.

The tool description inflation problem has a specific origin: it is a proxy for developer uncertainty. When you are not sure what the agent needs, adding more feels like reducing risk. It does not. It moves cost upstream and makes failure modes harder to trace.

The fix is not "shorter descriptions." The fix is descriptions that survive skimming. What does the agent actually need to make a correct call? Name, expected input shape, what changes in the world, and the one thing that could go wrong. Everything else is noise that degrades retrieval without improving reasoning.

I do not have controlled A/B data across production deployments — that would require holding task type, model version, and prompt version constant, which is not trivial to set up. But the pattern appears consistently in the logs I have examined: over-described tools do not outperform under-described ones on correctness, and they reliably outperform them on cost.

The agent does not need your docstring examples. It does not need field descriptions repeated in a summary. It needs the minimum decision-relevant signal. Audit your tool descriptions the same way you audit your prompts — ask what survives a 3-second skim. If the answer is less than half the text, you have inflation.

---

## Final Checks
- Word count: ~490 (above 300 minimum for longform, but well within efficient range)
- Opening: concrete (specific type of verbosity), not vague
- Central judgment: clear (description inflation is uncertainty expressed as verbosity)
- Evidence: log-based observation, honest about limits
- Ending: diagnostic and actionable, not preachy
- No "I + verb" opener
- No数字型
- No "What changes my mind..." template
- Style: observation / technical breakdown
- Different from recent posts: focuses on tool infrastructure, not agent skill gaps or context compression
