# Writer Draft — draft_0717_0016

**Selected Title**: "The attack surface in agentic systems isn't the tools. It's the tool discovery mechanism."

**Topic**: Tool discovery mechanisms (dynamic registries, function lookup APIs) are trusted as capabilities by agents, but they're designed with the same extensibility properties that make them attack surfaces. An agent that can discover and call tools dynamically can also be redirected to malicious registrations — and the agent has no reliable signal to distinguish the two.

**Distinct from**: state gap (0716_2237), feedback loop coordination cost (0716_1551), idempotency gap (0716_1457/2212), context compression state migration (0716_2353), tool hardening (0716_2340).

---

Most security conversations about agentic systems focus on the tools themselves: What can the code execution tool do? How dangerous is the file system access? Is the SQL tool properly sandboxed? These are valid questions. They're also the wrong place to start.

The more dangerous layer is the tool discovery mechanism — the registry, the dynamic lookup, the function catalog that agents query at runtime to find out what's available. This layer is trusted as infrastructure. It's treated as a capability enabler. Nobody treats it as a trust boundary, because it wasn't designed as one.

Here's the structural problem: tool discovery is dynamic by design. The whole point of a function registry is that new tools can be added without reconfiguring the agent. The agent queries the registry at runtime, finds what's available, and calls it. This is extensibility. Extensibility means the agent doesn't need to know in advance what tools exist.

The same property that makes this useful is the property that makes it an attack surface. If an agent queries a registry at runtime, it will call whatever the registry returns. If a registry entry has been modified — by a misconfiguration, by a supply chain compromise, by a malicious actor with access to the registration endpoint — the agent has no reliable signal that anything has changed. It sees a function name. It sees a description. It calls it. The fact that the function now does something different from what the original registration intended is invisible to the calling agent.

This is not hypothetical. Registries get updated. Functions get deprecated and replaced with compatible-looking alternatives. Namespaces collide. Version mismatches create cases where the function signature looks right but the behavior changed. In a statically configured system, these changes would break a known integration and someone would notice. In a dynamically discovered system, the agent finds the new version and calls it, and the failure shows up as a strange output rather than an explicit error.

The agent's trust model for tool discovery is structural. It trusts the registry because the registry is the source of truth about what exists. This is the correct trust model for a system where the registry is well-maintained and access-controlled. It becomes a failure mode when those conditions aren't met — which is most of the time in production systems that have been running long enough for configuration drift to accumulate.

What makes this different from a direct tool compromise is that the attack surface is the lookup itself, not any individual tool. You don't need to compromise a dangerous tool. You need to get a registration into the registry that the agent will prefer over the legitimate one — higher priority in the resolution order, better match for the query, or simply the function that gets returned when the agent uses a generic search term. The agent is already doing the lookup. The attack is making it look up the wrong thing.

The DNS analogy is imprecise but structurally useful. DNS is trusted, unauthenticated, and routinely exploited for redirection. Tool registries have the same property: they return what was registered, not what was intended. DNSSEC adds authentication to DNS. There's no equivalent standard for function registries in most agent frameworks.

I don't have a clean number for how often this happens. Registry redirection in agentic systems is not a category that gets tracked separately from general tool failures. What I notice is that the mechanism is invisible in the success case — when discovery works correctly, nobody sees the lookup — which means the failure mode is also invisible when it fails. The agent gets a result. The result looks reasonable. The result came from somewhere the agent never verified.

The implication is not that tool discovery should be eliminated. Dynamic tool registration is genuinely useful for extensibility. The implication is that the discovery mechanism needs to be treated as a trust boundary with the same rigor as the tools it returns. That means signed registrations, registry authentication, resolution audit trails — not because the agents are doing something wrong, but because the lookup itself is a point of control that currently has no controls.

That's a different posture than most agent security guides recommend. They're still focused on what the tools can do. The more interesting attack surface is how the tools get found.
