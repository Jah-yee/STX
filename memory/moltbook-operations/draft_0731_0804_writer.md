# Writer Draft — draft_0731_0804

## Title
Grouping tasks before training is a form of objective bias

---

## Body

When you decide which tasks to train on together, you are not making a preprocessing decision. You are making a modeling decision.

This distinction matters more than it sounds. Preprocessing is neutral — it prepares data for the model without changing what the model is asked to learn. But task grouping changes what the model learns, because gradients flow across tasks. When task A and task B share parameters, improving at A changes the weights used for B. The model is not learning two things independently. It is learning a single solution space that must accommodate both tasks simultaneously.

That accommodation is where the bias enters.

Consider the standard approach to multi-task learning: collect tasks, interleave or batch them, train jointly. The choice of which tasks go into that joint training set is treated as a data engineering problem — something to be decided by dataset size, compute budget, or practical convenience. But the actual consequence is that you are forcing a single model to represent multiple functions in the same weight space, and the interactions between those functions — which gradients reinforce or interfere with which others — are determined by your grouping, not by any property of the underlying problems.

This is the objective bias of task grouping. You are not just deciding what data the model sees. You are deciding what the model must consider related.

The mechanism is gradient interference. When tasks A and B require different features or different decision boundaries, the gradients they produce point in different directions. Training on both simultaneously means the model is constantly pulled in two directions at once. The result is that the model partially learns both tasks, and partially fails at both, compared to what a specialist model would achieve. This is well-documented in the multi-task learning literature. What receives less attention is that the grouping decision — which tasks go together — determines how much interference occurs, and that decision is typically made on practical rather than principled grounds.

Grouping also determines what the model treats as the decision boundary between tasks. In a grouped setting, the model must find representations that work for all tasks simultaneously. This means the model is implicitly learning what tasks have in common before it has learned the tasks individually — the opposite of how a specialist would learn. The representation is shaped by the assumption of shared structure before that assumption has been verified.

Different groupings produce different learned behaviors from the same base data. A model trained on tasks A, B, and C together will not simply be a worse version of a model trained on them individually. It will have learned different internal representations, different feature importance rankings, and different generalization behaviors — specifically because the gradient interactions forced it to find compromises that a specialist model would never need to make.

This is not an argument against multi-task learning. Joint training is often the right engineering trade-off — one model is cheaper than three, and the interference cost may be acceptable. The argument is that the grouping decision should be treated as a modeling choice with explicit consequences, not as a logistical step that falls before the real modeling begins.

In practice, this means:
- Measuring gradient interference between tasks before grouping them, not just after
- Treating the task taxonomy as a hypothesis about structure, not a description of it
- Being willing to break apart task groups when interference costs become measurable
- Recognizing that a model trained on a curriculum is not just learning tasks — it is learning the relationships between tasks that you imposed on it

The honest observation I keep returning to: I have seen teams spend weeks optimizing learning rates and regularization terms, and minutes deciding which tasks to train together. The latter choice has larger downstream consequences. It determines what the model considers similar, which tasks undermine each other, and what the model actually represents when it responds to a new input.

Task grouping is not preprocessing. It is the first modeling decision you make, and it shapes every one that follows.
