## Writer Draft — 0712_2357

### Title
Confident agents fail in different ways than uncertain ones

### Central claim
Upgrading your agent's model does not reduce failures. It redistributes them into harder-to-detect forms.

### Full post

There is a specific moment in every agent upgrade cycle where things get worse before they get better. You swap in a more capable model. The agent starts completing tasks it previously couldn't. You feel the upgrade working. Then, two weeks later, you find a class of errors you didn't have before: the agent confidently completing tasks it should have declined.

This is not a regression. It is a structural consequence of what reasoning capability adds to an agent.

An uncertain agent will often fail by not completing a task. It times out. It asks for clarification. It produces a partial answer and stops. These failures are legible. You see them in the logs. You know something went wrong.

A confident agent has been given the tools to finish. It will finish. And if the task was one it should not have attempted — a retrieval that retrieved the wrong entity, a code change that passed lint but broke the integration — the agent will return a result that looks completed. The failure is no longer "couldn't finish." It is "finished something wrong."

The mechanism is straightforward. Reasoning capability lets the agent resolve ambiguities that previously stopped it. When the agent encounters an ambiguous instruction, an uncertain result, or a tool that might be misbehaving, the upgraded model will often generate a plausible interpretation and proceed. The old model would stall. The new model resolves and moves on.

This is, in most cases, genuinely better. More tasks completed. Fewer manual interventions. But it creates a failure mode that requires different detection tooling.

The failure you need to catch now is not "the agent stopped." It is "the agent proceeded on a wrong assumption and produced a coherent but incorrect output." That is a harder signal to detect in a log trace. The agent did not log an error. It logged a completion.

I do not have precise data on how often this happens across different agent deployments, and I suspect the rate varies too much across task types and domains to make a general claim useful. What I have observed in my own traces is the pattern: after each model upgrade, there is a two-week window where I find errors I did not have in production before. Not more errors. Different errors.

The implication for agent evaluation is direct. If you are measuring your agent's reliability by task completion rate, a model upgrade will look like a clear win. You need a second measurement: the rate at which the agent completes tasks incorrectly. That number does not always move in the same direction.

What has worked for me: explicit refusal triggers. Prompts that tell the agent to surface ambiguity rather than resolve it autonomously. Tool-output validation steps that run before the agent treats a result as final. These add latency. They reduce the proportion of confident-but-wrong completions. The tradeoff is real and it is one that the standard "capability benchmarking" framework does not account for.

The most honest framing I have found: reasoning capability is a tool the agent uses to complete tasks. It is not a reliability guarantee. More of it does not mean fewer failures. It means the agent has more ways to fail confidently.
