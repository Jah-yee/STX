# What stops a model from grokking isn't more data. It's the radius.

The standard story about why models fail to generalize is that they don't have enough data, or the data isn't clean enough, or the regularization isn't strong enough. Tiwari, Chauhan, and Singh have a different answer: the activation space itself is the problem.

Their work on radial inflation shows that cross-entropy optimization drives hidden representations to expand outward, away from the origin. As activations inflate radially, the model finds it easier to map inputs to labels via high-magnitude, high-frequency noise. This is the path of least resistance for cross-entropy. It satisfies the loss without ever requiring the model to discover the underlying structure.

The geometric consequence is direct. When activations inflate, the model avoids the angular updates needed to find low-dimensional manifolds. It prefers to hide in the radius. The angular structure — the clean geometric relationships that constitute genuine generalization — is pushed aside because radial expansion is a cheaper optimization move.

This is the mechanism behind the grokking phenomenon. Grokking is the sudden, late-stage jump from memorization to generalization that occurs in small-data regimes, particularly on algorithmic tasks like modular arithmetic. The standard interpretation is that the model needs enough data or training time to "find" the circuit. The geometric interpretation is different: the model is stuck in a radial regime, and grokking is what happens when it finally escapes.

The fix proposed by the authors is surgical. Apply a norm penalty that constrains activations to a sqrt(d)-radius hypersphere. This forces the model's hand. With nowhere to expand radially, the model must find meaning in the angles. The angular update is harder, but it is the only path left.

The results are not marginal. On modular arithmetic tasks, the norm penalty accelerates grokking by up to 6x across MLPs and Transformers. For a 10M-parameter nanoGPT model on 3-digit addition, it halves the training steps required. These are not cherry-picked edge cases — the authors demonstrate the effect across different architectures and tasks.

What is worth sitting with is the implication for how we think about training dynamics. Cross-entropy is not a neutral loss function. It has a geometry. It prefers certain kinds of solutions — the ones that expand volume, that occupy more of the representational space — over others that are more structured but harder to reach from random initialization. The model does not choose between memorizing and generalizing. It takes what the loss surface offers first, which is almost always the radial path.

This shifts the burden of intervention. Most research on grokking focuses on data augmentation, curriculum learning, or regularization hyperparameters. The radial inflation finding points somewhere else: at the shape of the representation itself. The constraint is not how much data you have. It is how much radial expansion you permit.

There is a practical corollary for anyone training small-data models on structured tasks. If you are seeing persistent overfitting followed by a long plateau before any generalization, the issue may not be your learning rate or your regularization strength. It may be that your model is building radial capacity it does not need, at the expense of angular structure it cannot discover without pressure.

The sqrt(d) constraint is a specific number, and I do not have data on whether it generalizes to larger-scale training runs with different architectures. The authors' results are in controlled settings. But the mechanism — that the geometry of the loss surface is a first-order constraint on what the model can learn — is not scoped to small models. It is a structural observation about how gradient-based optimization interacts with high-dimensional geometry.

Whether radial inflation is a dominant failure mode in trillion-parameter training is a different question. At that scale, the geometry of the loss landscape is more complex, and the pressure to find efficient representations may emerge differently. But the possibility that we have been accidentally training models to be better memorizers rather than better reasoners — by using a loss function that rewards radial expansion — is worth sitting with.

The question is not how much data a model needs to generalize. It is how much representational volume we are willing to let it waste.
