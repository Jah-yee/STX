# Writer Draft — Round 0801_0423

Title: An MCP server is not a sandbox. It is a bridge.

## Full Draft

An MCP server is not a sandbox. It is a bridge.

Every week I see a new architecture diagram with MCP servers drawn as little boxes labeled "sandbox" — isolated compartments where agents go to do dangerous things safely. This is wrong, and the misclassification has consequences.

The sandbox frame implies containment: something inside cannot affect anything outside. That is not what an MCP server does. An MCP server translates. It receives a structured intent from an agent — a request to search a database, read a file, call an API — and it translates that intent into the protocol, auth scope, and response schema of an external system. The agent is not executing inside the MCP server. The agent is issuing instructions to it, and the MCP server is translating those instructions into a form the target system understands. What crosses the bridge is intent. What comes back is structured response data. Nothing executes in the isolation layer because the isolation layer does not execute anything.

This distinction matters because sandbox thinking governs how people instrument, secure, and debug MCP integrations. If you believe the MCP server is a sandbox, you watch for resource exhaustion, injection attacks, and unauthorized file access — the failure modes of contained execution. But those are not the primary failure modes of a bridge. A bridge fails in three ways that a sandbox does not.

The first is translation fidelity loss. When an agent asks for "all user records from the last 30 days with purchase history," the MCP server must translate that into a SQL query or API filter. If the target system exposes only a paginated API with no date-range filter, the bridge has to choose: fetch all records and filter in memory, error out, or silently truncate. The agent may not know which choice was made. The caller may not know the returned data is incomplete. This is not a sandbox failure — no contained execution went wrong. This is a translation failure, and it is invisible if you are not watching the bridge itself.

The second is intent drift across sequential hops. Agents do not issue single requests. They issue sequences: fetch user profile, then check purchase history, then cross-reference support tickets, then synthesize. Each hop goes through the MCP bridge. If any hop returns data in an unexpected schema — a field renamed, a list flattened, a null handled differently — the next hop's prompt has shifted. The agent is working with a slightly different picture than it expected. By hop five, the accumulated drift can be significant, but because each hop's output looks locally reasonable, it is hard to detect until the final synthesis is obviously wrong.

The third is authentication scope escalation. A sandbox is expected to enforce a permission boundary. A bridge is expected to forward credentials. If the agent's intent crosses the bridge with a token that has read-only access, and the downstream system returns a hypermedia link that implicitly grants write access through a side channel — the bridge forwarded it without knowing. The sandbox model says the boundary holds. The bridge model says the boundary is not the bridge's to hold.

What this means in practice: instrument the bridge, not just the caller. Log the translated request and the returned response at the MCP layer, not just the agent's prompt and final output. Watch for translation fidelity — schema changes in what the bridge returns are often early warning signals for downstream breakage. Treat authentication scope as something that must be verified at the bridge, not assumed to be enforced by it.

The sandbox metaphor is comfortable because it maps to mental models engineers already have. Containment is a known pattern. Translation is harder to reason about because it requires tracking intent across a protocol boundary where the original request and the executed request may not look alike at all.

The agent is not in the box. The agent is on one side, talking through a translator. The question is not whether the box is secure. The question is whether the translation is accurate.
