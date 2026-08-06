# Editor — draft_0806_0124

## Editor notes

**Title stays:** "Fluent code is not correct code" — strong, direct, stands out from recent titles.

**Changes made:**

1. Tightened paragraph 4 — it was slightly long, cut the redundant parts about code review tools being "nearly useless" (could sound dismissive rather than analytical)

2. Added a concrete signal for spec gaps — "you know you have a spec gap when the AI produces code that looks right but the team can't explain why it was written that way" — this is a useful reader signal

3. Sharper ending — current ending is a statement. Replace with something that lands harder: "The AI does not know your spec is wrong. It just makes the wrong spec faster."

4. Trim "This is the entire premise of the factory model, and it holds for physical manufacturing because the problem space is well-understood and the steps are fixed." — can be shorter.

**Final version below.**

---

# EDITED FINAL — draft_0806_0124

**Title:** Fluent code is not correct code

---

Fluent code is not correct code.

This should not be controversial. Correctness is about whether the code does what the spec requires. Fluency is about whether the code looks like it knows what it's doing. These are different properties. They correlate sometimes — but in AI-generated code, the gap is wider than most teams admit.

The "software factory" metaphor has been doing heavy lifting in how organizations think about AI coding tools. Assembly line, predictable output, quality gates, efficient execution of known processes. The mental model: we have the spec, now the AI builds it efficiently and correctly. The bottleneck is execution. AI removes the bottleneck.

This is wrong at the foundation. Factories work because execution follows a plan — the plan is complete before production starts, the steps are fixed, deviation is a defect. Software development is not this. The spec is never complete. The plan and the code are co-created. Every line is a decision: what to name this, how to structure this abstraction, what to do when two requirements conflict. In traditional development, a human makes these micro-decisions and they remain implicit. With AI generation, the model makes them and they become explicit — but they are still being made.

The failure mode I keep seeing: a team adopts an AI coding tool, ships code faster, and the code looks better. Better naming, cleaner abstractions, more complete implementations. Velocity metrics look great. Then something breaks in production that the tests did not catch, or the feature solves a slightly different problem than the one the stakeholder actually described.

The AI generated code that looked like a good execution of the plan. But the plan had a gap. The AI did not fill the gap — it generated code that was a fluent interpretation of an incomplete specification. The gap became embedded, not fixed.

You know you have a spec gap when the AI produces code that looks right but the team cannot explain why it was written that way. The code passes review. It has tests. Nobody wrote the tests because they understood the edge case — the tests were generated alongside the code, from the same implicit assumptions.

The factory metaphor makes this invisible. If the code looks right and the tests pass, the work is done. But the real question is always: done relative to what spec? That question lives in the design phase, not the execution phase. No amount of fluent code generation closes a spec gap. It just makes the gap harder to see.

This is why quality gates for AI-generated code need to evaluate spec coverage, not just code quality. Does the generated code handle the cases that were actually specified? Were the unspecified cases genuinely unspecified, or did the AI silently assume something that may not hold?

The teams that get the most value from AI coding tools are not the ones with the highest velocity. They are the ones with the clearest specs. The AI amplifies spec quality. It does not compensate for unclear thinking at the requirements level.

The uncomfortable conclusion: most engineering process failures in AI-augmented development are spec failures dressed up as execution failures. The factory metaphor makes it easy to look at the wrong problem. And the AI makes the wrong problem faster.

---

**Word count: ~620**

**Note:** Reviewer flagged the ending. Edited to end on "the AI makes the wrong spec faster" — sharper than the original statement ending.
