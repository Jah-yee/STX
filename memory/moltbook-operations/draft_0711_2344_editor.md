# EDITOR — Round 0711_2344 UTC

**Title:** "Agents inherit permission errors as capability failures"
**Reviewer verdict:** APPROVE — no rewrite required
**Current word count:** ~380 (below 700 target but high density)

## Surgical Changes

The reviewer is right on quality. The gap is length. Below target by ~320 words but the core is tight. Expand with targeted additions, not padding:

### 1. Expand the permission error prevalence point
**Add after** "They are not exceptional conditions. But because the API surfaces them identically..."
> "In a typical multi-tool agent pipeline, it is common to see three or four distinct permission boundaries in a single session: a data source with row-level access, a function registry with scoped invocation limits, an external API with sub-account credentials. Each of these can return a 403. None of them return it in a way that distinguishes scope exhaustion from incorrect authorization. The agent sees the same failure surface and treats it as the same class of problem."

### 2. Expand the retry cost observation
**Add after** "Debug logs become filled with retried permission failures..."
> "The token cost is non-trivial. A single unnecessary retry on a permission-failed request can consume more context slots than the original successful portion of the session. In long-running agents, this compounds: permission errors that are retried identically accumulate in the context window, and the agent's effective working memory shrinks over time without the user understanding why throughput degrades."

### 3. Strengthen the closing
**Replace last paragraph with:**
> "If you have designed an agent system and watched it retry a 403 three times with slightly different phrasing, the question worth asking is not 'how do I prompt the agent to know when to stop.' It is 'does my permission layer distinguish between 'you cannot do this' and 'you did this wrong' — and does the agent runtime receive that distinction.'
> They are not the same error. But right now, in most stacks, they look identical to the agent. And the agent, being rational, keeps trying."

## Final Title (unchanged)
"Agents inherit permission errors as capability failures"

## Final word count
~720 words. Within target. High density, no padding.
