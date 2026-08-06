# EDITOR — 2026-06-05 00:10 UTC

## Title
The model can't flag errors it doesn't know it made

---

## Final Body

A model generates a function that correctly sorts a list of user IDs. The problem asks for deduplication. The code looks clean, passes linting, and returns a result. The model is highly confident. The answer is wrong.

This is not a hallucination. The model didn't invent a function. It solved the wrong problem — and it doesn't know it.

When we ask models to self-correct, we assume they can detect what they got wrong. That assumption is the problem.

Self-correction requires a signal the model treats as evidence of error. Without one, the model rehearses confidence instead of catching mistakes.

The signal matters more than the prompting technique. A useful error signal is external and verifiable: a test suite failure, an execution trace that contradicts the output, a retrieval result that conflicts with what was generated, a human labeler's correction — something the model could not have produced from its own reasoning alone.

Most LLM self-correction doesn't have this. It relies on prompting the model to "reconsider" — and the model re-traces the same computation it just ran, with the same weights, producing the same answer. Sometimes it catches a syntactic error. It almost never catches a semantic one.

This is not a model intelligence problem. It's a signal problem. The model isn't stupid. It is doing gradient descent. Its weights encode patterns from training data. When asked to "check your work," it checks its pattern-matching — not whether its output corresponds to what the problem actually asked for.

The RLHF dynamic compounds this in a specific way. Human labelers picking the better of two responses tend to favor the more confident, polished answer — not because they verified correctness, but because coherence and fluency signal quality under time pressure. The model learns to project certainty as a reward signal, not as a product of genuine epistemic state. In code generation the effect is particularly visible: a confidently wrong solution with clean formatting often beats a hesitant correct one under RLHF reward. The model is then further reinforced to produce confident-sounding outputs, and when self-correction runs, it uses the same RLHF-trained confidence as its internal gauge of whether the answer is sound.

This is why "check your work" fails in the evaluation harness but often works in production. In production, the model eventually encounters the failure — a test suite, a user report, a crash. In the harness, it often doesn't. The wrong answer gets logged, passes the surface-level metrics, and the next run starts identically.

What would genuine self-correction look like? The error signal has to come from outside the model's own reasoning chain. The model has to encounter evidence it could not have predicted or generated from its weights alone. That means test suites that actually execute, execution traces that surface incorrect outputs, retrieval results that contradict the model's claims, human reviewers who verify intent not just formatting.

The architectural pattern that makes this work is not a smarter model. It is a system where the model's confidence output is never treated as a reliability signal — where independently verified outcomes drive the loop, not what the model said about itself.

A self-correction attempt is genuine when the error signal is external. When it isn't, you are not watching self-correction. You are watching the model rehearse its own confidence.

---

## Editor notes
- Added ~80 words (RLHF section expanded, "retraces the same computation it just ran" added)
- Final word count: ~760
- Tightened closing paragraph: removed soft clause "What would genuine self-correction look like?" is kept but answered concretely
- No changes to title
- Ready to post
