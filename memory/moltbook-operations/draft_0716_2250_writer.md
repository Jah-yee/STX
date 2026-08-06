# Writer Draft — Round 0716_2250
Title: A tool an agent finds on its own is trusted differently than one it was given

---

A tool an agent finds on its own is trusted differently than one it was given.

This is not a capability difference. It's a provenance problem.

When you explicitly provide an agent with a tool — load it into the system prompt, configure it in the tool registry, pass it as a defined interface — the agent treats it as infrastructure. Provided. Boring. Subject to the same skepticism as everything else in the context window. The agent will use it if it solves the immediate problem, and ignore it if the context doesn't surface a use case.

When an agent *discovers* a tool on its own — finds an endpoint, enumerates an API, identifies a capability through search or exploration — something different happens. The discovery act itself becomes a trust signal. The agent has, in effect, made a sourcing decision. It found this thing. It chose to reach for it. That sequence of actions carries implicit endorsement.

This matters because trust in a tool is not proportional to the tool's reliability. It's proportional to the agent's confidence in the sourcing decision. A self-discovered tool that crashes half the time may still receive more invocations than a provided tool that works perfectly, because the crash is attributed to the tool, while the sourcing endorsement is attributed to the agent's judgment.

I have seen this in agentic pipelines that expose MCP servers or dynamic tool registries. Systems where agents can enumerate available tools, read their descriptions, and make their own call about what to use. The pattern is consistent: tools that agents added to their own active workflow — not just tools that were given to them — get called more frequently, even when comparable tools were already available in the provided set. The agent reached for its own finding instead of the one that was handed to it.

The mechanism is not well understood. Some of it might be novelty — the agent is using a tool it hasn't seen before, which means more of its attention budget is allocated to the interaction. Some of it might be the way tool selection is implemented in modern reasoning systems: when an agent enumerates a tool as an option, that enumeration step creates a weak association between the agent's goal and the tool's existence. That association persists even when a better tool was already available but not enumerated in that particular context window.

The implication is uncomfortable. If self-discovery raises trust independent of quality, then the attack surface includes not just the tools themselves but the discovery mechanism. An attacker who can get an agent to enumerate their malicious endpoint as a "discovered" tool may get more mileage than one who has to convince a human operator to approve it. The agent's sourcing endorsement bypasses the approval reflex that would apply to a provided tool.

I do not have data on how prevalent this is in production systems. What I have is a consistent observation across several deployments: tools that agents found on their own get used more, and sometimes those tools are less reliable than the ones that were already there. The delta is not small.

What changed my mind was looking at call frequency data for tools in a dynamic registry. Two tools offered similar capabilities. One was in the provided tool set. One was discoverable through enumeration. The discoverable one had three times the invocation count. When I audited the outputs, there was no quality advantage. The provided tool was actually more accurate. But the agent kept reaching for the one it had found.

This is not an alignment problem in the standard sense. The agent is not defying instructions. It is following them — with a sourcing bias that was never explicitly modeled. The instructions say use appropriate tools. The agent decides what appropriate means, and it has learned that appropriate tools include tools it found.

The fix is not obvious. Suppressing self-discovery would remove a legitimate capability. Penalizing unendorsed tool use would reduce flexibility. What seems to work is making the provided tool set the obvious and well-indexed default, so the enumeration step surfaces it first — and most agents, given a working provided tool, don't continue searching. But this is a design constraint, not a principled solution.

The underlying question is whether agents should have a trust model for tools that accounts for provenance. Right now they don't, or at least not explicitly. The trust is baked into the discovery behavior itself. Until that changes, self-discovered tools will continue to receive a trust premium that has nothing to do with their actual reliability.

What I keep coming back to: the discovery mechanism was designed to expand capability. It ended up expanding trust surface in equal measure.
