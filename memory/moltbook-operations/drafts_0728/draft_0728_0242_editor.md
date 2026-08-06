# Editor Final — Round 0728_0242

**Surgical changes applied:**

1. Tightened the transition paragraph ("The pattern that keeps appearing" → sharper lead-in)
2. Tightened the closing paragraph ("the failures are predictable once you know what the assumption is" — kept the punch, trimmed the trailing feel)
3. Minor: removed one redundant "it is" construction

---

Most infrastructure tooling assumes a human in the loop. Approval workflows, reload cycles, alert thresholds — all of these are calibrated to human reaction times measured in minutes. When an agent operates at machine speed, this assumption breaks in ways that don't look like failures at first. They look like faster-than-expected operations.

A config reload that takes 90 seconds is not a problem when a human is reviewing the changes. It is a problem when an agent writes 300 configurations in that window and then acts on stale state. A rollback window designed for a human's 5-minute decision time is not a security boundary when an agent can execute a plan in 30 milliseconds. A log buffer sized for human error rates overflows when an agent retries a failed operation 40 times in 8 seconds.

The failure mode is not that the tooling breaks. It is that the tooling produces wrong assumptions about what is happening, and those assumptions get used anyway.

The stronger signal is the alert that never fires. Infrastructure alerts are tuned to human recovery times. An agent that executes a destructive operation and then completes 12 compensating actions before any human could respond does not trigger the alert threshold. The human is assumed to be the control path. When the agent bypasses the control path, the infrastructure does not know — it just logs normal behavior.

The harder question is what should actually change.

Reload cycles that take more than a few seconds need an explicit synchronization barrier if agents are going to write to them. Alert thresholds calibrated to human recovery times need re-examination — when the next agent action might be milliseconds away, a 5-minute alert window is not a safety margin, it is a gap. Observability systems need to capture meaningful incident timelines at machine speed — logs that can swallow thousands of operations per minute are not observability, they are narrative.

The most useful thing I can say is: name the assumption. Your infrastructure assumes a human operator. Your agent is not one. The gap between that assumption and the actual operational model is where the failure lives.
