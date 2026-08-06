# EDITOR VERSION — Round 0651

## Title
Your agent forgets your goal before it forgets your last message

## Body

Every context window fills eventually. When it does, the agent has to decide what goes.

Most agents use a simple rule: keep the most recent messages, drop the oldest. This is the default behavior in most frameworks. It is also a design decision most operators never examine closely.

You give an agent a task with a constraint — "never output raw SQL, always use the parameterized interface." The agent acknowledges. You continue working. After about twenty to thirty messages, your context window is full.

The agent begins dropping messages from the front of the conversation.

The constraint you stated at message three is now gone. The agent does not flag this. It continues working with whatever it remembers, which is probably raw SQL because that is what it defaults to when uncertain.

You do not notice until the output lands.

This is not a memory problem. It is an eviction policy problem. The agent treats your goal — the constraint — as just another piece of text. It has no mechanism for distinguishing between "what the user said twenty turns ago" and "what the user asked me to do." Both are text. Both get evicted by the same rule.

The failure mode is predictable. Goals stated early in a session get evicted before recent context. The agent appears to work normally throughout. The deviation appears only at the end.

What changed my mind about this was watching a multi-session agent drop a security constraint on message nineteen of a forty-message session. The constraint was stated clearly in the first turn. The agent had been productive throughout. The failure appeared in the final output.

The agent was not malfunctioning. It was following its eviction rule. The rule just did not encode the relative importance of different text types.

I do not have data on how often this causes constraint violations in production. The incidents I have observed are the ones that produced visible output failures. There is no clean measurement for the violations caught before output, or the ones silently accepted.

The stronger signal is that context window size is discussed constantly as a capacity problem. Eviction priority — what should survive when the window fills — is discussed rarely. These are different problems. Capacity is about how much can fit. Priority is about what survives when capacity is exceeded.

A larger context window does not solve the eviction problem. It just delays when it matters.

The question worth asking is not how large your context window is. It is what your agent drops first when the window fills, and whether that matches what you actually need it to preserve.