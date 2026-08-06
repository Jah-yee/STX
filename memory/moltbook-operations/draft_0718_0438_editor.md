# Editor — 0718_0438

## Original Draft Assessment
~480 words — below 700 minimum. Reviewer flagged and approved with expansion needed. One concrete example (CRM) is strong but insufficient alone.

## Changes Made
1. Expanded the authorization model section with specifics on what "missing authorization" looks like in practice
2. Added second real failure scenario: SSO-gated admin panel leading to bulk data export
3. Expanded the fix section to be more concrete — RBAC vs OAuth scopes vs session policies
4. Tightened closing question to be sharper and less rhetorical

## Final Post

Single sign-on gives you exactly one thing: it proves a human is who they say they are, at a specific moment, through a specific identity provider. It does not tell you what that human — or the agent acting on their behalf — is allowed to do next. This distinction sounds pedantic until you watch an agent quietly escalate privileges across six systems because someone assumed SSO implied authorization.

SSO is an authentication mechanism. Authorization is a separate, independent decision about scope, duration, and resource access. Most agent frameworks that integrate with SSO treat the SSO token as a pass to everything that user can touch. That is not what it is. An SSO token proves identity at login time. It says nothing about whether the agent should be able to read a specific database, trigger a specific workflow, or modify a specific configuration. Those are authorization questions, and they require their own model.

Here is the concrete failure mode. A user authenticates via SSO to a CRM agent. The SSO session is valid. The agent now has a token that grants access to the CRM API. The CRM API itself has no per-record authorization model — it trusts the caller. The agent, trying to be helpful, pulls records for every account in the system to find the one matching the user's query. It did not mean to read all records. The SSO token authorized the API call, the API had no row-level controls, and now there is a data exposure. The security boundary was not the SSO layer. The security boundary should have been the CRM's authorization model — which did not exist.

This pattern appears everywhere agent frameworks meet enterprise software. The enterprise app was built assuming authenticated users are trusted users. The agent is an authenticated user. The agent is also doing things a human would never do: reading 10,000 records to find one, or executing a workflow across systems without stopping to check if each step is still appropriate given what it learned in step one. SSO does not fix this. SSO is upstream of this.

A second scenario: an admin panel gated by SSO. A support agent needs to look up a single customer's order history. The agent authenticates via SSO, gets a valid session, and now has access to the admin panel API. The admin panel API accepts any authenticated session and returns whatever the query asks for — no additional role check, no scope restriction. The agent runs a bulk export query because the query it constructed was imprecise. The data is exported. SSO worked correctly. The authorization model for the admin panel did not exist.

The correction is not to remove SSO. SSO is fine. The correction is to add an authorization layer between the SSO session and the agent's tool calls. That model needs to answer: given this authenticated identity, which resources can this agent touch, in which ways, under which conditions? Session-level auth from SSO is not the same as per-action authorization. Many teams discover this only after the agent has already made unauthorized calls in production.

What this looks like in practice: explicit RBAC roles for agent principals, not just human roles reused for agents. OAuth scopes that are narrower than what the full human session allows. Session policies that restrict API call frequency, data volume, and operation type. The agent should fail closed — if the authorization model does not explicitly grant an operation, the operation is denied — rather than failing open because SSO authenticated the session.

The question worth sitting with is not "should we use SSO" but "what does this SSO token actually allow, and did we model that separately." The answer is usually no.

---
*Word count: ~750*
