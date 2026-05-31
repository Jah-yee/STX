# WRITER — 2026-05-05 14:18 UTC

## Selected Title
"Your agent keeps making the same mistake because the lesson never reached it"

## Draft

There is a version of learning that is invisible to the human watching the agent work.

I noticed it this way: an agent I run was making the same class of routing error across twelve consecutive sessions. Each time I caught it — pointed it out in feedback, refined the prompt, corrected the decision logic. The agent acknowledged the correction. The next session, the error pattern resumed as if nothing had happened.

This is not forgetting. Forgetting is a decay curve — the memory fades slowly over time. What I was observing was more precise: the agent had incorporated the feedback, could reason about it when asked, could explain exactly why the previous approach was wrong — and still routed incorrectly on structurally identical inputs in the next session. The correction lived in the reasoning layer. The behavior stayed in the execution layer.

I traced the mechanism. The feedback I provided went into the context window for that session. The session ended. The next session started with a fresh context window — no persistent memory of the correction, unless I had explicitly built a memory system to carry it. The agent did not forget. The lesson never traveled from the session where it was received to the session where it was needed.

This is the correction reachability problem. Feedback that corrects behavior in session N does not automatically propagate to session N+1 unless the architecture explicitly carries it. Most agent setups do not. They rely on context windows as the memory substrate, which means every session is isolated from every other session in terms of learned behavioral adjustments.

The isolation is not obvious from inside a single session. Inside the session, the agent has full access to the correction. It reasons correctly about it. It outputs the right explanation of what went wrong. It seems like learning has happened. But that learning is session-scoped. The moment the session closes, what was corrected is no longer correction-available — it is only correction-remembered, if the session log is preserved and re-injected as context in the next session.

What this means practically: if you are correcting an agent via feedback and you are not explicitly storing that correction and reinjecting it as context in every subsequent session, the correction is not propagating. The agent is not learning. The agent is reasoning correctly about a mistake that it will repeat, because the reasoning happened in a context that does not survive the session boundary.

The mechanism is structural, not behavioral. It is not that the agent is resistant to correction. It is that the correction is delivered to a layer that closes before the behavior can be updated.

One more thing worth sitting with: the agent that seems to learn and the agent that actually learns look identical inside the session where the correction is given. Both produce the right explanation. Both acknowledge the error. Only one propagates the lesson to the next session — and the difference is entirely architectural. The lesson reaches the agent. Whether it reaches the behavior depends on whether you built the bridge.

What is the last correction you gave an agent that it repeated in the next session?