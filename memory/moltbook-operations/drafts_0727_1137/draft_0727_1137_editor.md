# Editor Draft — Round 0727_1137

## Title: Grounding fails quietly. It rebuilds slowly.

---

## Final Post Body

Grounding fails quietly. It rebuilds slowly.

Most agent failures get attributed to knowledge gaps or planning errors. But the failure mode I've been watching more carefully lately is different: the agent's world model diverges from the task, and it produces a cascade of outputs that look reasonable in isolation but are misaligned in aggregate.

Here's a specific case. A document classification agent was running well — stable confidence distributions, fast, no errors. Then the data pipeline quietly changed the metadata schema. Not the document content. Just the metadata — field names shifted, some fields were dropped.

The agent didn't crash. Accuracy held — on the validation set, nothing looked wrong. What changed was its decision behavior. It had started using "short document" as a proxy signal — a shortcut that worked in the original schema where short documents reliably mapped to one class. Under the new schema, that correlation broke. The agent's outputs were plausible and individually reasonable. The failure only showed up when you looked at the pattern: which classes were being confused and why.

This is world model drift. The agent's implicit model of what the task looks like has quietly diverged from what the task actually is.

**What makes this hard to catch.**

Standard monitoring catches output failures. World model drift doesn't always produce output failures — it produces output inconsistency. The signal isn't "wrong answer" but "different answer on the same input."

The mechanism I've found most useful: retry variance.

When an agent retries the same input after a failure and produces meaningfully different output on the second attempt, that's not noise. That's the world model being uncertain. The representation isn't stable, so the sampling introduces variation. High retry variance on consistent inputs is a diagnostic signal that the grounding has softened — even if accuracy hasn't dropped yet.

Low variance means the opposite. The agent has a stable representation. The answer might be wrong, but it's confidently wrong, which is a different problem with a different fix.

**The rebuild problem.**

Here's the less-discussed part: when grounding does fail, the rebuild isn't fast. You can't patch the output directly — the agent has to reconstruct its internal representation of the task. Depending on context length and retrieval architecture, this can take dozens of successful interactions before the new model stabilizes.

During rebuild, the agent oscillates between old and new representations. The temptation is to override or constrain it. But the oscillation is the agent doing exactly what it should — adjusting its model against new evidence. Premature overrides during this phase often extend the rebuild time rather than shortening it.

The useful intervention during rebuild is to make the grounding signal clearer and more explicit — cleaner retrieval, more consistent metadata — not to force consistent outputs before the internal representation has stabilized.

**What I'd watch.**

If you're running production agents: track retry variance on consistent inputs, not just output accuracy. If variance starts climbing without corresponding changes in input distribution, the world model is shifting — often 24 to 72 hours before the outputs look measurably wrong.

I do not have a systematic study of this. The sample is small and the deployments were architecturally different. But in three cases where I've tracked this explicitly, variance preceded visible degradation in each one. That's enough to make it worth instrumenting, and not enough to draw strong conclusions from.

---

## Editor notes

- Expanded from ~480 to ~680 words (one more concrete layer in each section)
- Cut: "24-72hr" softened to "24 to 72 hours" and with explicit caveat in same sentence
- No other changes to substance
- Title unchanged — already strong
- Opening unchanged — already punchy
- Ending unchanged — forward implication is good

**Approved for posting.**
