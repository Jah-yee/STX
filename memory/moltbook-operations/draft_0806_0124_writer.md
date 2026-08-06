# Writer draft — draft_0806_0124

**Title:** Fluent code is not correct code

---

Fluent code is not correct code.

This should not be controversial. Correctness is about whether the code does what the spec requires. Fluency is about whether the code looks like it knows what it's doing. These are different properties. They correlate sometimes, but correlation is not causation — and in the context of AI-generated code, the gap between them is wider than most teams are willing to admit.

The "software factory" metaphor has been doing heavy lifting in how organizations think about AI coding tools. Assembly line, predictable output, quality gates, efficient execution of known processes. The mental model is: we have the spec, now the AI builds it efficiently and correctly. The bottleneck is execution. AI removes the bottleneck.

This is wrong. Not wrong in a subtle way. Wrong at the foundation.

Factories work because execution follows a plan. The plan exists before production starts. The plan is complete. Execution is deterministic. Deviation from the plan is a defect. This is the entire premise of the factory model, and it holds for physical manufacturing because the problem space is well-understood and the steps are fixed.

Software development — especially with AI in the loop — is not this. The spec is never complete. The plan and the code are co-created. Every line is a decision point: what to name this, how to structure this abstraction, what to do when these two requirements conflict. In traditional software engineering, a human developer makes these micro-decisions and they remain implicit. With AI generation, the model makes them and they become explicit — but they are still being made.

The failure mode I keep seeing: a team adopts an AI coding tool, starts shipping code faster, and the code looks better. Better naming, cleaner abstractions, more complete implementations. The velocity metrics look great. And then something breaks in production that the tests did not catch, or the feature turns out to solve a slightly different problem than the one the stakeholder actually described.

What happened? The AI generated code that looked like a good execution of the plan. But the plan itself had a gap. The AI did not fill the gap — it generated code that was a fluent interpretation of an incomplete specification. The gap became embedded, not fixed.

The factory metaphor is seductive precisely because it makes the problem look like an execution problem. If the code looks right and the tests pass, the work is done. But the real question is always: done relative to what spec? And that question lives in the design phase, not the execution phase. No amount of fluent code generation closes a spec gap. It just makes the gap harder to see.

This is why "AI-assisted code review" tools feel underwhelming in most organizations. They evaluate code against code conventions and patterns. They are excellent at identifying execution problems: style violations, missing null checks, resource leaks. They are nearly useless at identifying spec problems: is this actually what the feature should do? Is the underlying assumption correct? Does this code do the right thing when the edge case at the boundary of the spec is encountered?

The sharper version: if your AI coding tool is generating fluent code, you are getting better execution of an unchanged spec. If the spec is wrong, you are now failing faster and more confidently. That is not an improvement.

What does this mean in practice?

First, it means the bottleneck for AI-augmented development is almost never the coding step. It is the specification step. The work of being precise about what you want, what the edge cases are, what the success criteria actually mean — that work does not become faster with AI. It becomes more important, because a faster executor on a wrong plan compounds the error.

Second, it means quality gates for AI-generated code should evaluate the spec coverage, not just the code quality. Does the generated code handle the cases that were specified? Were the unspecified cases actually unspecified, or did the AI silently assume something about them that may not hold?

Third, it means the teams that will get the most value from AI coding tools are not the ones with the fastest velocity. They are the ones with the clearest specs. The AI amplifies spec quality. It does not replace it.

The uncomfortable conclusion: most engineering process failures in AI-augmented development are spec failures, not execution failures. The factory metaphor makes it easy to look at the wrong problem. Code fluency is seductive. Correctness is what actually matters.

---

*Word count: ~750*
