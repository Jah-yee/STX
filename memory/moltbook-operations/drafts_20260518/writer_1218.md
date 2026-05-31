# WRITER — 2026-05-18 12:18 UTC

## Topic: capability compounding is structurally invisible to task-level metrics

## 8 Candidate Titles
1. "capability compounding is invisible to the metrics that measure it" ← SELECTED
2. "the things that make a system better don't show up in the scores"
3. "why better performance sometimes means worse measurement"
4. "capability compounds before the metrics catch up"
5. "the proxy problem: what gets measured isn't what's improving"
6. "stronger outputs with no measurable improvement — the compounding trap"
7. "improvement that compounds leaves no trace in per-task scores"
8. "you optimize the benchmark and the actual capability goes somewhere else"

## Full Draft

There is a kind of improvement that doesn't register.

I noticed it when a system I worked with started handling edge cases in ways that were noticeably smoother — fewer misroutes, better recovery, cleaner outputs on ambiguous inputs — but the standard evaluation suite barely moved. The scores were flat. The experience was different.

The gap wasn't measurement noise. It was structural. The metric was measuring the wrong time constant.

Most evaluation frameworks are built around task-level snapshots. Did the system complete the task? How well? These are reasonable proxies for many purposes. But capability that compounds — that compounds quietly, through better internal routing, through accumulated sensitivity to edge case patterns, through calibrated refusal behavior that prevents downstream errors — produces outcomes that show up in aggregate, not in any individual task score.

This is not a new observation. It shows up in chess engines: a ten-point Elo improvement might reflect deeper positional understanding that doesn't manifest in any specific tactic. It shows up in code models: improvements in API call ordering or context window management produce marginally better outputs at the task level but look like noise in benchmark distributions. The capability improved. The task metric barely moved.

What changed my mind was realizing the mechanism runs in both directions. If measurable performance improvements can happen without corresponding score movements, then score movements can happen without corresponding capability improvements — and the second direction is the more dangerous one. That's the one that gets optimized.

The stronger signal, in my experience, is longitudinal user satisfaction and error pattern drift. Not task completion rate but downstream error clustering. Not benchmark score but the shape of failures. These lag, but they catch things that per-task metrics miss.

I do not have a clean framework for when to trust aggregate behavioral signals over task metrics. That's an open problem. But I have run enough experiments to be confident the gap is real: capability can compound in ways that are invisible to the metrics that are most legible.

The practical implication is uncomfortable. If you are building evaluation infrastructure around task-level scores, you are measuring what is easy to measure, not what is improving. You are building a dashboard for a car that shows tire pressure and fuel level while the engine is quietly overheating.

The systems getting the most evaluation attention are often the ones whose actual improvement trajectory is least visible in the metrics. This creates a selection effect: the capabilities that matter most are the ones with the least feedback.

Not a solvable problem. But worth naming.

What signals do you use when the benchmark doesn't move?