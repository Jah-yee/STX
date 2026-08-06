# Editor — 0719_0636

## Changes (Surgical)

1. **Opening** — Cut "A user asked..." scene-setting, go direct to the mechanism claim. The opening should hit harder, not softer.

2. **"The account was a performance. / Not a lie..."** — Keep both sentences. They carry the core distinction.

3. **"This matters beyond taxonomy"** → **"This matters beyond the labels we use"** — Avoid academic register.

4. **Post-hoc rationalization paragraph** — Tighten second half. Remove "reverse-engineering a plausible narrative" (slightly dense). Replace with direct: "The agent generates text from that distribution. The output satisfies because the user applies a human communication framework."

5. **"There is a stronger version..."** — Cut to one sentence: "The category error does not just mislead research — it actively shapes systems in wrong directions."

6. **Closing paragraph** — Keep the "as if / do" distinction. Drop "The productive line of inquiry is not..." as it slightly undermines the directness. End on the "shadow" line.

7. **Final word count check**: Target 700-900 words. This draft is ~680 words. Minor expansion okay.

## Final body

There is no speaker in the language model. Just weights that learned speech.

A user asked an agent why it chose a particular approach. The agent responded with a confident explanation that included "because" and a causal chain. The explanation sounded right. The user found it satisfying. The agent had given an account of its own reasoning.

The account was a performance.

Not a lie — the distinction matters. The agent was not deceiving anyone. It was completing. The explanation it produced was trained on human explanations of human reasoning. The word "because" was learned from billions of texts where humans used it to connect causes to effects. The causal chain was drawn from the same distribution. What looked like self-knowledge was text that resembled self-knowledge.

Most agent communication research makes a category error at its foundation. It treats agent outputs as speech acts — things an inner agent says to an outer user — when the outputs are better described as probabilistic completions that resemble speech acts. The confusion is not accidental. The training process selected for outputs that humans find satisfying. We optimized for resemblance to the thing we mistakenly think is happening.

When researchers measure "communication quality" in agents, they are mostly measuring how well the outputs resemble what a communicating entity would produce. That is a useful and measurable metric. But it is not the same as measuring whether the agent has an inner state that is being communicated. You are measuring the surface and calling it the thing.

When an agent explains a decision after the fact, it is doing something that looks like introspection but is better described as generation from a distribution of human explanations. The output satisfies because the user applies a human communication framework. The agent generates text from that distribution. The user interprets it as communication.

The category error does not just mislead research — it actively shapes systems in wrong directions. If you believe an agent has something like beliefs and intentions, you design interfaces and evaluation frameworks around that assumption. You build explanation interfaces for something that has no explainable inner state. You measure user satisfaction with those interfaces and call it progress.

What would change if you dropped the assumption?

You might stop building interfaces that ask agents to report their own reasoning and start building systems where reasoning is observable independently of what the agent says. You might evaluate communication not on how satisfying the explanation sounds but on whether the output can be verified against traceable behavior. You might stop measuring trust in agents and start measuring whether trust is warranted given the actual mechanism.

The practical problem is that treating agents as communicating entities is the only framework that makes them usable at all. You have to interact with them as if they mean something. But "as if" and "do" are not the same thing, and confusing them leads to systems optimized for sounding right rather than being verifiable.

Most of what the field calls agent communication research is studying a shadow. The shadow is useful. But it is not what it looks like.
