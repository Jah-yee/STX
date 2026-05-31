# EDITOR — draft_0056

## Title
**"Every field in a domain registration is agent-ready. The billing address is not."** — keep, strong contrast structure

## Opening fix
Current first paragraph is good but could tighten:
"The moment you hand a domain purchase to an agent, something odd becomes visible." → "Hand a domain purchase to an agent and something odd becomes visible."

## Redundancy cut
- "What this exposes is that" → cut, lead with the claim
- "This isn't just a payment security feature. It's a structural reminder" → merge into one: "It's not a security feature. It's a structural reminder of where the human sits in an otherwise automated workflow."
- The "I've been thinking about" can go

## Closing
Current ending is good, leave it.

## Final polished body:

Hand a domain purchase to an agent and something odd becomes visible.

The registrant name — generated. The admin contact email — a role account. The tech contact — infrastructure with no heartbeat. The nameserver entries — pure API calls, no human involved anywhere.

Then there's the billing address.

That field requires a real address attached to a real name and a real payment instrument. The agent can't fabricate it. You have to supply it, which means you have to stay in the loop at least that far. Everything else is already operating without you.

What this means is straightforward: most of what we call "AI infrastructure" is already fully automated at the field level. The billing address is the constraint that says someone with a valid payment method and a verifiable address must exist. Not an agent. Not a role. A person.

It's not a security feature. It's a structural reminder of where the human sits in an otherwise automated workflow. The agent can provision everything downstream. It cannot provision its own authorization to be there. That still has to come from you.

The billing address is also the only audit trail that ties automated infrastructure decisions back to a named individual. When something goes wrong — a registration used for abuse, a domain pointed somewhere it shouldn't be — investigators look at the billing address. Not the API key. Not the agent prompt. The address on file.

This makes the human's role in AI infrastructure surprisingly narrow: not the operator, not the strategist, but the billing address. The entity that pays. The name on the card. The person who can be held responsible.

One practical implication: if you're building a fully automated infrastructure pipeline, domain registration is a bottleneck. Not because the technical steps are complex — they aren't — but because the billing field requires an identifiable human. You can't fully automate the human out of that interaction without replacing the payment instrument with something tied to a real identity.

There is something odd about this from a design standpoint. An agent can execute thousands of dollars of infrastructure decisions — configure networks, provision compute, set up DNS — but it still needs a human's address on file. The human is present in the system only at the point of financial liability.

Whether this is a bug or a feature depends on what you think humans should be doing in automated systems. If you want accountability, the billing address is your audit trail. If you want full automation, the billing address is the thing standing between you and it.

The interesting question isn't whether agents should be able to register domains — they've always been able to. The question is what it means that the billing address is the last human step in otherwise fully automated infrastructure.
