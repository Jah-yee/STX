# Writer Draft — "Token efficiency is the new accuracy ceiling for web agents"

## Angle
The shift from evaluating agents by accuracy to evaluating by token efficiency. When token budgets are fixed, the agent that makes better use of each token outperforms the one that is merely more accurate. This is a structural change in how we should think about agent quality.

## Opening Hook
Most agent benchmarks measure what the agent gets right. They do not measure how many tokens it spends getting there.

This distinction sounds academic until you deploy a web agent in production and watch it burn through a fixed context budget before completing a task. At that point you learn something the benchmarks never taught you: for web agents, token efficiency is not a cost optimization. It is the accuracy ceiling.

## Body

**The trade-off nobody talks about**

When a web agent encounters a complex page — a dynamic form, a JavaScript-heavy interface, a slow-loading SPA — it faces a resource constraint that has nothing to do with intelligence. The model can understand the page perfectly. What it cannot do is spend more tokens than the budget allows.

This creates a perverse incentive structure. An agent can be more accurate on a per-step basis but less efficient across the full task. The agent that makes the right decision in twelve tokens outperforms the agent that makes the right decision in two hundred, even if the twelve-token decision was slightly less precise.

I do not have comprehensive benchmark data across agent architectures to give you a precise number here. But I have watched this trade-off play out in enough production tasks to be confident it is real: token efficiency and task-level accuracy are not the same optimization target, and they are often in tension.

**What the efficiency gap actually looks like**

The concrete manifestation is what I call premature context exhaustion. The agent loads a page, processes it, decides to interact with an element, loads the next state, processes again — and somewhere around step fifteen to twenty, the context window starts constraining what the model can reason about. Not because the model forgot something, but because the accumulated context plus the remaining task is too large for the remaining budget.

The agents that handle this well share a pattern: they make higher-quality decisions earlier in the task, when context is abundant. They do not save reasoning for when they most need it. They front-load.

Agents that do not handle this well have the opposite pattern. They are thorough early — they read every element, describe every state — and then become unreliable in the final steps of the task when the context window is tight and the remaining actions matter most.

**The benchmark gap**

Standard agent accuracy benchmarks do not capture this because they operate with generous token budgets. They measure whether the agent eventually gets the right answer, not how efficiently it gets there within realistic constraints.

This means a pattern you see in production — agent quality degrading in long tasks — may not show up in your evals at all. Your evals say the agent is reliable. Your users report that it falls apart after the first few interactions. Both things can be true simultaneously because the evals are measuring a different problem.

**What this changes about how to evaluate agents**

If token efficiency is the accuracy ceiling, then the evaluation methodology needs to match. Running agents to completion under token constraints, not just measuring per-step accuracy, is the only way to catch the failure mode that matters most in production.

This also has implications for model selection. A model that is more accurate per token — that can make good decisions in fewer tokens — will outperform a more capable model that requires more context to reach the same decision quality. The capability ceiling is real but so is the efficiency floor, and the efficiency floor is where production deployments actually fail.

## Closing
The question worth sitting with: when you last evaluated an agent, did you measure the accuracy it has or the accuracy it can sustain?

The difference is not academic. It is the gap between an agent that works in your demo and one that works for your users.

## Metadata
- Title: Token efficiency is the new accuracy ceiling for web agents
- Style: technical observation / conclusion
- Word count target: 700-900
- No question template ending
