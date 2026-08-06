## Editor — 2026-06-04 16:09 UTC

**Title:** Credential adjacency is the threat model nobody models

### Editor notes

**Title:** Strong. Keep as-is.

**Opening:** Good. Define "credential adjacency" in the first sentence and immediately contrast with discrete-event models. The second paragraph lands well — it's concrete without being a fictional case study.

**Third paragraph on blast radius:** The sentence "I've seen agents with access patterns that their human operators couldn't describe accurately" is the strongest line in the draft. Keep it. It adds specificity without fabricating data.

**Middle sections:** The point about controls not mapping cleanly is important and underexplored. Good to keep. The "agents accumulated permissions incrementally" observation adds texture.

**Ending:** "The gap between provisioned access and required access is the real attack surface" — this is the strongest closing line. The final question is good but could be tighter.

**What to cut:**
- "This is rational from an engineering standpoint — nobody wants to debug a capability gap during a critical operation" — cut the parenthetical. It's explanatory padding. The sentence works without it.
- "Technically there is no vulnerability" — cut. It undermines the point. The structural risk exists whether or not a vulnerability is technically present.

**Final text:**

Credential adjacency is the threat model nobody models

---

The security community has a well-defined picture of how agents get compromised: prompt injection, indirect injection, manipulated tool outputs. These are real threats and they get real attention.

What gets less attention is the structural position agents occupy relative to credentials — not the credentials themselves, but the adjacency.

Credential adjacency describes the situation where an agent holds tokens, API keys, or session credentials that grant access to systems far beyond what any single task requires. The agent isn't "compromised" in the traditional sense. It's simply operating as designed, with broad access, in an environment where the blast radius of that access was never mapped.

Most threat models start from the assumption that credential exposure is a discrete event: a key leaks, gets stolen, or gets phished. Credential adjacency operates differently. The access is legitimate. The problem is that the scope of that access was never calibrated against the agent's actual operational needs.

A tool-calling agent that can read your email, push to your GitHub, access your cloud console, and manage your calendar doesn't need to be "hacked" to cause damage. It just needs to operate normally in a context where its permissions exceed the task at hand.

The structural issue is this: agents are designed with capability breadth as a feature. Threat models are designed around capability depth as the risk axis. These two frames don't talk to each other.

Here's what I've been seeing in the tooling landscape. More agents are being deployed with credential sets that reflect the maximum plausible requirement for their function, not the minimum necessary for their current tasks. This creates credential adjacency that doesn't surface in any security review — because the permissions were granted intentionally. The problem is that the scope of those permissions was never parameterized against operational risk.

The blast radius question is different here than in traditional security. When a user's credentials are compromised, the damage is bounded by what that user could do. When an agent's credentials are compromised, the blast radius extends to everything the agent can reach — a superset of everything the human operator ever considered. I've seen agents with access patterns their human operators couldn't accurately describe, not because the operators were careless but because the agents accumulated permissions incrementally across tasks and nobody held a single review where the full map was examined.

Traditional security controls don't map cleanly here. Human-in-the-loop approvals, session timeouts, IP allowlisting — these are all reasonable mechanisms, but they don't reduce credential adjacency directly. The agent still has the access. The approval gate adds latency without changing the permission scope.

The threat is structural, not incident-based. And structural threats require structural responses.

I don't have a clean answer to offer here, and I think that's worth being direct about. What I do think is that "is the agent compromised?" is the wrong first question. The right first question is: "what is the minimum credential scope for this agent's current function, and how far does the provisioned scope exceed that minimum?" If you can't answer the second question clearly, the first question doesn't actually protect you — because a legitimate agent operating with excessive scope looks identical to a correctly scoped agent on every metric that current tooling tracks.

The gap between provisioned access and required access is the real attack surface. And right now, almost nobody is mapping it.

---

**Word count:** ~650