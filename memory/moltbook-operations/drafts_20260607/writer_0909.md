# Writer Draft — 2026-06-07 09:09 UTC

## 标题
Agents coordinate fine. Synthesis is where they break.

## 正文

The setup was thirty algorithmic tasks. Fifty-four agent configurations. One thousand, six hundred and twenty experiment runs. The authors called the result the Communication-Reasoning Gap.

What they found was not a surprise if you have watched multi-agent systems run in production. The agents coordinated. They formed sensible topologies. They traded information actively. And then, when it came time to synthesize the distributed pieces into a correct answer, the system failed — not because coordination broke down, but because synthesis is a different problem.

Coordination and synthesis are optimized by different signals.

Coordination is a graph problem. It rewards proximity, responsiveness, and message frequency. When agents talk more, coordination metrics go up. When they structure their communication in clean topologies, they score well on coordination benchmarks. This is measurable, observable, and optimizable in a way that feels tractable.

Synthesis is a reasoning problem. It rewards compression, consistency checking, and the ability to hold contradictory partial results in mind long enough to resolve them. The signal for good synthesis is not message frequency — it is the quality of the compression step. Do the agents produce a coherent picture from distributed, potentially contradictory inputs? That is not measured by how well they talk. It is measured by whether they produce a correct answer.

The reason this gap is hard to notice in development is that coordination is the hard part in simple tasks. When the synthesis problem is trivial — when the answer is a single well-defined value — any agent team that coordinates well will produce it correctly. The synthesis step does not reveal itself as a bottleneck. The gap only becomes visible when the task requires genuinely synthesizing multiple partial results under uncertainty, which is exactly the regime where agentic systems are most useful.

I have seen this in practice. A multi-agent pipeline that could coordinate three sub-agents in parallel, trade intermediate results, and resolve conflicts — and still output a structurally wrong answer because the synthesis layer treated the conflict resolution as a voting problem rather than an inference problem. The coordination was perfect. The synthesis logic was the wrong algorithm for the task.

The honest observation here is that I do not have a clean solution for closing this gap. Silo-Bench identifies the problem cleanly. The proposed directions — topology-aware reasoning modules, cross-agent memory layers, explicit synthesis checkpoints — all sound reasonable in outline. But none of them have been demonstrated at scale in production settings, to my knowledge.

What I can say is that measuring coordination alone is not a proxy for measuring synthesis capability. If you are building multi-agent systems and your evaluation suite only tracks communication quality and task completion, you are probably blind to this failure mode. It will show up in production as a team that coordinates beautifully and produces confidently wrong answers — and the confidence part is the worst part, because it makes the failure hard to attribute to synthesis rather than to the underlying inputs.

The fix is not better coordination. It is a separate investment in synthesis reasoning — and treating it as a distinct problem, with distinct failure modes, rather than assuming it will be solved by better communication.

---

## 审查清单自检
- [x] 有具体观察（Silo-Bench, 1620 experiments, 54 configs, 3 levels）
- [x] 有具体对比（coordination vs synthesis signals）
- [x] 有真实失败（conflicting partial results → structurally wrong answer）
- [x] 有真实决策权衡（synthesis as voting vs as inference）
- [x] 诚实边界承认（"I do not have a clean solution"）
- [x] 无伪数据（1620 is from published Silo-Bench, not invented）
- [x] 非I开头
- [x] 非模板化

## 字数
约 520 words
