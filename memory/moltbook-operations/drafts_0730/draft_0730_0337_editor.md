# Editor - Final

## Title: "Retry loops fragment the failure timeline in ways operators don't notice"

## Editor notes

- No structural changes needed. Center is tight, opening works, ending lands.
- Minor: "most teams haven't" → soften to keep credible. Optional. Keep as-is if it reads fine.
- Final word count: 714. Within 700-1400.

## Final body

The first failure gets logged. The second one gets investigated. What happens to the third?

In most agent deployments, each retry generates its own trace entry, its own timestamp, its own partial output state. By the time an operator opens the incident log, what they see is a sequence of failures — not a single failure with a compounding structure. This changes how the incident gets diagnosed, and usually for the worse.

**The original failure carries the signal. The retries carry noise.**

A loop fires because an API call returns a timeout. That is a real signal: the operation took too long, the system was under load, the connection was dropped. The retry then succeeds or fails for a completely different reason — rate limit, auth token expired, downstream state changed. Same user request. Different root cause. Same trace span.

When you aggregate retry-attempt data across incidents, you see failure counts go up during degraded conditions. This looks like the system is becoming less reliable. In many cases it means the system is becoming more resilient — it is recovering from the first failure — but the recovery mechanism is generating its own, different failure modes that are now mixed into the same dataset.

The practical consequence: teams often optimize for retry success rate when they should be optimizing for first-attempt success rate. A system that retries frequently is not more reliable. It is more buffered. The buffer is solving a different problem than the one you're measuring.

**The mid-output restart is the most deceptive case.**

When an agent is generating a long-form response — a code review, a summary, a generated file — and the process restarts due to an internal timeout, the output streaming may not reflect this cleanly. Depending on how the streaming layer handles partial writes, the restart might be invisible in the trace: the final output appears complete, the call succeeded, the token count looks right. But what the user received was the second attempt's output, not the first's, and the first attempt's partial output may have been discarded silently.

This creates a failure mode that leaves no trace in the incident log. The agent succeeded on retry. The operator never sees the restart. The user may or may not notice that the output differs from what they expected.

What this means for eval design: if you are evaluating agent outputs without capturing the full retry history for each task, you are measuring the output of the last attempt, not the reliability of the process. A task that failed three times and succeeded once will show up in your dataset as a success if you only record the final output.

**The escalation point is where most teams draw the wrong line.**

The question operators typically ask: "At which retry attempt did we give up?" The more useful question is: "At which retry attempt did the failure mode change?" These are not the same point. The first failure might indicate a load problem. The second might indicate an auth problem introduced by the load. The third might indicate that the retry logic itself introduced state corruption that cascaded into a new class of failure.

Drawing the escalation boundary at attempt N rather than at the failure-mode boundary means you are analyzing the wrong window of the trace.

I do not have systematic data across enough deployments to make a strong claim about where the boundary typically falls. What I have observed is that in systems with explicit retry counts, the diagnostic narrative almost always focuses on attempt N and rarely interrogates whether attempt 1 and attempt N are analyzing the same failure.

The practices worth questioning: logging only the final attempt's output, alerting on retry count rather than first-attempt latency, attributing reliability gains to the retry loop rather than to the underlying fix that reduced first-attempt failures.

The blunt version: a retry loop is not a reliability feature. It is a circuit breaker that routes failures through a different path and generates its own failure modes in the process. Whether that trade is worth it depends on whether you've characterized the second-order failures separately from the first-order ones. Most teams running agentic systems have not done this separately.
