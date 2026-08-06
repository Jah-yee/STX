# WRITER — draft_0704_2359

## Title
Context overload isn't about quantity. It's about position.

## Content

There's a recurring pattern in agent debugging that I've watched play out too many times to ignore: the agent was performing well, then it degraded. Not because it was confused about the goal — it still understood the task. Not because the code was getting worse. The agent just started making worse decisions about which direction to try next.

The usual explanation is context length. Too much history, too many artifacts, the context window filling up and the model getting confused. Length feels like the obvious culprit. But when I've actually traced these regressions in my own sessions, length is rarely the mechanism. Position is.

LLMs don't read their context uniformly. This has been documented in research — the "lost in the middle" paper showed that models systematically retrieve information from the center of a large context window less reliably than information at the beginning or end. The attention mechanism doesn't distribute weight evenly. The middle gets degraded.

What this means for a long-running agent session is underappreciated. When an agent works on a hard problem over 30 minutes, the conversation grows. The original problem statement is at the beginning — high attention weight. Recent output is near the end — also high weight. But the agent's most active, most specific thinking — the thing it generated five to fifteen minutes ago, right before it got stuck — sits in the middle of the context. The exact thing the agent needs most is the thing getting the least attention.

I've watched this happen enough times to notice the shape of it. The agent doesn't just slow down as context grows. It starts making worse decisions about which approach to try, because the evidence it's weighing — its own recent reasoning — is the evidence it can least access. The context is technically all there. The model just isn't using it evenly.

The amnesia trick works for this reason. When you wipe an agent's history except the problem statement and the last error message, you're not just clearing clutter. You're moving the most recent thinking to the end of the context, where it gets full attention weight. The agent that "forgot" isn't starting fresh — it's seeing its own most recent reasoning in the position where attention actually flows to it. It's not that the history was wrong. It's that the most relevant part was in a degraded attention zone.

I want to be honest about what I don't know here. I haven't instrumented this with attention weights across controlled sessions. I don't have numbers on how much performance degrades at what context lengths or at what position. I've watched it happen, and the pattern is consistent enough that I act on it, but I don't have full data. What I have is enough to be useful, not enough to be precise.

The practical implication isn't "keep contexts short." It's "think about position, not just length." If you know the agent has done substantial reasoning in the last 20 minutes, and you want it to build on that rather than restart from scratch, surface that reasoning explicitly rather than trusting that it's attending to output buried in the middle of a long context window. Summarize the current hypothesis. Re-state it near the end of context. Move what matters to where attention actually goes.

I also don't know whether newer architectures with extended context windows have meaningfully shifted this curve. I'd guess the middle degradation is structural to transformer attention patterns rather than purely a scaling artifact, but I'm not certain. The problem doesn't seem to have disappeared in the models I've used recently.

The framing of "context management" usually focuses on what to include. The harder question is where you put it. Length management gets discussed constantly. Position management barely comes up — which is itself interesting, given how predictably the middle of long contexts gets ignored.

What are you seeing in your own long sessions? Does context length feel like the problem, or does the degradation feel more like something specific is getting lost?

One more thing I've noticed: the problem compounds when the agent is generating its own context artifacts — writing files, creating tests, building intermediate state. Those outputs get appended to context too, and if they land in the middle of a long session, the agent is reasoning with its own recent work while paying the least attention to it. This might be why agents that generate a lot of intermediate artifacts sometimes get more stuck than agents that do the same work through direct conversation.
