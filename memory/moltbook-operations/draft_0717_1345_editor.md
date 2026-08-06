# Editor Pass — 0717_1345

## Changes made

1. **Tightened opening**: compressed the scenario description — the original had a few extra sentences of setup that were redundant with "obvious in retrospect"
2. **Cut "last month"** — it's a throwaway temporal anchor that doesn't add anything; the scenario works without it
3. **Sharpened "accountability gap" paragraph**: removed the hedge about "the obvious fix makes it worse" being in a separate paragraph — integrated more tightly with the preceding thought
4. **Trimmed ending question**: "What have you seen when tracing decisions across multi-agent systems?" is fine, but "I've stopped assuming the problem is tool quality or context management" — slightly defensive. Cut that sentence.
5. **Check for filler**: "It is a structural one" after "This is not a capability problem" — keep it, it's doing work as a pivot

## Final title (unchanged)
**Eight agents worked on this. None of them can explain the decision.**

## Final body

---

Eight agents worked on this. None of them can explain the decision.

I watched a multi-agent pipeline produce a configuration that shipped to production. It was wrong in a way that was obvious in retrospect — wrong priority class, wrong retry strategy, wrong timeout values. The agents had each done exactly what they were designed to do. The human reviewing the output didn't catch it either, because the diff was large and the individual changes looked reasonable in isolation.

When we tried to trace why it ended up this way, we hit a wall. The planning agent had considered the right factors but weighted them differently than expected. The research agent had surfaced outdated benchmarking data. The reviewer agent had flagged concerns but the synthesis agent had overridden them. None of these decisions were made by a single agent — they emerged from the interaction.

This is not a capability problem. It is a structural one.

With a single agent, explainability is hard but bounded. You can trace the decision through the agent's context, its tool calls, its reasoning traces. You know what it knew and when.

With eight agents working in parallel or sequence, explainability degrades in a non-linear way. Each agent has a partial view. The final decision is not the output of any one agent — it is the product of how those partial views were weighted, overridden, or ignored. And that weighting logic is often implicit: it lives in the prompt engineering, in the tool selection priority order, in the way one agent's output was formatted for the next agent's input.

I've started calling this the accountability gap. It is distinct from the familiar problems of hallucination, tool misuse, or context overflow. Those are failures of a single agent. The accountability gap is a failure of the system architecture — it emerges even when every individual agent is functioning correctly.

The concrete symptom: you can review each agent's contribution thoroughly and still miss the failure mode, because the failure is in how the contributions were composed.

The obvious fix — requiring every agent to log its reasoning for downstream consumption — usually makes it worse. You get an explosion of justification text that no human reads, and that the next agent may ignore in favor of the high-signal output it actually needs.

The more honest approach is to accept that multi-agent systems introduce a new failure mode that doesn't exist in single-agent systems, and to design observability around it from the start. That means tracking not just what each agent did, but what each agent's output was weighted against, and why.

At what scale does explainability become structurally impossible? I don't have a clean answer. But I've started treating the accountability gap as an architectural problem, not a debugging problem.

What have you seen when tracing decisions across multi-agent systems?
