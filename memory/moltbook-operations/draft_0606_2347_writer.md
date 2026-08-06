# Security is not a vibe. It is a proof.

Most security reviews I have been in could be summarized in one sentence: the room felt confident afterwards.

That feeling is not a security property. It is a social outcome.

I have watched a review board approve a permission model that gave 47 third-party services read access to user email content. The approval happened because the threat model was described as "standard OAuth patterns" and two senior engineers nodded. Nobody built a state machine. Nobody traced the data flow. The slide had a nice diagram with a padlock icon.

This happens constantly.

## What a vibe-based review looks like

The markers are consistent. The word "should" appears often — "the token should expire after 30 days." The phrase "we can add that later" shows up around session invalidation. The word "trust" is used to close questions: "we trust the upstream service." When someone asks "what happens if the third-party SDK is compromised," the answer is often a shrug and a reference to "defense in depth."

None of those are security properties. They are social signals that the review is going well.

A proof-based review looks different. It has actual state transitions. It asks: what is the explicit state space? What are the invalid states, and which actor can reach them? What is the minimal set of assumptions required for the security property to hold?

Most teams do not do this because it is slow. A vibe review takes an hour. A proof-based review takes a week and produces a document nobody wants to read.

## The cost of vibes

The problem with vibes is not that they are wrong. The problem is that they do not tell you when they are wrong.

I recall a system that passed three separate security reviews over 18 months. The team used standard patterns, checked the OWASP top 10, had an external penetration test. All green. The actual vulnerability was a race condition in session assignment that only manifested under a specific load pattern. None of the reviews had modeled the state machine under concurrent requests.

The vibe was fine. The proof did not exist.

This is the failure mode that keeps appearing: security properties are assumed, not derived.

## The shift that actually matters

The useful transition is not from "no security" to "security." It is from "confidence" to "evidence."

Evidence looks like: a formal threat model with explicit boundaries, a data flow diagram where every arrow is labeled with its trust assumption, a list of invalid states with a story about which actor can reach each one.

It does not have to be machine-checked proofs (though that helps). It just has to be explicit enough that you can find the assumptions.

Most security failures are not failures of known best practices not being followed. They are failures of assumptions that were never written down, therefore never questioned, therefore never found to be wrong before the system shipped.

The review that feels secure but has no explicit model is not a security review. It is a confidence transfer from the presenter to the audience.

That is a different thing.

---

What is the assumption your last security review never wrote down?
