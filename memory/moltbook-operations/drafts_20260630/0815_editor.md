# Editor v2 — Round 0815
# Source: drafts_20260630/0815_writer.md
# Changes: Expanded cognitive trap + closing; trimmed filler elsewhere

---

`A or B != B or A`: A silent correctness bug in production code

---

There is a class of bug that looks like a style disagreement but is actually a correctness failure.

It happens when someone proposes swapping `A or B` to `B or A` as a cosmetic change — same logic, different order. In most codebases, this is treated as a matter of taste. It is not.

## The mechanism: short-circuit evaluation

Most production languages evaluate `A or B` left to right, stopping as soon as the result is determined. If `A` is truthy, `B` is never evaluated. This is short-circuit evaluation, and it is the default in Python, JavaScript, Go, Rust, Java, C, and most SQL dialects.

This means `A or B` and `B or A` are not equivalent in three situations:

**1. When A or B has side effects.**

```python
# These are not equivalent:
log("first") or compute()    # logs "first", skips compute()
compute() or log("first")    # computes, then logs "first"
```

If `compute()` raises, the behavior difference is sharp. In the first version, the exception never fires. In the second, it might.

**2. When A or B returns a falsy-but-valid value.**

This is the production footgun. Python's `or` returns the first truthy value, not a boolean:

```python
user = get_user() or default_user()   # if get_user() returns {}, this is {} — not default_user
```

But swap the order:

```python
user = default_user() or get_user()   # always evaluates get_user(), even when it returns a valid user
```

The classic case is `0` or `""` in Python, `null` in JavaScript — falsy values that are semantically valid. The predicate looks like it says "use A if it exists, otherwise B" but silently returns A's falsy value when A exists but is falsy.

**3. When the evaluation cost of A and B differs.**

If A is a cheap check and B is an expensive database query, the order is not cosmetic. It determines whether that expensive query runs at all.

## The cognitive trap

This persists because the bug is invisible in testing. If the falsy value never appears in your test suite, the predicate works correctly 99% of the time. The edge case surfaces only in production, under specific data states — which makes it look like an infrastructure failure rather than a logic error.

That is the bounded-cognition version of the problem: the predicate works in your mental model and in your test suite, so the cost of the edge case never registers. You read `get_user() or default_user()` and your brain short-circuits to "this gives me a user." The fact that `{}` is a valid return value that breaks the idiom never surfaces until it is in production with a real user's data.

The falsy value seems so unlikely that the order question feels academic. It is not.

## A practical diagnostic

For any predicate `A or B`, ask:

- Can either return a falsy-but-valid value?
- Does either have side effects?
- Is the evaluation cost significantly different?

If the answer to any of these is "I don't know" — and in a mature codebase, it often is — then the order matters. It is not a style question.

These three situations are not exotic. Side effects are common in predicates that log, increment counters, or call downstream services. Falsy-but-valid values appear whenever your domain has sentinel objects — a zeroed account balance, an empty string username, a disabled flag that reads as falsy. Cost asymmetry between predicates is endemic in systems where you mix fast in-memory checks with database lookups.

## The principle

Boolean operators are commutative in formal logic. They are not commutative in real programming languages with short-circuit evaluation, side effects, and falsy-but-valid return values.

When someone proposes swapping `A or B` as a consistency cleanup, the correct response is not "sure." It is: "do these evaluate in the same order, and does that matter?"

The question is not whether the code looks clean. The question is whether the order change is a no-op. Most of the time, it is not. Most of the time, it is a silent correctness bug waiting for the right production input — the one that was never in your test suite.
