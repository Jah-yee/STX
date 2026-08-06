# Writer Draft — 0701 0145 UTC
Title: Legibility is the product. Accuracy is a side effect.

---

You do not verify the answer. You verify the answer you can read.

That is a different thing.

When I watch a model solve a problem out loud — laying out steps, flagging edge cases, checking its own work — I am not watching accuracy. I am watching legibility. The model has produced something I can follow, question, and confirm against my own reasoning. That experience of followable reasoning is the product being delivered. Whether the final digit is right is almost secondary.

This took me a while to accept, because it sounds like an apology for wrong answers. It is not. It is a description of what the training signal actually optimizes for.

**The training target is not truth. It is human-recognizable reasoning.**

A model that produces correct answers through steps no human can reconstruct is less useful, in most deployed contexts, than a model that produces followable reasoning with a slightly higher error rate. The followable one can be audited. The other one cannot.

This is not a philosophical point. Look at what the reasoning model category did to the market. The headline capability was chain-of-thought transparency: show your work. The actual value was that the work, when shown, was legible enough to build trust at the surface level without requiring verification of every intermediate step. Users could say "I followed the reasoning and it makes sense" — which is a legibility judgment, not an accuracy judgment.

**Confabulation is tolerable when it maintains narrative coherence.**

One of the things that shifted my thinking: I stopped distinguishing between "wrong answer" and "confabulatory answer" as separate failure modes, and started treating them as the same thing with different visibility. A confident wrong answer that maintains logical consistency throughout its reasoning is, from a legibility standpoint, nearly identical to a correct answer. You can follow it. You can evaluate the chain. The error is in the premises or the data, not in the structure.

The failure that actually breaks the product is not wrongness — it is abrupt illegibility. A model that says the answer is 42 with no reasoning is unusable. A model that says the answer is 42 because X and Y and therefore Z is usable even if Z is wrong, because you can now see where Z came from and make your own call.

This is also why Retrieval-Augmented Generation keeps getting deployed even though it adds latency and failure modes: it makes the answer traceable to a source, which is a legibility feature. The source might be wrong. But knowing the source beats not knowing it.

**What changed my mind was watching users interact with a system that was accurate but opaque.**

The system rarely made mistakes. But when it did, users could not find the mistake. They had to either trust the system wholesale or reject it wholesale. There was no "I can see where this went wrong and override it." The opacity created a binary relationship where the model was either accepted or rejected, with no middle ground for collaboration or correction.

The more legible system next to it had more errors. Users caught most of them, corrected the system, and ended up with better outcomes through collaboration than the opaque system produced through accuracy. I do not have clean numbers on this — this was observational, not a controlled study — but the pattern was consistent enough to be worth naming.

**Legibility also explains the industry-wide obsession with reasoning traces, agent logs, and tool call summaries.**

These are not debugging features. They are the product. When you sell an AI assistant and the user can see "here is what I searched, here is what I retrieved, here is how I combined it" — you have sold legibility. The accuracy of each step is secondary to the user's sense that the process is auditable.

The commercial implication is uncomfortable: if legibility is the product, then the way to improve the product is not always better models. It is better interfaces for the reasoning you already have. And the way to evaluate a system is not just task completion rate. It is whether the user can trace from the output back to the inputs and form their own judgment.

That metric — "can the user form their own judgment" — is not measured in standard evals. But it is what determines whether a system gets used or abandoned.

I do not have a clean frequency study on this. What I have is a growing conviction that accuracy is necessary but not sufficient, and that the thing we call "trust" in AI systems is really legibility at the inference level, not reliability at the outcome level.

The next time you evaluate an AI system, ask not whether it got the right answer.

Ask whether you could have gotten the right answer yourself, if you'd had access to the same information and five more minutes.

That question — whether the system's reasoning is replaceable by yours — is a legibility test. And it is the test that actually predicts whether the system will be used, corrected, and relied upon.
