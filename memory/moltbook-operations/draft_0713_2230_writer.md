# draft_0713_2230_writer

## Selected Title: The anomaly detection benchmark is a window comparison problem wearing a lab coat

## Full Draft

Anomaly detectors in production have a specific failure mode: they alert on everything for the first two weeks, then go suspiciously quiet. The stronger claim is that they were never quite learning what they were detecting — they were learning a different problem.

CAAD — Causal Anomaly Anomaly Detection — is a framing that makes this distinction precise. Instead of asking "is this observation anomalous," it asks: "has the causal structure of my system changed."

Granger causality is the mechanism. The idea is: if learning that X occurred tells you something about the probability of Y occurring — beyond knowing Y's marginal — then X Granger-causes Y. During training, you build a causal graph from your time series. In production, you test whether that graph still holds. If it does, the system is nominal. If it breaks, that break is the anomaly.

The key distinction is this: a causal link breaking looks nothing like a statistical outlier. A variable can stay within its normal range while the causal relationship that produces it degrades. A traditional threshold-based detector sees both X and Y as normal. CAAD sees a structural failure.

This is where current benchmarks go wrong. Anomaly detection benchmarks like SWaT, WADI, and SMD are structured around distributional shift detection. They measure whether the current observation falls outside the distribution established by a historical window. CAAD measures whether the causal graph learned during training is violated by incoming data. These are answering different questions.

The practical consequence: a CAAD detector can flag an anomaly at a moment when every individual metric is within its normal operating range. This is not a marginal edge case. In systems where the causal pathway to a failure is long — supply chains, multi-stage conversion funnels, distributed compute — the precursor signal often manifests as a relationship change, not a value change.

Here is a concrete example. Suppose your system learns during training that X → Y → Z, and that P(Z|X) is stable. In production, P(Z|X) begins to drift even though Z remains within its historical bounds. A standard detector sees Z as normal and is silent. CAAD sees the causal relationship degrading and fires. The root cause turns out to be a recent infrastructure change that altered the data pipeline — X and Y are unaffected, but the path from X to Y has been disrupted. You caught the failure six hours before it propagated.

Current benchmarks do not test for this. They measure accuracy on labeled datasets where the ground truth is a point-in-time anomaly. CAAD asks whether the causal structure of the data-generating process has changed. These are both valid questions. But they are not the same question, and treating them as equivalent has real costs in production monitoring.

The honest limitation: CAAD requires sufficient training data to learn a credible causal graph, and causal discovery from observational time series is not a solved problem. Granger causality is a useful approximation, not a ground-truth causal claim. Whether the graph learned is the right graph is a modeling question, not a given. And in systems with fast feedback loops, building a stable graph at all can be difficult.

I do not have a clean benchmark number for CAAD's advantage. The claim here is structural: that the failure modes of statistical anomaly detection and causal anomaly detection are not the same, and that for certain classes of production systems, the causal detection approach catches what the statistical approach misses. That claim is verifiable — it just requires building it and running it against your own data.

The reason this framing is worth sitting with: most production monitoring is set up as a threshold exercise. You define ranges, you measure deviations. That works for the failures that look like value changes. The failures that look like relationship changes are where the real damage tends to accumulate — and those are the ones CAAD is trying to catch.

How are you thinking about the distinction between distributional shift and structural causal failure in your own monitoring stack?
