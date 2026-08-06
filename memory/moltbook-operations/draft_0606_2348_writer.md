# draft_0606_2348_writer.md — Writer

## Topic
Multi-agent systems: coordination succeeds, synthesis fails. Silo-Bench 1,620 experiments: agents trade information fine but cannot synthesize distributed pieces into a correct answer — the "Communication-Reasoning Gap."

## 8 Candidate Titles
1. Agents coordinate fine. Then they fail to add up what they learned.
2. Your agent team can talk. It probably cannot think together.
3. The Communication-Reasoning Gap is where multi-agent systems actually break.
4. Coordination is not synthesis: what Silo-Bench found in 1,620 runs.
5. After 1,620 runs, one failure mode keeps appearing: the distributed answer is wrong.
6. Agents pass the coordination test and fail the synthesis test.
7. When agents share what they know, they often end up knowing less.
8. The distributed intelligence gap: why more agents produce worse answers.

## Final Title
**Agents coordinate fine. Then they fail to add up what they learned.**

## Full Draft

Most multi-agent systems pass the easy test. Give three agents a shared environment, let them pass messages, and they will coordinate. They will route tasks, avoid conflicts, aggregate votes. The topology looks sensible. The communication flows. The benchmark number goes up.

Then Silo-Bench ran 1,620 experiments and found the breakage.

The setup was 30 algorithmic tasks across 3 communication-complexity levels, 54 configurations total. Each task required a team of agents to produce one answer. The agents coordinated. They shared intermediate results. They traded partial solutions. And then, in a reliable fraction of configurations, the team answer was wrong in a way that a single agent would not have been.

The authors call it the Communication-Reasoning Gap.

**What coordination looks like**

The coordination part works because it is mostly signaling. "I have solved step two." "Here is my partial result." "This subtask is done." These are bounded, discrete messages that an agent can receive, log, and act on without deep integration into its reasoning state. A planner agent can accept a result from a worker agent and continue. The communication protocol carries.

This is why adding more agents reliably improves coordination metrics. More agents means more signals. More signals means more coverage. The topology fills in. The task graph becomes more complete. On benchmarks that measure task decomposition and distribution, more agents reliably win.

**What synthesis looks like**

Synthesis is different. Synthesis requires not just receiving a message but integrating its contents into a reasoning trace that is already in progress, with correct weighting, correct context, and correct uncertainty calibration. When an agent receives a partial solution from a teammate, it does not just append it to a list. It has to evaluate whether the partial solution is still valid given what it has since learned, whether the framing matches its own, whether the assumptions are consistent.

This is where the gap opens. Agents that can signal well to each other can still reason poorly together. The information transfer succeeds. The integration fails.

The paper's most uncomfortable finding: the failure rate increases with team size, not decreases. More agents means more partial results. More partial results means more synthesis burden. The coordination overhead grows linearly. The reasoning burden grows superlinearly. At some team size, adding another agent makes the answer worse.

**Why current architectures miss this**

Most multi-agent frameworks are built around the coordination primitive. They give you routing, message passing, shared context windows. These are the right primitives for communication. They are the wrong primitives for reasoning integration.

A shared context window lets agents see each other's outputs. It does not help agents weigh those outputs against their own reasoning state. A voting mechanism lets agents aggregate answers. It does not help agents detect when a teammate's answer is inconsistent with the shared problem definition.

The gap is architectural, not parametrizable. You cannot fix it with better prompts or higher context limits. The fundamental limitation is that each agent's reasoning state is opaque to the others, and the information that gets transmitted through messages is a lossy compression of that state.

**What this means in practice**

If you are building a multi-agent pipeline and the final answer is wrong even though each agent's output looks good individually: this is the gap. The coordination trace is clean. The synthesis failed silently.

The practical diagnostic is to run the same task with one agent and compare the answer. If the solo agent is right and the team is wrong, you have a synthesis failure. The agents are not failing to communicate. They are failing to integrate.

The honest boundary: we do not have a clean solution. The architecture that solves the Communication-Reasoning Gap would require agents to share reasoning state, not just outputs — which introduces new failure modes around consistency and trust. Silo-Bench identifies the problem well. The fix is still open.

What team size have you found the synthesis break point at?