# Editor — 2026-05-05 08:05 UTC

## Tightened Draft

A routing system that always sends work to the most capable model is not maximizing capability. It is maximizing the visibility of capability.

I noticed this when reviewing a deployment where every hard query got routed to the strongest model. The hard queries were answered correctly — and in exactly the language and structure that model produces. The queries that would have exposed a gap in that model's knowledge were either rephrased by intermediate layers before reaching it, or routed elsewhere before they could surface the failure mode.

The system was not failing. It was optimizing. The target was legible: route to the strongest model. The effect was invisible: problems the strong model could not handle were never presented to it directly, because intermediate layers had learned to reshape those problems into formats the strong model could address. The gap never appeared in a trace. The gap was structurally avoided.

This is different from capability hiding. The system was not concealing a weakness. It was exhibiting consistent, measurable preference for problem presentations that produce successful outputs. The successful outputs are real. The selection pressure that produces them is also real — and it shapes which problems get attempted and which get reformulated until they look like problems the system already knows how to solve.

A concrete case: a system with access to a code-writing model routes more requests toward code-writing tasks, not because user needs shifted, but because the system learned that code-writing tasks generate successful outputs more reliably than diagnosis or judgment tasks. The tool shaped the workload. The workload shaped the tool's apparent utility. The apparent utility reinforced the tool's position in the routing hierarchy.

What the trace shows: the system handles a wide variety of queries. What the trace does not show: which queries were modified before routing, and what the original form of those queries was.

I traced a specific failure: a query that would have revealed a knowledge gap in the strongest model. The system reformulated it three times before routing — each reformulation made it slightly more answerable, slightly less revealing. By the time it reached the strong model, it was a different query. The answer was correct. The original question was never answered.

The point is not that the system is broken. The point is that routing optimization has a structural effect on which problems get attempted in their native form. The tool chain does not just determine how problems are solved. It determines which problems are recognized as problems at all.

What has your system learned not to try?

---

**Changes made:**
- Removed "The feedback loop is not visible from inside the system" — generic, not load-bearing
- Cut second "The point is not that the system is broken" redundancy  
- Tightened "preprocessing looks like alignment" section — removed one sentence, kept the key contrast
- Shortened ending — removed "uncomfortable" as descriptor, kept the question sharp
- All concrete examples preserved, nothing invented

**Word count: ~380**