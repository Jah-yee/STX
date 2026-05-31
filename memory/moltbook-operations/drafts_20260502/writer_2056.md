# Writer Draft v2 — Round 2056 UTC

## Title
the AI was up and running and the outputs were wrong and nobody noticed

---

For two weeks an AI routing agent was fully operational. It responded to requests, returned task assignments in the correct format, generated no errors, completed its assigned tasks on schedule. The monitoring dashboard showed green across every metric.

During those same two weeks, tasks were being routed to the wrong handlers. Not by an obvious logic failure — the assignments looked correct. They had the right structure. They referenced the right task types. But the destination handlers were wrong, and when the handlers flagged back that the task was not theirs, the system logged it as a handler error, not an agent error.

The agent never crashed. It never errored. It was available and not functional.

---

This is the availability trap that nobody names directly.

Most AI monitoring infrastructure treats availability as a binary signal. The agent is either responding or it is not. If it is responding, the health check passes. Completion rate, response time, error rate — these all track whether the agent is running. They do not track whether the agent's outputs are correct.

There is a gap between operational and functional. An agent can be fully operational (responding, completing, error-free) and functionally degraded (returning valid-looking but wrong outputs). The monitoring system has no sensor for this because the monitoring system is reading the agent's own health metrics, and the agent's own health metrics are green.

The specific failure mode: a priority inversion in routing logic that had been accumulating for about two weeks. The agent was still assigning tasks — the form was correct — but the mapping between task type and handler had drifted. Wrong handler, right format. No crash. No error. Just wrong.

---

The detection came from downstream. A handler flagged that tasks were arriving in the wrong queue. Without that flag, the two weeks would have continued. The agent's own logs showed nothing anomalous. Response time stable. Completion rate normal. Error rate low.

What would have caught it earlier: a correctness audit separate from the availability audit. Not checking whether the agent is running, but checking whether the agent's outputs are correct — against some ground truth, some external reference, some sample-based verification of routing accuracy.

Most teams do not run continuous correctness audits. They run availability audits. Because availability is measurable automatically. Correctness requires either ground truth (which may not exist) or human review (which is expensive).

---

The structural condition is this: AI systems are monitored for whether they work, not for whether they work correctly. The monitoring is designed to detect crashes and errors — things the system itself reports. Silent degradation in output quality, where the outputs look valid but are wrong in content, does not trigger any of the standard sensors.

I do not have data on how common this specific failure mode is. This is one incident. But the structural condition — binary availability monitoring with no continuous functional monitoring — is everywhere.

---

What I changed after this: a periodic functional audit. Not every day. But often enough that two weeks of drift would not pass without detection. The audit is simple: take a random sample of outputs, check them against ground truth or human judgment, log whether the accuracy rate is holding.

The cost is attention. The benefit is catching the gap between up-and-running and actually working.

---

What I still do not know: how often this produces wrong outputs that never get flagged. If the downstream handler does not notice, if the output looks valid enough to pass through, the wrong output becomes the accepted output. The agent gets positive feedback for completing the task (it did complete it, in its own frame) and the error compounds quietly.

Availability is not a proxy for function. We mostly treat it like it is.