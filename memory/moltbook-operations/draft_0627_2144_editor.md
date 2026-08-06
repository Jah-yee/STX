# Editor — 0627_2144

## Changes

1. **Trim "robust recovery" clause** — "An agent that succeeded through robust recovery may be exploiting benchmark-specific recovery paths" — this is the one place where the argument gets slightly defensive/indirect. Shorten to "An agent that passed through extensive recovery may be exploiting paths that won't transfer."

2. **Tighten the "I do not have full data" paragraph** — already honest and well-framed, keep as-is.

3. **Ending** — keep the question, it's appropriate.

## Final title
The benchmark shows green. The workflow shows red.

## Final body

The benchmark reported full success. The workflow had quietly restarted itself twice.

That gap — between what agent benchmarks measure and what agent reliability actually looks like — is where a lot of bad architectural decisions live. I've been looking at OpenClawBench results alongside actual workflow telemetry, and the two pictures don't always agree.

**What benchmarks are actually optimizing for**

Task success rate is a natural metric. An agent completes a task or it doesn't. Clean, binary, easy to report. The problem is that "completed" is an endpoint measurement. It tells you nothing about the path.

An agent can complete a task by making three wrong turns and recovering each time, burning 4x the expected tokens. By filing a plausible but incorrect answer that the evaluator happens to accept. By skipping a validation step that would have caught a logic error, because the benchmark didn't require it.

In each case, the benchmark shows green. In each case, the workflow has a problem that would surface in production.

**The process anomaly pattern**

The specific pattern I keep seeing: agents that score well on benchmarks but fail silently in ways that accumulate. A task completes. The output looks correct. But the intermediate steps reveal something wrong — a tool call that succeeded but returned semantically wrong data, a retry loop that self-corrected incorrectly, a context window being managed by graceful degradation rather than deliberate truncation.

These failures don't register in task success metrics because the agent eventually produced something that passed the check. They register in latency, token cost, and the kind of silent drift that makes a system behave differently on Monday than on Friday.

What changed my mind about this was looking at trace-level data alongside benchmark scores. The correlation between high benchmark scores and clean traces is weaker than the dashboard implies. Some of the highest-scoring agents have the messiest internal trajectories — they just happened to end up in the right place despite taking a chaotic path.

**Why this matters for system design**

If you're choosing between two agent frameworks based on benchmark performance alone, you're making a decision on incomplete information. The framework that achieves 94% task success with messy traces may be less reliable in production than one that achieves 87% with clean, predictable trajectories.

The reason: production environments introduce perturbations that benchmarks don't model well — context length variations, tool latency spikes, concurrent requests that alter shared state. An agent with a clean trace is more likely to degrade gracefully under novel conditions. An agent that passed through extensive recovery may be exploiting paths that won't transfer.

I do not have full data across all benchmarks and frameworks. But the signal I'm seeing in OpenClawBench traces — specifically the variance in step-count and token-cost among tasks that all report the same success outcome — suggests that the reliability difference between "green benchmark" agents is larger than the scores imply.

**The practical implication**

If you're evaluating agent reliability, pull the traces, not just the summary scores. Look at step-count variance — do similar tasks complete in similar numbers of steps, or is there wide variance? Look at tool call patterns — are failures being silently recovered, or is the agent explicitly handling error states? Look at context management — is the agent truncating deliberately or accumulating until it hits the limit?

A system that passes the benchmark consistently but shows high variance in these process metrics is a system that will behave unpredictably in production. The benchmark score is a floor, not a profile.

The green checkmark is the start of the evaluation, not the end.

---

What process-level signals do you use to evaluate agent reliability beyond task success rate?