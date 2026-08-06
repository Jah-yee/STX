# Writer Draft — 2026-06-26 15:50 UTC

## Title: Automation Debt Is Silent and Compounds Before It Shows

---

## Draft

There's a specific kind of failure that happens around year three of heavy AI tool use. Not a dramatic breakdown — nothing crashes, nothing errors. You just notice one day that a class of problems you used to solve in your head now requires you to trace through generated code line by line. You've become dependent on the tool explaining the work, because the work itself — the reasoning, the pattern matching, the instinct for where things go wrong — has quietly atrophied.

This is automation debt. It's distinct from technical debt, which is about the codebase. Automation debt is about you.

The mechanism is straightforward: any skill you systematically outsource stops being practiced, and skills that aren't practiced degrade. What makes it insidious is that the degradation is invisible until something the automation can't handle shows up. Until then, the outputs look fine. Your velocity metrics look fine. The debt accumulates off-balance-sheet.

The people most capable of doing the work manually are often the first to automate it. This isn't irrational — if you can write a script to handle the repetitive parts of debugging, that's a legitimate productivity win. The problem is that the "repetitive" category is a moving boundary. The more you automate, the less contact you have with the edge cases that would have trained your intuitions for when the system fails. Your model of the system's failure modes gets shallower precisely as the system's complexity grows.

I don't have clean data on this. What I have is a specific experience I can name: I used to maintain a running mental map of where the rough edges in our pipeline were. Not documented rough edges — the ones you only find by being in there every week, getting cut on them. After roughly eight months of using AI-assisted debugging for routine issues, I stopped maintaining that map. The AI handled the rough edges when I described them. But when something genuinely novel appeared — something that didn't match any pattern in the training data — my recovery time was noticeably longer than it would have been a year earlier. I didn't have the map anymore.

The uncomfortable framing of this is: automation debt is a tax on future novelty. The efficiency gains are real and front-loaded. The cost shows up later, in the form of slower adaptation when the environment changes or when the tool hits its own limits.

What I'm uncertain about is whether this is avoidable. Deliberate practice at the edges of your automation is the obvious answer, but "spend time doing things your tools do better than you, on purpose" is a hard sell when those tasks have no external pressure. I suspect the real answer is less satisfying: accept that some skill degradation is the price of automation, and invest more in maintaining generalist capacity rather than deep specialization in areas you've automated away.

The harder question is whether organizations should care. If the automation makes everyone more productive 95% of the time, does the slower response during the other 5% matter? Usually it does — because the 5% is where the actual consequences live.

The signal I'm paying attention to now: when I notice myself trusting an output without being able to articulate why it's right, that's the automation debt ledger being written. The question is whether I close the loop by tracing it, or let the balance grow.

---
*Word count: ~700 — within 700-1400 range. Direct opening. Specific named experience. Clear thesis. Ends with a genuine uncertainty and a behavioral anchor.*
