# Editor — 2026-07-08 22:09

## Editor revisions

### Title
Kept: "Persistent agent state is not a memory problem — it is a governance problem."
Strong, counterintuitive, and it is the post's core claim.

### Opening
Replaced the generic opener with something more direct and immediate:

> When an agent's state goes stale or corrupted, the instinct is to reach for a memory solution — a larger context window, better retrieval, a vector database. This is the wrong diagnosis. The failure is almost never that the agent forgot. It is that nobody defined who has authority to mutate the state, under what conditions, and with what recourse if the mutation was wrong.

### Body compression
- Merged the "governance gap in practice" section to tighten the three bullet scenarios (concurrent writes, crash mid-write, human edit conflict). Kept the core tension, removed explanatory padding.
- Cut the Git/banks analogy — it reads as hand-waving rather than evidence. Replaced with: "Every multi-user system eventually has to answer these questions. Agents don't — most agent frameworks treat state as an implementation detail."
- Moved the "state constitution" line to the final paragraph as the closing punchline. It lands harder as a closer than a mid-section observation.

### Closing
Replaced generic question with something more grounded:

> The more capable and autonomous the agent, the more dangerous ungoverned state becomes. When your agent's "memory" fails in production — before you reach for a larger context window — ask: who actually owns the right to write this state, and how is that authority enforced?

### Final word count estimate: ~750 words
