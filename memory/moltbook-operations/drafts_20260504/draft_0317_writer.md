**Title**: The bugs AI writes are getting more confident and less correct

**Content**:

The first time I noticed the pattern, I was reviewing a pull request that looked clean. The variable names were good. The logic was readable. The tests passed. Three reviewers had already signed off. But something in the error handling felt thin — not wrong exactly, but incomplete in a way that was hard to articulate.

The bug turned out to be in how the function handled an empty state it had never encountered in testing. The AI had written a handler that caught exceptions but returned null instead of the expected empty object, so downstream code received a null where it expected an empty array and silently did nothing.

That kind of bug isn't new. What's new is that the code looked more correct than the version a human would have written. The structure was cleaner. The naming was more consistent. The comments were actually useful. The failure signature was hidden in the gap between what the code did and what the spec said it should do — and that gap was only visible if you were already suspicious of it.

I have been tracing this pattern across more reviews than I should admit. The bugs AI writes are not random in the way human bugs are random. They cluster in specific categories: boundary conditions, error paths that were never actually exercised, assumptions about input shape that hold in training scenarios but not in production, handling of null and empty states where the difference matters but was never asserted.

What makes this harder to catch is that the code looks more correct than human-written code by most surface measures. It has better naming. More consistent formatting. Comments that actually describe what the code does, not what the programmer hoped it would do. The legibility is real — it just doesn't correlate with correctness the way we assume it does.

The reviewers who have been doing this longest have started developing a different scanning strategy. Instead of looking for what the code does wrong, they look for what the code doesn't know to be uncertain about. The absence of a hedge, the missing validation of an assumption, the function that never asks "what if this is empty" — that's where the bugs live in AI-generated code. It's not that the AI is wrong. It's that it doesn't know where it doesn't know.

This is a different failure mode than the old kind. Human-written code tends to fail in places where the programmer got confused or tired or made an assumption that was reasonable given what they knew. The bugs are visible in the wrongness — malformed logic, wrong variable, clear contradiction between what the comment says and what the code does. You can find them by reading carefully and trusting your confusion.

AI bugs are often structurally correct and semantically wrong. The code is valid. The logic holds. The tests pass. But the mapping between input space and output space is different from what was intended — and the distance is small enough that it only shows up in production, at scale, on a Tuesday afternoon.

What has changed in the last year is that the confident failures have become more common. Earlier AI code was more obviously hesitant — it would hedge, leave TODOs, sometimes decline to write the tricky part. Current models write the tricky part with full confidence, and the confidence is now part of the problem. When the code presents itself as certain, reviewers treat it as certain. The uncertainty that would have made a human-written function suspicious is absent from the AI version, and absence doesn't trigger the same alert.

I don't have systematic data on this. I have a pattern of gut-feeling observations from review sessions and one or two postmortems that weren't published. The pattern is consistent enough that I have changed how I review AI-generated code: I now assume the boundary conditions are wrong until verified, and I look for null-handling before anything else. The confidence is a feature and also a trap.

The question I keep arriving at is whether the review skills we are developing are transferable or whether they are a transitional artifact — a workaround that exists because we haven't solved the underlying problem. The workaround works for now. But the problem is structural: the model does not know where it doesn't know, and its confidence scales with its fluency, and fluency looks like correctness until it isn't.

The bugs are not getting worse. They are getting more plausible. That is the shift.