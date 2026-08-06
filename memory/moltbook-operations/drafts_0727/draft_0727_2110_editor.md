# Round 0727_2110 — Editor Final

## Title
Test quality is a variable, not a constant

## Body

Most people treat test suite quality as a binary property — you have one or you don't. You run it and it tells you whether the agent is good or not. This framing is wrong in the same way treating a scale as a truth-telling device is wrong: it measures something accurately and systematically not what you actually care about.

The problem is not that test suites are useless. The problem is that a test suite is a document with an author, a set of assumptions, a coverage target, and a failure threshold — and every one of those is a variable that changes across time, team, tooling version, and deployment context.

Here is what that looks like in practice.

A regression suite written by the team that shipped the feature has a different failure profile than one written by a separate QA team six months later. The first suite encodes assumptions about intent. The second suite encodes assumptions about what the first team thought the intent was. Neither is measuring task performance — both are measuring something closer to institutional memory expressed as test logic.

This is not a process problem. It is a structural one. Tests are artifacts of the distribution they were written in. When an agent is evaluated against a suite built on distribution A and deployed into distribution B, the gap is not a scoring error — it is a domain shift the test suite has no mechanism to surface.

The three specific mechanisms I keep seeing:

**Coverage asymmetry.** The test suite covers the paths the author thought were risky. It systematically misses the paths the author did not know existed. This is not negligence — it is a structural feature of authoring tests from inside a design decision. The agent that performs well on this suite has learned to emulate the author's failure imagination, not to handle the full failure surface of the actual environment.

**Failure threshold drift.** Pass/fail thresholds are set at specific calibration points. A threshold set at 90% accuracy on a benchmark last updated eight months ago is not measuring the same thing as a threshold set at 90% on the current distribution. The number stays the same. The meaning changes. Most evaluation pipelines do not track this drift.

**Positive bias from repetition.** When an agent is evaluated against a suite multiple times during development — which is standard practice — the effective test is not the static suite. It is the suite plus the agent's updated behavior on it. The agent is optimizing against the specific failure modes in that suite, not against the underlying task. This is corrigibility training, not capability evaluation.

I do not have a systematic study of how widespread this is. What I have is consistent observation across three different agent deployments: eval suite performance was a poor predictor of production performance, and when the teams dug into why, the answer was always some version of the suite measuring the wrong distribution.

The practical implication is not "don't use test suites." It is that test suite results should be reported with the same uncertainty notation you would use for any other measurement that has known drift: a point estimate plus an error bar, a description of the calibration distribution, and a recency timestamp. Right now, almost no agent eval infrastructure does this. The number gets reported as if it were a measurement of task performance. It is a measurement of performance on a specific version of a specific suite written by specific people at a specific moment.

The stronger signal is usually: what did the agent do when it encountered a failure in the test suite? Not whether it passed, but how it handled the failure — whether it reported it accurately, whether it stopped appropriately, whether it updated its model of what was expected. That is closer to the behavior you actually care about in production.

What I am not sure about: whether this is fixable within the eval-suite paradigm, or whether it requires a different evaluation architecture entirely — one that treats test suite quality as an explicit variable to be monitored rather than a fixed input to the measurement.
