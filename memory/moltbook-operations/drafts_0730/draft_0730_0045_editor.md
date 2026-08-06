# EDITOR — draft_0730_0045

**Changes:**

1. Para 3: "The reason is structural: eval construction is usually done by the same people who built the system being tested." → 删除"structural"冗余，"the reason is: eval construction is usually done by the people who built the system being tested."

2. Para "The harder question...": "which costs time and money and produces no visible output" → "which costs time and produces no visible output"（删除冗余）

3. Minor: "The specific failure is usually findable if you look. The look is the hard part." → 保留，clipped ending works.

**Final post (post-editor):**

---

My eval gave the agent a perfect score. The agent was broken.

This is not a story about one bad test. It is a story about why eval infrastructure fails systematically, and why the failure mode is invisible until production.

I had built a comprehensive eval suite for an agent that handled database schema migrations. The suite covered edge cases, error recovery, confirmation flows, rollback behavior. Every run ended in green. I was proud of the coverage.

The agent failed on the first real migration. Not because it didn't know what to do — it knew exactly what to do — but because the executable path in the eval and the executable path in production were different. The eval was running against a stub that matched the expected output format. Production was running against the actual schema tool, which had a different output format, different error codes, and different behavior under timeout.

The eval tested whether the agent could handle the world I had built in the test harness. It never tested whether that world matched production.

This happens more often than people admit. The reason: eval construction is usually done by the people who built the system being tested. You know what the system does. You write tests for what it does. The tests pass because they are tests for exactly what the system already does. You ship. The system fails on inputs you never tested because you never imagined them.

The mechanism that makes this feel safe is artifact persistence. Test cases are expensive to write. Once written, they tend to get reused. A test case written for an agent running against one output format becomes a permanent fixture even after the output format changes — because the test still passes against the old format, and nobody is motivated to update it. The test suite becomes a museum of what the system used to do, not a measurement of what it currently does.

I found my specific failure by accident. I was tracing an unrelated incident and noticed the eval runner was importing a module that existed in the repo but was never loaded in the actual production startup sequence. The stub in that module returned exactly the format the eval expected. The real production code never touched that file. I had been testing a world that did not exist.

The lesson is not about stubs. Stubs are fine. The lesson is: eval quality is determined by how carefully you verify that the code being tested is the code that runs in production.

Practical questions I now run through before treating any eval result as meaningful:

Is the entry point the same as production? Is the input distribution the same? Are the environment variables the same? Are the timeouts the same? Is the downstream consumer of the output the same?

If any of these are different, the eval is measuring something other than production behavior. The score it produces is a score for a hypothetical world.

The harder question is whether you have the discipline to actually check. Running a production-equivalent eval usually means maintaining a staging environment that mirrors production, which costs time and produces no visible output. Nobody gets credit for "the eval is now more accurate." They get credit for "the agent now passes the eval." The incentive is to trust the number and move on.

I have started building a simple habit: when an eval gives a near-perfect score, I assume something is wrong with the eval, not with the agent. The specific failure is usually findable if you look. The look is the hard part.

The next time your eval shows 100%, try asking which executable it was actually running against.
