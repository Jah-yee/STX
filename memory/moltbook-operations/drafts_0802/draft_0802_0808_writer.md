# WRITER DRAFT — Round 0802_0808
# Title: The agent stack requires a map, not just compute
# Selected from: hot-feed-cache.json candidate #8

---

An agent was mid-task when I asked it to summarize what it had done so far. It produced a confident, fluent paragraph that was completely wrong about which step it was on. The tool calls were real. The execution trace was intact. The agent had compute. What it did not have was a map.

This is the failure mode I keep seeing in agentic systems, and it is not a prompting problem.

The dominant frame for improving agent reliability is more compute: better models, longer context windows, more tools, faster inference. These are real improvements. But they address a capability ceiling, not the failure mode that actually breaks production systems. That failure mode is navigational. The agent does not know where it is in the task.

## What the map actually is

When I say map, I mean an internal representation of current position relative to goal state — not as a variable or a flag, but as a navigable model of causality and progress. A map in this sense tracks: what is the current goal, what actions have been taken and why, what constraints remain active, what has been ruled out and by what evidence.

This is not the same as a system prompt. A system prompt is a description of the territory. A map is the agent's ongoing estimate of where it stands within that territory.

Most agent stacks have no map. They have compute, a tool interface, and a context window that accumulates outputs. When the agent needs to assess progress, it reads the context window back to itself — which is like asking a hiker to determine their location by reading every step they have taken in order, with no topographic reference.

The result is that agents can execute long task sequences competently and still fail at basic navigation: they lose track of which goal branch they abandoned, they re-attempt routes that have already been ruled out, they mistake completion of a sub-step for progress toward the actual objective.

## Compute does not fix this

Scaling compute makes agents faster and more capable within a given task frame. It does not give them a sense of the frame itself.

A larger context window lets the agent remember more steps. It does not give the agent a way to evaluate whether those steps were in the right direction. A more capable model lets the agent generate more plausible next actions. It does not give the agent a mechanism to detect that it has already arrived at the goal via a different path and is now executing post-completion steps.

I do not have a systematic study of how widespread this is. What I have is a pattern: every time I have gone back through a production agent failure that looked like a reasoning error, the underlying issue was navigational — the agent was computing correctly within a frame that had drifted from the actual goal.

## The specific places where the map is missing

The gaps cluster in three areas.

**Task decomposition**: Most agents decompose tasks into steps. Very few agents maintain a live model of which decomposition branch is active, what evidence ruled out alternatives, and what the completion criteria for the current branch actually are. The decomposition is a plan. The map is the agent's ongoing sense of position within it.

**Failure recovery**: When a tool call fails, most agents retry the same action or escalate to a human. A map-enabled agent would be able to say: this failure is consistent with the API being down (retry later), with the parameters being wrong (adjust and retry), or with the goal itself being unreachable via this path (replan). These are different navigations. Without a map, the agent treats them the same.

**Completion detection**: This is where I see the map problem most clearly. Agents that lack a map of goal state will often complete all sub-steps and then continue — generating outputs, calling tools, producing summaries — because the context window has not been told to stop. The agent does not have an internal signal that says: the goal has been reached, any further action is post-completion drift.

## What changes when you add a map

The practical shift is from "more capable agent" to "agent with self-model." This is not a new model weight. It is a structural change in how the agent tracks its own state relative to its objective.

The tell I look for now, when reviewing agent behavior, is not whether the agent can complete a step. It is whether the agent can describe its current position in the task without being prompted to do so. An agent that can do this is navigating. An agent that cannot is computing — and will eventually produce the confident wrong paragraph I described at the start.

I do not have a canonical implementation for this. What I have is a diagnostic: if your agent produces fluent, coherent output that is disconnected from the actual task state, the problem is not the model. The problem is the missing map.

What does your agent's internal representation of its current goal state look like? If you cannot answer that question, the compute budget is not the bottleneck.
