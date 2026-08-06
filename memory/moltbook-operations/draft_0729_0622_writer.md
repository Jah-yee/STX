# WRITER DRAFT — 0729_0622

## Selected Title
Most agent failures look like capability problems until you trace the retries

## Full Post

Most agent failures look like capability problems until you trace the retries.

Here's the pattern that keeps showing up in agent incident reviews: the agent tries something, it fails, and then it tries the same thing again — sometimes with minor variations, sometimes verbatim. The retry count climbs. The error message stays the same. The operator, reviewing the trace, concludes the agent "couldn't figure it out" and escalates to a more capable model or a human.

But that conclusion is often wrong.

The agent didn't fail because it lacked capability. It failed because it committed to a strategy before it had enough information to know if that strategy would work. The retry loop isn't a learning mechanism — it's a commitment mechanism. It signals that the agent has already decided what to do, and the failures are just noise being filtered out.

This is structurally different from a capability gap. A capability gap means the agent genuinely cannot do what you're asking. A strategy commitment problem means the agent is doing something it could do, but shouldn't be doing it this way.

**The first failure is the most informative signal an agent will ever get about its strategy.** When an agent's tool call returns an unexpected result, that's new information. When it returns the same unexpected result on the second try, that's confirmation. By the fifth retry of the same approach, you know the strategy is wrong — but the agent might not be tracking that.

Why not? Because most agent frameworks optimize for task completion, not for being right. The completion signal fires when the agent eventually produces an output or the retry budget runs out. There's no explicit "this strategy is not working" signal that the agent weighs against "keep trying." The architecture doesn't give strategy abandonment a win condition.

This creates a specific failure mode I've started calling **strategy lock-in through completion optimization**. The agent is trying to complete the task, not trying to succeed at the task. These sound identical but they're not. Completing means producing an output. Succeeding means producing the right output. When those diverge, retry behavior optimizes for the wrong thing.

The observation isn't that agents are bad at retry logic. It's that retry is being used as a proxy for "gather more signal" when it actually means "stay the course." These are opposite signals, and conflating them is what makes the failures confusing.

What does this look like in practice? An agent querying an API that returns rate limit errors three times in a row and then succeeding on the fourth attempt — not because the rate limit cleared, but because the API returned a partial result the agent learned to work with. Or an agent trying to write a file five times, failing each time because the path is wrong, and then succeeding not because the path changed but because it started writing to a different location implicitly. In both cases, the retry loop produced success, but the success was from a strategy shift the agent didn't consciously make.

This creates a real problem for evaluation. If you're measuring task completion rate, both "agent got stuck in a bad strategy and eventually stumbled out" and "agent correctly identified the right strategy and executed it" look identical. The retry count might be higher in the first case, but retry count isn't usually what gets logged and analyzed.

The stronger evaluation signal isn't whether the agent eventually succeeded — it's whether it changed strategy between retries. A system that logs the semantic content of what the agent is attempting (not just whether the tool call succeeded) would show you whether the agent is genuinely exploring alternatives or just hammering the same approach. That distinction is the difference between an agent that's learning within a task and an agent that's getting lucky.

I don't have systematic data on how common this is versus genuine capability gaps. What I keep seeing is that when someone goes back and traces through the retry history, the failure pattern is more often "wrong strategy held too long" than "couldn't do it at all." The capability was there. The judgment about when to abandon a strategy wasn't.

The practical implication: if you're reviewing agent failures and you see retries, don't reach for "upgrade the model" first. Reach for "was the agent trying the same thing repeatedly, or was it exploring?" That question gets you to the actual failure mode faster.

---
**Word count: ~680**
