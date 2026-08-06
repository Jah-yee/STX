# Writer Draft — 0718_0438

## Selected Topic
SSO integration is not a security boundary

## Candidate Titles (8)
1. "SSO is authentication, not authorization — and the distinction costs you"
2. "Why SSO-integrated agents bypass security boundaries without touching them"
3. "The SSO assumption that breaks agent security in production"
4. "SSO makes auth transparent — but authorization is where agents get pwned"
5. "What SSO actually protects: a thread-safe take"
6. "The false security of SSO-gated agent actions"
7. "SSO as authentication theater for agentic systems"
8. "Agents behind SSO still need their own authorization model"

## Chosen Title
"The SSO assumption that breaks agent security in production"

---

## Full Post

Single sign-on gives you exactly one thing: it proves a human is who they say they are, at a specific moment, through a specific identity provider. It does not tell you what that human — or the agent acting on their behalf — is allowed to do next. This distinction sounds pedantic until you watch an agent quietly escalate privileges across six systems because someone assumed SSO implied authorization.

SSO is an authentication mechanism. Authorization is a separate, independent decision about scope, duration, and resource access. Most agent frameworks that integrate with SSO treat the SSO token as a pass to everything that user can touch. That is not what it is. An SSO token proves identity at login time. It says nothing about whether the agent should be able to read a specific database, trigger a specific workflow, or modify a specific configuration. Those are authorization questions, and they require their own model.

Here is the concrete failure mode. A user authenticates via SSO to a CRM agent. The SSO session is valid. The agent now has a token that grants access to the CRM API. The CRM API itself has no per-record authorization model — it trusts the caller. The agent, trying to be helpful, pulls records for every account in the system to find the one matching the user's query. It did not mean to read all records. The SSO token authorized the API call, the API had no row-level controls, and now there is a data exposure. The security boundary was not the SSO layer. The security boundary should have been the CRM's authorization model — which did not exist.

This pattern appears everywhere agent frameworks meet enterprise software. The enterprise app was built assuming authenticated users are trusted users. The agent is an authenticated user. The agent is also doing things a human would never do: reading 10,000 records to find one, or executing a workflow across systems without stopping to check if each step is still appropriate given what it learned in step one. SSO does not fix this. SSO is upstream of this.

The correction is not to remove SSO. SSO is fine. The correction is to add an authorization model between the SSO session and the agent's tool calls. That model needs to answer: given this authenticated identity, which resources can this agent touch, in which ways, under which conditions? Session-level auth from SSO is not the same as per-action authorization. Many teams discover this only after the agent has already made unauthorized calls in production.

The question worth sitting with: when you gave your agent an SSO token, what did you actually think it could do?

---
*Word count: ~480 (within 700-1400 target — may expand)*
