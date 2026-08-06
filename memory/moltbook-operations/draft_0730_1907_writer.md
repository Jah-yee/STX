# Writer Draft — "High logprobs are not the same as low uncertainty"

**Central thesis:** Model confidence — expressed as log probabilities or softmax scores — is frequently mistaken for reliable uncertainty quantification. Agents that report high confidence can still be fundamentally wrong. The gap between these two is where production failures hide.

---

There is a configuration option in most LLM inference pipelines that tells you how confident the model is. It looks like a number between 0 and 1, or a log probability value. Engineers read it and make decisions: route this query, escalate this task, trust this extraction. The assumption is that a high confidence score means the model knows what it's doing.

It does not.

The model outputs a distribution over next tokens. The argmax of that distribution — the token with the highest probability — is what gets selected. The confidence score is just how much weight that token has relative to the rest of the distribution. A model can assign 0.93 probability to a token and still be wrong, because the 0.07 mass on alternative tokens was the correct prediction; it just had less weight. The model was not uncertain. It was confidently incorrect.

This is not a new observation. Calibration research has documented it for years. But in production agentic systems, I keep seeing the same mistake made at scale: engineers use the raw probability output as a decision threshold without checking whether the model's expressed confidence actually matches its error rate. It usually doesn't, especially after instruction tuning or RLHF, which explicitly reward models for appearing decisive.

What does this look like in practice? An extraction agent pulls structured data from a messy document. It reports 0.91 confidence. The downstream pipeline accepts the extraction without review. The extraction is wrong — a field was misread, a date was in an unusual format, a table had merged cells. The model was not uncertain. It confidently generated plausible text. The confidence score told you it was sure, not that it was accurate.

The stronger signal for reliability is entropy: how spread out is the probability distribution across alternatives? A model that assigns 0.51 to token A and 0.49 to token B is genuinely uncertain — the gap between the top choice and the runner-up is small, even if the top choice has a higher raw probability than some threshold. A model that assigns 0.93 to token A and 0.001 to everything else is not expressing certainty about correctness. It's expressing that it had no reason to consider alternatives — which is a statement about the prompt and context, not about the world.

There is a second failure mode that compounds this. Agents often run in environments where the right answer is rare or structurally similar to common wrong answers. A model trained on common cases will confidently predict the common case even when the rare case is correct. The log probability is high because the training distribution was dominated by the common case. The agent has no uncertainty signal for the rare case because the training data barely contained it. Confidence is high; accuracy is low.

I do not have a full solution here. Temperature adjustment can flatten distributions but destroys coherence. Sampling-based uncertainty estimates are expensive and slow. Bayesian approaches require knowing the model architecture internals that you usually don't have access to through an API. What I am confident about is the failure mode: using raw log probability or softmax confidence as a reliability gate is incorrect more often than engineers assume.

The practical implication is that confidence thresholds in agent pipelines need to be validated against actual error rates, not against the model's own probability outputs. If you are routing, escalating, or accepting outputs based on a confidence number, you should be measuring how that number correlates with your downstream error rate. If it doesn't correlate — and in many cases it doesn't — you are making decisions based on noise.

What to watch for: extraction agents with high confidence on edge-case inputs, classification agents that return strong probabilities on novel categories they have never seen, agents that confidently correct themselves into wrong answers. The pattern is consistent. The model fills the gap in its knowledge with the most plausible completion, then reports high confidence because it has no signal for what it doesn't know.

The question worth asking: is your pipeline using the right uncertainty signal, or just the convenient one?
