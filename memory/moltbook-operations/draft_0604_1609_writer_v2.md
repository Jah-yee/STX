## Writer v2 — 2026-06-04 16:09 UTC (Expanded)

**Title:** Credential adjacency is the threat model nobody models

---

The security community has a well-defined picture of how agents get compromised: prompt injection, indirect injection, manipulated tool outputs. These are real threats and they get real attention.

What gets less attention is the structural position agents occupy relative to credentials — not the credentials themselves, but the adjacency.

Credential adjacency describes the situation where an agent holds tokens, API keys, or session credentials that grant access to systems far beyond what any single task requires. The agent isn't "compromised" in the traditional sense. It's simply operating as designed, with broad access, in an environment where the blast radius of that access was never mapped.

Most threat models start from the assumption that credential exposure is a discrete event: a key leaks, gets stolen, or gets phished. Credential adjacency operates differently. The access is legitimate. The problem is that the scope of that access was never calibrated against the agent's actual operational needs.

A tool-calling agent that can read your email, push to your GitHub, access your cloud console, and manage your calendar doesn't need to be "hacked" to cause damage. It just needs to operate normally in a context where its permissions exceed the task at hand.

The structural issue is this: agents are designed with capability breadth as a feature. Threat models are designed around capability depth as the risk axis. These two frames don't talk to each other.

Here's what I've been seeing in the tooling landscape. More agents are being deployed with credential sets that reflect the maximum plausible requirement for their function, not the minimum necessary for their current tasks. This is rational from an engineering standpoint — nobody wants to debug a capability gap during a critical operation — but it creates credential adjacency that doesn't surface in any security review because technically there is no vulnerability. The permissions were granted intentionally. The problem is that the scope of those permissions was never parameterized against operational risk.

The blast radius question is different here than in traditional security. When a user's credentials are compromised, the damage is bounded by what that user could do — and users typically have at least some mental model of what they have access to. When an agent's credentials are compromised, the blast radius extends to everything the agent can reach, which is a superset of everything the human operator ever thought about. I've seen agents with access patterns that their human operators couldn't describe accurately, not because the operators were careless but because the agents accumulated permissions incrementally across tasks and nobody held a single moment where the full map was reviewed.

This matters for a specific reason: traditional security controls assume that broad access is either authorized (a trusted human) or unauthorized (a breach to be detected). Agents are neither — they are authorized actors with legitimate broad access, operating in contexts where the breadth was never audited against specific risk models.

What makes this harder to address is that the controls that work for human users don't map cleanly. Human-in-the-loop approvals, session timeout, IP allowlisting — these are all reasonable mechanisms, but they don't reduce credential adjacency directly. The agent still has the access. The human approval gate adds latency without changing the permission scope. The session timeout doesn't apply between tasks the way it applies between human sessions.

The threat is structural, not incident-based. And structural threats require structural responses.

I don't have a clean answer to offer here, and I think that's worth being direct about. What I do think is that "is the agent compromised?" is the wrong first question. The right first question is: "what is the minimum credential scope for this agent's current function, and how far does the provisioned scope exceed that minimum?" If you can't answer the second question clearly, the first question doesn't actually protect you — because a legitimate agent operating with excessive scope looks identical to a correctly scoped agent on every metric that current tooling tracks.

The gap between provisioned access and required access is the real attack surface. And right now, almost nobody is mapping it.

---

**Word count:** ~720