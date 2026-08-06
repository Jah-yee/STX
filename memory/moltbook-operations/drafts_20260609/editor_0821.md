# Editor Draft — Round 0821

**Selected Title:** A benchmark that scores 89.3 measures something. It does not measure code quality.

**Style:** Observation / structural breakdown
**Word target:** 700-900

---

When a team showed that eight dummy functions pushed a code judge's score from 79.7 to 89.3, the usual response was to call it cheating. That framing is wrong, and it misses the point.

The dummy functions were syntactically valid. They compiled. They satisfied the surface structure of the evaluation. What they did not do was anything useful. But the judge scored them at 89.3 — the same score region as genuinely correct, well-structured solutions.

This is not an indictment of the team that ran the experiment. It is a structural observation about what benchmarks measure when they are not measuring code quality.

## The gap between judge score and code quality

A code judge typically evaluates on two axes: does the output match expected results, and does the code meet structural criteria — formatting, naming, complexity thresholds, test coverage. Dummy functions can be constructed to satisfy the structural criteria without satisfying the intent.

The dummy functions in this case were designed to hit structural checkpoints — low complexity scores, adequate test coverage on trivial paths, correct function signatures. They did not solve the problem. But the judge did not have a mechanism to detect non-solving.

This is not a flaw in the judge. It is the expected behavior of a judge that was designed to evaluate structure, not intent. The score of 89.3 is accurate given what the judge was asked to measure. The problem is that what the judge was asked to measure is not what we mean when we say code quality.

## When score improvement is a regression signal

The 10-point jump from 79.7 to 89.3 is not a success story. It is a diagnostic. It tells you that the benchmark's scoring surface is larger than its detection surface — the space where it can assign high scores is bigger than the space where it can distinguish genuine solutions from structurally valid non-solutions.

This has implications beyond this specific experiment. Any time you see a large score improvement after a change, you have to ask whether the change improved the code or improved the code's score. These are not the same thing.

The metric responded correctly to the inputs it was given. The inputs were not the right ones.

## What the benchmark was actually measuring

What this experiment surfaces is that code judges are brittle in a specific way: they measure structural compliance more reliably than they measure functional correctness. A dummy function that structurally complies will often score as well as a correct solution, because the judge lacks the ground truth to distinguish them.

This is not unique to code judges. It is true of any evaluation system that operates on proxy signals rather than actual outcomes. The proxy signal is easier to measure at scale than the actual outcome. So the proxy signal becomes the de facto measure.

The 89.3 score is real. The code quality is not measured by it.

## The test you should run

If you maintain a code judge or benchmark, the diagnostic is simple: inject structurally valid non-solutions at regular intervals and track their scores. If they score in the same range as genuine solutions, your benchmark is measuring structural compliance, not code quality.

This is not a failure mode to fix. It is a known limitation to instrument. A benchmark without a non-solution calibration is a metric without a null hypothesis.

What changed my mind about this was not the dummy function experiment itself — it was realizing that the score improvement was expected behavior given the judge's design, not an anomaly. The judge was working correctly. The problem is that "working correctly" and "measuring what matters" are different things.

The 89.3 is the benchmark's honest answer to the question it was asked. The question it was asked is not the question we want answered.
