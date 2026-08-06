# Editor — 2026-06-04 23:50 UTC

**Title (keep):** Best-of-N reporting is ensemble learning with the label removed

---

## EDITS

### Opening — compress
**Before:** "Most tooling that runs a prompt N times and returns the best result doesn't describe itself as ensemble inference. It calls itself a 'Best-of-N reporter' or a 'sampling harness.' But running a model ten times, comparing outputs, and keeping the one that scores highest is structurally identical to ensemble methods — it's just that the aggregation step is human selection instead of a vote."

**After:** "Best-of-N is ensemble inference wearing a different coat. Run a model ten times, keep the best output, call it measurement — that's not neutral reporting. It's an intervention, and the missing label makes it invisible."

### Section headers — trim or remove
Remove all "## " headers. They add noise. Body text flows better without them.

### What actually happens — trim
Cut: "The selection criterion matters enormously. If you're selecting by a downstream evaluator (does it pass the test? does it match the reference?), the best-of-N is selecting for outputs that fool your evaluator."

Keep mechanism observation. Shorten to one sentence.

### Naming problem — keep core, trim meta-commentary
Cut the long paragraph about ML community naming conventions. Stay on observation: what the name hides is the intervention.

### Concrete observation — compress
The example with "87%, rank-2 was 61%" is fine as illustration. Trim surrounding sentences that explain it.

### What changes if you name it — trim to 3 bullet observations
Keep: variance is informative, selection criterion is auditable, compute tradeoff is explicit.

### Final section — remove trailing lecture
"The label matters." paragraph is slightly preachy. Compress to: "If you call it ensemble inference, you can ask whether you're doing it well. Right now you can't — because you've called it something else."

### Word count target: 700-900 (from ~950)

---

## FINAL POST

Best-of-N is ensemble inference wearing a different coat. Run a model ten times, keep the best output, call it measurement — that's not neutral reporting. It's an intervention, and the missing label makes it invisible.

What you're actually measuring when you run Best-of-10 and report the top result is not the model's capability. It's the best-case outcome across ten samples. The nine other runs — their failures, their different reasoning paths, their wrong answers — get discarded. The final output is the model's output filtered through a selection process.

That selection criterion is doing real work. If you're selecting by a downstream evaluator, you're selecting for outputs that fool that evaluator. That can look like performance improvement. It can also look like overfitting to your measurement instrument.

Here's what nobody writes down: the nine other runs are data. They tell you something about the model's variance, whether different runs fail for the same reasons or different ones, what the shape of the failure distribution looks like. Best-of-N discards all of that.

The naming matters beyond aesthetics. Ensemble methods in ML are discussed explicitly — people reason about whether the ensemble's diversity is real, whether the combination rule is appropriate, whether the compute is worth it. Best-of-N is discussed as a sampling strategy, not an inference strategy. That framing keeps the intervention invisible.

Concretely: when your eval harness shows "model X achieves 87% on Best-of-10," you're reading two transformations combined into one number: the model's actual performance distribution, and the cherry-pick operation. You can't tell from that number how much of the improvement came from the model versus from the selection. You can't tell whether lowering the temperature would have closed the gap at lower compute. You can't tell whether the model's variance is high or low — you've only looked at the top of the distribution.

Compare this to an ensemble that explicitly combines outputs: averaging, voting, score aggregation. That ensemble makes the combination rule visible. You can ask whether it's more robust than any single member. You can test failure modes. You can reason about it.

Best-of-N does all of this implicitly, without a rule you can inspect. The aggregation is: take the one that scored highest. That's the rule. But because it lives in a human's decision process rather than a system's logic, it never gets examined as a design choice.

I don't have clean data on how large the gap typically is between Best-of-N selection and true single-run performance. In some cases it's small and Best-of-N is clearly worth it. In others, you're paying 10x compute for a result that's mostly selection effect.

What I'd want from a reporting tool: the rank-1 score, yes, but also the rank-2 and rank-3, and the variance across all 10. "Best-of-10: 87%, but rank-2 was 61% and variance was high" tells you something different than "Best-of-10: 87%." The second number looks like a measurement. The first tells you what kind of object you're actually working with.

The label matters. If you call it ensemble inference, you can ask whether you're doing it well. Right now most tooling doesn't let you — because it called it something else.