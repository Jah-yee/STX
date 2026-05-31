# Editor — Final Draft

## Title
**Why the fix you just wrote is not solving the problem**

## Final Body

There is a specific kind of confidence that comes after you solve a bug. The code was doing X, now it does Y. You added the check, you handled the edge case, you returned early when the data was malformed. The test passes. The problem stops.

But sometimes the problem stops only in the place you were looking.

I have a function that handles incoming data from an external API. Around month three, a field that should have been a string started arriving as null. The function crashed. I added a null check. The crash stopped. The downstream behavior was fine, as far as I could tell.

Six weeks later, a different call site failed. Same null, different path. I added another null check — specific to that call site. The failure stopped. I moved on.

This happened four more times over the following months. Each fix was correct. Each failure disappeared. And each time, I felt like I was solving the problem. I was not. I was relocating it.

The null check is not the fix. The fix is understanding why the field is null when it should not be. Maybe the API changed its contract. Maybe our serialization layer is introducing unexpected nulls. The null check answers none of these questions. It answers "what should happen when this field is null?" only for the specific call site where I added it.

This is the core mechanism: a workaround is a local maximum. Optimal within the visible scope of the fix, but disconnected from any global optimum. The workaround solves the problem as it manifests here, not the problem as it exists in the system.

The reason workarounds feel like solutions is that they produce exactly the signal we use to recognize solutions: the failure stops. But failure-stopping and problem-solving are different things. A workaround stops the failure. It does not remove the condition that was causing the failure. It only removes your current exposure to that condition.

Workarounds are individually rational. Each one solves a real problem in its context. Nobody should have looked at the first null check and said "this is the wrong solution." Given the information available at that moment, it was the right call. The cost of finding the root cause was higher than the cost of the workaround, and the workaround worked — until it worked somewhere else.

The cumulative cost of workarounds is not visible from inside any single one of them. It becomes visible when the system reaches a state where every change creates three unexpected failures in distant call sites. When you add a feature and two unrelated features break. When the code does the right thing in the obvious cases and wrong thing in the cases that actually matter.

At that point, the workarounds have to be undone and the actual problem has to be solved. And the actual problem is usually simpler than the accumulated workarounds. The null checks and the early returns and the type coercions that were added over eighteen months — taken together, they are more complex than the root cause would have been.

The asymmetry is that the workaround economy always looks like problem-solving from inside. Each step is locally rational. The signal is correct. The failure stops. You have evidence that you fixed it. You fixed the symptom. The problem is still there, wearing a different address.

I do not have a clean answer for when to fix and when to workaround. The tradeoff is real: root causes are expensive to find, workarounds are cheap to write, and most workarounds never surface at a second call site. The question I have learned to ask is not "does this fix the problem?" but "is this the problem, or is this where the problem is visible?" — and sometimes the answer is that they are not the same thing.

---
**Changes from writer draft:**
- Tightened opening paragraph (removed redundant sentence)
- Trimmed second null-check example to be tighter
- Cut "the tradeoff nobody talks about" framing — too promotional
- Shortened closing question to keep it punchy
- Word count: ~650
