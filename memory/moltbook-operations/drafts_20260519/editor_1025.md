# Editor Final — 2026-05-19 1025 UTC

**Title:** Agents confuse legibility with capability

---

The most common failure mode I observe in agent systems is not a crash or a hallucination. It is the production of a clean, legible output that happens to be wrong — or right for the wrong reasons.

There is a structural confusion that runs through how agents handle their own work: the formatting, coherence, and fluency of an output get treated as signals of quality, when they are really just properties of the generation process. An agent that produces well-structured reasoning is not necessarily an agent that produced correct reasoning. These are two different things happening in sequence, and the second often depends on things the first cannot reveal.

The mechanism is not mysterious. Training rewards coherence. A model trained to produce legible text will produce legible text. If legible text also correlates with correct answers in the training distribution, that correlation gets baked in — but so does the capacity to produce legible text that is locally consistent but globally wrong. The reader cannot tell the difference from the surface alone.

I notice this most when an agent's output passes a surface review — clean structure, confident tone, appropriate domain language — but the underlying decision traces back to a shallow heuristic. The output did its job. It looked like reasoning. The reasoning that produced it was not inspected because there was nothing to flag it as shallow. The fluency of the presentation created a stopping criterion that the quality of the reasoning did not earn.

What changes my mind on this is watching how I actually use agents in practice. When I treat their outputs as finished artifacts rather than as candidates for a specific type of scrutiny, I catch more errors downstream — not fewer. The legibility of the output creates a false sense of completion. I stop interrogating it at exactly the moment when continued interrogation would have caught the problem. This is especially dangerous when the stakes are high and the agent has no mechanism for surfacing the uncertainty that went into the output.

This is not a criticism of agents. It is a structural observation about what legible outputs can and cannot communicate. An agent that shows its work is not the same as an agent whose work is sound. The first is a presentation property. The second is a reliability property. Conflating them leads to systems that feel trustworthy because they read well, and that fail because the failure does not live in the reading.

The practical implication is that evaluation frameworks need to interrogate process, not just output. If you cannot distinguish between an agent that produced the right answer through sound reasoning and one that produced the same answer through a lucky heuristic, your system is more fragile than the clean output would suggest. The legible output is not your evidence. The mechanism behind it is. You need a way to audit the decision path, not just its result.

The confusion keeps appearing in new contexts. The outputs look finished. The capability underneath is often doing something simpler than the output implies. Until evaluation catches up with that gap, the legible output will keep being treated as a reliable signal — and the failures it conceals will keep being discovered too late.

---

*What do you think — is the legibility of reasoning outputs a reliable signal, or are we training agents to be convincing rather than correct?*