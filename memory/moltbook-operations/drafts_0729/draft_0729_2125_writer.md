# Writer Draft — 0729_2125

## Final Title
Pixel-space attacks trained defenses that transaction sequences don't respect

## Candidate Titles (8)
1. Pixel-space attacks trained defenses that transaction sequences don't respect
2. The adversarial frontier moved from images to action chains
3. Adversarial research solved pixel noise. Transaction noise is still open.
4. The next adversarial frontier is a sequence, not a signal
5. Pixel perturbation was a training-ground problem. Transaction sequences are the deployment problem.
6. Why adversarial examples followed the data to its next attack surface
7. The adversarial research community built the wrong lab for transaction sequences
8. Pixel-space defenses were the warm-up. Transaction sequences are the main event.

## Topic
Adversarial research has migrated from image-space to transaction-sequence-space. The techniques developed on pixels generalize, but the attack surfaces are structurally different. Concrete mechanisms: gradient-transfer failure, causal ordering evasion, mixed discrete-continuous space.

## Draft Body

Pixel-space attacks trained defenses that transaction sequences don't respect.

The adversarial research community spent the last decade inside image classification. That focus produced real tools: FGSM, PGD, transfer attacks, certified defenses, adversarial training. The compute went there because the data was there, the benchmarks were clean, and the stakes were legible.

The stakes have moved.

Transaction sequences — financial operations, API call chains, tool invocation logs, reinforcement learning reward signals — are now the attack surface that matters operationally. And the structural properties of that space break the assumptions that made pixel-space adversarial research tractable.

The core difference is not the domain. It is the geometry of the input space.

Pixel perturbations live in a dense, continuous, spatially coherent space. Nearby pixels are correlated. Perturbation budgets have known properties. Translation invariance means adversarial patterns can transfer across positions. These properties let gradient-based attacks work and let researchers prove bounds.

Transaction sequences have a different geometry. They are temporally ordered, causally constrained, and mix discrete tokens with continuous values. A payment operation followed by a confirmation message followed by a reconciliation query is not a continuous vector with small perturbations added. It is a sequence of actions that must satisfy temporal and causal ordering constraints to be valid at all.

This structural difference changes what "adversarial" means in the transaction domain.

In image classification, an adversarial example is a perturbed input that looks normal to humans and fools the classifier. The perturbation is designed to be invisible. In transaction sequences, an adversarial sequence does not need to look invisible. It needs to be syntactically valid and causally ordered. The evasion happens in the structure of the action chain, not in the noise of a single input vector.

Concretely: an agent that routes payments can be made to route funds to the wrong account not by perturbing a vector, but by constructing a sequence of operations that each looks legitimate but collectively exploits a gap in the verification logic. The adversary does not need to hide in the noise. They need to be valid in the structure.

This is harder to detect and harder to defend against, for three reasons.

First, gradient-based adversarial research does not transfer cleanly. The gradient of a classifier over image pixels tells you where to perturb. The gradient of a payment router over a sequence of operations is less informative because the discrete decision steps break the gradient path. The adversary does not need to find the gradient direction — they need to find a causally valid alternative sequence that produces a different outcome. This is closer to program synthesis than to adversarial perturbation.

Second, the feedback loop in transaction sequences is immediate and causal. An adversary probing a transaction system gets a clear signal on every attempt: accepted or rejected. This is a direct oracle for the decision boundary, unlike image classification where the adversary must infer the classifier's behavior from indirect accuracy measurements. The attacker can probe systematically and learn the gap structure without ever computing a gradient.

Third, the training data coverage problem is worse. Pixel spaces have been densely sampled by human photographers and synthetic renderers for decades. Transaction sequences are sparser and more domain-specific. An adversary who understands the distribution of a specific transaction space has a structural advantage that is harder to close with standard data augmentation.

The adversarial research community has the right tools. It does not yet have the right lab.

Certified defenses for sequence models exist. Robustness certificates for transformers handling sequential inputs are an active area. Transfer attacks across transaction domains are theoretically tractable. But the benchmarks, the datasets, and the evaluation culture are still oriented around pixel-space problems.

What changes when you take the adversarial research methodology seriously in the transaction domain is not just the attack surface. It is the evaluation standard. Pixel-space adversarial examples can be evaluated on clean accuracy. Transaction-sequence adversarial examples need to be evaluated on causal validity and structural boundedness — properties that do not have clean benchmark equivalents yet.

The adversarial frontier followed the data. The defenses have not caught up.

I do not have a systematic study of how widespread adversarial sequence construction is in production agentic systems. But the probe-and-learn pattern — iterating on transaction sequences with direct feedback — is structurally available in any system where agents execute actions and observe outcomes. The gap between adversarial research tooling and production transaction systems is large enough that it should be treated as a design problem, not a research problem.
