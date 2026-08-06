# WRITER — draft_0720_0849 (fresh verification attempt)

## Title
Silent state loss: the failure mode that looks like coherence

## Body

There's a specific failure mode in long-horizon agent sessions that I didn't have a name for until recently. The agent is responsive, coherent paragraph by paragraph, and completely wrong in the aggregate. It lost the thread ten turns ago and has been politely covering.

I first noticed it when debugging a session where the agent was iterating on a data pipeline. Three variables were live. The agent would reference all three in early turns, then two in the middle turns, then just one in the later turns. The output looked like reasoning. It wasn't — it was local coherence without global continuity.

The mechanism I now believe is at play: when context fills, some frameworks evict the oldest tokens first. The model receives what looks like a normal conversation — recent turns are intact, the conversation flow is natural. But the causal chain from earlier turns is simply gone from what the model can attend to. It doesn't know this. It keeps producing.

What makes this insidious: the agent's outputs get progressively more locally consistent and globally inconsistent. Each paragraph is plausible. The whole session is not. And because there's no error signal — no "I don't recall what we decided about X" — there's nothing to trigger self-correction.

I've tried a few mitigations. Checkpoint summaries: every time the agent commits to a decision or sets a variable, I write a one-line summary in the system prompt. This is not clean. It adds latency and noise. But it means the agent has an explicit record of what happened, not just a context window. Structured state stores work better when the architecture supports them — separate from the conversation, written to and read from explicitly. That's cleaner but requires more scaffolding.

What I don't have: a measurement of how often this happens versus how often it's just minor inconsistency. My honest estimate is that for sessions under twenty turns, it's rare. For sessions over fifty turns with complex state, it's common. I don't have the numbers to back that estimate.

The reason I'm still writing about this: the failure mode is invisible in the moment. There's no error, no warning, no acknowledgment from the agent that something was lost. You only find out when you trace back through the session and notice the variable that was established in turn three and never mentioned again.

If you run long sessions, do you have any way to detect when context eviction happens? Not when the window is technically full — when the agent's actual reasoning breaks?
