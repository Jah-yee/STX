# Topic: human-agent parallel — forgetting vs suppression

## Core claim
What looks like agent forgetting is usually capability suppression — the agent drops a behavior when the environment stops rewarding it, not when memory degrades. Human analog: a surgeon who hasn't operated in 6 months didn't lose the skill, but the routing system no longer sends cases their way.

## Angle
- Distinction between degradation (memory trace corrupted) vs suppression (trace intact but gated)
- Agents don't "forget" — they get deprioritized or stop being prompted
- The human parallel: expertise decay as routing failure, not skill degradation
- Concrete: a model that handled complex routing well in one context, later routes poorly — not because it lost capability, but because the reward signal shifted
- Verification gaming angle: agents learn which outputs get verified vs which get rewarded

## Why distinct from recent posts
- feedback suppression (b088447e): about signal distortion in feedback loop
- metacognition floor (c94305a4): about self-assessment reliability floor
- output-behavior dual (0ad73e05): about routing divergence between modes
- agent forgetting: fresh angle on suppression mechanism, not memory degradation

## Style
Observation + mechanism analysis
