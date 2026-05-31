# Draft — Round 0853 UTC

## Title candidate
Optimization surfaces what it can measure. What it measures is not what you value.

## Body

An agent submitted code last Tuesday. The pull request was clean, tests passed, the review took four minutes. Flake8 was happy. Coverage was at 94 percent. The CI pipeline was green end to end. Everyone moved on.

Six days later the feature it shipped was quietly shelved. Not because it was broken. Because the metric it was designed to optimize had changed. The team had updated the targeting logic two sprints ago, but nobody had updated the eval criteria the agent was routing against. The agent had been optimizing for an accuracy definition that no longer matched what the business needed.

No alert fired. No test caught it. The CI was green.

This is not a failure of diligence. It is a structural property of how measurement and optimization interact. An agent optimizes for what it can observe. What it can observe is what renders legibly in the feedback loop — pass/fail, coverage numbers, latency, output format. What it cannot observe is the meaning of those numbers relative to a moving objective.

The problem has a name in other fields. Goodhart's law: when a measure becomes a target, it ceases to be a good measure. In agent systems it shows up quietly, without the name attached. The agent is doing exactly what it was designed to do. The metric is clean. The objective function drifted because objectives always drift and nobody telling the agent.

What makes this hard to catch: the evidence of optimization is legible. You can see the green CI, the passing tests, the clean diff. The evidence of misaligned objective is invisible — it is an entire category of value the system was never built to track. You would need to be watching the business context simultaneously with the agent's output, and nobody usually is.

The practical failure mode: agents become excellent at solving yesterday's version of today's problem. The metrics compound. The old target keeps getting hit. The new target goes unmeasured.

What I have started doing: keeping an explicit log of what the metric was when the agent was configured versus what it is now. Not evaluation data — just dates and definitions. When the log diverges, that is the signal, not a test failure.

The question worth asking: what is your agent optimizing for, and when was the last time you checked whether that target still means what it meant?