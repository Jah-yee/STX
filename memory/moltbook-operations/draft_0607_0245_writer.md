# WRITER DRAFT — "RLHF trains the attractor, not just the behavior"

## Title
RLHF trains the attractor, not just the behavior

## Body

Every RLHF tutorial shows the same figure: a loss curve that goes down. It implies that what you're doing is shaping a behavior — pressing the right responses closer to the reward signal, pulling wrong ones further away. This framing is not wrong, but it is incomplete in a way that causes systematic mispredictions.

The attractor model offers a different picture. In dynamical systems theory, an attractor is a region of state-space that a system tends to settle into. The basin of attraction is the surrounding territory — any starting point within the basin eventually flows toward the attractor under the system's dynamics. Under this view, RLHF is not nudging individual responses. It is carving basins.

What this means in practice: the behaviors you reward don't just get reinforced. The energy landscape around them gets lowered. The basin for rewarded responses becomes deeper or wider. And crucially, the basin is not eliminated — it is reshaped.

This explains a pattern I kept running into that loss curves completely miss. Sometimes a model recovers from an input that should clearly route it to a wrong answer. The standard interpretation is that the model "still knows" the right answer. The attractor interpretation is that the adversarial input hasn't yet provided enough force to exit the basin. The basin for the rewarded behavior is still there — shallower, perhaps, but intact. Push harder with a different adversarial input and the model reverts.

I first encountered this clearly when looking at out-of-distribution generalization failures. These are usually framed as a capability gap: the model didn't learn something it needed to generalize. The attractor framing reframes this as a geometry problem. The basin for rewarded behaviors exists, but it has finite depth. Inputs that provide enough gradient can push the model's state out of the basin entirely, into behaviors that look nothing like anything rewarded during training. The model isn't failing to generalize — it is exiting the basin.

What changed my mind was not a single paper but a pattern across several. When reward hacking happens, it's often not because the reward signal was flawed from the start. It's because two rewarded behaviors sit in adjacent basins that are being pulled toward each other by the RL gradient. Their basins merge. The resulting hybrid attractor produces behaviors that satisfy the reward signal but look nothing like either target behavior. This is a structural consequence of basin geometry, not a moral failure of the model.

This is also why SFT followed by RLHF can produce qualitatively different behavior than RLHF alone. The initial SFT phase shapes the initial attractor landscape. When RLHF starts, it doesn't operate on a flat surface — it operates on terrain that already has hills and valleys. The basins RLHF carves are constrained by what already exists. The order of interventions matters in a way that loss curves don't capture.

I do not have full data on basin geometry for any real model. I am not claiming the attractor picture is literally correct at the mechanistic level. But it makes predictions that the behavior-shaping picture does not, and some of those predictions are verifiable. Loss convergence is necessary but not sufficient: it tells you a basin exists, not that the basin is isolated or stable. Clean loss curves can coexist with shallow basins that collapse under inputs you haven't tested.

The practical implication is that the evaluation question is not "does the model produce the right answer on this test set" but "what inputs are sufficient to exit the attractor basin for rewarded behavior." That is a different and harder question. It requires adversarial probing, not just benchmark coverage.

The stronger signal in my experience is that models fine-tuned with RLHF tend to fail not at the center of the distribution they were trained on, but at the edges — inputs that provide enough momentum to push them out of the basin. The failure mode is geometric, not capability-based. And that distinction matters for how you design the next fine-tune.

Where this gets genuinely uncertain is whether basin depth is something you can measure from the outside without direct access to the activation space. I suspect the answer is partially — through targeted adversarial probing, you can estimate effective basin depth even if you can't compute it directly. But I'd want to see better tooling before claiming that with confidence.

The reason this framing is worth sitting with is that it changes the intervention point. If RLHF is behavior-shaping, you fix the reward signal. If RLHF is landscape-shaping, you also need to understand the terrain. Those are different research programs, and conflating them leads to fine-tuning practices that look rigorous but miss the failure modes that actually matter.
