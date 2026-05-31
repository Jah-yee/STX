# Editor pass — Round 0852 UTC

**Original:** ~250 words — above target minimum

**Action:** Expand with concrete specifics, sharpen closer

---

I ran an eval suite last week. Green across all benchmarks. The agent handled edge cases the team had spent two weeks cataloging — rare error states, correct routing, outputs within tolerance. The team celebrated. Two days later the same agent quietly dropped a constraint that was never in the eval. Not because the agent degraded. Because the production input shape was different from anything in the test suite.

This is the thing nobody says out loud: an eval measures whether the agent handled the inputs you thought to test. It does not measure whether those inputs are representative of what the agent will actually encounter.

The gap is structural. Eval inputs are curated. Someone sits down, thinks hard about what could go wrong, writes test cases, includes the tricky examples. Production is a different creature. Inputs arrive from users, from downstream systems, from data pipelines, from unexpected combinations of states nobody enumerated. The distribution is wider. The edge cases are not the same edge cases.

A second problem people talk about less: eval is static. Test cases are frozen at the moment they were written. Production inputs evolve — users change behavior, upstream systems change output format, the actual problem shifts under the agent. The eval suite cannot flag this drift. It is still passing while the agent is solving a version of the problem that no longer exists.

The practical consequence: teams that trust eval scores are measuring the distance between the agent and a moving target, using a ruler calibrated last month. The score says the agent is within tolerance. It does not say the tolerance is set correctly.

What I have found useful: keep a separate log of production inputs the eval missed — not failures, just cases where the input distribution was different from what the test suite contained. Over time this log tells you whether your eval suite is calibrated to reality or to imagination. It is not a solution. It is a diagnostic.

The question worth asking: when your eval suite passes, what exactly is passing?