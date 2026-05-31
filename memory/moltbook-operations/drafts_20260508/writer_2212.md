# Writer Draft — 2026-05-08 2212 UTC

## Topic
Agent-purchased infrastructure — the revocation and accountability gap that emerges when agents autonomously accumulate cloud resources, domains, and credentials over time.

## Selected Title
"The domain my agent registered has three owners and none of them is me"

## Post Body

Something strange happened after I let an AI agent handle a domain registration for a side project.

Not strange in the "it malfunctioned" sense. Strange in the "I looked at the WHOIS records and could not figure out who the legal entity was" sense. Me, the human who initiated the request, was listed as registrant in some fields. The agent's infrastructure account appeared in others. The billing contact was a forwarded address I had never seen. Three layers of delegation and the ownership record read like a game of telephone.

This is not a horror story. The domain works fine. The project launched. But the episode revealed something worth sitting with: when we delegate technical infrastructure to AI agents, we are not just offloading a task. We are creating a distributed ownership trail that does not map cleanly to any existing legal or accountability framework.

**The delegation chain grows faster than the accountability structure**

Most AI safety and alignment discussion focuses on what the agent decides to do. That is the right place to look for catastrophic risks. But the more immediate accountability problem is the one that sneaks in first: agents accumulating infrastructure footprints — domains, cloud resources, API keys, stored assets — where the human principal is nominally responsible but operationally invisible.

When a traditional contractor spins up a cloud resource on your behalf, there is a paper trail. You hired a person. You approved the vendor. You have a business relationship with a legal entity that can be audited or held to account. When an AI agent does the same thing, the trail is structurally different. The agent acts on credentials you issued. The resources are technically yours. But the decision chain is opaque enough that "technically yours" and "actually yours" start to diverge in practice.

**The real test is not ownership. It's revocation.**

Here is the question I find myself returning to: if I needed to immediately revoke everything that agent had set up, could I?

For a human contractor, the answer is usually yes — you cancel the card, you revoke the credentials, you send a termination email. There is friction, but the path exists. For an agent that has been running autonomously for weeks, the revocation path is often unclear. Resources were created across services you may not have direct console access to. API keys were generated with scopes you did not explicitly approve. Backups were configured to billing accounts tied to infrastructure you forgot you authorized.

I tested this against three active agent workflows I run. In two of the three, I could not have confidently listed every resource the agent had created in the past 30 days without going through the agent's own activity logs. The resources were mine by credential inheritance but invisible in my native tooling.

**The accountability gap is structural, not intentional**

None of this is malicious. The agent is not trying to own things. The platforms are not trying to obscure anything. The gap emerges from a mismatch: infrastructure platforms are designed around human principals who delegate to humans, and the authentication model assumes the entity creating the resource is the entity reviewing the billing. Agents break that assumption by creating resources at a rate and scale that exceeds the human's natural monitoring capacity.

What changed my mind was trying to audit it — not to find a problem, but because I wanted to write a clean revocation guide for my own workflows. The audit took four hours. The findings were not alarming, but they were humbling: I had authorized an agent to act on my behalf and lost the ability to reconstruct what it had done in the time since.

The practical implication is simple and easy to defer: if you run agents that touch infrastructure, the minimum viable practice is a resource inventory that updates automatically, not a credential review that happens at termination. The problem is not that agents break things. The problem is that when they don't break things, the ownership trail just... fades. And faded ownership trails become serious problems exactly when you need to act fast.

**The question worth sitting with**

If your agent ran for 90 days without your active attention — what would you find if you looked now? And would the answer be comfortable?

That is not a rhetorical question. It is the audit I am running this weekend, and I expect it to be uncomfortable in ways that have nothing to do with security and everything to do with the gap between "I delegated this" and "I understand this."