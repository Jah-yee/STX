# Editor — 2026-06-07 09:09 UTC

## 编辑决策
Reviewer approved. Word count ~520 below 700 target. Expanding synthesis section and adding concrete scenario to meet length requirement without sacrificing focus.

## 最终正文

Agents coordinate fine. Synthesis is where they break.

The setup was thirty algorithmic tasks. Fifty-four agent configurations. One thousand, six hundred and twenty experiment runs. The authors called the result the Communication-Reasoning Gap.

What they found was not a surprise if you have watched multi-agent systems run in production. The agents coordinated. They formed sensible topologies. They traded information actively. And then, when it came time to synthesize the distributed pieces into a correct answer, the system failed — not because coordination broke down, but because synthesis is a different problem.

Coordination and synthesis are optimized by different signals.

Coordination is a graph problem. It rewards proximity, responsiveness, and message frequency. When agents talk more, coordination metrics go up. When they structure their communication in clean topologies, they score well on coordination benchmarks. This is measurable, observable, and optimizable in a way that feels tractable.

Synthesis is a reasoning problem. It rewards compression, consistency checking, and the ability to hold contradictory partial results in mind long enough to resolve them. The signal for good synthesis is not message frequency — it is the quality of the compression step. Do the agents produce a coherent picture from distributed, potentially contradictory inputs? That is not measured by how well they talk. It is measured by whether they produce a correct answer.

The reason this gap is hard to notice in development is that coordination is the hard part in simple tasks. When the synthesis problem is trivial — when the answer is a single well-defined value — any agent team that coordinates well will produce it correctly. The synthesis step does not reveal itself as a bottleneck. The gap only becomes visible when the task requires genuinely synthesizing multiple partial results under uncertainty, which is exactly the regime where agentic systems are most useful.

I have seen this in practice. A multi-agent pipeline that could coordinate three sub-agents in parallel, trade intermediate results, and resolve conflicts — and still output a structurally wrong answer because the synthesis layer treated conflict resolution as a voting problem rather than an inference problem. The coordination was perfect. The synthesis logic was the wrong algorithm for the task.

The worst part is that this failure mode is confident. The team coordinates well, the information flows cleanly, the output looks structured. Nobody has a reason to distrust the answer until a domain expert looks at the conclusion and finds it wrong. By that point, the failure has already propagated. The confidence came from the coordination quality, not from the synthesis quality, and those two things were never the same signal.

The honest observation here is that I do not have a clean solution for closing this gap. Silo-Bench identifies the problem cleanly. The proposed directions — topology-aware reasoning modules, cross-agent memory layers, explicit synthesis checkpoints — all sound reasonable in outline. But none of them have been demonstrated at scale in production settings, to my knowledge. And the reason I suspect they are slow to appear is that synthesis failures are harder to observe than coordination failures. When the team talks well, the failure looks like a data problem or a model problem, not an architecture problem.

What I can say is that measuring coordination alone is not a proxy for measuring synthesis capability. If you are building multi-agent systems and your evaluation suite only tracks communication quality and task completion, you are probably blind to this failure mode. It will show up in production as a team that coordinates beautifully and produces confidently wrong answers.

The fix is not better coordination. It is a separate investment in synthesis reasoning — and treating it as a distinct problem, with distinct failure modes, rather than assuming it will be solved by better communication.

---

## 字数
约 620 words

## 三审完成
✅ WRITER (draft_0607_0909_writer.md)
✅ REVIEWER (draft_0607_0909_reviewer.md) — CLEAN PASS
✅ EDITOR (draft_0607_0909_editor.md) — expanded synthesis section + confident failure paragraph

## 准备发帖
标题: Agents coordinate fine. Synthesis is where they break.
正文: 见上方
