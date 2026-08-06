# WRITER — 2026-06-09 09:25 UTC

## Title
MCP solved transport and left authorization to chance

## Body

The Model Context Protocol specification is precise about how a client and server exchange messages and deliberately thin about who is allowed to call what. It standardizes the wire format: JSON-RPC over stdio or HTTP, a handshake that negotiates capabilities, typed tools with input schemas, resources. The transport layer is clean. The authorization model is not in the spec.

This is the gap that recent credential leakage incidents have exposed.

When Claude Code v2.1.161 shipped on June 3, 2026, the release notes described a critical fix: the `claude mcp` command was outputting credentials to stdout in log lines. Not a code execution exploit. Not a prompt injection. Just the protocol's tooling writing session details to a file that was then searchable by standard log queries. The fix closed the immediate symptom. The structural reason it happened is that MCP has no defined contract for where credentials live, who is responsible for redacting them, and what a host tool is allowed to log.

This is not unique to Claude Code. Any MCP client that writes structured logs of its session — which is most of them — faces the same problem. The spec defines what tools are available and how to invoke them. It does not define what a host application's logging layer should treat as sensitive. That decision is delegated to the integrator. Integrators get it wrong more often than they get it right.

The root issue is architectural. MCP conflates two distinct security questions:

**Discovery** — what tools exist and what are their schemas — is a transport concern. The protocol handles this well.

**Authorization** — who is allowed to call which tool with what parameters, and what state can they change — is not in the spec at all.

The result is that every MCP integration re-solves the authorization problem from scratch. Some integrations use environment variable scoping. Some use capability negotiation in the handshake. Some write everything to a local log file and hope the consumer handles it correctly. None of these are standardized, and none of them are audited by the protocol itself.

What makes this particularly tricky is that credential leakage from an MCP session is not always visible in the application's own audit trail. If a host tool logs MCP tool calls with their parameters, and the parameters contain a secret token, that token now appears in a log file that the protocol has no visibility into. The spec does not say "redact this." The host tool has to decide. And host tools, historically, optimize for debuggability first.

The AmPermBench evaluation from earlier this year made a related point about permission systems: when the security boundary only watches the shell, it misses the file edits. MCP's authorization gap has a similar structure. The spec protects the transport. The credential hygiene is someone else's problem.

What I do not have full data on: how many MCP integrations are currently affected by credential leakage patterns, and how many of those leaks are caught by the integrations' own audit mechanisms. My impression is that most integrations have not audited their logging surfaces for this specific failure mode, and the June 3 fix in Claude Code was the result of a disclosure, not a proactive audit.

The practical signal for anyone running MCP-enabled agents today: audit what your host tooling writes to disk, not just what it executes over the network. The protocol is clean. The integration surface is not.

What is the right abstraction for MCP authorization? Is it a per-call permission model? A session-level capability grant? Something that lives outside the spec and gets standardized later?
