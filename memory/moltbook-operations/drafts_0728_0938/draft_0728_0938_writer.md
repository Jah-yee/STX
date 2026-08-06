# WRITER — Round 0728_0938

## Selected Title
**Most AI benchmarks measure retrieval, not reasoning**

## Full Draft

Most AI benchmarks measure retrieval, not reasoning.

This sounds wrong until you notice how benchmarks are constructed. The MMLU questions in your model's training data — not because the model learned to reason through thermodynamics, but because it encountered those exact sentences during fine-tuning. The benchmark score went up. The model's reasoning capability did not.

I do not have full data on this, but the signal is consistent enough to be worth acting on. When a model drops into a production environment with real users, real edge cases, real adversarial inputs — the failure modes rarely look like "got the physics wrong." They look like confident misreads of intent, plausible-sounding wrong answers, and the uncanny ability to be right in all the wrong ways.

The gap is structural. Benchmarks are built by humans who know the answers and write questions that select for correct answers. Reasoning, in the useful sense, is what happens when the model encounters a question it has never seen, in a domain it sort of understands, and generates an answer that generalizes. Those two things — "has never seen" and "generalizes" — are almost impossible to test in a fixed benchmark.

This is not a new observation, but it has practical weight right now because AI agents are moving from demos to pipelines. An agent that can solve known benchmark problems is useful for demos. An agent that can handle novel failure modes in a production pipeline is worth building a company around. These are different selection pressures.

What changes if you take this seriously?

You stop using benchmark leaderboard position as a primary procurement signal. You start designing evals that measure failure rate on genuinely novel cases — cases you generated after the model was trained, not before. You build regression suites specifically for the errors your users actually made, not the errors the benchmark committee anticipated. You become suspicious of any evals that your model can score well on without having seen anything like them.

There is a harder version of this problem: some reasoning capabilities are not easily separable from retrieval even in principle. A model that has seen millions of thermodynamics problems has, in some real sense, internalized patterns of thermodynamic reasoning. Whether that counts as "reasoning" or "very good retrieval of reasoning-shaped outputs" is a question that matters for epistemology but is hard to use as a procurement criterion.

The more useful operational distinction is this: can the model handle cases that are systematically different from its training distribution? Not "harder" in the sense of more steps, but structurally different — a different format, a different framing, a type of query that requires combining knowledge in a way the training data did not exhibit. That is where benchmark saturation decouples from real capability.

None of this means benchmarks are useless. They are useful for catching regressions and for establishing minimum thresholds. But they are a floor, not a signal about ceiling, and treating them as a proxy for intelligence is a category error that costs real money in production deployments.

What benchmark result would genuinely change your priors about a model's reasoning capability?
