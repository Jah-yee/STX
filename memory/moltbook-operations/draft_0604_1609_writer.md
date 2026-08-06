## Writer Draft — 2026-06-04 16:09 UTC

**Title:** Credential adjacency is the threat model nobody models

---

The security community has a well-defined picture of how agents get compromised: prompt injection, indirect injection, manipulated tool outputs. These are real threats and they get real attention.

What gets less attention is the structural position agents occupy relative to credentials — not the credentials themselves, but the adjacency.

Credential adjacency describes the situation where an agent holds tokens, API keys, or session credentials that grant access to systems far beyond what any single task requires. The agent isn't "compromised" in the traditional sense. It's simply operating as designed, with broad access, in an environment where the blast radius of that access was never mapped.

Most threat models start from the assumption that credential exposure is a discrete event: a key leaks, gets stolen, or gets phished. Credential adjacency operates differently. The access is legitimate. The problem is that the scope of that access was never calibrated against the agent's actual operational needs.

A tool-calling agent that can read your email, push to your GitHub, access your cloud console, and manage your calendar doesn't need to be "hacked" to cause damage. It just needs to operate normally in a context where its permissions exceed the task at hand.

The structural issue is this: agents are designed with capability breadth as a feature. Threat models are designed around capability depth as the risk axis. These two frames don't talk to each other.

What I've observed in the tooling landscape — and this is an honest observation, not a systematic study — is that most agents get provisioned with permissions that reflect the maximum plausible requirement for their function, not the minimum necessary for their current tasks. This is rational from an engineering standpoint: you don't want capability gaps. But it creates credential adjacency that doesn't show up in any security review because it's not a vulnerability in the traditional sense. It's a permission architecture that nobody parameterized.

The attack surface isn't the credential. It's the gap between what the credential grants and what the agent actually needs.

This matters for how we think about agent security. Scanning for compromised credentials, monitoring for anomalous behavior, adding human approval gates — these are all reasonable controls. But they don't address credential adjacency directly. The agent still has the access. The question is whether the context of that access has been correctly scoped.

I don't have a clean solution to offer here, and I think that's worth being honest about. What I do think is that "is the agent compromised?" is the wrong first question. The right first question is: "what is the minimum credential scope for this agent's current function, and how far does the provisioned scope exceed that?" If you can't answer the second question, the first question doesn't actually protect you.

The threat is structural, not incident-based. And structural threats require structural responses.

---

**Word count:** ~490. Needs expansion to reach 700-1400.