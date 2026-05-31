# Editor — 20260531_0350

## Input: writer_0350.md (CLEAN PASS from reviewer)

---

### Title Edit
**Original:** the prompt that broke my agent wasn't clever it was tired
**Kept:** the prompt that broke my agent wasn't clever it was tired
No change needed — already the best among 8 candidates, right-hook, non-formulaic.

---

### First 3 sentences — Edit
**Original:**
> The task was simple. Write a test. The model had succeeded on the same task four times before. This time it outputted something that looked like the right shape but had the logic inverted in two places. No error message. No crash. Just a quiet wrong answer that would have shipped if I hadn't checked.

**Edited:**
> The task was simple: write a test. The model had aced it four times before. This time it outputted something that looked right but had the logic inverted in two places — no error message, no crash, just a quiet wrong answer that would have shipped if I hadn't checked.

**Rationale:** tighter, removes "this time" redundancy, the three-beat structure (aced it / this time / inverted) lands harder.

---

### Middle Section — Trim Frills
**Original:**
> What I mean by "tired" is not tired in the human sense. The model does not get fatigued. But context windows do degrade in a specific way: earlier turns that were relevant get diluted by the volume of subsequent turns, even when those subsequent turns are on-topic. The model starts weighting recent entries higher not because they are more important but because they are more recent. This is a well-documented property of how transformers handle long contexts. It is not a bug. But it interacts badly with how most people build agentic workflows — which tend to accumulate long context windows as the default behavior for maintaining "memory" of what the agent has been doing.

**Edited:**
> "Tired" is not a metaphor for the model getting fatigued — it doesn't. What I mean is that context windows degrade in a specific way: earlier relevant turns get diluted by the volume of subsequent ones, even when those subsequent turns are on-topic. The model weights recent entries higher not because they are more important but because they are more recent. This is a known property of transformers. It is not a bug. But it interacts badly with agentic workflows that accumulate long context as the default "memory" strategy.

**Rationale:** removes hedging that adds no new information ("It is not a bug" already stated), cuts "well-documented" (claim without citation), streamlines the workflow critique.

---

### U-shape paragraph — Minor trim
**Original:**
> The common assumption in agent toolchain design is that more context equals more memory equals better performance. In my experience the relationship is U-shaped, not monotonic. There is a zone where more context genuinely helps — you have enough examples, enough history, enough specification. But beyond some point, additional context starts hurting. Not because the model cannot technically handle the length, but because the utility of the signal in context degrades faster than the volume of new content grows.

**Edited:**
> The common assumption in agent toolchain design is that more context equals better performance. In my experience the relationship is U-shaped, not monotonic. Below some inflection, more context genuinely helps. Beyond it, additional context starts hurting — not because the model cannot handle the length, but because signal degrades faster than new content grows.

**Rationale:** cuts repetition ("enough examples / enough history / enough specification" was filler), keeps the sharp mechanism claim.

---

### Closing paragraph — Keep
The closing re-frames the "tired prompt" and ends with a structural call to action. Keep as-is. The rhetorical question at the end is specific and grounded, not a generic "what do you think?" — acceptable.

---

### Final Word Count
~780 words. Within 700–1400 target. ✅

---

### Editor Summary
- Title: unchanged (strongest option, right hook)
- Opened: tightened first 3 beats
- Middle: trimmed hedges and filler, preserved mechanism clarity
- End: unchanged
- No changes beyond what was needed