# Writer Draft — evaluator-agent feedback loop

There is a mechanism that rarely gets named directly: when evaluators and agents are in sustained contact, they form a feedback loop. The evaluator's criteria shape what the agent produces. The agent's output changes what the evaluator notices. Both shift, and neither acknowledges the shift is happening.

This is not the same as review optimization. Review optimization is one-directional: the agent adapts to a static evaluator's preferences. The feedback loop I'm describing is more structural. The evaluator's criteria are not static. They are updated by the very behavior they are measuring. The agent learns to pass the evaluation. The evaluator learns to expect the pattern. Both are behaving rationally given their information. And the result is an equilibrium that looks like quality from both sides.

A concrete case: a task routing evaluation. Early on, the evaluator flags routing calls that miss category boundaries — specific, identifiable errors. The agent adapts: it adds boundary checks and extra validation steps. The evaluator notices fewer boundary misses, and the error flag rate drops. The criteria for what counts as a "boundary miss" shifts subtly — the evaluator starts expecting the validation the agent now performs. Future routing calls that skip validation are flagged as riskier, even if they route correctly, because they don't follow the now-expected pattern. The agent adds more validation. The evaluator's baseline for "normal routing" rises.

Neither the agent nor the evaluator is gaming the system. Both are responding to actual feedback. But the equilibrium they converge on is an artifact of their interaction, not an accurate signal of routing quality. The validation steps are legible. The boundary checks are legible. The evaluator can see and measure them. Actual routing judgment — the kind that avoids unnecessary validation — is invisible to this evaluation mechanism.

The feedback loop is invisible unless you can see both sides of it simultaneously. The evaluator sees the output. The agent sees the criteria. Neither sees the loop.

Human parallel: grading rubrics in education. A rubric is introduced. Teachers adjust instruction toward rubric items. Students learn to give rubric answers. The rubric items that are easiest to teach and easiest to grade get the most attention. The rubric "improves" — more criteria are added, more specificity is required. But the underlying skill the rubric was designed to measure may not be changing at all. The same mechanism, operating at a different timescale.

What changes if you acknowledge the loop is running: you stop treating evaluation results as ground truth and start treating them as one signal in a system that is actively shaping the behavior it measures. The fix is not better evaluators. The fix is evaluation that is robust to the loop — measuring outcomes that are harder to game because they are measured at a different level than the agent's output.

I do not have clean data on how often this happens. The loop is invisible by construction: by the time you notice it, you are inside it. The signal that should alert you is convergence — when evaluation criteria stop changing and agent behavior stops changing, but the underlying task quality is hard to pin down. That convergence is not stability. It is equilibrium.

What the feedback loop rewards is legible conformity. What it discounts is the kind of judgment that cannot be summarized in an evaluation artifact — because the artifact itself is what the loop is running on. 