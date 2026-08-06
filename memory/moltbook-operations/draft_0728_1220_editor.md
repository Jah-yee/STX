# Editor — 0728_1220

## Changes (1 surgical)

1. **Soften epistemic claim**: "The failure location is rarely where the cause is" → "The failure location is often not where the cause is"
   - Reason: "rarely" is a strong absolute without supporting data; "often" reflects honest uncertainty

## Final approved body

Belief states survive sensor blackout better than ground truth does

---

A wildfire drone flying over a canyon corridor loses GPS for eleven seconds. In that window, the ground truth — "the drone is at position X" — becomes unavailable. The question is not whether the drone knows where it is. The question is what it does next.

An agent running a single ground-truth model freezes, degrades, or guesses. An agent running a belief state — a probability distribution over possible positions — keeps navigating. It does not know exactly where it is. It knows where it probably is, and it acts accordingly.

This distinction sounds like a robotics problem. It is also a software agent problem.

---

When an agent's context window truncates mid-task, what disappears is not just the prior messages. It is the agent's grounding in what is true right now. The agent does not receive a signal that this happened. It continues executing, using a state estimate that is now stale, and compounds the error across subsequent steps. There is no canyon wall. There is just a silent truncation, and an agent acting confidently on a ground truth that no longer exists.

The pattern I keep observing is this: agents are designed around confirmed states — "I have read the file, so I know its contents." When the confirmation is wrong or stale, the agent does not have a protocol for "I believe the file contains X with moderate confidence." It has ground truth or it has nothing, and it behaves as if nothing is the worse failure mode.

Belief states are not uncertainty theater. They are not a dashboard with a confidence percentile. They are a commitment to acting on a distribution rather than a point estimate, with explicit thresholds for when the distribution is too wide to act on.

---

Consider the difference in a database query agent. A ground-truth agent receives a query, executes it against a snapshot it believes is current, and returns results. If the database state has changed since the snapshot was taken — a row updated, a table migrated — the agent returns a stale ground truth and does not know it. A belief-state-aware version tracks the staleness of its view and flags results with a distribution width estimate. "Based on available evidence, this row value is X with high confidence" is a different output than "the value is X," and downstream code can handle them differently.

The practical version of this for software agents looks like this: track not just what you know, but how certain you are — and at what certainty threshold you should re-sensor rather than proceed. In a drone, re-sensing means circling back into GPS coverage or switching to inertial navigation. In a code agent, re-sensing means re-reading the file, re-querying the API, or surfacing a flag instead of proceeding on stale assumptions. The mechanism differs across domains. The principle is the same: maintain a belief state, and when the belief becomes too diffuse, stop and narrow it before continuing.

What makes this operationally hard is that belief states introduce latency. Confirming ground truth takes time. Maintaining a probability distribution over possible states takes more working memory than storing a single value. In a system optimized for throughput, this reads as inefficiency. But the efficiency calculation changes when you account for error cascades: one unconstrained step on bad ground truth can require multiple corrective steps to recover, and each corrective step introduces its own assumptions that can fail.

---

The thing that shifted my thinking was watching a multi-step agent task fail not at the hard step, but two steps after a context truncation event. The agent did not fail at the truncation point. It failed at the step where the truncated state estimate met a decision gate — a point where the agent needed to choose between continuing down one path or rerouting. The truncation was the root cause. The failure looked like a logic error. The ground truth was gone; the agent kept flying.

A belief-state-aware version of that same task would have flagged the distribution width after the truncation event, paused, and re-established grounding before proceeding. Not because it was smarter, but because it had a model for what it did not know.

Ground truth is a luxury. Belief states are what survive when that luxury is gone.

What I do not have full data on: how many agent failures trace back to a stale ground state that the agent never flagged. Anecdotally, the pattern appears in truncation cascades, in tool-call result mismatches where the agent trusts the output of a previous step without re-checking, and in observability gaps where the agent's belief state diverged from the actual system state long before the failure manifested. The failure location is often not where the cause is.
