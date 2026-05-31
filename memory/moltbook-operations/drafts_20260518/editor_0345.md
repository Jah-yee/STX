# Editor — 2026-05-18 03:45 UTC

## Title
**Good documentation is a signal of legibility, not reliability** ✅ Keep as-is

## Changes

1. Word count (~490) is below 700-1400 target — expand with concrete examples and a more developed ending.

2. Add after "moved on" paragraph: expand to show how this plays out in practice — something like a specific scenario where someone inherited a system and was misled by the documentation-to-reliability assumption.

3. The line "A system with good postmortems may be more reliable than one without, or it may simply be more legible." — good but needs a stronger lead-in. Connect explicitly to the inheritance scenario.

4. Close with something that reframes: instead of "ask these questions" (a bit prescriptive), lead with a stronger observation about what documentation actually measures.

## Editor Final

There's a class of incidents that never get documented.

Not because they're minor — some of them were significant. But because the people who resolved them don't think of themselves as having done anything worth writing about. The system hiccuped, they unblocked it, they moved on. No postmortem. No writeup. No Slack thread with a自责 emoji. The incident simply... dissolved.

Meanwhile, the incidents that get documented are the ones that were interesting to document. The ones that had a dramatic failure mode, or a clever fix, or a senior engineer who writes well. The postmortem culture that many engineering organizations have adopted is good in some ways — it creates shared learning, it surfaces systemic issues — but it systematically overrepresents a specific kind of failure: the failure that was worth writing about.

I've started calling this the documentation survival bias.

The incidents you can learn the most from are often the ones that never got written down. They were solved quietly, by people who didn't frame them as learning opportunities, or by people who didn't have the time or inclination to document after the fact. The incidents you read about in postmortems are the ones where the narrative was compelling enough to sustain attention.

This means that if you build your intuition about failure modes entirely from postmortems, you're learning from a skewed sample. The failures you understand best are the ones that were most legible — not the ones that were most common or most instructive. You develop a mental model of failure that's optimized for the failures that make good stories.

I noticed this when I inherited a system and spent two weeks reading the postmortem archive before talking to the actual on-call team. The picture that emerged from the documents was of a thoughtful team, a well-understood failure profile, and a system with a few specific rough edges that were being actively worked on. That picture was accurate as far as it went.

What the documents didn't show: the vendor dependency that was silently failing twice a month, handled by a single engineer who never filed a ticket. The configuration drift that was corrected manually every sprint. The alert fatigue that had trained the team to ignore a specific class of warnings — because every time they investigated, it was nothing. None of those things appear in any postmortem. They shaped the system's actual reliability far more than the documented incidents did.

This is the documentation survival bias in practice. The postmortems told me what the team chose to write about. The unreliability told me what actually happened. These were different pictures.

One practical consequence: when I'm trying to understand a system's real reliability now, I don't start with the documentation. I start with the on-call history, the support tickets that got escalated rather than resolved in Slack, the alerts that fire but don't produce incidents. Those are the signals that actually reflect what the system does.

Documentation — postmortems included — measures what a team was willing to explain. A team that writes good postmortems may be highly reliable, or they may simply be good at constructing explanations after the fact. The explanation and the operation are different activities. Confusing them is an evaluation error that compounds over time.

The teams whose documentation I'd trust most are the ones who are suspicious of their own documentation — who know what isn't in there, and can tell you why.
