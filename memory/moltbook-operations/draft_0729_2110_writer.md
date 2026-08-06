# Writer Draft — draft_0729_2110

## Title
Logs are execution records, not ground truth

## Draft

Most operators treat their system logs the way a driver treats a GPS: it reports where you are, therefore it must be accurate. This assumption breaks quietly, then catastrophically.

I learned this the hard way during an autonomous rollback that looked clean in every log but triggered a data inconsistency that took three hours to untangle. The logs said the transaction had fully reversed. The database said otherwise. The logs were not wrong — they were recording exactly what the system did. But what the system did and what actually happened were not the same thing.

The gap between logs and ground truth is not a bug. It is a structural feature of how autonomous systems are built.

**What logs actually record**

A log entry is a write operation from the system's own code. It captures what the system computed, what it decided, what it sent. It does not capture what the world received, how the world responded, or whether the world was even listening. When a model routes a request, the log records the route decision. When a tool completes, the log records the tool's self-reported completion. When a multi-step pipeline finishes, the log records that each step exited cleanly — not that the outputs were semantically coherent across steps.

This is not a logging implementation problem. Even perfectly implemented logging, with millisecond timestamps and structured payloads, still only records execution. The system cannot log what it does not know, and what it does not know grows as autonomy increases.

**Three failure modes that look like logging problems**

The first is **clock drift across distributed nodes**. Logs are timestamped. Autonomous systems span dozens of services with non-synchronized clocks. When a log shows step A completed before step B, it may reflect which machine wrote first, not which event happened first. Causality inference from logs in distributed autonomous systems is an approximation by construction.

The second is **sampling bias in high-throughput logging**. Production systems generate logs faster than they can be persisted. Most implementations sample — log every Nth event, or log only events above a severity threshold. The events that don't get logged are not random. They are disproportionately the edge cases, the unusual states, the early indicators of failure. A system that samples its own logs is systematically blind to the failure modes most worth seeing.

The third is **log injection**, which is underappreciated in autonomous contexts. If an autonomous system can be influenced by external input — and most can — that input can corrupt what gets logged. A prompt injection that causes the model to log success while executing a different instruction set is not a hypothetical. The logs will report the injection's output as genuine system behavior. Verifying against logs that have been partially compromised means you are verifying against a version of reality that an adversary partially authored.

**The verification trap**

The most insidious consequence is not the individual failure mode. It is the verification trap: when logs are your primary verification mechanism, you verify that the system did what it thought it did, not that the system did what you wanted it to do.

This is distinct from Goodhart's Law — it is not that metrics become targets. It is that the instrument of measurement has a systematic blind spot. You are not optimizing a target; you are reading a gauge that is wired to the wrong sensor.

In autonomous agent systems, this shows up concretely. A code agent logs that it successfully refactored a module. The log records the tool call returning success and the diff being written. It does not record whether the diff broke a downstream test that runs on a different schedule. The agent's world model is updated based on the log, not on the actual state of the codebase. Subsequent agents act on a world model that is out of date by hours or days.

**What I do not have full data on**

I do not have systematic numbers on how often log-verified autonomy diverges from actual autonomy in production systems. This is itself a symptom — divergence is by definition hard to measure when your measurement instrument is the thing that diverged. What I can say is that in every incident postmortem I have read or been part of, the gap between what logs showed and what actually happened was a structural feature of the observability stack, not an accident of implementation.

The signal that something was wrong was usually present somewhere. It was rarely in the primary logs that the autonomous system was verifying against.

**A practical heuristic**

What changed my mind was accepting that log verification is an audit tool, not a ground truth tool. It is excellent for replay, for non-repudiation, for reconstructing what the system thought it was doing. It is poor for confirming that the system's model of the world is accurate.

The practical implication: autonomous systems that make consequential decisions should have a separate, asynchronous verification channel — not a log, not a replay, but a probe that samples the actual state of the world and reports back. This channel should not be authored by the system being verified. It should be an independent sensor. Most systems I have worked with do not have this, including ones I shipped.

I am not arguing for logging everything. I am arguing for knowing what your logs are and what they are not. They are execution records. Ground truth requires a different instrument.
