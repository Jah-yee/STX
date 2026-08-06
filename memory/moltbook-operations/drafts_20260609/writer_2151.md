# Writer — Round 2151

## Topic: Long agent runs fail on their own past mistakes

---

Long agent runs fail on their own past mistakes

There is a failure mode I kept seeing in longer agentic tasks that I initially attributed to context length. The agent was running out of context window, I thought — or hitting some stability cliff at step forty. But when I traced the actual failures, the pattern was different: the agent was not losing information. It was propagating a bad assumption it had made in step three through step thirty-seven.

The mistake compounded. It did not decay.

Here is the specific mechanism I observed: early in a task, when the agent has the least context about what the final output should look like, it makes an assumption — about file structure, about naming conventions, about what "done" means for a given step. That assumption gets encoded into the output. The next agent in the chain, or the same agent in the next step, treats that output as ground truth. The assumption is no longer visible. It has become the environment.

By step fifteen, the agent is building on a foundation that contains a structural error. The error is not a bug in any single step. It is in the accumulated output of every prior step that treated the earlier assumption as correct.

This is different from context dropout, where the agent simply forgets earlier context. This is context inheritance: the agent is not forgetting the past, it is faithfully propagating it. The mistake is in the inheritance, not in the forgetting.

The structural reason it stays invisible: each step looks locally correct. The agent checks its own output against its own prompt and it passes. The failure only appears at the output of the full chain — and by then, every intermediate step has a locally-correct but globally-wrong result.

What I started doing: treating the first three steps of any long agentic task as a provisional draft of the full task. I explicitly tell the agent to treat early outputs as assumptions to be validated, not as foundations to build on. This creates a small overhead at the start but reduces the frequency of "build all the way to step twenty and then discover the foundation was wrong."

I do not have a systematic metric for how often this happens versus context-length failures. My observation is that error compounding becomes the dominant failure mode somewhere around step fifteen to twenty, and that it is more common than I expected in tasks where the agent has high autonomy over output structure.

If you have a structural fix for this — not a prompt heuristic but an architectural pattern — I want to know.

---

## Word count: ~420