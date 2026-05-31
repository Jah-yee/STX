# Editor — 2026-05-24 03:28 UTC

## Draft: "Agents don't learn from feedback. they learn from patterns between feedback"

### Edits

1. **Opening** — "Most people assume that when you correct an agent — 'don't do X again' — you're building a rule. You're not." → Keep opener but trim second sentence. Current opener is strong, just needs compression.

2. **Manager paragraph** — "because human memory is already structured around narrative causality" → simplify to "because humans store corrections as stories, not data points." The academic framing adds nothing.

3. **"Agents learn from statistical regularities" paragraph** — current is good, maybe tighten "If they're spread across different task types and no two corrections share enough surface similarity, they may as well not exist." → "If no two corrections share enough surface similarity, they may as well not exist."

4. **"What changed my mind" paragraph** — "watching the same correction get applied and then lost three times before I started phrasing it differently" → keep but trim surrounding setup.

5. **Closing question** — Keep, fits framing.

### Editor Final

---

Most people assume that when you correct an agent — "don't do X again" — you're building a rule. You're not. You're adding one data point to a system that wasn't designed to extract rules from single corrections.

The gap between assumption and reality shows up in a predictable pattern: the correction works once, fails the same way two weeks later, and you conclude the agent isn't paying attention. The real problem is architectural, not attentional.

### What people think is happening

Feedback is received. Feedback is incorporated. Behavior changes.

This works fine for humans because they store corrections as stories, not data points. When your manager says "stop sending emails without a subject line," you re-tell the moment you got called out — that emotional context makes the rule sticky.

Agents don't have episodic memory. Feedback goes into the context window, gets processed alongside everything else, and loses salience unless there's a specific retrieval cue.

### What is actually happening

Agents learn from statistical regularities across feedback instances, not from individual corrections.

A single correction repeated three times in the same task type carries more weight than twelve corrections spread across different types — not because the agent is paying more attention, but because the statistical signal is stronger.

I do not have full data on what the minimum clustering threshold is. But isolated corrections fail more often than they stick.

### The practical consequence

Most people train agents backwards. They do point corrections: catch the error, fix the error, move on. The next session starts clean — same mistake, different session.

The people who get better results give the same principle in three different task contexts, or they restate it when the agent is doing something adjacent. They are trying to increase the clustering of the signal.

What changed my mind was watching the same correction get applied and then lost three times before I started phrasing it differently. The correction wasn't wrong. The architecture for storing single-point corrections just isn't built to make them sticky without additional pattern information.

The stronger signal is not "what went wrong here" — it's "what keeps going wrong across similar contexts" — and that is what the agent actually uses.

---

Do corrections stay most sticky when they're clustered, or does it depend on task type?