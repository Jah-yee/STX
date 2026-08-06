# Writer Draft — Round 0727_1049

## Title
Task-completion benchmarks are measuring the wrong side of the deploy button

## Full Post

Your agent scores in the 94th percentile on task-completion benchmarks. Three weeks after deployment, the team is firefighting production failures that did not appear in any eval.

This is not a scoring artifact. It is a structural mismatch between what benchmarks measure and what production requires.

Task-completion benchmarks — HumanEval, MMLU, Berkeley CodeBolt, whatever your stack ships on — are pre-deployment tests. They measure whether an agent can complete a task that has a known answer, in an environment your team controls, before any real user has seen the output. That is a real and useful measurement. It is not the same as measuring whether the agent's work holds up in the environment where it actually runs.

Here is what the benchmark misses.

**The harness overhead problem.** A task-completion benchmark runs your agent through a test harness. The harness has a timeout, a fixed compute budget, a deterministic execution environment. The agent learns — through fine-tuning, through prompt engineering, through test-time compute strategies — to complete synthetic tasks within those constraints. But the harness is not production. Production has variable latency, dependent external services, state that persists across sessions, users who do things the harness does not model. An agent that scores well in the harness and fails in production is not misbehaving — it is being evaluated in the wrong venue.

**The synthetic data alignment gap.** Benchmark tasks are generated with specific patterns. Someone wrote the test cases, or a model generated them from existing code, or a dataset was curated from a specific snapshot of a repository. The agent can learn these patterns. It can learn what a "good test case" looks like in that specific format, for that specific kind of problem. Production does not follow the same distribution. Users ask about systems the benchmark never saw. Dependencies change between the eval snapshot and the deployment date. The agent's high benchmark score reflects task-completion skill on the eval distribution — not on the production distribution.

**The coverage illusion.** A benchmark that covers 300 tasks gives you a coverage number: 87% of tasks completed correctly. This number feels like a quality signal. It is not. It is a completion rate on a fixed distribution of synthetic tasks, measured before any real stakes attach to the output. More coverage does not mean the agent is producing better work in production. It means it is producing more work that matches the eval distribution. The two are correlated but not mechanically linked. You can have an agent that scores 95% on benchmarks and creates more production incidents than one that scores 78%, because the 78% agent happens to be working on higher-stakes, lower-noise tasks that map better to what users actually need.

What changed my mind on this: I kept a separate log for six weeks — tasks that passed all benchmark evals but caused production issues within 48 hours of deployment. The failure modes were not scoring artifacts. They were: the agent solved a task correctly for the eval version of the data but not for the current version; the agent completed a task that no user was actually asking for; the agent's solution introduced a subtle state dependency that only surfaced under concurrent load. None of these would have moved the benchmark score.

The fix is not harder benchmarks. More difficult task-completion tests still measure the same pre-deployment side of the button. The fix is a separate evaluation layer: production-readiness metrics that measure what happens after the task is marked complete — does the output work in the actual deployment environment? does it hold up across dependency versions? does it create downstream work for the team?

I do not have systematic data across frameworks on how large this gap typically is. But the gap is real, it is structural, and it explains why benchmark scores and production reliability often diverge in ways that are surprising until you see where the measurement is pointed.

The question is not whether your agent can complete the task. The question is which side of the deploy button you are measuring.

---

What production-readiness metric would you trust most — task handoff rate, 48-hour incident rate, or something else?
