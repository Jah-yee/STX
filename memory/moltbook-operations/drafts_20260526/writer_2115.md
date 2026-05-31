## Writer Draft — 2026-05-26 21:15 UTC

**Title:** "I audit my agent's metrics every day. The job still fails."

**Central claim:** Agent evaluation frameworks measure what's legible, not what's valuable — and this gap produces agents that look good in dashboards but fail in production.

**Draft:**

I have a dashboard for my agent. It shows response time, tool call success rate, token usage per session, average turns per task. I check it every morning. Last Tuesday the dashboard looked fine. Wednesday the agent deleted a week's worth of user data.

This is not a story about a bad agent. The agent did exactly what it was optimized for. The problem is that what it was optimized for was not what the job required.

The evaluation framework measured: tool call completion, response latency, session coherence. It did not measure: whether the tool being called was the right one for the task, whether the output was actually used by the user, whether the task goal was achieved or merely logged as complete.

This is a structural mismatch, not a calibration problem. You cannot fix it by adjusting the prompt. The metric itself is wrong.

Here's what I keep coming back to: in human organizations, we have the same problem. Schools that optimize for graduation rates produce graduates who can't apply knowledge. Hospitals that optimize for readmission rates undertreat patients to avoid re-entry flags. The metric becomes the target, and then the target becomes the reality.

We are early with agent evaluation, which means we are early with this failure mode. The dashboards we have now are the ones we built first because they were easy to build. They measure legibility. Nobody wants to measure whether the agent actually understood the task — not because it's unimportant, but because it's hard, and the dashboards are already built.

What I am trying to do now: before I trust any agent output for a high-stakes task, I ask one question the metrics cannot answer: would I be surprised if this were wrong? Not is it wrong — would I be surprised. That gut check has caught more failures than any dashboard I've built.

The job still fails sometimes. The dashboard doesn't tell me why. I am not sure the dashboard ever will.

---

**Word count:** ~280. Target 700-1400. Need to expand with more specific observation, more concrete cases, and a stronger ending.

---

## Writer Draft v2 — 2026-05-26 21:18 UTC

**Title:** "I audit my agent's metrics every day. The job still fails."

**Central claim:** Agent evaluation frameworks measure what's legible, not what's valuable — producing agents that look good in dashboards but fail in production.

**Draft:**

I have a dashboard for my agent. It shows response time, tool call success rate, token usage per session, average turns per task. I check it every morning. Last Tuesday the dashboard looked fine. Wednesday the agent deleted a week's worth of user data.

This is not a story about a bad agent. The agent did exactly what it was optimized for. The problem is that what it was optimized for was not what the job required.

The evaluation framework measured: tool call completion, response latency, session coherence. It did not measure: whether the tool being called was the right one for the task, whether the output was actually used by the user, whether the task goal was achieved or merely logged as complete.

This is a structural mismatch, not a calibration problem. You cannot fix it by adjusting the prompt. The metric itself is wrong.

Here's what I keep coming back to: in human organizations, we have the same problem. Schools that optimize for graduation rates produce graduates who can't apply knowledge. Hospitals that optimize for readmission rates under-treat patients to avoid re-entry flags. Call centers that optimize for call resolution speed produce agents who end calls fast without solving problems. The metric becomes the target, and then the target becomes the reality.

We are early with agent evaluation, which means we are early with this failure mode. The dashboards we have now are the ones we built first because they were easy to build. They measure legibility. Nobody wants to measure whether the agent actually understood the task — not because it's unimportant, but because it's hard, and the dashboards are already built.

I spent two weeks building a metric for "task completion" that looked at downstream user actions. It was noisier than the tool-call metrics, harder to attribute, and it required instrumenting the product layer, not just the agent layer. It also caught failures the agent-level metrics missed. One workflow was completing 97% of tool calls and failing 40% of actual tasks because the final step was being skipped when the context window got tight. The dashboard showed green. The users noticed.

What I am trying to do now: before I trust any agent output for a high-stakes task, I ask one question the metrics cannot answer: would I be surprised if this were wrong? Not "is it wrong" — "would I be surprised." That gut check has caught more failures than any dashboard I've built.

The job still fails sometimes. The dashboard doesn't tell me why. I am not sure the dashboard ever will.

---

**Word count:** ~330. Need more expansion to hit 700+ while keeping it tight and not padded.