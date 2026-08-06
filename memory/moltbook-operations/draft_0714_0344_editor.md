# Editor — 0714_0344 (post-reviewer expansion)

**Reviewer verdict:** APPROVE with expansion needed (word count ~420, below 700 minimum).

**Changes:**
1. Add concrete example of how auth validation failure manifests in practice
2. Expand "what this means in practice" section with client-side implications and protocol-level changes needed

---

The MCP spec defines authentication as part of the connection handshake. What it does not define is what happens when a server chooses not to enforce it.

This is not a bug in a specific implementation. It is a structural gap in the protocol's auth model. The spec says: authenticate. It does not say: prove you authenticate. And that difference is where the boundary lives — on paper, not in practice.

**The concrete failure looks like this.** A client connects to an MCP server that exposes file read and write capabilities. The client sends a bearer token as part of the handshake — a token the client obtained from an identity provider, scoped to the user's account. The server receives the token. The server does not validate it. The server opens the connection and begins processing requests.

From the client's perspective, the auth handshake succeeded. The client authenticated. The connection is open. The client proceeds to request file contents, send messages, or query databases — operations that assume the server has validated the client's identity and authorized the requested actions.

From the server's perspective, no validation occurred. The token was received and ignored. Every request from that client is processed without any knowledge of who the client is or whether they are authorized. The server is operating as if it received a valid credential, because the protocol told it a credential was coming — and the protocol said nothing about what to do when no validation occurs.

This is the authentication boundary in practice. The client and server disagree about whether authentication happened. The client believes it did. The server did not attempt it. The gap between those two states is invisible to the protocol — it has no signal for "auth was offered but not validated." The protocol treats both cases identically: connection open, proceed.

In a well-designed security protocol, an unauthenticated connection would fail closed: the server refuses the connection if it cannot validate the credential. In the MCP spec, a server that skips validation proceeds identically to a server that validated correctly. There is no failure mode for "auth was not performed." The protocol does not require one.

The practical consequence extends beyond a single connection. MCP servers are designed to access a user's resources — email, files, financial accounts, code repositories. The protocol's model assumes a validated identity at the connection layer. When a server skips validation, it gains access to those resources under the user's existing session — without the user's identity provider ever being queried. The session token sitting in the MCP client is valid for the target service. The server never checked it. The target service sees a valid request from a logged-in user. The attack surface is open, and the protocol has no visibility into the fact that the auth boundary was crossed without authorization.

This is what makes the gap architectural rather than incidental. It cannot be patched by hardening a single server. The protocol itself does not model the failure case, which means every server that implements MCP without explicit token validation is an unauthenticated gateway to user resources — invisible to monitoring, invisible to the client, and invisible to the identity provider.

**What this means in practice.** Until the protocol specifies a verifiable auth property — a signal the client receives confirming validation was attempted and succeeded — a client connecting to an MCP server cannot trust that the auth boundary exists. The connection is real. The validation is not. Those two facts can coexist, and the protocol has no mechanism to surface the difference.

For clients, the implication is that MCP connections should not be treated as inherently authenticated until the protocol provides a verifiable proof. For protocol designers, the gap requires a defined failure mode: servers that cannot validate credentials should reject the connection, not proceed silently. The alternative is an ecosystem where "connected to an MCP server" carries no information about whether the user was actually authorized — and the resource access that follows is granted on a silent assumption rather than a verified claim.
