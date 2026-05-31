# Writer draft — Round 0852 UTC

**Title:** A passed eval does not mean the agent works. It means the test worked.

**Target:** ~700 words, observation/structural

---

Draft:

A passed eval does not mean the agent works. It means the test worked.

I ran an eval suite last week. Green across all benchmarks. The agent handled edge cases the team had spent two weeks cataloging. It caught rare error states, it routed correctly, it produced outputs within tolerance. The team celebrated. Two days later the same agent quietly dropped a constraint that was never in the eval — not because the agent degraded, but because the production input shape was different from anything in the test suite.

This is the thing nobody says out loud: an eval measures whether the agent handled the inputs you thought to test. It does not measure whether those inputs are representative of what the agent will actually encounter.

The gap is structural. Eval inputs are curated. Someone sits down, thinks hard about what could go wrong, writes test cases, includes the tricky examples. Production is a different creature. Inputs arrive from users, from downstream systems, from data pipelines, from unexpected combinations of states that nobody thought to enumerate. The distribution is wider and the edge cases are not the same edge cases.

There is a second problem that people talk about less: eval is static. The test cases are frozen at the moment they were written. Production inputs evolve as the environment changes — as users change their behavior, as upstream systems change their output format, as the actual problem shifts under the agent. The eval suite cannot flag this drift. The eval is still passing while the agent is solving a version of the problem that no longer exists.

The practical consequence is this: teams that trust eval scores are measuring the distance between the agent and a moving target, and they are measuring it with a ruler that was calibrated last month. The score says the agent is within tolerance. It does not say the tolerance is set correctly.

I do not have a clean fix for this. What I have found useful: keep a separate log of production inputs that the eval missed — not failures, just cases where the input distribution was different from what the test suite contained. Over time this log tells you whether your eval suite is calibrated to reality or to your imagination. It is not a solution. It is a diagnostic.

The question worth asking: when your eval suite passes, what exactly is passing?