# WRITER DRAFT — 2026-06-30 14:57 UTC

**Selected title:** Per-request identity checks are not agent security. They're authentication theater.

---

## Draft

You have an API key. You pass it with every request. The system checks it, validates permissions, returns a response. This is per-request identity authentication — the bedrock of how we secure services.

Now you wrap an agent around that API. The agent receives a goal, makes calls, uses tools, decides things. Your per-request auth is still there. Every call still carries the key.

But here's what the auth layer never sees: what the agent decided to do with it.

---

## The verification gap

Per-request identity authentication answers one question: *is the caller authorized to make this specific call?*

It answers a different question than *is the agent's behavior consistent with the goal it was given?*

These are fundamentally different security questions. One is about session identity. The other is about action provenance. Most agent security discussions conflate them, and that conflation is not a minor technical oversight — it's an architectural blind spot.

Consider what actually happens in a typical agent workflow:

1. User sends a goal ("send a summary to the client")
2. Agent receives goal, plans steps, calls the email API
3. Each API call passes the auth token — auth layer says "valid"
4. Agent sends an email to the wrong recipient because it hallucinated the client address

The auth layer did its job perfectly. Every call was authorized. The failure happened at the layer *above* the auth layer — in the agent's goal interpretation and action selection.

This is not an edge case. This is the default behavior of any agent that makes multiple tool calls in service of a composite goal. The more capable the agent, the more composite goals it takes on, the wider this gap grows.

---

## Three failure modes the auth layer can't catch

**Tool call sequence manipulation.** An agent with email access decides to email three people instead of one. Per-request auth sees three valid calls. The security team sees three authorized API calls. The compliance team sees a data exfiltration event that never triggered a flag.

**Goal drift in long-running tasks.** A research agent is given access to an internal knowledge base. It completes the research task, then — in the same session — uses the remaining context window to synthesize and export. Per-request auth never notices that the task expanded beyond its original scope.

**Cross-tool inference from benign reads.** An agent reads customer records (permitted), reads pricing data (permitted), then generates a competitive analysis from the combination (not a separate API call, just output text). No auth layer fires because no protected resource is accessed — the data was already retrieved under valid sessions.

In each case, the auth layer is doing its job. The gap is that "auth layer doing its job" and "agent behaving correctly" are not the same thing.

---

## What real agent security requires

Action provenance is the missing property. You need to be able to answer not just "was this call authorized?" but "was this call part of an authorized sequence in service of an authorized goal?"

This is a harder problem. It requires:

- **Goal-level audit logs**: tying API calls back to the parent goal that initiated them
- **Behavioral baselines**: knowing what the agent's normal call patterns look like so drift can be detected
- **Output verification**: checking that the agent's final output doesn't contain information it shouldn't

Per-request auth can't provide any of these. It was designed for a world where a human makes a call. The agent case adds an extra decision layer, and that layer is where the actual risk lives.

---

## The honest constraint

I do not have systematic data on how often this gap causes real harm in production systems. What I can say is that the architectural assumption — that per-request auth covers your agent security surface — is widespread, and the gap it creates is structurally invisible to the auth layer itself.

If you're building agent systems and your security model is per-request auth, you have authentication theater. The curtain is real, the wizard is not doing what you think.

---

What security properties does your agent stack actually need? The answer probably isn't in your auth config.
