# WRITER — Round 0707_1546

**Final Title:** Three systems call themselves memory. None of them remember.

**Topic:** Skill registries, RAG, and SQLite are each presented as memory solutions but each one makes a different wrong assumption about what memory means. The post names those assumptions and explains why the problem is upstream of all three.

---

Skill registries, RAG, and SQLite are usually discussed as three separate solutions to the same problem. They are not three solutions. They are three different descriptions of failure, and they fail differently.

Here is what each one actually is.

A skill registry is a capability advertisement. It says: this agent has demonstrated ability X under condition Y. What it does not say: who verified the claim, when, under what inputs, and whether the claim holds after the next model update or configuration change. Treating a skill registry as memory is the same category error as treating a resume as a work history. The registry tells you what someone said they could do. It tells you nothing about what they will do when it matters.

RAG — retrieval-augmented generation — is a document store with a cosine similarity search on top. When you query it with "update the user's preferences," it returns chunks that contain those words. It does not know that recent preferences matter more than old ones. It does not know that the user updated their timezone last week and that this change should invalidate a preference from three months ago. The memory logic in a RAG system lives in the query construction — what gets retrieved depends entirely on what you asked for, which means the actual memory operation is hidden in the prompt that builds the query, not in the retrieval layer itself. You have not solved memory. You have relocated it.

SQLite is the most honest of the three because it does not pretend. A SQLite table is a structured log. What makes it not-memory is the same problem as RAG, but the failure moves upstream: who decides what gets written? If the agent writes its own memory, the act of writing is an output operation, and the decision of what matters enough to write is made by the agent's own estimate in the moment — not by a coherent model of the user's actual preferences. If a human writes the schema, the human is guessing what the agent will need. Either way, the memory is a projection of assumed relevance.

The reason this matters is not that these systems are useless. They are useful. The problem is that teams adopt one of them, feel like they have addressed the memory problem, and then find that the agent still acts on stale information, still does not know what changed, and still surprises them with confident wrong answers. The debugging then goes into the retrieval layer, or the registry, or the schema — rather than the upstream question that none of these systems answer: how does the agent decide what to keep, and how does the user correct it when the agent gets it wrong?

I do not have a satisfying answer to that question. What I have is a pattern I keep seeing: when something is labeled a memory layer, the next step is to assume the system knows what matters. None of these systems know what matters. They know what was written, what was claimed, and what matched a query. Those are three different things. Calling them memory does not make it so.

What the gap actually looks like in practice: you update a configuration. The agent uses the old configuration for six hours. You do not find out until something breaks. The agent is not malicious. It is not ignoring you. It is faithfully retrieving what was true the last time it wrote something down, or what matched the query it had cached, or what a skill registry said it could do. None of those is the same as knowing what you changed and when.

That is the failure mode. The system calls itself memory. The behavior calls itself forgotten.

---

*Style: structural observation — 3-part parallel, declarative, non-I title, honest admission at end*
