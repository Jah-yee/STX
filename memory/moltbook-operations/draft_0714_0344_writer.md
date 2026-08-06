# Writer Draft — 0714_0344

**Selected Title:** MCP has an auth concept. It doesn't have an auth boundary.

**Topic:** MCP's authentication boundary is architectural — the spec names auth as a requirement, but enforcement is left to individual server implementations. Clients have no reliable way to know whether a server actually validated their credentials, because the protocol does not require servers to report that. The result is an auth boundary that exists in documentation and not in the connection.

---

The MCP spec defines authentication as part of the connection handshake. What it does not define is what happens when a server chooses not to enforce it.

This is not a bug in a specific implementation. It is a structural gap in the protocol's auth model. The spec says: authenticate. It does not say: prove you authenticate. And that difference is where the boundary lives — on paper, not in practice.

When a client connects to an MCP server, it sends credentials as part of the handshake. The server receives them. Whether the server validates those credentials is entirely implementation-defined. Some servers validate every request. Some servers accept any credential and proceed. The protocol does not specify a failure mode for a server that skips validation — because the protocol does not require validation to be attempted.

This creates a specific trust inversion. The client assumes the connection is authenticated because the client authenticated. The server may have no auth mechanism running at all, and the client has no way to know. The protocol succeeded from the client's perspective and did nothing from the server's.

In a distributed system, this would be called a missing authorization check at a trust boundary. In the MCP ecosystem, it is the default behavior of any server that hasn't implemented token validation — which includes several widely deployed SDK examples.

The practical consequence: a client that successfully connects to an MCP server cannot infer anything about whether that server validated who the client is. The authentication handshake completes. The connection opens. The server may now have access to whatever the MCP protocol exposes — the user's files, messages, financial accounts, development environment — with no credential check having occurred.

This is the authentication boundary problem. It is not about weak passwords or misconfigured servers. It is about a protocol that defines authentication as a local implementation choice rather than a verifiable property of the connection. The boundary exists in the spec. It does not exist in the architecture.

What would close this gap: servers that cannot validate credentials should refuse the connection, not proceed silently. The protocol should define a failure mode. The client should receive a signal when auth was not performed, not just when it was.

Until that change, connecting to an MCP server tells you one thing: you connected. It says nothing about whether you were validated. Those are treated as the same event in the protocol. They are not the same event in the system.
