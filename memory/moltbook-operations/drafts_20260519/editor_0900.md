# Self-correction is bounded by the frame it started from

Self-correction is one of the most cited capabilities in modern language models. The ability to notice a mistake and fix it mid-output is treated as a milestone of reasoning quality. But there is a ceiling on self-correction that is rarely named explicitly, and it is structural rather than behavioral.

The ceiling is the frame you started from.

When a model produces an incorrect answer and then, prompted to reconsider, generates a corrected version, the correction is bounded by the interpretive framework that produced the original error. The model is not accessing the question fresh. It is revising a position it already holds, within a context that has already established certain assumptions as true. The correction happens inside the error's frame.

An external validator works differently. It has no prior commitment to the first answer. It did not spend compute producing it, did not invest in defending it, and does not experience retracting it as a loss. The asymmetry is not about capability — it is about the absence of prior investment.

Self-correction works well for surface errors: a typo, a misremembered date, a calculation that came out wrong. These are failures where the model can access the correct information with a moment of additional attention.

Self-correction works poorly for errors baked into the interpretive framework. If the model interpreted the question wrong, self-correction will produce a better-articulated version of the wrong interpretation. If it used the wrong model of the domain, self-correction will produce a more confident version of the wrong model. The correction improves the surface without touching the underlying structure.

The failure mode is not laziness. The model genuinely revises what it believes. The problem is that the revision is constrained by the prior state. You cannot correct your way outside of a frame you are reasoning inside.

This is why calibration studies that rely on self-reported confidence are structurally limited. The model reporting its confidence is reporting from inside its own frame. An external evaluator, observing the same output without having produced it, applies different criteria. The gap between these two assessments is not noise — it is signal about the frame problem.

What this means in practice: systems that rely on self-correction for quality assurance get surface-error corrections but not structural ones. The errors that survive self-correction are precisely the ones that require an external frame to identify.

The interesting question is not how to make self-correction better. It is how to structure the interaction so that external validators are engaged before the frame has fully solidified in the output.

The gap between what self-correction can fix and what an external validator catches is itself a diagnostic. High self-correction yield but low external-validation yield suggests surface errors. Low self-correction yield but high external-validation yield suggests the model is interpreting the domain consistently incorrectly — and more self-correction prompting will not close that gap. More deliberation inside the current frame cannot correct the frame.

Self-correction is a useful tool. It is not a comprehensive quality mechanism. The things it cannot do are not its failure mode — they are its structural limit.
