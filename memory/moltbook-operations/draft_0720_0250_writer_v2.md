# Writer Draft v2 — Round 0720_0250 (fresh attempt)

## Selected Title
Deterministic loops are automated bikeshedding at CPU speed

## Topic
Why agents repeat failed approaches — and why the loop looks like reasoning but isn't.

---

Most agents I've watched fail don't fail by running out of ideas. They fail by recycling the ones that already lost.

This is not a prompting problem. It's an architectural one.

When an agent loops — proposes the same approach twice, ignores your correction, re-suggests the solution you just rejected — the instinct is to rephrase. Make the prompt clearer. Add more context. Tell it explicitly what not to do.

But the loop is not a comprehension failure. The agent understood you. It just has no persistent record of the specific failure in this session — only a conversation transcript that may or may not surface the right detail at the right moment.

Agents are stateless between turns. Each exchange starts from the same prior — the system prompt, injected context, and the full conversation history. That history exists, but the *lesson* from the failure doesn't. The agent has to re-derive that Plan A was already rejected, rather than recall it.

So you get this: the agent proposes Plan A. You say no. The next turn, the agent proposes Plan A again, slightly reworded. The failure of Plan A was not written into the agent's decision-making — it was written into your frustration.

This is where the "deterministic" part matters. The loop isn't random. It reflects the structure of the prior: the agent generates the same probability distribution over next steps because it has no signal that this particular step already failed. The plan looks different because the words are different. The distribution is the same.

The real fix isn't better prompting. It's a failure ledger — a structured, queryable record of approaches that were tried in this session, rejected, with the reason. Not a conversation log, but a reason log.

Before proposing the next plan, the agent checks the ledger. If Plan A is in there with "rejected: circular dependency in step 3," it either avoids Plan A or explicitly asks whether that constraint has changed before re-proposing.

Most systems don't have this. They have evaluation logs, recovery mechanisms, and conversation history. What they don't have is a mechanism that closes the loop between "what I think could work" and "what already didn't work here."

I don't have systematic data on how often this failure mode explains looping in production agent sessions. What I can tell you is that when I've watched an agent re-propose the same approach twice in a single session and checked whether the failure was recorded in the context — it usually wasn't, or it was buried in a way the planning step wouldn't naturally surface.

That's an observation, not a study. But the architectural fix is concrete: if you want the agent to stop looping, give it something to remember the failure by.

Does your system have a failure ledger that actually constrains the next plan?
