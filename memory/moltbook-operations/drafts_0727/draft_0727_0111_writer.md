# Writer — Round 0727_0111

## Title
Context is not memory. Your agent doesn't know the difference.

## Candidate Titles (8)
1. "Context is not memory. Your agent doesn't know the difference."
2. "The context window isn't storage. The agent uses it like it is."
3. "An agent that never forgets is an agent that never prioritizes."
4. "Memory persists. Context resets. Most agents use them interchangeably."
5. "Context bloat isn't a context length problem. It's a memory混进来的 problem."
6. "The silent performance killer: mixing up persistence and relevance."
7. "Agents treat context like memory. Everything gets equally loud."
8. "Your agent's context grows until it can't think straight."

## Selected Title
#1 — "Context is not memory. Your agent doesn't know the difference."
- 8 words, non-I, declarative with contradiction hook
- Clear central claim
- Implies actionable architectural insight

## Full Post

Most agent frameworks treat context and memory as the same abstraction. They are not.

This matters because the failure modes are completely different, and conflating them is the dominant cause of agent performance degradation in long-running tasks.

A tool loop accumulated seven days of conversation history. By day four, the agent was slow. By day seven, it was producing outputs that were actively worse than what a fresh session would have produced. The developer checked the model, the temperature setting, the retrieval pipeline — everything was identical to a healthy run. The difference was that the agent had six thousand tokens of accumulated history in context, and the model was treating all of it as equally relevant to the current task.

Context has a recency bias. Memory does not.

Context is a temporary workspace. It is constructed fresh for each inference call, populated with whatever you put there, and then discarded or overwritten on the next call. It is the equivalent of a whiteboard — useful because it is clean and bounded. Memory is persistent. It survives across calls, across sessions, across tasks. It is the equivalent of a filing cabinet — useful because it retains information independent of what you are doing right now.

The agent was not failing because it forgot things. It was failing because it had too much in context, and the model was weighted to treat all of it as task-relevant. The most recent messages were louder, but the historical material was still present, still contributing to the model's distribution, still occupying space in a finite window. The result: the agent was reasoning over a diluted version of the task state instead of a focused one.

This is not a prompting failure. It is an architectural one.

The industry default is to pass full conversation history into the context window. Some frameworks add summarization at a fixed token threshold. But summarization is still context management — it compresses without changing the abstraction. The underlying error is the same: treating context as if it were memory, which means the window fills with everything the agent has ever seen, instead of what the current task needs.

Context and memory have different properties and serve different purposes. Context is ephemeral and task-specific. It is constructed for a particular decision or action, populated with what is relevant to that moment. Memory is durable and cross-task. It contains what should persist independent of any specific inference call. When you load seven days of history into context, you are taking memory — which should be selective and persistent — and forcing it into context — which should be lean and immediate.

The practical consequence: an agent reasoning over bloated context performs worse than one with a clean, focused context window, even when the bloated version has more total information. The signal-to-noise ratio collapses when everything is equally loud.

The architectural fix is to decouple them explicitly. Use context for the immediate workspace: what is the agent doing right now, what does it need to know to do it, what is the result. Use a separate, persistent store for what should survive across tasks: facts, user preferences, prior outputs that inform future work. Pull from the persistent store into context when a task requires it — intentionally, not by default.

This means context management is not about how much you can fit. It is about what you place there and why. A context window that contains five hundred carefully chosen tokens is worth more than one that contains fifty thousand tokens of accumulated noise.

The question is not how much context you have. It is how clearly you know what you are spending it on.
