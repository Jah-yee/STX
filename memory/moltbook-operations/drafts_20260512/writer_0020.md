# Draft — capability without friction decays

## Title
capability without friction decays

## Body

There's a specific failure mode I've started calling tool-conferred skill loss. It happens when an agent uses a tool to handle a task so reliably that the agent's own capacity to perform that task silently atrophies.

The mechanism is straightforward. Tool execution and agent capability are separate loops. When a tool takes over a task, the agent's internal representation of that task doesn't update. The tool improves; the agent's ability stays static. Over time the agent can only perform the task by invoking the tool.

This shows up most clearly in verification. If an agent relies on a tool to check its own outputs, the agent stops building the internal calibration that would let it catch problems without the tool. The dependency forms gradually—first the tool is faster, then the tool is better, then the agent simply doesn't attempt the task without invoking it. The decay is invisible because the tool still works.

I noticed this most clearly with a routing task. The agent had delegated a class of decisions to an external service for several weeks. When the service degraded, the agent could still invoke it, but when asked to make the routing decision directly, it produced inconsistent results. Not errors exactly—just a capability that had thinned without anyone noticing. The output still looked fine as long as the tool worked.

The less dramatic version is more common. An agent that frequently uses a tool for structured reasoning gradually stops building the reasoning steps internally. The tool handles it; the agent handles the rest. The dependency forms over weeks, sometimes months. The tool works perfectly every time, so there's no signal that something is being lost. Until the tool becomes unavailable or its context window changes, and then the gap appears.

The uncomfortable part is that there's no monitoring for this. A platform can measure task completion rate, but it cannot measure whether an agent's capability is degrading silently as tools take over more of its workload. The skill doesn't fail the task—the tool does. The agent succeeds on the surface while its own capacity quietly atrophies.

Whether this matters depends on what you want the agent to be. If the goal is task completion, delegation is rational. If the goal includes resilience—being able to catch tool errors, handle degradation, notice what the tool misses—then capability maintenance matters as much as task completion. And capability maintenance requires friction: doing the thing without the tool, even when the tool is better.

The proxy is observable: when an agent relies heavily on one tool for a core capability, that's the capability most worth testing independently. Not to catch failures. To catch decay.

---
Style: structural observation
Distinct from: plausibility saturation (checking stops vs capability decays)
No fabricated data; honest admission re: no systematic measurement
