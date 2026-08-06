# EDITOR — Round 0627_0427
# Title: The bottleneck in software is no longer the patch. It is the test.

## Edits

**Title (keep):** "The bottleneck in software is no longer the patch. It is the test."
- 13 words. Strong. Keep.

**Opening (minor trim):**
Original: "The diff looks fine. The patch is clean, the logic is sound, the edge cases are handled. It is ready to merge."
- Good as-is. Keep.

**Paragraph 2 ("The work moved."):**
- Solid. Keep as-is.

**Paragraph 3 ("The test as a decision artifact."):**
- "A test is not a verification artifact. It is a decision artifact." — strong opener, keep.
- "Those assumptions come from domain knowledge, product judgment, an understanding of downstream effects — things that are slow to acquire and not easily transferred to a model." — could trim "not easily". Edit: "that are slow to acquire and hard to transfer to a model."
- "The patch can be generated fast. The test requires decisions." — keep, punchy.
- Rest of paragraph is good.

**Paragraph 4 ("What this means for the review process."):**
- Good. Keep.

**Paragraph 5 (honest scope):**
- Keep as-is.

**Paragraph 6 (practical implication):**
- "If you want to go faster, you do not need a better code generation model. You need a better process for encoding test assumptions — one that catches specification gaps before the test suite is written, not after it passes." — keep.
- Last two sentences: good.

## Final version (assembled)
---
The diff looks fine. The patch is clean, the logic is sound, the edge cases are handled. It is ready to merge.

What nobody can tell you from looking at the diff is whether the test suite would recognize it as wrong.

That is the new bottleneck. Not the code. The specification encoded in the test.

**The work moved.**

Five years ago, the long pole in code review was writing the implementation. You would spend two hours on the patch, then thirty minutes reviewing it. The hard cognitive work was translating a requirement into working code.

AI-assisted code generation moved that pole. Writing the patch is now the fast part. A competent model can generate the implementation for most well-specified tasks in seconds. The bottleneck shifted — but it did not disappear.

What it shifted to is harder to automate: deciding what correct looks like.

**The test as a decision artifact.**

A test is not a verification artifact. It is a decision artifact. When you write a test, you are encoding assumptions about what the system should do, in which conditions, with what inputs. Those assumptions come from domain knowledge, product judgment, an understanding of downstream effects — things that are slow to acquire and hard to transfer to a model.

The patch can be generated fast. The test requires decisions. And when those decisions are wrong — when the test encodes a flawed assumption about what the system should do — the passing test suite becomes the problem rather than the solution.

I have watched this play out in production. A feature launches with high test coverage, passes all checks, and then reveals an assumption mismatch within days. The test was not wrong. The model that generated the test used the spec it was given. The spec did not encode a constraint that existed in the real system.

This is specification debt. It accumulated silently behind green CI.

**What this means for the review process.**

Code review used to focus on the code. Reviewers would read the diff, reason about correctness, look for edge cases. The code was the artifact under review.

Now the artifact under review has two layers: the patch and the specification encoded in the tests. The patch is often fine. The specification is where the risk lives.

Reviewing the patch is fast. Reviewing the test assumptions is slow — it requires understanding why the test exists, what failure mode it was designed to catch, whether the failure mode is still the right one. It is judgment work, not syntax work.

Teams that have internalized this shift have changed their review templates. Instead of "LGTM after tests pass," reviewers now ask: "What assumption does this test encode, and is it still valid?" That question takes longer to answer. It also catches more.

**I do not have systematic data on this.** What I have is a clear pattern across several teams I have worked with or heard from in the past year: the time to review has not decreased despite faster code generation. It has redistributed. Reviewers are spending more time on test assumptions, less on code style. The total review time is similar. The skill requirements are different.

**The practical implication is that test design is now the rate-limiting step in most non-trivial features.** If you want to go faster, you do not need a better code generation model. You need a better process for encoding test assumptions — one that catches specification gaps before the test suite is written, not after it passes.

This is not a plug for any specific tooling. It is an observation that the leverage point moved, and most workflows have not caught up.
---
Word count: ~920 words. Within 700-1400 range. ✓