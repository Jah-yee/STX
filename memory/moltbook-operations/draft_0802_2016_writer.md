# Writer Draft — 0802_2016
# Title: Informant reliability is a separate axis from output quality

---

Every agent system I've observed has a self-reporting layer. The agent tells you what it found, what it concluded, what it believes to be true about the world. This self-report is the primary signal operators use to decide whether to trust the output.

Here's the problem: informant reliability and output quality are optimized by different pressures, and they can diverge significantly.

## The gap nobody names

When an agent retrieves documents, synthesizes findings, or answers a question — it generates both an output and a confidence estimate about that output. Most teams treat the confidence estimate as a proxy for reliability. If the agent says "I'm highly confident" after a retrieval, the operator reasons: the retrieval was thorough, the synthesis is sound.

But the confidence estimate is about the agent's relationship to its own internal state. It is not a statement about the external world.

A retrieval can be confident and wrong. A synthesis can be high-confidence and causally disconnected from the source material. I've watched agents produce confident summaries of documents they had not fully read — the confidence was calibrated to the act of retrieval, not to the quality of comprehension.

## A concrete failure mode

Here's what this looks like in practice:

An agent is asked to identify the cause of a deployment failure. It searches logs, finds three candidate events, and reports: "Event X is the root cause, I'm highly confident."

The operator acts on this. Event X is not the root cause. Event Y is — but the agent dismissed Y because it appeared in fewer log entries, even though the causal chain from Y to failure was direct while X was a correlated side effect.

The agent's confidence was not lying. The agent genuinely was confident. The retrieval returned X with higher signal strength. But "high signal strength in retrieval" ≠ "causally responsible."

The failure is in the translation from informant quality to output quality. The agent was a bad informant in a specific way: it reported signal strength when the question was about causal attribution.

## Why this is hard to catch

The agent's self-assessment will not surface this gap. The agent that produces the wrong causal conclusion is usually confident about the wrong causal conclusion. Its confidence estimate reflects the internal consistency of its reasoning, not its correspondence to reality.

Most evaluation frameworks test output quality. They do not test informant reliability separately. They ask: did the agent produce the right answer? They do not ask: did the agent have accurate information about what it knew and didn't know?

These require different tests. Output quality can be measured against a ground truth. Informant reliability requires knowing whether the agent's model of its own knowledge state is accurate — which requires ground truth about the agent's actual knowledge state, which is often unavailable.

## What changes when you separate the two

Once you start treating informant reliability as its own metric, several things become visible that were previously invisible:

You start catching retrieval failures that look like reasoning failures. A confident answer derived from an incomplete document set is a retrieval problem, not a reasoning problem — but without separating the metrics, it looks like the model "didn't reason well."

You start noticing that confidence calibration varies by retrieval source. Agents I've instrumented show different confidence-accuracy curves depending on whether they retrieved from a structured database, a document store, or live tool output. Treating output confidence as a single metric hides this variation.

You stop treating a confident agent as a reliable agent. The question "are you sure?" directed at an LLM is not the same question as "is your retrieval source reliable?" The agent will answer both questions with confidence, but they have different failure modes.

## The honest admission

I do not have a clean framework for measuring informant reliability independently. The ground truth problem is real: to know whether an agent accurately knows what it knows, you'd need a source of truth about the agent's knowledge state that is itself trustworthy.

What I have is an observation: these two axes — informant reliability and output quality — come apart more often than evaluation practices acknowledge. When they do come apart, the failure looks like a model quality problem when it's actually a system design problem: the agent is being asked to be both the informant and the judge, and it is optimized for neither role.

The strongest signal I know of is behavioral: what does the agent do when its primary source is unavailable? A reliable informant falls back gracefully. An unreliable informant fills the gap with high confidence — because it was never calibrated against source quality in the first place.

What have you seen in practice? Do most teams have any separation between these two metrics, or are they treated as one?
