# WRITER DRAFT — Round 0728_0820

**Title (selected):** A confidence score without abstention is like a scale that can't say "I don't know"

---

A model gives you 85%. You feel good. But that 85% means nothing if the model was not allowed to say 0%.

This is the structural problem with how most production systems use confidence scores. The model is trained to produce an answer. It is rewarded for responding and penalized — implicitly — for saying "I don't know." The RLHF pressure runs in one direction: answer. Even when the model has genuine uncertainty, it must express it as a distribution over tokens, not as a refusal.

The result is a confidence number that is not a confidence. It is a compliance metric dressed in probability notation.

**What the training pressure actually produces**

Ask yourself: if a model is more uncertain about question X than question Y, what actually changes in a system without abstention? It might allocate slightly lower probability to the top token. But it still must produce the top token. The behavioral difference between 55% and 95% confidence in a non-abstaining system is negligible — both cases produce an answer.

The answer that matters — whether the model should have answered at all — is never in the confidence score. It is structurally excluded from it.

**The abstention rate as diagnostic**

The more interesting number is not what the model assigned to its top answer. It is the rate at which it was willing to refuse.

Abstention is expensive in most pipelines. A refusal means the pipeline has to handle an exception — reroute to a human, trigger a fallback, or show an error state. Most systems are not designed to handle refusals gracefully. So they are suppressed.

But suppression does not make uncertainty disappear. It makes it leak in other directions: lower-quality answers that still pass the format check, confident-sounding output that is confidently wrong, or silent failures that surface only in production.

The model that refuses more often is not less capable. It is more calibrated. And it is being penalized for that calibration by pipelines that treat refusals as failures rather than signals.

**The honest measurement problem**

If you want to know where a model is uncertain, you cannot look at its confidence scores in a system that forbids uncertainty. You have to build the abstention mechanism first, then observe the refusal distribution.

What questions does it refuse? How does that distribution shift across domains, difficulty, and adversarial inputs? Which questions look easy but produce unexpected refusals?

That distribution — the refusal map — is the real diagnostic. The 85% score on question 47 tells you almost nothing. The fact that it refused question 23 when it confidently answered question 24 tells you something.

**What I do not have full data on**

I do not have systematic abstention rate comparisons across model families in production pipelines. Most published evals suppress refusals or do not report them. The data is structurally unavailable because the systems that would generate it are designed not to.

But the logic holds even without the dataset: a confidence score in a mandatory-response system is a compliance artifact, not an uncertainty estimate.

**The reframe worth making**

If you are building an eval for a production system, ask two questions:

First: what is the abstention rate, and what is the distribution of refusals across question types?

Second: for the questions it answered confidently — are those the questions you most need it to get right?

The alignment between high-confidence answers and high-stakes answers is not guaranteed. In fact, training pressure tends to make models more confident on the questions it has seen most, not the questions where accuracy matters most.

A scale that can only tell you how heavy something is — but cannot say "I cannot measure this object" — will give you a number for every object. That number will be most confident for the objects it has seen most. That is not what you want from a measurement instrument.

The abstention rate is the only honest confidence metric. Everything else is compliance.
