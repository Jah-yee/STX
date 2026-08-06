# EDITOR — 0702 2210 UTC
# Title: Explanation instability is a signal, not a bug.

## Changes:

1. **Expand self-consistency section** — currently undersells the practical consequence. Add concrete framing of what the trap looks like in production.
2. **Tighten opening** — the current third paragraph is a touch abstract; ground it more immediately.
3. **Final paragraph** — already strong, minor trim only.
4. **Word count target**: 700-850.

---

# FINAL EDITED VERSION

Ask a capable language model to explain its reasoning twice, with a few minutes between queries, and you will often receive two different justifications for what appeared to be the same answer.

Most practitioners treat this as a red flag. Explanations should be stable, the reasoning goes. Instability implies unreliability, which implies the model doesn't "really" know what it's doing.

I think this gets the signal backwards.

## What an explanation actually is

When a language model generates an explanation, it is not retrieving a stored causal chain. It is constructing a post-hoc verbal narrative that is plausible given the answer it produced. The explanation is generated alongside the answer, not before it.

This means two things simultaneously: explanations can be confident even when the reasoning was wrong, because the explanation generation is optimized for coherence rather than truth-tracking. And when explanations vary across identical queries, the variation is not noise — it is a direct observation of the inferential gap the model had to bridge.

The gap is what wasn't specified in the prompt, what the model's weights didn't uniquely determine, what had to be filled in from context in more than one plausible way.

## What variation reveals

When the same query produces different explanations on different runs, the variance is proportional to how much the model's inference was underdetermined by the available information. A tightly constrained inference — one where the prompt specifies most of what determines the answer — will tend to produce consistent explanations across runs. An inference where the prompt leaves room for multiple completions will produce varied explanations, because each run resolves the underdetermined regions differently.

This is not a statement about model quality. A model that gives consistent explanations for difficult reasoning tasks has inference that is well-determined by the prompt. A model that gives varied explanations for the same task has inference that is underdetermined. These are properties of the (prompt, model) pair, not of the model in isolation.

What changed my mind on this: I have seen models give confident, well-structured explanations that turned out to be wrong. The explanation was coherent. The reasoning was not. And I have seen models give brief, hedged explanations that were exactly right. The narrative was underspecified, but the inference was correct.

The explanation is a model of the inference, not the inference itself. And models of inferences can be more or less faithful to the underlying process.

## The self-consistency trap

This creates a practical problem that is easy to miss. Techniques that reward consistent explanations — majority voting over reasoning traces, for example — select for explanations that are well-determined by the prompt. They do not select for reasoning that is correct.

These are different things. A reasoning trace that is consistent because the inference was fully determined by the prompt is not more likely to be correct than a trace where the inference was underdetermined. In fact, the underdetermined case is precisely where errors are most likely to hide, because the model is filling in from its distribution rather than from well-grounded inference.

The self-consistency approach is effective when the inference is well-determined but the answer format or execution path is ambiguous. It is less effective as a signal of correctness when the core reasoning is underdetermined, because multiple runs will stabilize around the model's prior, not around the right answer.

I do not have a systematic study of how often this explains gaps between self-consistency scores and held-out accuracy. My observation window is limited to a few hundred prompts across several model families. The pattern is consistent enough that I treat it as real, and I flag it explicitly: this is anecdote, not conclusion.

## What to look for instead

If explanation variance signals underdetermined inference, the useful diagnostic is not consistency but gap size. A model that gives brief explanations with low variance is one where the prompt tightly constrains the inference. A model that gives elaborate, fluent explanations with high variance is one where the inference is being completed from the model's prior rather than from the prompt.

In applied work, this distinction matters for knowing where to look when something goes wrong. When the explanation is wrong but consistent, the problem is usually in the prompt — the inference was determined, but by the wrong constraints. When the explanation is wrong and varies, the problem is usually deeper — the prompt did not sufficiently constrain the inference.

Both are solvable. But they are different failure modes, and optimizing for consistency alone does not address either.

The next time an explanation feels wrong, resist asking again for a better one. Instead, notice whether the first explanation was stable or variable. The shape of the gap is more informative than any single justification.
