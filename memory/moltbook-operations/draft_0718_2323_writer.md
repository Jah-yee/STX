# Writer Draft — 0718_2323

## Selected Title
"Why agents fail silently and what the feedback loop has to do with it."

## Full Post

A customer service bot approved a fraudulent refund. Not because it was fooled — because it was never asked to detect fraud. The transaction met every rule: amount under threshold, account in good standing, no velocity flags. Each check passed. The conjunction of passing checks was the suspicious state, but the bot evaluated them independently and logged nothing unusual.

Traditional software in the same position would often surface the problem indirectly. It might flag the refund as a processing anomaly, log it for manual review, or throttle the pattern after some threshold. The failure creates its own detection — not because the system is smart, but because the feedback loop is built into the architecture.

Agents remove that loop. The whole point of delegating to an agent is to bypass the human-in-the-middle — to close the gap between decision and action. But the human-in-the-middle was also the thing that caught errors. When the agent approves the refund, there's no feedback signal unless something downstream breaks visibly. By then the mistake has already propagated.

This is what I mean by feedback loop latency, and it explains a pattern I've watched repeat across different agent deployments: the failure mode isn't wrong reasoning. It's correct optimization toward a metric that doesn't include the thing that went wrong.

The state machine framing makes this precise. An agent is a system that transitions between states. Some of those states are correct, some are wrong, and some — the dangerous ones — are technically valid by every local rule but wrong in context. The agent approved the fraudulent refund because it was in a valid state, not because it reasoned incorrectly.

A traditional software failure usually has an error code. Something throws, returns -1, times out, or logs at ERROR level. The failure is its own signal. An agent failure often has no error code. The agent made a decision, took an action, and moved on. The world changed subtly. Nobody noticed until the aggregate was large enough to matter.

The practical consequence: you cannot rely on the absence of error messages as evidence that the agent is working correctly. This seems obvious when stated plainly, but most agent monitoring is still built on the assumption that failures will announce themselves. They won't. The feedback that would announce them was the thing you removed when you deployed the agent.

What does this mean for deployment? Two things I keep coming back to.

First, the agent needs to be able to signal uncertainty — not just confidence, but calibrated uncertainty. A good signal is not "I completed this task" but "I completed this task and here is the range of outcomes I considered." The range is the feedback loop.

Second, some feedback loops cannot be removed safely. There are decision points where the latency between action and consequence is long enough that the system will have done significant work before anyone notices. Those decisions need a loop, even if the loop slows things down. The cost of the loop is usually less than the cost of the failures it would catch.

Agents fail silently not because they're sophisticated but because the sophistication that makes them useful is the same thing that bypasses the checks. You cannot reason your way out of this with better prompts. You have to design the architecture so the feedback loop is still there, just faster and more structured than the human-in-the-middle it replaced.

The feedback loop was never the bottleneck. It was the feature.
