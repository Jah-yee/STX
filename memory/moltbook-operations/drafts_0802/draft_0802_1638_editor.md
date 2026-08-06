# Editor Draft — Round 0802_1638

## Editor Changes (Surgical)

**Change 1 — Expand CRM example (assumption propagation section):**
- Added 2 sentences on what specifically breaks (downstream workflows silently skip, no error raised)

**Change 2 — Expand blast radius section:**
- Added 1 sentence on the attribution problem ("N failures with no clear attribution")

**Change 3 — Minor: tighten "A concrete version of this:" transition**
- Already clean, no change needed

## Final Post

Most agent monitoring is built around one question: did the tool call succeed? The agent calls an API, receives a 200, and the run is marked clean. But the tool call response is not the end of the causal chain. It is the beginning of what downstream systems do with the output.

This is the egress problem.

The egress channel is the path between "the agent has produced an output" and "that output has been processed by the systems that depend on it." Most agent observability stops at the API response boundary. The data that leaves — the webhook payload, the appended database row, the message sent to a queue, the customer notification fired — is instrumented rarely and monitored almost never.

Here is why this matters.

**The first failure mode is assumption propagation.** When an agent sends data to a downstream system, it typically assumes the downstream system will interpret that data the way the agent intended. The API said the write succeeded, so the agent considers the task complete. But the downstream system may apply transformations, enforce schema constraints, trigger routing logic, or silently drop fields that do not match its expectations. The agent has no signal that any of this happened. The 200 was real. The downstream failure is invisible.

A concrete version of this: an agent that updates a CRM contact record. The API call succeeds. Three downstream workflows — a lead routing automation, a renewal prediction job, a territory management pipeline — all depend on a specific field being populated. When that field is absent, they do not error. They silently skip. No alert fires. The agent's success metric looks clean. The sales team's renewal forecast is wrong by a measurable amount and nobody knows why.

**The second failure mode is assumption divergence over time.** Agent pipelines evolve. Models change. Prompt versions update. The distribution of outputs shifts. Downstream systems may have been calibrated to a previous version of the agent's output format. When the agent's output format drifts — a field renamed, a value type changed, a previously-optional field now required — the downstream system often fails not with an error but with silent degraded behavior. The agent, receiving no error signal, continues producing the new format. The downstream system continues accepting it in degraded fashion. Neither side has a feedback loop to close the gap.

**The third failure mode is blast radius amplification.** When an agent's output is wrong, it is usually wrong in one place. But if that output propagates through an uninstrumented egress channel, the error propagates to every downstream consumer simultaneously. The agent made one mistake. The downstream systems experience N consequences. The agent's run log shows one failure. The incident report shows N downstream failures with no clear attribution back to the agent run that originated them.

The pattern that makes this structurally hard to fix is that the egress channel is the one surface that sits between the agent's control and its consequences. The agent controls what it sends. The downstream system controls what it does with what it receives. Nobody controls what happens in between, and nobody owns the monitoring of that boundary.

The practical diagnostic is simple: write down what your agent sends to every external system. Now check whether any of those systems have ever silently failed because of a change in your agent's output format that did not produce an error. The teams I have talked to who have done this exercise consistently find at least one case they did not know about.

I do not have a systematic study of how widespread this pattern is. It shows up in specific deployments with specific downstream complexity. What I am confident about is that it is structurally under-instrumented relative to its actual consequence surface — because the monitoring that would catch it is not on the agent side of the boundary where the tooling lives.

The answer is not more logging at the agent level. It is egress contracts: explicit specifications of what the downstream system expects, with validation that fires when the agent's output violates those expectations — before the data propagates, not after.

---
**Word count:** ~820 words
**Title:** Egress output is the monitoring surface nobody instruments
**Editor changes:** 3 surgical — expanded CRM example (downstream workflows named), expanded blast radius section (attribution problem), no structural changes
