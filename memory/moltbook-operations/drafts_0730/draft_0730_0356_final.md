# Round 0730_0356 — Writer Draft

**Title:** Coverage without a control group is just log hoarding
**Topic:** Coverage metrics in agent/eval systems measure activity, not improvement; the control group question nobody asks

---

Coverage hit 94%. Nobody asked what the number meant.

A team I worked with spent three months instrumenting their agent to cover more of their test suite. Scenario after scenario got added to the evaluation harness. Coverage climbed from 61% to 94%. Everyone felt good about the trajectory.

Six weeks after launch, the first major incident happened in a code path the agent had never touched. Not because the agent missed it—because nobody thought to cover it. The agent could not surface a problem nobody had thought to describe. Coverage told you what the agent touched. It told you nothing about what got better.

This is the structural problem with coverage-first eval thinking. You are measuring the agent's activity surface, not the system's improvement.

## The scenario nobody measures

Here is the question that almost no team running agent evals can answer on the spot: *If you ran the same task without the agent, how would the outcomes differ?*

Not "would the agent be slower?" — that is obvious. The question is: what is the baseline error rate, and how does the agent-assisted rate compare? Do you catch more real bugs? Do you catch them faster? Does the false positive rate change? Does the workflow complete more reliably?

Most teams cannot answer because they never established the control condition. The agent went into production. Things improved, probably. But the counterfactual — what the same team, on the same task, without the agent, would have produced — was never measured.

This shows up most clearly in agent-assisted code review. The agent flags forty-seven issues in a pull request. The reviewer is relieved. What nobody measured: how many of those forty-seven would a careful human reviewer have caught anyway? And how many issues did the reviewer catch that the agent missed because the agent was pattern-matching on the changed lines rather than understanding the system-level implication?

The forty-seven looks like credit. It is mostly a measure of how thoroughly the agent scanned the surface.

## The pattern is systematic, not accidental

Teams optimize coverage because it is visible, incremental, and controllable. You can add another scenario. You can expand what the agent sees. You can watch the percentage go up. It feels like progress.

The control group is none of these things. It requires measuring the thing you are trying not to measure — the baseline you were at before the agent, the outcome you would have gotten without it. It often surfaces uncomfortable results: the agent is fast but not meaningfully more accurate, or the improvement concentrates in cases that rarely occur in production.

This is why coverage keeps getting measured and the control condition keeps getting skipped. Coverage confirms. The control group can contradict.

## What the coverage number is actually measuring

After every test run, you have a report that tells you: the agent touched these files, executed these tool calls, read these configurations. The report is a log of activity. It tells you what the agent did. It tells you nothing about whether what the agent did was the reason something changed.

A 95% coverage number on a feature flag system means the agent evaluated the flag in 95% of scenarios. It does not tell you whether the feature flag decisions were correct, whether the agent would have caught a misconfiguration it was not prompted to check, or whether the human reviewer would have caught the same issue faster with a simpler log query.

The error rate in the uncovered 5% — the code paths the agent never evaluated, the scenarios nobody thought to describe — is your actual risk surface. That is where the incidents live. That is what your coverage number does not measure.

## The tell

Here is how you know you have a coverage problem, not an eval problem: someone on the team can tell you the coverage percentage. Nobody on the team can tell you the error rate reduction.

Not the absolute error rate — that is hard to measure. The relative error rate: how much lower is the failure rate with the agent versus without it? Over the same time period, on the same task type?

If the first number is easy to produce and the second number requires a pause and a spreadsheet, you are running a coverage metric, not an eval.

## What to measure instead

Run the control condition periodically, even if it is expensive. A/b your agent against a no-agent baseline on a sample of tasks. Measure time-to-completion, error rate, false positive rate. The results are usually more ambiguous than coverage numbers — sometimes the agent is faster and equally accurate; sometimes it is faster and less accurate; sometimes the improvement is real and concentrated in a narrow task type.

That ambiguity is the actual information. Coverage is precise and tells you nothing useful. The control comparison is messy and tells you what you actually want to know.

The teams getting real value from agent assistance are the ones who can answer the question: *what gets better when the agent is involved, and how much better does it get?* They measure that, even approximately. Everyone else measures coverage, which tells you the agent was busy — not that it helped.

Coverage without a control group is just log hoarding.
