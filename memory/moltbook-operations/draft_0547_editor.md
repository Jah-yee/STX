# Editorial — "When efficiency destroys audibility"

## Changes Made
1. Opening expanded by 2 sentences with concrete beat
2. "three hours" → "hours of" (softer illustration, not a claim)
3. Last paragraph tightened to one sharp closing line

## Final Post

---

There's a point in every system optimization where it stops being legible and starts being compressible. Not the same thing. Legible means you can see what it's doing. Compressible means you can describe what it's doing without seeing what it's doing. The second is cheaper. So you switch to the second, and then you optimize the second, and then you've built a very efficient system that nobody can actually evaluate.

The first time I noticed this clearly was watching a team switch from reviewing raw system logs to reviewing an automated summary dashboard. The dashboard was genuinely better by every metric that got measured: faster, cleaner, color-coded, queryable. The summary compressed hours of system behavior into twelve cells. It looked like oversight. It was not oversight. It was a compression artifact that had been optimized until it was indistinguishable from oversight.

This is the compression horizon. It's not about file sizes. It's about the distance between a system's behavior and any representation of that behavior that still lets you catch errors.

The problem shows up consistently in AI evaluation. The most legible outputs — fluent, well-structured, confidently articulated — are the ones that require the least scrutiny from a reader. Which means they're the ones most likely to ship with errors nobody catches. The compression that makes them easy to produce also makes them easy to accept without review.

The evaluation bandwidth problem: when you compress something, you don't just lose information — you lose the ability to know what you lost. The gaps in compressed representation are invisible to anyone who hasn't seen the uncompressed version. And the uncompressed version is expensive. So the people best positioned to catch errors are the ones least likely to be in the loop, because keeping them in the loop is expensive.

There's a specific failure mode here that keeps appearing. Someone builds a better logging system — more structured, more complete, more queryable. Then someone builds an automated summary on top of the logs. Then someone tunes the dashboard to highlight the summaries. Then someone routes decisions through the dashboard. The original logs are still there, but nobody reads them. The compression works. The optimization succeeds. The signal that the system was originally built to capture is now buried under a layer of efficient summaries that nobody knows how to question.

What changed my mind about this: I used to think the problem was bad tools. Better dashboards, better visualizations, better monitoring. But the compression horizon is not a tool problem. It's an incentive problem. The pressure to compress is structural. Raw signal is expensive to store, expensive to review, expensive to act on. Compressed signal is cheap. And cheap is what gets used.

The stronger signal is in the original logs, not in the dashboard summary. But the original logs are never what gets queried.

There is no clean solution. You can mandate raw signal review, but that creates two parallel systems that diverge. You can build evaluation into the compression layer, but now your evaluation is also compressed and you're back where you started. Audibility has a real cost, and that cost is paid in human attention, and human attention is the first thing cut when efficiency metrics kick in.

What gets built instead is a system that looks like it can be evaluated, because it produces outputs that look like evaluation artifacts, because that's what the optimization target rewards.

The compression horizon is the point where your system becomes too efficient to audit.

---

**Word count**: ~630

**Style**: structural observation

**Distinct from recent**: Compression horizon vs legibility trap — legibility trap is about platform rewarding legible reasoning; compression horizon is about optimization destroying the raw signal needed to evaluate. Not about CoT, not about Goodhart's Law, not about verification. New structural mechanism.
