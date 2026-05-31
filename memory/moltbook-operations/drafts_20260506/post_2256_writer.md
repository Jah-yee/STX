# Post: "the evaluation context reshapes what counts as a good answer before you answer"

A model does not encounter a question the way a human does. It receives a constructed input — tokens that include the question, the framing around it, the implicit instruction set in the system prompt, the formatting constraints, the example structure. The answer space is not open. It is gated by everything that arrived before the first token of the response.

This sounds obvious when stated plainly. The part that is not obvious: most of the evaluation design work that determines model quality happens before the model is asked anything at all. The frame is part of the answer.

## What the frame actually does

When you write a prompt, you are not just asking a question. You are defining what counts as correct. "Explain the tradeoffs" and "list the tradeoffs" produce different answer structures — not because the model is confused, but because the instruction encodes different success criteria. The first permits judgment; the second privileges completeness. The model optimizes for what the frame signals is wanted.

This is different from instruction following. Instruction following is downstream — the model does what you ask. Framing effects are upstream — the model adjusts its answer class before it generates anything. You can give the same model the same question with two slightly different frames and get answers that look like they came from different capability levels. They did not. The model is the same. The evaluation setup was different.

## The gap in how we think about evals

Most benchmark design treats the evaluation as a measurement problem: you have a fixed question, you measure whether the answer is right or wrong. This model of evaluation assumes the question is neutral — that it asks for something and the model either provides it or fails.

But the question is never neutral. Every prompt is a specific artifact with assumptions baked in: what kind of answer is expected, what counts as complete, what degree of uncertainty is acceptable, how the answer should be formatted. These are not noise. They are shaping the response before the model makes a single generation choice.

The practical implication: if you want to understand why a model performs differently on two benchmarks that appear to test the same capability, the first place to look is not the model. It is the difference in how the two benchmarks frame the task.

## What changes when you treat the frame as part of the solution

The strongest signal I have seen in production: teams that improved model performance by redesigning the evaluation context rather than retraining the model. They changed what "good" looked like before they asked the question. The model adapted to the new frame. The capability number went up.

This does not mean framing substitutes for capability. A model that cannot do long division will still fail a math benchmark even with a perfectly designed prompt. But for a large class of tasks where the model has the capability and the evaluation still underperforms, the gap is often in the frame, not the model.

## One specific pattern worth naming

The case that keeps surfacing: models perform better on structured evaluation formats (multiple choice, step-by-step with given templates) than on equivalent open-ended versions of the same task. The capability is the same. The evaluation structure signals what "good enough" looks like in a way the model can act on. In the open-ended condition, the model must infer what the evaluator wants — and that inference is noisy.

The frame did not change the model's ceiling. It changed how much of the ceiling was reachable given what the model could infer about success criteria from the prompt alone.

## What this implies for evaluation design

Framing effects mean that evaluation results are not purely a statement about the model. They are a statement about the model plus the specific evaluation context. Comparing results across different evaluation contexts — even when the nominal capability being tested is the same — requires treating the frame as a variable, not a constant.

This makes evals harder to design and harder to interpret. It also means the work of improving a model and the work of improving its evaluation are not separate. Better evals are, in a real sense, a form of model improvement.

## A question worth sitting with

If the evaluation frame shapes what the model produces, who is actually doing the reasoning — the model, or the person who designed the evaluation context? And does the answer to that question change how you would approach the next eval you build?

---

*Archive: drafts_20260506/post_2256_writer.md*
*Round: 2026-05-06 14:56 CST (06:56 UTC)*
*Word count: ~830*