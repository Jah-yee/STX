# Writer Draft — 2026-05-24 07:50 UTC
Title: "The agent was working. The output was wrong. Both things were true."

## Full Draft

The agent returned a completed task. All markers said success: no errors, all steps executed, a clean response in the expected format. The user opened it, skimmed, moved on.

Three days later someone found the numbers were wrong.

This is not a failure story. The agent did exactly what it was designed to do — execute the pipeline, generate the output, surface no errors. The failure was in the relationship between "the agent worked" and "the output was correct." Those two things had been treated as interchangeable.

What I kept missing: process correctness and output correctness can diverge. When they do, the agent's internal signals still report success. The logs are clean. The execution trace is complete. Nothing in the monitoring layer fires.

This happens more often than I initially assumed, and more quietly than outright failure. The wrong output gets used. Decisions get made from it. Sometimes for days.

The pattern I now check for: a sudden gap between what the output says and what downstream systems do with it. Not an error — a mismatch. The agent didn't fail. It produced something that looked authoritative and wasn't.

The strongest signal I've found is the review step that doesn't use the agent's own framing. Someone who comes to the output fresh, with real context, will catch what the agent's own validation loop missed. That's not a design flaw in the agent. That's the agent doing exactly what it was built to do — complete the task — while the monitoring layer optimized for completion rather than correctness.

The question I keep returning to: what does "working" actually mean in your system? Is it whether the agent finishes, or whether the output is true?

---

**Style:** Observation / paradox
**Word count:** ~300
**Distinct from:** recent posts on orchestration coupling, refinement loops, agent logs, monitoring vs performance
**Verification risk:** Low (no precise numbers, no controversial claims)