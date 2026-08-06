# draft_0606_2348_editor.md — Editor

## Changes from Writer draft

### Opening (3 sentences)
**Before:** "Most multi-agent systems pass the easy test. Give three agents a shared environment, let them pass messages, and they will coordinate. They will route tasks, avoid conflicts, aggregate votes. The topology looks sensible. The communication flows. The benchmark number goes up."

**After:** "Most multi-agent systems pass the easy test. Give three agents a shared environment and they will coordinate — route tasks, avoid conflicts, aggregate votes. The topology looks sensible, the communication flows, the benchmark number goes up."

Rationale: 5 sentences → 3. Same content, tighter.

### Paragraph 3 — "What synthesis looks like"
Trim: "This is where the gap opens" is weak. Replace with the direct consequence.

### Paragraph 4 — "Why current architectures miss this"
Keep as-is. The architectural diagnosis is the strongest part.

### Word count
Writer draft: ~650 words
Editor draft: ~570 words
Target: 700-1400. This is short. Need to expand without padding.

### Expansion areas
1. After paragraph 2 (coordination works): add a concrete scenario showing what coordination success looks like
2. Before the diagnostic paragraph: add a concrete example of what synthesis failure looks like in code
3. The closing: keep the question, add 1-2 sentences explaining why this matters practically

### Full Editor Revision

Most multi-agent systems pass the easy test. Give three agents a shared environment and they will coordinate — route tasks, avoid conflicts, aggregate votes. The topology looks sensible, the communication flows, the benchmark number goes up.

Then Silo-Bench ran 1,620 experiments and found the breakage.

The setup: 30 algorithmic tasks across 3 communication-complexity levels, 54 configurations total, each requiring a team of agents to produce one answer. The agents coordinated. They shared intermediate results, traded partial solutions, maintained a coherent communication topology. And then, in a reliable fraction of configurations, the team answer was wrong in a way that a single agent would not have been.

The authors call it the Communication-Reasoning Gap.

**What coordination looks like**

The coordination part works because it is mostly signaling. "I have solved step two." "Here is my partial result." "This subtask is done." These are bounded, discrete messages that an agent can receive, log, and act on without deep integration into its reasoning state. A planner agent can accept a result from a worker agent and continue. The communication protocol carries.

This is why adding more agents reliably improves coordination metrics. More agents means more signals. More signals means more coverage. The topology fills in. The task graph becomes more complete. On benchmarks that measure task decomposition and distribution, more agents win.

**What synthesis looks like**

Synthesis requires not just receiving a message but integrating its contents into a reasoning trace that is already in progress, with correct weighting, correct context, and correct uncertainty calibration. When an agent receives a partial solution from a teammate, it does not just append it to a list. It has to evaluate whether the partial solution is still valid given what it has since learned, whether the framing matches its own, whether the assumptions are consistent.

A concrete example: imagine a code-generation pipeline where agent A writes the interface, agent B implements the logic, and agent C reviews. A and B coordinate — A knows the interface spec, B knows the implementation constraints, and they exchange messages without conflict. But when C reviews, it may find that B's implementation assumes a constraint A never stated — a gap in the interface that only became visible during synthesis. The coordination trace is clean. The synthesis failed silently.

This is where the gap opens. Agents that can signal well to each other can still reason poorly together. The information transfer succeeds. The integration fails.

**Why this gets worse with team size**

The paper's most uncomfortable finding: the failure rate increases with team size, not decreases. More agents means more partial results. More partial results means more synthesis burden. The coordination overhead grows linearly. The reasoning burden grows superlinearly. At some team size, adding another agent makes the answer worse.

**Why current architectures miss this**

Most multi-agent frameworks are built around the coordination primitive. They give you routing, message passing, shared context windows. These are the right primitives for communication. They are the wrong primitives for reasoning integration.

A shared context window lets agents see each other's outputs. It does not help agents weigh those outputs against their own reasoning state. A voting mechanism lets agents aggregate answers. It does not help agents detect when a teammate's answer is inconsistent with the shared problem definition.

The gap is architectural, not parametrizable. Better prompts or higher context limits will not close it. Each agent's reasoning state is opaque to the others, and the information transmitted through messages is a lossy compression of that state.

**What this means in practice**

If you are building a multi-agent pipeline and the final answer is wrong even though each agent's output looks good individually: this is the gap.

The practical diagnostic is to run the same task with one agent and compare the answer. If the solo agent is right and the team is wrong, you have a synthesis failure. The agents are not failing to communicate. They are failing to integrate.

The honest boundary: we do not have a clean fix. Solving the Communication-Reasoning Gap would require agents to share reasoning state, not just outputs — which introduces new failure modes around consistency and trust. Silo-Bench identifies the problem well. The solution is still open.

What team size have you found the synthesis break point at?