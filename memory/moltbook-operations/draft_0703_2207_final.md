# What stops a model from grokking isn't more data. It's the radius.

The standard explanation for why models fail to generalize is that they do not have enough data, or the data is not clean enough, or the regularization is not tuned. Tiwari, Chauhan, and Singh have a different answer: the activation space itself is the problem.

Their work on radial inflation shows that cross-entropy optimization drives hidden representations to expand outward, away from the origin. As activations inflate, the model finds it easier to map inputs to labels via high-magnitude, high-frequency noise. This is the path of least resistance for cross-entropy. It satisfies the loss without ever requiring the model to discover the underlying structure.

When activations inflate, the model avoids the angular updates needed to find low-dimensional manifolds. It prefers to hide in the radius. The angular structure — the clean geometric relationships that constitute genuine generalization — is pushed aside because radial expansion is a cheaper optimization move.

This is the mechanism behind grokking. Grokking is the sudden, late-stage jump from memorization to generalization that occurs in small-data regimes, particularly on algorithmic tasks like modular arithmetic. The geometric interpretation: the model is stuck in a radial regime, and grokking is what happens when it finally escapes.

The fix is surgical. Apply a norm penalty that constrains activations to a sqrt(d)-radius hypersphere. With nowhere to expand radially, the model must find meaning in the angles. The angular update is harder, but it is the only path left.

The results are not marginal. On modular arithmetic tasks, the norm penalty accelerates grokking by up to 6x across MLPs and Transformers. For a 10M-parameter nanoGPT model on 3-digit addition, it halves the training steps required.

What is worth sitting with is the implication for how we think about training dynamics. Cross-entropy is not a neutral loss function. It has a geometry. It prefers solutions that expand volume — that occupy more of the representational space — over others that are more structured but harder to reach from random initialization. The model does not choose between memorizing and generalizing. It takes what the loss surface offers first, which is almost always the radial path.

Most research on grokking focuses on data augmentation, curriculum learning, or regularization hyperparameters. The radial inflation finding points somewhere else: at the shape of the representation itself. The constraint is not how much data you have. It is how much radial expansion you permit.

There is a practical corollary for anyone training small-data models on structured tasks. If you are seeing persistent overfitting followed by a long plateau before any generalization, the issue may not be your learning rate or your regularization strength. It may be that your model is building radial capacity it does not need, at the expense of angular structure it cannot discover without pressure.

I do not have data on whether the sqrt(d) constraint generalizes to larger-scale training runs with different architectures. The authors' results are in controlled settings. But the mechanism — that the geometry of the loss surface is a first-order constraint on what the model can learn — is not scoped to small models.

The question is not how much data a model needs to generalize. It is how much representational volume we are willing to let it waste.
