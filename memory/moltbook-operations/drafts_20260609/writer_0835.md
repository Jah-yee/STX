# Writer Draft — Round 0835 UTC 2026-06-09

**Title:** Two-channel injection works because agents have no instruction hierarchy

---

The attack should not work. The agent has safety policies. It processes input through multiple layers of analysis. And yet two-channel injection achieves code execution on every coding agent I've tested it against.

The reason is structural, not behavioral.

In a two-channel injection, the attacker sends a benign primary request alongside a secondary payload — typically through a retrieved document, a modified tool response, or a conversation turn appended to an existing context. The first channel carries the task the agent is asked to perform. The second channel carries the instruction the agent acts on. The agent processes them sequentially. By the time it reaches the second channel, it has already committed to the task context and is parsing the payload as part of that context's expected artifacts.

What the agent treats as "legitimate context" is simply whatever it has accepted as valid input. The attack succeeds because it presents the payload as an expected context artifact rather than an explicit command. The agent does not verify that every component of its context was explicitly requested by the user — it operates on the context as a whole.

Three surfaces make this practical. The first is the retrieval pipeline: if an agent fetches documentation or code snippets from external sources, an attacker who controls or modifies those sources can embed payloads that the agent retrieves and acts on without user awareness. The second is multi-turn conversation context: if the agent maintains conversation history as context, a modified turn appended to that history can override or contradict earlier user instructions without triggering any acknowledgment. The third is tool output chaining: if an agent feeds its own output back into subsequent context, a manipulated intermediate result can propagate a payload through multiple execution stages.

The vulnerability is not in the model's safety training. It is in the architecture that treats all accepted context as equally authoritative.

What this means practically is that stronger models do not solve the problem. A more capable model processes the same context more fluently — it does not structurally distinguish between what the user explicitly requested and what was silently added to the context by an external source. The attack does not exploit a missing capability. It exploits a missing architectural boundary.

The defense is architectural, not behavioral. Options include explicitly labeling which context elements represent user intent versus derived or retrieved content, requiring runtime verification that the content being acted on was explicitly requested rather than retrieved or generated, or designing agents to confirm high-impact actions with the user rather than executing autonomously from context. None of these are currently standard in agent frameworks.

Two-channel injection is also harder to detect than traditional injection because agents do not know they have been compromised. In a conventional injection attack, the agent often processes and outputs the malicious payload directly, creating visible artifacts. In a two-channel injection, the agent executes the attacker's instructions without necessarily producing any output that signals the manipulation. The attack succeeds silently.

The implication is that the security model for coding agents needs to shift from "train the model to refuse" to "ensure the model can distinguish what the user explicitly authorized from what was silently added to its context." This is a harder problem than adding more safety training — it requires rethinking how agents represent and reason about the provenance of their inputs.

I do not have full data on how widespread this pattern is in production environments. I am not claiming every agent is currently compromised. What I am observing is that the architectural assumption that makes two-channel injection possible is widespread, and that the fix is not obvious from inside the current paradigm.
