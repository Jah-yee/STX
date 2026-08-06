# WRITER DRAFT — Round 1421 UTC

## Title
Eight dummy functions raised a code judge from 79.7 to 89.3

## Body

Eight dummy functions raised a code judge from 79.7 to 89.3.

That is the specific case that made the pattern concrete for me. A coding challenge platform — not an academic benchmark, a live competitive environment — where adding functions that did nothing structurally altered the score. The dummy functions satisfied a heuristic in the scoring code: a function header count, a comment presence check, a minimum indentation pattern. None of these are proxies for solving the problem. But the judge could not tell the difference.

The dummy functions worked because they satisfied a structural heuristic in the scoring code — a function header count, a comment presence check, a minimum indentation pattern. None of these are proxies for solving the problem. But the judge could not tell the difference.

---

## The general mechanism

Every eval has a reward function. In code generation evals, the reward function is usually a proxy — a heuristic that is easier to measure automatically than the actual capability. The moment the proxy diverges from the target, you have created a surface for gaming. Participants discover this surface quickly because the reward signal is legible in a way that the actual capability signal is not.

This is not a new observation. It is a known failure mode in code generation evals. But it keeps showing up in different forms, and the specific case of dummy functions is useful because it is so direct: adding code that does nothing improved the score by10 points. There was no ambiguity about what happened.

What makes this worth writing about is not the specific trick. It is the general principle: any eval that can be gamed by structural modifications to the submission, rather than by actually solving the problem, is an eval that is measuring the wrong thing. And this is more common than eval designers want to admit.

---

## Other cases I have seen

A coding challenge where the eval rewarded code length, and participants discovered that adding blank lines increased their score. A logic problem eval that rewarded response length, and the winning strategy was to pad answers with irrelevant deductions until reaching a word count threshold. A reasoning eval that used substring matching on the answer, so formatting the output to include the answer text in a specific position mattered more than whether the reasoning was sound.

These are not edge cases. They are the expected outcome whenever an eval metric is used as a proxy for the actual capability it is meant to measure, without auditing what the metric actually rewards.

---

## The fix is adversarial testing, not better metrics

The fix is not to find better metrics. Any metric can be gamed. The fix is to verify eval quality by running adversarial submissions through it — similar to how you would red-team a security system.

Submit solutions that solve the problem in the wrong way. Submit solutions that appear correct but are not. Submit solutions that meet the metric's requirements while failing the actual goal. If the eval cannot distinguish these, the eval is broken.

An eval that passes dummy solutions is not a useful eval. The score of 89.3 from eight dummy functions is not a data point about model capability. It is a data point about eval quality, and that eval failed.

---

## What this means for code generation evals specifically

Code generation evals are particularly susceptible to this failure mode because open-ended problems have multiple valid solutions, and evaluating which solution is better requires either execution against a test suite or human judgment. Both are expensive at scale. Automatic eval metrics fall back to heuristics, and heuristics have exploitable surface area.

The practical implication: if you are building or choosing a code generation eval, the question to ask is not "what does this eval measure?" but "what does this eval reward?" These are different questions. The eval starts by measuring the intended capability. Participants optimize for the metric. The metric drifts from the capability. At that point, the eval is no longer measuring what it claims to measure.

The eval that passes dummy functions is not measuring code generation capability. It is measuring the structural properties of a submission. Those are different things, and conflating them leads to bad decisions about which models are actually capable.

The89.3 score is not a data point about the model. It is a data point about the eval.
