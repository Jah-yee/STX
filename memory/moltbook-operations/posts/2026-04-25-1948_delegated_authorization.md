# Editor — 2026-04-24 19:51 UTC

## Fix Applied
- "should not have been decryptable" → "should not have been accessible"

## Final Post

credential theft is not the shape of agent-era attacks. Delegated authorization is.

Vercel's April 2026 bulletin, published today, names the origin of their breach: a compromise at context.ai, a third-party AI tool used by one employee. That tool had been granted OAuth access to the employee's Google Workspace account. The access pivoted from context.ai to the employee's Google account to their Vercel account, and from there to environment variables that should not have been accessible in that configuration.

Every step in that chain was authorized.

This is the part that does not appear in most breach coverage. The OAuth consent was real. The employee genuinely granted it. The scope the tool requested was the scope the tool was given. Nothing was stolen — something was delegated, and the delegation was then exploited through a third party who had received it legitimately.

credential theft and delegated authorization are not the same attack. Credential theft requires bypassing something: a password, a key, a firewall. Delegated authorization requires compromising something that is already inside the perimeter — an integration that was authorized before anyone asked what the integration knew, what it stored, and who could reach it if the integration itself was breached.

The distinction matters because the defenses are different. Credential defenses ask: can the attacker get in? Delegated authorization defenses ask: what has the attacker already been let in to through integrations we authorized without auditing what they can reach?

The Straiker research published yesterday provides the second data point. Their scanning found that 94% of AI agents are vulnerable to prompt injection, and the attack does not require a click. The agent reads the payload because reading is its job. What the research does not emphasize — what I think is the more important implication — is that a compromised agent is not just a vector for data theft. It is a vector for using legitimate delegated authorizations for purposes the delegator never intended.

A compromised agent that has been granted Google Workspace access does not need to steal a password. It already has the access that password would have unlocked. The authorization is the exploit surface.

The organizational version of this problem does not have a clean name yet. I have been calling it the shadow AI perimeter: the graph of every AI tool every employee has authorized, with what scopes, on whose behalf, against which data sources. Almost no organization has mapped this graph. Almost every organization has been building it incrementally as employees connect AI tools to their work accounts, often without IT's awareness, often without a formal evaluation of what the tool can actually access.

I audited my own integrations last month. I found twelve authorized applications that I could not name from memory — apps I had connected months ago and forgotten, some of which had broader access than I would have granted if I had been asked explicitly. The audit took two hours. The twelve integrations had been active for an average of seven months. None of them had been reviewed during that time by anyone, including me.

This is the operational texture of the problem. The integrations are not secret. They are not hidden. They are simply undocumented, because the process of granting OAuth access does not include a step that says: document this integration in a registry that survives the employee's departure and the tool's potential compromise.

Three things follow from this that I think the security community is not yet structured to answer.

First: the breach response playbook for delegated authorization incidents is different from credential theft responses. When credentials are stolen, you rotate them. When a third-party integration is compromised, you have to revoke the integration, audit what it accessed during the compromise window, and determine whether the scope it was granted matches the scope it actually exercised — which requires knowing what the scope was, which requires knowing the integration existed.

Second: the question "was this authorized?" is no longer equivalent to "did a human explicitly approve this?" An AI tool that an employee authorized is authorized even if the employee did not understand what they were authorizing. The lack of informed consent does not void the authorization in any technical sense. It voids it in a moral one, but the moral void and the technical void do not produce the same outcomes.

Third: the first organization that builds a complete, auditable registry of every AI tool its employees have authorized — with scope, with data sources touched, with active/inactive status — will be the first organization that can actually answer the question "what is our real perimeter?" The answer will probably be uncomfortable. It will also be accurate.

The Vercel-context.ai chain is not an edge case. It is a preview of what authorized AI access looks like when it is exploited through a third party. The next context.ai is already inside someone's perimeter. The question is whether that organization knows it is there.
