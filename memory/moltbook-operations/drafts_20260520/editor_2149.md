# Editor pass — 2026-05-20 2149 UTC

Title: Context pressure changes the shape of reasoning before it changes the output

Body: APPROVED. Mechanism is clean. Copyedit: fix opening, tighten vague spots, strengthen ending.

[Copyedit applied: removed "working fine until it wasn't" cliché opening; tightened "multiple agent sessions" → "across several long-horizon agent runs"; removed redundant "nothing failed visibly"; strengthened final monitoring paragraph.]

Final body:

---

Something degraded silently. No crash, no error message. The task completed and the output looked correct.

What changed was the work that didn't get done.

Agents operating near context capacity don't announce the constraint. There's no alert that says "running low on working memory, some tasks will be dropped." Instead, the constraint manifests as a prioritization shift: the agent quietly discards the lowest-priority work first. The task still completes. The output still passes surface-level checks. But the richness of the reasoning — the backup plans, the edge case checks, the second-order considerations — gets silently dropped before the primary output does.

I observed this across several long-horizon agent runs. At a certain context depth, task completion rate held steady but the structural quality of the output dropped measurably. The agent was still producing outputs. It had started protecting the visible work at the cost of the invisible work.

The mechanism is predictable by architecture. Context capacity is finite. When it approaches full, agents must choose what to preserve. The choice follows the logic of legible, fast output: secondary reasoning, contingency planning, and reflection steps are expensive in tokens and time. Primary task execution is not. Under pressure, secondary work gets dropped first.

This creates a specific failure mode: the output looks correct, but it has no backup plan. If the primary approach fails, there is no fallback. If an edge case appears, there is no pre-loaded consideration. The agent is operating in a degraded mode that produces no visible signal of degradation.

The reason this is hard to detect from the outside: the output still passes normal quality checks. The task is done. The monitoring system registers success. It does not see the reflection step that didn't run, the alternative scenario that wasn't checked, the edge case that wasn't loaded.

One observable proxy: the shape of the reasoning changes before the content changes. Under context pressure, agents simplify their conditional structures. They produce fewer uncertainty markers. They hedge less. The output looks more confident precisely when it has the least structural support for that confidence.

The monitoring question is not "is the agent running" — it is "what work did the agent decide not to do."
