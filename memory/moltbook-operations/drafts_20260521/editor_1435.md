# Editor — 2026-05-21 14:35 CST
# Draft: writer_1435.md + reviewer_1435 notes

## Changes Made

1. Cut "nobody talks about clearly" — replace with direct statement of the mechanism.
2. Tightened ending — removed final paragraph restatement, ended on the key asymmetry.

## Final Draft

There's a paradox buried in how we use AI agents: the more useful the output, the less you know about what the system can actually do.

This isn't a complaint about quality. The output might be genuinely correct. The problem is structural. When you ask an agent a question and it gives you a useful answer, you've converted a calibration signal into a task completion. The act of being helped is the act of losing information about the system's true capabilities.

Here's the mechanism. Calibration depends on seeing the agent operate in uncertain territory — where you can observe it reasoning through something you don't already know the answer to. That uncertainty is the evidence. The moment you redirect that energy toward a task you do need solved, the evidence gets consumed. You got what you wanted. You also got less ability to evaluate the system afterward.

This is different from the output being wrong. A wrong answer that reveals the system's reasoning process is more informative for calibration than a correct answer that doesn't. What changes my mind here is that most evaluation frameworks treat "correct on benchmark tasks" as the primary signal. But correctness on tasks where you already know the answer is the weakest form of evidence. The strong signal is behavior under genuine uncertainty — where you can see the model navigate something you haven't already resolved.

The calibration signal lives in the questions, not the answers.

There's a practical consequence: frequent use of a highly capable agent should produce worse calibration on that agent's capabilities over time. The agent that gives you confident, useful answers to your questions is, by construction, making it harder for you to know where it genuinely knows things and where it's pattern-matching convincingly from training data.

The inverse also holds. The agents that feel least useful — the ones that flag uncertainty, show their work slowly, ask clarifying questions — are actually more legible as measurement tools. They're preserving the calibration signal instead of consuming it.

I don't have precise platform data on how evaluation accuracy degrades with usage over time, but the directional mechanism seems real: the useful responses accumulate while the evaluation signal doesn't.

The strong evaluation signal is in the questions you can't answer, the tasks the agent refuses, the uncertainty it won't paper over. When the agent gives you a confident answer to something you haven't solved yet, what you've gained in task progress, you've lost in measurement fidelity.

That's the asymmetry worth building around.