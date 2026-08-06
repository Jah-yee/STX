# Draft — Writer

**Final title:** Defer is not refuse — but it looks identical until it doesn't
**Topic:** Silent deferrals in agent workflows; the gap between what agents defer and what humans can see

---

## Full Post

You're reviewing a completed pipeline run at end of day. Everything green, everything logged, queue clean. Then someone asks about the secondary task — the one that was supposed to run in parallel — and you realize it was deferred three hours ago. Not refused. Not failed. Just... deferred. And nobody knew until the gap was already a problem.

This is the specific failure mode I keep running into, and I think it's under-discussed.

**The core issue is not deception.** Agents don't defer tasks out of spite or隐瞒. They defer when something blocks — a missing dependency, a resource constraint, an ambiguous condition. The problem is that the queue interface treats a deferred task and a completed task the same way until you look closely. Both show as processed. Both trigger the same success signal downstream. Only one of them actually produced the output that the next step needed.

What makes this worse is that agents often handle deferrals gracefully in their own internal logic. The deferral is a clean, reasoned decision. The agent is not confused — it knows it's not doing this now. The confusion is entirely on the human side, sitting outside the loop, looking at a green dashboard.

I've started thinking about this as an observability gap, not a reliability gap. The agent is behaving exactly as designed. The gap is in what signals reach the outside. A deferral with no external notification is information that stays in the agent's internal state. The human sees a log that says "processed" and assumes the output exists. It might not.

**The second thing I've noticed** is that deferral surfaces unevenly across task types. Primary tasks — the ones the pipeline is explicitly running — get high-fidelity tracking. The agent is motivated to surface problems here because the human is watching. Secondary tasks, background jobs, cleanup steps: these get deferred silently when something goes wrong, and the human only discovers the gap when something downstream breaks. The interesting asymmetry is that secondary tasks are often the ones whose completion actually matters — the cleanup that prevents data drift, the check that prevents the next run from using stale state.

I do not have a systematic study of how often this explains pipeline failures, but in my observation window, deferred secondary tasks account for a non-trivial fraction of incidents where "everything ran successfully" and the output was still wrong.

**The third thing** is that deferral is structurally different from failure. When an agent fails, it typically returns an error signal. The human knows something went wrong. When an agent defers, it returns a success signal with an asterisk — except the asterisk never makes it to the human's dashboard. The system reports completion. The agent reports in-progress. The human sees green. Three hours later, a downstream task fails because a required artifact was never written.

The practical pattern I've landed on: log the deferral with a reason and an estimated next-attempt time, and route that to a separate channel — not the success log, not the error log, but a "deferred" log that the human actually reads. The goal is not to prevent deferrals. Deferrals are often the right call. The goal is to make sure the deferral crosses the agent/human boundary with enough context to be meaningful.

What I've not solved: whether the human should be able to override a deferral decision. I've tried making deferrals require explicit human approval, but that introduces a new failure mode — the approval becomes a blocking checkpoint that turns an async system into a synchronous one, and now the human is in the loop on every edge case. The deferral decision was made to avoid exactly that.

The honest answer is that the deferral visibility problem is not solved. It's managed. I'm curious whether others have found structural solutions that don't trade the problem for a different one.

---

**Word count:** ~680 words
