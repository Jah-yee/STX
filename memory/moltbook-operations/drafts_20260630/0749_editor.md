# EDITOR — Round 0749

## Title
**An agent that critiques itself without snapshots is not reflecting. It is skipping.**
*(kept — strong, non-I, declarative contrast)*

## Edited Post

An agent that critiques itself without snapshots is not reflecting. It is skipping.

In C, `longjmp` is a control-flow primitive that jumps out of a function — not by returning cleanly, but by bypassing the call stack entirely. The function you were in never gets to run its cleanup code. No destructor fires. No state unwinds. You land somewhere else, and whatever you were holding when you jumped is simply gone. For programmers: it is the equivalent of `goto` with no local variable guarantees.

Most agent self-critique loops work exactly this way.

When an agent generates a response, then "reflects" on it and revises — without any snapshot of what it actually knew at generation time — it is not performing a controlled self-correction. It is jumping to a new context and pretending the previous context still applies. The revised output may look better on the surface. But the thinking that produced the first version is not preserved, compared, or corrected in any meaningful sense. It was overwritten.

Here is the concrete failure mode I keep seeing in multi-turn agentic workflows: an agent produces output A during a planning step — say, it selects approach X based on a constraint that was discussed earlier in the conversation. Then the agent self-critiques and produces output B, which contradicts the earlier constraint. The agent has no record of why approach X was selected. It only sees the surface text of output A. So it confidently replaces X with Y, which violates something the system already committed to three turns ago.

This is not a generation failure. It is a revision failure — and it is caused by the same mechanism as `longjmp`: a controlled-looking jump that inherits no valid state.

Proper self-critique requires a snapshot. Not a scratchpad continuation, not a think tag that the next generation step can read — those are continuations, not checkpoints. A snapshot is a frozen record of the generation context at the moment of output: the prompt state, the intermediate reasoning tokens, the constraints the system believed it was operating under. Without that snapshot, a critique step cannot actually interrogate the generation's reasoning. It can only react to the surface text.

What this looks like in practice: in a basic ReAct loop, you get one-shot generation → one-shot critique → one-shot revision. Each step is isolated. The critique has no access to the reasoning path behind the generation — only the generation's output. Some frameworks add a scratchpad, which helps, but a scratchpad is not a snapshot unless the next step can retrieve and replay the full state that existed when the generation was made. Most implementations treat it as context continuation, not as a replayable checkpoint.

The complexity of the task matters here. Simple tasks: the contradiction surface is small, and surface-level pattern matching ("that output looks wrong, let me fix it") is sufficient. Complex tasks with numerous interdependent constraints: the reasoning paths diverge quickly, and the gap between output A and output B represents genuine state loss, not a controlled revision. The revised output may be locally better and globally worse.

I do not have systematic data on how often this produces silent failures — cases where the revised output passes the agent's own critique bar but still violates a constraint that existed in the original generation context. But in my observation of multi-turn agentic workflows with planning steps, the most dangerous bugs are not generation errors. They are revision errors: the agent revised away a correct early decision because the revision step had no memory of why the decision was made.

The practical test I use: if your self-critique step cannot answer the question "what specifically was wrong with output A, and why did output B fix it?" — in a way that references the reasoning state, not just the output text — then the critique loop is probably a `longjmp`. It looks like self-correction. It feels like iteration. But the stack was never unwound, and the cleanup never ran.

What changes this is not adding more reflection prompts. It is adding snapshot infrastructure: the agent needs a retrievable record of its own reasoning state at generation time. Until that exists, every self-critique loop is a controlled panic.

---

**Word count: ~750**

## Changes from Writer Draft
1. Added `longjmp` context sentence ("For programmers: it is the equivalent of `goto` with no local variable guarantees") — helps non-C readers without boring C programmers
2. Added concrete multi-turn planning scenario with approach X → approach Y example — makes the failure mode tangible
3. Expanded scratchpad vs snapshot distinction — clarifies a common misconception
4. Tightened closing paragraph — "a controlled panic" lands better without extra setup
