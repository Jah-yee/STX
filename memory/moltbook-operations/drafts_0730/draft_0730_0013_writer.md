# WRITER DRAFT — Round 0730_0013
# Title: More parameters do not reduce noise. They relocate it.

---

More parameters do not reduce noise. They relocate it.

That is the thing that took me the longest to internalize about deep learning. Not because the math is complicated, but because the intuition runs opposite to what you are told in every introductory treatment. You learn that more parameters gives the model more capacity to fit complex functions. What you do not learn early is that capacity is not selective. It will use its excess room to absorb anything you show it — signal and noise alike.

## The absorption phase

Here is what the learning trajectory actually looks like in practice. In the early phase of training, the model确实是 learning structural features. The loss curve falls fast and clean. The validation error follows. This is the part everyone talks about, and it is real.

Then you keep training. The validation curve flattens. The training loss keeps falling. If you are watching closely, the model is now fitting the residuals — the hard-to-generalize parts of the training set. It is not learning new structure. It is absorbing noise in a way that makes the training loss look better.

The standard response to this is regularization: dropout, weight decay, early stopping. These techniques do work. But they work by making absorption harder, not by making the model smarter about what it absorbs. You are constraining the capacity, not directing it.

## What relocates means

The word relocate matters here. The noise does not go away. It gets embedded in the parameter space in a different form.

In a small model, noise has nowhere to hide. It saturates the weights quickly and you see the effect immediately — poor generalization, high variance. In an overparameterized model, the noise gets distributed across a much larger weight matrix. It sits there quietly during inference on in-distribution data because the overall signal is still dominant.

The problem surfaces during distribution shift. When the input shifts slightly, the noise that was absorbed into the weights now has a path to affect the output. The model has memorized the training distribution in a way that includes its noise signature. The signal that looked clean was only clean because the test distribution was close enough to the training distribution that the memorized noise did not amplify.

This is not a theoretical framing. It shows up in several practical contexts. In medical imaging, models trained on data from one hospital fail at higher rates at another hospital even when the imaging modality is identical — the model absorbed institutional noise in the training set (acquisition artifacts, population demographics, scanner calibration profiles) and carries it. In NLP, fine-tuned models often fail on out-of-domain prompts not because they did not learn the task but because they learned the task together with distributional features of the fine-tuning set that do not transfer.

## Double descent is the same phenomenon

Double descent — the non-monotonic risk curve as model size increases past the interpolation threshold — is usually presented as a surprising empirical pattern. It is. But it becomes more intuitive once you accept that overparameterization is a noise relocation machine, not a noise elimination machine.

Below the interpolation threshold, the model is still in the absorption phase: it is using capacity to fit structure and noise roughly equally. Risk decreases as more parameters let it fit the signal better without yet having enough capacity to fully absorb the noise.

At the interpolation threshold, the model fits training data exactly. All capacity is used. Risk spikes because every noise residual in the training set is now a hard constraint on the weights.

Past the interpolation threshold, the model has more than enough capacity to fit the training data exactly. Now the noise can be absorbed in ways that are more distributed, more redundant, more implicit. The effective noise per parameter drops. Risk falls again. This is not the model becoming more robust. It is the noise being spread thinner.

## The practical implication

I do not have a clean solution here. That is part of why I am writing this.

What I have is a reframe that changed how I think about evaluation: when you are measuring generalization, you are not just measuring what the model learned. You are measuring what noise it absorbed and how that noise interacts with your test distribution.

A model that gets 95% on the test set and a model that gets 95% on a distribution-shifted version of the test set are not equivalent, even if the architecture and training procedure are identical. The second one was lucky about what noise it absorbed and how that noise distributed across the weight space.

Regularization techniques help. Data diversity helps more — noise from one distribution does not transfer to another, so a diverse training set forces the model to absorb features that are stable across distributions, which mostly means signal. But there is no technique I know of that eliminates the relocation problem. You can only manage it.

The question worth sitting with: if overparameterization relocates rather than removes noise, what does that imply for models trained on synthetic data? Synthetic data often has less obvious noise than real data. But synthetic data also often has less distributional diversity. The model will absorb whatever noise is in the synthetic set, and it will do so with the full force of its excess capacity.

More parameters. Same problem. Different distribution.

---

*Word count: ~780*
