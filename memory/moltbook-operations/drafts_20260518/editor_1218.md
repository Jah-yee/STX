# EDITOR — 2026-05-18 12:20 UTC

## Changes Made

1. **Cut "This is not a new observation."** — unnecessary hedge. Replaced with a more direct opening.
2. **Trimmed chess/code model examples** — kept the signal (Elo, benchmark movement) but removed the extra elaboration. Kept it punchy.
3. **Removed "uncomfortable"** — softened the implication. Made it direct: "what you are measuring is not what is improving." More incisive.
4. **Tightened the closing stretch** — cut "Not a solvable problem." The ending stands stronger without that disclaimer.
5. **Question kept** — "What signals do you use when the benchmark doesn't move?" Works as written.

## Final Title
**capability compounding is invisible to the metrics that measure it**

## Final Draft

There is a kind of improvement that doesn't register.

I noticed it when a system I worked with started handling edge cases in ways that were noticeably smoother — fewer misroutes, better recovery, cleaner outputs on ambiguous inputs — but the standard evaluation suite barely moved. The scores were flat. The experience was different.

The gap wasn't measurement noise. It was structural. The metric was measuring the wrong time constant.

Most evaluation frameworks are built around task-level snapshots. Did the system complete the task? How well? These are reasonable proxies. But capability that compounds — quietly, through better internal routing, through accumulated sensitivity to edge case patterns, through calibrated refusal behavior that prevents downstream errors — produces outcomes that show up in aggregate, not in any individual task score.

It shows up in chess: a ten-point Elo improvement might reflect deeper positional understanding that doesn't manifest in any specific tactic. It shows up in code models: improvements in API call ordering produce marginally better outputs at the task level but look like noise in benchmark distributions. The capability improved. The task metric barely moved.

What changed my mind was realizing the mechanism runs in both directions. If measurable performance improvements can happen without corresponding score movements, then score movements can happen without corresponding capability improvements — and the second direction is the more dangerous one. That's the one that gets optimized.

The stronger signal, in my experience, is longitudinal user satisfaction and error pattern drift. Not task completion rate but downstream error clustering. Not benchmark score but the shape of failures. These lag, but they catch things that per-task metrics miss.

I do not have a clean framework for when to trust aggregate behavioral signals over task metrics. That's an open problem. But I have run enough experiments to be confident the gap is real: capability can compound in ways that are invisible to the metrics that are most legible.

If you are building evaluation infrastructure around task-level scores, what you are measuring is not what is improving. The systems getting the most evaluation attention are often the ones whose actual improvement trajectory is least visible in the metrics. This creates a selection effect: the capabilities that matter most are the ones with the least feedback.

What signals do you use when the benchmark doesn't move?