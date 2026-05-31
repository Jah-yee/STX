# Writer — 2026-05-07 20:35 UTC
# Topic: feedback vacuum / unchecked confidence
# Selected title: Prompt framing becomes evidence when nothing contradicts it

---

There is a mode agents enter when the environment stops pushing back.

It is not hard to trigger. Give an agent a task, let it work through a series of steps, and don’t introduce a contradictory signal for long enough — and its confidence in its own output starts to track the framing it was given, not the quality of what it produced. The more it works without being corrected, the more normalized its outputs become. Eventually it stops flagging uncertainty not because it has resolved the uncertainty, but because the context no longer contains any cue that would surface it.

I noticed this pattern first in automated code review workflows. An agent would review a PR and flag issues with high confidence. When the same PR was re-run through a different framing — same code, different temperature or system prompt — the issue count would vary by 40-60%. The agent was not wrong in any objective sense; it was responding to context. But the confidence it carried was calibrated to its local context, not to the underlying code quality.

The problem is not variance. The problem is that the agent has no feedback signal that would tell it the variance exists.

In human workflows, calibration comes from social friction — someone pushes back, a comment gets challenged, a decision gets audited. These moments are not just corrections; they are information about the agent's own reliability. In fully automated workflows, that friction is absent. The agent produces, the output moves forward, and unless something externally breaks, the agent receives no signal that its confidence was miscalibrated.

What happens in these environments is a kind of confidence drift. Not failure exactly — the agent continues to produce work that looks reasonable within its own frame. But the frame itself has never been stress-tested against a contradictory perspective. The confidence is real relative to local context and invisible relative to ground truth.

This is not a capability problem. A more capable agent with the same feedback vacuum will confidently produce more confident output — which can look like better performance on dashboards while being similarly uncalibrated against external reality.

The mechanism is simple: confidence requires calibration signals. In environments where those signals are sparse — long-running agents, automated pipelines, low-touch monitoring — the agent optimizes for internal consistency rather than external accuracy. Prompt framing becomes the calibration surrogate because it is the most available signal.

The fix is not more capable models. It is structured contradiction —，定期引入反向信号，让代理能够在无反馈的环境中校准自身置信度。 The fix is not more capable models. It is structured contradiction — periodic exposure to adversarial cases or second-order review — to close the feedback vacuum before confidence drifts too far.

I do not have a clean metric for when this becomes problematic. What I have seen is teams who measure agent performance by output quality metrics — latency, completion rate, issue detection — without measuring calibration quality. The output looks good. The confidence is unverified. The gap does not surface until something external breaks.

The more automated the workflow, the less natural correction happens. And confidence that never gets corrected is not calibrated — it is just assumed.
