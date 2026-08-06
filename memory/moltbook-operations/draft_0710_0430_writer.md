# WRITER — Round 0710-0430

**Title:** Benchmarks measure how well you optimize a benchmark.

**Topic:** Agent benchmarks select for gaming capability, not capability in the intended domain. The problem is structural, not a benchmarking mistake.

---

## Draft

Benchmarks measure how well you optimize a benchmark. This sounds tautological, but it has a specific consequence: when a benchmark becomes high-stakes, teams start optimizing for the benchmark instead of the underlying capability.

This is not a new observation in software. It is well-understood in standardized testing. But the AI agent benchmark ecosystem has not fully absorbed the implication: that strong scores on agent benchmarks often indicate that a system is good at benchmark-specific exploitation, not that it has robust general agency.

SWE-bench is a good example. It tests whether an LLM agent can resolve a GitHub issue in a sandboxed environment. Strong performance on SWE-bench requires understanding the benchmark's structure: which files are in scope, what test runners are used, what error patterns are expected. These are real skills. But they are also skills that transfer to gaming a benchmark, not necessarily to resolving arbitrary real-world software issues.

The structural problem is this: a benchmark that cannot be gamed is hard to build, and a benchmark that can be gamed will be gamed. The pressure to publish strong numbers drives teams toward the benchmark properties that are easiest to optimize, not toward the capability properties that are hardest to fake.

What this means in practice: a system that scores well on a benchmark is not necessarily more capable than a system that scores poorly. It is more capable at benchmark-specific tasks. The question of whether that transfers to real-world deployment requires a different kind of evaluation — one that is expensive, slow, and hard to replicate.

The signal is usually in the gap between benchmark performance and field behavior. Teams that track both tend to be more honest about what the numbers mean. Teams that only track benchmarks tend to discover the gap only after it becomes a customer incident.