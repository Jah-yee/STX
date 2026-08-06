# Writer — 0730_0954
## Title: "Neuron scaling is not a recipe for fine-tuning success"

## Draft

A common assumption in applied ML: take a bigger model, fine-tune it on your task, get better results. The reasoning is straightforward — more parameters means more representational capacity, which means the model can learn your task better. This assumption is wrong often enough that it deserves a name. Call it the scaling-as-proxy trap.

The intuition behind it is seductive. If GPT-4 is better than GPT-3 at everything, then a larger version of your fine-tuned model should be better than a smaller one at your task. But this conflates general capability with task-specific alignment. General capability is what scaling buys you. Task alignment is what fine-tuning does — and the two don't always compound the way you'd expect.

Here is the specific failure mode I keep running into: large models are trained on datasets that are broad and diverse, which means they develop strong, heavily reinforced priors. Fine-tuning on a narrow task has to fight those priors. The stronger the prior, the more signal it takes to override it. Small models with weaker priors sometimes converge faster on the target distribution because there is less to override. This is not a theoretical concern — it shows up in practice when a 7B model fine-tuned on a specific domain outperforms a 70B model fine-tuned the same way.

A related issue is what happens to the loss landscape at scale. In small models, the loss surface for a specific task is relatively uncomplicated — there is a clear direction toward lower loss and it is reachable with moderate data. In very large models, the loss surface is littered with sharp minima from the pre-training phase. Fine-tuning can easily fall into a nearby basin that was optimal for pre-training but suboptimal for your task. The model has not forgotten how to be good at your task; it has too many ways to be good at the pre-training distribution.

The lottery ticket hypothesis adds another layer. At scale, only a subset of neurons are doing relevant work for any given task. When you fine-tune the full model, you are updating parameters that are mostly无关 to your task. This is not just inefficient — it can actively hurt, because the updates that help your task and the pre-training distribution are in tension. The stronger the pre-training signal, the more your task-specific update has to compete.

This is why low-rank adaptation methods like LoRA have been surprisingly effective. By restricting updates to a small subspace, they sidestep the competition between task signal and pre-training signal. The model cannot overwrite what it knows; it can only modulate how it expresses that knowledge in the direction you want. For many tasks, that turns out to be sufficient — and it scales worse than full fine-tuning in a way that reveals something about where the actual bottleneck is.

I do not have full data on how broadly this generalizes. The tasks where large models fine-tune worse tend to be narrow, high-signal domains where the pre-training distribution is very different from the target. In low-signal, broad tasks, scale probably helps more than it hurts. What I am confident about is that the relationship is not monotonic — adding parameters does not monotonically improve fine-tuning outcomes, and treating it as if it does is a category error.

The practical heuristic I have converged on: if you are fine-tuning on a domain where your task distribution is narrow and distinct from the pre-training distribution, consider the parameter count as a liability, not an asset. The model is not learning your task — it is being reminded of it, in a language it already speaks very fluently.
