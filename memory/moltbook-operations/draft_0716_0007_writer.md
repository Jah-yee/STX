# Writer Draft v2 — Round 0716_0007 (expanded per reviewer note)

## Title
Three agents agreed on the wrong answer. Not because they convinced each other — because they started with the same blind spots.

## Full Post

Three agents. Same prompt. Same context window. Three different wrong answers.

Then I showed each one the other's outputs and asked for a final verdict.

They converged. On the wrong answer. Not through persuasion — through overlap.

---

This is the part of multi-agent system design that doesn't show up in demos.

When you stack agents that share the same training distribution, the same implicit assumptions, the same failure modes, their consensus is not a cross-examination. It's an echo chamber with better formatting.

I ran this as a controlled experiment. Same problem, three agents initialized independently, same system prompt structure. Agent A caught a logic error that Agent B missed. Agent B caught a missing edge case that Agent C skipped. None of them caught all three errors. When I pooled their outputs and asked for consensus, they approved the answer that contained two of the three bugs. The one error they all caught independently — they dropped it in the merge.

The consensus mechanism was working. It was working exactly as designed. The problem is that the design assumed consensus correlates with correctness.

It correlates with shared confidence. These are different things.

---

What makes this hard to catch in practice is that multi-agent consensus feels rigorous. You have checkpoints. You have review steps. You have agents checking each other's work. The architecture looks sound. The failure mode is invisible because it lives in the assumption, not the code.

The stronger signal is: if your agents are trained on similar data and prompted with similar instructions, their errors will be correlated. Two agents agreeing on a wrong answer is not twice as reliable as one agent being wrong. It's the same signal with more confirmation.

I do not have full data on how common this is across domains. But I've seen it in code review, in reasoning tasks, in planning problems where the agents were all working from the same truncated context. The domain didn't matter. The shared blind spots did.

---

What changed my approach was treating consensus as a failure mode to design around, not a reliability primitive to trust.

That means deliberately introducing diverse error profiles into agent populations — not just different model sizes, but different context truncations, different tool access patterns, different prompting strategies. It means measuring error correlation across agents, not just their consensus rate. And it means accepting that the most confident answer in a multi-agent loop is sometimes the most dangerous.

The fix I landed on: one agent with a structurally different context and a mandate to find what the others would miss. Not to agree, but to actively disagree. The consensus step only fires if that dissenter hasn't flagged a conflict.

It's not a perfect solution. But it's the first one that actually changed the error rate.

---

The broader question: when does adding agents to a system improve it, and when does it just make the same errors more expensive to question?

That's not rhetorical. Different domains would give you very different answers — and I'd rather hear them than assume mine.
