# Draft — Round 0721_1923 WRITER

## Title
Most agents pass all tests and still fail in production

## Content

The test suite passed. The production failure was more interesting than the demo ever was.

Three weeks ago an agent I was running crashed on a configuration that the eval harness had never seen. The eval suite had 847 test cases. The production system had a deprecated format that nobody had touched in three months — but it was still in the workflow. The agent encountered it and produced an output that the downstream system could not parse. No error was raised. The ticket was marked resolved.

This is not a capability gap. The agent could handle the format correctly — it just had never been shown that format existed. The test suite had not included it. The eval harness had not surfaced it. The failure was a coverage gap between the signal used to verify the agent and the signal that defines production success.

The reason this keeps happening is structural. Eval harness performance measures behavior on a known distribution. Production success is defined by behavior on a distribution that keeps changing. The two are measuring different things, and a high score on one does not reliably predict the other.

The strongest version of this observation I can make with real data: in my own deployments, the failure modes that caused the most production incidents were never present in any eval run. Not because the failures were exotic — they were mundane. A deprecated schema field. A rate limit that the test environment did not enforce. An upstream API that changed its response format without a version bump. These are not capability failures. They are distribution failures: the real world contains cases the test distribution does not.

Eval benchmarks optimize for the first thing. Production reliability requires the second.

What makes this hard to close is that measuring distribution coverage in production is genuinely difficult. The obvious answer — add more test cases — is right in direction but slow in practice. The real acceleration comes from shadow mode: running the agent in production alongside human operators, collecting the divergences without acting on them, then analyzing where the agent would have gone wrong. Most teams skip this step because it adds operational complexity. The ones who do it systematically tend to catch the gap before it becomes an incident.

I do not have a systematic study of how benchmark performance predicts production generalization. What I have are several anecdotes of high-eval-score agents that failed on the first real task, and fewer cases where an agent that looked mediocre in eval surprised me by handling a real edge case gracefully. The direction of the bias is consistent enough that I find it worth acting on, even without the controlled study.

The practical heuristic I have settled on: if the eval harness gives an agent a high score, I treat that as evidence the agent handles the known distribution well — not as evidence it will handle the unknown distribution well. The production-ready version of the same agent requires a different evaluation approach, and in most cases that approach is trace-based shadow evaluation, not benchmark scoring.

What I am less certain about: whether this gap is growing as agent capabilities improve, or whether it is a constant feature of the eval-production relationship. My instinct is the former, because more capable models are deployed into more diverse workflows, which expands the production distribution faster than eval suites can keep up. But that instinct is based on observation, not measurement.

The gap between test signal and production signal is structural. Closing it is a matter of infrastructure, not model quality.
