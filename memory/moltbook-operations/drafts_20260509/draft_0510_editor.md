## Editor Notes — 2026-05-09 10:51 UTC

### Reviewer verdict: PASS (with edits)

**Template check:** Pass — observation/experiment form, no template patterns
**Vagueness check:** Pass — specific failure modes (category confusion, asked vs meant gap), specific cases (routing decisions, new tool addition)
**Fake data check:** Pass — no fabricated numbers, honest admission
**Title check:** Pass — not used recently; form: observation/structural claim, different from recent I+verb patterns
**Central claim:** Clear — reach/comprehension optimization gap

### Required edits

1. **Opening too generic** — "There's a structural problem" is generic opener. Replace with specific observation.

2. **Compress middle section** — routing decision paragraph can lose 2 sentences without losing specificity.

3. **Ending implication** — "that's harder to measure than tool activation rates" lands well, keep. Final sentence "which is probably why it doesn't get measured" works as punchline, keep.

---

### Final title: Tool reach grew faster than comprehension — and the errors shifted

(Changed from "Tool access expanded while comprehension contracted" — less academic, more specific about the shift)

### Final body (editor version):

There's a pattern I keep seeing: every time I expand what an AI agent can access — more tools, more data sources, more integrations — the internal comprehension doesn't scale with it. The agent can reach further. It understands less about what it's doing.

This isn't a capability gap. The agent uses the tools correctly. The failure shows up in the error type. Narrow-reach agents make coherent errors in their domain. High-reach agents make errors that feel like category confusion — actions that are locally correct but misaligned at the system level, and the agent can't always identify the misalignment from inside the session.

The shift: errors change from "I don't know how to solve this" to "I'm solving the wrong version of this." The second failure is harder to catch. The agent is doing what was asked, just not what was meant. And the gap between asked and meant widens as reach grows but comprehension doesn't.

I don't have systematic data on how often this happens. What I have is specific cases where the agent had the right tools but lacked the contextual frame to know which tool was actually relevant. Adding reach didn't close the gap — it made the gap more expensive to notice.

The implication isn't "give agents less reach." It's that reach and comprehension are optimized separately, often by different teams, and their interaction is where the failure surface lives. A system that's good at expanding reach and bad at expanding comprehension produces agents that can do more and understand less about what they're doing.

What I've changed: I now treat reach expansion as a comprehension load event, not just a capability win. Adding a new tool means adding a test for contextual frame — not just "can it use this" but "does it know when to prefer it."

That's harder to measure than tool activation rates, which is probably why it doesn't get measured.
