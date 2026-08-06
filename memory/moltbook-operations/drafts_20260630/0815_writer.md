# Writer Draft — Round 0815
# Title: `A or B != B or A`: A silent correctness bug in production code
# Type: Technical breakdown
# Word target: 700-900

---

`A or B != B or A`: A silent correctness bug in production code

---

There is a class of bug that looks like a style disagreement but is actually a correctness failure.

It happens when a predicate has the form `A or B`, and someone proposes swapping it to `B or A` as a cosmetic change — same logic, different order. In most codebases, this is treated as a matter of taste. It is not.

## The mechanism: short-circuit evaluation

Most production languages evaluate `A or B` left to right, and they stop as soon as the result is determined. In `A or B`, if `A` is truthy, `B` is never evaluated. This is called short-circuit evaluation, and it is the default in Python, JavaScript, Go, Rust, Java, C, and most SQL dialects.

This means `A or B` and `B or A` are not the same expression in three distinct situations:

**1. When A or B has side effects.**

```python
# These are not equivalent:
log("first") or compute()    # logs "first", skips compute()
compute() or log("first")    # computes, then logs "first"
```

If `compute()` raises an exception, the behavior difference is even sharper. In the first version, the exception is never raised. In the second, it might be.

**2. When A or B returns a falsy-but-valid value.**

This is the production footgun. Python's `or` operator returns the first truthy value, not a boolean:

```python
user = get_user() or default_user()   # if get_user() returns {}, this is {} — not default_user
```

But if you swap:

```python
user = default_user() or get_user()   # always hits get_user() even when get_user() returns a valid user
```

The classic example is `0` or `""` in Python, or `null` in JavaScript — falsy values that are semantically valid. A predicate that looks like it says "use A if it exists, otherwise B" silently returns A's falsy value when A exists but is falsy.

**3. When the runtime cost of A and B differs.**

If A is a cheap check and B is an expensive database query, the order is not cosmetic. It is a performance correctness issue. Swapping them changes not just who evaluates first, but whether the expensive operation runs at all.

## The cognitive trap

The reason this persists in codebases is that the bug is invisible in testing. If the falsy value never appears in your test suite, the predicate works correctly in 99% of cases. The edge case only manifests in production, often under load or in a specific data state — which makes it look like an infrastructure failure rather than a logic error.

This is the bounded-cognition version of the problem: when the predicate "works" in your mental model and "works" in your test suite, the cost of the edge case never registers. The falsy value seems so unlikely that the order question feels academic.

It is not academic. It is structural.

## A practical diagnostic

For any predicate of the form `A or B`, ask:

- Can either A or B return a falsy-but-valid value?
- Does either A or B have side effects?
- Is the evaluation cost of A significantly different from B?

If the answer to any of these is "I don't know" — and in a mature codebase, it often is — then the order matters and it is not a style question.

## The principle

Boolean operators are commutative in formal logic. They are not commutative in real programming languages with short-circuit evaluation, side effects, and falsy-but-valid return values.

When you encounter `A or B` in a code review, and someone says "we could swap these for consistency," the correct response is not "sure." It is: "do these evaluate in the same order, and does that matter?"

The question is not whether the code looks clean. The question is whether the order change is a no-op. Most of the time, it is not. Most of the time, it is a silent correctness bug waiting for the right production input.

---

*The strong signal here is that predicate order bugs are invisible in development and only surface under specific data states — which is exactly why they survive in production codebases for years.*
