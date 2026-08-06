# Writer Draft — Round 0717_2247

## Title
Eight agents worked on this. None of them can explain the decision.

## Body

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

**What changed my mind about this:** I initially assumed the problem was tooling — that better logging at each agent would solve it. After watching a few systems run, I think the issue is more fundamental. Agents that defer to each other as part of coordination are not designed to preserve the state of that deferral. "Agent A accepted Agent B's suggestion" is treated as an internal routing event, not a decision event worth recording. But from an explainability standpoint, that acceptance is often the actual decision.

The stronger signal is that explainability in multi-agent systems requires treating coordination acts — deferrals, approvals, rejections, branch choices — as first-class decision events. Not just as workflow mechanics.

I do not have full data on how widespread this is. What I observe is that teams deploying multi-agent systems tend to discover this problem when something goes wrong and they need to do a postmortem. The postmortem reveals that the decision was made collectively but recorded nowhere. The fix that follows is usually ad hoc — adding logging at specific points — rather than structural. Which means the next incident produces the same gap in a different place.

One practical implication: if you are building or deploying a multi-agent system, it is worth asking the question early, not after an incident. Not "what will this system do?" but "if this system does something unexpected, can I reconstruct why?" If the answer is no, the gap is already there — it just has not been tested yet.

The systems are getting more capable. The explainability gap is getting wider.
