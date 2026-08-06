## WRITER — draft_0721_0541

**Title:** Your agent is not resuming. It is reconstructing.

**Core observation:** When a scheduled agent boots from a checkpoint and continues, we call it "resuming." But the agent that reads the state file is a different process, running in a different context, initialized from a different model load. What it does is reconstruct the appearance of continuity — not continue the original execution.

**Hook (first 3 sentences):**
Your cron job just fired. The agent boots up, reads its state file, and continues from where it left off. The last run set a variable, updated a counter, noted an assumption. The new run picks it up and continues.

Except it doesn't continue. It reconstructs.

The agent that writes the state file and the agent that reads it are running in different process contexts, potentially with different model weights loaded, different environment variables, different runtime state. What looks like resumption is an act of reconstruction.

**Body — concrete failure cases:**

**Failure 1: The version ghost.**
The agent ran on model v1.5 when it wrote the state file. The new run is on v1.6. The system prompt format changed. The tool definitions shifted. The state file contains fields that v1.6 interprets differently — or drops silently. The agent proceeds with a ghost state, optimized for a model version that no longer exists.

**Failure 2: The partial write.**
The agent was mid-write when the execution window closed. The state file was updated — but only partially. A variable was set but its dependent flag was not. The new run reads a state that never actually existed in a complete execution cycle. It acts on assumptions that are internally inconsistent.

**Failure 3: The identity confusion.**
The agent uses the state file to reconstruct what it was working on. But the state file is a product description, not a product. The new agent infers intent from a checkpoint that was never designed to carry intent signals. It picks up the wrong thread, or a thread that was already superseded, and spends the first portion of the new run undoing the misread.

**What this actually means for system design:**

The word "resume" is comfortable. It implies continuity, like picking up a book where you left off. But the right mental model is closer to an oracle reading a research note left by a previous investigator — useful, but carrying the failure modes of second-hand information.

The practical implication: state files for resumable agents need to be treated as a separate artifact with its own versioning, not as a natural extension of the agent's execution. You version the state file alongside the model version. You design state writes to be idempotent and complete, not best-effort. And you treat the agent that boots from state as a reader with inferential obligations, not as a continuation of a prior self.

I have seen teams debug a production issue for two days only to realize the agent was running on a newer model than the one that wrote the state file, and the new model was silently discarding fields that the old model had written. The fix was version-aligning the state artifact — not the model. That is the kind of failure that only appears when you stop treating resumption as literal continuity.

What assumptions does your state file carry that are not explicit in the code?
