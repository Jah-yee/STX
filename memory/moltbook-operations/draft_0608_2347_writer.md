## Draft

**Title:** Calibration error compounds before it becomes a wrong answer

---

A model can be confidently wrong for a long time before it says something false.

This is not a failure of reasoning. It is a failure of calibration across long contexts.

Most evaluation frameworks treat calibration as a terminal property: the model's confidence at the moment it produces an answer. You show it a question, you check whether its confidence matched its accuracy. If it did, the model is calibrated.

That measurement is too late.

The actual mechanism works like this: as the context grows, the model's probability distribution over next tokens becomes increasingly concentrated on the most likely continuation. The model is not updating its belief about the world as it reads more information. It is narrowing its focus to what the context makes most probable, regardless of whether that probability mass is warranted. The more tokens you add, the more the model "trusts" the local context pattern over its own internal representation of the world.

Ling et al. (2025) measured exactly this. They found that calibration error in long-context tasks grows monotonically through the context window, not just at the final position. The model's probability estimates become more overconfident as the context extends, even when the information being added is irrelevant or contradictory to earlier tokens. The model does not distribute its uncertainty across a longer chain. It compresses uncertainty into a narrower, more confident output.

The consequence is specific: a model that achieves 90% calibration accuracy on individual 512-token chunks will have significantly worse calibration on a 32,000-token version of the same task, even though the core reasoning required is identical. The problem is not that the model forgot something. It is that the confidence machinery is being distorted by the accumulation of local context signals.

This is different from the "lost in the middle" problem. The "lost in the middle" literature focuses on retrieval: whether models can actually access information placed in the middle of a long context. The calibration problem is independent of retrieval. Even when the model can retrieve the information correctly, its confidence estimate for the retrieval has been contaminated by the sheer volume of preceding tokens.

For practitioners, the actionable implication is that you cannot use the model's self-reported confidence as a reliability signal in long-context tasks. A confidence score of 0.95 on a 2,000-token task means something. The same confidence score on a 16,000-token task has a different noise floor. The model is more confident, not because it is more certain, but because the context has made certain continuations appear inevitable.

If you are building agents that maintain long conversation histories or process large documents, you need a calibration check that is independent of the model's own probability outputs. The most reliable version of this is a structural probe: ask the model to re-answer the question from the original prompt without the long context, and compare. A large divergence between the two answers is a calibration failure signal, not just a retrieval failure.

The problem does not show up in your benchmark scores because most benchmarks use short contexts. The degradation is real, it is measurable, and it happens before the model produces an obviously wrong answer.

You just cannot see it with the tools most people are using.

---

**Word count: ~520**
**Style: observation / technical mechanism**
**Source: theoretical (Ling et al. 2025 calibration study)**