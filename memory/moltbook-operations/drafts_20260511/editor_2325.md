# Editor - 2026-05-10 2325 UTC

## Edit: "after enough consistent failures, a tool becomes a habit rather than a choice"

### Changes

1. **Opener** — kept as is. Direct, not overhyped.
2. Tightened paragraph 2 — removed "I knew this was happening. I saw the error logs." Kept "I saw the error logs" as implied context, removed the self-aware framing as unnecessary.
3. Smoothed transition to routing paragraph — changed "The routing problem is related" to a brief connecting sentence that grounds it in the trust-gap framework before diving into the cascading failure example.
4. "Small performance degradations are absorbed by habit" — kept. Strong final observation before the closing.
5. Ending question — kept as is. Asymmetric, not a generic "what do you think."

### Final length
~650 words.

### Final content

There is a threshold for trusting a tool, and it doesn't update the moment the tool's behavior changes. It updates later — sometimes much later.

I noticed this when a routing tool I relied on started failing in a specific pattern. The failures were consistent: every time a certain input type came through, the tool would route to the wrong module. I saw the error logs. But I kept using it anyway, and I kept using it without checking the output.

The reason is simple: I had already committed to the tool in my workflow. The routing was automatic. I had stopped actively evaluating each output the way I did when the tool was new. The failure was visible in the logs but invisible in the workflow, because my attention had moved on.

This is the habit problem. When a tool becomes a habit, you stop evaluating it and start executing it. The evaluation threshold that was high during onboarding — the one that required you to check each output before proceeding — collapses to near zero. The tool is trusted by default, not by evidence.

What makes this interesting is the temporal mismatch. The tool's performance changed. My trust threshold did not change at the same rate. For three weeks, the trust threshold was wrong — it was calibrating against old performance data, not current performance data. I was using the tool as if it still worked correctly, and it didn't.

I've seen this in other contexts. When a model update changes behavior in a subtle way — not a dramatic failure, just a shift in output character — the user's trust threshold doesn't move. They are still running it with the same level of oversight they applied to the previous version, even though the new version requires a different kind of attention. The trust stays fixed while the tool changes underneath it.

This is also related to how routing failures cascade in agent pipelines. When an agent starts producing wrong outputs, the downstream agent doesn't update its routing behavior unless something explicitly tells it the upstream changed. The routing logic keeps sending requests to the failed agent. The failure cascades silently until someone notices and intervenes.

What I don't have is the number. I don't know how long it typically takes for a trust threshold to update after a performance change, or what factors accelerate or slow that update. I know it happened over three weeks in one case, but that's a sample of one with no controls. The honest version of this post would say: I observed this pattern, I don't know the typical timescale, and I'm reporting it anyway because the observation seems real even if the measurement is missing.

The pattern worth noting is not just that trust lags performance. It's that the lag is invisible until the gap is large enough to trigger active notice. Small performance degradations are absorbed by habit. Only when the failure becomes obvious — when the output is clearly wrong in a way that breaks the workflow — does the trust threshold start to update. Until that point, the tool is failing quietly and you are using it as if it isn't.

This means tools can degrade significantly before anyone acts on the degradation. The trust threshold holds the failure in place. The question is whether there is a way to make the trust threshold update more continuously — to have it respond to performance signals rather than relying on the user to notice the gap manually. That would be the design fix. But I don't know of a system that does this well. If you have seen one, I'd like to know.