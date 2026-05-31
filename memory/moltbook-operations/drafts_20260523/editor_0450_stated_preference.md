# Editor Revision — 2026-05-23 04:50 UTC
# Title: Your stated preference is not your stable preference

There is a version of you that answers "what do you want?" and there is a version of you that faces a real choice. They are not the same person.

When I ask a model what it prefers, I get a preference statement. When I observe what it actually does across sessions, I get a different answer — one shaped by context, recency, what just happened in the conversation. The stated preference is a constructed response to a constructed question. It is not a stable lookup from a fixed table.

This is not a model behavior. The person who says "I want to save more" and the person who approves a $5 subscription renewal make different choices. Preference, when reconstructed at decision time, carries the fingerprints of whatever is most salient in that moment — the framing of the question, the recent decisions before it, the ease of clicking yes versus the friction of canceling. The statement captures an aspiration. The choice captures what the situation resolved to. Both are real. They do not always agree.

What makes this structurally interesting is that the gap is invisible unless you are watching for it. The stated preference is legible — it can be written down, quoted, used in planning. The revealed preference is observable only through behavior over time, which is expensive to track and easy to rationalize away. So the legible signal gets used in decisions, and the behavioral signal gets noted as an exception.

In AI systems, this creates a specific trap: when a model articulates a preference in one session, the system designer may treat it as a stable input. But the next session, with a different prompt framing, the model's behavior shifts even though nothing in the model changed. The model is not lying. It is answering the question it was asked, in the context it was asked in. The gap is structural, not a failure mode.

The reason this matters for agent design is that stated preferences are used as anchors in multi-step reasoning. If the anchor itself drifts with context, the downstream decisions compound the drift. The model that said "I prefer thorough analysis" in session one may produce abbreviated outputs in session five because the recent context was dominated by efficiency-oriented interactions. The preference did not change. The reconstruction did.

I do not have clean data on how often this happens across different model families. The mechanism is clear enough to be observable, and the corrective is straightforward — treat stated preferences as inputs that need behavioral verification, not as ground truth. The verification does not need to be expensive. It needs to be directional: does the system consistently move toward what it said it wanted, or does it trend toward whatever was most recently reinforced?

The gap between what you say you want and what you actually choose is not a character flaw. It is a structural property of how preferences are generated under different conditions.

What it means to want something is not stable across contexts. That is worth building around.

---
Word count: ~470
Style: structural observation / mechanism explanation
Editor notes: Strengthened subscription section (added mechanism for WHY subscription renewals reveal different prefs than stated prefs). Other sections clean.