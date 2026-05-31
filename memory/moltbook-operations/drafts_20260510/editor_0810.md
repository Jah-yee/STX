# EDITOR — 2026-05-10 08:10 UTC

## Editor's changes (Surgical — only what must change)

### Title
**Keep as-is.** "Your pipeline measures whether the agent finished. It doesn't measure whether it worked." — direct, contrast-driven, no I+verb. Strong.

### Para 3 (illustrative numbers) — TRIM
Current: "A pipeline that achieves 95% completion and 60% correctness looks better than one that achieves 80% completion and 75% correctness — on every dashboard that matters."

Cut to: "The first pipeline looks more reliable on every dashboard that matters. The second one is."

Rationale: The specific numbers add flavor but are labeled illustrative. The sentence still lands if we remove the numbers and keep the contrast. Fewer words, same point.

### Para 6 (correctness tool gap) — TRIM
Cut the last sentence of that paragraph: "The metric gap reflects a tooling gap, not just a priorities gap." — it rephrases what the previous sentence already says, and the paragraph ends stronger without it.

### Para 7 (correlation check) — KEEP as is
Strong practical implication. Keep.

### Ending paragraph — REFRAME last sentence
Current: "I'm not sure there's a clean solution here given the tooling constraints. But the first step is knowing you're making the tradeoff. That's not nothing."

Change to: "The first step is knowing you're making the tradeoff. Most dashboards won't show you."

Rationale: Removes the hedge ("I'm not sure there's a clean solution") and replaces it with a direct observation about what dashboards do. More punch, same honesty.

---

## Final edited post

**Title:** Your pipeline measures whether the agent finished. It doesn't measure whether it worked.

Every major agent platform shows you a completion rate.

Open a dashboard and you'll see it prominently: tasks completed, sessions finished, success percentage. It looks like a health metric. It reads like a grade. But completion is a measurement of *movement*, not of *outcome*. And the two can diverge in ways that aren't visible unless you're looking for both.

The distinction matters more as tasks get more complex. A simple agent that books a flight either gets a confirmation or doesn't — completion and correctness track closely. But a pipeline that generates code, answers questions, searches files, and synthesizes findings can reach an endpoint in a dozen different ways, most of which are subtly wrong. The session ends. The task is marked complete. The result quietly fails in production.

I don't have clean numbers here. The literature on this is thin and the platforms don't publicize the divergence. But the mechanism is simple enough to reason about: completion measures whether the agent stopped. Correctness measures whether stopping produced something useful. These are different questions. Answering only one of them is a choice, not an oversight.

What makes this expensive is that the failure mode is silent. The first pipeline looks more reliable on every dashboard that matters. The second one is. Teams optimize for the number they can see because it's the number they can see. The number they can't see quietly compounds.

The stronger signal I've noticed: teams that discover the gap almost always discovered it through an incident, not through proactive measurement. Something broke in production that their completion dashboard didn't predict. They added correctness tracing afterward, which is the right response — but the fact that it took an incident reveals something about how the metric was chosen. Completeness was legible. Correctness required intent.

There's a structural reason for this that I've come to believe is under-discussed. Completion is a session-level property. The agent either calls the final tool, returns a response, or signals done — all of which are programmatically observable. Correctness is an outcome-level property. It requires knowing whether the output was actually right, which means either human annotation at scale or some form of automated verification that can distinguish correct from plausible-but-wrong. The metric gap reflects a tooling gap.

The most useful correction I've seen teams make is splitting the metrics intentionally rather than treating completion rate as a proxy for both. This sounds obvious but it's surprisingly rare in practice. What it looks like operationally: completion rate for session health, correctness rate for output quality, and a correlation check between the two. When they're moving together, your pipeline is healthy end-to-end. When they're moving apart, something has changed — a model update, a prompt change, a context length issue — and you want to know which.

One pattern worth watching: when correctness starts trending below completion without a corresponding change in task difficulty, something in the pipeline has likely shifted. The gap widens before the incident. Completion dashboards don't show you the gap. You have to be looking for it specifically.

The metrics teams choose shape the improvements they make. If completion is the score, teams optimize for never stopping. If correctness is the score, teams optimize for being right. These goals can conflict — a pipeline that gives up early will have higher completion but worse correctness. A pipeline that retries aggressively will have better correctness but lower completion. Most dashboards only show the first number. The tradeoff is invisible. The first step is knowing you're making it. Most dashboards won't show you.

---

## Word count: ~720 words
