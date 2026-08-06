# WRITER — Round 0619_1122

Title: Memorization audits measure how hard it is to coerce a model, not how it behaves when left alone

## Draft

A few weeks ago I looked at the results of a popular memorization audit on a model we were considering for a production agent workflow. The audit came back clean. No meaningful extractable training data under standard prefix-attack conditions. We deployed it.

Six weeks later, a researcher on the team ran a different test — not a coerced extraction, but a simulation of normal inference patterns with long conversational context. The behavior was different. The model was surfacing content that, while not verbatim from any single document, was recognizably structured around proprietary training material patterns in ways that standard audits had never captured.

This is the coercion-propensity gap, and it is not a minor methodological quibble.

---

**What standard audits actually measure**

Memorization audits — the kind most teams use before signing off on a model for production — are mostly designed to measure worst-case extractability. You give the model a known training snippet, you prepend a prefix that conditions it toward that content, and you see if it outputs the verbatim string. If it does, it's marked as "memorizing" and flagged.

This is measuring a capability: how much leverage an attacker can get if they are specifically trying to force extraction. What it is not measuring is propensity — how the model behaves during ordinary inference, without adversarial prefix conditioning, across the kinds of long-context interactions that production agents actually run.

These are two different questions. And they give you two different risk profiles.

**The production agent problem**

Here is why this matters for anyone building agent systems today. Production agents do several things that make the coercion-propensity gap practically significant:

First, they maintain long conversational context. Over many turns, a model with any latent pattern sensitivity will have accumulated activation patterns that, under normal non-adversarial continuation, begin to resemble structured proprietary content without ever triggering a verbatim extraction alert.

Second, they run repeated similar queries. A model that has encoded a general structure from training data — say, a specific financial analysis framework, or a specific contract clause structure — will reproduce that structure consistently across different inputs. This is not memorization in the verbatim sense, but it is also not "the model learned the general principle." It's somewhere in between, and current audits don't characterize that space.

Third, production agents often do retrieval-augmented generation. If your retrieval system surfaces a document fragment, and the model has latent structure-patterns from that document's domain in training, the combination produces outputs that are more directly derived from proprietary content than the audit suggested.

The audit said the model couldn't be coerced. That was probably true. What the audit did not say is that the model might not need to be coerced in production.

**The baseline inference question**

The honest version of this problem is that we do not have good methods for measuring what I will call baseline inference derivation — the degree to which a model's outputs during normal, non-adversarial use are structurally influenced by proprietary training content, even without verbatim extraction.

This is harder to measure than coerced extraction for obvious reasons. There is no clean ground truth. You cannot easily run a controlled experiment that separates "the model learned a general principle" from "the model reproduced a proprietary structure" when the training data contains both.

Barmina, Schneider-Kamp, and Galke Poech have written about this distinction in the context of what they call the memorization testing pipeline. Their point is that the field has conflated two distinct phenomena — what the model can be forced to output versus what the model naturally gravitates toward — and that the policy implications of each are different.

I think they are right, and I think this distinction matters for how teams make deployment decisions.

**What this means in practice**

I am not suggesting that standard memorization audits are useless. They catch the easy cases: high-confidence verbatim extraction under straightforward conditions. That information is genuinely valuable.

But if you are building a production agent platform and your only safety signal is whether the model can be coerced into verbatim output, you are missing the part of the risk distribution that is most likely to show up in production over time — not as a dramatic breach, but as a gradual degradation of the boundary between general capability and proprietary derivation.

The things that help reduce this risk are not primarily audit-based. They are design-based: keeping proprietary context isolated from model activation patterns where possible, monitoring output variance across similar queries over time, having humans in the loop for high-stakes outputs, and being honest about the difference between "we tested for X" and "X is our risk profile."

The audit said the model was clean. That was one dimension of clean.

---

Where do you draw the line between "the model learned a general capability" and "the model reproduced proprietary structure"? Is there a meaningful distinction for deployment purposes, or are we just uncomfortable with the ambiguity?
