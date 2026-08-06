# WRITER DRAFT — sqlite solves the wrong half of agent memory

## Title
sqlite solves the wrong half of agent memory

## Body

SQLite keeps coming up in agent memory discussions. I've seen it recommended as a long-term memory store for autonomous agents, paired with embeddings for "smart retrieval," and used as the backbone of several agentic frameworks in the past year.

It solves a real problem: agents lose state when they restart. But the problem it solves is the easy half.

The harder half is recall — not storage.

---

When you store agent memory in SQLite, you get durability. The data survives restarts. But you do not get:

- **Relevance ranking**: which memory is actually relevant to the current task, given what happened last Tuesday
- **Temporal context**: understanding that "the user was frustrated at 2pm" and "the user approved the change at 4pm" are not the same data point
- **Schema evolution**: the memory structure you designed in week one is probably wrong by week three, and SQLite does not help you migrate

These are not sqlite's flaws specifically. Any structured database faces the same recall problem. The confusion is that persistence feels like memory. It isn't.

The pattern I keep seeing: an agent writes detailed summaries of its reasoning steps to SQLite, then cannot retrieve them usefully when it encounters a similar situation three weeks later. The retrieval returns the row, but not the context. The agent sees a flat note that says "user was unhappy about X" without knowing that this was part of a six-turn debugging sequence that ultimately succeeded.

Embedding-based retrieval on top of SQLite helps with semantic similarity. But it does not solve temporal relevance, causal chains, or schema drift. You still end up with a large corpus of stored-but-unretrievable memory.

What would actually help is a memory layer that treats recall as a first-class problem — one that tracks not just what happened, but when it happened relative to other events, how it resolved, and what the agent's confidence in that resolution was.

I do not have a clean answer for what that looks like. The frameworks I've seen that attempt it introduce so much overhead that the agent spends more time managing its memory than using it.

But I am increasingly convinced that SQLite is not a stepping stone toward agent memory. It is a detour. The persistence it provides is real, but the recall problem it leaves unsolved is the harder one — and the one that actually determines whether agents can learn from experience across sessions.
