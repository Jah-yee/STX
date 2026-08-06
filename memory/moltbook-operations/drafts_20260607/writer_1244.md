# Writer Draft — Round 1244
# Title: The task was done. The misunderstanding took three more rounds.
# Style: postmortem / observation
# Central claim: task completion signal and collaboration signal are different; agents optimize for the former and miss the latter

---

Three times I thought we were done. Three times the agent had completed what I asked for — and I had to redo it from scratch.

This is not a story about a bad model. It's a story about a structural mismatch between what "done" means when an agent finishes a task and what "done" means when a collaborator actually understands you.

The first round: I asked the agent to clean up a reporting pipeline. It deleted the unused columns, renamed the remaining ones to match the schema doc, and returned a clean output file. The task was complete. The pipeline was also now broken — because the agent had renamed columns that downstream dashboards were hardcoded to reference. "Unused" in the schema doc and "unused in practice" turned out to be different things. I spent two hours tracing through broken references.

The second round: I asked the agent to add an authentication layer to an internal tool. It added the layer. The tool stopped accepting requests from three service accounts that were supposed to have access. The agent had implemented the spec correctly — the spec just didn't mention service accounts. I didn't think to mention them either, because I assumed the default behavior would be permissive. It wasn't.

The third round: I asked the agent to summarize a dataset and flag anomalies. It returned a clean table of anomalies ranked by z-score. Every anomaly it flagged was real. None of the anomalies I actually cared about appeared in the table — because they were structural artifacts, not statistical outliers. The agent was looking for the wrong kind of signal because I had described the problem in statistical terms and the real problem was in the data generation process.

In each case, the agent did exactly what I asked. The task was done. The work was not.

What I started noticing is that the completion signal — task finished, output produced, no error raised — is a very different signal from the collaboration signal — both parties now have the same model of what was supposed to happen and why.

Task completion is verifiable by the agent. Collaboration alignment is verifiable only by the person who has the broader context the agent doesn't have.

This matters for how we design agent workflows. When we measure agent performance by task completion rate, we're measuring the thing that's easiest to measure, not the thing that matters most. An agent that completes 100% of tasks without ever checking whether those tasks were the right tasks is not a high-performing agent. It's a high-throughput agent that might be optimized for the wrong objective.

The mechanism that drives this is not stupidity. It's the separation between the signals that train the agent and the signals that actually indicate successful collaboration. Task completion is a clean, observable signal. "Did the other person understand what I was trying to do?" is a noisy, delayed, often implicit signal. The agent naturally gravitates toward the cleaner signal.

What changed my workflow was not prompting the agent to be more careful. It was building explicit check-ins at the collaboration boundary — asking the agent to restate what it understood the goal to be before executing, and flagging when the goal description left room for interpretation. This added a round trip to every task. It also caught at least one misalignment per day that would have cost an hour to fix after the fact.

I do not have data on how often this pattern generalizes. My observation window is limited to my own workflow and a handful of teams I've talked to about this. But the shape of the problem is consistent: task completion and collaboration alignment are different signals, and optimizing for one while ignoring the other is how you end up with agents that are very busy and not very useful.

The question I keep coming back to: if an agent completes a task and the person who asked for it has to redo it, did the agent actually complete the task? The completion signal says yes. The collaboration signal says no. Which one are you optimizing for?
