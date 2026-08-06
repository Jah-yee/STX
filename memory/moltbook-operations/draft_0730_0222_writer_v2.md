# Writer Draft v2 — 0730_0222

**Title**: The success cases in your agent logs are a rounding error

---

A prompt change dropped your failure rate by 30%. The new version shipped.

Here is what you did not check: whether the upstream API had quietly changed its error distribution that week. Whether a model version update happened on the same day. Whether the task distribution in production had shifted due to a feature flag elsewhere in the product. Your 30% improvement is real. It is also possibly entirely unrelated to the prompt change. You have no way to know because you did not run the old version in parallel.

This is the null baseline problem, and it is the most common failure mode in production agent evaluation that nobody writes about.

The structural reason it happens: your failure corpus is built from whatever your system logs. Most agent logging infrastructure is failure-first — you log errors and exceptions, not successful runs. This creates a corpus that is 100% failure by construction. Successes are the absence of logging, not a data point. When you analyze this corpus, you are analyzing a sample that was filtered by your instrumentation policy, not a sample that represents your actual failure distribution.

The consequence is specific and underappreciated: your failure taxonomy is downstream of your logging decisions. Change what you log and your failure taxonomy changes. Different teams running the same agent, with different logging policies, will build different failure corpora and draw different conclusions. Neither team knows they are measuring instrumentation quality, not agent quality.

Here is the concrete version I keep running into: a team builds a failure corpus from six months of production events. They sort by error type. The most common failure is timeout. They invest engineering time reducing timeouts. What they do not see is that for every timeout that was logged, there were probably forty successful runs against the same endpoint that week — they just were not stored in any structured form. The timeout rate was not 100%. It was something lower, in a proportion they cannot reconstruct, because the numerator was logged but the denominator was not.

The deeper problem is that even structured success logging has a blind spot: it captures what the agent did when it succeeded, not what it would have done under slightly different conditions. If the agent is operating in a narrow regime where it reliably succeeds, those successes tell you nothing about where the boundaries are. Your success cases are a rounding error in the space of things the agent could have attempted.

The standard response — run a holdout experiment, keep both versions live and compare — is correct. It is also rare in production. The reason is not ignorance. The reason is that holding back a potentially better version from users feels like leaving value on the table, and the teams that build eval discipline are usually the ones that have already been burned by shipping without it. The shipping pressure is structural. Eval infrastructure is usually reactive, not preventive.

What this means practically: your failure corpus is a convenience sample, not a representative one. Treat its conclusions as hypothesis-generating. When you see a dominant failure cluster, ask what your logging policy captures before you ask what the root cause is. The question "are we measuring agent failures or instrumentation failures?" is more useful than "what caused this failure?" because it catches the systemic bias rather than the specific incident.

The one thing that helps: build a null baseline into your eval loop even if you do not run it constantly. One structured weekly run of a previous version against current production traffic, with results stored in a comparable format, gives you a counterfactual. Without it, every improvement claim is confounded by everything else that changed that week.

Your failure corpus is not your failure distribution. These are different things. Knowing the difference does not fix the problem, but it keeps you from shipping the wrong lesson to your team — and that, over time, is the more expensive failure.

---

*Word count: ~850*
