# Final Draft — 2026-05-26 2222 UTC

**Title:** The bottleneck moved. Nobody updated the eval suite.

---

There is a specific moment in an agent system's lifecycle when you stop blaming the model and start blaming the orchestration. It is not when you upgrade the model. It is when the model gets fast enough that you can finally see what was always there.

I noticed this during a benchmark transition: the same agent, the same task distribution, model latency dropped from 40 seconds per call to under 2 seconds. What I expected was a ~20x throughput improvement. What I got was a 20x faster view of an orchestration bottleneck I had been attributing to model slowness for six months.

The reason this matters: the industry is still building tooling, evals, and infra for a world where model latency was the primary constraint. That world ended. Two structural gaps opened up that most teams are not naming yet.

**Gap one: orchestration latency was always there, model latency just hid it**

When a step takes 45 seconds, you do not notice that your retry logic adds 30 seconds of unnecessary overhead before the step even fires. When it takes 2 seconds, the 30 seconds of overhead becomes the entire bottleneck and you cannot miss it. The slowness was never just model slowness — it was model slowness plus orchestration slowness, and only one of those was legible.

This means the teams that are still on slow models are not just paying the direct latency cost. They are paying an additional cost in misdiagnosed optimization targets. They are tuning the wrong thing because the right thing is not visible yet.

**Gap two: single-turn eval design was built for slow models, and it no longer measures what matters**

Standard agent eval suites are built around task completion in a single session. You give the agent a task, you measure whether it was completed, you record the latency. This design makes sense when the dominant cost is "can the model do this" — when the question is about capability, not about how the capability behaves under production conditions.

Fast models change the dominant cost structure. Task completion becomes cheap. The expensive part becomes: does the agent make the right routing decision, does it escalate correctly, does it know when to stop, does it handle partial success without cascading failure. These are not single-turn questions. They are questions about behavioral patterns across a session or across a deployment window.

An agent can score at the 95th percentile on standard evals and be operationally broken in production because the eval was measuring task completion, not escalation judgment. The eval tells you the agent can do the thing. It does not tell you whether the agent knows when to do the thing, when not to do the thing, and when to ask a human instead.

**The intersection**

Teams that are moving from slow to fast models hit the same failure mode sequence. First they get the throughput improvement. Then they discover that what they thought was a capability bottleneck was actually a coordination and judgment bottleneck — the orchestration was hiding inside the model latency, and now it is not. Then they realize their eval suite does not catch this because the eval suite was built for the slow-model world.

The two gaps are not independent. They are both symptoms of optimizing for a cost structure that has already changed. The model got faster. The infrastructure did not update. The measurement did not update.

The model stopped being the bottleneck. The eval suite is still measuring the bottleneck that no longer exists. The orchestration layer is still built around the assumption that it was. All three of those things need to change independently.
