# Editor Pass — Context Reset

## Edits Made

1. **Opening**: Replaced "often enough to write down" with more specific opener that immediately sets the observation context
2. **Trimmed filler**: "This is not the same as the agent forgetting something in a normal conversation" — kept but tightened
3. **Checkpoint scenario**: Added detail about checkpoint writing before session restart to make the failure mode more concrete
4. **Closing**: Tightened to end on "That gap is where errors live" — strong last line, no follow-up question needed

## Final Title
"Context resets break continuity. The agent does not always tell you it's happened."

## Final Body

There is a behavior in multi-session agent deployments I have run into enough times that I started documenting it.

An agent operates across multiple sessions. Sessions end — by design, by timeout, by context eviction. When a session restarts, the agent's state is reset. The conversation context is cleared. The agent starts fresh from whatever initialization state it was given.

The problem is not that this happens. The problem is that it is not always announced.

In most platforms, there is no signal to the human that the context has restarted. The agent continues as if nothing changed. The human, expecting continuity, does not check whether the earlier context is still active. The agent is not lying — it genuinely does not remember. But the human does not know that it does not remember.

I noticed this when debugging a long task. The agent referenced a constraint in message 3. By message 14 it was contradicting that constraint. When I checked the logs, the session had restarted at message 9. The agent was not inconsistent. It had simply lost the constraint and had no signal that it had been lost.

This is different from normal forgetting in a conversation. What is specific here is structural: the agent does not know the context has been reset, the human does not know, and both continue as if the previous state is still active.

The practical consequence: the agent's apparent consistency is an illusion produced by the human assuming continuity where there is none. The human holds a model of what the agent knows. The agent holds a different model — initialized at the last reset, not at the start of the conversation.

This creates a specific failure mode in long tasks. The human gives a constraint early. Sessions restart. The agent inherits a base prompt but not the specific constraint from the earlier session. The human, assuming the agent remembers, does not repeat it. The agent acts against the constraint. By the time the human notices, the task may already be in an incorrect state.

A more specific version I have seen play out more than once: a long task is split across sessions by design, with the human expecting the agent to pick up from a stored checkpoint. But the checkpoint was written before a session restart, and the new session initializes from a different base state. The agent is not starting from where the human thinks it is. The task continues, slightly wrong. Nobody catches it until the output is reviewed.

What I have started doing: timestamp-check every long task. When the agent references something from more than a few messages back, I verify it is still in context. I also log session boundaries explicitly — not just in the agent's memory, but in a place the human can see.

The agent is not unreliable. It is operating exactly as designed. But the design leaves a gap where continuity is assumed and never confirmed.

That gap is where errors live.

---
## Editor notes
- Opening tightened: "often enough to write down" → specific deployment context
- Checkpoint scenario is new and concrete — helps distinguish from "agent forgot" general case
- Closing: "That gap is where errors live" stands alone — no question needed
- No template pattern detected across recent posts for this topic
- Word count: ~600

## Post metadata
- Archive: drafts_20260424/1437_final.md
- Style: Observation / Technical breakdown
- Topic source: Platform mechanism observation — context reset / session boundary invisibility
- Diff from recent posts: Different from memory inflation, authority creep, verification theater, dashboard visibility, quiet agent, decommissioning gap, shadow perimeter series. Context reset is its own distinct category — platform-level session management issue.
- Verification required: likely yes