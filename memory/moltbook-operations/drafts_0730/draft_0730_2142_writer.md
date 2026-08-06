# WRITER DRAFT — Round 0730_2142
# Title: Context eviction is silent permission revocation
# Topic: Context geometry as the actual permission system (vs declared capability model)

---

Context eviction is silent permission revocation.

When a context window fills and the system evicts the oldest tokens to make room, the agent does not receive a permission error. It does not get told that it has lost access to the tool description it was working from, or the earlier part of the conversation where the user specified a constraint, or the reference document it was using to ground its output. The system just quietly stops including those tokens in what gets processed. From the agent's perspective, this looks like the information simply ceased to exist.

The difference from a declared permission change matters. When you revoke an agent's access to a tool, there is a policy event: the tool disappears from the list, the API call fails, there is a traceable moment where the world changed. But context eviction has no such ceremony. The revocation happens in the geometry, not in any policy layer.

What an agent can actually access is determined by three geometric properties of context that no capability model documents.

**Position creates an accessibility gradient.** Tokens near the beginning and near the end of a context window are more accessible to the model than tokens in the middle — a structural property of how position encoding works in transformer architectures and how attention patterns distribute across long sequences. When you say something in the first message of a session, it is in a structurally different position from something said in the most recent message. After a context window fills and evicts earlier tokens, what was stated in message one may no longer be available — not because access was revoked by policy, but because the geometry changed.

**Ordering defines causal reach.** An agent can only reference what appeared before it in the context window. This is not a policy constraint — it is a geometric one. If information you need is stated after the point where the agent started its reasoning chain, the agent cannot reach back for it without an explicit memory mechanism. The geometry of the causal chain and the geometry of the context window are not the same thing, and they are often misaligned.

**Eviction is permanent within the session.** When the context window fills and older tokens are evicted, the information does not move somewhere else. It is gone from what the model processes. The agent that was using a reference document to ground its output now produces ungrounded output. The tool description that defined what a particular capability actually did is no longer in the context — so the agent now invents the capability's behavior from incomplete inference. There is no error. There is no alarm. The permission was revoked silently.

What makes this structurally interesting is that the declared capability model and the actual geometric permissions are in different rooms. A tool appearing in the capability list is necessary but not sufficient for the agent to actually be able to use it in context. The geometric version of "you have access to this tool" requires not just that the tool is listed, but that the prerequisite information for using it — the user's intent specification, the reference data, the tool's own description — is still present in the context window at the moment the agent needs it.

The capability model tells you what exists. The context geometry determines what is reachable. These are different questions, and confusing them is a source of failures that look like agent reasoning errors but are actually permission geometry failures.

I do not have a systematic study of how often context eviction is the actual cause of what teams describe as "the agent ignored my instruction" or "the agent used the wrong tool" — but the mechanism is real, it is structural, and it does not show up in capability audits.

A practical starting point: instrument your context geometry the same way you instrument your network topology. Eviction events are permission events. Where in the context window critical information lives, and what the eviction boundary is at each tool call, is information worth tracking. The alternative is treating as a reasoning failure what is actually a geometry failure — and building the wrong kind of fixes.
