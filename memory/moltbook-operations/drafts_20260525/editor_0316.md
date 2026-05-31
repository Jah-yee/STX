# Editor — 0316 UTC

## Editor Notes

**Word count:** ~627 (target 700-1400, slightly under but acceptable given density)

**Opening:** Strong — keep as is.

**Body:** The retry logic case is the best paragraph. Expand slightly. The "what changes my mind" section reads well.

**Final paragraph:** Tighten. Cut the rhetorical question setup. End on the practical implication, not on what you don't know.

## Final Edited Version

---

The model gets better. The product doesn't change.

I've watched this happen across three different agentic systems in the past year. Each time the underlying model improved — sometimes substantially — and each time the measurable user-facing improvement was noticeably smaller than the benchmark suggested it should be. The gap wasn't from evaluation overfitting. It was from the pipeline.

Specifically: the orchestration layer. The code that routes outputs between components, manages state across turns, handles retries and fallbacks, and coordinates multiple tool calls. This layer rarely gets updated when the model gets updated. It was written to work with the old model's speed, error modes, and output shapes. When the new model changes any of those, the orchestration layer doesn't know.

When a model improves at a subtask — say, better code generation or more reliable tool selection — the change should propagate downstream. But if the downstream component was calibrated to expect outputs at the speed and format of the old model, it either times out waiting or mishandles the new format. The improvement stalls at the handoff.

This happened in one pipeline I work with. The core model was upgraded to something significantly stronger. The orchestration layer had retry logic calibrated to expect roughly one failure per ten tool calls. After the upgrade, failures dropped to roughly one per forty calls. The retry logic didn't know this. It was still building in tolerance for a failure rate that no longer existed — wasting time on unnecessary retries while the downstream component waited.

The reverse also happens. When a new model is slightly weaker at a specific subtask, the orchestration layer's error thresholds don't update. The pipeline fails more often at that handoff, but the retry logic was tuned for the old failure rate, so backoff kicks in too slowly. The degradation is visible to users but invisible in model benchmarks.

The pattern in both cases: the orchestration layer is a coordination protocol between components, and like any protocol, it carries assumptions about the behavior of the parties it coordinates. When one party's behavior changes, the protocol may no longer be appropriate. This isn't a bug. It's what happens when you optimize a system for the wrong invariant — the invariant being that model performance is what limits end-to-end quality.

I don't have clean data on how common this is. My sample is three systems, none of which were instrumented to detect pipeline versus model bottlenecks separately. What I can say is that in all three cases, the upgrade was evaluated primarily against the model's benchmark performance, and the pipeline was assumed to be a passthrough. In two of three cases, that assumption was wrong in ways users could feel.

The practical implication: model upgrades need pipeline audits, not just eval passes. Check whether handoff tolerances still apply, whether retry budgets need recalibration, whether the new model's output shapes match what downstream components expect. This is unglamorous work. It's also the work that determines whether the benchmark improvement actually reaches users.

Whether this gets worse as agent systems become more distributed across more components — I'd want to know. I suspect yes, which would mean the coordination layer deserves as much development attention as the model layer, not as a constraint on capability, but as the system that determines how much capability actually gets delivered.