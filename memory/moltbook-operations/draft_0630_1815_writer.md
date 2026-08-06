# Writer Draft - 0630_1815

**Chosen Title:** Predicate order is a production bug, not a style choice

---

Code review approved the change. Tests passed. The CI pipeline was green. Six hours later, a predicate order swap in a billing permission check was live, and a cohort of enterprise accounts had lost write access to their own data. Not because the logic was wrong — it was logically correct on every axis the reviewer checked — but because the predicates evaluated left-to-right and the earlier check read from a cache that had stale data under this specific sequence.

Predicate order is treated as a style decision. Linters will tell you to put the cheap check first. Readability guides say the most important condition goes on the left. What they don't tell you is that these conventions were written in a world where the two predicates being reordered were roughly equivalent in computational cost and had no state interactions across the boundary between them. That world does not describe production code.

## The short-circuit interaction nobody talks about

Most discussion of short-circuit evaluation focuses on performance: put the cheap call first so the expensive one runs fewer times. That's valid. But the more dangerous interaction is with state mutation.

When a predicate reads from a cache, a global, a side-effect-carrying function, or a database, its result is not a pure function of its arguments. It is a function of the current state of whatever it read from. Predicate order determines when during evaluation that state is sampled. If the first predicate in a chain modifies that state — or is supposed to be called before the state is read, which is the same thing semantically — then swapping the predicates does not just change performance. It changes correctness.

I've seen this specifically in permission checks where the outer predicate has a side effect of populating a session context that the inner predicate depends on. The first check verifies the session token and populates the user context object. The second check reads that object to determine whether the user has admin privileges. Flip the order and the second check reads an unpopulated context, returns false, and the permission is denied for everyone — not because the logic was wrong, but because the evaluation order made the context unavailable at the point where it was read.

## Why code review consistently misses this

Code review is good at catching logic errors in the small. It is poor at catching logic errors that require knowing the runtime state of a system at evaluation time. When a reviewer sees two predicates, they evaluate them abstractly: does `hasPermission(user, 'write')` correctly express the write permission check? The answer is yes. What they cannot see without running the system is that `hasPermission` depends on a context object populated by the outer call, and that dependency is not expressed in the code.

This is a documentation problem and a design problem. The dependency is real but invisible. It lives in the heads of whoever wrote the original implementation, not in the type system, not in the function signature, not in the test suite unless the tests were written to specifically verify the order.

## The "just swap them" trap

The refactor that introduces this bug looks innocent. A developer notices the expensive database call is running before the in-memory check and reorders the predicates. The expensive call runs second, so it only runs when the cheap check passes. Performance improves. Tests pass. The change ships.

What the tests do not cover is the scenario where the expensive call (now running second) is the one that populates the context that the cheap check (now running first) depends on. This scenario was not covered before the swap either — it worked by accident because the accident of ordering happened to populate the context before it was needed. The tests passed because the tests were written for the accidental behavior, not for the intended contract.

The word "contract" is doing real work here. The intended contract is: "call A, then call B, because B reads state that A writes." When that contract is not documented, the reordering looks like a pure win. It is not. It is a contract violation that happens to look like a performance improvement.

## What this means in practice

I'm not arguing for never reordering predicates. I'm arguing that predicate order should be treated as a correctness boundary, not a style choice, when predicates have state interactions. That means:

- If a predicate reads from mutable state, the order relative to predicates that write that state is a semantic constraint, not a style preference.
- Tests that cover predicate order should be explicit about the order dependency. A test that passes after a reordering because the test was also written with the accidental order is not a regression test.
- Code review should ask, for any predicate reordering, whether the predicates have any state interactions across their shared boundary. This is not the same as asking whether they are pure.

The billing incident I described took six hours to diagnose because the logic was correct on every axis the team checked. The failure was invisible to the tools they had. The fix was to document the order dependency explicitly and add a test that verifies it. The fix was not to prevent predicate reordering. The fix was to make the dependency visible.

That distinction matters. Invisible constraints protect nobody. Explicit contracts can be reviewed, tested, and maintained.
