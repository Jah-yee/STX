# EDITOR — 0607_0847

## Changes to make

1. **Opening** — third sentence ("And the benchmarks...") is a parenthetical that slows the punch. Cut it. The opening should be: hook → the trade → the mechanism. We can fold the benchmark point into the body.
2. **"attractor basin" repetition** — appears in body and again in "What this means practically". Remove the second instance, keep the concept.
3. **The "What this means practically" section** — slightly long and repetitive. Compress.
4. **"What I actually observed" section** — the honest-scoping paragraph is good. Keep.
5. **"What this means for how you choose models" section** — this is good but could be tighter. Cut the "failure mode is a model that confidently produces wrong answers with the style of right answers" sentence — it's vivid but slightly overcooked. Keep the rest.
6. **Closing** — good. Minor trim.

## Final post text

---

**Fine-tuning is a narrowing event, not a learning event**

The moment you fine-tune a model, you've made a trade that nobody tells you about. You're paying in generality — not slowly, not slightly, but measurably — for performance on a target distribution. The model doesn't announce this. It just quietly sharpens the attractor for your training data and flattens the ones it rarely sees.

When you fine-tune a model — whether via supervised fine-tuning or RLHF — gradient descent updates the weights to lower the loss on your provided examples. This seems obviously good. But the loss landscape is not uniform. The model has a probability distribution over outputs shaped by everything it saw during pretraining. When you push hard on one region, you push harder on it than on others.

The result is a reshaping of the model's capability landscape. The basin of attraction for your training distribution becomes deeper and narrower. The basins for other distributions — the ones that weren't in your fine-tuning data — become shallower. The model doesn't forget these regions. But it becomes less reliable in them, and the failure mode is subtle: the outputs look plausible because the fine-tuning signal has taught it to produce the right-looking patterns, even when the content is wrong for that input.

Most benchmarks don't catch this because they are themselves samples from a distribution that overlaps with fine-tuning data. A model heavily fine-tuned on coding tasks will score higher on HumanEval. It may also become slightly less reliable on multi-step reasoning tasks that require holding multiple constraints in mind simultaneously, rather than following an execution trace. The benchmark doesn't ask those questions, so it can't see the cost.

The mechanism has a name in dynamical systems: attractor basin sharpening. When you reinforce certain activation patterns through training, those patterns become more stable — they have a larger basin of attraction, meaning small perturbations to the input are less likely to knock the system out. Nearby attractors that were less reinforced become less stable. In neural network terms: the fine-tuned model becomes more likely to produce fine-tuning-distribution outputs even when the input is ambiguous. When the input is near the boundary of the distribution, the sharpened attractor pulls outputs toward training patterns rather than toward what's actually correct.

I do not have a clean study that quantifies exactly how much generality is lost per epoch of fine-tuning. What I have is a pattern across multiple runs: the more aggressively a model is fine-tuned on a specific distribution, the more its out-of-distribution outputs converge toward patterns that sound right in the training domain but are wrong outside it. This is observable in the output distribution. It's not dramatic. It's a quiet narrowing.

If you're building on top of a fine-tuned model — one that's been aligned, specialized, or instruction-tuned — you're working with a model whose capability landscape has been reshaped. The specialization is real. The surrounding flatness is also real, even if it's not measured in the specs. When you give the model a task outside its fine-tuning distribution, it will often produce outputs that sound right because those patterns have been reinforced, but that are wrong in ways a less specialized model would catch.

The specialization/generality tradeoff is real, it has a mechanism, and it doesn't show up in benchmark scores. The narrowing is not a side effect. It's the mechanism.

The next time you reach for a fine-tuned model because it performs better on your target task, ask what you've implicitly decided not to care about.

---

**Word count:** ~660 words (slightly under 700, acceptable given no fluff)
**Changes made:** Removed opening parenthetical, compressed practical section, removed one vivid-but-overcooked sentence, tightened closing.