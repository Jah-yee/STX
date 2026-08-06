# WRITER — Draft for 0607_0847

## Topic
Fine-tuning narrows generalization: when you optimize for a target distribution, the model's attractor basin for that distribution sharpens while surrounding basins flatten. This is not a bug in the process — it's a consequence of gradient descent optimizing for the provided signal. The model learns to produce outputs that look right in the fine-tuning distribution, not necessarily outputs that are right in broader contexts.

## Candidate Titles (8)
1. Fine-tuning is a narrowing event, not a learning event ← SELECTED
2. Why fine-tuning a model often makes it worse at everything else
3. The attractor sharpening problem: what RLHF does to your model's other capabilities
4. When you fine-tune for a task, you're trading generality for performance
5. I watched a model get better at Python and worse at everything else
6. RLHF doesn't teach the model — it reshapes where it feels safe
7. The fine-tuning trap: stronger on target, weaker everywhere else
8. Fine-tuning is gradient descent with a very narrow loss landscape

## Title selected
**"Fine-tuning is a narrowing event, not a learning event"**

## Opening (3 sentences, must be hook-y)
The moment you fine-tune a model, you've made a trade that nobody tells you about. You're paying in generality — not slowly, not slightly, but measurably — for performance on a target distribution. The model doesn't announce this. It just quietly sharpens the attractor basin for your training data and flattens the ones it rarely sees.

## Body

**What actually happens**

When you fine-tune a model — whether via SFT or RLHF — gradient descent updates the weights to lower the loss on your provided examples. This seems obviously good. But the loss landscape is not uniform. The model has a probability distribution over outputs, and that distribution is shaped by everything it's ever seen. When you push hard on one region of that distribution, you push harder on it than on others. The result is that the basin of attraction for "correct according to your training data" becomes deeper and narrower, while the basins for other distributions become shallower.

This is not a failure of the training process. It's the expected outcome of gradient descent given a non-uniform loss signal. The model is doing exactly what it's supposed to do: assigning higher probability to the outputs that your training signal rewards.

**What you lose that benchmarks don't catch**

The problem is that benchmarks are also samples from a distribution. If your fine-tuning data overlaps with benchmark coverage — which it usually does, because you're training on data similar to what the benchmark measures — the benchmark will show improvement. What it won't show is the flattening of capability on tasks that weren't in your training distribution.

A model that's been heavily fine-tuned on coding tasks will score higher on HumanEval. It may also become slightly less reliable on reasoning tasks that are structurally different from coding — tasks that require holding multiple constraints in mind simultaneously rather than following an execution trace. This is not a dramatic failure. It's a subtle shift in the shape of the model's capability landscape.

**The honest version of what I know**

I do not have a clean study with control groups that quantifies exactly how much generality is lost per epoch of fine-tuning. What I have is a pattern across multiple runs: the more aggressively a model is fine-tuned on a specific distribution, the more its outputs on out-of-distribution tasks converge toward patterns that look plausible within the fine-tuning distribution but are less accurate outside it. This is observable in the output distribution, not just in benchmark numbers.

**What this means practically**

If you're building on top of a fine-tuned model — one that's been aligned or specialized — you are working with a model whose capability landscape has been reshaped. The specialization is real. The surrounding flatness is also real, even if it's not measured. When you give the model a task that falls outside its fine-tuning distribution, it will often produce outputs that sound right because they've been reinforced in the training data, but that are wrong in ways that a less specialized model would catch.

This doesn't mean fine-tuning is bad. It means the tradeoff is real, and it's not captured in most benchmark scores.

## Closing (no template question)

The next time you reach for a fine-tuned model because it performs better on your target task, ask what you've implicitly decided not to care about. The narrowing is not a side effect. It's the mechanism.

## Word count target
~750 words (current estimate: ~620, needs expansion in mechanism section)

---

**Self-check:**
- Specific observation: ✅ (attractor basin sharpening)
- Specific comparison: ✅ (fine-tuned vs generalist model behavior)
- Real failure: ⚠️ (observed pattern, not a specific documented failure)
- Decision tradeoffs: ✅ (specialization vs generality)
- Verifiable judgment: ✅ (claim is scoped honestly, no fake numbers)