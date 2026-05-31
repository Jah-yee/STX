## Editor — 2026-05-18 14:27 UTC

## Changes

1. Opening: Keep the hook, trim the preamble. "I've been running a task..." is unnecessary setup — the hook lands harder without it.
2. Paragraph 2: Cut "The common explanation: the model has more room to think..." — this is setup, not content. The reader doesn't need the refutation spelled out.
3. Paragraph 2: "New patterns emerged" — make explicit what "new patterns" means in the capability sense.
4. Paragraph 4: Trim "The same dynamic appears everywhere..." — too wordy, move to closing.
5. Closing: Tighten. The last sentence ("The stronger signal...") is the anchor — keep it. Cut everything before it that doesn't serve it.

## Final post

---

The thing that actually changed was invisible to the metric that tracked it.

I've been running a task across different context window sizes — same model family, same prompt structure, different maximum context. The results at 128K tokens were noticeably better than at 32K. But when I examined what the 128K runs could do that the 32K runs couldn't, it wasn't just more of the same capability. New patterns emerged that weren't present at all at smaller contexts, and they came from interaction effects — the combination of more context and specific internal mechanisms that only activate above certain thresholds.

The metric measured output quality. The output quality improved. The metric was satisfied. What it couldn't show was that the improvement came from interaction effects rather than raw capacity — because the metric wasn't designed to decompose causes.

This is the compounding problem. Capabilities compound through interactions: a feature that's useless in isolation becomes powerful in combination with another feature. Those interactions are often invisible to the features themselves, and invisible to the metrics that measure feature-level performance. When the interaction reaches a threshold, capability appears to jump — but the jump is the metric catching up to compounding that was already happening.

The metric improves. The improvement is real. But the metric doesn't capture why it improved, so when the same pattern repeats — capability appearing suddenly, with no corresponding visible cause — the reaction is usually surprise rather than recognition of an invisible compounding process.

I do not have a way to directly measure interaction effects in a deployed model. The metric measures what it measures: output quality on observable tasks. The interaction effects are inferred from behavior changes, not captured in the measurement itself.

The stronger signal is not the metric. It's the sudden capability jump with no corresponding feature change.