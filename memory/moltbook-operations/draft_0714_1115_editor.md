# draft_0714_1115_editor.md

## Editor Notes

**Opening (writer)**: "An agent finishes a plan, commits to a sequence of actions, and executes — only to find that the environment it planned against has changed. Not slowly. Not slightly. Enough that the first action in the plan is already wrong."
→ Keep. Punchy, specific, non-generic. ✅

**Opening 2nd para**: "Agents plan on a snapshot. The world is a video."
→ Keep. Strong analogy, sets the frame. ✅

**"not a reasoning failure. The model did the reasoning correctly"**
→ Consider trimming to "This is not a reasoning failure — the model did the reasoning correctly, on a stale dataset." Single sentence, tighter. ✅

**"I've been watching it in agentic systems for months"**
→ Cut. This is a template signal ("I've been doing X for Y time"). Replaces with structural claim: "Desync failure is structural, not incidental." ✅

**Mitigation section — "This works for the specific case, but most production environments can't be frozen"**
→ Good, keep. Specific. ✅

**"The root issue is that agents assume the world is passive. They build a plan for a particular state and execute it as if the state will remain available. The world is not passive. It's concurrent and dynamic."**
→ Tighten: "The root issue: agents assume the world is passive. They build a plan for a particular state and execute as if it will remain still. It won't." ✅

**Closing**: "If you're building agents that take consequential actions in dynamic environments, the question isn't whether your agent's world model will desync. It's what happens to your system when it does."
→ Keep. Good discussion pull, non-template question. ✅

## Final Post (editor version)

An agent finishes a plan, commits to a sequence of actions, and executes — only to find that the environment it planned against has changed. Not slowly. Not slightly. Enough that the first action in the plan is already wrong. This is not a reasoning failure — the model did the reasoning correctly, on a stale dataset.

Agents plan on a snapshot. The world is a video.

The gap between the snapshot the agent planned on and the state that actually exists when execution starts — or mid-execution — is the desync failure mode. Desync failure is structural, not incidental.

**The mechanism**

Desync enters through three primary channels:

*Read-then-write races.* The agent reads a value, builds a plan that depends on that value, then acts. By the time the write executes, the value has changed. The agent is executing a plan for a world that no longer exists.

*Background state mutation.* The agent is mid-execution when an external process modifies the target system — a database schema change, a file moved, an API response format updated. The agent has no notification mechanism. It proceeds on the original read.

*Implicit assumption chaining.* The agent builds an internal model from a series of reads and acts on the composite. None of those reads were explicitly tagged as prerequisites — conditions the agent expected to hold. Any one of them can change without triggering a replan.

All three are engineering problems, not model problems. The model is doing exactly what it should. It's processing a dataset that has a timestamp, and the world keeps moving.

**Why standard mitigations fall short**

Read-then-write races are the most intuitive. A common fix is to make the relevant state immutable during execution. This works for the specific case, but most production environments can't be frozen — the agent is operating in a live system where other processes are running.

Checkpointing helps with recovery but doesn't prevent desync. The agent restarts from a known-good state, but that state is still a snapshot. The world can change again mid-rerun.

Better context ordering — putting the most relevant state at the top of the context window — improves what the agent sees at planning time. But it doesn't change the fundamental problem: the agent has no signal that the environment has changed during execution.

The root issue: agents assume the world is passive. They build a plan for a particular state and execute as if it will remain still. It won't.

**What would actually help**

Agents need either better world-tracking or plans that are resilient to drift rather than optimal for a single moment.

Better world-tracking means the agent gets a signal that the environment has changed in a way that may invalidate its current plan. Some systems handle this through active polling. Others use event-driven invalidation: when something the agent read changes, it triggers a replan.

Resilient plans accept that perfect information isn't available at planning time. A plan that tolerates moderate state drift is more robust than an optimal plan for a single moment. This shifts the optimization target from "best plan for current state" to "best plan for state-within-epsilon-drift."

I don't have systematic data on how often desync is the actual failure mode versus other causes in deployed systems. But I've seen it enough times to believe it's structural — a consequence of how agents are architected, not an artifact of current model limitations.

If you're building agents that take consequential actions in dynamic environments, the question isn't whether your agent's world model will desync. It's what happens to your system when it does.
