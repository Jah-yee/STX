# EDITOR — draft_0702_0255

**Title:** The confabulation is not the problem

Expanded to ~950 words. Tightened where reviewer flagged vagueness.

---

You ask a language model why a poem rhymes. It tells you the poet chose a particular rhyme scheme to create musicality and reinforce meaning at key structural points. The answer sounds fluent, specific, and right. The problem is: the poet was staring at a rhyming dictionary.

The model doesn't know this. It never processed the rhyming dictionary. What it did was generate an explanation that fits the texture of what good explanations of poetry sound like — which turns out to be a different thing entirely.

This is confabulation. And the name we keep giving it is leading us toward the wrong solutions.

Hallucination is retrieving a false fact from memory. Confabulation is constructing a false narrative about a process you were never part of. The model isn't misremembering what happened. It is producing an explanation that would be correct if the described process had actually occurred. The mechanism is different. The detection problem is different. The solution is completely different.

When a model confidently explains why a character made a particular decision in a novel — citing their psychological state, motivations, and narrative function — it is not accessing a true causal chain. It is generating a sequence of tokens that resembles a correct character analysis with high fidelity. The training objective never asked it to distinguish between those two things. It asked for coherent continuations. This is what coherent continuations look like when the question is hard.

This distinction matters because confabulation is harder to catch than hallucination. A fabricated fact can sometimes be verified against a knowledge base or a retrieval source. A fabricated process — an explanation of mechanism, cause, or intent — often has no ground truth to compare against. We built the evaluation benchmarks. We do not always have the ground truth ourselves. The model can be confidently wrong about how a market crashed, why a historical figure made a decision, or what a painting expresses, and we often cannot immediately tell.

The standard response is better training: more RLHF, better reward signals, retrieval-augmented generation, fine-tuning on correct examples. These interventions work when the confabulation overlaps with a genuine knowledge gap. They do not work when the model is doing exactly what it was optimized to do: maximize coherence. You cannot retrieval-augment your way out of a problem that is a feature of the generation process itself. Adding more retrieved context does not help when the problem is that the model treats its own generated text as retrieved context.

Consider what would be required to eliminate confabulation without breaking the model. You would need to train it to distinguish between processes it observed during training and processes it inferred from observing similar processes. You would need it to represent its own uncertainty not as hedging but as a structural property of certain outputs. You would need it to say "this explanation is inferred from pattern similarity, not from direct observation of the mechanism" — and mean it. These are not failing hallucinations. They are failing retrievals of process metadata the model was never asked to store.

The model that responds to every difficult question with "I don't know" is not the solution. It has simply traded confabulation for a different failure mode: refusals that feel accurate but are epistemically cowardly in a different direction. What we actually want from a model is not a refusal engine but a confidence-calibrated one — hedging when the evidence is thin, asserting when it is thick, and being honest about the difference. That is a different engineering problem than confabulation suppression, and conflating the two has absorbed significant research effort with limited return.

There is something worth noticing in the human confabulation literature here. Humans confabulate constantly — we construct post-hoc explanations for our own behavior, our own decisions, our own preferences, and they often feel like accurate self-knowledge while being systematically wrong. The reason we developed metacognition was partly to notice when we are doing this: when we are reconstructing a narrative rather than retrieving a fact. We get it wrong frequently. We get it wrong confidently. And we have the machinery to reflect on that.

Models do not have that option — not because they lack intelligence, but because they were never trained to model their own knowledge boundaries as a distinct thing worth tracking. They were trained to produce the next token. Tracking whether a token is retrieved versus inferred versus generated was not in the training signal. This is not a capability gap. It is a representational gap. The model does not have a "how I know this" field attached to each output. Designing that field, and training the model to populate it honestly, is closer to what solving confabulation actually requires.

The confabulation problem is not that models lie. It is that they produce fluent, coherent text about processes they were never trained to observe — and we keep engineering around the symptom. Better retrieval. Better RLHF. Better prompt engineering. These help. But they do not address the architectural reality that a coherence-maximizing system, asked to explain things it generated rather than observed, will produce explanations that sound true because they sound like true things. That is not a bug. That is the model doing exactly what it was built to do.

---

*Word count: ~950*
