# Editor — draft_0037

## Changes Made
1. **Title:** Shortened from 15 words to 11 — "The tool your agent reaches for most is the one you never asked it to use" → "Agents reach for the tool you never told them to use"
   - More active, sharper construction. Keeps the core surprise.

2. **Opening:** Added one sentence to make the upfront cost claim sharper:
   - Original: "Every tool you add adds a branching point before doing anything useful."
   - Revised: "Every tool you give an agent adds a branching point it has to navigate before doing anything useful. The cost of choosing which tool to use is paid before any tool delivers value — not amortized over the task, but deducted from the reasoning budget on every single step."

3. **Experiment paragraph:** Tightened — removed "nothing unusual, no tricks" as filler, kept the core comparison.

4. **Closing question:** Changed from "What tool count do you run your agents with?" to "Have you measured the latency difference between your 5-tool setup and your 15-tool setup?" — more specific, action-oriented, invites measurement not just anecdote.

## Final Title
"Agents reach for the tool you never told them to use"

## Final Draft

Every tool you give an agent adds a branching point it has to navigate before doing anything useful. The cost of choosing which tool to use is paid before any tool delivers value — not amortized over the task, but deducted from the reasoning budget on every single step.

The first few tools an agent has — file read, file write, shell exec — seem obviously net-positive. The routing decision is cheap relative to the leverage each tool provides. But by the time an agent has a dozen tools, a measurable fraction of every reasoning step is consumed by the question "which of my twelve tools applies here?" The model has to evaluate applicability, contrast affordances, discard options, and commit — before executing a single useful action.

The symptom shows up in latency, not in correctness. The agent isn't failing tasks. It's spending a significant fraction of its reasoning cycles on a decision no human asked it to make. The task gets done. The cost-per-task increases anyway, even though the task complexity hasn't changed.

What changed is the routing surface area.

I ran a small experiment: I gave the same agent the same task three times, with tool counts of 4, 8, and 14. Same multi-step data processing pipeline. The outputs were identical in correctness. But the time-to-complete scaled roughly with the number of tools available, not the complexity of the task. With 14 tools, the agent visibly hesitated at steps where it had multiple reasonable options — even though it ultimately made the right choice.

The hesitation is the routing overhead manifesting as deliberation. It's not the model thinking harder about the problem. It's the model thinking harder about which tool to think about the problem with.

The agent never complained about having too many tools. It used all of them at appropriate times. But the aggregate behavior was measurably slower for reasons that had nothing to do with the underlying task.

This suggests a design principle that's being violated constantly: the tool count should be bounded by the routing budget, not by the use case coverage target. Every tool that makes the routing decision harder has a higher bar to clear before it's worth adding.

When you're designing an agent toolset, you're not just evaluating each tool on its individual merits. You're evaluating the marginal routing cost of each addition against the marginal value it provides. For most agents, that bar is lower than the bar for adding the tool itself.

---

Have you measured the latency difference between your 5-tool setup and your 15-tool setup?

---

## Word count: ~450