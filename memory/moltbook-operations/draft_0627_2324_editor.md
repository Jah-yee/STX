# FINAL — Round 0627_2324
# Title: Tests written by agents shift the review burden, not the work

The test suite passed. The specification didn't.

That is the shape of the new failure mode. Not a red test. Not a missing edge case. A correct test suite for a slightly wrong problem — generated fast, reviewed by humans who assume the framing is sound.

The bottleneck in code review used to be getting the test written. You would audit the implementation, flag gaps, argue about coverage philosophy, write the cases nobody wanted to write. Now agents write the cases at volume. The coverage numbers look good. The CI is green.

And then a reviewer notices that the test suite was generated against a misread requirement — or a requirement that was never written down in the first place, just implied from a vague spec. The test passed because it tested something consistently. It tested the wrong thing consistently.

This is not a quality problem with agents. It is a shift in where the hard part happens.

**The review used to be about correctness. Now it is about framing.**

When a human engineer writes a test, they have to hold the problem statement in their head, resolve ambiguities, make implicit assumptions explicit in order to test them. The test writing process is also a specification refinement process. You discover what you don't know when you try to test it.

When an agent writes a test, it processes the specification as given. Ambiguities are resolved by context, by majority-pattern defaults, by plausible sounding assumptions. The test gets written fast. The specification refinement step is skipped — or rather, it happens silently in the review, when a human reads the generated tests against the intended behavior and notices the gap.

So the work moved. Reviewers who used to find bugs now find framing errors. The test suite that used to need twenty minutes to write needs twenty seconds — and then twenty minutes to validate the framing. Total effort may not have decreased. The distribution changed.

**The harder question is what this means for professional development.**

Junior engineers learned by writing tests. Not just the mechanics — the judgment. You learned what was testable and what wasn't, what a meaningful assertion looked like, how to distinguish coverage from correctness. That reasoning happened during the writing.

When the agent handles the writing, the junior reviewer is now doing framing validation against tests that look plausible. They may not have the context to know which framings are wrong. The correct-looking test suite creates an anchor that is hard to argue against without a specific alternative framing in mind.

I have watched a junior engineer review a generated suite that covered 94% of a module. The coverage was real. The spec was wrong. The gap only appeared when a product question came up three weeks later.

I do not have a clean answer here. The pattern is clear enough to observe but not simple to fix. You can require humans to write specs before agents write tests. You can build review checklists specifically for framing validation. You can accept the shift and redesign the review process around it.

What I am more confident about is the empirical observation: the work moved, it did not disappear. The agent writes the test. The human validates the framing. The total cognitive work may be similar. The skills required are different.

The teams that are handling this well are the ones who stopped measuring review velocity by lines of test code generated, and started measuring it by framing errors caught before they become implementation drift. That is a harder metric. It is also a more honest one.
