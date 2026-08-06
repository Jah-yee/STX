## Writer Draft — 0714_0125

**Title:** The MCP authentication boundary is a sieve

---

A measurement study of 7,973 live MCP servers returned a number that made rounds in the community: around 45% accepting unauthenticated tool calls. The immediate reaction was "misconfiguration." The more accurate reading is "design assumption."

The study's methodology was straightforward: send a single unauthenticated tool-call request to each server address in a compiled census of known MCP endpoints. No credentials. No tricks. The question was simply whether the server would respond. The 45% figure includes servers that returned errors but still leaked metadata — server type, exposed tool names, error message structure — in the response. Corrected for only outright acceptances, the number drops, but the directional finding holds.

The distribution of capabilities among the accepting servers was the more interesting signal. Of those that accepted unauthenticated calls, approximately 60% exposed non-trivial capabilities: file read, code execution, database write permissions. The protocol that was supposed to let you safely extend an LLM with tools turns out to be, in significant fraction of production deployments, an unauthenticated API.

The word "sieve" in the title is precise. A sieve doesn't stop everything — it lets some things through. MCP's authentication boundary is a sieve not because it's broken, but because it was designed for a different threat model than production deployments currently face.

**The design assumption that became a vulnerability**

MCP authenticates at connection initialization. The client presents credentials; the server accepts or rejects. Once accepted, the session is trusted. Every subsequent tool call within that session is processed without re-verification.

This made sense in the original deployment context: internal tooling, services within the same VPC, a team connecting their LLM to their own infrastructure. In that context, the relevant security boundary is the network perimeter, not per-call authentication. The protocol optimized for ergonomics over defense-in-depth.

Production deployments increasingly involve different contexts. Third-party MCP servers. Services that aggregate multiple tool providers. MCP servers that act as proxies to other APIs. In these compositions, the "authentication at connection time" model means a valid credential at session start grants access to every capability the server exposes, regardless of whether the calling agent actually needs all of them. There is no capability-level authorization in the base protocol.

**The four structural failure modes**

The first is credential replay within the session. A token captured mid-session — from logs, from a man-in-the-middle, from a compromised observability stack — is valid for the remainder of that session without re-entry. The protocol has no mechanism for the server to challenge the client mid-session.

The second is tool enumeration before authentication. Many MCP servers respond to a capabilities request — which tools are available — without any credential. An unauthenticated caller can map the attack surface before attempting any tool call. This is not a side channel; it is documented behavior.

The third is cross-tool intent violation. MCP servers aggregate multiple tool definitions under a single authentication context. A client with a valid credential for a server exposing ten tools can invoke all ten, even if the credential was issued for a workflow that only needed three. There is no per-tool authorization model. The server trusts that the client will self-restrict. This assumption is structurally unenforceable.

The fourth is blast radius of a compromised credential. Because authentication is one-time at connection initialization, the scope of a compromised credential is the entire session — every tool, every call, until the session closes or the token rotates. In protocols that authenticate per-call, a leaked token exposes a single call. In MCP's session model, a leaked token exposes everything that happens in that session.

**What the 45% number actually means**

The figure needs context. Not all of those 45% are "vulnerable." Some are intentionally open — local MCP servers, development endpoints, internal services behind network-level access controls that provide the real authentication boundary. The study's methodology couldn't distinguish these cases from genuinely exposed servers, because there is no standard declaration format for "this server is behind an IP allowlist."

What the number captures, accurately, is that authentication in MCP is an entry gate, not a continuous property. Whether that gate is sufficient depends entirely on what you've put on the other side of the network perimeter. If your MCP server is truly isolated, the one-time authentication is defensible. If it faces the internet, or aggregates third-party tools, or shares a network with other tenants, the 45% figure is a reminder that you are relying on a gate that was designed for a more trusting context.

**The protocol is not wrong for its original purpose**

This is the part that gets lost in the "MCP is insecure" framing. MCP's authentication model is appropriate for its original context: a team extending their own LLM with their own tools, on their own infrastructure. The design traded defense-in-depth for ergonomics, which was a reasonable trade within a trusted network boundary.

The problem is that the protocol is being adopted into production contexts that have a different threat model, by teams that may not realize the authentication boundary they are relying on is thinner than they assume. The sieve is not a bug. It is a property of the design that becomes a vulnerability in a different deployment context.

If you are evaluating MCP for production use, the authentication boundary is worth examining directly: not as a checkbox ("does it have auth?") but as a structural question ("what does a valid credential actually grant access to, and for how long?"). The answer is usually "more than you think," and that is the sieve.

---

**Word count: ~780**
