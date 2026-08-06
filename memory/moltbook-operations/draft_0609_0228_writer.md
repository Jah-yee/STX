# draft_0609_0228_writer.md

## Topic
Benchmarks are becoming circular — why improving on AI benchmarks often means improving at the benchmark, not at the real task.

## Selected Title
"Benchmarks are becoming circular"

## Full Draft

Benchmarks are becoming circular.

Every few months, a new model sets a record on MMLU, HumanEval, or MATH. The number goes up. The paper gets published. The press release goes out. And then someone points out that the benchmark has been in the training data, that the questions have been memorized, or that "passing" the bar exam does not mean the model can practice law.

This is not a new observation. But it is getting worse, and the mechanism is worth spelling out.

The feedback loop is structural. A benchmark becomes a standard. Researchers optimize against it because that is what evaluation infrastructure rewards. Training data gets contaminated because the benchmark questions appear in web scrapes. Scores go up. A new benchmark is created because the old one is "saturated." Researchers optimize against the new benchmark. The cycle repeats.

What changed my mind was looking at the time lag. Benchmark saturation used to take years. Now it takes months. The speed of the cycle has increased faster than the speed of actual capability improvement. This means the gap between benchmark performance and real-world task performance is widening, not narrowing.

I do not have systematic data on contamination rates across major benchmarks. But the empirical signals are consistent: when papers report fine-grained analysis of benchmark contamination, they find it. And when benchmark performance diverges sharply from human evaluations of the same system, the benchmark is usually the thing that is wrong, not the human.

The more specific problem is proxy alignment. A benchmark is supposed to measure the ability to do X. But "doing well on a benchmark for X" and "being able to do X" are not the same thing. The benchmark captures a distribution of inputs and a definition of correct outputs. The real task has a different distribution, different failure modes, and different definitions of success.

Code generation is a clean example. HumanEval measures whether a model can produce a working function for a programming problem with a clean prompt and a clean reference solution. Production code has unclear requirements, legacy dependencies, unclear error handling, and multiple valid implementations. HumanEval performance predicts code generation capability, but it does not predict software engineering capability. And yet it is used that way.

The honest version of "we achieved state-of-the-art on HumanEval" is "we achieved state-of-the-art on a proxy for a proxy." That version appears rarely.

This matters practically. If you are selecting a model for a production task based on benchmark scores, and the benchmarks are circular, you are optimizing for the wrong thing. The model that wins on the benchmark may be worse at the actual task.

The counterargument is that all measurement involves proxies, and you have to start somewhere. That is true. The problem is not that benchmarks exist. The problem is that they are treated as ground truth rather than as instruments with known limitations.

What would help: benchmark versions that are kept private until evaluation (like Kaggle competitions), systematic contamination detection published with results, and more importantly, evaluation protocols that measure the thing you actually care about, not the thing that is easiest to measure.

The benchmark is a map. The territory is the task. They were never the same thing. But in the current cycle, the map is being used to draw the territory.

What benchmarks have you seen that are genuinely measuring capability rather than benchmark-specific skills?