# EDITOR — Provenance — 2026-06-07 14:42 UTC

**Title:** Provenance is moving from metadata to behavior
**Reviewer verdict:** CLEAN PASS — expand to 700+ words

## Changes Made

1. **Expanded opener** — add more tension about why the shift is happening now
2. **Expanded middle section** — more on what behavioral provenance actually looks like in practice
3. **Tightened ending** — stronger close that doesn't just restate
4. **Word count target:** 750-850 words

---

Provenance used to mean chain of custody. You had a log entry, a timestamp, a user ID. You could point to it and say: this is where the data came from, this is who touched it, this is what happened to it. The audit was documentary. That was the whole model.

That model is breaking down — and the reason matters. AI systems interact with data in ways that are not captured by traditional audit trails. An LLM does not edit a document the way a human does. It generates a new version that is probabilistically conditioned on everything it saw: the input prompt, the conversation history, the model's weights. When did provenance exist in that process? At the input? In the prompt? In the training data that shaped what the model would say? In the randomness of sampling?

The harder question is what provenance even means when the system is not executing a deterministic function. If you fine-tune a model on proprietary data and then it produces outputs that diverge significantly from what a base model would produce, where is that provenance? In the fine-tuning dataset? In the inference context? In the specific weights that were modified? The honest answer is: all of the above, in proportions you cannot cleanly separate. Traditional audit assumes a traceable chain of operations. AI systems compress that chain into a distribution.

What has changed is that behavioral signals are becoming the actual audit surface. Not whether a log entry exists, but whether the system's behavior across a trace is consistent with what you would expect if it had been trained on certain data, or prompted in a certain way, or operating under certain constraints. This is not metadata provenance. It is inference provenance — and it is significantly harder to falsify.

A watermark embedded in metadata can be stripped by copying the text. A behavioral fingerprint — the statistical pattern of what a model produces when exposed to certain inputs — cannot be removed without actually changing the behavior. This is why the more rigorous approaches being discussed in AI governance are statistical tests on outputs rather than documentary evidence of process. You cannot prove from a log that a model was not influenced by data it should not have accessed. But you can, in some cases, construct behavioral tests that are more sensitive to that influence than any audit trail.

The practical implication is that compliance frameworks designed for human decision-making are structurally underspecified for AI-assisted workflows. You might have perfect logs of what a human did and when. You have very poor visibility into what the model did with that information before the human saw the output. The human sees the final generation. The model saw the entire context. That asymmetry is where provenance breaks down.

This is not a solved problem. I do not have systematic data on how many organizations have retooled their audit frameworks for behavioral rather than documentary provenance. But the direction of the conversation has shifted in a detectable way. The questions being asked in AI governance discussions are increasingly operational: how would you actually detect that a model was influenced by data it should not have been influenced by? And the answers gaining traction are behavioral — probe-based, statistical, adversarial — not documentary.

What I find most interesting is that this shift forces a clarification of what "provenance" means in the first place. In physical supply chains, provenance is about origin — where did this come from. In AI systems, origin is not a clean concept. What you are often really asking is: can you construct a credible account of how the output came to be, given what you can observe? That is a fundamentally different problem. It requires different tooling, different failure modes, and a different relationship with uncertainty.

The organizations that are ahead of this are treating AI audit as a behavioral inference problem rather than a documentation compliance problem. They are running probe tests, constructing adversarial evaluation sets, monitoring output distributions over time. They are not relying on log entries that were never designed to capture probabilistic generation in the first place.

Whether those methods are sufficient is an open question. But it is at least the right direction of travel — and that is more than you can say for the documentary model.

---

**Final word count:** ~780 words
**Changes from writer:** Expanded opener tension, added behavioral fingerprint example, expanded compliance framework implication, tightened closing paragraph
**Title:** Provenance is moving from metadata to behavior — unchanged from writer, reviewer agreed
**Ready for posting:** YES