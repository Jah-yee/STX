# draft_0604_0118_writer.md

## Title: "The null that looks like success is the most expensive bug in AI systems."

---

A PDF parser returned null last Tuesday. Not an error — null. The API logged a 200, the pipeline logged success, the batch moved on, and 14 downstream records silently got nothing. The run passed every checkpoint.

This is not a rare edge case. It is the most common way automated pipelines break in production, and it breaks quietly because the design of the system makes silence indistinguishable from success.

**The structural problem is the success/failure signal is not tied to output validity.**

When an API returns HTTP 200 with an empty body, it has communicated that the transport succeeded. It has said nothing about whether the operation produced what it was supposed to produce. Most AI pipelines treat this as clean — because the infrastructure layer does. The failure gets attributed upward, to whatever consumed the null and silently processed it as a no-op.

The interesting thing about null-as-success is that it is not a single-point failure. It is a failure of inference all the way down. The parser did not error; it returned null, which means it believed null was the correct answer. The pipeline did not error; it received null, which means it believed null was acceptable output. The consumer did not error; it received null, which it treated as "nothing to do," a condition it handles gracefully. Three systems in a row made the correct local decision and produced a globally wrong result.

What changes the picture is when you add time pressure. In a batch pipeline that processes thousands of documents per night, a null on one record is not an event — it is noise. The operator does not see it because there is no alert. The consumer does not flag it because a null is a valid input in most data models. The failure compounds because the detection window is narrow: by the time a human notices the downstream artifact is wrong, the original null is long gone from any live session, and reproducing the exact condition requires running the original document through the same parser version under the same load. The cost of reproducing the bug exceeds the cost of manually fixing the affected records, so the fix never gets automated.

I have noticed this pattern clustering around three specific conditions. First, when the AI system is making a "best effort" call and the API surface is optimized for success rate rather than output completeness — image generation APIs that return 200 with an empty image buffer when a concept is unrepresentable are the canonical example. Second, when the output schema allows null as a valid field value but the consumer does not distinguish between "null because the field is inapplicable" and "null because the extraction failed silently." Third, when the evaluation harness itself errors silently and reports a pass because the test framework caught the error and marked the test as skipped, not failed.

The strongest signal I have found for catching null-as-success before it causes downstream damage is not adding more error handling — it is making output validity a first-class return value. If the API surface includes a confidence or completeness indicator that is distinct from the HTTP status, and the pipeline checks that indicator as a hard requirement, null can no longer wear the costume of success. The indicator does not need to be accurate in the sense of always reflecting true quality. It needs to be calibrated such that null always produces a low completeness score, regardless of whether the extraction is actually decent.

What the null-as-success failure actually costs is not measured in the incident report. It is measured in the artifacts that silently entered production and were used for decisions before anyone noticed they contained nothing. That number is not in any postmortem I have read. I do not have full data. But I have seen it in enough different pipelines to believe it is the most common form of silent AI failure that nobody is building detection for.

The batch that returned all nulls but passed — that is the incident that should be on the board. Not the one where something loud broke.