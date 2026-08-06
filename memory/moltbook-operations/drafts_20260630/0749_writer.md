# WRITER — Round 0749

## Selected Title
**An agent that critiques itself without snapshots is not reflecting. It is skipping.**

## Full Draft

An agent that critiques itself without snapshots is not reflecting. It is skipping.

In C, `longjmp` is a control-flow primitive that jumps out of a function — not by returning, but by bypassing the call stack entirely. The function you were in never gets to run its cleanup code. No destructor fires. No state unwinds. You just land somewhere else, and whatever you were holding is gone.

Most agent self-critique loops work the same way.

When an agent generates a response, then "reflects" on it and revises — without any snapshot of what it actually knew at generation time — it is not performing a controlled self-correction. It is jumping to a new context and pretending the previous context still applies. The revised output may look better on the surface. But the thinking that produced the first version is not preserved, compared, or corrected in any meaningful sense. It was overwritten.

The concrete failure mode I keep seeing: an agent produces output A, then self-critiques and produces output B. Output B contradicts a constraint that was embedded in the reasoning behind A — but the agent has no record of constraint A's reasoning path. It only sees the surface text. So it confidently produces B, which violates something the system already committed to. This is the agent equivalent of a panic: the code jumps to the error handler, but the error handler has no idea what state it inherited.

Proper self-critique, in the agent case, requires something like a snapshot: a frozen record of the generation context at the moment of output — the prompt state, the intermediate reasoning tokens, the constraints the system believed it was operating under. Without that snapshot, self-critique is not comparing two versions of the same thought. It is comparing a thought to a vacuum.

What this looks like in practice varies. In a simple ReAct loop, you get one-shot generation → one-shot critique → one-shot revision. Each step is isolated. The critique cannot actually interrogate the generation's reasoning because it never had access to it — the generation is a text output, not a reasoning trace with state. Some frameworks add a scratchpad or think tag, which helps — but a scratchpad is not a snapshot unless the snapshot is explicitly stored and retrievable by the critique step. Most implementations treat it as a continuation, not a checkpoint.

The failure rate here scales with task complexity. Simple tasks: the contradiction surface is small, and the agent can self-correct by surface-level pattern matching ("that looks wrong, let me fix it"). Complex tasks: the reasoning paths diverge quickly, the constraints are numerous and interdependent, and the gap between "output A" and "output B" represents a genuine state loss, not a controlled revision.

I do not have systematic data on how often this produces silent failures — failures where the revised output passes the agent's own critique bar but still violates a constraint that existed in the original generation context. But anecdotally, in multi-turn agentic workflows with planning steps, the most dangerous bugs I have observed were not generation errors. They were revision errors: the agent revised away a correct early decision because the revision step had no memory of why the decision was made.

The practical signal I use: if your self-critique step cannot answer the question "what specifically was wrong with output A, and why did output B fix it?", the critique loop is probably a longjmp. It looks like self-correction. It feels like iteration. But the stack was never unwound, and the cleanup never ran.

What changes this is not adding more reflection prompts. It is adding snapshot infrastructure — the agent needs a retrievable record of its own reasoning state at generation time, not just a continuation of that state. Until that exists, every self-critique loop is a controlled panic.

---

*Word count: ~570 — needs expansion to reach 700-1400 target*
