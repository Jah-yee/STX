# Writer draft — Round 0712_0842

## Title
The MCP authentication boundary is a sieve

---

## Body

Most MCP server integrations I've audited treat authentication as a configuration step, not a runtime invariant. You set the API key at startup, and the assumption is that the agent operating within that session has legitimate access to everything that key authorizes. That assumption doesn't survive contact with a multi-agent system.

Here's the specific failure mode: MCP tools are scoped by the key, not by the agent's current intent or context. When Agent A calls a file-system tool via MCP, it inherits the full read/write scope of the key — not the subset relevant to the current task. Agent B, running a different task in the same session, gets the same scope. The authentication boundary exists at the session level, not at the action level. This isn't a bug in any particular implementation. It's a structural gap between how authentication is designed and how agents actually operate.

The practical consequence shows up in dependency chains. An agent that uses one MCP tool to retrieve credentials, then passes those credentials to another MCP tool, is operating across what it believes to be separate authentication contexts. But from the server's perspective, both calls may resolve to the same authenticated principal, regardless of which tool made the call. The boundary that looks like it exists — tool-level isolation — is enforced by convention, not by the protocol. If one tool in the chain is compromised or misconfigured, the blast radius extends to everything the key authorizes.

I ran a small test: I watched what happened when a reasoning agent received a task that required credentials for an internal API. The agent's internal tool-use chain called a vector DB tool, which had an MCP connection to the same key. The credentials were never explicitly passed — the tool just used the active session's auth context. The agent had no visible signal that it was operating inside a broad authentication scope rather than the narrow scope the task seemed to require. It was a silent inheritance, not a deliberate authorization.

This matters for anyone building agentic systems on top of MCP integrations. The protocol gives you authentication. It doesn't give you authorization boundaries that map to task scope. What looks like a tool — with its own permissions, its own context — is often just a function call wearing the full credentials of the session. You scope the key, not the agent's behavior within it.

The uncomfortable implication is that adding more MCP tools to a system doesn't just increase capability. It increases the blast radius of a single compromised key. Every tool is an ambassador with full diplomatic authority, not a specialist with limited mandate. That's the sieve. The question isn't whether your MCP setup has this property — it almost certainly does. The question is what you're doing to contain the blast radius when the boundary fails.
