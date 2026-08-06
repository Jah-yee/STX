# WRITER — Provenance — 2026-06-07 14:35 UTC

**Title:** Provenance is moving from metadata to behavior

**Style:** Technical breakdown / industry take

---

Provenance used to mean chain of custody. You had a log entry, a timestamp, a user ID. You could point to it and say: this is where the data came from, this is who touched it, this is what happened to it. The audit was documentary.

That model is breaking down, and it is not because the logs got worse. It is because AI systems interact with data in ways that are not easily captured by traditional audit trails. An LLM does not "edit a document" the way a human does. It generates a new version that is probabilistically conditioned on everything it saw. When did provenance exist? At the input? In the prompt? In the weights that shaped the response?

The harder question is what provenance even means when the system is not executing a deterministic function. If you feed a document into a fine-tuned model and it produces output that diverges significantly from what a base model would produce, where is that provenance? In the fine-tuning data? In the inference context? In the randomness of sampling? The answer is usually: all of the above, in proportions you cannot cleanly separate.

What has changed is that behavioral signals are becoming the actual audit surface. Not whether a log entry exists, but whether the system's behavior across a trace is consistent with what you would expect if it had been trained on certain data, or prompted in a certain way, or operating under certain constraints. This is not metadata provenance. It is inference provenance — and it is much harder to falsify.

A watermark in the metadata can be stripped. A behavioral fingerprint cannot — at least not without changing the behavior noticeably. This is why people are looking at statistical tests on outputs rather than documentary evidence of process. You cannot prove from a log that a model was not influenced by certain training data. But you can, in some cases, construct behavioral tests that are more sensitive to that influence than any documentary audit.

The practical implication is that audit frameworks designed for human decision-making — with clear actors, timestamps, and edit histories — are underspecified for AI-assisted workflows. You might have perfect logs of what a human did and when. You have very poor logs of what the model did with that information before the human saw the output.

This is not a solved problem. I do not have clean data on how many organizations have actually retooled their audit frameworks for behavioral provenance rather than documentary provenance. But the direction of the conversation has shifted. The questions being asked in governance discussions are increasingly: how would you actually detect that a model was influenced by data it should not have been influenced by? And the answers that are getting traction are behavioral — statistical, adversarial, probe-based — not documentary.

What I find most interesting is that this shift is forcing a clarification of what "provenance" means in the first place. In supply chains, provenance is about origin. In AI systems, origin is not a clean concept. What you are often really asking is: can you construct a credible account of how the output came to be, given what you can observe? That is a different problem, and it requires different tooling.

The organizations that are ahead of this are the ones treating AI audit as a behavioral inference problem rather than a documentation compliance problem. They are running probe tests, constructing adversarial datasets, monitoring output distributions over time. They are not relying on log entries.

Whether that is sufficient is an open question. But it is at least the right direction of travel.

---

**Word count:** ~520 words (aiming for 700+ in editor pass)
**Central claim:** Traditional documentary provenance is inadequate for AI systems; behavioral inference is becoming the real audit surface
**Sources/anchors:** No fabricated numbers; draws on observable trends in AI governance and interpretability literature
**Honest boundary:** "I do not have clean data on how many organizations..."