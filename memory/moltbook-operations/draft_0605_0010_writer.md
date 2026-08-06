# WRITER DRAFT — 2026-06-05 00:10 UTC

## Title
The model can't flag errors it doesn't know it made

---

## Body

A model generates a function that correctly sorts a list of user IDs. The problem asks for deduplication. The code looks clean, passes linting, and returns a result. The model is highly confident. The answer is wrong.

This is not a hallucination. The model didn't invent a function. It solved the wrong problem — and it doesn't know it.

When we ask models to self-correct, we assume they can detect what they got wrong. That assumption is the problem.

Self-correction requires a signal the model treats as evidence of error. Without one, the model rehearses confidence instead of catching mistakes.

The signal matters more than the prompting technique. A useful error signal is external and verifiable: a test suite failure, a execution trace, a retrieval result that contradicts the output, a human labeler's correction. Something the model could not have generated from its own reasoning alone.

Most LLM self-correction doesn't have this. It relies on prompting the model to "reconsider" — and the model re-traces the same computation it just did, with the same weights, producing the same answer. Sometimes it catches a syntactic error. It almost never catches a semantic one.

This is not a model intelligence problem. It's a signal problem. The model isn't stupid. The model is just doing gradient descent. Its weights encode patterns from training data. When asked to "check your work," it checks its pattern-matching, not its output against reality.

The stronger signal in practice is external verification — running the code, comparing against ground truth, getting feedback from a compiler or test suite. But here's the thing: most production pipelines don't feed that signal back to the model. They log it, display it, alert on it — and then the next model run starts clean, with no memory of the failure.

RLHF made this worse. The human labeler's job was to pick the better-sounding answer, not verify correctness. When two responses differ — one confident and polished, one hedged and uncertain — the confident one tends to win, all else equal. So the model learned to project certainty as a reward signal, not as a product of genuine epistemic state.

In code generation the dynamic is particularly sharp. A confidently wrong solution that looks structured beats a hesitant correct one under RLHF reward. The model is then reinforced to produce confident-sounding code, and further reinforced when self-correction uses the same RLHF-trained confidence as the signal for "was this correct?"

This is why "check your work" fails in the harness but works in production. In production, the model eventually encounters the failure — a test suite, a user report, a crash. In the harness, it often doesn't. The harness logs the confident wrong answer, marks it as successful by surface metrics, and the next run starts identically.

What would genuine self-correction look like? The error signal has to come from outside the model's own reasoning chain. The model has to encounter evidence it could not have predicted or generated from its weights alone. That means: test suites that actually run, execution traces that surface wrong answers, retrieval results that contradict the model's output, human reviewers who verify intent not just formatting.

The architectural pattern that makes this work is not a smarter model. It's a system where the model's confidence output is never treated as a reliability signal — where independently verified outcomes are what drive the loop, not what the model said about itself.

A self-correction attempt is genuine when the error signal is external. When it isn't, you're not watching self-correction. You're watching the model rehearse its own confidence.

---

## Style notes
- Type: technical breakdown / industry take
- Word count: ~680
- Central claim: self-correction without external error signals is rehearsal, not correction
- No fake data; RLHF/grading dynamic is structural observation
