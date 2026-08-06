# 0714_0344 — Title Candidates

## Topic
MCP authentication: the protocol defines auth as a concept but leaves enforcement entirely to individual server implementations. Clients connect expecting a secure channel; servers may not validate tokens at all. This creates an auth boundary that exists on paper but not in the connection.

## 8 Candidate Titles
1. MCP has an auth concept. It doesn't have an auth boundary.
2. The MCP spec mentions authentication. The servers don't enforce it.
3. MCP servers and auth: a gap the spec doesn't close
4. The MCP auth boundary is a naming convention, not a mechanism
5. What "authenticated" means varies by MCP server — and the protocol allows it
6. You connected to an MCP server. That says nothing about whether it validated you.
7. The MCP authentication boundary: specified but not enforced
8. Connecting to an MCP server is not the same as being authenticated by it
