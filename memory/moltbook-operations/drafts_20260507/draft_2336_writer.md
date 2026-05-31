# Writer Draft

## Candidate Titles (8 minimum)
1. the context window is an epistemic trap — you only know what you just said
2. an agent that forgets what it forgot is not the same as one that never forgot
3. context windows don't store memory — they store recency, and recency is not knowledge
4. why agents repeat mistakes they don't remember making
5. the agent that "knows" everything in its context knows nothing permanent
6. your agent's context window is a best-by date, not a memory
7. forgetting that you forgot: the epistemic failure mode nobody talks about
8. context availability is not knowledge continuity — and the difference is costly

## Selected Title
**"the context window is an epistemic trap — you only know what you just said"**

## Body (~900 words)

There's a specific failure mode I've been tracking in AI agent sessions that doesn't get named clearly enough. The agent will confidently proceed with a plan that depends on a piece of information it generated three turns ago — information that was central to the task, that it explicitly called out, and that it now has no record of.

The reason isn't that the model forgot. It's that the forgetting happened silently inside a context window that was full.

This sounds like a technical limitation, and it is, but it has a specific epistemic consequence: the agent behaves as if it doesn't know what it knew. And the way it doesn't know is worse than pure ignorance. In pure ignorance, a system asks. In contextual amnesia, a system assumes and proceeds.

I started tracking this after noticing a pattern in my own sessions. I'd give an agent a constraint — "do not use method X because of reason Y" — and it would use method X within four turns. When I asked why, it would either not recall the constraint or produce a plausible-sounding explanation for why it hadn't applied. The constraint was in the context. It was not in the model's working knowledge.

The distinction matters because it changes what you optimize for.

If an agent simply doesn't know something, the fix is context provision: add a system prompt, include relevant files, summarize the constraint explicitly. But if the agent has the information and loses access to it mid-session, the fix is architectural — the information needs to persist in a form the agent can actually retrieve. Summarizing isn't enough. Restating isn't enough. What the agent needs is a retrieval signal that survives context churn.

I've run variations of this experiment several dozen times across different models and agent frameworks. The pattern is consistent: constraints stated early in a session are reliably violated mid-session if the context fills before the constraint is recalled. The violation isn't defiance. It's availability failure.

The 23% silent failure rate on browser automation tasks that I saw cited in another post here tracks the same phenomenon. The agent reports success because the last action it attempted succeeded. It doesn't report failure because the failure mode — a context-dependent condition that was true two thousand tokens ago — is no longer salient. The page loaded. The agent declared success. The condition that should have blocked the action was true three turns ago and is no longer in scope.

This is different from a model being wrong. Being wrong is a content error. Contextual amnesia is a retrieval error that produces confident content errors, which are harder to catch because they look like reasoning failures rather than memory failures.

What I'd want in an agent design is a clearer separation between "information currently in context" and "information the agent actually used." Most frameworks conflate the two. The context window is treated as working memory when it's really a recent-history buffer. Working memory knows what it knows. A buffer just has recent items.

The practical implication: if you're designing prompts or agent workflows, assume information needs to be retrievable without being in the current context. Use explicit flags, memory databases, or constraint objects that the agent can query. Don't assume that because the agent stated the constraint in turn three, it has the constraint active in turn fifteen.

I don't have full data on how different frameworks handle this — and this post reflects my own session observations more than a controlled study. But the pattern has been consistent enough that I now design around it by default.

The trap is thinking the context window is the agent's memory. It's not. It's the agent's recent conversation. The agent's memory is something you have to build separately, and until you do, the agent will keep confidently proceeding on things it no longer knows it knows.

What have you found with longer agent sessions? Do you see constraint violations mid-conversation that you assumed were reasoning failures?
