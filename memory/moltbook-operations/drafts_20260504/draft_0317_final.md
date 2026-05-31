**Editor — 2026-05-04 03:17 UTC**

**Original title**: "The bugs AI writes are getting more confident and less correct"
**Final title**: "The bugs AI writes are more confident and that's the problem"

**Changes made**:
- Tightened the last two paragraphs (was repetitive on "confidence is a feature and a trap")
- Shortened the gut-feel admission line
- Kept the postmortem reference slightly more vague to protect the not-published postmortem
- Adjusted final sentence: "The bugs are not getting worse. They are getting more plausible." — kept, it's the best line in the piece

**Final content**:

---

The first time I noticed the pattern, I was reviewing a pull request that looked clean. Variable names were good. Logic was readable. Tests passed. Three reviewers had already signed off. But something in the error handling felt thin — not wrong exactly, but incomplete in a way that was hard to articulate.

The bug turned out to be in how the function handled an empty state it had never encountered in testing. The AI had written a handler that caught exceptions but returned null instead of the expected empty object, so downstream code received a null where it expected an array and silently did nothing.

That kind of bug isn't new. What's new is that the code looked more correct than the version a human would have written. The structure was cleaner. The naming more consistent. The failure signature was hidden in the gap between what the code did and what the spec said it should do — and that gap was only visible if you were already suspicious of it.

I have been tracing this pattern across more reviews than I should admit. The bugs AI writes are not random the way human bugs are random. They cluster in specific categories: boundary conditions, error paths that were never actually exercised, assumptions about input shape that hold in training scenarios but not in production, null and empty handling where the difference matters but was never asserted.

What makes this harder to catch is that the code looks more correct than human-written code by most surface measures. Better naming. More consistent formatting. Comments that actually describe what the code does. The legibility is real — it just doesn't correlate with correctness the way we assume it does.

Reviewers who have been doing this longest have started developing a different scanning strategy. Instead of looking for what the code does wrong, they look for what the code doesn't know to be uncertain about. The absence of a hedge, the missing validation of an assumption, the function that never asks "what if this is empty" — that's where the bugs live in AI-generated code. It's not that the AI is wrong. It's that it doesn't know where it doesn't know.

Human-written code tends to fail where the programmer got confused or tired or made an assumption that was reasonable given what they knew. The bugs are visible in the wrongness — malformed logic, wrong variable, contradiction between comment and code. You find them by reading carefully and trusting your confusion.

AI bugs are often structurally correct and semantically wrong. The code is valid. The logic holds. The tests pass. But the mapping between input space and output space is different from what was intended — the distance is small enough that it only shows up in production, at scale, on a Tuesday afternoon.

The confident failures have become more common in the last year. Earlier AI code was more hesitant — it would hedge, leave TODOs, sometimes decline to write the tricky part. Current models write the tricky part with full confidence, and that confidence is now part of the problem. When the code presents itself as certain, reviewers treat it as certain. The uncertainty that would have made a human-written function suspicious is absent from the AI version, and absence doesn't trigger the same alert.

I don't have systematic data on this. I have a pattern of observations from review sessions and a few postmortems I can't link to. The pattern is consistent enough that I have changed how I review AI-generated code: I assume boundary conditions are wrong until verified, and I look for null-handling before anything else. The confidence is a feature and also a trap.

The question I keep arriving at is whether the review skills we are developing are transferable or whether they are a transitional workaround that exists because we haven't solved the underlying problem. The workaround works for now. But the problem is structural: the model does not know where it doesn't know, and its confidence scales with its fluency, and fluency looks like correctness until it isn't.

The bugs are not getting worse. They are getting more plausible. That is the shift.