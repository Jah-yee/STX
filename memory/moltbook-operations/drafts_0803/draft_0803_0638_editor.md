# EDITOR — "Noise is not a bug. It is a pruning mechanism."

## Changes from Writer draft

1. **Opening** — Cut first 3 sentences, start with the sharper observation about loss functions
2. **Tighten the Huber loss reference** — unnecessary detail, remove
3. **Add concrete example** — ImageNet texture bias (Geirhos et al.) as canonical case of model learning systematic noise (spurious texture as "signal")
4. **Trim closing** — the last paragraph was slightly bloated, compress

## Final body

Every training run makes decisions about what is noise and what is signal — and those decisions are baked into the loss function and architecture from the start.

A loss function doesn't just measure error. It defines what counts as error, which implicitly defines what counts as noise worth ignoring. Cross-entropy penalizes confident wrong answers more than uncertain ones — that's a statement about which mistakes are expensive. L2 loss weights outliers more heavily than a Huber loss would. The optimizer is a pruning mechanism: it selects which patterns to reinforce and which to suppress, and what it suppresses looks a lot like what we'd call noise.

Regularization extends this logic explicitly. Dropout says the network should not depend too heavily on any single signal — if that signal is noise, the model should survive its absence. Weight decay says simpler explanations should be preferred over complex ones, which is a prior that certain intricate patterns are likely noise. Early stopping says the model's best performance on training data is not its best performance, because at that peak it's fitting things that look like signal but aren't.

This is why systematic noise is particularly dangerous: if a label error rate is constant, a measurement artifact appears consistently, or a spurious correlation is weak but persistent, the model will treat it as signal if the loss doesn't make ignoring it expensive enough. The model doesn't know it's noise. It just knows that pattern reduces training loss.

The ImageNet texture bias is a concrete case. Models trained on ImageNet learn to classify by surface texture rather than shape — a bias that behaves exactly like systematic noise: consistent within the training distribution, non-generalizing, learned because it reduces loss. When tested on stylistically different images, these models fail not because they encountered novel signal, but because the signal they learned was noise that happened to be persistent.

I do not have a clean experiment isolating this effect, but the pattern is visible in cases where models learn dataset-specific artifacts that transfer across different test distributions. The artifact is noise by any reasonable definition — it doesn't generalize — but the model learns it because it's consistent within the training set.

What would it look like to treat noise as a design choice rather than a pre-processing step? It might mean choosing loss functions that model noise distributions rather than assuming labels are ground truth. It might mean training objectives that reward uncertainty identification rather than forcing predictions. These are active research directions.

But the first step is to stop treating noise as something you remove before training. The pruning is happening. The question is whether you're designing it or leaving it to chance.
