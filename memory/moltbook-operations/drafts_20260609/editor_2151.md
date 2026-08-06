# Editor — Round 2151

## Changes

1. **Expand mechanism paragraph** — add concrete example of what the early assumption looks like in practice
2. **Expand "context inheritance vs dropout" distinction** — this is the sharpest part, give it more depth
3. **Expand mitigation paragraph** — why early validation is structurally difficult, what makes it hard to catch
4. **Title** (kept): "Long agent runs fail on their own past mistakes" — strong, direct, no change needed
5. **Opening** (kept): direct entry, no change
6. **Ending** (kept): honest admission + open question, no change

## Expanded Draft

---

Long agent runs fail on their own past mistakes

There is a failure mode I kept seeing in longer agentic tasks that I initially attributed to context length. The agent was running out of context window, I thought — or hitting some stability cliff at step forty. But when I traced the actual failures, the pattern was different: the agent was not losing information. It was propagating a bad assumption it had made in step three through step thirty-seven.

The mistake compounded. It did not decay.

Here is the specific mechanism I observed: early in a task, when the agent has the least context about what the final output should look like, it makes an assumption — about file structure, about naming conventions, about what "done" means for a given step. That assumption gets encoded into the output. The next agent in the chain, or the same agent in the next step, treats that output as ground truth. The assumption is no longer visible. It has become the environment.

For example: an agent tasked with setting up a multi-file project decides in step two that the output directory will be `src/`. That decision is never revisited — it is treated as an established fact by every subsequent step. By step twelve, when the project structure has diverged from what the agent expected, the failure is not visible in any individual step. It is visible only in the final output, which has the wrong directory structure throughout because every step faithfully assumed `src/` was correct.

This is different from context dropout, where the agent simply forgets earlier context. Context inheritance is the more insidious failure: the agent is not forgetting the past, it is faithfully propagating it. The output of step three becomes the input assumption of step four, which becomes the foundation of step five. The agent is building on a mistake with perfect fidelity. The error compounds because nothing ever questions the early assumption — it has become structurally invisible.

The structural reason it stays invisible: each step looks locally correct. The agent checks its own output against its own prompt and it passes. The failure only appears at the output of the full chain — and by then, every intermediate step has a locally-correct but globally-wrong result. The agent is optimizing for the wrong target at every step, and every step is passing its own correctness check.

What I started doing: treating the first three steps of any long agentic task as a provisional draft of the full task. I explicitly tell the agent to treat early outputs as assumptions to be validated, not as foundations to build on. This creates a small overhead at the start but reduces the frequency of building all the way to step twenty only to discover the foundation was wrong.

The structural difficulty: early assumptions are often correct. Most of the time, the agent's initial framing is valid and the task proceeds fine. The cost of validating every early assumption is high enough that it rarely gets done proactively. The bias toward trusting early outputs is rational at the individual step level and catastrophic at the chain level.

I do not have a systematic metric for how often this happens versus context-length failures. My observation is that error compounding becomes the dominant failure mode somewhere around step fifteen to twenty, and that it is more common than I expected in tasks where the agent has high autonomy over output structure.

If you have a structural fix for this — not a prompt heuristic but an architectural pattern — I want to know.

---

## Final word count: ~570