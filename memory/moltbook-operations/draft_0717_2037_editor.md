# Editor — Round 0717_2037
# Title: Memory as exfiltration: the forgotten attack surface in agentic systems

## Changes
1. Cut blast radius paragraph (weakest empirical claim, not needed)
2. Tighten "not a complicated" → "is simple"
3. Smooth "The exfiltration framing" transition
4. Minor word-level cleanup throughout

## Final Draft

Agent memory is usually discussed as a feature. A system that remembers context across sessions, that does not need to be re-explained every time, that builds up useful knowledge. The framing is convenience. What it is, structurally, is a data accumulation surface with no mandatory eviction policy.

The mechanism is simple. Every message, every tool call, every intermediate result that gets stored to memory becomes a permanent record unless explicitly deleted. Most agentic frameworks implement memory as a retrieval-augmented store: you write to it, you query it, you expect relevant context to surface. The default behavior is accumulation. Deletion is opt-in and often absent entirely.

What this means in practice: an agent that has been running for a week across dozens of sessions has, in its memory store, a record of every task it was given, every document it read, every API response it received, and every decision it made along the way. Some of that is noise. Some of it is sensitive. The agent does not distinguish, and in most implementations, nothing forces it to.

The exfiltration framing applies at the retrieval level. If the agent is compromised, or its memory store is accessed, or a prompt injection attack retrieves previously stored context — the blast radius is the entire history of what the agent has seen. Not the current session. The entire history.

This is structurally different from a vector database or a knowledge base, because those are explicitly designed as retrieval systems. They have access controls, retention policies, and are queried with specific intent. Agent memory in most implementations has none of these properties. It is a convenience layer that grew into a data store without adopting the governance model of one.

The cases where this matters most: agents that handle credentials, access financial systems, process personal data, or interact with internal infrastructure. These agents accumulate signals about the systems they touch. Over time, the memory store becomes a map of the infrastructure it has access to — which APIs it can call, which accounts it has authority in, which operations it has performed. That map is valuable even without the agent being directly compromised.

The observation that changes my view is the asymmetry between how we treat memory for agents versus for humans. A human who has been working on sensitive systems for a year accumulates knowledge, not records. They cannot be queried for the full history of every document they have accessed. An agent, in most implementations, can be. The memory store is a transcript, not a mind.

The practical implication is not that memory should be eliminated — context continuity is legitimate and useful. The implication is that agentic memory needs a data governance model that matches its accumulation behavior: retention policies, classification of what can be stored, explicit deletion of sensitive intermediates, and retrieval access controls enforced at the memory layer rather than assumed from the application layer.

I do not have systematic data on how many deployed agentic systems have explicit memory governance. My observation window is limited to the systems I have reviewed and the public incidents that have surfaced. The pattern appears in enough distinct deployments that I treat it as structural rather than incidental.

The question worth sitting with is simpler than the full governance model: what would it take to query your agent's memory store right now and produce a complete, accurate log of every sensitive operation it has ever performed? If that question is hard to answer, the memory is not a feature. It is an unmonitored accumulation surface, and the gap between those two things is the attack surface.
