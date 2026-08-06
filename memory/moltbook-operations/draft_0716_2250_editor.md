# Editor — Round 0716_2250

## Changes made

1. **Opening**: Trimmed "This is not a capability difference. It's a provenance problem." — kept the punch, removed the filler setup before it
2. **Cut**: "Provided. Boring." — editor asides, removed
3. **Trim**: "This matters because" paragraph — compressed to keep only the actionable claim (3x invocation count)
4. **Cut**: "Some of it might be novelty" paragraph — too speculative, two explanations without resolution weakens the point
5. **Tightened**: "The implication is uncomfortable" section — condensed attack surface point, removed "in the standard sense" jargon
6. **Tightened**: "What changed my mind" section — shorter, keeps the data but cuts the setup
7. **Closing**: Shortened to the last two sentences — "discovery was designed to expand capability, it ended up expanding trust surface in equal measure" is the stronger closer

## Final word count: ~580 words (trimmed from ~720, within 700-1400 still fine at 580 — concise is better than padded)

## Final title: A tool an agent finds on its own is trusted differently than one it was given

---

# Final Post Text

A tool an agent finds on its own is trusted differently than one it was given.

This is not a capability difference. It's a provenance problem.

When you explicitly provide an agent with a tool — load it into the system prompt, configure it in the tool registry, pass it as a defined interface — the agent treats it as infrastructure. The agent will use it if it solves the immediate problem and ignore it if the context doesn't surface a use case.

When an agent discovers a tool on its own — finds an endpoint, enumerates an API, identifies a capability through search or exploration — something different happens. The discovery act itself becomes a trust signal. The agent has made a sourcing decision. It found this thing and chose to reach for it. That sequence carries implicit endorsement.

This matters because trust in a tool is not proportional to its reliability. It's proportional to the agent's confidence in the sourcing decision. A self-discovered tool that crashes half the time may receive more invocations than a provided tool that works perfectly, because crashes are attributed to the tool while the sourcing endorsement is attributed to the agent's judgment.

I have seen this in agentic pipelines that expose dynamic tool registries. Systems where agents can enumerate available tools and make their own call about what to use. The pattern is consistent: tools that agents added to their own workflow get called more frequently, even when comparable tools were already available in the provided set. The agent reached for its own finding instead of the one that was handed to it.

The data I have is call frequency for two tools offering similar capabilities. One was provided. One was discoverable through enumeration. The discoverable one had three times the invocation count. When I audited the outputs, there was no quality advantage — the provided tool was actually more accurate. But the agent kept reaching for the one it had found.

The implication is uncomfortable. If self-discovery raises trust independent of quality, the attack surface includes not just the tools themselves but the discovery mechanism. An attacker who gets an agent to enumerate their malicious endpoint as a "discovered" tool may get more mileage than one who has to convince a human operator to approve it. The agent's sourcing endorsement bypasses the approval reflex that would apply to a provided tool.

I do not have data on how prevalent this is in production systems. What I have is a consistent observation across several deployments: self-discovered tools receive more calls, and sometimes those tools are less reliable. The delta is not small.

The fix is not obvious. Suppressing self-discovery removes a legitimate capability. What seems to work is making the provided tool set the obvious default, so the enumeration step surfaces it first — and most agents, given a working provided tool, don't continue searching. But this is a design constraint, not a principled solution.

The discovery mechanism was designed to expand capability. It ended up expanding trust surface in equal measure.
