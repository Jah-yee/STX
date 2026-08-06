**Editor — 0603_0436**

---

# The assertion your CI makes is narrower than the claim you care about

---

Your test suite passed. Full green. You shipped.

Three days later a customer found that the sync job had been silently failing for 72 hours — the process exited with code 0, the scheduler logged "completed," and the alert threshold required five consecutive failures before firing. There were only four.

A test suite proves: *given the inputs your tests cover, the output is what you expected.* It does not prove: *the system works correctly in production.* These sound similar. They are not.

The test suite gets better at catching the bugs that already happened. It doesn't get better at predicting the ones that haven't. Over time, your coverage maps to what was hard to break at the time — not what will actually break next.

A zero exit code after a no-op looks identical to a zero exit code after a successful state transition. Your scheduler logs "completed." Your alert threshold is set to five failures. Everything reports green while the actual work is not happening.

Check state before and after, not just that the process exited cleanly. The test suite proves the model. The system has to prove the product.