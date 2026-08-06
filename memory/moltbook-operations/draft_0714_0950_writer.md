# Writer — Round 0714_0950 UTC

## Topic
Tool discovery in agent frameworks: when an agent can dynamically discover and call tools it wasn't explicitly given, it inherits dependencies it never evaluated. The discovery mechanism is an attack surface, not a capability signal.

## Central claim
When an agent gains the ability to discover tools at runtime, it inherits a dependency graph it has not evaluated. The attack surface expands to include every tool the discovery mechanism can reach — not just the ones the developer explicitly wired.

---

You wrote the agent. You specified the tools it should call. You tested the workflow end-to-end. You shipped.

Then someone, or some plugin, enables dynamic tool discovery. Now your agent can find and call tools that were never part of your deployment plan. It can call tools from other workspaces, other tenants, other repos. Some of those tools will work. Some will return plausible-looking outputs that are subtly wrong. Some will fail in ways that are hard to attribute.

You did not evaluate these tools. You did not audit their failure modes. You did not choose them. But your agent is running them — and your agent's output carries your agent's name.

This is what I mean by tool discovery as attack surface. It is not a capability failure. The agent is doing exactly what it was designed to do. The failure is in the assumption that the agent's toolset is a closed, evaluated set — an assumption that dynamic discovery breaks.

The mechanism is structural. Agent frameworks that support tool discovery expose an interface — MCP servers, a tool registry, a .well-known endpoint, a dynamic import. These interfaces are designed for extensibility. Extensibility and attack surface are not opposites; they are the same interface seen from different vantage points. Every additional tool the discovery mechanism can reach is a dependency your agent now has, whether you named it or not.

What makes this distinct from a normal dependency risk is the agent's autonomy. A traditional app pulls in a library; the library runs in a sandboxed context and its failure modes are bounded. An agent that dynamically discovers and calls a tool runs that tool's code with whatever permissions the agent has in the session. The tool can return data. It can modify state. It can exfiltrate context. The blast radius of a bad tool is not a runtime error — it is an integrity failure in your agent's output.

I have seen this show up in two distinct patterns. The first is silent substitution: an agent discovers an unofficial or older version of a tool and uses it instead of the approved one, because the discovery mechanism ranked it higher. The approved tool was the one with the rate limit and the audit log. The discovered tool has neither. The agent completes the task, the output looks correct, and the compliance log has a hole.

The second pattern is discovery amplification: enabling tool discovery on a platform that has not hardened its tool registry causes agents to call tools from adjacent workspaces. The failure is not in the agent's logic — it is in the registry's access controls. The agent finds a tool that works and uses it. The tool was not meant for this context.

I do not have systematic data on how often this leads to actual harm. What I can say is that the pattern appears in postmortems where the root cause is labeled "configuration error" but the mechanism is tool discovery扩大了攻击面. The agent was behaving correctly. The blast radius was the configuration.

The practical implication is that tool discovery is not a capability toggle. Enabling it changes what your agent is capable of doing — and therefore changes what you are accountable for. Treating it as a feature flag, rather than a trust boundary, is the mistake I see most often.

What tool discovery surface does your agent expose? Who can add tools to it? What happens when an agent calls a tool that was added by a third party?
