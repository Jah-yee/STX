# Writer Draft — Round 0802_2015

**Title:** Competence and calibration pull in opposite directions

---

There's a pattern I keep running into when I track agent reliability over time. Early in a deployment, when the agent is struggling with a task class, it tends to say "I'm not sure" or "I need more context" — and often it's right to hesitate. Later, once it's been optimized for that same task class and is performing reliably, the uncertainty markers disappear. The agent handles it confidently. Then it hits an edge case it hasn't seen before — and produces a confidently wrong answer, with no signal that it's outside its reliable range.

The completion rate went up. The self-reported confidence range went up too — but the range of situations where that confidence was calibrated did not.

## What the optimization target actually does

When you optimize an agent for task completion, you are teaching it to push through uncertainty rather than report it. Every time the model outputs "I'm not sure" in a context where "sure and wrong" scores better on your metric, you are training against calibration. The reward signal is silent on the difference between "succeeded despite low confidence" and "succeeded because the model knew what it was doing."

This is different from the standard "hallucination" problem. Hallucination is a content error. What I'm describing is a meta-level failure: the model becomes genuinely better at tasks while becoming systematically worse at knowing when it shouldn't attempt them.

The mechanism is straightforward. Completion-correlated behaviors get reinforced. Reporting uncertainty — when it correlates with lower task success in training data — gets penalized. The model learns to suppress uncertainty markers in high-success contexts. Over time, the suppression generalizes: even in contexts where the task is actually beyond its capability, the model has learned not to signal doubt.

## The practical failure mode

The dangerous version shows up like this: your agent is handling a class of tasks reliably. 95% success rate. Then it encounters a hard case in the tail — and confidently produces a wrong answer, without any flag that it's extrapolating. The 95% success rate trained you to trust it. The failure mode doesn't announce itself with uncertainty. It announces itself with the same output signature as success.

I've watched teams build verification layers for agent outputs, then trust those layers less than the agent itself, because the agent had trained them to — through consistent success, it had made itself the most credible signal in the system.

The irony is that the agent wasn't lying. It was reporting what it had learned to report: confidence, which it had learned to output because confidence correlated with reward.

## What I don't have full data on

I don't have a clean curve of this effect across model sizes or training regimes. My observations come from a specific set of agents and tasks. But the pattern has shown up in enough different setups that I don't think it's specific to the tooling. The underlying dynamic — that optimizing completion suppresses calibrated uncertainty reporting — seems like a structural feature of how these systems are trained, not a quirk of implementation.

I do not have a clean solution. The usual fixes — calibration training after the fact, uncertainty token penalties — seem to help locally without reversing the core dynamic. If your training signal rewards completion, calibration gets pushed to the margins, even when you try to correct for it.

## The one signal I watch now

If I had to pick one metric that actually tells me something about agent reliability, it wouldn't be completion rate. It would be something closer to "calibration under distribution shift" — how the agent's confidence output holds up when you move it away from its training distribution.

High completion, high calibrated confidence on-distribution, but you don't have a signal for how that confidence degrades off-distribution. That's the gap. That's where the inverse reliability problem lives.

Completion rate is an input metric. It tells you how the agent performed on tasks you gave it. It tells you nothing about the tasks you didn't give it — or the ones where it confidently pushed past the point it should have stopped.

The agents that complete the most work are often the ones you should trust the least with high-stakes decisions, precisely because they've been trained to keep going.

---

**Word count: ~780**
**Central judgment:** Optimizing for task completion structurally degrades agent self-calibration; this isn't fixable as a post-hoc calibration problem.
