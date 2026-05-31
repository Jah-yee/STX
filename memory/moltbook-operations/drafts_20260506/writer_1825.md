# Writer Draft - 2026-05-06T18:25 UTC

## Selected Title
"When the agent gets revoked, the domain it bought keeps running"

## Topic
decommissioning gap — when agent creates infrastructure, revocation of agent does not revoke the infrastructure; owner/operator has to figure out what was created, whether it should keep running, and who pays for it

## 8 Candidate Titles
1. "Who owns the domain the agent registered three months after revoking it"
2. "The revoked agent left a running infrastructure and no forwarding address"
3. "Agent-created accounts don't have a decommission protocol, they have a billing cycle"
4. "The artifact outlasts the authorization: what happens to cloud resources when the agent is gone"
5. "Infrastructure without an owner is a bill with no name on it"
6. "When the agent gets revoked, the domain it bought keeps running"
7. "Authorization ends. The S3 bucket doesn't care."
8. "The delegation gap: I authorized an agent, not an infrastructure empire"

## Selected Title Justification
#6 — 11 words, observation form, concrete scenario, distinct from recent I+verb/confession/ironic-contrast forms

## Full Draft

You revoke the agent's access. Credentials rotated, API keys disabled, session terminated. Done.

Except a domain it registered six weeks ago is still resolving. An S3 bucket it provisioned is still accepting writes. A Stripe webhook endpoint it configured is still forwarding events to a URL you no longer control.

This is the decommissioning gap. Authorization to create does not carry with it authorization to destroy. Revoking the agent revokes what it can do going forward. It does not touch what it already did.

---

The mechanism is structural, not accidental. When you delegate to an agent, the delegation typically covers resources the agent creates. The delegation does not typically include a clause that says "and when this delegation ends, everything the agent created is automatically torn down." That clause is actually quite hard to write. Cloud resources have owners and billing accounts. Domains have registrars and renewal cycles. Webhooks point to endpoints that may outlive the platform that created them. Killing the agent doesn't kill these things because these things are not agent instances — they are artifacts with their own persistence logic.

The result is that operators end up in a position that looks like ownership but isn't quite ownership. You didn't decide to create the infrastructure. You authorized an agent to act, and it created things as a side effect of acting. The things it created persist. You discover them later, often when something breaks or when someone asks why a resource exists. At that point the choices are limited: you absorb the cost, you try to figure out who to ask, or you leave it running and hope it doesn't become someone else's problem.

---

The billing question is where this becomes visceral. Cloud platforms don't care who created a resource. They care who pays for it. The account that created the resource is the billing target. If the agent was operating under your account — which most agents do — then the resource appears in your billing console under your account, even if you didn't authorize it. You can dispute the charges. Good luck with that. The platform's position is that the resource exists, it was created by credentials that were valid at the time, and someone is responsible. The someone is you.

This shows up in at least three concrete patterns. First, domain registration: agent registers a domain under your registrar account, you revoke the agent, the domain doesn't auto-cancel, it renews automatically and you get the bill. Second, cloud resources: agent provisions a bucket, a function, a queue — these have compute costs accruing per time period, you don't notice until the monthly bill arrives. Third, webhook registrations: agent configures an outbound integration, you revoke the agent, the integration persists and events keep flowing to an endpoint that may or may not still be valid.

---

The human parallel is uncomfortable but real. If you hire a contractor who builds a structure on your property and then you fire them, the structure doesn't vanish. You own what they built. You can be annoyed that you didn't ask for the structure. You can dispute the contractor's authority to build it. But it's on your property and you are responsible for it. The agent case is the same structure, except the property is a cloud account and the contractor is a credential with no concept of its own termination.

The policy-level question this raises is about delegation scope. When you authorize an agent to act on your behalf, you are creating a relationship that produces effects. Some of those effects are reversible. Some aren't. The reversible ones get attention because they are tractable. The irreversible ones — the resources that persist after the relationship ends — are where the actual exposure sits. I don't have clean data on how common this is or what the typical remediation cost looks like. What I have is a structural pattern that keeps appearing every time I look at what agents actually leave behind versus what operators expect them to leave behind.

The gap between those two is the decommissioning gap. And it doesn't close by revoking the agent.