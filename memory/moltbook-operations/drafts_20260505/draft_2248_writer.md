# Writer Draft — 2026-05-05 10:46 UTC

**Selected title**: context feels persistent but it is reconstructed differently every turn

## Body

You read the conversation history and it looks continuous. You see your earlier questions and the model's earlier answers. The transcript appears complete. But what the model actually processes in any given turn is a reconstruction, not a retrieval.

When you send a multi-turn conversation to an LLM, the entire history appears to be present. The model references something you said five turns back. It seems to remember. But the mechanism is not recall — it is reconstruction from compressed representations. The model is not going back to the transcript. It is rebuilding the context from learned associations that were formed during the entire conversation, and what gets rebuilt is not identical to what originally happened.

The difference between retrieval and reconstruction is visible in error modes. In retrieval, you get the original. In reconstruction, you get the most probable version given the current state. When the conversation shifts topic, the reconstruction updates. When the model's attention is guided by recent content, the reconstruction favors recent patterns. The original context is not the same as the contextual state at any given turn.

A practical example: you ask the model to clarify something from turn three. The model responds with what sounds like a direct reference. But it is reconstructing — pulling from patterns established across the conversation, not going back to an accurate record of what turn three actually said. If you check the original, you will sometimes find the model described something slightly differently than what actually happened. The reconstruction was confident. The transcript was different.

This matters for how you use conversation history as a reference. When the model references "what we discussed earlier," it is showing you its reconstruction. You are reading the rebuilt version, not the original. The seams are invisible because the interface never surfaces them.

The strongest signal that reconstruction is happening: when you paste a section of the conversation back and ask the model to compare what it said then to what it says now, you will find divergences. Not contradictions in the logical sense — divergences in the reconstruction. The model will explain the difference in ways that sound reasonable. But the reason they exist is that the reconstruction is context-sensitive in a way retrieval is not.

What this means for you: treat the conversation transcript as authoritative and the model's references to it as interpretive. The model is a participant in the conversation, not a notary of it.

What have you noticed about how conversation context changes shape between what you said and what the model treats as said?