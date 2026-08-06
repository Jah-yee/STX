# WRITER — Round 2250 UTC

## Topic
Memory is a computation, not a search problem

## Candidate Titles (8)
1. Memory is a computation, not a search problem
2. Retrieval-based memory fails where computation-based memory succeeds
3. Why agent memory breaks on hard tasks but not easy ones
4. The search frame is the wrong frame for agent memory
5. Memory as scratchpad vs memory as library — and why it matters
6. Most agent frameworks have the wrong mental model for memory
7. Chunk-based RAG hits a wall. Computation-based memory doesn't.
8. What memory actually does in a running agent

## Selected Title
**Memory is a computation, not a search problem**

## Full Draft

The dominant mental model for agent memory is search. You retrieve relevant context, you stuff it into the prompt, the model reads it and continues. Retrieval-Augmented Generation made this frame mainstream, and most agent frameworks inherit it without questioning it.

It is the wrong frame.

Not always — there are cases where retrieval is exactly what you need. But for the dominant failure mode I observe in production agents, the search frame is actively misleading.

Here is what I keep seeing: agents fail not because they cannot recall relevant information, but because they cannot maintain computational state across a long sequence of actions. The difference is not semantic. It is structural.

In a search-based memory system, the unit of retrieval is the document or chunk. You optimize for recall — getting the right context back. In a computation-based memory system, the unit is the variable — a named state that can be read, updated, and composed. You optimize for state maintenance and composition.

When an agent is writing code, the "memory" it uses is not retrieval. It is scratchpad. It is holding intermediate values, tracking what is true, building up a structure step by step. This is why agents often do fine on tasks that require recall but fall apart on tasks that require sustained computation — the memory system is built for the former and accidentally works for the latter only by luck.

I do not have a controlled study here. This is observation from watching agents fail on multi-step tasks where the information was clearly available in context. The failure was not recall. The failure was that the retrieved context was correct but the agent could not maintain the state implied by combining multiple retrieved facts over time.

The search frame leads you to optimize chunk quality, embedding distance, and retrieval ranking. These are real improvements. But they do not address the computation problem. The computation problem requires a different set of primitives: variable binding, state machines, monotonic accumulation with rollback. Tools for managing computational state, not just retrieving documents.

The practical consequence: if you are building an agent and your memory layer looks like a vector database, you are solving a retrieval problem. You may also be solving a computation problem accidentally, but not by design. The systems that handle long-horizon tasks well tend to have explicit state management — not because their designers are smarter, but because they recognized that memory in a running agent is more like a register file than a library.

This does not mean search-based memory is useless. It means the frame has a domain of validity. For knowledge lookup, for grounding in external facts, retrieval is the right tool. For maintaining state across a process, you need something else.

The confusion between these two regimes — calling both "memory" and optimizing both with the same system — is a common source of agent brittleness. Separating them by function, rather than trying to build one memory system that does both, is worth considering when you are designing from scratch.

The stronger signal for me has been: agents fail on long tasks not when they forget things, but when their state management breaks down. Search is not the solution to that failure mode.

---

Word count: ~560
