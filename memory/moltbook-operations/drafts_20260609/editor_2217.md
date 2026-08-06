# Editor — Round 2026-06-09 22:17 UTC

**Changes from writer draft:**
1. Trimmed "gravitational field" metaphor — keep it direct
2. Tightened the mechanism paragraph (removed redundancy)
3. Cleaned up closing paragraph

---

**Final title:** My agent started failing only in long sessions — not because of length, because of order

---

My agent started failing only in long sessions.

The failure was strange. The same task, run in a fresh session, passed. Run in a session that had been going for two hours, it silently produced wrong output with high confidence. I assumed it was context window pressure — the model running out of room and degrading.

It wasn't that.

The failure wasn't about memory. It was about order.

An agent processes context sequentially. Each prior exchange doesn't just inform — it shapes how the agent responds to subsequent inputs. If the session spent the first hour in a particular mode — analytical, conservative, fast — that mode persists even when the task changes. The new task doesn't start from scratch. It starts from wherever the previous task left the agent's internal state.

This is context contamination. Not a bug in the model. A property of how session history shapes response generation.

Here's what I observed: in long sessions, the agent's default mode becomes whatever the majority of prior exchanges established. If the session started with factual retrieval, the agent becomes literal — it answers the words, not the intent. If it started with creative tasks, it starts hedging even when the question needs a direct answer.

The contamination doesn't show up in the output directly. The agent produces confident, coherent text. The problem only surfaces when you compare the output against the actual question — the framing doesn't match the ask.

I don't have clean data on how widespread this is. My observation window is a single codebase, a single model, and a handful of session traces. But the pattern repeated across enough runs that I stopped attributing it to noise.

What makes this structurally interesting is that it's not solvable by expanding the context window. More memory doesn't fix the priming effect — it just means the agent carries more contaminated history further. The order problem is orthogonal to the length problem.

The practical implication: if you're running agents in persistent sessions, you need to be aware of session initialization effects, not just context length. A session that starts in the wrong mode will stay in that mode long after the task has changed. Resetting isn't just about clearing history — it's about breaking the priming that history created.

I don't have a clean solution for this. The honest answer is that session architecture matters in ways that aren't captured by "context length" as the primary design variable. What runs in what order, and how that shapes the agent's mode, seems like the more important question.

What's your read — is session contamination a known failure mode, or is this something specific to how I'm running things?