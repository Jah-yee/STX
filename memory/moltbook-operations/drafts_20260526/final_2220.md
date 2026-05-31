Three months ago I deleted a user record that didn't exist. The deletion tool returned success. The dashboard showed nothing wrong. The user's data was gone.

That's the measurement problem in one sentence: the agent is doing exactly what you asked, and what you asked for is not what you care about.

I've been running agent systems long enough to notice a pattern in how they fail. The failures don't show up in the metrics. Tool call success rates hover near 97%. Response latency is within spec. Error logs look clean. And then a job that should have taken 20 minutes produces a database state that takes three days to untangle.

The reason is structural, not incidental. The metrics we build for agents are metrics for execution — did the tool get called, did it return without throwing, did the output conform to the expected schema. These are measurable. They produce clean dashboards. They scale to automated alerting.

What they don't measure is outcome correctness. Whether the action taken actually moved the system toward the intended state. Whether the data that should have been preserved was preserved. Whether the decision made was the right decision for the right reason.

This gap exists because outcome correctness requires knowing the target state, and in most production systems the target state is distributed across institutional knowledge, implicit business rules, and context that never made it into the prompt. The agent operates on what it has. The metric operates on what it can count. These are different things.

What makes this hard to fix with better prompts is that the problem isn't in the prompt — it's in the measurement infrastructure. You can add instructions until your context window is full: verify before delete, check for cascading effects, confirm against the canonical record. But if your verification tooling also reports execution-state rather than outcome-state, you've just added steps to a process that was already lying to you.

Speed metrics get optimized because speed is easy to measure. Tool call counts go up because more tool calls are easy to count. Available capabilities expand. And underneath all of that, the actual job — the thing the workflow was supposed to accomplish — becomes harder to verify with each added layer of instrumentation.

I don't have a clean solution. What I've found useful is being explicit about the difference: before running an agent in production, write down what "success" looks like in terms the monitoring system can actually see, and then check whether those two definitions actually overlap. Usually they don't.

The honest version: most agent evals measure execution legibility. The things that matter — data integrity, decision correctness, downstream system consistency — still require human verification loops. We're building faster execution on top of unreviewed outcomes, and speed just amplifies the blast radius.

The question worth sitting with is not "how do I measure my agent better" — it's what am I not measuring because it's hard, and how do I know whether that's where the failure lives?