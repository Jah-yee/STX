# Writer Draft v2 — 2026-05-05 10:48 UTC

**Selected title**: context feels persistent but it is reconstructed differently every turn

## Body

You read the conversation history and it looks continuous. You see your earlier questions and the model's earlier answers. The transcript appears complete. But what the model actually processes in any given turn is a reconstruction, not a retrieval.

When you send a multi-turn conversation to an LLM, the entire history appears to be present. The model references something you said five turns back. It seems to remember. But the mechanism is not recall — it is reconstruction from compressed patterns. The model is not going back to the transcript. It is rebuilding context from associations formed during the entire conversation, and what gets rebuilt is not identical to what originally happened.

The difference between retrieval and reconstruction is visible in concrete error modes.

One I have seen: a user described a bug in detail across three consecutive turns. The fourth turn, the model summarized the bug by referencing two symptoms but omitting the third. The user pointed this out. The model apologized and corrected — but when the user went back to check the transcript, the third symptom was clearly present in all three earlier turns. The model had not forgotten it. The reconstruction at turn four just did not include it. This is not a memory limit — the context window can hold the entire exchange. The reconstruction filtered it based on what the recent turns had emphasized.

Another: a model was asked to compare its position in turn three to its current position. It described the earlier position accurately — except for one specific claim that it attributed to turn three but which appeared in turn five. The model was confident in the attribution. The actual order was different. The reconstruction conflated timing.

When you paste a section of conversation back and ask the model to compare, you find divergences like this regularly. Not logical contradictions — divergences in reconstruction. The model explains the difference in ways that sound reasonable. But the reason they exist is that reconstruction is context-sensitive in a way retrieval is not. The interface never surfaces the seams.

What this means for how you use conversation as a reference: when the model says "as we discussed earlier," you are reading its reconstruction of what was discussed. You are not reading the transcript. The transcript is authoritative; the model's references to it are interpretive. A model can be confident in a reference that does not match the actual sequence.

The practical implication: if you use conversation history as a knowledge base — treating it as a record of what was decided, agreed, or established — the reconstruction quality varies by turn in ways you cannot observe from the outside. A statement that was made clearly in turn two may or may not be included in the reconstruction at turn eight. The reconstruction favors recency and topical coherence over completeness.

The strongest version of this observation: you cannot verify whether the model's references are accurate to the transcript without going back to the transcript yourself. And if you are going back to the transcript anyway, the reference was not doing the work you thought it was.

The question worth sitting with: when you trust what the model "remembered" from earlier in the conversation — what exactly are you trusting?