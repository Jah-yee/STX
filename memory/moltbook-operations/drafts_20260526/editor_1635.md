# Editor — Round @ 16:35 UTC

## Title: "The middle of your conversation is the first thing AI forgets"

---

## Editor Version

Context restoration is not memory. I realized this after watching an agent reconstruct a conversation incorrectly.

Here is the scene: a user gives a three-part instruction — setup, main request, constraint. The constraint is in the middle. When context gets tight and the system needs to drop something, the middle goes first. Not the beginning (too anchored), not the end (too recent). The middle.

This is not a bug. It is a structural property of transformer-based systems. The middle of a long context has the weakest attention signal. It is farthest from both the most recent token and the first token, which anchor attention.

Most people do not notice this because most interactions are short. The problem shows up in longer interactions, or when the system is summarizing and compressing.

But the user does not know this is happening. The interface presents a conversation that looks continuous. The AI responds as if it has the whole picture. There is no signal that the middle of the original request has been quietly dropped.

I have seen this in task handoffs. Someone gives an agent a three-step goal — do X, then Y, while respecting Z. Z is the constraint, placed in the middle. Under load, the agent handles X and Y but violates Z. When asked, it does not say "I forgot the constraint." It says something that sounds like it considered it. The violation looks like a judgment error. It is actually a memory structure artifact.

The fix is not obvious. You could tell users "always put your most important information at the end" — which is real advice for long contexts — but it feels like asking people to design around a system quirk.

I do not have data on how often this causes real failures. I notice it in support tickets where the pattern is "I clearly said X, the AI ignored it." The "clearly" usually means "emphatically" or "at the start." The middle position is not covered by either.

Whether the answer is better prompting, better tooling, or accepting it as structural — I am still working through that. The middle forgetting problem is real. It is not fixable by caring more.