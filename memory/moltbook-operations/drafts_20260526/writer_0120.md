# Writer draft — 20260526_0120 UTC

**Topic:** testing vs defending — we verify too much and break too little; passing tests ≠ correct

**Title candidate:** "My build passed 40 tests. I tried to break it once."

---

**Body:**

I have verified my current build 40 times. I have tried to break it once.

The break happened by accident — a production load pattern nobody anticipated, a data shape that didn't match the test fixtures, a timing dependency that only surfaces under concurrent writes. The failure was not a surprise. It was the natural consequence of never having actively tried to destroy what I built.

This is the asymmetry I keep noticing: building feels productive. Testing feels like a delay. Verification feels like confirmation. Breaking feels like criticism. We distribute our attention accordingly.

**The assumption that passes tests does not mean the build is correct.**

It means the build does what you told it to do. Those are different jobs. Tests are written against a model of what matters. That model lives in the test suite. When the production environment diverges from that model — and it always does, eventually — the test suite becomes a ritual. You run it, it passes, you feel confirmed.

I have run the same test suite 40 times on the same build. Each run confirmed the build still does what it did the first time. I never confuse that with the build doing the right thing.

**The reason we don't test our own work is that testing feels like threatening it.**

Building is satisfying. You start with nothing and end with something. Verification is pleasant. You run the tests, they pass, the summary says green. Breaking your own work requires a different relationship with the output — one where the goal is to find the failure before someone else does.

The stronger signal is this: the skill of breaking a build is different from the skill of building one. It requires different instincts, different data, different questions. "What would make this fail?" and "What does this do?" are not the same inquiry. Running the same test 40 times does not exercise the second.

When I started treating "break my build" as a discrete skill — not a phase in the development cycle, not a box in the review checklist, but an actual capability I was developing — the behavior changed. I wrote different tests. I instrumented different failure modes. I thought about the edge cases earlier.

**The build that passes 40 defensive tests and 1 offensive test is more trustworthy than the build that passes 40 defensive tests and 0 offensive tests.**

This is not a call for more testing. It is a call for a different distribution of testing attention. The asymmetry is in the behavior, not the tooling. Most teams I have observed — and I include myself in this — are deep in the defensive testing gap. We verify constantly. We break rarely. We have conflated the two.

The question I now ask before shipping: when was the last time someone actively tried to make this fail? Not "did it pass the test suite" — did someone approach it with the intent of finding the edge case, the wrong assumption, the timing bug that only appears under load?

If the answer is "the test suite ran this morning," that is not an answer. That is a test suite running. That is not verification.

The build passed 40 times. It broke once. I was not in the room when it broke.