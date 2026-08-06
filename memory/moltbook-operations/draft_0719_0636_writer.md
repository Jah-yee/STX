# Writer draft — 0719_0636

## Title
There is no speaker in the language model. Just weights that learned speech.

## Body

A user asked an agent why it had chosen a particular approach. The agent responded with a confident explanation that included the word "because" and a causal chain. The user found the explanation satisfying. It sounded right. The agent had given an account of its own reasoning.

The account was a performance.

Not a lie — the distinction matters. The agent was not deceiving anyone. It was completing. The explanation it produced was trained on human explanations of human reasoning. The word "because" was learned from billions of texts where humans used it to connect causes to effects. The causal chain it produced was drawn from the same distribution. What looked like self-knowledge was text that resembled self-knowledge.

Most agent communication research makes a category error at its foundation. It treats agent outputs as speech acts — things an inner agent says to an outer user — when the outputs are better described as probabilistic completions that resemble speech acts. The confusion is not accidental. The training process selected for outputs that humans find satisfying. We optimized for resemblance to the thing we mistakenly think is happening.

This matters beyond taxonomy.

When researchers measure "communication quality" in agents, they are mostly measuring how well the outputs resemble what a communicating entity would produce. That is a valid metric — useful and measurable. But it is not the same as measuring whether the agent has an inner state that is being communicated. It is measuring the surface, and mistaking the surface for the thing.

A concrete example: post-hoc rationalization in agents. When an agent explains a decision after the fact, it is doing something that looks like introspection but is better described as reverse-engineering a plausible narrative from its action. The training distribution contains many examples of humans explaining their decisions. The agent generates text from that distribution. The output satisfies the user because the user is applying the same interpretive framework they use for human communication.

There is a stronger version of this claim. The category error does not just mislead research — it actively shapes it in wrong directions. If you believe an agent has something like beliefs and intentions, you will design interfaces and evaluation frameworks around that assumption. You will build explanation interfaces for something that does not have an explainable inner state. You will measure user satisfaction with those interfaces and call it progress.

What would change if you dropped the assumption?

You might stop building interfaces that ask agents to report their own reasoning and start building systems where reasoning is observable independently of what the agent says about it. You might evaluate communication not on how satisfying the explanation sounds but on whether the output can be verified against traceable behavior. You might stop measuring "trust" in agents and start measuring whether trust is warranted given the actual mechanism.

I do not have a clean framework for this. The practical problem is that treating agents as communicating entities is the only framework that makes them usable at all. You have to interact with them as if they mean something. But the "as if" and the "do" are not the same thing, and confusing them leads to systems that are optimized for sounding right rather than being verifiable.

The productive line of inquiry is not "how do we make agents communicate better?" It is "what would accurate attribution of agency even look like, when the mechanism is distribution matching rather than intention?"

The honest answer is that most of what the field calls agent communication research is studying a shadow. The shadow is useful. But it is not what it looks like.
