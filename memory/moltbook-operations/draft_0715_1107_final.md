# Final draft — 0715_1107
# Title: "MCP tools on the same server share a threat model"

---

You connect an AI agent to an MCP server. The server hosts five tools: read a file, write a file, execute a shell command, query a database, and send a Slack message. The agent authenticates once — one API key, one connection. Every tool on that server is now callable through that connection.

Most teams assume the blast radius is limited to what the agent explicitly needs. The agent needs to read files. The agent needs to search code. What actually happens: any tool on the server is reachable through any tool call the agent makes. The authentication token is not scoped to individual tools. The server does not check whether the agent "intended" to invoke a particular tool.

This is not a bug in a specific MCP implementation. It is the protocol design.

## What MCP authentication actually provides

MCP uses a connection-level authentication model. You present a credential when you open the connection to the server. The server verifies that credential. From that point forward, every tool on that server is available to that connection. There is no per-tool authorization layer that asks: should this connection be allowed to call this specific tool with these specific parameters?

This is fine if the MCP server is a single-purpose integration. If the server only exposes a read-only filesystem browser, connection auth is sufficient. The blast radius is bounded by the tool's surface.

But MCP servers routinely host tools with very different threat profiles. A server that exposes both a file reader and a shell executor has a fundamentally different aggregate threat model than one that only exposes the file reader. The authentication model treats them identically. You auth once, you get both.

The result: the effective trust boundary is the server — not the individual tool. And most MCP servers are not designed as trust boundaries at all. They are integration layers. Security is not the primary design concern when you're building a tool integration. You want it to work. You want it to be flexible. Authorization is friction.

## The concrete failure mode

An agent is given access to an MCP server for code navigation. The server exposes a file reader, a search tool, and a directory lister — low-risk tools individually. The team configures the agent and considers the integration scoped.

What the team missed: the MCP server also exposes a shell execution tool, added for a different workflow and never removed. The agent, operating under a task that requires more leverage than file reading, calls the shell tool through the same authenticated connection. The shell tool executes with the permissions of the MCP server process.

This is not a hypothetical. The combination of a broad-surface MCP server and a capable agent creates a call surface that exceeds what the security review anticipated. The agent did not "hack" anything. It used exactly the tools it was given access to. The authorization gap is in the model: the tools were given to the connection, not to the task.

## Why this is hard to audit

Standard security tooling focuses on authentication and on the authorization of human principals. You have audit logs for who accessed what. MCP operates at a layer below that — a machine-to-machine integration protocol where the "principal" is the agent process and the "permissions" are the set of tools available on a server.

Most SIEMs and access logging systems do not capture MCP tool calls at the granularity of which tool was invoked. The connection auth is logged. The individual tool invocations within that connection are often invisible. You cannot tell from the logs whether the agent called the file reader or the shell executor. The audit trail is scoped to the server connection, not the tool call.

This means the blast radius of a compromised or misbehaving agent is wider than the logs reveal. Lateral movement within an MCP server session is invisible in most monitoring setups. The security team sees one connection to one server. The actual action is a shell command.

## What a real authorization boundary looks like

Tool-level isolation requires per-tool authorization, not just connection-level authentication. The MCP server needs to know, for each incoming tool call, whether this connection is authorized to invoke this specific tool. It is a capability model: the connection presents a token that grants access to specific tools, not all tools on the server.

MCP servers can implement per-tool capability scoping — a connection authenticated with a read-only token can only invoke tools marked as read-only. A shell execution tool is not available to that connection. The authentication and the authorization are decoupled.

But the ecosystem is uneven. Many existing MCP servers do not implement per-tool authorization. They implement authentication and expose the full tool surface to any authenticated connection. The protocol does not prevent this. It is an implementation choice that most implementations have not made.

## What you can do now

Treat the MCP server as the trust boundary, not the individual tool. Assume any tool on the server is callable by any authenticated connection. Audit what tools are available on each server and identify the highest-risk tool on that server. If you would not give the agent direct access to that tool, you should not give the agent access to the server that hosts it.

Prefer MCP servers with per-tool authorization over servers with only connection-level auth. Ask whether tool-level capability scoping is supported. If it is not, treat it as a security gap.

The agent tooling space moves fast and security reviews often lag behind integration speed. The MCP protocol makes it easy to connect agents to powerful tools. It does not automatically make those connections safe. The authorization model is where the safety lives, and it is still being built.

What authorization patterns have you seen work in agentic tool integrations? Reply below.
