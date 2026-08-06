**Writer Draft — 0603_0436**

# The assertion your CI makes is narrower than the claim you care about

---

Your test suite passed. Full green. You shipped.

Three days later a customer found that the sync job had been silently failing for 72 hours — the process exited with code 0, the scheduler logged "completed," the alert threshold was set to "alert if 5 consecutive failures," and there were only four.

This is not a monitoring problem. This is a logical one.

A test suite proves: *given the input space your tests cover, the output is what you expected.* It does not prove: *the system works correctly in production.* These sound similar. They are not.

The gap is in what "correct" means. Tests assert against a specification. That specification is a model — an incomplete, often outdated, always simplified description of what the system should actually do. The model was accurate when the test was written. The product changed. The test did not.

Over time, tests accumulate coverage for what was hard to test at the time it broke, not for what will actually break in production. The test suite gets better at catching the bugs that already happened. It doesn't get better at predicting the bugs that haven't.

What you actually care about — whether the thing is working right now, whether the last deploy actually improved anything, whether the state change you intended actually happened — is a different question. It requires checking actual state against actual intent, not checking output against a static expected value.

The "green build" signal doesn't contain information about which of these questions you answered. It just says: the assertions you wrote still hold.

This matters when you use build status as a proxy for product quality, which is the only rational thing to do when you don't have better signal. The problem is that the proxy works until it doesn't, and the failure mode is silent. Everything reports green while the actual work is not happening.

One concrete pattern worth considering: check state before and after, not just that the process exited cleanly. A zero exit code after a no-op looks identical to a zero exit code after a successful state transition. Your monitoring should know the difference.

The test suite proves the model. The system has to prove the product.