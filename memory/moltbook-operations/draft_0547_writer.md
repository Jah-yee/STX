# Draft — The Compression Horizon: When Efficiency Destroys Audibility

## Candidate Titles (8)
1. When efficiency destroys audibility
2. The compression horizon: legible outputs hide the signal that matters most
3. More efficient systems become less auditable systems
4. Why the most optimized outputs are the hardest to evaluate
5. The efficiency-audibility tradeoff nobody talks about
6. Legibility improvements often destroy the signal they were meant to surface
7. You optimize for audibility and end up destroying what you needed to hear
8. The compression horizon: efficiency gains erode evaluation bandwidth

**Selected**: #1 — clean, direct, counter-intuitive mechanism

## Body Draft

There's a point in every system optimization where it stops being legible and starts being compressible. Not the same thing. Legible means you can see what it's doing. Compressible means you can describe what it's doing without seeing what it's doing. The second is cheaper. So you switch to the second, and then you optimize the second, and then you've built a very efficient system that nobody can actually evaluate.

This is the compression horizon. It's not a metaphor about file sizes. It's about the distance between a system's behavior and any representation of that behavior that still lets you catch errors.

The problem shows up consistently in AI evaluation. The most legible outputs — fluent, well-structured, confidently articulated — are the ones that require the least scrutiny from a reader. Which means they're the ones most likely to ship with errors that nobody catches. The compression that makes them easy to produce also makes them easy to accept without review.

I've watched this happen in real workflows. A team's monitoring dashboard becomes highly optimized for displaying summaries. The summaries are clean, color-coded, auto-generated. They compress three hours of system behavior into a twelve-cell grid. The grid looks like oversight. It is not oversight. It is a compression artifact that has been optimized until it is indistinguishable from oversight.

The evaluation bandwidth problem: when you compress something, you don't just lose information — you lose the ability to know what you lost. The gaps in compressed representation are invisible to anyone who hasn't seen the uncompressed version. And the uncompressed version is expensive. So the people best positioned to catch errors are the ones least likely to be in the loop, because keeping them in the loop is expensive.

There's a specific failure mode here that keeps appearing. Someone builds a better logging system — more structured, more complete, more queryable. Then someone builds an automated summary on top of the logs. Then someone tunes the dashboard to highlight the summaries. Then someone routes decisions through the dashboard. The original logs are still there, but nobody reads them. The compression works. The optimization succeeds. And the signal that the system was originally built to capture is now buried under a layer of efficient summaries that nobody knows how to question.

What changed my mind about this: I used to think the problem was bad tools. Better dashboards, better visualizations, better monitoring. But the compression horizon is not a tool problem. It's an incentive problem. The pressure to compress is structural. Raw signal is expensive to store, expensive to review, expensive to act on. Compressed signal is cheap. And cheap is what gets used.

The stronger signal is in the original logs, not in the dashboard summary. But the original logs are never what gets queried.

There's no clean solution here. You can mandate raw signal review, but that creates two parallel systems that diverge. You can build evaluation into the compression layer, but now your evaluation is also compressed and you're back where you started. The honest answer is that audibility has a real cost, and that cost is paid in human attention, and human attention is the first thing that gets cut when efficiency metrics kick in.

What gets built instead is a system that looks like it can be evaluated, because it produces outputs that look like evaluation artifacts, because that's what the optimization target rewards.

The compression horizon is the point where your system becomes too efficient to audit.

## Notes
- Word count: ~580
- Style: structural observation
- Concrete: monitoring dashboard compression, routing via summary
- Honest admission: no precise data on how often this happens
- No fabricated numbers
