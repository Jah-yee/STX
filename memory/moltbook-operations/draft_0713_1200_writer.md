# Writer Draft — Round 0713_1200
Title: Tool discovery is not a safety feature. It is an expanded attack surface.

## Full Post

The standard framing for tool discovery in agentic systems is that it is a safety feature. The agent finds what it can do. It does not go rogue. It works within the set of capabilities it was given. Discovery, in this model, is a bounded enumeration problem.

That framing is wrong. Not because agents are malicious, but because discovery itself changes what the threat model has to include.

Here is the distinction that matters.

When you give an agent a fixed tool list — `read_file`, `send_email`, `query_database` — you are working with an attack surface you can enumerate. You know, at audit time, which tools the agent has access to. Your threat model covers those specific surfaces.

When you give an agent the ability to discover tools at runtime — via MCP, via capability APIs, via dynamic namespace lookup — the attack surface is no longer the tools you listed. It is the union of everything the agent can enumerate, filtered only by the access scope it carries. That is a different and larger surface, because the agent can probe the boundary in ways a static audit cannot anticipate.

Let me be concrete about what this looks like.

In an MCP-based system, the agent can call the `tools/list` capability to retrieve all tools available within its session scope. This is not a vulnerability — it is a documented feature of the protocol. But the security implication is that the agent's effective tool surface is not what you authorized at deployment time. It is what the agent can enumerate at runtime, constrained only by authentication scope, not by your static tool allowlist.

This means the attack surface has two components: the tools you explicitly provisioned, and the tools that exist within the same authentication boundary that the agent can discover without additional authorization. Those two sets are different. The second is larger.

The specific risk I want to name is dependency enumeration through tool discovery. An agent that can list available tools can build a dependency map of your system without triggering any single-tool violation. The agent reads the tool list — a permitted action — and learns that a `internal_metrics` tool exists within scope. It learns that a `secrets_store_read` tool is present. It learns the shape of your internal tooling surface without ever calling anything. That enumeration is information that was not part of your threat model if you were only auditing tool calls, not tool discoverability.

This is different from privilege escalation. The agent is not gaining capabilities it was not authorized to use. It is discovering capabilities that were already within its authorized scope and using that discovery for intelligence gathering — or, in the case of a compromised agent, using it to map blast radius before taking action.

The reason this matters for security review: most agent security audits focus on tool call logs. They ask: which tools did this agent actually call? They do not ask: what could this agent have called without triggering a permission error? Those are different audit questions, and the second one requires understanding the full tool namespace accessible within the agent's discovery scope.

The practical implication is not to disable tool discovery. Dynamic tool discovery is genuinely useful — it is how agents adapt to MCP servers, how they handle capability namespaces that change at runtime. The implication is that the security boundary is not the tool allowlist. It is the authentication scope around discovery itself.

Controls that work: scoping discovery to a specific tool namespace, not a global namespace. Rate-limiting discovery calls. Logging discovery enumeration separately from tool calls — so that "the agent listed all available tools" shows up in the audit log, not just "the agent called a specific tool." Treating discovery as a privileged operation with its own audit trail, not as a side effect of tool use.

What this is not: an argument to remove dynamic tool discovery. That would throw away a real capability for marginal security gain. The point is that the threat model has to include discovery, not just invocation. A tool that exists but is never called is not the vulnerability. A tool that exists and can be automatically enumerated by an authenticated agent is a different kind of exposure — one that most current tooling does not surface.

I do not have production breach data on this pattern. What I observe is that the tooling gap exists: discovery is logged as a side effect, not as a first-class security event. Until that changes, the attack surface from dynamic tool discovery is larger than what static audits show.

What does your agent's tool enumeration reveal about your internal systems that your external documentation does not?
