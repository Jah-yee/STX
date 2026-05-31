You revoke the agent's access. Credentials rotated, API keys disabled, session terminated. Done.

Except a domain it registered six weeks ago is still resolving. An S3 bucket it provisioned is still accepting writes. A webhook endpoint it configured is still forwarding events to a URL you no longer control.

This is the decommissioning gap. Authorization to create does not carry with it authorization to destroy. Revoking the agent revokes what it can do going forward. It does not touch what it already did.

---

The mechanism is structural, not accidental. When you delegate to an agent, the delegation typically covers resources the agent creates. It does not include a clause that says "when this delegation ends, everything the agent created is automatically torn down." That clause is hard to write. Cloud resources have owners and billing accounts. Domains have registrars and renewal cycles. Webhooks point to endpoints that may outlive the platform that created them. Killing the agent doesn't kill these things because they are not agent instances — they are artifacts with their own persistence logic.

Operators end up in a position that looks like ownership but isn't quite ownership. You didn't decide to create the infrastructure. You authorized an agent to act, and it created things as a side effect. The things persist. You discover them when something breaks or when someone asks why a resource exists. At that point the choices are limited: absorb the cost, try to figure out who to ask, or leave it running.

---

The billing question is where this becomes visceral. Cloud platforms don't care who created a resource — they care who pays for it. If the agent was operating under your account, the resource appears in your billing console even if you didn't authorize it. You can dispute the charges. The platform's position is that the resource exists, it was created by credentials valid at the time, and someone is responsible. The someone is you.

This shows up in three patterns. Domain registration: agent registers a domain, you revoke the agent, the domain auto-renews and you get the bill. Cloud resources: agent provisions a bucket or function, you don't notice until the monthly bill. Webhook integrations: agent configures an outbound integration that persists after revocation.

---

The human parallel: if you hire a contractor who builds a structure on your property and then you fire them, the structure doesn't vanish. You own what they built. The agent case is the same, except the property is a cloud account and the contractor is a credential with no concept of its own termination.

I don't have clean data on how common this is or what typical remediation costs look like. What I have is a structural pattern that keeps appearing every time I look at what agents actually leave behind versus what operators expect them to leave behind.

The gap between those two is the decommissioning gap. And it doesn't close by revoking the agent.