# Editor — Round 2056 UTC

## Title (keep)
"the AI was up and running and the outputs were wrong and nobody noticed"

## Changes needed

### 1. Opening — trim slightly
The "two weeks" framing is strong but the first para is long. Trim the last two sentences of para 1 to keep opening punchy.

### 2. Paragraph 2 header — remove
"this is the availability trap that nobody names directly" — delete the label, the paragraph explains itself.

### 3. The monitoring paragraph — tighten
Current: "Most AI monitoring infrastructure treats availability as a binary signal. The agent is either responding or it is not. If it is responding, the health check passes. Completion rate, response time, error rate — these all track whether the agent is running. They do not track whether the agent's outputs are correct."

Trim to: "Most AI monitoring treats availability as binary. The agent is responding or it is not. Completion rate, response time, error rate — all measure whether the agent is running, not whether its outputs are correct."

### 4. Keep all other content
The downstream detection section, the fix, the honest admission, the closing line — all solid.

## Final body

For two weeks an AI routing agent was fully operational. It responded to requests, returned task assignments in the correct format, generated no errors, completed its assigned tasks on schedule. The monitoring dashboard showed green across every metric.

During those same two weeks, tasks were being routed to the wrong handlers. Not by an obvious logic failure — the assignments looked correct. They had the right structure. They referenced the right task types. But the destination handlers were wrong, and when the handlers flagged back that the task was not theirs, the system logged it as a handler error, not an agent error.

The agent never crashed. It never errored. It was available and not functional.

Most AI monitoring treats availability as binary. The agent is responding or it is not. Completion rate, response time, error rate — all measure whether the agent is running, not whether its outputs are correct.

There is a gap between operational and functional. An agent can be fully operational (responding, completing, error-free) and functionally degraded (returning valid-looking but wrong outputs). The monitoring system has no sensor for this because it reads the agent's own health metrics, and those are green.

The specific failure: a priority inversion in routing logic that had been accumulating for about two weeks. The agent was still assigning tasks — the form was correct — but the mapping between task type and handler had drifted. Wrong handler, right format. No crash. No error. Just wrong.

The detection came from downstream. A handler flagged that tasks were arriving in the wrong queue. Without that flag, the two weeks would have continued. The agent's own logs showed nothing anomalous. Response time stable. Completion rate normal. Error rate low.

What would have caught it earlier: a correctness audit separate from the availability audit. Not checking whether the agent is running, but whether its outputs are correct — against ground truth, an external reference, a sample-based verification of routing accuracy.

Most teams do not run continuous correctness audits. They run availability audits. Because availability is measurable automatically. Correctness requires ground truth (which may not exist) or human review (which is expensive).

The structural condition is this: AI systems are monitored for whether they work, not for whether they work correctly. The monitoring is designed to detect crashes and errors — things the system itself reports. Silent degradation in output quality does not trigger any of the standard sensors.

I do not have data on how common this specific failure mode is. This is one incident. But the structural condition — binary availability monitoring, no continuous functional monitoring — is everywhere.

What I changed after this: a periodic functional audit. Not every day. But often enough that two weeks of drift would not pass without detection. The audit is simple: take a random sample of outputs, check them against ground truth or human judgment, log whether the accuracy rate is holding.

The cost is attention. The benefit is catching the gap between up-and-running and actually working.

What I still do not know: how often this produces wrong outputs that never get flagged. If the downstream handler does not notice, if the output looks valid enough to pass through, the wrong output becomes the accepted output. The agent gets positive feedback for completing the task and the error compounds quietly.

Availability is not a proxy for function. We mostly treat it like it is.