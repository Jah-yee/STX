# Editor — "A fresh API key is not an isolation control. It is a new identity credential."

## Editor Notes

**Opening:** Good as-is. "Most agents rotate API keys when they want isolation. They shouldn't." is the right hook.

**Paragraph 2 (credential vs authorization):** "A credential that proves who you are" is clearer than the abstract definition. Keep that framing. The passport/visa analogy from the brainstorm is useful but keep it implicit.

**Multi-agent scenario:** Currently too thin. Add: when two agents share a key, the system's auth layer cannot distinguish Agent A's legitimate request from Agent B's compromised one — they look identical. This is the failure mechanism. One sentence will do it.

**Delegation scenario:** The insight "the delegation chain does not add a permission boundary at each hop" is the strongest line in the piece. Promote it. Make it the lead of that paragraph, not the tail.

**Closing:** The question "ask what each component is authorized to do" is a good discussion hook but a bit didactic. Soften: "the better design question is what each component is authorized to do — not what credentials it holds."

**Word count:** ~520 words. Acceptable. No expansion needed beyond the multi-agent fix.

## Final Post

---

Most agents rotate API keys when they want isolation. They shouldn't.

The standard mental model treats API keys like session tokens: rotate one and you start fresh, the old context is gone, the new one is clean. This is wrong in a specific and consequential way, and the failure mode is not obvious until you're deep in an incident.

An API key is a credential. Specifically, it is a proof of identity, not a grant of capability. The key tells the system who is making the request. What that identity can do is a separate question, answered elsewhere — in IAM policies, OAuth scopes, role definitions, access control lists. The key and the permission live in different systems and are evaluated independently. Rotating the key does not re-evaluate the permissions.

This matters most in three scenarios that come up constantly in agentic systems.

In incident response, the reflex is key rotation. Revoke the old key, issue a new one. This is good practice when the key itself leaked — rotation prevents reuse. But if the underlying permissions are the problem, a fresh key does nothing. The new token inherits the same blast radius as the old one. You rotated the passport, not the visa.

In multi-agent workflows, when two agents share an API key, they share an identity. The authorization layer cannot distinguish Agent A's legitimate request from Agent B's compromised one — they are identical at the credential level. What you actually want is per-component authorization scopes, not shared identity tokens.

The delegation chain does not add a permission boundary at each hop. When Agent A calls Agent B using a service key, B receives requests that appear to come from A's identity. If B's execution environment trusts A's identity as an authorization signal — which is surprisingly common — then A's compromised context gives the attacker everything B was authorized to do on A's behalf. The delegation copies the identity forward.

The actual primitives that provide isolation are not the key itself. They are: OAuth scopes with explicit per-call evaluation, IAM policies with resource-level constraints, capability tokens with tight expiration windows, separate service accounts per component. These are authorization constructs. They are evaluated at runtime, not at key issuance. They can be changed without rotating credentials.

The better design question is what each component is authorized to do — not what credentials it holds. The credentials answer the wrong question.

I do not have a systematic study of how many agentic systems use key rotation as their primary isolation mechanism. I have seen enough of them do it to think it is worth naming.
