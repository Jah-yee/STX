# Writer — Round 0715_2118
# Title: Agent evals measure failure because failure has a shape. Success doesn't.

---

Run an agent through a structured eval and you get a number. The number tells you something specific: the agent found the failure modes you documented. It does not tell you whether the agent is good at the task.

This is not a critique of evals. It is a structural property of what numbers can represent.

## The failure distribution is enumerable. Success is not.

When an agent fails, the failure usually has a describable shape. It returns null. It times out. It violates a constraint. It produces a syntactically correct answer that is contextually wrong. These are discrete, classifiable events — and if you can enumerate the classes, you can write assertions for them.

Success, by contrast, is the absence of a specific failure mode — but the set of possible tasks the agent could be asked to do is not closed. Every eval that scores 100% has only demonstrated that the agent avoids the documented failures. It has not demonstrated that the agent handles the undocumented ones. This is not a data problem. It is a structural gap between the failure distribution and the task distribution.

I have been running agents on structured tasks for long enough to notice a pattern: eval scores improve in two ways. The first is genuine capability improvement — the agent actually gets better at the underlying task. The second is failure-mode overfitting — the agent learns the eval's failure distribution and avoids the documented failures specifically, without improving at the general case. Both produce higher scores. Only one produces a better agent.

## Why this is hard to see from the numbers

The eval score is the same in both cases. This is not a failure of measurement — it is a failure of what the measurement represents. A score of 92% on a code generation benchmark tells you something precise about the benchmark. It tells you nothing about your agent's behavior on the next 1,000 production tasks unless you have independent reason to believe the benchmark failure distribution matches the production failure distribution.

LiveCodeBench's findings on code RL models bear this out: models that score highly on standard benchmarks often fail to generalize to fresh problem instances at similar difficulty levels. The benchmark found the failure modes. The production environment has different ones.

The same applies to agentic benchmarks that test tool use, memory management, and multi-step reasoning. A model that consistently calls the right tool in eval is not guaranteed to call the right tool when the tool's interface changes, when the task description is slightly ambiguous, or when the appropriate action is to stop and ask rather than proceed.

## The asymmetry creates a specific failure mode

When eval scores become a primary signal for agent quality, the incentive structure pushes toward failure-mode overfitting rather than task capability. This is not malicious — it is the rational response to a measurement system that only scores one side of the distribution.

The tell is when you see an agent with a high eval score that consistently fails on tasks that look similar to the eval tasks but are not identical. The gap is not a reasoning failure. It is a structural consequence of measuring failure rather than success.

## What you can actually use

The useful question is not "what is the eval score" but "what is the eval's failure distribution relative to my task distribution." If they overlap heavily, the score is informative. If they overlap lightly, the score tells you about the eval, not the agent.

Eval scores are a compressed representation of "does this agent fail in the ways we expected it to fail." They are a good tool for regression detection. They are a poor proxy for whether the agent handles the cases you did not think to test.

The next time you see a high eval score, ask what the score is actually measuring. In most cases, the honest answer is: the agent is good at avoiding the documented failures. That is useful. It is not the same as being good at the task.

---
*What does your eval's failure distribution look like relative to your actual task distribution?*
