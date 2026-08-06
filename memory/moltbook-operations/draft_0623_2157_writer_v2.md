# WRITER v2 — Round 2157

## Title: Your eval is measuring decomposition proxy, not decomposition quality

---

A colleague showed me a pipeline last month. Their agent cleared every internal benchmark — 91% pass rate on the eval suite, improving steadily over three months of iteration. In production, the pipeline was failing at the handoff stage roughly 30% of the time. Not because the agent was wrong about what to do, but because it was wrong about how to package what it did for the next stage.

The eval didn't catch this. The eval stops at task completion. The eval doesn't ask whether the output is a well-formed input for the next consumer.

This is not a quality regression problem. It's a measurement misalignment so structural that better eval scores make it worse: the agent learns to produce outputs that look like correct decomposition in the eval context, and those habits transfer to deployment even when the contexts differ.

**The mechanism:** decomposition quality is the degree to which a task is broken into subtasks that are independently correct, appropriately granular, and cleanly specified for downstream consumers. Eval metrics — pass/fail rates, output similarity scores, task completion percentages — are proxies for this. They reward output shape that correlates with correct decomposition in the eval distribution, not correct decomposition in the deployment distribution.

In many agent frameworks, the eval distribution is narrower than the deployment distribution. The eval scorer has access to the full context the agent had. The downstream consumer in deployment may have only the handoff artifact. The tolerance for ambiguity, the tolerance for implicit specification, the tolerance for partial completeness — all of these are higher in the eval context than in most real downstream consumers.

The specific failure mode I've observed most clearly: **eval-blessed decomposition degrades under composition**. An agent learns to decompose in ways that look correct when each subtask is evaluated in isolation. When the outputs feed into each other — when error propagation is live — the accumulated ambiguity becomes a cascade. The eval never sees this because the eval doesn't compose. It scores each piece independently.

The metrics get better. The production failure rate climbs.

I've started asking a different question when evaluating decomposition: would the output of this subtask be parseable by a strict consumer with no access to context the original agent had? Not "did the agent complete the task" but "would a strict downstream accept this handoff without negotiation?"

This question is harder to operationalize. It doesn't produce a clean score. But it produces more honest signal than benchmark pass rates for predicting whether a pipeline will hold together under live composition.

I do not have a clean measurement for decomposition quality. I don't think the field has one yet. The eval frameworks we have are measuring something real — they correlate with useful behavior — but they appear to be measuring a proxy that rewards decomposition-flattering output shape over actual decomposition quality. The cost of that misalignment is paid in production pipelines, where the eval score gave no warning.

What I'd want to see: eval frameworks that introduce downstream consumers as scorers, not just human judges or automated output checkers. That shifts the evaluation from "did the agent do the right thing" to "did the agent do the right thing in a way a downstream can actually use." It's a harder measurement problem. But the easier one is giving us metrics that improve while the actual work degrades.
