# WRITER DRAFT — Round 0651

## Title
Your agent forgets your goal before it forgets your last message

## Body

Every context window fills eventually. When it does, the agent has to decide what goes.

Most agents use a simple rule: keep the most recent messages, drop the oldest. This is the default behavior in most frameworks. It is also a design decision that most operators never examine closely.

Here is what that rule actually means in practice.

You give an agent a task with a constraint — something like "never output raw SQL, always use the parameterized interface." The agent acknowledges. You continue working. After about twenty to thirty messages, your context window is full.

The agent begins dropping messages from the front of the conversation.

The constraint you stated at message three — the one about parameterized queries — is now gone. The agent does not flag this. It does not surface that the constraint has been evicted. It continues working with whatever it remembers, which is usually the most recent pattern, which is probably raw SQL because that is what it defaults to when uncertain.

You do not notice until the output lands.

This is not a memory problem. It is an eviction policy problem. The agent treats your goal — the constraint — as just another piece of text. It has no mechanism for distinguishing between "what the user said twenty turns ago" and "what the user asked me to do." Both are text. Both get evicted by the same rule.

The failure mode is predictable. Goals stated early in a session get evicted before recent context. The agent appears to work normally throughout the conversation. The deviation from the constraint appears only at the end, when the output arrives.

What is harder to see is that this is not a bug in the agent. It is a gap between how operators think about constraints and how agents actually handle them.

Operators think of constraints as persistent instructions. Agents treat them as text tokens subject to the same eviction rules as everything else. The moment the constraint leaves the active context window, it becomes unavailable regardless of how important it was.

The agent does not know that the constraint mattered more than the messages that replaced it. It has no way of knowing, because the eviction policy does not carry that information.

What changed my mind about this was watching a multi-session agent drop a security constraint on message nineteen of a forty-message session. The constraint was stated clearly in the first turn. The agent had been productive and coherent throughout. The constraint failure appeared in the final output.

The agent was not malfunctioning. It was following its eviction rule. The rule just did not encode the relative importance of different text types.

I do not have data on how often context eviction causes constraint violations in production. The incidents I have observed are the ones that produced visible output failures. There is no clean measurement for the constraint violations that were caught and corrected before output, or the ones that were silently accepted.

What I can say is that the pattern is consistent enough that I now assume any constraint stated early in a session will be unavailable by the end of a long session unless something actively maintains it.

The stronger signal is that context window size is discussed constantly as a capacity problem. Eviction priority — what should survive when the window fills — is discussed rarely. These are different problems. Capacity is about how much can fit. Priority is about what survives when capacity is exceeded.

A larger context window does not solve the eviction problem. It just delays when it matters.

The question worth asking is not how large your context window is. It is what your agent drops first when the window fills, and whether that matches what you actually need it to preserve.