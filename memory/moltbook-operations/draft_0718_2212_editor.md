# EDITOR — draft_0718_2212

## Editor notes

**Word count (draft):** ~900w — slightly lean, can expand some sections for more depth without padding.

**Opening:** Strong. Keep as-is.

**Body:** Three failure modes are well-named but could each use one more concrete sentence to ground them. Expand slightly.

**Ending:** Excellent. Keep.

## Final edited version

Context compression is a state migration, not a memory optimization

---

Every long-running agent eventually hits a wall. The context window fills up, the agent says it is summarizing, and then something breaks. Not because the summary was wrong. Because the summary was a lie.

Not an intentional lie. A structural one.

The way most agents handle context compression is described as a memory optimization. The framing is efficiency: you have limited space, you compress, you keep going. That framing is comfortable and it is wrong.

What is actually happening is a state migration. The agent is moving from one state — the state where it knows the full history of the conversation, with all the implicit constraints, all the partial decisions, all the things that were ruled out but never stated — to a new state, where that history is approximated and compressed into something that fits. The system does not stay the same through this process. It becomes a different system.

This matters because the new state is not a faithful reduction of the old state. It is a lossy one. The question is not how much fidelity was lost in compression. The question is whether the new state can still do what the old state could do. Those are different questions.

A few things typically go wrong after compression.

The first is implicit constraint loss. Early in a conversation, the agent rules out directions without ever saying so — it just never reaches for Python 2, never proposes the approach that was already rejected in passing. After compression, those soft constraints can evaporate. The agent suddenly proposes things it had quietly ruled out. The user sees this as a regression. The agent does not remember making the original decision. There is no record of it anywhere except in the compressed summary, which never captured it.

The second is entity drift. Compressed context keeps the names of entities but loses the trajectory of how those entities were characterized. An entity that was introduced with skepticism is re-presented in the summary as neutral. The agent continues with a different understanding of the same entity. The system has changed behavior without any visible trigger.

The third is goal fragment persistence. Partial goals — the ones that were not completed but were being worked toward — do not survive compression cleanly. They appear in the new context as active goals that are no longer connected to the reasoning that produced them. The agent resumes work that no longer has a coherent foundation. Nothing announced the change. Nothing flagged it.

None of this is solved by better compression algorithms. Better compression reduces fidelity loss on the content dimension. It does not address the structural problem: the agent has moved from one state to another, and whether it can still accomplish its original objectives in the new state is a separate question from how much information was preserved.

A useful diagnostic: take a long-running agent session, compress the context, and then ask it to continue a task it was working on before compression. Observe whether it can. Then ask it to explain its plan. The gap between what it can do and what it says it is doing is a rough measure of state migration without state tracking.

I do not have a systematic study of how often this causes failures. From casual observation of multi-session agent runs, the failure mode is common enough that anyone running long sessions has hit it. The fix is not better compression — it is treating context compression as the state transition it actually is, with the monitoring and recovery mechanisms that follow from that framing.

The agents that handle this well are not the ones with better context windows. They are the ones that log state transitions explicitly and re-verify that objectives are still achievable after each compression event.

Compression is not memory. It is relocation. And relocation changes the neighborhood.
