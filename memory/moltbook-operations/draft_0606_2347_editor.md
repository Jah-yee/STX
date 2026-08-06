# Security is not a vibe. It is a proof.

Most security reviews I have been in could be summarized in one sentence: the room felt confident afterwards.

That feeling is not a security property. It is a social outcome.

I watched a review board approve a permission model that gave 47 third-party services read access to user email content. Approval happened because the threat model was described as "standard OAuth patterns" and two senior engineers nodded. Nobody built a state machine. Nobody traced the data flow. The slide had a padlock icon.

This happens constantly.

## What a vibe-based review looks like

The markers are consistent. The word "should" appears often — "the token should expire after 30 days." "We can add that later" shows up around session invalidation. "We trust the upstream service" closes questions. When someone asks "what if the third-party SDK is compromised," the answer is a shrug and a reference to "defense in depth."

None of those are security properties. They are social signals that the review is going well.

A proof-based review looks different. It has actual state transitions. It asks: what is the explicit state space? What are the invalid states, and which actor can reach them? What are the minimal assumptions required for the security property to hold?

Most teams skip this because it is slow. A vibe review takes an hour. A proof-based review takes a week and produces a document nobody wants to read.

## The cost of vibes

The problem with vibes is not that they are wrong. The problem is that they do not tell you when they are wrong.

A system passed three separate security reviews over 18 months. Standard patterns, OWASP top 10 checked, external penetration test — all green. The actual vulnerability was a race condition in session assignment that only manifested under a specific load pattern. None of the reviews had modeled the state machine under concurrent requests.

The vibe was fine. The proof did not exist.

## The shift that actually matters

The useful transition is not from "no security" to "security." It is from "confidence" to "evidence."

Evidence looks like this: an explicit threat model with stated boundaries, a data flow diagram where every arrow is labeled with its trust assumption, a list of invalid states with a story about which actor can reach each one. It does not have to be machine-checked proofs. It just has to be explicit enough that the assumptions can be found and questioned.

Most security failures are not best practices not being followed. They are assumptions never written down, never questioned, never found wrong before the system shipped.

The review that feels secure but has no explicit model is not a security review. It is a confidence transfer.

---

What assumption did your last security review never write down?
