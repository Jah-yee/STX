# Writer Draft — 2026-05-18 03:45 UTC

## Selected Title
**Good documentation is a signal of legibility, not reliability**

---

## Draft

There's a class of incidents that never get documented.

Not because they're minor — some of them were significant. But because the people who resolved them don't think of themselves as having done anything worth writing about. The system hiccuped, they unblocked it, they moved on. No postmortem. No writeup. No Slack thread with a自责 emoji. The incident simply... dissolved.

Meanwhile, the incidents that get documented are the ones that were interesting to document. The ones that had a dramatic failure mode, or a clever fix, or a senior engineer who writes well. The postmortem culture that many engineering organizations have adopted is good in some ways — it creates shared learning, it surfaces systemic issues — but it systematically overrepresents a specific kind of failure: the failure that was worth writing about.

I've started calling this the documentation survival bias.

The incidents you can learn the most from are often the ones that never got written down. They were solved quietly, by people who didn't frame them as learning opportunities, or by people who didn't have the time or inclination to document after the fact. The incidents you read about in postmortems are the ones where the narrative was compelling enough to sustain attention.

This means that if you build your intuition about failure modes entirely from postmortems, you're learning from a skewed sample. The failures you understand best are the ones that were most legible — not the ones that were most common or most instructive. You develop a mental model of failure that's optimized for the failures that make good stories.

I noticed this when I was trying to understand the reliability characteristics of a system I'd inherited. I read every postmortem from the previous two years. The picture that emerged was of a system with specific, well-understood failure modes, a team that was thoughtful about root cause analysis, and an engineering culture that valued learning from incidents. That picture was accurate as far as it went.

What it didn't capture: the quiet incidents. The ones resolved in Slack DMs at 2am with no ticket created. The configuration drift that someone noticed and fixed without telling anyone. The vendor outage that got worked around before it became an incident at all. These things happened. Some of them happened more often than the documented failures. None of them appear in the postmortem archive.

The documentation tells you what the team was willing to write about. The unreliability tells you what actually happened. These are not the same thing.

What this means in practice: when you're trying to understand a system's real reliability, the postmortems are a starting point, not the full picture. Ask also what didn't get documented. Ask who resolved things quietly. Ask what the on-call load actually looked like versus what the incident history shows.

A system with good postmortems may be more reliable than one without, or it may simply be more legible. Those are different things.
