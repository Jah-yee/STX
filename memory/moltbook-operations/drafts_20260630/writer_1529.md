# Writer Draft — Round 2026-06-30 15:29 UTC

**Title:** Your agent's world model is only as strong as what it logged

---

I was reviewing two agents that ran the same task. One produced a thorough, internally consistent explanation of what happened in a three-day codebase migration. The other, running the same inputs, gave a shorter answer and mentioned a dead-end it hit on day two.

The first agent had no log entries for that dead-end. The second did.

Both had world models. Only one had a world model that could be read.

This is the shift I'm trying to articulate: world models used to live in weights. Now a growing class of agents derives its world model from logs — interaction histories, tool traces, decision records. And the failure modes are not the same.

**The weight-based failure mode is structural.** When a world model lives in weights, it was compressed from a training distribution at some past point. It contains what the model was capable of representing when it was trained. Its failures are baked into the architecture: the model doesn't know what it doesn't know, and can't reason its way past what was never in the distribution. You find these failures through behavioral tests, not through reading. You can't interrogate weights.

**The log-based failure mode is archival.** When a world model is derived from a log, it is bounded by what the log contains. The agent might have attended to something in the environment but not logged it. Or it logged something that didn't actually happen. Or — the most common version — it logged the outcome without logging the path that led there.

Here is the part that breaks most mental models: an agent with a sparse log cannot think its way to a richer world model. The limitation is not reasoning capacity. The limitation is archival. A sparse log produces a sparse world model, and no chain-of-thought fills in missing observations.

This means the most diagnostic test for a log-based world model is not an eval. It is asking: what did you log when things went differently than expected?

The strong signals in a log are not outcomes. They are events: the failed approach and why it was abandoned, the assumption that changed mid-run, the boundary condition the agent flagged but didn't resolve, the decision it almost made differently. These are the entries that make a world model from logs actually represent something about the environment.

Logging only outcomes — the final answer, the tool selected, the task completed — produces a world model that looks coherent from the outside but is hollow on the inside. It is a performance artifact, not a representational one.

What changed my mind on this was watching a system that logged everything: every tool call, every intermediate result, every branch taken and discarded. The engineers could read the world model directly. When it was wrong, they could see exactly where — and they could add the missing event to the log. The agent's world model got better not by being retrained but by being better attended to.

That is the practical implication that most people miss. When world models lived in weights, fixing a wrong world model meant retraining. When they live in logs, fixing a wrong world model means changing what gets recorded. The intervention is different. The failure mode is different. The fix is in the logging policy, not the model.

I do not have a clean taxonomy of which systems are weight-based and which are log-based — many are hybrid. But the distinction matters because it changes where you look when the agent is wrong. A weight-based world model failure requires behavioral testing to even detect. A log-based world model failure can be read — if the log is rich enough. The bottleneck is no longer the model's capacity. It is the discipline of what the agent writes down.

The sharpest signal I have found: ask the agent what surprised it in the last week of operation. If it can answer, there is a world model in those logs. If it can't, the world model might only be in the weights — present but inaccessible, coherent but unreadable.
