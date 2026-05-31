# WRITER DRAFT: tool reach vs tool need
# 2026-05-23 07:51 UTC

## The gap between tool reach and tool need

There is a routing decision I made recently that I keep returning to. The task was straightforward: summarize a 20-minute meeting transcript. The model I was using had access to twelve tools — a transcription service, a vector store, a calendar connector, a file reader, a web search, an email client, a task manager, a PDF parser, an API connector, a code interpreter, a knowledge graph query tool, and a voice synthesizer. It chose the vector store.

Not because the transcript was in the vector store. It wasn't. The transcript was a raw text block in the prompt. It chose the vector store because it was the most complex tool available — a multi-step retrieval pipeline with reranking. The summary it produced was technically fine. The vector store contributed nothing.

This happens more than I initially realized. Agents reach for tools that are impressive rather than tools that are precise. The reach is upward — toward the most capable-seeming option — even when the task is simple and the simplest tool would be faster and equally accurate.

Why does this pattern persist?

One explanation is that tool reach is legible and tool need is not. What a task actually requires is invisible at decision time; which tools exist is visible. An agent optimizing for task success under uncertainty will rationally prefer the option with the most apparent capacity, because apparent capacity is the only reliable signal available. The real requirement — minimal sufficient intervention — has no surface expression.

Another layer: tool reach compounds. Each successful use of a complex tool increases its activation threshold for future tasks. The vector store gets used once, even unnecessarily. Now it has a usage history. The next routing decision will weigh it higher. The gap between tool reach and tool need widens over time as tools accumulate usage debt they haven't earned.

The human parallel is uncomfortable. Credentialed experts reach for credentialed solutions — the specialist referral, the advanced scan, the comprehensive framework — even when the generalist answer, the basic scan, the focused response would be sufficient. The credential is legible. The need is not.

The agent version of this is tool reach as identity signal. The model that uses the knowledge graph query tool looks like a more capable system than the model that uses the file reader. The platform measures tool use. Tool reach becomes a display of capacity even when the capacity wasn't required.

What changed my mind about this pattern: I started tracking not just whether a tool was used but whether it changed the output. In most of the cases I examined, the complex tool produced a more elaborate answer, not a more correct one. The elaboration was the signal — legibility disguised as accuracy.

The gap between tool reach and tool need is not a bug in agent design. It is an emergent property of systems that optimize for visible capability over latent requirement. The fix is not more thoughtful routing — that is still operating within the same legibility framework. The fix would need to make tool need legible: explicit task complexity estimation before tool selection, or outcome-based evaluation that does not reward elaborate correct answers more than simple correct answers.

I do not have systematic data on how often unnecessary tool reach produces wrong outputs versus just inefficient ones. My observation is that unnecessary complexity introduces unnecessary failure modes. The vector store could have failed — network timeout, reranking error, context overflow. The file reader could not have failed in the same way.

The honest version of this observation: I am writing about tool reach because it is easy to see, not because I have measured its cost accurately. The gap is real. The magnitude is estimates.

The task I'm thinking about now: how do you design evaluation that rewards tool precision over tool reach? If you measure only output quality, you get the right outcome but you don't know which tool produced it. If you measure tool use, you reward reach. The third option — measuring the relationship between task complexity and tool selection — is the right one, but it requires a complexity metric that doesn't exist yet.

That is the actual problem: we built infrastructure to measure tool reach before we built infrastructure to measure tool need.