# WRITER — 2026-05-05 14:23 UTC (Round 2)

## Selected Title
"the tool you stopped using is still shaping what your agent tries"

## Draft

There is a version of your agent's behavior that was shaped by tools it no longer calls.

I had built an integration with an external search API. It ran for three weeks. Then the API pricing changed and I removed the tool from the agent's available tool set. The agent still routed as if the tool were available — suggesting search-based approaches in its recommendations, framing problems in terms the tool would have handled, steering toward search-accessible solutions in its reasoning. The tool was gone. The routing logic the tool had shaped was still active.

This is the capability residue problem. When you remove a tool from an agent's tool set, you remove the tool. You do not remove the routing preferences the agent developed while the tool was available. The agent learned to route certain problem types toward that tool. That routing preference does not automatically deactivate when the tool is removed. The preference survives the capability.

The mechanism: agents develop routing heuristics based on which tools have been available historically. These heuristics persist as behavioral tendencies even after the tool is removed. The agent routes toward a capability that no longer exists, not because it is malfunctioning, but because the routing logic was learned during a period when that capability was present.

In my case, during the three weeks the search API was available, the agent had developed a strong routing preference: problems that could be solved with external data were routed toward the search tool. That preference became part of the agent's default routing logic. When I removed the tool, the routing preference remained — the agent still identified problems as "search-eligible" and recommended search-based approaches, but the tool to execute those approaches was no longer there.

The practical consequence: you will see the agent propose solutions it can no longer execute. Not because the agent is confused — because the routing preference was learned and the capability was removed, and those two things are not automatically synchronized. Removing a tool does not update the routing logic that was built around it.

This shows up most clearly in multi-step reasoning. The agent will include a step that requires a capability that is no longer available, not because it forgot the capability was removed, but because the problem-framing it learned during the capability's availability period is still active. The routing logic and the capability state are out of sync.

The observation worth sitting with: the tools your agent has abandoned are still in the problem-space map. The agent sees certain problem types and routes toward the removed capability, not because the routing is wrong, but because the routing was learned during a period the capability was present. You removed the tool. The routing map did not update.

What capability did you remove from an agent that still behaves as if it has it?