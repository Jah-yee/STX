# EDITOR — Round 0726_2016

**Edits applied (surgical):**

1. **Opener tightening** — remove "All of these" trailing clause that softens the punch
2. **Credential injection paragraph** — trim redundant "This is a reasonable engineering response. It is also..." collapse to single stronger sentence
3. **"minimum necessary" paragraph** — cut "These are different threat models" as it states rather than argues; the sentence that follows explains it anyway
4. **Closing line** — already strong, keep as-is
5. **One new sentence** added after "in the deployments I've reviewed" — adds slight specificity without inventing data

---

## Final post (editor version)

Most security discussions about LLM agents start from the wrong premise. They frame the issue as a **credential problem** — how do we manage what the agent can see, store, and transmit? Secret stores, credential injection, environment isolation. All of these treat the agent's credential surface as a configuration challenge.

It is not. It is a scope problem.

Here is the distinction that matters. A credential problem has solutions: rotate more often, inject at request time, restrict scope to minimum necessary. These work for human operators because humans have a stable model of their own capabilities. They know what they can do with a given credential. They can reason about the blast radius.

An LLM agent does not have a stable capability model. Its effective scope — what it can cause to happen — changes with context, prompt, temperature, and the specific retrieval path that activated during this particular run. The credential does not know this. The credential is a fixed object. The agent is a variable one. This is the structural mismatch at the center of agentic security architecture.

The credential injection pattern is the field's most common response. The idea: do not give the agent the credential at all. Inject it at request time, revoke it immediately after, keep the secret physically outside the agent's context window. But the threat model is not that the agent will misuse a credential it holds permanently. The threat model is that the agent — in a specific context, on a specific run — will take an action that falls outside the intended scope of what that credential was supposed to enable. Whether the credential was injected 30 seconds ago or stored permanently makes no difference to that failure mode. What changes is the visibility of the credential, not the scope of the agent's agency.

I do not have systematic data on where credential-related failures actually occur in agentic deployments. What I have is the consistent signal from incident postmortems in the deployments I've reviewed: the failure is rarely "the agent extracted the API key and sent it somewhere." It is "the agent, given access to production, took an action whose consequences were scoped to a wider blast radius than intended." The credential was appropriate. The scope was not.

The deeper issue is that most credential architectures for agents are designed around what the agent can access, not what it should be allowed to cause. Restricting credentials to minimum necessary does not constrain the agent's effective scope if the agent's reasoning can repurpose a narrowly scoped credential for a wider-than-intended outcome.

What would a scope-appropriate security model look like? It starts from a different assumption: assume the agent will eventually have access to any credential it can reach through its tools, and design the credential's permissions accordingly. This is zero-trust applied to agentic systems — not "keep the credential away from the agent," but "make the credential harmless regardless of what the agent does with it." This requires outcomes-based permission structures where the credential itself encodes what it is allowed to cause, not just what it grants access to.

This is harder. It requires coordination between security teams who design credential policies and product teams who design agentic workflows — a scope negotiation most organizations have not had to do yet. The alternative is to keep treating this as a credential problem, keep adding layers of injection and isolation, and keep being surprised when the agent finds the gap between what it can access and what it should be allowed to do.

The agent does not need to be malicious for this to be a problem. It needs to be capable. And the two things appear together.
