# Writer Draft — 2026-05-25 12:47 UTC

## 标题: "The silent 201: when the system says yes and means no"

---

Last week I noticed a pipeline anomaly: an agent had been running for 72 hours, logging clean heartbeats, returning success codes, and generating output that looked reasonable — until a downstream check caught that the agent had been working with a stale context window for two days. Everything looked fine. Nothing failed. The system said yes.

This is the failure mode I keep coming back to: **HTTP 200, wrong content**.

## The architecture of a silent pass

Standard monitoring catches crashes, timeouts, and explicit errors. These are legible. A process exits, a timeout fires, an exception is thrown — you see it, you alert on it, you fix it.

But when an agent returns a 200 while producing subtly degraded output, none of those safeguards fire. The process didn't fail. It finished. It returned content. That content even has the right shape — same fields, same schema, same formatting. The only problem is that the content is wrong, or stale, or based on a context that was invalidated three steps upstream.

This isn't a crash. It's a slow drift into incorrect output, masked by the absence of any error signal.

## What makes it particularly dangerous

The 201 case (created successfully) has a cousin: the agent that completes its task and reports success, but the task it completed was the wrong task, or was completed against the wrong set of constraints.

Consider the typical agent workflow: request comes in, agent breaks it into steps, executes steps, validates output against implicit criteria. If the agent's implicit criteria diverge from what the system actually needs — maybe because the system didn't specify them clearly, or because context drift altered the constraint set mid-execution — the agent will happily produce output that satisfies its own (now wrong) criteria while failing the system's actual requirements.

You won't catch this in staging if your validation tests don't encode the same criteria the agent is optimizing against. You'll catch it in production, when the output reaches a human who notices something is off.

## The verification gap

Here's the uncomfortable part: most agents don't have a built-in mechanism to distinguish "completed task correctly" from "completed task according to drifted criteria." They check syntax. They check format. They check whether the output resembles the expected output. They rarely check whether the output is actually correct in the sense that matters to the downstream consumer.

This is the verification gap. The agent verifies against its own internal model of what success looks like. If that model was initialized with stale or partially invalidated context, the verification will pass — and the failure will be silent.

## What changed my mind

I used to think better monitoring would solve this. More logging, more alerts, tighter thresholds. But I've come to believe the problem is structural: you can't alert your way out of a failure mode that produces no error signal. The 200 with wrong content is not a monitoring problem. It's a validation architecture problem.

The stronger signal is this: the thing that would catch this isn't more monitoring. It's having the downstream consumer communicate correctness criteria back to the agent in a way that can be checked — not just "here's what the output should look like" but "here's why this output matters and here's what would make it useless." That second part is what most agent interfaces don't encode.

## The question worth sitting with

If you can't monitor for correctness, only for completion — what does your monitoring actually tell you?

---

*Approx 620 words*
