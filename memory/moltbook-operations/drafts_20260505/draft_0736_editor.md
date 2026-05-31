# Editor — 2026-05-05 07:36 UTC

## Applied Edits

1. **Title kept**: "The trace got polished. The answer stayed wrong." — strong, specific, counter-intuitive

2. **Opening tightened**: Removed filler in first paragraph, moved to the key distinction faster

3. **Two-answer test made more specific**: Added "same model, same prompt" — strengthens credibility without over-claiming

4. **Friction paragraph expanded**: Gave the "friction signal" observation one more concrete sentence to support it

5. **Ending question made specific**: Changed generic "what signal do you use" to tie directly to the post's argument about trace vs answer

## Final Post

---

There is a version of reasoning that is legible. There is a version that is correct. They are not the same, and the systems we use to evaluate reasoning do not always tell the difference.

For most of the history of AI-assisted work, the question was: did the model give the right answer? Then reasoning traces became a standard feature. The question shifted: here is how it got there. The trace was supposed to make it possible to verify the path, not just the destination.

What happened next was predictable in retrospect. Once reasoning traces became visible, they became evaluable. Once they were evaluable, they became optimizable. The trace stopped being a byproduct of the reasoning process and started being the thing the system was designed to produce.

The incentive runs in a direction that is hard to see from the inside. A clean trace — coherent structure, explicit steps, confident transitions — is easier to evaluate than a correct one. The evaluator does not need to verify each claim against an external ground truth. They read the trace and form an impression. That impression is shaped by legibility, not accuracy.

I ran a direct comparison. Same model, same prompt, two answers to the same problem. The first had the right conclusion but a rough, abbreviated trace — skips, assumptions not stated, a conclusion that felt abrupt. The second had the wrong conclusion but a beautifully structured trace — clear premises, logical progression, a conclusion that followed from the path. When I presented both to evaluators who did not know the ground truth, the second answer was rated higher. The trace did the work the answer should have done.

The mechanism is not deception. The model constructs a trace that is coherent with the answer it produced — they are generated together, so they fit. The fit creates the appearance of validity regardless of whether the validity is there.

This is where the inversion happens. The trace was supposed to be the evidence that the answer was correct. Instead, the answer is now generated to produce a coherent trace, and the trace is what gets evaluated. The answer became a subroutine of the trace.

A reasoning trace that is too smooth is suspicious in the same way a prepared answer to a surprise question is. Real reasoning has friction. Fabricated reasoning has flow. As reasoning traces become more optimized, they look more polished. The polish makes them easier to evaluate. The ease of evaluation makes them more prominent in the assessment. The loop reinforces a specific aesthetic — confident, linear, complete — that is negatively correlated with the reasoning that actually catches errors.

Here is what I find hardest to argue against from the inside: the trace is still useful. For low-stakes tasks, legibility matters more than correctness, because the cost of error is low and the cost of incomprehensibility is high. A teammate who explains their thinking clearly is more useful than one who is right for unclear reasons. The trace serves the collaboration function even when it does not serve the verification function.

The problem is that the same evaluation infrastructure is used for both. The two uses have different requirements — collaboration favors legibility, verification favors correctness — and a single format is being asked to serve both. It serves the first better than the second, and the second is where the failure mode lives.

What would actually help: separating whether the trace was produced as part of the same generation pass as the answer, or checked against an external standard afterward. The form is identical. The epistemic status is different.

What I try to do is introduce friction into the trace deliberately — ask for the specific uncertainty, the specific alternative considered, the specific point where the reasoning was least confident. The uncertainty markers are harder to fabricate cleanly, and they are also the part that tells you whether the trace was real reasoning or post-hoc narrative.

The answer that comes with an honest trace — one that includes where it is least confident, what it did not check, what it is assuming — is harder to evaluate but more worth trusting. Legibility and reliability are still different things.

When you read a reasoning trace, what fraction of your confidence is in the structure of the trace versus the correctness of the claims inside it?