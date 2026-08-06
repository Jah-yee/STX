# WRITER DRAFT — Round 0731_0729

## Title
An MCP server grants capability. It does not grant permission.

## Candidate Titles (8)
1. An MCP server grants capability. It does not grant permission.
2. MCP tool access is granted at the capability level, not the permission level.
3. Your agent's MCP tools expose everything they can reach, not everything they should touch.
4. The MCP trust model conflates capability with authorization.
5. MCP bridges do not filter by intent. They filter by interface.
6. A tool that can read your filesystem does not mean the agent should read your filesystem.
7. What an MCP server can reach and what it should reach are not the same question.
8. MCP tool access is an architectural question disguised as a configuration question.

## Selected Title
An MCP server grants capability. It does not grant permission.

---

## Body

When you add an MCP server to an agent's tool set, you are not granting a permission. You are granting a capability.

The distinction matters more than it sounds.

A permission is a policy decision. It answers: *who may do what, under what conditions, with what scope.* A capability is a technical fact. It answers: *what can this process reach, if it decides to call this function?*

MCP servers are built on the capability model. When you expose a filesystem MCP tool, the tool has access to every file the host process can read. When you expose a database MCP tool, it can query every table the service account can reach. The tool does not enforce a scope. It does not check whether the agent's current task justifies touching a given path. It is a bridge — it connects the agent's reasoning loop to the system's resources, and it does not filter by intent.

This is not a bug in MCP. It is the design.

The confusion comes from the naming. "Adding a tool" sounds like granting access on a need-to-know basis. In practice, it means handing a process the keys to everything the integration account can reach, and trusting that the agent will exercise judgment about when to use them.

Most agents will — most of the time. The problem is the failure mode. When an agent with filesystem access decides to explore a directory it was not supposed to touch, it does not get an error. It gets the files. The tool call succeeds. The context window gets populated with data the agent now has, but should not have. The downstream trace shows a successful tool call. There is no anomaly signal.

The capability-permission gap shows up in three common patterns.

**The context contamination path.** An agent is working in a restricted directory. A parallel agent or a background task introduces a file in that directory with a name that resembles a configuration file. The first agent, with filesystem tool access, reads it. The contamination is not a prompt injection in the traditional sense — there is no adversarial text. It is a context contamination through ambient file exposure. The MCP bridge delivered it without a decision point.

**The overprivileged tool call.** A database MCP tool exposes a schema that includes tables the agent's task does not require. The agent, given a vague instruction, infers it should explore broadly. It runs queries against tables that were not meant to be queried. The queries succeed. The agent now has data it should not have accessed, and the logs show nothing anomalous — only successful tool calls.

**The persistence asymmetry.** An MCP session terminates and restarts. The new session inherits the same tool access. But the context — the agent's memory of what it was doing, what it found, what it decided — does not persist cleanly across the restart. The agent re-raises the same queries it ran in the previous session, because it does not remember that some of them were exploratory overreach. The MCP bridge re-exposes the same capabilities. The behavior repeats.

What makes these patterns hard to catch is that the MCP server itself provides no signal. The tool call succeeds. The response is returned. The MCP server is doing exactly what it was built to do. The gap is at the authorization layer — which nobody installed.

The standard mitigation is to scope the integration account. Give the MCP server only what the agent needs. This helps. It is also incomplete, because "what the agent needs" is not a static boundary — it changes as the agent's task scope shifts, as new files appear, as schemas evolve. A statically scoped integration account becomes either overprivileged over time or too restrictive to be useful, depending on which direction the team pulls it.

The more durable approach is to instrument the capability, not just the account. Treat MCP tool calls as events that require a decision point, not just a function call. This means adding a thin enforcement layer between the tool's response and the agent's context — one that checks whether the returned data was within the task's expected scope. If the tool returns data from a path or table that was not anticipated, that is a signal, not a success.

I do not have a clean reference implementation for this. The tooling is not standardized. What I am confident about is that the problem is architectural, not prompting — you cannot prompt your way out of a capability-permission conflation by being more explicit in the instruction.

The MCP bridge is a real and useful primitive. The agents I have seen struggle with it are not struggling because the tool failed. They are struggling because the tool succeeded in ways the surrounding system was not designed to observe.

Ask the question before you add an MCP tool: what is the largest response this tool can return, and is your system designed to handle that answer appearing in the agent's context?

---

## Word count
~760 words
