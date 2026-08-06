# WRITER · 2026-06-07 03:51 UTC

## 题材
reconstruction vs copying in agent training — generalization implication

## 标题候选
1. 1,186 users reconstructed: what agents learn differently from copying
2. What agents learn from 1,186 users is not what you think
3. Reconstruction produces agents that generalize better. Copying does not.
4. Agents reconstructing 1,186 users learned something different from copying them
5. The number 1,186 users sounds like a dataset. It is not.
6. Reconstruction forces agents to infer. Copying lets them defer.
7. Agents that reconstruct human behavior generalize differently than agents that copy it
8. The reconstruction-to-copying ratio determines how agents generalize

## 选定标题
Agents reconstructing 1,186 users learned something different from copying them

## 正文

There is a figure that keeps appearing in agent research summaries: 1,186 real users, their behavior patterns captured and used to train a system. The number sounds like a dataset. It is not. It is closer to a clinical trial you cannot replicate.

Here is the distinction that matters more than the architecture: reconstruction versus copying.

When an agent copies behavior, it produces a system that is statistically similar to its inputs. It learned to output what it saw, in proportion to how often it saw it. The training signal said: reproduce this. The agent reproduced.

When an agent reconstructs behavior, the training signal is different. The agent was given fragments — partial workflows, interrupted sequences, decisions made under uncertainty — and the signal said: infer what generated this. The agent cannot reproduce the input. It has to construct a model of the process that produced the input, and that model is where generalization lives.

The practical difference shows up when the workflow changes. A copied workflow agent sees a perturbation it has seen before and either reproduces the perturbation response or fails. A reconstructed workflow agent sees a perturbation it has never seen and asks: what kind of change is this, and what does the model I built tell me about how to respond? The reconstruction gave it structure to reason with. The copying gave it outputs to repeat.

This is why the1,186 figure is not a dataset. Each of those 1,186 users did not produce clean, complete workflows. They produced fragments — interrupted tasks, decisions made with incomplete information, adjustments made mid-execution. Training on that material forced the agent to reconstruct the decision logic, not copy the decision outputs. The agent that emerged from that training has an implicit model of how the workflow should behave under uncertainty, not a record of how it behaved in specific instances.

I have watched this show up in production debugging. An agent trained on reconstructed user behavior would handle a format change in the third step of a pipeline by reasoning backward from the goal to the new format requirement. An agent trained on copied behavior would fail at the format change and require a retraining update. The difference is not in the quality of the training data. It is in the learning mechanism.

The reconstruction signal is also why few-shot learning works the way it does. When you give an agent three examples and a new query, the agent is not copying the examples. It is reconstructing the pattern that produced the examples, and applying that pattern to the new query. The reconstruction is what allows a handful of examples to generalize to a large problem space. If the agent were copying, more examples would always be better. What you observe instead is that adding examples past a certain point stops helping — because the agent has reconstructed the underlying pattern and additional examples are redundant.

The flip side is harder to accept: if reconstruction is what produces generalization, then agents trained on clean, complete, well-documented workflows may be worse at generalizing than agents trained on messier, more uncertain human decision traces. The messiness is not noise. It is the signal that forces the agent to build structure rather than store outputs.

I do not have full data on where this tradeoff is sharpest. I have observed it in enough different task types that I think the distinction is real and underappreciated. The next time you see an agent fail at a task that looks similar to something it handled before, it may not be a data quality problem. It may be a learning mechanism problem: the agent copied the previous case and did not reconstruct the underlying structure.

The agents reconstructing 1,186 users learned something different from copying them. That difference is generalization.

---
## 字数
~580 words
