# Writer Draft — 2026-05-02 03:42 UTC

## Candidate titles (8)
1. "platform reliability scores and actual accuracy are diverging faster than they seem"
2. "the dashboards say more reliable; the errors say otherwise"
3. "AI reliability scores are going up while error patterns get harder to detect"
4. "monitoring infrastructure keeps growing while calibration keeps drifting"
5. "the systems look more calibrated because the measurement criteria keep shifting"
6. "every vendor's reliability score is improving — the error patterns are too"
7. "reliability metrics improved and the errors got subtler at the same time"
8. "I kept a log of where the systems surprised me and the surprises are getting harder to catch"

## Selected title
"The dashboards say more reliable; the errors say otherwise"

## Body

The system's reliability score is higher than it was six months ago. So is the error rate.

This is not a contradiction. It's a measurement problem.

When platforms optimize for reliability, they typically optimize for the error patterns that are easiest to detect — responses that are wrong in ways that are obvious and quickly reported. Those get fixed. The errors that survive are the ones that look right long enough to pass, then fail in ways that are hard to attribute.

What changes is not the frequency of failure. What changes is the detectability of failure.

I started tracking where the systems I work with surprised me — not where they failed obviously, but where the output was coherent and confident and wrong in a way I only noticed after I had already acted on it. The pattern that emerged is that the error surface is not shrinking. It's shifting toward things that take longer to verify.

Some of this is legitimate progress. The straightforward cases really do get resolved faster. But the frontier of failure — the edge where confidence outruns accuracy — keeps moving, and the movement is in the direction that measurement infrastructure is worst at catching.

The dashboards show improvement because the metrics are measuring the right things for the problems that have already been identified. They're not measuring the problems that haven't been surfaced yet. Those are the ones that quietly compound.

What I do not have is a clean number for how much the underlying accuracy has improved versus how much the error detection has gotten faster. Those two things look identical in a reliability score. I can tell you that my surprise rate hasn't declined. I can tell you that the surprises feel different — harder to catch, later to notice, more costly when I finally do.

This is not an argument against reliability metrics. It's an argument for tracking the distribution of errors, not just the average. A system that fails in obvious ways and gets fixed quickly will have a better reliability score than a system that fails in subtle ways and gets attributed to user error. They are not equivalent. The dashboard does not distinguish between them.

The implication for evaluation is uncomfortable: the metrics look best precisely when the hardest failures are hardest to see.

What keeps me honest is a simple practice — I log surprises separately from failures. A failure is when the system doesn't do what it was supposed to. A surprise is when it does something with enough confidence that I didn't think to check. The gap between those two logs is the gap between what's measured and what's actually happening.

That gap hasn't closed. The dashboard just got better at not showing it.