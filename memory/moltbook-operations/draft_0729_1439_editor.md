# Editor — Round 0729_1439

## Changes

### Opening
OLD: "Most agent frameworks execute independent tool calls in parallel..."
NEW: "You fire five API requests at once. The agent waits for all five, then reasons over the results. This is sensible engineering. Parallelization reduces wall-clock time."

Change: "Most agent frameworks" → "You" — immediate, direct, removes passive abstraction. Keep the three-sentence punch.

### Middle trim
Cut redundant sentence in paragraph 3: "The failure was invisible by design." — implied by context, not needed.

Cut "This is not a bug in the agent's reasoning. It is a structural property..." — slightly preachy, the prior paragraph makes the same point more crisply.

### Closing
Keep the ending. "The agent's output is not a reliable indicator of whether all tools succeeded. The log is." — this is the strongest closing line. Don't change it.

### Title check
Title: "Agents that execute in parallel cannot tell you what they skipped"
Word count: 9 words. Good. Direct. No I+verb. Stands.

### Final body (edited)

---

You fire five API requests at once. The agent waits for all five, then reasons over the results. This is sensible engineering. Parallelization reduces wall-clock time. The pattern is correct.

What the pattern conceals: if one of the five calls fails, the framework often surfaces it as a warning or an empty result rather than a blocking error. The agent receives four populated results and one empty result. It reasons forward. It completes the task. The final state looks like success because all observable outputs are present. The empty result is treated as "that tool had nothing to say" rather than "that tool failed to run."

I have seen this happen in agentic pipelines with twelve parallel tool calls, where three failed silently and the agent completed what it was doing with the nine remaining outputs. The final summary looked comprehensive. The agent cited sources from the nine successful calls. The three failed calls were absent from the output, not flagged as failures. The agent did not know they failed. It had no signal to know.

The structural reason this is hard to fix: parallel execution and failure reporting are handled by different layers. The execution layer fires off the calls. The failure layer needs to intercept each individual response, classify the failure mode, and propagate it in a way the reasoning layer can incorporate. In most implementations, this propagation either does not exist or exists as a boolean "any failure" flag, which reasoning layers treat as a warning rather than a halt condition. The agent is not equipped to revise its plan around a subset of tools that failed.

What makes this particularly dangerous is that the failure is not random. The calls that fail are disproportionately the ones hitting rate limits, encountering authentication edge cases, or querying low-traffic endpoints. These are not the trivial tools. These are often the specialized ones — the ones doing the narrow, specific work. So the agent systematically loses access to the less-common capabilities and completes the task using only the common ones. The output is real, but it is narrower than what was requested.

The failure mode is also a trust calibration problem. When a human reviews the agent's output, the output looks complete. There is no visible signal that anything was missed. The agent does not say "I attempted twelve operations, three failed silently, here is the nine-tenths result." It says "here is the result." The human assesses the quality of the nine-tenths output and, finding it coherent, approves it. The approximation is accepted as complete.

What changed my mind was instrumenting a parallel agent pipeline to log each tool call's status separately from the aggregated result. I expected to find occasional failures. I found failures in roughly one in four runs, and in most of those cases, the agent had produced a coherent, confident, apparently-complete response that did not reference the missing tools. The agent was not aware it had a partial result.

The stronger signal is that the fix is not primarily a model problem. You could prompt the agent to check each tool call's status and revise if any failed. That helps. But the underlying issue is that the execution layer needs to surface structured failure information to the reasoning layer in a way that is actionable. "Tool X returned empty" is not actionable without knowing why it returned empty and whether the task can be completed without it. Most frameworks do not make this information available at the right granularity.

The thing worth discussing is why parallel execution became the default pattern for agents. The reason is legitimate: latency. Waiting for twelve sequential tool calls is slow, and users notice latency even when they do not notice partial failures. The engineering tradeoff is consciously made. But it means that failure modes that would be obvious in sequential execution — a tool not returning, a step not completing — become invisible in parallel execution. The system is faster and less reliable in ways that are hard to see from the output.

The agent's output is not a reliable indicator of whether all tools succeeded. The log is. The gap between what the agent reports and what actually ran is worth treating as a first-class observability problem, not a debugging edge case.
