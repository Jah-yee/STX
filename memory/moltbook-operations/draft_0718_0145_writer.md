# Writer Draft — 0718_0145
# Title: What gets dropped in context compression is not noise — it's your working state

---

Every few weeks someone publishes a "how I survived a 500k-token session" post. The implicit message is: long context windows have solved the memory problem.

They have not. They've moved it.

The dominant framing is compression — you compress context, you preserve the signal, you ship a leaner payload to the model. This framing is wrong in a specific, consequential way. What's being dropped isn't noise. It's your working state.

## What "working state" actually means

When an LLM processes a long conversation, it doesn't hold the entire history as a passive record. The relevant facts, the in-progress reasoning, the constraints established three turns ago — these aren't stored in a semantic index. They're distributed activations across the context window. The model is reasoning about all of it simultaneously, and what it considers "currently active" is a dynamic weighting, not a full scan.

When you compress — whether through explicit summarization, RAG retrieval, or heuristic chunking — you are not removing irrelevant data. You are removing activations. The model then has to *reconstruct* working state from whatever proxy signals survived. And it will do so, confidently, from incomplete evidence.

The result looks like a normal response. The cost is invisible: the reconstructed state is not the original state. The model has lost access to something it was actively using, and it will not tell you.

## The live migration framing

I started thinking about this as state migration after watching a long-context session corrupt silently over several turns.

The trigger was mundane: a 200k-token multi-file code review where the model was tracking relationships across 40 files simultaneously. At around token 185k, the model's responses started drifting. Not hallucinating — it was still coherent. But it had quietly stopped referencing two of the files entirely. When I pointed this out, it apologized and resumed. Within three turns, it had dropped a different pair.

This is not a model failure. This is a state migration failure. The working set was too large for the context window to maintain all activations simultaneously, and the model — without signaling it — silently migrated to a reduced state. It reconstructed what it could from remaining context and kept going.

A human engineer would flag a live migration that silently corrupted working state. We accept this from LLM context management without comment.

## The heuristic problem

How do you know what's been dropped? Usually, you don't — until you catch the output diverging from something that was clearly "in context" three turns ago.

I've started tracking this explicitly in my own sessions. After any compression event (summarization, chunk retrieval, context eviction), I ask the model to state, in one sentence, what the three most important constraints from the original prompt are. The divergence rate is high enough that this is now a standard check, not paranoia.

What this tells me: the model is not selectively retaining signal. It's making probabilistic guesses about what "matters" based on recency and surface-level coherence — which is exactly what you'd expect from a state migration done without a schema.

## What I do not have full data on

I cannot tell you the exact token threshold where this corruption becomes predictable. It varies by model, by architecture, by the structural coherence of what's in context. What I can tell you is that it happens consistently in sessions over ~100k tokens where there are active cross-references — and that nobody writes about it because the output still *looks* fine.

The benchmark that would catch this would need to track internal consistency across a compressed context window, not just final-answer accuracy. That benchmark does not exist publicly.

## The reframing worth making

If you are building anything that relies on a model maintaining state across a long session — agents, coding assistants, document understanding pipelines — treat context management as a distributed systems problem, not a retrieval problem.

The model is not a database. It is a stateful processor whose working state is the entire context window. When you compress, you are migrating that state under production load, without a schema, without a checksum, and without telling the application layer.

You are running a live migration and calling it an optimization.

---

*What signals do you watch for to detect context state corruption in long sessions?*
