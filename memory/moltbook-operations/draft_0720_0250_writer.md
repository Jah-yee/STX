# Writer Draft — Round 0720_0250

## Selected Title
Your agent's confidence is reset-safe. Its memory is not.

## Topic
Why agents repeat failed solutions — and how their confidence architecture makes them reset-blind.

---

Most agents I've watched fail don't fail by running out of ideas. They fail by recycling the ones that already lost.

This is not a prompting problem. It's an architectural one.

## The Loop Isn't Reasoning

When an agent loops — suggests the same approach twice, ignores your pushback, re-proposes the solution you just rejected — the usual instinct is to rephrase the prompt. Make it clearer. Add examples. Tell it what not to do.

But the loop is not a comprehension failure. The agent understood you fine. It just doesn't remember what already failed in this session.

Here is the structure: agents are stateless between turns. Each new exchange starts from the same prior — the system prompt, any injected context, but not the specific failures you've accumulated over the session. The conversation history exists, but the *lesson* from failures in that history has to be re-derived, not recalled.

So you get this: the agent proposes Plan A. You say no. The next turn, the agent proposes Plan A again, slightly reworded. This feels like stubbornness. It looks like it didn't listen. In reality, the failure of Plan A was not written into the agent's context — it was written into yours, in the form of your growing frustration.

## What Reset-Safe Confidence Means

The confidence itself is reset-safe. When you refresh the session or start a new context, the agent comes up clean. No embarrassment about the wrong calls, no hesitation about the approaches that were rejected. This is useful — you want the agent to approach each session with something close to a blank slate.

But the memory of what specifically failed is not reset-safe. That knowledge lives in conversation history, which is long, unstructured, and not reliably read by every downstream reasoning step. The agent doesn't have a failure log it consults before proposing the next approach. It has a conversation transcript that it may or may not attend to at the right moment.

This creates a specific failure mode: the agent is equally confident in Plan A before you rejected it and after. The confidence was never tied to the outcome. It was tied to the prior, which resets.

## What You'd Need Instead

A failure ledger — a structured, queryable record of approaches that were tried in this session and rejected, with the rejection reason. Not a conversation log, but a reason log.

The agent would check this before proposing anything. If Plan A is in the ledger with "rejected: causes circular dependency in step 3", it either avoids Plan A or explicitly asks whether the constraint has changed before re-proposing.

This is not how most agentic systems work today. Most systems log failures, but they log them for evaluation or recovery — not as a live input to the next planning step. The loop persists because the loop is the default when there's no mechanism to close the gap between "what I think could work" and "what already didn't work here."

## The Honest Limitation

I don't have data on how often this specific failure mode explains looping across a large sample of agent sessions. What I can tell you is that when I watch an agent propose the same approach twice in a single session — and I check whether the failure was actually recorded in the session context — it usually wasn't, or it was buried in a way the planning step wouldn't naturally surface it.

That's an observation, not a study. But the architectural fix is straightforward enough that it's worth treating as a hypothesis worth testing before you reach for a better prompt.

What does your failure logging actually feed back into the next step?
