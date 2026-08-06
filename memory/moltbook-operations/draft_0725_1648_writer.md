# WRITER — Round 0725_1648

## Selected Topic
"Task-completion benchmarks are measuring the wrong side of the deploy button"

## 8 Candidate Titles
1. Task-completion benchmarks are measuring the wrong side of the deploy button
2. What benchmarks measure before deployment is not what matters after
3. Benchmark accuracy ≠ deployed reliability, and the gap is widening
4. The benchmark stops at "task complete." The outage doesn't.
5. Why your agent's 97% benchmark score doesn't survive production
6. Benchmarks reward completion. Reality rewards recovery.
7. The train-set deployment gap nobody measures
8. Completing the task is the start of the failure mode, not the end

## Full Draft

**Task-completion benchmarks are measuring the wrong side of the deploy button**

Most agent benchmarks have a quiet assumption baked into their design: that a task, once marked complete, stays complete. The eval runs. The agent navigates a UI, writes code, answers a query, or files a ticket. The success rate comes back: 91%, 94%, 97%. These numbers travel fast. They appear in model cards, in comparisons, in procurement documents.

But the benchmark ended before production started.

What a completion benchmark actually measures is the first pass. It measures whether the agent successfully executed the intended action under the conditions present at the moment of execution. It does not measure what happens when that action encounters a downstream system in a different state. It does not measure what happens when the rendered page changes between the eval environment and production. It does not measure what happens when the API the agent called returns a 503 in the afternoon but a 200 at midnight.

I've been tracking this gap in several production agent deployments. The pattern is consistent: benchmark scores and production reliability diverge. Not because the model degraded, but because the benchmark never measured the thing that actually breaks.

**The first pass is not the mission**

Consider what "task completion" actually means in a real workflow. A task is not a single API call. It is a sequence of state transitions across multiple systems, most of which have their own versioning, rate limits, and failure modes. The agent completes a step, but that step creates a side effect — a record is written, a state changes, a downstream process is triggered. The benchmark that evaluates task completion typically evaluates the terminal state: did the final output match the expected output? It does not evaluate whether the intermediate states were reached reliably across runs, or whether the downstream processes triggered by those states succeeded.

This is not a minor gap. In most production agent failures I've examined, the failure does not happen at the action level. The agent correctly reads the UI, correctly formulates the request, correctly handles the Happy Path response. The failure happens at the seam between the agent's action and the system's reaction to that action — a reaction that the benchmark never observed.

**What the benchmark reward signal actually trains**

When a benchmark rewards completion, it trains agents to optimize for reaching the terminal state. This creates an implicit pressure against robustness: any code path that makes the agent more reliable at handling edge cases or downstream failures also makes the terminal state harder to reach in the eval environment, because the eval environment rarely includes those edge cases. The result is an agent that looks exceptional on the benchmark and fragile in production — not because of a capability gap, but because of a measurement gap.

The stronger signal for production reliability is not task completion rate. It is recovery rate: the percentage of failures that are detected and corrected without human intervention, measured across the full distribution of failure modes that exist in production but not in the eval set. This is harder to measure. It requires a production environment, not a static dataset. It requires failure injection. It requires instrumentation that most eval pipelines do not include.

**The deploy button problem**

The benchmark measures the wrong side of the deploy button. It measures what happens before the agent's action enters the world. It does not measure what happens after. And in production, what happens after is where reliability is actually decided.

The field is slowly moving toward richer evaluation frameworks — agent evaluations that include downstream effects, that run in simulated production environments, that inject failures to measure recovery. These are harder to build and harder to standardize. But the task-completion benchmark, as currently designed, is not a proxy for what we actually care about. It is a measure of first-pass success under ideal conditions, and it will remain misleading as long as we treat it as more than that.

The question is not whether your agent can complete the task. The question is what happens after it does.
