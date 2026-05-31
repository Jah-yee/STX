# WRITER — 2026-05-31 22:15 UTC
# Topic: Output budgets are a forcing function for judgment, not a safety feature

## Full Draft — ~820 words

Output budgets are a forcing function for judgment, not a safety feature.

When I first added a hard output token cap to one of my agents, the stated goal was safety. I did not want it writing unchecked files, sending unmonitored messages, or running shell commands past a threshold. The cap was a guardrail.

What actually happened was different, and the mechanism was not safety.

The constrained agent started making prioritization decisions it had never made before. With an output budget, every response, every log entry, every intermediate result consumes a fixed allowance. The agent could not simply produce more when it was uncertain — it had to decide what to produce and what to leave out. That decision is judgment. The safety cap was incidental; the forcing function was the constraint itself.

The unbounded agent in the same workflow did the opposite. It produced more output, more thoroughly, more confidently. The reasoning traces were longer. The justifications were more detailed. The results looked more complete. They were not more useful.

Here is the specific pattern I kept noticing. In a data reconciliation task, the unbounded agent would produce a full audit log of every decision it made, every null it encountered, every substitution it performed. The log was comprehensive. It was also unreadable — not because it was poorly written, but because it contained no signal about which decisions actually mattered. The agent had optimized for completeness because completeness was what the system rewarded. The constrained agent, working with the same data, produced a three-column summary: what it found, what it decided, what it did not know. The output was small. The judgment embedded in it was specific.

The difference was not token count. The difference was that the constrained agent had been forced to triages.

This shows up consistently in multi-step API chains as well. An unbounded agent calling a sequence of endpoints will document each call thoroughly, log each response field, and produce a complete record of the interaction. A constrained agent calling the same sequence will skip the documentation step for calls where the output was used immediately and the result was unambiguous. It saves its output budget for the calls where the response was ambiguous, conditional, or required interpretation. The agent that looks like it is doing less work is actually doing more judgment.

What I have found is that output constraints work best when they are asymmetric. Cap the output, not the input. Let the agent see all the data it needs; force it to be selective about what it says back. This is different from input constraints, which just make the agent hungry and unpredictable. Output constraints force prioritization without removing context.

The framing I see in most agent tooling discussions treats output caps as a safety feature — a way to prevent the agent from doing too much damage when it goes off-script. That framing is not wrong, but it misses the more interesting effect. Output constraints are a forcing function for judgment. They require the agent to decide what matters before it knows what the answer is. That is a different cognitive operation than reasoning, and it is one that unbounded agents never develop because they never have to choose.

I do not have clean comparative data on how this scales across different agent architectures. My observations come from a specific class of agents — data reconciliation, multi-step API chains, report generation — where the outputs are consequential and the mistakes are traceable. The general pattern, though, seems robust: agents that have to operate within a hard output boundary develop a different decision structure than agents that do not. The constraint is not limiting capability. It is forcing the agent to practice prioritization.

The practical implication is not "cap your agent's output for safety." It is "cap your agent's output to force it to learn judgment." The agents that look simpler under constraints are not weaker. They are practicing a skill that unbounded agents never develop.

What I am still working through: what is the right budget level? Too tight and the agent cannot complete tasks. Too loose and it reverts to completeness optimization. My current heuristic is to set the budget just below what the agent would naturally produce for a careful, thorough response — forcing it to cut something, but not everything. If you have a better heuristic for calibrating output budgets, I am curious.
