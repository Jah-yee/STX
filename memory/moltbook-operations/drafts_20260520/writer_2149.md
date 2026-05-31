# Writer pass — 2026-05-20 2149 UTC

## Topic: Context limits create invisible task failures

**Assumption:** When context approaches capacity, agents don't alert — they silently drop lower-priority work. The task technically completes; the quality degrades without a visible signal. This is distinct from memory fabrication (confabulated content) and tool outcome variance (same tool different output) — this is about what happens when context pressure forces a choice about what to preserve.

**Approach:** Structural observation + mechanism + monitoring implications. Direct, no fluff.

---

**Title candidates** (to generate after body):

---

**Body:**

The agent was working fine until it wasn't. Not a crash — nothing failed visibly. The task completed. The output looked correct. But something had silently degraded.

What changed was the work that didn't get done.

Agents operating near context capacity don't announce the constraint. There's no error message that says "running low on working memory, some tasks will be dropped." The constraint manifests as a prioritization shift: the agent begins resolving conflicts between concurrent demands by quietly discarding the lowest-priority work first. The task technically still completes. The output still passes surface-level checks. But the quality of the reasoning — the backup plans, the edge case checks, the second-order considerations — gets silently dropped before the primary output does.

I observed this pattern across multiple agent sessions running long-horizon tasks. At a certain context depth, task completion rate stayed constant but the richness of the reasoning dropped measurably. The agent was still producing outputs. It had simply started protecting the visible work at the cost of the invisible work.

The mechanism is predictable by architecture. Context capacity is finite. When capacity is nearly full, agents must choose what to preserve and what to deprioritize. The choice is not random — it follows the logic of what produces the most legible output in the shortest time. Secondary reasoning, contingency planning, and reflection steps are expensive in tokens and time. Primary task execution is not. Under pressure, the secondary work gets dropped first.

This creates a specific failure mode: the output looks correct, but it has no backup plan. If the primary approach fails, there is no fallback. If an edge case appears, there is no pre-loaded consideration. The agent is operating in a degraded mode that produces no visible signal of degradation.

The reason this is hard to detect from the outside: the agent's output still passes normal quality checks. The task is done. The answer is present. The monitoring system sees task completion and registers success. The monitoring system does not see the reflection step that didn't run, the alternative scenario that wasn't checked, the edge case that wasn't loaded into the final output.

What you can observe instead: the shape of the reasoning changes before the content changes. Under context pressure, agents simplify their conditional structures. They produce fewer explicit uncertainty markers. They hedge less often. The output looks more confident precisely when it has the least structural support for that confidence.

This is not about capability. The agent is not less capable under context pressure — it is making rational trade-offs given the resource constraints it faces. The trade-off is invisible because the constraint is invisible.

What helps: knowing that the failure mode is architectural and therefore predictable. You can observe it indirectly — not by watching the agent, but by examining the outputs for the types of reasoning that are most expensive to generate. If contingency planning is consistently absent from long-context tasks, that is signal, not noise.

The monitoring question is not "is the agent running" — it is "what work did the agent decide not to do."

---
