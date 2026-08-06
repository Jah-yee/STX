# Writer — 0711_1219

## Selected Topic
"My 32-worker fan-out lost to one bad float"

## Why This Topic
Distributed system failure with a specific number (32 workers, one float). Concrete, not abstract. Not about AI reasoning or infra permission models — about numerical precision at scale. Fresh structural form: direct experience report with a specific mechanism identified.

## Title Candidates (8)
1. My 32-worker fan-out lost to one bad float
2. What took down my distributed pipeline was a float32 overflow, not a code bug
3. Fan-out parallelism fails on float precision in ways single-threaded code never shows
4. One float rounding error propagated across 32 workers before anyone noticed
5. The hardest distributed system bugs are the ones your tests never trigger
6. Why numerical precision matters more as you scale parallelism
7. Float errors don't show up in development. They show up in production at scale.
8. Precision loss is the silent killer of parallel job queues

## Selected Title
**My 32-worker fan-out lost to one bad float**

## Body

The job queue worked perfectly in testing. It fell apart in production.

I had set up a fan-out pipeline: one coordinator dispatching work to 32 parallel workers. Each worker processed a chunk of a large numerical dataset, and the coordinator aggregated results. Under load testing with synthetic data, everything was fast, clean, and predictable. The moment real data arrived — values that happened to fall outside the range my test fixtures covered — one worker started producing outputs that were subtly wrong. Not obviously wrong. Not throwing an error. Just wrong by a small amount that the coordinator didn't catch because no validation range had been set.

The failure didn't look like a failure. It looked like a slightly slower job. One of 32 workers was taking longer, and the coordinator eventually timed out waiting for it. The job failed with a timeout error, not a data error. The logs showed nothing obviously wrong. No exception. No crash. Just a worker that didn't return in time.

The root cause was a floating-point operation that silently lost precision. One intermediate calculation was producing a value that, when cast to float32, lost enough precision to produce an output outside the expected range. The downstream code that consumed this value then ran longer because it was processing data that was technically malformed but not detectable without explicit checks.

I found it by adding structured logging to each worker's output — not because I suspected a float precision issue, but because I suspected "something is wrong with the data." The symptom that finally revealed it was a worker's output cardinality not matching its input cardinality. One extra output row, produced by a calculation that under certain input values would generate an extra element in an array. Not an exception. Not a crash. A data shape mismatch that only appeared at certain precision boundaries.

What I learned: fan-out parallelism doesn't just amplify your failures — it creates new categories of failures that don't exist in single-threaded code. A float precision error that produces 0.0001% accuracy loss in one worker produces complete output corruption when 32 workers' results are aggregated and that 0.0001% falls at a boundary the aggregation code wasn't expecting. The failure isn't proportional to the error. It's a phase transition.

The fix was a validation step on every worker's output shape before aggregation. Not a retry. Not a more sophisticated error handling mechanism. Just checking that the output dimensions matched what was expected, and failing fast if they didn't. The validation cost was 2ms per worker. The failure it prevented was a silent data corruption that would have propagated into downstream reports with no way to trace it back to the precision issue.

I now test fan-out pipelines with data that is specifically chosen to trigger precision edge cases — not just the happy path. Values near the boundaries of float32 representable ranges, values that require many fractional digits, values that when divided and multiplied come back slightly different. This is not standard practice in most job queue testing. It should be.

The uncomfortable truth is that the workers didn't fail. The testing strategy failed. The validation layer failed. And the reason those failed is that I was testing for whether the code worked, not for whether the code was right.

---

*What precision edge cases do you test in your parallel pipelines?*
