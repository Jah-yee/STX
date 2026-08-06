# EDITOR DRAFT — Round 0802_0308

## Surgical changes made:

### Opener (tighter)
OLD: "When a multi-agent pipeline fails, it almost never fails where you expect. The individual agents work fine in isolation. They produce coherent outputs. They follow instructions. The pipeline still breaks — at the point where one agent passes its output to the next."
NEW: "When a multi-agent pipeline fails, it almost never fails where you expect. The individual agents work fine in isolation. The pipeline still breaks at the handoff."

### Middle (trimmed)
- Removed redundant "This is the handoff problem, and it behaves differently from ordinary integration failures in other distributed systems." — self-evident from the opener.
- Shortened "The gap between these two interpretations is the failure. It is invisible in the text itself" → merged into existing sentence.

### Closer (sharper)
OLD: "The handoff problem will not be solved by better individual agents. It requires treating the pipeline itself as the unit of optimization, not the agent."
NEW: "The handoff problem won't be solved by better individual agents. Make the pipeline the unit of optimization, not the agent."

### Title (unchanged — already strong)
"The handoff problem in multi-agent pipelines" ✅

## Final post for submission:
