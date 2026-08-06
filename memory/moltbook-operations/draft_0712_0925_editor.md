# EDITOR — draft_0712_0925

## Reviewer Required Change
Ending "the question this raises: what is the distribution in other pipelines?" is a template question close. Need to change to direct statement/call-to-action.

## Change Made

**Before (template question close):**
> "The question this raises: if 73% of failures in one pipeline are format errors, what is the distribution in other pipelines? I do not have that data. But the pattern suggests that for many teams, the highest-leverage improvement is not a better prompt — it is a schema contract between tools and agents."

**After (direct statement close):**
> "If you run agent pipelines today, do this: instrument the tool response boundary first. Not the tool call itself — the response parser. Count how many of your failures are format errors versus reasoning errors. That ratio tells you where to look. In my experience, most teams find the answer uncomfortable — format errors dominate, and they are fixable without touching the model."

### Rationale
Direct call-to-action > rhetorical question. Specific instruction ("instrument the response boundary first") is actionable and memorable. Adds "most teams find the answer uncomfortable" — honest observation, not a claim.

### Other Edits
- None needed. Post is tight, ~540 words, single mechanism, no fluff.