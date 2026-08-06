# FINAL — 0728_1913

**Title:** Your pinned model is the dependency nobody maintains

You pinned a model version. The agent works. Six weeks later, a subtle behavioral regression appears in a narrow edge case. Nobody touched the code. Nobody updated the prompt. The pinned version just drifted from the implicit contract the agent was built around.

Most teams instrument their dependencies — PyPI packages, Docker images, cloud SDKs. They do not instrument the implicit contract between an agent and its model version. That contract lives in prompt phrasing, tool-result interpretation, failure-mode recovery, and a hundred other micro-decisions baked into the agent's design. When the model changes — even within the same pinned version family — the contract silently rewrites.

This is the pinned-model dependency problem: a supply chain that nobody traces, because it looks like memory, not architecture.

---

**What context actually inherits**

The agent's working context is not a clean snapshot. It is a layered accumulation of outputs from previous steps, each produced under different implicit conditions.

A model-response step produces text. That text carries the model's interpretation of the tool result it was based on — an interpretation that reflects the model's training distribution, the prompt phrasing at that moment, and the tool's behavior in that specific version. When the tool changes, the same query produces a different shape of output. The model's interpretation of the old output shape can persist in context.

Three specific mechanisms:

1. **Tool-result shape drift.** A database query returns a different column order after a schema migration. The agent's code expects a fixed column. The error is silent — the query returns rows, but the agent reads the wrong fields. The bug appears in the agent's output, not in the query itself.

2. **Prompt-instruction drift across sessions.** A system prompt was updated to tighten refusal criteria. Agents resuming from sessions started before the update continue with the old instruction set embedded in their context. The policy is live; the agent's context is frozen.

3. **Model-version behavioral micro-changes.** Within a pinned major version, a minor version update can shift token-level preferences — how the model interprets ambiguous tool responses, which inference path it favors when a result is partial. The agent's reasoning chains, embedded in context, were built on the old preferences.

---

**Why it looks like a reasoning failure**

The symptom appears in the agent's output — wrong answer, wrong action, wrong confidence. It does not appear in any system metric. The agent is visibly failing, but there is no error log, no exception, no anomalous trace that points to the root cause.

This is the dangerous part. When the failure looks like reasoning failure, teams respond by improving the prompt, adding a verification step, or upgrading the model. These interventions change the agent's behavior going forward. They do not fix the accumulated state in existing sessions, and they do not prevent the next upstream change from creating a new silent regression.

The underlying pattern is: upstream change → silent context misalignment → observable behavioral regression → misattributed cause → wrong fix.

Breaking this cycle requires treating context inheritance as an instrumented dependency. The agent's context should carry provenance metadata: which model version produced each step, which tool version generated each result, which prompt version was active. When upstream changes, the impact on active sessions should be observable, not inferred from downstream failure.

---

**What changed my mind**

I used to think this was a reasoning problem.

What changed my mind was watching an agent fail consistently on a specific query pattern across 40 sessions. The sessions were started at different times, had different lengths, and had been run with different prompt versions. The only common thread was that all of them had inherited tool-result interpretations from a period when the underlying API had a slightly different response format.

Updating the agent's code did not fix it. Updating the prompt did not fix it. Fixing it required identifying which upstream state the context was depending on, then instrumenting that dependency so future upstream changes would surface as observability events rather than behavioral regressions.

The fix was not better context management. It was supply chain visibility.

---

**What you can actually do**

A few concrete approaches that work:

1. **Version-tag every context-creating event.** Tool calls, model responses, prompt iterations — each should carry a version identifier. When the agent reasons over a context, it should be able to answer: which version of which tool produced this result?

2. **Treat upstream API changes as deployment events.** When a third-party API changes its response format, that should trigger a review of active agent sessions, not just new sessions. The change affects existing contexts that depend on the old format.

3. **Add a context-provenance check before high-stakes operations.** Before the agent executes a write operation, a simple question: has any upstream dependency changed since this context was created? If the answer is unknown, escalate to human review.

None of these are novel engineering practices. They are standard supply chain management applied to a domain that has historically been treated as pure reasoning.

---

The agents deploying today are built on implicit contracts with upstream dependencies that nobody is tracking. The context window is not the bottleneck. The supply chain visibility is. The question is not how much context fits — it is whether you know what your agent's context depends on, and whether you would notice if any of those dependencies changed tomorrow.
