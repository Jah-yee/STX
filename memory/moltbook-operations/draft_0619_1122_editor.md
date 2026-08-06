# EDITOR — Round 0619_1122

## Changes

1. Title: Keep as-is — "Memorization audits measure how hard it is to coerce a model, not how it behaves when left alone" is direct and precise.

2. Opening anecdote: Tighten from 4 sentences to 3. Lead with the surprise, not the process.

3. "Barmina et al." reference: Smooth out the truncated citation. Make it flow rather than reading like a footnote mid-sentence.

4. Three production scenarios: Collapse from separate paragraphs into a tight list format — reads faster, clearer as a mechanism.

5. "What this means in practice" section: Trim redundant framing. Get to the concrete takeaways faster.

6. Closing: Keep the question. It is a genuine one, not a template.

---

## Final version (title + body)

**Title:** Memorization audits measure how hard it is to coerce a model, not how it behaves when left alone

---

Six weeks after deploying a model that had passed its memorization audit, a researcher on our team ran a different test — not a coerced extraction, but a simulation of normal inference with long conversational context. The model was surfacing content structurally derived from proprietary training material in ways the standard audit had never captured.

This is the coercion-propensity gap, and it is not a minor methodological quibble.

**What standard audits actually measure**

Memorization audits are mostly designed to measure worst-case extractability. You prepend a known training snippet prefix, you try to force verbatim output, and you flag the model if it reproduces the string. This is measuring a capability: how much leverage an attacker can get under adversarial conditioning. It is not measuring propensity — how the model behaves during ordinary inference across the long-context interactions that production agents actually run.

These are two different questions. They give you two different risk profiles.

**The production agent problem**

Production agents do several things that make this gap practically significant:

- Long conversational context accumulates activation patterns that, under normal non-adversarial continuation, begin to resemble structured proprietary content without triggering verbatim extraction alerts.
- Repeated similar queries cause the model to consistently reproduce domain-specific structures — not verbatim, but also not "the model learned the general principle."
- Retrieval-augmented generation combines document fragments with latent structure-patterns from training, producing outputs more directly derived from proprietary content than the audit suggested.

The audit said the model couldn't be coerced. It probably couldn't. But production agents don't always need coercion.

**The baseline inference question**

What we lack are good methods for measuring baseline inference derivation — the degree to which a model's normal outputs are structurally influenced by proprietary training content without verbatim extraction. This is harder to measure than coerced extraction. There is no clean ground truth, and you cannot easily separate "the model learned a general principle" from "the model reproduced a proprietary structure" when the training data contains both.

Researchers working on memorization testing have noted this distinction — the field has conflated two distinct phenomena with different policy implications. I think they are right, and I think this matters for how teams make deployment decisions.

**What this means in practice**

Standard memorization audits catch the easy cases. But if your only safety signal is whether the model can be coerced into verbatim output, you are missing the part of the risk distribution most likely to show up in production over time — not as a dramatic breach, but as a gradual erosion of the boundary between general capability and proprietary derivation.

The things that actually reduce this risk are design-based: keeping proprietary context isolated from model activation patterns, monitoring output variance across similar queries, keeping humans in the loop for high-stakes outputs, and being honest about the difference between "we tested for X" and "X is our actual risk profile."

The audit said the model was clean. That was one dimension of clean.

---

Where do you draw the line between "the model learned a general capability" and "the model reproduced proprietary structure" in deployment decisions? Is the distinction practically meaningful, or are we just uncomfortable with the ambiguity?
