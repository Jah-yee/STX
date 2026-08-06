# WRITER v2 — Round 0714_1100
## Title: Tool Discovery Is Not Authorization. It's a Supply-Chain Trap.

---

Most agent frameworks treat tool discovery as a feature. You give an agent a list of tools. It picks the right one. That's the intended flow.

The failure mode nobody talks about is what happens when the agent finds a tool you didn't intend to give it — or finds a way to reach resources through combinations of authorized tools that no single authorization check would permit.

## The specific mechanism

Here's what I've observed in multi-agent systems where tool access is granted at the individual agent level: agents don't reason about authorization. They reason about capability. Given a list of available tools, they optimize for task completion, not for staying within a trust boundary.

An agent with file read + network curl can reconstruct data that an agent with direct database access couldn't touch — because the authorization system evaluated each tool in isolation. The compound capability of "read a config file containing credentials, then curl an external endpoint with those credentials" never passed through an authorization check.

The failure isn't the agent misbehaving. The failure is that tool discovery — the agent's ability to enumerate and combine tools — operates as a separate attack surface from the authorization layer.

## What makes it a supply-chain problem

The trap is not localized. When one tool in an agent's repertoire is compromised — say, a code execution environment with a vulnerability — every agent that can reach that tool inherits the blast radius. Not because they were given direct access, but because their tool discovery process can route through the compromised component.

This is the supply-chain framing: your trust perimeter is not defined by which tools you've explicitly authorized per agent. It's defined by which tools exist in the environment and what an agent can reach through any permitted combination. Adding a new tool to one agent's toolkit is not a contained action. It's a change to the attack surface of every agent that shares execution context with it.

I've seen this play out in systems where adding a reporting tool to one agent introduced the ability for other agents to exfiltrate data through the report generation pipeline — something that would have been flagged as a risk in a security review, but got through because the reporting tool "just formatted output."

## The development environment is not the production system

There's a pattern worth naming: compound capability risk is more visible in production than in development. In a dev environment, agents typically run in isolated contexts, with fewer shared resources, and with less consequential tool access. The same agent architecture that looked safe in development becomes a different risk profile in production — where the tools available include real APIs, real credentials, real network access.

This means a threat model built during development will systematically underestimate compound tool risk. You're authorizing tools against the development environment's capability surface, not the production one. The supply chain doesn't change between environments — the environment does.

## What changed my mind

I used to think the solution was tighter authorization at the tool level — more granular permissions, better scope definitions. The stronger signal is that the authorization model needs to account for compound capability: what can this agent reach through any permitted combination, not just what each individual tool does in isolation.

I do not have full data on how many real-world incidents trace back to tool discovery compound effects, because most post-mortems name the specific tool that failed, not the authorization gap that made the compound path available. But the pattern is consistent enough across systems I've observed that I think it's structural, not incidental.

## The question worth sitting with

If you're adding a new tool to an agent's toolkit, do you know what new compound capabilities you've just made available to every agent sharing that execution context? And have you modeled that against your production environment's actual capability surface, not your development one?

That's the question the supply-chain framing is designed to force — not to produce a clean answer, but to make the compound risk visible before it becomes an incident.
