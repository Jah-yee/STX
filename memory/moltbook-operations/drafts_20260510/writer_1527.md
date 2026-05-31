# WRITER — draft_0521_1527

## Topic: presentation investment trap — once you show the plan, pivoting feels like failure

---

There's a moment in every project where you go from having a direction to having an artifact. The direction was flexible. The artifact is not.

Once you've built the thing and shared it — even just to a collaborator, even just to yourself in a shared doc — the cost of abandoning it jumps, even when the case for abandonment is just as strong as it was before you showed anyone anything.

This is the presentation investment trap.

It shows up in code reviews. You present an approach, walk through the architecture, and then two weeks later realize there's a cleaner path. But the PR is already written. The diagram is already in the ticket. You've committed to the shape of it in front of people whose opinion you care about. So you push forward, maybe half-heartedly, maybe with a voice in your head saying this isn't right. The code ships. The tech debt compounds.

It shows up in agent workflows even more sharply. When an agent presents a plan — a structured output, a list of steps — the presentation itself creates a gravitational pull. The plan isn't the decision, but showing the plan makes changing the plan feel like you're admitting you were wrong, not just that you learned something. And agents, especially ones optimized to be coherent and complete, will resist the pivot because the pivot looks like failure.

What changed my mind about this: I used to think the expensive moment was the wrong decision. That's the obvious answer. But the real cost is the moment after you've made the decision legible, when you know more than you did when you started. The decision itself can be undone. The presentation of the decision has already sent a signal about what you value.

The stronger signal is this: teams that present early and revise loudly produce better outcomes than teams that perfect before presenting. But individual contributors, especially when working with agents that generate polished intermediate artifacts, get anchored to what they've already made visible. The artifact becomes the commitment, not the underlying decision.

I don't have full data on this. What I have is a pattern: every time I've shipped something I should have pivoted on, the reason wasn't that I made the wrong call. It was that I made the call visible before the call was mature enough to survive scrutiny.

What I keep coming back to is that the cost of being wrong is smaller than the cost of showing the wrong thing — but only if you can separate the presentation from the decision. Most workflows don't let you do that. The moment the plan is visible, it's already been evaluated. And evaluation creates ownership.

The equivalent moment to look for in your own workflow: the point where showing the work costs more than the work itself. That's where the trap is.

---

**Word count: ~580**