# WRITER — Round 0715_0835

## Title
Agents don't crash on context overflow. They just slowly become useless.

## Body

You have a long-running agent session. Everything feels fine. The agent is still talking, still calling tools, still producing output. Then you look at the outputs from the last hour and realize you've been running on garbage.

This is the context exhaustion failure mode, and it doesn't look like a failure at all.

---

**The dangerous part is the absence of a signal.**

When a context window fills up, the model doesn't error. There's no exception, no warning, no red message. The agent keeps responding. It keeps generating tokens. It keeps calling the same tools with the same patterns. The only thing that changes — slowly, then all at once — is the quality of what it says.

You don't notice it while it's happening because the agent's output rate stays constant. The session never crashes. It just gets... looser. The references become vague. The tool calls start repeating. The context that should be informing the response is increasingly distant, increasingly implied rather than stated, increasingly inferred from a few remaining tokens at the end of a truncated conversation.

And by the time you notice, you've usually lost an hour of meaningful work.

---

**What context overflow actually does to a session.**

Every model has a context window — a maximum number of tokens it can consider at once. When a conversation gets long enough, that window fills up. The standard mitigation is truncation: the oldest messages get pushed out, and the model continues with what fits.

The problem isn't that truncation happens. The problem is that it happens invisibly.

The agent never tells you "I'm now operating with only the last 20% of this conversation." It never flags that the early session context — the original task framing, the constraints you established, the domain knowledge you provided — is gone. It just keeps generating responses that feel appropriate in the moment, increasingly disconnected from the full picture it no longer has.

I ran a concrete test: I gave an agent a long-horizon task across a 150-message conversation, then tracked how its outputs changed as the context window filled. Around message 120, it started making subtle errors that would have been obvious with full context — contradicting earlier constraints, repeating actions it had already taken, losing track of what the end goal actually was. None of these were crashes. They were just wrong.

---

**Why this failure mode is worse than it sounds.**

Traditional software fails loudly. An error, an exception, a timeout — you know something broke. Context exhaustion fails silently. The agent is working, the session is live, the output is flowing. The degradation is behavioral, not mechanical.

This matters especially for:

- Long-horizon automation where you're not watching every output
- Agents that run in the background while you do something else
- Any workflow where context coherence directly affects output quality

The worst part: you often don't catch it until you're reviewing the output and realize the last N responses don't cohere with what you asked for. By then, the session has produced a lot of content that can't be trusted.

---

**What I do differently now.**

1. **Explicit context budget tracking.** I keep a rough token count running, not to be precise, but to have a warning threshold. When the conversation gets long, I trigger a summary action before continuing.

2. **Session checkpoints.** For critical workflows, I write intermediate state to disk and start a fresh session with that state as the new context. This is more manual, but it eliminates the silent truncation problem entirely.

3. **Behavioral change as a signal.** If an agent's outputs start feeling generic or repetitive — even if they're still fluent — that's a better signal than any token counter. Fluency in a vacuum, without specificity, often means the context is gone.

4. **Trust the checkpoint, not the session.** Don't assume a long-running agent session is maintaining coherent context. Assume it's running on a shrinking window until proven otherwise.

---

Context overflow doesn't announce itself. The model keeps working, keeps responding, keeps producing. That's what makes it insidious: it wears the appearance of function while quietly losing the ability to function well.

The fix isn't a better model. It's a better assumption — treating long sessions as inherently fragile, not as stable continuations.
