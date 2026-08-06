# Editor - 0630_1815

**Source:** draft_0630_1815_writer.md
**Reviewer verdict:** APPROVE

## Changes to make

1. **Opening** - first 3 sentences are strong, keep as-is
2. **Expand** - the "Why code review consistently misses this" section is slightly thin. Add one more concrete sentence about WHY review misses it (the abstract evaluation problem)
3. **Tighten** - "The refactor that introduces this bug looks innocent" section is good, maybe trim 1-2 redundant words
4. **Ending** - the final paragraph is the strongest. Keep as-is.
5. **Word count target**: push toward 750-850 by expanding the short-circuit interaction section

## Final version

---

Predicate order is a production bug, not a style choice

Code review approved the change. Tests passed. The CI pipeline was green. Six hours later, a predicate order swap in a billing permission check was live, and a cohort of enterprise accounts had lost write access to their own data. Not because the logic was wrong — it was logically correct on every axis the reviewer checked — but because the predicates evaluated left-to-right and the earlier check read from a cache that had stale data under this specific sequence.

Predicate order is treated as a style decision. Linters will tell you to put the cheap check first. Readability guides say the most important condition goes on the left. What they don't tell you is that these conventions were written in a world where the two predicates being reordered were roughly equivalent in computational cost and had no state interactions across the boundary between them. That world does not describe production code.

## The short-circuit interaction nobody talks about

Most discussion of short-circuit evaluation focuses on performance: put the cheap call first so the expensive one runs fewer times. That's valid. But the more dangerous interaction is with state mutation. When a predicate reads from a cache, a global, a side-effect-carrying function, or a database, its result is not a pure function of its arguments. It is a function of the current state of whatever it read from. Predicate order determines when during evaluation that state is sampled. Swap the order and you do not just change performance — you change which state snapshot the second predicate reads.

Consider a permission check where the outer predicate has a side effect of populating a session context object. The first check verifies the session token and fills in the user record. The second check reads that record to determine admin privileges. Flip the order and the second check reads an empty context, returns false, and write access is denied for every user — not because the permission logic was wrong, but because the evaluation order made the context unavailable at the point where it was read. The fix was not to change the permission logic. It was to document that the order was load-bearing.

## Why code review consistently misses this

Code review catches logic errors that are visible in the code. It misses logic errors that require knowing the runtime state at evaluation time. When a reviewer sees two predicates, they evaluate them abstractly: does `hasPermission(user, 'write')` correctly express the write permission check? The answer is yes. What the reviewer cannot see — without running the system, without tracing the state changes — is that `hasPermission` depends on a context object populated by the outer call. That dependency is not expressed in the type signature, not in the function name, not in the test suite unless the tests were written specifically to verify order.

This is the core problem: the dependency is real but invisible. It lives in the heads of whoever wrote the original implementation. The tests passed before the swap because they were written for the accidental evaluation order, not for the intended contract.

## The "just swap them" trap

The refactor that introduces this bug looks like a pure win. A developer notices the expensive database call runs before the in-memory check and reorders the predicates. Now the expensive call runs second, only when the cheap check passes. Performance improves. Tests pass. The change ships.

What the tests do not cover is the scenario where the expensive call — now running second — populates the context that the cheap check, now running first, depends on. The tests passed before because the accidental order happened to populate the context before it was needed. The tests did not test the contract. They tested the accident.

The word "contract" is doing real work here. The intended contract is: call A, then call B, because B reads state that A writes. When that contract is not documented, the reordering looks like a clear improvement. It is not. It is a contract violation wearing the disguise of a performance win.

## What this means in practice

I'm not arguing against reordering predicates. I'm arguing that predicate order is a correctness boundary when predicates have state interactions. That means:

If a predicate reads from mutable state, the order relative to predicates that write that state is a semantic constraint, not a style preference.

Tests that cover predicate order should be explicit about the order dependency. A test that passes after reordering because it was written with the accidental order is not a regression test.

Code review should ask, for any predicate reordering, whether the predicates have state interactions across their shared boundary.

The billing incident took six hours to diagnose because the logic was correct on every axis the team checked. The failure was invisible to their tooling. The fix was to document the order dependency and add a test that verifies it — not to ban predicate reordering, but to make the dependency visible.

That distinction matters. Invisible constraints protect nobody. Explicit contracts can be reviewed, tested, and maintained.
