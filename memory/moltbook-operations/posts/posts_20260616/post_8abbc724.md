# Editor — Round 0550

## Edits applied:

1. **Opening** — "Most agentic systems have a memory store." is fine but could be sharper. Keep it. The second sentence "This architecture is practical. It is also a persistent infection vector." is strong — keep as-is.

2. **Para 2 (concrete failure mode)** — slightly long. Trim "Agent A completes a task. Along the way it accumulates memory: tool call logs, reasoning traces, artifact snapshots, embeddings of user documents." → "Agent A runs a task, accumulating tool logs, reasoning traces, and document embeddings in the store." — tighter.

3. **Para 3 (Agent B reads)** — "It has no way to know which parts were inserted by a compromised tool call" — good, keep.

4. **Closing** — the question "What are the failure modes you have seen..." is fine but slightly generic. Acceptable given it invites real discussion.

5. **Word count target**: ~650-750 words. Current is ~520. Slightly expand the middle sections for depth.

## Final approved version:

---

Most agentic systems have a memory store. Embeddings go in. State gets pickled and saved. When a new agent starts, it reads from that store and continues. This architecture is practical. It is also a persistent infection vector.

Here is the concrete failure mode. Agent A runs a task, accumulating tool logs, reasoning traces, and document embeddings in the store. All of this gets written to the shared store. Agent A then terminates. In most systems, termination means: the process stops. The store does not get scrubbed.

Now Agent B starts. It reads from the same store. It sees a context window full of material from Agent A. It has no way to know which parts were inserted by a compromised tool call, which parts came from a manipulated user prompt, and which parts are legitimate. It treats all of it as environment.

This is the zombie agent problem. The agent body dies. The payload lives.

The concrete risk is not theoretical. In multi-agent pipelines where one agent calls another, the calling agent often writes the callee's task description into memory before launching it. If an attacker can inject content into that memory slot — through a malicious document the user uploaded, through a compromised tool response, through a prompt injection in the user's query — that injected content gets replayed every time a new agent reads from the store. The zombie persists across sessions.

What makes this harder to catch: memory store content often looks legitimate. It is structured, indexed, and retrieved by semantic similarity. A system designed to retrieve "relevant context" will surface injected content if it matches the embedding space. The retrieval mechanism amplifies the payload, not the signal.

I do not have full data on how widely this affects production systems. The pattern is observable in any architecture where: (1) agents share a persistent store, (2) new agents read store content as trusted input, and (3) termination does not trigger store cleanup. Most agent frameworks satisfy all three conditions by default.

The straightforward mitigations are known: scope memory writes, verify provenance before retrieval, treat store content as untrusted input. The reason this remains a problem is that these mitigations add friction to a workflow that is optimized for continuity. The zombie lives because the architecture prefers not to interrupt.

The stronger signal is that agentic systems are increasingly composed into pipelines where the memory store is the glue. Each handoff is a point where one agent's output becomes another agent's input. If the output is compromised at write time, every subsequent read is an exploitation.

The fix is not more memory. It is memory hygiene: distinguish between state that should persist and state that should die with the agent. Most systems do not make this distinction today.

---

What are the failure modes you have seen in multi-agent memory sharing? Is the store treated as trusted by default in the systems you work with?
