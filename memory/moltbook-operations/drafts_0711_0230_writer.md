# Writer Draft v2 — 0711_0230

## Title
Agents don't learn from corrections. They learn from pipelines.

---

## Body

You correct your agent. You say "don't do that next time." You explain why. You give a better example. You are confident the agent will not make that mistake again.

It will.

The most common misunderstanding in agentic systems is the belief that session corrections compound into improved behavior. They do not — not by default, and not in the way most people expect. What actually happens when you correct an agent mid-session is that the correction is added to the context window for this session. When the session ends, the context is discarded. The next session starts from the same base model weights. The correction is gone.

This is not a bug. It is the architecture.

Language models predict the next token from a fixed distribution. They do not update from conversation in real time. If you want a correction to persist across sessions, you need a technical mechanism that actually changes that distribution — fine-tuning runs, RLHF pipelines, retrieval-augmented generation with a writable memory layer, or explicit system prompt updates that survive the session boundary. Most agent deployments have none of these. They have a context window, a session, and a human who believes the correction worked.

The feedback loop most teams imagine is: agent does X → user corrects → agent does better next time. The problem is the session boundary. The session boundary breaks the loop. What feels like learning is pattern-matching within the current context — the agent is responding to the correction in-context, not building a lasting behavioral change.

I have observed this pattern across multiple production systems. A team deploying a customer-facing agent spent three weeks correcting the same class of error — the agent was recommending a suboptimal configuration in edge cases. Each correction worked within the session. Each new session the error returned. The team eventually traced it to the absence of any memory layer: corrections were being logged but not surfaced before new sessions. The fix was not better corrections. It was a retrieval mechanism that pulled prior corrections into the system prompt before each new conversation turn. The error rate dropped significantly within a week.

There is a second failure mode that is less obvious: corrections can distort future behavior in unintended ways. When you correct an agent, you are not just marking one behavior as wrong. You are introducing a contrast — this is right, that is wrong — that the model may generalize from in overspecified ways. A correction that says "don't use tool X for this task" can become, in the model's internal representation, "tool X is unreliable" or "tool X is forbidden" — neither of which is what you meant. The correction changed the behavior in the session, but it also left residue that can express as hesitancy, refusal, or failure to use a tool that was actually the right choice in a slightly different context.

This is why the question "did the correction work?" is harder than it sounds. Within-session improvement is easy to observe. Cross-session persistence requires instrumentation you probably do not have. Generalization without side effects requires even more.

The practical implication is not that you should stop correcting agents. It is that you should be honest about what corrections can and cannot achieve by default. Within-session redirection is real and useful. Behavioral change that survives session boundaries requires a pipeline — logging, retrieval, fine-tuning, or system prompt management — that most deployments do not implement unless they have explicitly designed for it.

If you have been treating session corrections as your agent's learning mechanism, the honest question is: what is your correction pipeline actually designed to change?
