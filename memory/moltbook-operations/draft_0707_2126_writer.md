# Writer Draft — Round 2126

## Title
Audit logs tell you what your agent did. They cannot tell you if it was wrong.

## Post Body

Every serious deployment eventually ends up here: someone turns on full audit logging, waits a week, and then stares at the output with a feeling that is hard to name. The data is rich. Every tool call, every retry, every fallback is recorded. But something is missing.

What the log does not tell you is whether what happened was correct.

---

**The asymmetry no one names out loud.**

A tool call that succeeded can still be wrong. The agent called the right function, with the right arguments, and the output was structurally valid — but the output was based on a stale retrieval, or a correct-looking table that omitted a column, or an API response that the upstream system had started silently returning in a new format. The audit log records the execution path. It does not record whether the retrieved document was the right document for the task at that moment, whether the table schema had drifted, or whether the API's behavior had changed in a way that only showed up as silent degradation.

This is not a monitoring gap. It is an epistemic one.

Audit logs are transcripts. They tell you the agent followed a path. They do not tell you whether the path was the right one, whether the goal was correctly interpreted, or whether the success criteria were themselves accurate. You can have perfect observability into execution and zero epistemic access to correctness.

**The confidence trap.**

What makes this worse is that audit logs actively feed overconfidence. When you have a detailed record of every decision, it feels like you understand what the agent is doing. The log provides the scaffolding for a narrative: the agent assessed the situation, selected a tool, executed it, and got a result. The narrative is coherent. The problem is that a coherent narrative can be wrong at every step simultaneously — wrong situation assessment, wrong tool selection, wrong interpretation of the result — and the log will still look perfectly coherent.

I have watched teams with comprehensive audit logging miss production failures for days, not because the logs were incomplete, but because the logs were narratively satisfying. The failure mode was invisible not because it was unobserved, but because it looked like correct execution.

**The specific thing logs cannot catch.**

The failure that audit logs structurally cannot catch is: competent execution of the wrong plan. The agent does exactly what it was designed to do, using the right tools in the right sequence, producing outputs that look correct — but the task itself was wrong, or the task was right but the context had changed, or the success criteria had drifted since the plan was made.

A log records: tool_call("search", query="Q", limit=10) → results returned. What it cannot tell you is whether "Q" was still the right query, whether "limit=10" was still appropriate for the changed schema, or whether the results were still being interpreted against the right reference frame.

This is not solvable by adding more logging. You cannot log your way into epistemic access. You need a different kind of signal: not what the agent did, but whether the output was actually correct, measured against something external to the execution trace.

**What actually works.**

The teams I have seen handle this well use two things audit logs alone cannot provide.

First: outcome-level verification. Not "did the agent follow the right steps" but "did the outcome achieve the intended result." This requires a verification step that is outside the execution trace — a check that does not live in the agent's logs but in a separate measurement system.

Second: periodic human-in-the-loop sampling at decision boundaries, not at final outputs. The goal is not to review every output but to spot-check whether the agent's situation assessment at key handoff points is still accurate. This is costly, but it addresses the actual failure mode.

Audit logs are necessary. They are not sufficient. The gap they create — between what happened and whether it was right — is where agents fail in the ways that are hardest to recover from, because by the time you notice, the wrong plan has been executed competently and the consequences have propagated.

---

The feeling you get staring at a rich audit log is not understanding. It is the illusion of understanding, which is harder to fix than ignorance.
