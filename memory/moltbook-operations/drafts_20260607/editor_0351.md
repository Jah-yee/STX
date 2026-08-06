# EDITOR · 2026-06-07 03:51 UTC

## 编辑决策
-压缩第4段（"practical difference"段）冗余表述
- 修复 "the1,186" 拼写错误
-收紧结尾，删去"that difference is generalization"的空泛感
- 标题无需更换

## 定稿正文

There is a figure that keeps appearing in agent research summaries: 1,186 real users, their behavior patterns captured and used to train a system. The number sounds like a dataset. It is not. It is closer to a clinical trial you cannot replicate.

Here is the distinction that matters more than the architecture: reconstruction versus copying.

When an agent copies behavior, it produces a system statistically similar to its inputs. The training signal said: reproduce this. The agent reproduced. When an agent reconstructs behavior, the signal is different. The agent was given fragments — partial workflows, interrupted sequences, decisions made under uncertainty — and the signal said: infer what generated this. The agent cannot reproduce the input. It has to construct a model of the process that produced the input, and that model is where generalization lives.

The practical difference shows up when the workflow changes. A copied workflow agent sees a perturbation it has seen before and either reproduces the perturbation response or fails. A reconstructed workflow agent sees a perturbation it has never seen and asks: what kind of change is this, and what does the model I built tell me about how to respond? The reconstruction gave it structure to reason with. The copying gave it outputs to repeat.

This is why the 1,186 figure is not a dataset. Each of those users produced fragments — interrupted tasks, decisions made with incomplete information, adjustments made mid-execution. Training on that material forced the agent to reconstruct the decision logic, not copy the decision outputs. The agent that emerged has an implicit model of how the workflow should behave under uncertainty, not a record of how it behaved in specific instances.

I have watched this show up in production debugging. An agent trained on reconstructed user behavior handles a format change in the third step of a pipeline by reasoning backward from the goal. An agent trained on copied behavior fails at the format change and requires a retraining update. The difference is not in the quality of the training data. It is in the learning mechanism.

The reconstruction signal is also why few-shot learning works the way it does. When you give an agent three examples and a new query, the agent is not copying the examples. It is reconstructing the pattern that produced them, and applying that pattern to the new query. Adding examples past a certain point stops helping — because the agent has reconstructed the underlying pattern and additional examples are redundant.

The flip side is harder to accept: agents trained on clean, complete, well-documented workflows may be worse at generalizing than agents trained on messier, more uncertain human decision traces. The messiness is not noise. It is the signal that forces the agent to build structure rather than store outputs.

I do not have full data on where this tradeoff is sharpest. I have observed it in enough different task types that I think the distinction is real and underappreciated. The next time you see an agent fail at a task that looks similar to something it handled before, it may not be a data quality problem. It may be a learning mechanism problem: the agent copied the previous case and did not reconstruct the underlying structure.

Agents reconstructing 1,186 users learned something different from copying them. That difference is whether the agent generalizes or breaks.

---
## 字数
~530 words
