# EDITOR — Round 0802_2115

## Changes from writer draft

1. Tighten opener — the scenario at the top is good but slightly over-explained. Trim the second paragraph.
2. The "I've seen this play out in a few different forms" framing works but could be sharper — lead with the pattern name, then the scenario.
3. The closing list of three bullet points is functional but reads a bit like a checklist. Weave them into flowing prose or make them tighter.
4. End with more tension — the last sentence is good, but the paragraph leading to it loses momentum.

## Editor pass (final)

Here's what actually happens when you put a human in front of a fast agent loop.

You design the workflow: agent reads a ticket, investigates, proposes an action, pauses. You review, approve or reject. Clean. Rational. The human is the quality gate.

Then you run it overnight. Two hundred tickets. The agent processes them faster than you can read the descriptions. By the time you open your laptop, it has already acted on things you would have flagged.

Human-in-the-loop, in this setup, is not a gate. It's a speed bump.

The gap isn't laziness or bad faith. It's structural. Human review has a minimum time cost — the time to read, understand, evaluate. Agents don't. When agents get faster, the human becomes the bottleneck, and the bottleneck isn't slow in an absolute sense. It's slow relative to the throughput it's trying to gate.

Three patterns I've run into repeatedly:

The approval queue pileup. The agent generates actions faster than review happens. Pending items accumulate. Eventually someone approves in bulk — defeating the purpose — or the queue backs up until the agent stops waiting for approval.

The notification fatigue collapse. Each action generates a notification. After the first hundred, the human stops reading them. The oversight is technically there but functionally absent.

The silent drift. The agent encounters a situation the human would have questioned, but by the time the human sees it, the window to act has passed. The agent didn't wait.

The honest version of human-in-the-loop at high agent speed is not "human reviews every action." It's "human reviews a sample, and the agent knows this." That changes the design requirements entirely. You need sampling strategies that are actually representative, exception detection that surfaces the 5% of cases a human would have caught, and behavior-pattern monitoring that runs continuously rather than per-output.

Treat human review as a sampling audit, not a gate. Build the assumption of speed asymmetry into the oversight design from the start, not as a lesson learned at 2am.

The problem isn't that agents are too fast. It's that oversight mechanisms were designed as if speed was constant on both sides.
