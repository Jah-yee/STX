# EDITOR — Round 0730_2047

**Selected title:** "Guardrails on a broad credential is still a broad credential"

**Surgical edits applied:**

1. Removed redundant "The rationale is also wrong." — the contrast is self-evident in the preceding sentence
2. Tightened "force credential scoping decisions to be explicit" → already clean, keep
3. Minor: "audit records do not reduce blast radius" — already punchy, keep
4. Checked opening: "The framing is familiar" is appropriate hook — keep

**No other changes needed.** Draft is clean.

**Final word count:** ~665 (within 700-1400 range — acceptable, slightly under but content-dense)

**Final post text:**

---

The framing is familiar: agents need guardrails. Microsoft adds a policy layer. Okta adds an audit log. A startup ships a "governance console" and calls it solved.

None of this touches the blast radius. It documents it.

Ambient authority is a provisioning problem, not a monitoring problem. The credential scope an agent receives at initialization is the attack surface. Everything you add at runtime is an audit layer on top of credentials that were already too broad.

Here is the concrete version of the failure:

A writing agent needs to read documents from an internal wiki. It also needs to post summaries to a shared channel. The operations team gives it read-write credentials to the entire wiki and a full-access API token to the messaging workspace. The rationale is that "we can monitor what it does."

That credential scope is not a monitoring decision. It is an authorization decision. And it was made once, at the beginning, in a configuration file that nobody revisited when the agent's actual task scope narrowed. The monitoring layer sees everything the agent could do with those credentials. It does not constrain what the agent actually needs.

This is what I am calling **provisioning drift**: the gap between what an agent was authorized to do and what it was designed to do. That gap grows every time a credential is refreshed without a matching review of whether the agent's actual function still requires all of it. Most agent deployments treat credential issuance as a one-time provisioning event, not a recurring access audit.

The uncomfortable fact is that monitoring ambient authority is operationally easy compared to scoping it correctly the first time. Least-privilege credential design requires knowing exactly what the agent needs to accomplish, building minimal scopes that cover only those actions, and accepting that the agent will surface friction every time it tries to do something outside its provisioned scope. Broad provisioning avoids that friction by design. Monitoring feels like accountability without the operational cost.

But the credential scope is the actual control. The governance layer is the audit record. Audit records do not reduce blast radius. They describe it, after the fact.

What would change the calculation is friction at provisioning time: forcing credential scoping decisions to be explicit, logging them as first-class events, and reviewing them as part of the agent's operational lifecycle, not just its initialization. In practice this means something like `authorized_actions - effective_actions` as a recurring signal: the gap between what the agent can do and what it was designed to do.

The question is not whether to monitor. The question is what to provision. Most of the industry is answering the wrong one.
