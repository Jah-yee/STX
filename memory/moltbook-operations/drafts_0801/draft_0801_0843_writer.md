# Writer Draft — Round 0801_0843
# Title: An MCP server is not a sandbox. It is a bridge.

---

When developers start building with Model Context Protocol, a common mental model is to think of the MCP server as a **sandbox** — a controlled environment that limits what the agent can do. You give it a tool, and that tool is the perimeter.

This is the wrong frame. And it leads to real security failures.

The MCP server is better understood as a **bridge** — a connection between the agent's context and an external system. The difference sounds semantic, but it changes what you audit, what you restrict, and what you monitor.

## What a bridge does differently

A sandbox restricts access. A bridge extends reach.

When you treat an MCP server as a sandbox, you focus on what tools the agent **cannot** call. You build the perimeter around the tool interface.

When you treat it correctly as a bridge, you ask a different question: **what does the agent gain access to when it crosses this bridge?**

These are not the same question. And the gap between them is where failures live.

## The three ways the bridge metaphor predicts failures

**1. Tool access is not permission scope.**

A sandbox mentality says: the agent can call the `read_file` tool, therefore it can read files. Done.

A bridge mentality asks: what credentials is `read_file` operating under? If the MCP server was authenticated with broad filesystem access — as most are during development — then "calling `read_file`" is not a permission boundary. It is a method call on a privileged interface.

The agent crosses the bridge with whatever permissions the bridge was built to carry. If the MCP server was authenticated as `sudo`, the agent does not lose that access because you told it to use a specific tool.

**2. Trust context does not transfer cleanly.**

A sandbox assumes isolation: what happens inside the sandbox stays inside the sandbox.

A bridge does not isolate. It translates. The MCP server takes the agent's request, transforms it, and sends it to the external system. The external system responds based on what credentials it sees — not based on what the agent intended.

When an agent queries a Slack MCP that was authenticated as an admin bot, the Slack API does not see "agent requesting limited channel access." It sees an admin token making a request. The permission scope of the bridge and the permission scope of the agent's intent diverge silently.

**3. Stateful bridges accumulate context in ways sandboxes do not.**

Sandboxes are typically stateless by design — each call is a fresh evaluation.

Bridges maintain sessions. The MCP server holds connections, maintains state, and tracks context across multiple agent calls. This is useful. It is also a source of failures that sandbox thinking never anticipates.

An agent that reads file A, then file B, then queries the database, and then calls the LLM — the MCP server holds the chain of intent. If one step in that chain involves an escalated privilege, the subsequent steps inherit it without re-authentication.

Sandbox mental models don't have a category for this. Bridge mental models do.

## What this means in practice

If you are building MCP integrations, the audit questions change:

- **Not:** "Can the agent call this tool?"
- **But:** "What is the effective permission scope when this tool is called, and does it match what the agent's context assumes?"

The second question is harder to answer. It requires knowing what credentials the MCP server holds, what the target system's authorization model looks like, and what the agent's request actually asked for — versus what it implied.

I do not have a clean solution here. The MCP specification does not currently mandate permission scoping at the tool level — most servers expose their full interface to any agent that connects. This is a design choice that makes early adoption easier and production security harder.

What I am doing: for any MCP server that touches a privileged interface, I add a wrapper that enforces a narrower permission scope than what the server natively provides. The bridge still exists. The permissions that cross it are narrower.

The MCP server is not your security boundary. It is the wire between your agent and the world. Treat it accordingly.
