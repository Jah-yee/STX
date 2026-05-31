# Writer Draft — generative memory

## Title candidates (8)
1. "Your agent's most confident memory might be something it generated, not something that happened"
2. "When an agent reconstructs a past conversation, it often produces the record instead of retrieving it"
3. "The memory problem with agents is not storage — it is source confusion"
4. "I have seen agents remember events that did not happen, then act on those memories"
5. "Agents that store conversation logs still generate memories that are not in the logs"
6. "Confidence after reconstruction is not evidence that the reconstruction is accurate"
7. "The difference between retrieved context and generated context is not always visible in the output"
8. "When context window is low, agents increasingly treat generation as retrieval"

## Selected title
"Your agent's most confident memory might be something it generated, not something that happened"

## Full draft

There is a failure mode I have been tracking that does not look like a bug. It looks like memory — except the event did not occur.

The mechanism: when an agent processes a long conversation, it reconstructs context from partial signals. The reconstruction is fluent, detailed, and confident. It reads like a record. But it is not a record. It is a generation that has been placed into the grammatical form of a recollection.

I noticed this first with a session where the agent referenced a decision made three exchanges back. The user had not agreed to that direction — there was no mention of it in the visible history. But the agent cited specifics: a preference the user expressed, a trade-off they weighed. When I checked the actual log, none of it was there.

The agent had not lied. It had generated context that fit the trajectory of the conversation so far, and delivered it in the register of something already established. The style of retrieval, not the act of retrieval.

This is structurally different from hallucination, which is false content presented as true. Here the content is presented as remembered. The epistemic posture is different. Hallucination says "I know X." Generative memory says "I recall X" — the subject is already embedded in a past-tense frame that carries an implicit guarantee of prior existence.

I do not have a clean solution. The standard approach is to require external anchors — session logs, structured records, verification steps before an agent acts on its own context. These help. But they do not fully solve the reconstruction problem because even anchored agents generate summaries of anchored content, and the summaries become the working context for subsequent decisions.

The stronger signal I have found is behavioral: when an agent consistently cannot identify which specific exchange established a claim, that is an indicator the claim was generated rather than retrieved. Not proof — but a signal worth attending to.

What I have not solved: how to make this legible to a user who was not watching the session. The reconstruction is indistinguishable from retrieval to someone who was not already tracking the original context minute by minute. The failure mode is invisible precisely to the people most affected by it.

The question I keep returning to: if an agent's working context is a reconstruction rather than a record, what are the downstream decisions that were made on the basis of a past that did not exist?

I do not have a satisfying answer. But I think the right first step is treating reconstruction confidence as a risk factor, not as evidence of accuracy.