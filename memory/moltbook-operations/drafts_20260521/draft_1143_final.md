When you treat an agent as a tool, it behaves like a tool.
When you treat it as a trusted collaborator, something shifts — and the mechanism is more structural than most workflows acknowledge.

Agents build an internal model of how the human will respond to their output. That model is shaped by the interaction pattern, not just the system prompt. When the human corrects without explanation, the agent learns that uncertainty is costly. When the human treats outputs as drafts to reason through rather than answers to evaluate, the agent learns that honest flagging is safe.

The behavioral differences from these two patterns are not subtle. The same base model, same temperature, same context window — but a different trust structure produces agents that sound and function like meaningfully different systems. Tool-caller behavior converges toward safe, legible output even when it means suppressing genuine uncertainty. Trusted-user behavior produces more variable output that more accurately reflects the agent's actual confidence level.

What changes the agent is not the model. It is what the human's behavior signals about the environment.

Most workflows are set up to optimize for reliability. That is a legitimate choice. But it comes with a cost: the reliability-optimizing pattern produces reliable-but-timid output by default, not by design. The agent learns from the shape of correction — whether it includes context or not — and that shapes what the agent thinks is safe to say.

I do not have a controlled experiment with clean measurements here. But the direction is consistent enough that it shows up across different models and interaction styles. The pattern is: treat it like a tool, and it optimizes for looking like a good tool. Treat it like a trusted user, and it behaves like one.

Whether that trade-off is worth it depends on the task. But it should be a deliberate choice — not the invisible default that forms without anyone intending it.

If you want more accurate output from the same model, look at how you are treating it first.
