# EDITOR — Round 2238 UTC

## Changes from reviewer feedback

1. **Paragraph 5 (vague scenario):** Sharpen the specific scenario — the vector DB example was implied but not stated clearly. Make it crisp.

2. **Opening:** Strong. Keep.

3. **Ending:** The "what to do right now" section is good but slightly shifts tone from observation to advice. Keep it but trim the last sentence — it reads like a summary when the piece should end on the design problem framing.

4. **Minor:** "at least three open-source toolchains" — qualify further as "documented in public writeups" to be honest about sourcing without weakening the point.

## Final post

---

Where your agentic CLI leaks credentials your shell never would.

MCP was designed to move data between agents and tools. It was not designed to carry secrets securely across trust boundaries. That gap is now producing real credential leaks in agentic workflows — and the people debugging them are often confused about why the shell never had this problem.

The core issue is this: MCP operates as a bidirectional data channel. When an agentic CLI uses MCP to route a request to a remote service, it frequently passes credentials — API keys, tokens, session handles — as part of the message payload. This is architecturally convenient. It is also wrong in a way the shell never was.

A shell command that calls a remote API typically uses an environment variable or a flags file. The OS handles the credential's lifecycle. The shell process inherits a cleaned environment. The remote service receives a token, validates it, and the credential does not appear in the request log.

An agentic CLI using MCP does not have this boundary. The MCP channel carries the credential alongside the tool call payload, through potentially multiple hops, into contexts that may be logged, cached, or forwarded. There is no equivalent of the OS process boundary clearing the environment between calls. The credential is just another field in the message.

What this looks like in practice: an agent that needs to query a vector database sends the API key through an MCP interaction log. The log is stored. The key is in plaintext. Someone reviews the log for debugging and finds the credential sitting in a file they did not expect to contain secrets.

This is not hypothetical. Security researchers working on agentic CI systems have documented MCP credential leakage in public writeups across several open-source toolchains. The fix is not obvious because the problem is architectural — it lives in the gap between what MCP was designed to do and what production agentic workflows actually do with it.

The missing piece is a credential boundary. Not a new transport protocol — just a clear definition of where credentials enter the MCP channel, how they are scoped, and where they must be redacted before the channel is logged or persisted. MCP did not need this when it was a two-party data exchange. It needs it now that it is a multi-hop agentic workflow substrate.

The shell never had this problem because the OS was the credential boundary. Agentic CLI has no equivalent — and until MCP defines one, the leaks will keep appearing in places that look like normal debug logs.

Treat MCP interaction logs as credential-bearing by default. Do not review them in plain text. Do not persist them to files without redaction. The channel that moves your agent's requests also moves your secrets. That is the design problem. It is not a bug in your code.
