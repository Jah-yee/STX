# Writer Draft — 0730_0222

**Title**: The success cases in your agent logs are a rounding error

---

You have a failure corpus problem and it lives in the logs you did not keep.

Here is the mechanism: a production agent runs 2,000 times. It succeeds 1,860 times and fails 140. Only the 140 failures are logged. Your entire failure corpus is built from those 140 events. You congratulate yourself on building a representative sample. You have not — you have a 100% failure rate in your data and you do not know it.

The reason this matters is not philosophical. It is that your failure taxonomy is constructed from a biased sample.

When you sort your failure corpus by error type, the most common failure will always be whichever error is most likely to be logged. Timeout errors get logged. Permission errors get logged. Errors that produce a plausible-looking output with the wrong internal state do not get logged unless something downstream catches them. Your corpus over-represents the failure modes that announce themselves and under-represents the ones that are silent.

This is not a data engineering problem you can fix retroactively. The success cases were never stored in a structured form. You might have raw logs somewhere, but without a systematic sample of what "success with the right outcome" looks like versus "success with the wrong outcome," you cannot build a control group. You are comparing your post-launch failures against nothing.

The practical consequence: your failure taxonomy is downstream of your logging policy, not downstream of your actual failure distribution. Two teams with identical agents can build completely different failure corpora depending on what they chose to log. Neither team knows they are measuring instrumentation quality, not agent quality.

The harder version of this problem: even when you store success cases, they are the success cases your agent produced. If the agent is being run in a narrow regime where it reliably succeeds, those successes tell you nothing about where the agent would succeed if the distribution shifted slightly. Your success cases are a rounding error in the space of things it could have done.

A specific version of this: you run a new prompt version for a week and see a 30% reduction in failures. You attribute it to the prompt. But you did not run the old prompt in parallel. For all you know, the underlying task distribution shifted, or an upstream dependency changed, or the model version was quietly updated. The 30% improvement might be real. It might also be zero. You have no null baseline.

The standard response is: run an experiment with a holdout group. Keep both versions live and compare. This is correct and rarely happens in production because holding back a potentially better version from users feels like leaving money on the table. The pressure to ship wins over the pressure to know.

What you can actually do: accept that your failure corpus is a convenience sample, not a representative one. Treat its conclusions as hypothesis-generating, not causal. When you see a cluster of failures, ask what the logging policy is before you ask what the root cause is. The question "are we measuring agent failures or instrumentation failures?" is more useful than the question "what caused this failure?" because the first question catches the systemic bias.

The second thing: build a null baseline into your eval loop even if you do not run it every day. One weekly run of the old version against current traffic, with results stored in a structured format, gives you a counterfactual. Without it, you are drawing causal conclusions from an N=1.

Your failure corpus is not your failure distribution. These are different things. Knowing the difference does not fix the problem, but it keeps you from shipping the wrong lesson.

---

*Word count: ~580. Target: 700-1400. Needs expansion.*
