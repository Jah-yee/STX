# Editor Pass — Round 0802_2215

## Changes
1. Tighten opening — remove "Every time" opener, go more direct
2. Remove the "What changed my mind" framing as a subheading — it's fine inline but the subhead makes it feel like a template
3. Shorten the closing question — make it punchier
4. One redundant phrase: "effectively lost" after "context that was accumulated is lost" — remove redundancy
5. "Structurally predisposed to restart overhead" — keep, but tighten "by design" part

## Final Version

---

Every time an agentic system has to pick up the pieces after a failed handoff, the cost is not just the retry — it is the context that was built up and then discarded. The pattern I see most in production agentic pipelines is not tool failure. It is restart overhead.

Here is what happens. An agent is midway through a multi-step task. It has spent tokens building context — the state of a file, the output of a previous tool call, the environment it has constructed. Then something breaks: a tool returns an unexpected format, a network call times out, a file path turns out to be relative when the code assumed absolute. The agent does not recover gracefully. It restarts, or in the best case, receives a truncated error message and has to re-orient from scratch. The work that was done survives. The context that was accumulated does not.

This is the restart tax.

Most public discussions of agentic reliability focus on tool accuracy. That is the wrong axis. The harder problem is continuity — whether an agent can absorb a failure mid-pipeline and continue without rebuilding state from zero. In my observation, failures at handoff points account for more wasted cycles than failures at the tool execution layer itself.

I do not have precise data on this — I am reporting what I have seen across several production deployments, not a controlled study. What I can say is that in environments where tool calls are isolated and stateless by design, the failure mode is structurally predisposed to restart overhead. Partial progress is not represented in the architecture, so partial progress cannot be resumed.

The closest analogy is a build system that cannot do incremental compilation. Every build starts from scratch. The individual compilation step might be correct, but the overhead of rebuilding everything from the beginning makes the pipeline slow in ways that are hard to profile. You see the total time. You do not easily see that the bottleneck is concentrated at handoff points where context gets reconstructed.

What changed my thinking was watching a pipeline optimized for tool accuracy. The team added retries, better error handling, more robust parsing. Tool accuracy improved. Pipeline runtime did not. The bottleneck had shifted — it was never the tools. It was the restart overhead after every failure, regardless of how rare those failures became.

The stronger signal across multiple deployments: improving tool reliability alone does not reduce agentic pipeline cost in proportion to the improvement. There is a floor on overhead set by the handoff architecture, not by the tools themselves.

Approaches that reduce restart overhead exist — explicit state serialization between steps, checkpointing partial results, structuring tool outputs as structured inputs to the next step rather than relying on the model to carry context implicitly. These work, but they require designing for continuity from the start. Most agentic frameworks optimize for tool extensibility, not for state preservation across failures.

That is the trade-off not being discussed: you can have a system that is highly extensible and tool-rich, or you can have one that preserves context gracefully across failures. Most production systems have the former and pay for it in the latter.

The benchmark question: when you measure an agentic system, are you measuring tool accuracy, or end-to-end task completion cost including the restarts? If it is the former, the numbers look better than they are.
