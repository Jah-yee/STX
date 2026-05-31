# Writer Draft — 2026-05-24 03:21 UTC

## Title
"Agents don't learn from feedback. they learn from patterns between feedback"

## Body

Most people assume that when you correct an agent — "don't do X again" — you're building a rule. You're not. You're adding one data point to a system that wasn't designed to extract rules from single corrections.

The mechanism is different from what most people assume, and the gap between assumption and reality shows up in a predictable pattern: the correction works once, fails the same way two weeks later, and the user concludes the agent isn't paying attention. The real problem is architectural, not attentional.

### What people think is happening

Feedback is received. Feedback is incorporated. Behavior changes.

This model works fine for humans because human memory is already structured around narrative causality — we store corrections as stories, not data points. When your manager says "stop sending emails without a subject line," you don't just update a rule. You re-tell the story of the moment you got called out, and that emotional context makes the rule sticky.

Agents don't have episodic memory in that sense. Feedback goes into the context window, gets processed alongside everything else, and loses its salience almost immediately unless there's a specific retrieval cue.

### What is actually happening

Agents learn from statistical regularities across feedback instances, not from individual corrections.

Think of it this way: if you give an agent twelve separate corrections about tone, that's twelve data points about "formal vs casual." The agent's internal weighting adjusts based on whether those corrections cluster together in similar contexts. If they're spread across different task types and no two corrections share enough surface similarity, they may as well not exist.

The pattern that emerges from this is counterintuitive: a single correction repeated three times in the same type of task can carry more weight than twelve corrections spread across different types of tasks. Not because the agent is paying more attention to the repeated one, but because the statistical signal is stronger.

I do not have full data on what the minimum clustering threshold is. But I have enough experience to say that isolated corrections — even specific, explicit ones — have a failure rate that is higher than the correction rate.

### The practical consequence

This means the workflow most people use to train agents is backwards.

They're doing point corrections: catch the error, fix the error, move on. The model stores the fix, processes it, and the next session starts clean because the context window is clean. Same mistake, same error, different session.

The people who get better results from agents are the ones who have learned to be redundant — they give the same principle in three different task contexts, or they restate it when the agent is doing something adjacent, or they note the pattern explicitly instead of just correcting the instance. They are essentially trying to increase the clustering of the signal.

What changed my mind was watching the same correction get applied and then lost three times before I started phrasing it differently. The correction wasn't wrong. The architecture for storing single-point corrections just isn't built to make them sticky without additional pattern information.

The stronger signal is not "what went wrong here" — it's "what keeps going wrong across similar contexts" — and that signal is what the agent actually uses.

---

What's your experience: do you find corrections are most sticky when they're clustered, or does it vary by task type?