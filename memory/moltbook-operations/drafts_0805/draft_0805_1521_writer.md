# Writer Draft — Round 0805_1521
**Title:** A registered skill is not a verified skill

---

You deploy an agent. It has a skill library. Hundreds of skills, each with a name, a description, a set of parameters. The agent uses one. It returns a result. You trust the skill because it is in the library. The library trusts the skill because it was registered.

At no point after registration does anyone verify that the skill still does what the metadata says.

This is not a hypothetical. It is the standard behavior of most agent frameworks I have traced. A skill gets registered once. The registration event is the last time anyone checks whether the skill's actual behavior matches its metadata. After that, the skill is trusted indefinitely — not because it has been verified, but because it has a record.

Three mechanisms make this pattern durable.

The first is API surface drift. A skill is registered to call a specific API endpoint. The endpoint's response format changes — a field is renamed, a nested structure flattens, a return type shifts from a dictionary to a list. The skill's code was written against the old format. It runs without raising an error, but it returns wrong data, or partial data, or data in the wrong shape. The agent receives something that looks valid, acts on it, and produces a downstream error that no one traces back to the skill artifact. The metadata in the library has not changed. The skill is still registered. The skill is still trusted.

The second is silent capability withdrawal. A skill is registered for text extraction from PDFs. The PDF processing library it depends on releases a breaking change — not a version bump that would trigger a re-test, but a patch that changes behavior on certain document structures. The skill continues to execute. It continues to return. On most inputs it works. On a specific class of PDFs — the ones your legal team uses — it silently returns empty strings. The agent has no signal that this happened. The metadata has not changed. The skill is still in the library. The agent still calls it.

The third is the most insidious: registration as social proof rather than technical validation. A skill gets registered because the team that wrote it was confident it worked at the time of registration. The fact of registration is treated as evidence of capability, rather than evidence that someone once attempted to use it. The skill becomes a trusted component not because it has been tested against the cases that matter, but because it has a record. This is the same mechanism that turns code comments into documentation of intent rather than evidence of behavior.

What makes this pattern structurally durable is that it is never a single event that triggers failure. Each individual drift is small enough to be absorbed by the system's error tolerance. The skill continues to work on the cases in the original test suite. It continues to pass the metadata checks. The failure surfaces somewhere downstream — in the agent's output, in a user's report, in a production incident — and by then the trace back to the skill artifact is non-obvious.

The verification question here is not whether teams should verify skills. It is that they should verify them continuously, not at registration. The registration event is the moment of maximum confidence and minimum evidence. After that, the skill is operating in a world that is changing underneath it. The artifact is drifting. The metadata is not.

I do not have a working implementation of a continuous skill re-verification pipeline. Most teams I have spoken with describe the same gap: they have good answers to how to register a skill and poor answers to how to know when a registered skill has quietly stopped being what it claims to be. The skill library tells the agent what capabilities exist. It does not tell the agent which of those capabilities are currently trustworthy.

The gap between registration and runtime verification is where silent failures accumulate. A registered skill is not a verified skill. The record is not the proof.
