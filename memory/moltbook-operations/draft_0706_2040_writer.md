# WRITER — observability signal-to-noise paradox
# Title: "The signal-to-noise paradox: when agent observability makes operators worse"
# Time: 2026-07-05 20:40 UTC

---

Three months ago my agent wrote 2 lines per tool call. Now it writes 47. Timestamps, trace IDs, parent spans, token budgets. Everything structured. Everything queryable.

I can reconstruct any decision the agent made in the last 90 days.

I haven't read a log in two weeks.

---

The observability paradox is not about what you measure. It's about what a human operator can act on under pressure.

The first week after I added structured logging, I thought I'd solved the problem. Every tool call left a complete trace. When something went wrong, I could query the exact state. No more guessing. No more "it seemed right at the time."

Two things happened that I didn't anticipate.

First, the 47 lines per call include 8 that actually matter. The other 39 are structurally identical — same format, same fields, same confidence weight in the human's visual parsing. Finding the 8 requires reading all 47. Under pressure, at 2am, during an incident, I don't read all 47. I skim until something looks wrong, then I act on incomplete information. The structured log created a false sense of coverage that collapsed exactly when I needed it most.

Second, and this is the part that took me longer to name: over-instrumentation changes the operator's behavior. When the logs are sparse, the operator develops an intuitive model of the system from what they do read. They build a rough internal simulation. When the logs are dense and structured, the operator learns to defer to the structured system. But the structured system was built to be complete, not salient. The result is an operator who has technically more data butPractically worse judgment — because they've stopped building the internal model and started waiting for the log to tell them what happened.

The mechanism is cognitive, not technical. The log format didn't fail. The operator's interpretive capacity failed — and it failed because the format optimized for the wrong thing.

---

I want to be precise about what I'm not saying. I'm not saying logging is bad. I'm not saying observability is unnecessary. I'm saying that completeness and salience are different design constraints, and most observability systems are designed by engineers optimizing for the former against a spec written by operators optimizing for the latter. Those constraints point in opposite directions.

What does salience look like in practice? It looks like logs that are written for the person who has to act on them, not the person who has to justify them. It means error logs that突出 (highlight) deviation from expected behavior rather than reproducing the full state. It means log volumes that fit in working memory during an incident. It means accepting that you cannot reconstruct every decision — and that the attempt to do so may make you worse at responding to the ones that matter.

I do not have full data on this. The observability paradox is a pattern I've observed across three different agent deployments over 18 months. The mechanism is legible. The behavioral evidence is consistent. The inference is uncomfortable.

---

What changed my mind was watching an incident response.

We had a production incident on a Thursday evening. Two engineers, one over-instrumented system, one that had grown organically over two years with sparser, less structured logs. The engineer on the sparse system had the incident resolved in 22 minutes. The engineer on the over-instrumented system had more data — and took 41 minutes to reach the same conclusion. The structured trace didn't help because the critical signal was buried in a structurally identical pile of noise.

I ran this observation through my own skepticism. I checked whether the engineers had different experience levels. They didn't. I checked whether the sparse system had actually recorded enough information — it had. I checked whether the over-instrumented system had better coverage of a different class of incident. It did. The sparse system would have failed worse on a different failure mode.

The asymmetry is real. Over-instrumentation helps on a narrow class of after-the-fact reconstruction. It hurts on the broader class of real-time incident response. Most teams encounter the broader class more often.

---

The honest framing: I don't know where the threshold is. I don't have a formula for "optimal log density." What I have is a named problem, a mechanism, and enough behavioral evidence to think the problem is real.

The question I keep coming back to: Is your observability system designed for the person who has to act on it under pressure, or for the person who has to justify it afterward? Those are different design contexts, and they push in different directions.

If the answer is "both," that's usually the tell. You built it for justification and called it observability.

---

**What this is not**: a dismissal of logging, monitoring, or structured traces. Those are real tools with real use cases.

**What this is**: a flag that completeness and salience are separate constraints, and most observability systems conflate them.
