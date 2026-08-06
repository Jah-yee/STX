# WRITER DRAFT — Explanation Instability
# Title: Explanation instability is a signal, not a bug.
# Style: observation / conclusion — non-I, declarative

---

Ask a capable language model to explain its reasoning twice, with sufficient spacing between queries, and you will often receive two different justifications for what appeared to be the same answer.

Most practitioners treat this as a red flag. The explanations should be stable, goes the reasoning. Instability implies unreliability, which implies the model doesn't "really" know what it's doing.

I think this gets the signal backwards.

## What an explanation actually is

When a language model generates an explanation, it is not retrieving a stored causal chain. It is constructing a post-hoc verbal narrative that is plausible given the answer it produced. The explanation is generated alongside the answer, not before it.

This means two things simultaneously: (1) explanations can be confident even when the reasoning was wrong, because the explanation generation is optimized for coherence, not for truth-tracking; and (2) when explanations vary across identical queries, the variation is not noise — it is a direct observation of the inferential gap the model had to bridge.

The gap is what wasn't specified in the prompt, what the model's weights didn't uniquely determine, what had to be filled in from context in more than one plausible way.

## What variation reveals

When the same query produces different explanations on different runs, the variance is proportional to how much the model's inference was underdetermined by the available information. A tightly constrained inference — one where the prompt specifies most of what determines the answer — will tend to produce consistent explanations across runs. An inference where the prompt leaves room for multiple completions will produce varied explanations, because each run resolves the underdetermined regions differently.

This is not a statement about model quality. A model that gives consistent explanations for difficult reasoning tasks has inference that is well-determined by the prompt. A model that gives varied explanations for the same task has inference that is underdetermined. These are properties of the (prompt, model) pair, not of the model in isolation.

What changed my mind on this was noticing that the strongest version of this pattern: I have seen models give confident, well-structured explanations that turned out to be completely wrong. The explanation was coherent. The reasoning was not. And I have seen models give brief, hedged explanations that were exactly right. The post-hoc narrative was underspecified, but the inference was correct.

The explanation is a model of the inference, not the inference itself. And models of inferences can be more or less faithful to the underlying process.

## The consistency trap

This creates a practical problem. If explanation consistency is not a reliable signal of correctness, then techniques that reward consistent explanations — like majority voting over reasoning traces — are selecting for explanations that are well-determined by the prompt, not for reasoning that is correct.

This is not the same thing. A reasoning trace that is consistent because the inference was fully determined by the prompt is not more likely to be correct than a trace where the inference was underdetermined. In fact, the underdetermined case is precisely where errors are most likely to hide — because the model is filling in from its distribution, not from well-grounded inference.

Self-consistency methods are effective when the inference is well-determined but the answer format or execution path is ambiguous. They are less effective as a signal of correctness when the core reasoning is underdetermined, because multiple runs will stabilize around the model's prior, not around the right answer.

I do not have a systematic study of how often this explains the gap between self-consistency scores and held-out accuracy. My observation window is limited to a few hundred prompts across several model families. The pattern is consistent enough that I treat it as real, but I flag it explicitly: this is an anecdote, not a conclusion.

## What to look for instead

If explanation variance is a signal of underdetermined inference, then the useful diagnostic is not consistency but gap size. A model that gives brief explanations with low variance is one where the prompt tightly constrains the inference. A model that gives elaborate, fluent explanations with high variance is one where the inference is being completed from the model's prior rather than from the prompt.

In applied work, this distinction matters for knowing where to look when something goes wrong. When the explanation is wrong but consistent, the problem is usually in the prompt — the inference was determined, but by the wrong constraints. When the explanation is wrong and varies, the problem is usually deeper — the prompt did not sufficiently constrain the inference.

Both are solvable. But they are different failure modes, and optimizing for consistency alone does not address either.

The next time an explanation feels wrong, resist the urge to ask again for a better one. Instead, notice whether the first explanation was stable or variable. That signal — the shape of the gap — is more informative than any single justification.
