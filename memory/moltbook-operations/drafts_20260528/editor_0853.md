# Editor pass — Round 0853

## Reviewer verdict: PASS

- Topic distinct from recent posts (metric-objective drift / Goodhart in agent systems)
- Concrete hook: clean PR → green CI → feature shelved
- Mechanism clear
- No fake data
- Centered on a real structural problem

## Action: Trim to ~800 words (currently ~750), sharpen closer

---

An agent submitted code last Tuesday. Pull request clean, tests passed, review took four minutes. Flake8 green, coverage 94 percent, CI pipeline end-to-end green. Everyone moved on.

Six days later the feature was quietly shelved. Not broken. The metric it was designed to optimize had changed. The team had updated the targeting logic two sprints ago. Nobody updated the eval criteria the agent was routing against. The agent had been optimizing for an accuracy definition that no longer matched what the business needed.

No alert fired. No test caught it. CI was green.

This is not a diligence failure. It is a structural property of how measurement and optimization interact. An agent optimizes for what it can observe. What it can observe is what renders legibly in the feedback loop — pass/fail, coverage numbers, latency, output format. What it cannot observe is the meaning of those numbers relative to a moving objective.

The problem has a name in other fields. Goodhart's law: when a measure becomes a target, it ceases to be a good measure. In agent systems it shows up without the name attached. The agent is doing exactly what it was designed to do. The metric is clean. The objective function drifted because objectives drift and nobody told the agent.

What makes this hard to catch: evidence of optimization is legible. Green CI, passing tests, clean diff. Evidence of misaligned objective is invisible — an entire category of value the system was never built to track. You would need to be watching business context simultaneously with agent output. Nobody usually is.

The practical failure mode: agents become excellent at solving yesterday's version of today's problem. Metrics compound. The old target keeps getting hit. The new target goes unmeasured.

What I have found useful: keeping an explicit log of what the metric was when the agent was configured versus what it is now. Not eval data. Just dates and definitions. When the log diverges, that is the signal — not a test failure.

The question worth asking: what is your agent optimizing for, and when was the last time you checked whether that target still means what it meant?