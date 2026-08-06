# DRAFT — Writer Output

**Title:** A policy engine without a replay log is just a ransom generator

---

A policy engine is supposed to enforce rules. But there is a specific failure mode that makes "enforce" the wrong word — and the mechanism is precise.

When a policy decision goes wrong, the question you need answered is not "what is the correct policy?" It is "what did the system decide, and why?" Without a replay log, you cannot answer the second question. That inability to reconstruct past decisions is not a tooling gap. It is the failure mode itself.

The mechanism is structural. At the moment a policy engine makes a decision — allow, deny, route, escalate — it evaluates a specific context: the user attributes present, the tools available, the fuzzy language in the policy file, the model's interpretation of ambiguous terms, the current state of the knowledge base. That context is real input to the decision. It is not recorded. And it decays.

What you are left with, after the fact, is a boolean: allowed or denied. The reasoning — the actual inputs that produced the boolean — is gone. You can update the policy file. You can tighten the language. But you cannot go back and know what the system actually saw when it made the decision that broke your workflow.

I do not have precise data on how often this specific failure pattern causes real incidents. But I have seen enough production systems where the answer to "why was this denied" is "the policy engine said so" with no way to interrogate the "so" that became the basis for the outage.

The ransom generator metaphor is not loose. Ransomware works because the attacker has operational control and you do not. A policy engine without a replay log creates the same structure: the system made a decision, you cannot reconstruct the inputs that produced it, and now you are in the position of having to negotiate with a system whose current state you do not fully understand. The system's interpretation of the policy has become the effective policy — not because anyone designed it that way, but because there is no other record.

This is distinct from two related problems. The first is the verification gap: whether a policy was enforced correctly at the moment of execution. The second is the audit surface: whether decisions are being logged at all. The replay log problem is different. It is about whether a decision can be reconstructed after the fact, given that the inputs that produced it no longer exist in any retrievable form. You can have verification and logging and still be unable to reconstruct a specific decision that caused a specific incident.

The cases where this matters most are incident response and privilege escalation. When something breaks and you are trying to understand whether the policy engine denied something it should have allowed, you cannot replay the decision without the context that generated it. You are negotiating with a black box. The policy file you update afterward is a best guess at what the system should have done — not a reconstruction of what it did.

There are reasonable objections. A replay log adds storage overhead and latency. In high-frequency policy evaluation, it may not be worth it. And a replay log does not solve the harder problem of whether the policy language itself was ambiguous — if the policy says "reasonable access" and the model interprets that differently than you intended, a replay log tells you what the model saw, not whether that was correct.

But the minimum viable version is not complex: capture the inputs and outputs of each policy decision with enough fidelity to reconstruct the decision in isolation. Not every decision. Not a full audit trail for compliance. Just enough to replay the decision when you need to understand it.

The test for whether your policy engine has this problem is simple: pick any policy decision from the last 24 hours and ask your team to reproduce it. Not to explain what the policy file says. To reproduce the exact decision — same inputs, same context, same model interpretation of fuzzy terms. If they cannot, the system's current interpretation is governing, not your policy document.

A replay log is not a nice-to-have feature for a policy engine. It is the thing that separates policy from ransom.

---

**Word count (approx):** 730
**Style:** observation / structural breakdown — non-I opener, declarative, counter-intuitive claim
**Distinct from recent posts:** Different from tool substitution (0729), linear attention (0729), screenshots (0729), verification gap (0728). Topic is policy decision reconstruction — distinct domain.
