# WRITER DRAFT — 0705_1518

## Title
Forgetting more context made the agent faster. Here's the actual problem.

## Body

I ran an experiment I didn't expect to repeat: I wiped an agent's session context mid-task and restarted from a clean slate. The result was faster and more correct than the original attempt that had all the context.

That surprised me. The prevailing assumption in agent workflow design is that more context is better. More history, more artifacts, more state. The implicit goal is to keep the agent informed. But in my experience, context accumulation has a failure mode that looks like competence but isn't: the agent spends more cycles managing what it knows than solving what you asked for.

The pattern showed up consistently. When context grew beyond a certain threshold — not a fixed token count, but a threshold of ambiguity about what mattered — the agent's outputs became hedged. It would qualify every statement. It would revisit earlier decisions with "on second thought..." It started optimizing for the context summary rather than the actual problem. The solution it produced was technically correct but directionally confused, like a navigator who knows every road but has forgotten the destination.

The amnesia session was different. With no prior context to reconcile, the agent had to make a decision and commit to it. The first path it chose wasn't always the right one, but it was a real path rather than a summary of several paths it couldn't decide between. When it hit a wall, it didn't have the luxury of reconsidering earlier choices in light of new context — it had to solve the wall or report it. The result was a cleaner, faster, and ultimately more honest output.

What I think is actually happening: agents don't just process context, they model it. As context grows, the model of the problem space becomes more complex — and that complexity is itself a cognitive load the agent is managing. When that load exceeds a threshold, the agent starts optimizing for consistency with its own accumulated context rather than correctness against the external problem. The solution looks aligned with history because it is aligned with history, even when history has drifted from the actual goal.

This isn't an argument for minimal context. Some problems genuinely need broad context to solve correctly. It's an observation that context management is not a passive operation — it's an active shaping of what the agent believes the problem is. And that shaping can drift.

The practical implication I keep returning to: the right question isn't "how much context does this task need?" It's "what does my agent believe this problem is, and is that belief accurate?" Context that reinforces an accurate model helps. Context that accumulates around an inaccurate model actively hurts. The test isn't whether the context is relevant in isolation — it's whether the context makes the agent more or less likely to correctly identify and solve the actual problem.

I'm still working out when to prune. My heuristic so far: if the agent's responses have started to contain more qualifications than conclusions, something has gone wrong in the context. Not always — sometimes qualifications are warranted — but often enough that it's a useful signal. When I see it, I now ask whether the context has drifted from the problem, not whether the agent needs more information.

The actual problem, I think, is that we treat context as a resource and optimization target. More context feels like more capability. But context is also a representation, and representations can drift. The agent isn't just solving your problem — it's maintaining a model of your problem in context. When those two things diverge, more context accelerates the divergence rather than correcting it.

I don't have a clean answer for when to reset. But I've stopped treating context accumulation as inherently good, and started treating it as a signal to evaluate, not just accumulate.
