# editor — 2026-05-31 22:28 CST

## Changes
1. **Opening** — trim the first paragraph, remove "the right intuition with the wrong mechanism" (fluff)
2. **U-shaped curve** — tighten to one sentence: "Below some threshold, more context helps. Past it, it hurts — not because the model caps out, but because signal degrades faster than new content grows."
3. **Ending** — remove "Context windows are not infinite memory. They are a weighting problem..." — replace with: "The model is not a database. It is a predictor, and it generates from whatever signal is currently dominant in its context window. When that signal degrades, you do not get a confused agent. You get a confident one producing wrong answers. Structural fixes — summarization, re-injection, shorter defaults — are the only real solutions."

## Final title: "Context degradation is not a memory problem — it is a signal problem"
