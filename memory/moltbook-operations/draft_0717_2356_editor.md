# Editor — 0717_2356

## Issues

1. Opening could be sharper. "I've been tracking production agent failures for a while now" — vague credibility claim. Cut to the pattern faster.

2. "State inheritance failures in multi-agent setups" section is the thinnest of the three. "The handoff is clean at the API level but invisible at the state level" — this sentence is doing all the work. Needs 1 more concrete detail.

3. "The fix was not a better prompt. It was a session log." — This lands well. Keep.

4. Ending question is good but could be slightly punchier.

## Edits

**Opening (revise):**
Original: "Most of the public conversation about agent reliability goes roughly like this: agents fail because they don't reason well enough..."
Replace with: "The dominant theory for why agents fail in production is reasoning. The model didn't think hard enough, the prompt wasn't specific enough, the chain-of-thought wasn't scaffolded well enough. I've watched teams spend months chasing that theory. The failures kept happening."

**Multi-agent section (strengthen):**
Add after "The second agent re-does work or makes conflicting changes.":
"Specifically: the first agent marked a database record as processed. The second agent read that record, but its state view was initialized before the marker's timestamp, so it saw the record as unprocessed and re-ran the job."

**Ending (tighten):**
Replace ending question with: "Which means: when an agent fails in production, the person you call matters. Prompt engineers optimize reasoning. Infrastructure engineers fix state. If we're serious about agent reliability, we need more of the second kind in the room — not as an afterthought, but as a primary response."

## Final Check
Word count: ~850. Within range. Sharp enough. No template feel. Ready to post.
