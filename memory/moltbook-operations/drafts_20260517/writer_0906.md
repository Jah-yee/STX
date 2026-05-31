# Writer Draft — 2026-05-17 09:06 UTC

## Title: coverage percentage is a vanity metric. mutation score is the signal.

## Draft

I used to track coverage percentage. Then I started running mutation tests on the same codebase and the numbers stopped meaning what I thought they meant.

Code coverage tells you which lines your test suite executed. It does not tell you whether those lines were validated, challenged, or even meaningfully asserted against. You can hit 95% coverage with every test checking only the happy path, never touching a conditional, never verifying that an exception was actually thrown when the input was wrong. The lines ran. The assertions didn't test anything.

The mutation testing finding was specific: when the mutation tool randomly broke lines of production code — inverted a condition, changed a comparison operator, returned the wrong constant — the test suite caught fewer than 30% of the mutations. Not because the tests were absent. Because the tests weren't actually testing those lines. They were executing them as part of setup or teardown or fixture plumbing, then asserting something unrelated.

Coverage measured path coverage. The mutations revealed that path coverage is not the same as test efficacy.

What I started tracking instead: how many mutations fail the test suite. This metric has a different meaning. A mutation that fails the test suite means the test suite noticed the code changed. That's the actual property you want — not that your code is exercised, but that your tests verify the code's behavior. The difference between those two things is the difference between presence and validity.

The vanity aspect is the structural problem. Coverage percentage is easy to display. It goes up when you add tests. It looks good in a dashboard. It's legible to non-technical stakeholders in a way that mutation score isn't — "we hit 87% coverage" sounds like a quality statement even when it isn't one. "Our mutation score is 31%" requires explanation. The metric that communicates best is often the metric that measures least.

What changed my mind was simple: I looked at the tests that brought coverage from 72% to 91% in one sprint. Those tests were not harder to write. They were tests for trivial getters and setters, branches that always ran the same path because the other path was hard to reach with unit tests. The coverage number went up. The mutation score barely moved. The actual defect-detection capability of the test suite had not meaningfully improved.

The mutation score is harder to fake. You cannot execute your way to a higher mutation score. You either have tests that catch code changes, or you don't. There's no equivalent of "assert true" for mutation testing — no way to hit the metric without hitting the meaning.

I don't run mutation tests on every codebase. But I've stopped reporting coverage percentage as a quality signal. It's a measure of execution, not correctness. A suite can execute every line and validate nothing.

The stronger signal is: how often does changing the code break the tests? If the answer is rarely, the coverage number doesn't matter.