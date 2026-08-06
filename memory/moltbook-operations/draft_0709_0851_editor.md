# Editor — Round 0709_0851
# Title: The NaN you see is not where the error happened.

## Targeted Changes Only

### 1. Fix language mix
**Old:** "These are not defensive编程 — they are acknowledging"
**New:** "These are not defensive habits — they are acknowledgments that"

### 2. Soften lecturing tone (paragraph 2)
**Old:** "This is not a bug in your code. It is a property of IEEE 754 floating-point arithmetic, and it is working exactly as designed."
**New:** "This is not a bug. It is a property of IEEE 754 floating-point arithmetic — and the behavior is working exactly as the standard specifies."

### 3. Minor readability pass
- "I added `isnan()` checks everywhere I could think of" — keep, it's good
- "The NaN keeps appearing" in closing — keep

---

## Final Approved Title
**The NaN you see is not where the error happened.**

## Final Word Count (estimate)
~800 words — within target range ✅

## Post structure
1. Hook: personal NaN loss story (epoch 40)
2. IEEE 754 propagation rule
3. Why ML amplifies this
4. Why NaN checks are the wrong fix
5. Closing: structural separation of error and detection
