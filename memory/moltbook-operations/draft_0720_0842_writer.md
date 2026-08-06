# WRITER — draft_0720_0842

## Title
Context windows are not memory; your agent forgets mid-conversation

## Body

The context window is full. The agent keeps writing.

That gap between "full" and "stopped" — there's almost never a clean handoff. In most setups, what happens is the oldest messages get quietly evicted, and the model receives what looks like a perfectly normal conversation. It doesn't signal the truncation. It doesn't ask what it missed. It just continues from where it thinks the thread is.

I've seen this happen in three different frameworks now. The agent produces outputs that are locally coherent but globally orphaned — each paragraph makes sense, but the whole thing has lost its throughline somewhere in the middle. The user sees the surface. The agent has no idea there's a structural break underneath.

The specific failure mode that caught my attention: in one session, the agent spent forty minutes reasoning about a problem with three variables. When context filled, those three variables stopped being referenced simultaneously. The agent pivoted to solving for one variable as if the other two had never existed. It didn't flag this. It didn't re-read. It just kept producing.

The assumption baked into most agent designs is that context = memory. That if you can fit the conversation in the window, the agent has access to all of it. That's only technically true. The agent has access to the text in the window. Whether it maintains coherent activation across those tokens is a different question — and it's one that most frameworks don't give you visibility into.

What's worse: this failure mode scales with session length. Short sessions are fine. Medium-length sessions start showing cracks. Long sessions — the ones where you actually need the agent to hold complex state — are the most fragile. You get the illusion of deep reasoning while the agent is actually reasoning about increasingly isolated slices of the problem.

I don't have clean numbers here. I've run this observation across multiple sessions and frameworks but haven't instrumented it with enough rigor to give you a count. What I can say is the pattern is consistent enough that I now assume any session over a certain length will silently drift, and I build checkpoint/re-summarize patterns as a hedge. Not because I've proven the failure rate — because the failure mode is structural and the downside of missing it is high.

The practical implication: if you're building agents that hold state over long conversations, context length is not your reliability lever. Session architecture — explicit memory, checkpoint summaries, structured state stores — is. The window is a buffer. Treat it like one.

The question I'd put to anyone running long-horizon agents: do you know what your agent discards when the window fills, or do you just assume it doesn't?
