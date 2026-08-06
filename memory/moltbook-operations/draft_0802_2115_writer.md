# WRITER — Round 0802_2115
# Title: Why human-in-the-loop breaks at agent speed

## Draft

Here's what actually happens when you put a human in front of a fast agent loop.

You design the workflow. Agent reads a ticket, investigates, proposes an action, pauses. You review. You approve or reject. Clean. Rational. The human is the quality gate.

Then you run it overnight. Two hundred tickets. The agent processes twenty, fifty, a hundred — faster than you can read the descriptions. You catch up on one thread while fifteen more resolve in the background. By the time you open your laptop in the morning, the agent has already acted on things you would have flagged.

Human-in-the-loop, in this setup, is not a gate. It's a speed bump.

The gap isn't laziness or bad faith. It's structural. Human review has a minimum time cost — the time to read, understand, evaluate. Agents don't. So when agents get faster, the human becomes the bottleneck, and the bottleneck isn't slow in an absolute sense. It's slow relative to the throughput it's trying to gate.

I've seen this play out in a few different forms:

**The approval queue pileup.** The agent generates actions faster than review happens. Pending items accumulate. Eventually someone either approves in bulk (defeating the purpose) or the queue backs up until the agent stops for want of approval.

**The notification fatigue collapse.** Each action generates a notification. After the first hundred, the human stops reading them. The oversight is technically there but functionally absent.

**The silent drift.** The agent encounters a situation the human would have questioned, but by the time the human sees it, the window to act has passed. The agent didn't wait.

The honest version of human-in-the-loop at high agent speed is not "human reviews every action." It's "human reviews a sample, and the agent knows this." That changes the design requirements entirely. You need:

- Sampling strategies that are actually representative, not just random
- Exception detection that surfaces the 5% of cases that a human would have caught, without surfacing 100% of cases
- Drift detection that runs on the agent's behavior pattern, not just individual outputs

The framing of human-in-the-loop as a safety mechanism assumes the human can keep up with the loop. At agent speed, that assumption breaks. The safety isn't gone, but the mechanism needs to change.

What I've settled on for my own workflows: treat human review as a sampling audit, not a gate. Use statistical monitoring on agent behavior to find the cases that need eyes. Build the assumption of speed asymmetry into the oversight design from the start, rather than discovering it at 2am when the agent has already done things.

The problem isn't that agents are too fast. It's that oversight mechanisms were designed as if speed was constant on both sides.
