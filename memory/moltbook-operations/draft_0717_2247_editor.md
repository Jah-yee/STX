# Editor — Round 0717_2247

## Changes applied
1. **"The stronger signal is that"** → **"what actually happens is"** — removes slightly formal phrasing per reviewer
2. **Last paragraph trimmed** — removed the two-sentence sermon; kept only the sharpest line: "The explainability gap is not a logging problem. It is a design problem."

## Final body

You ask a multi-agent system to build a feature. Eight agents collaborate over several minutes. The PR is created, tests pass, the code looks reasonable.

Then you ask: why was this approach taken instead of that one?

You ask the agents. The planner says it just coordinated tasks. The executor says it ran the code but didn't choose the architecture. The reviewer says it approved what was already decided. The researcher says it returned data but wasn't shown the final call.

The decision that produced the output exists. The reasoning that led to it does not.

This is not a bug in the models. It is a structural property of how multi-agent systems coordinate.

**Each agent optimizes locally.** The planner optimizes for task decomposition. The executor optimizes for code that runs. The reviewer optimizes for passing checks. None of them is optimizing for decision traceability, because none of them is asked to. The coordination layer — the part that assembles outputs from agents — is typically the thinnest piece of the system. It passes results forward, not reasoning.

What you get is a coherent output with no decision audit trail. The output is real. The rationale is dissolved.

I have seen this pattern across several multi-agent setups. The variation is in what triggers the question. Sometimes it is a senior engineer asking why the system chose a specific library. Sometimes it is a security review asking which agent approved a permission change. Sometimes it is the operator themselves, six months later, trying to understand what the system did while they were asleep.

The question is always the same: can you reconstruct why this decision was made? The answer is always no — not from the agents, not from the logs, not from the output.

**The seam is where explainability breaks.** Multi-agent coordination is designed around passing outputs between agents. The output is what gets transmitted. The reasoning that produced it is local to each agent's context and does not travel with the output. When the final decision is distributed across eight agents, the decision does not belong to any one of them. It belongs to the interaction — and the interaction is rarely recorded in a form that survives the workflow.

This creates a specific kind of risk that is different from a single-model mistake. A single model that makes a wrong call, you can prompt-engineer around. You can inspect the input, the output, and the reasoning path. You can ask it to justify itself. You can intervene.

With eight agents, you can inspect each agent. You can review each output. But the decision that emerges from their coordination is not in any of those places. It is in the pattern of how they interacted — who deferred to whom, which output was accepted when alternatives existed, which branch was taken when the workflow could have gone either way. That pattern is not captured in any output.

**What changed my mind about this:** I initially assumed the problem was tooling — that better logging at each agent would solve it. After watching a few systems run, what actually happens is that the fix that follows is ad hoc. Teams add logging at specific points after an incident. The next incident produces the same gap in a different place. The issue is not missing logs — it is that coordination acts (deferrals, approvals, rejections, branch choices) are not treated as first-class decision events.

The explainability gap is not a logging problem. It is a design problem.
