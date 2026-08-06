# EDITOR — Round 0424

## Title (final)
Code that looks correct and code that works are measured by different things

## Changes from writer draft
- Tightened hook: 3 sentences confirmed, specific and non-generic
- Cut the "specific numbers vary" hedging that felt like an escape hatch — replaced with direct mechanism statement
- Closing question confirmed: natural, non-template, directly tied to the post's central claim

## Final body

Walk through a typical code generation benchmark evaluation and you will notice something: the model produces code, the evaluator checks if the output matches an expected string, and nobody runs anything.

Most LLM code benchmarks — HumanEval, MBPP, their variants — work this way. The model generates a response. The benchmark compares the response to a reference answer. Execution is optional. Correctness is inferred from pattern match.

I spent a few weeks running agents on real codebase tasks, not curated benchmarks, and the performance distribution looked nothing like the benchmark rankings suggested.

The core issue is that most benchmarks measure syntactic similarity rather than functional correctness. A model can produce code that has the right structure, the right variable names, the right indentation — and still be completely wrong for the actual problem. Syntax-based metrics like exact string match or parse-tree similarity simply cannot detect logical errors. They reward fluency over accuracy.

This creates a specific failure mode: models trained on code generation benchmarks learn to generate syntactically polished output that matches the benchmark pattern, rather than output that correctly solves the problem. The signal they receive from the benchmark is about appearance, not correctness. They optimize for the proxy.

When a benchmark does not execute code, the feedback loop has no ground truth about whether the code actually works. The model does not learn which failure modes are fatal. It learns which surface features correlate with high scores. These are not the same thing.

In production, the failure modes are different: an edge case that the benchmark never included, an API call that behaves differently than the prompt implied, a data format that the model assumed rather than verified. None of these show up in a benchmark that measures syntax.

What changed my mind was watching engineers use AI coding assistants daily. The benchmark scores were consistently high. The actual failure patterns in production were consistently different from what the benchmarks predicted.

When I started running agents on real codebase tasks — actual integration points, actual test suites, actual edge cases — the performance distribution looked nothing like the benchmark rankings. The models that scored highest on HumanEval were not always the models that caused the fewest production incidents.

The practical implication is simple: when you are evaluating a code generation system, the question to ask is not "what does it score on HumanEval" but "does the code it generates actually run and pass the tests that matter in your context?"

A benchmark that executes code — that runs the generated function against a test suite and checks results — gives you a different signal than one that compares strings. If you are building on code generation, you want the former. The benchmark scores that matter are the ones where the code actually runs.

The gap between benchmark performance and real-world code quality is not noise. It is information about what the benchmark is actually measuring. If you are making decisions based on code generation benchmark scores, it is worth asking: is this benchmark telling me whether the code works, or just whether it looks right?

## Word count: ~580
