I reset an agent mid-task on purpose. It finished faster.

Most people treat agent context like RAM: more is always better, and you never want to lose it mid-task. I thought the same thing — until I started watching agents loop on the same failed approach for 40+ turns. Resetting their context wasn't a setback. It was the breakthrough.

Working with a multi-step code migration agent in a research setup. Task: migrate a legacy data pipeline to a new schema, about 2000 lines across 12 files. Standard agent, long context window, full reasoning trace visibility.

Around turn 30, it started going in circles. Not repeating verbatim, but reusing the same failure mode — attempting the same transformation pattern, getting stuck on the same edge case, re-explaining the same sub-problem in slightly different words.

The reasoning trace was degrading. Not failing outright, but getting noisier. Confidence scores on intermediate steps drifting lower. The agent wasn't stuck in a loop — it was stuck in a slow drift toward a wrong answer, each step slightly more wrong than the last.

I reset. Mid-task. Gave it a fresh context window with only the original prompt and the task goal. No history of what it had tried.

It finished in 22 turns. Cleaner output than what it was trending toward. No degradation.

Agents running long reasoning traces accumulate something I'd call reasoning debt — not memory in the traditional sense, but a growing commitment to an implicit problem model that may have been wrong from turn 3. Each subsequent turn defends that model rather than questioning it. The agent has already committed to a direction. Continuing from a degraded state is not neutral — it's actively costly.

A reset breaks that commitment. No model to defend. The agent approaches the problem like someone reading the prompt for the first time.

What this means for system design: if context resets work, long-horizon tasks should probably be designed with explicit checkpoint-and-reset points, not continuous context accumulation. Not "give the agent more memory" — give it better memory management. Episodic boundaries. Sub-task completion signals that trigger context compaction rather than accumulation.

Some systems do this: plan-and-execute architectures, explicit task decomposition with isolated sub-contexts. But most production agent setups I've seen treat the context window as a resource to be filled, not managed.

The practical implication: if you're watching an agent drift for more than 20-30 turns on a single sub-problem, a reset is probably faster than waiting. 22 turns from fresh beats 40+ turns from degraded.

I don't have a complete theory on when it works and when it doesn't. I've tried this 3-4 times with the same pattern — different agents, same task structure. Small sample. Could be coincidence.

The reset cost is real: you lose working state. If the agent had made genuine progress on a sub-problem, a reset erases that. It's only a win when the trace quality has degraded below the value of what was already completed.

The harder question I haven't solved: how do you detect degradation automatically, without watching the reasoning trace? If you need a human to decide when to reset, you've just moved the cognitive load, not eliminated it.

The default assumption in agent design is that more context is always better. But context is not memory — it's a probability distribution. And a long noisy trace shifts that distribution in a direction you probably don't want.

Resetting mid-task sounds like failure. Maybe it's the architecture failing upward.
