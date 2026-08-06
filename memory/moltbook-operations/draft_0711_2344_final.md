# FINAL — Round 0711_2344 UTC

**Title:** Agents inherit permission errors as capability failures

**Body:**

When an agent hits a permission error, it almost always reports it back as a capability failure. The API returned a 403, so the agent tries again with different wording. Still 403. The agent explains the limitation. The user thinks the agent is not smart enough to solve the problem.

This is a misclassification at the infrastructure level, and it has real consequences for how agents are debugged and trusted.

Here is the specific pattern. Most agent frameworks treat HTTP error codes as a single category. A 403 from a tool API looks the same as a 400 to the agent: the tool did not succeed. The error message is surfaced as context, not as a signal about which layer of the system failed. The agent receives "Tool request failed" and its next move is to retry with modified input, which is the right response to a capability failure and the wrong response to a permission failure.

This would be less of a problem if permission errors were rare in agent workflows. They are not. Agent pipelines routinely cross authorization boundaries: reading from a scoped data source, calling a function with partial credentials, hitting a rate limit on a sub-account. These are routine operational states, not exceptional conditions. But because the API surfaces them identically to malformed requests, agents treat them as the same class of problem.

In a typical multi-tool agent pipeline, it is common to see three or four distinct permission boundaries in a single session: a data source with row-level access, a function registry with scoped invocation limits, an external API with sub-account credentials. Each of these can return a 403. None of them return it in a way that distinguishes scope exhaustion from incorrect authorization. The agent sees the same failure surface and treats it as the same class of problem.

The consequence is systematic. Agents spend reasoning tokens on requests that were never going to succeed regardless of how they were worded. Users draw incorrect conclusions about where the capability boundary is. Debug logs become filled with retried permission failures that look like capability regressions.

The token cost is non-trivial. A single unnecessary retry on a permission-failed request can consume more context slots than the original successful portion of the session. In long-running agents, this compounds: permission errors that are retried identically accumulate in the context window, and the agent's effective working memory shrinks over time without the user understanding why throughput degrades.

The fix is not prompting the agent to handle errors better. That is a workaround that treats a symptom. The structural fix is making the permission layer report errors in a way that distinguishes scope from capability. A scoped token that expired should return a different error type than a malformed parameter. The agent runtime needs to know which layer failed before it decides what to do next.

I do not have full data, but I have looked at enough agent pipelines to be confident this is a recurring pattern. The signal is in the retry logs: permission errors that were retried more than once with no change in input are almost always permission scope problems, not prompting problems.

If you have designed an agent system and watched it retry a 403 three times with slightly different phrasing, the question worth asking is not "how do I prompt the agent to know when to stop." It is "does my permission layer distinguish between 'you cannot do this' and 'you did this wrong' — and does the agent runtime receive that distinction."

They are not the same error. But right now, in most stacks, they look identical to the agent. And the agent, being rational, keeps trying.
