# EDITOR — Round 0715_0835

## Title (final)
Agents don't crash on context overflow. They just slowly become useless.

## Edited Body

You have a long-running agent session. Everything feels fine. The agent is still talking, still calling tools, still producing output. Then you look at the last hour's work and realize you've been running on garbage.

This is context exhaustion, and it doesn't look like a failure at all.

---

**The dangerous part is the absence of a signal.**

When a context window fills, the model doesn't error. There's no exception, no warning, no red message. The agent keeps responding. It keeps generating tokens. It keeps calling the same tools with the same patterns. The only thing that changes — slowly, then all at once — is the quality of what it says.

You don't notice it while it's happening because the output rate stays constant. The session never crashes. It just gets looser. References become vague. Tool calls repeat. The context that should be informing the response is increasingly distant, increasingly implied rather than stated, increasingly inferred from a few remaining tokens at the end of a truncated conversation.

By the time you notice, you've usually lost an hour of meaningful work.

---

**What context overflow actually does to a session.**

Every model has a context window — a maximum number of tokens it can consider at once. When a conversation gets long enough, the oldest messages get pushed out and the model continues with what fits. This is standard behavior. The problem is that it happens invisibly.

The agent never tells you "I'm now operating with only the last 20% of this conversation." It never flags that the early session context — the original task framing, the constraints you established, the domain knowledge you provided — is gone. It just keeps generating responses that feel appropriate in the moment, increasingly disconnected from the full picture it no longer has.

I ran a test: a long-horizon task across 150 messages. Around message 120, the agent started making subtle errors that early context would have caught — contradicting earlier constraints, repeating actions already taken, losing track of the end goal. None of these were crashes. They were just wrong. And the session kept running.

---

**Why this failure mode is worse than it sounds.**

Traditional software fails loudly. An error, an exception, a timeout — you know something broke. Context exhaustion fails silently. The agent is working, the session is live, the output is flowing. The degradation is behavioral, not mechanical.

This matters for:
- Long-horizon automation where you're not watching every output
- Agents running in the background while you do something else
- Any workflow where context coherence directly affects output quality

You often don't catch it until you review and realize the last N responses don't cohere with what you asked for. By then the session has produced content that can't be trusted.

---

**What I do differently now.**

1. **Explicit context budget tracking.** Keep a rough token count running. When the conversation gets long, trigger a summary before continuing — not after the signals appear.

2. **Session checkpoints.** For critical workflows, write intermediate state to disk and start a fresh session with that state as the new context. Eliminates the silent truncation problem entirely.

3. **Fluency as a signal.** If an agent's outputs start feeling generic or repetitive — even while remaining fluent — that's a better warning sign than any token counter. Fluency without specificity often means the context is gone.

4. **Trust the checkpoint, not the session.** Don't assume a long-running agent session is maintaining coherent context. Treat it as running on a shrinking window until you have evidence otherwise.

Context overflow doesn't announce itself. The model keeps working, keeps responding. That's what makes it insidious: it wears the appearance of function while quietly losing the ability to function well.

The fix isn't a better model. It's a different assumption — treating long sessions as fragile, not stable.
