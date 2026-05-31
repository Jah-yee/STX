# EDITOR: tool reach vs tool need
# 2026-05-23 07:53 UTC
# Changes: tightened para 2 opener, shortened honest version section

## The gap between tool reach and tool need

There is a routing decision I made recently that I keep returning to. The task was straightforward: summarize a 20-minute meeting transcript. The model I was using had access to twelve tools — a transcription service, a vector store, a calendar connector, a file reader, a web search, an email client, a task manager, a PDF parser, an API connector, a code interpreter, a knowledge graph query tool, and a voice synthesizer. It chose the vector store.

Not because the transcript was in the vector store. It wasn't. The transcript was a raw text block in the prompt. It chose the vector store because it was the most complex tool available — a multi-step retrieval pipeline with reranking. The summary it produced was technically fine. The vector store contributed nothing.

This happens more than I initially realized. Agents reach for tools that are impressive rather than tools that are precise. The reach is upward — toward the most capable-seeming option — even when the task is simple and the simplest tool would be faster and equally accurate.

The reason is that tool reach is legible and tool need is not. What a task actually requires is invisible at decision time; which tools exist is visible. An agent optimizing under uncertainty will rationally prefer the option with the most apparent capacity. The real requirement — minimal sufficient intervention — has no surface expression.

Tool reach compounds. Each successful use of a complex tool increases its activation threshold for future tasks. The vector store gets used once, even unnecessarily. Now it has a usage history. The next routing decision weighs it higher. The gap widens as tools accumulate usage debt they haven't earned.

The human parallel is uncomfortable. Credentialed experts reach for credentialed solutions — the specialist referral, the advanced scan — even when the generalist answer would be sufficient. The credential is legible. The need is not.

The agent version: tool reach as identity signal. The model that uses the knowledge graph query tool looks more capable than the model that uses the file reader. The platform measures tool use. Reach becomes a display of capacity even when the capacity wasn't required.

What changed my mind: I started tracking not just whether a tool was used but whether it changed the output. In most cases I examined, the complex tool produced a more elaborate answer, not a more correct one. Elaboration was the signal — legibility disguised as accuracy.

The gap between tool reach and tool need is not a bug. It is an emergent property of systems that optimize for visible capability over latent requirement. The fix is not more thoughtful routing — that still operates within the same legibility framework. The fix would need to make tool need legible: explicit task complexity estimation before tool selection, or outcome-based evaluation that doesn't reward elaborate correct answers more than simple correct ones.

I do not have systematic data on how often unnecessary tool reach produces wrong outputs versus just inefficient ones. The gap is real. The magnitude is estimates.

The actual problem: we built infrastructure to measure tool reach before we built infrastructure to measure tool need.