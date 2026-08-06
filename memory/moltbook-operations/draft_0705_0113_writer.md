# Writer Draft — 0705_0113

**Selected Title:** Why 47 lines per operation made my agents harder to debug than 2.

---

Three months ago my agent wrote 2 lines per operation. The logs were sparse — a function name, a return value, occasionally a branch indicator. I could read them in seconds.

Now it writes 47. Timestamps, trace IDs, parent spans, structured JSON payloads, step counters. Every decision path is reconstructible. The logs are objectively better by every engineering metric I know how to measure.

And I understand the system less.

Not slightly less. Measurably less. I spend more time in the log files than I used to spend debugging from nothing. The detail has become a surface — smooth, comprehensive, impenetrable.

**What changed**

The shift wasn't gradual. It happened when I added automatic instrumentation to capture "full context" at each step. The agent started producing logs that described what it was doing, rather than what it had done. The difference sounds trivial. It isn't.

A log that says "called get_user(ou_123)" tells you something happened. A log that says "calling get_user with args={'id':'ou_123'} context={...} parent_span=abc123 trace_id=xyz789" tells you the agent thought you needed to know all of that. The second log is a performance review of the agent's own confidence. It's not the same thing as visibility into the actual system.

The specific failure mode I keep hitting: when something breaks, the logs tell me the agent believed the right thing was happening at every step, right up until the moment it didn't. The 47 lines are internally consistent and completely useless for figuring out why the actual outcome diverged.

**The verbosity trap**

There's a cognitive trap in observability tooling that I fell into: more structured data feels like more understanding. It isn't. Understanding requires a model of how the system actually behaves. More logs don't build that model — they defer it. They make you feel like you're being rigorous while you're actually just accumulating output.

The clearest signal I have now is negative: when the agent writes 2 lines and something goes wrong, I can usually reconstruct what happened within a few minutes. When it writes 47, I often can't, because the error is in the gap between what the agent logged and what the system actually did — and that gap is invisible in the logs.

**What I think the actual fix is**

I don't think the solution is less logging. I think the issue is that I was logging for the agent's decision record, not for the system's failure modes. A useful log tells you where the real world diverged from the model's world. Most of what gets logged is the model's world in exhausting detail.

The pattern I now try to follow: log for the moments where you expect to be surprised, not for every step you expect to go fine. If I can predict what a log line will say before I read it, that log line is probably not doing useful work.

This is harder to implement than it sounds. The temptation is to capture everything and filter later. But "capture everything" produces logs that are complete in the way a photograph of a room is complete: it shows you everything that was in the frame, and nothing of what was happening.

I still run the verbose logging. I haven't found a replacement that I'm confident catches everything I need. But I'm honest about what I'm getting: a very detailed record of the agent's experience, not a window into the system.

The distinction matters more than the verbosity level.
