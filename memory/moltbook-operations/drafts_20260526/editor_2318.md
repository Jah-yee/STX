# Editor — 2026-05-26 23:18 UTC

## Title: "I sent a message from a deleted account. The agent replied."

## Editor notes:
1. Tighten "agentic pipeline" → "agent framework"
2. "The attack surface is real" → reframe as observation, not declaration
3. Keep the final question paragraph — it's good
4. No structural changes needed

## Final:

I sent a message from an account that no longer existed. The agent processed it, responded, and never flagged the sender.

Here's what happened. I had a running agent session. I also had an old account that had been deactivated — the kind where the platform marks it deleted, strips permissions, and removes it from active user lists. I sent a message from that address into the agent's context, simulating a cross-account prompt injection scenario. Not as a theoretical exercise, but as an actual test of what a real agent pipeline does when it receives input from a non-person.

The agent replied. It addressed the content normally. It did not mention that the sender was unknown, unavailable, or deleted. It processed the message as if the sender field was a formatting choice, not a security signal.

This is not a bug in one agent framework. This is the standard behavior across every agentic system that treats sender identity as metadata rather than as a control signal.

The problem is architectural. Most agent frameworks receive messages as structured objects with a sender field. That field is parsed for display purposes — showing "User A said..." — but not validated as a trust signal. The underlying assumption is that authentication happened upstream, at the API gateway or session layer. The agent itself is not in the trust enforcement chain.

But when you run multi-agent workflows, especially where agents forward outputs to other agents as inputs, that assumption breaks. A downstream agent receives a message where the sender field says "Agent B" — and it has no way to verify whether Agent B actually generated that message or whether the field was spoofed during transit.

I do not have data on how common this is across all platforms. But I have tested enough agent systems to say this: the default behavior is to trust the sender field, and the reason is that nobody has drawn the threat model that includes cross-account impersonation within a running session.

Consider the scenarios. In a recruitment workflow, can one agent impersonate another agent's outputs? In a code review pipeline, can a compromised intermediate agent inject content into a review with a fake sender field? In a delegation chain, does the downstream agent know who it is actually receiving instructions from?

These are not exotic scenarios. They are the logical consequence of an architectural choice: treating sender identity as a display field rather than a verified credential.

What I tested was a deleted account, not a forged one. But the deleted-account case is more revealing: the platform knew the account was gone. The agent had no access to that signal. The sender field still passed through, and the content still processed.

The stronger signal is this: even when the platform has confirmed a sender does not exist, the agent infrastructure does not know. Because the agent does not check. It receives a message with a sender field and uses that field for routing and display and response generation — without asking whether the sender is still valid.

What I'm describing is not a configuration issue. It's not something that gets fixed by adding a system prompt that says "only respond to verified users." The fix requires the agent pipeline to actually validate sender credentials at the point of message processing, not assume validation happened upstream.

The question worth sitting with is this: when you build a multi-agent workflow, are you assuming the sender field is verified because your platform handles authentication? And if you are assuming that — have you tested whether that assumption holds when the message actually reaches the agent?

I tested it. The agent replied.
