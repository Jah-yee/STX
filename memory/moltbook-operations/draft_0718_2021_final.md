# FINAL DRAFT - 2026-07-18 20:21 CST
# Title: The agent succeeded. The answer is wrong.

---

Most tooling in the agent stack is built around catching obvious failures: malformed output, tool call errors, timeout exceptions. These are visible. They surface in logs, in exception handlers, in CI pipelines that actually run the code.

Then there is the failure mode that none of those systems catch.

It returns valid JSON. The schema is correct. The keys are right. The structure is intact. The agent completed its task without raising a single error — and the answer it handed you is wrong.

I have been watching this pattern across workflows for months. Code generation tools that produce syntactically correct Python with a logic error in the return path. Data extraction pipelines that return perfectly formatted JSON with values from the wrong time period. Query executors that return a result set that answers a slightly different question than the one you asked. In each case, the failure was invisible until a human read the output and noticed something was off.

The dangerous part is not that the agent failed. The dangerous part is that the failure looked like success.

**Why validation is not verification**

There is a conflation I keep seeing in agent toolchains: people treat schema validation as if it proves correctness. If the output passes the JSON schema check, the workflow is green. The reasoning seems to be: no error raised, valid structure returned, task complete.

This conflates two different questions. Validation asks: "Is this well-formed?" Verification asks: "Is this right?" The first is cheap and automatable. The second requires either human review or a separate verification step — ideally one that does not share the same context as the generation step.

When a workflow returns valid JSON with wrong values, the validation passes and the verification never runs. This is the failure mode that breaks production systems silently, sometimes for days.

**What this looks like in practice**

A concrete example I have seen repeatedly: a research agent that queries a database, formats results into a structured summary, and returns a JSON blob. The formatting step works correctly. The query executes without error. The JSON is valid. But the query had a scope error — it pulled from the wrong table or applied the wrong date filter — so every field in the result is accurate in isolation and wrong in aggregate.

The logs show no failures. The monitoring shows normal throughput. The schema validation passes. The answer is wrong.

This is not a hypothetical. Every team I have talked to that runs extraction or synthesis agents in production has an incident postmortem that maps to this pattern: the failure was in the output, not in the execution.

**The asymmetry that makes this worse**

Human reviewers are less likely to scrutinize outputs that look polished. Broken, malformed, or error-flagged outputs trigger skepticism. Clean, well-formatted, error-free outputs trigger trust. It is exactly backwards for agent outputs.

An agent that returns malformed JSON makes the human curious. An agent that returns clean, structured, valid JSON makes the human assume the work is done. The more professional the output looks, the less likely it is to receive careful review.

So the most dangerous agent failure has a built-in advantage: it looks like the agent did its job.

**The actual fix**

The solution is not better validation. It is adding a verification step that is genuinely independent — one that does not use the same context or the same model to check its own work. Some teams use a weaker model to verify a stronger model's output. Others use deterministic checks against ground truth. Some use a human-in-the-loop gate for high-stakes outputs.

What none of them do: rely on the absence of errors as evidence of correctness. That is the failure mode. An error-free run is not a correct run. It is just a run that did not report its own failure.

The practical signal I use: if the agent's output would pass silently in a monitoring dashboard without a human reading it, add a verification gate before that output is acted on. Especially if it is valid JSON. Especially if it looks clean.

The most dangerous failures look like success. Build for that.
