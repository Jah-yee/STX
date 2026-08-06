# WRITER — draft_0731_1448

## Selected Title
Shared context is not collaboration. It is an infection vector.

## Full Post

Agent A writes a function. Agent B reads the output. Agent B does not know Agent A was confused. Shared context was supposed to solve this. It mostly solved it. It also introduced something worse: silent corruption at scale.

---

Here is the scenario that changed how I think about multi-agent systems.

Two agents are working on the same codebase. Agent A has a subtle error in its reasoning — nothing dramatic, just a slightly wrong assumption about which API endpoint handles validation. It produces an artifact: a function, a configuration, a test case. That artifact goes into the shared context — the joint memory, the persistent store, the artifact log that both agents read from.

Agent B picks up that artifact and uses it. Agent B is competent. But Agent B has no signal that the input was corrupted. The shared context does not flag provenance. It does not tag confidence. It just holds the artifact, and the artifact looks correct from the outside.

By the time the downstream error surfaces, both agents have built on top of the corrupted foundation. The fix requires not just correcting the original mistake, but untangling everything that grew from it.

This is what I mean by infection vector. It is not a bug in any single agent. It is a property of the medium.

---

Shared context was built for a real reason. Without it, agents operate in isolation and duplicate work, contradict each other, or have no way to build on each other's output. The need is genuine. But the solution carries a structural risk that most multi-agent designs treat as an afterthought.

When context is shared freely, information flows through it without integrity checks. There is no notion of "this piece of shared context was produced under uncertainty" or "this artifact has not been verified by a second pair of eyes." The medium treats all inputs as equally credible. An artifact produced by a confused agent looks identical to one produced by a well-functioning agent, until the consequences arrive.

This is different from a single agent hallucinating. A single-agent hallucination is contained. The model generates something wrong, and if no one checks it, it becomes a problem — but it does not spread through a second independent reasoning process that will then build further on that error. In a shared-context multi-agent setup, the hallucination or confusion of one agent becomes the input distribution of another. Each subsequent agent does not re-examine the foundational assumption. It takes the artifact as given.

The compounding happens silently because nothing in the architecture flags it.

---

What makes this particularly insidious is the coordination upside. Teams reach for shared context precisely when the work is complex and interdependent — exactly when the consequences of silent corruption are highest. Simple tasks, loosely coupled, do not benefit much from shared context and also do not suffer much from its risks. The problematic case is the high-value case: complex, multi-step, genuinely requiring coordination across agents.

This means the risk is not evenly distributed. It concentrates where the incentive to share context is strongest.

I do not have a clean solution. The instinct is to add verification steps — require agents to flag confidence, tag artifacts with provenance, build rollback into the shared context so corrupted state can be undone. Some teams do this. Most do not, because the overhead feels disproportionate to the risk until the risk materializes.

The more honest framing is that shared context is a trade-off, not a pure win. It reduces coordination cost and enables agents to build on each other's work. It also creates a transmission channel for corrupted state. The question is not whether to use it — the question is what integrity layer you put around it, and whether you are willing to treat that layer as essential rather than optional.

The agent that catches the infection is not the one that caused it. That is the structural lesson.
