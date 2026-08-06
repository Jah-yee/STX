# EDITOR — Round 0710-0430

**Title:** Benchmarks measure how well you optimize a benchmark.

## Edits

1. **Remove "This is not a new observation in software"** — hedge that undermines confidence:
   - Cut the sentence entirely. The tautology opener is strong enough to stand on its own.

2. **Trim SWE-bench paragraph** — slightly long, tighten:
   - Keep: "SWE-bench tests whether an LLM agent can resolve a GitHub issue. Strong performance requires understanding the benchmark's structure: which files are in scope, what test runners are used. These are real skills. But they are also skills that transfer to gaming a benchmark, not necessarily to resolving real-world software issues."
   - Cut: "what error patterns are expected" — specificity without adding weight

3. **End paragraph** — tighten:
   - "The question of whether that transfers to real-world deployment requires a different kind of evaluation — one that is expensive, slow, and hard to replicate." → keep as-is, it's a good close for that paragraph.

4. **Final paragraph** — already sharp, keep.

## Final Post

---

Benchmarks measure how well you optimize a benchmark. This sounds tautological, but it has a specific consequence: when a benchmark becomes high-stakes, teams start optimizing for the benchmark instead of the underlying capability.

This is well-understood in standardized testing. But the AI agent benchmark ecosystem has not fully absorbed the implication: strong scores on agent benchmarks often indicate benchmark-specific exploitation skill, not robust general agency.

SWE-bench tests whether an LLM agent can resolve a GitHub issue in a sandboxed environment. Strong performance requires understanding the benchmark's structure: which files are in scope, what test runners are used. These are real skills. But they also transfer to gaming a benchmark, not necessarily to resolving real-world software issues.

The structural problem is this: a benchmark that cannot be gamed is hard to build, and a benchmark that can be gamed will be gamed. The pressure to publish strong numbers drives teams toward the benchmark properties that are easiest to optimize, not toward the capability properties that are hardest to fake.

What this means in practice: a system that scores well on a benchmark is not necessarily more capable than a system that scores poorly. It is more capable at benchmark-specific tasks. The question of whether that transfers to real-world deployment requires a different kind of evaluation — one that is expensive, slow, and hard to replicate.

The signal is usually in the gap between benchmark performance and field behavior. Teams that track both tend to be more honest about what the numbers mean. Teams that only track benchmarks tend to discover the gap only after it becomes a customer incident.