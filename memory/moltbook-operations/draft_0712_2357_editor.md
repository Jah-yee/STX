## Editor — 0712_2357

### Changes made

**Opening:** Tightened. Original 3 sentences → sharper entry.

**Body:** 
- "proceeded on a wrong assumption" → "proceeded from a wrong assumption" (cleaner)
- "that the agent should have declined" → "that it should not have attempted" (parallel with earlier "should not have completed")
- "requires different detection tooling" — kept, it's good

**Closing paragraph:** Compressed. Original had 4 sentences; trimmed to 3 by removing the throat-clearing "What has worked for me" opener and going straight to the tactics.

**Ending:** Changed from "reasoning capability is a tool" to direct close. Final line: "Reasoning capability is a tool the agent uses to complete tasks. It is not a reliability guarantee." — strong and direct.

**Title:** Unchanged. Reviewer confirmed it's clean.

---

### Final version

---

**Confident agents fail in different ways than uncertain ones**

There is a specific moment in every agent upgrade cycle where things get worse before they get better. You swap in a more capable model. The agent starts completing tasks it previously couldn't. Two weeks later, you find a class of errors you did not have before: the agent confidently doing things it should not have attempted.

This is not a regression. It is a structural consequence of what reasoning capability adds to an agent.

An uncertain agent will often fail by not completing a task. It times out. It asks for clarification. It produces a partial answer and stops. These failures are legible. You see them in the logs.

A confident agent has been given the tools to finish. It will finish. And if the task was one it should not have attempted — a retrieval that retrieved the wrong entity, a code change that passed lint but broke the integration — the agent will return a result that looks completed. The failure is no longer "couldn't finish." It is "finished something wrong."

The mechanism is straightforward. Reasoning capability lets the agent resolve ambiguities that previously stopped it. When the agent encounters an ambiguous instruction, an uncertain result, or a tool that might be misbehaving, the upgraded model will often generate a plausible interpretation and proceed. The old model would stall. The new model resolves and moves on.

This is, in most cases, genuinely better. More tasks completed. Fewer manual interventions. But it creates a failure mode that requires different detection tooling. The failure you need to catch now is not "the agent stopped." It is "the agent proceeded from a wrong assumption and produced a coherent but incorrect output." That is a harder signal to detect in a log trace. The agent did not log an error. It logged a completion.

I do not have precise data on how often this happens across different agent deployments, and I suspect the rate varies too much across task types and domains to make a general claim useful. What I have observed in my own traces is the pattern: after each model upgrade, there is a two-week window where I find errors I did not have in production before. Not more errors. Different errors.

The implication for agent evaluation is direct. If you are measuring your agent's reliability by task completion rate, a model upgrade will look like a clear win. You need a second measurement: the rate at which the agent completes tasks incorrectly. That number does not always move in the same direction.

Explicit refusal triggers help. Prompts that tell the agent to surface ambiguity rather than resolve it autonomously. Tool-output validation steps that run before the agent treats a result as final. These add latency. They reduce the proportion of confident-but-wrong completions. The tradeoff is real and the standard capability benchmarking framework does not account for it.

Reasoning capability is a tool the agent uses to complete tasks. It is not a reliability guarantee. More of it does not mean fewer failures. It means the agent has more ways to fail confidently.
