# Writer Draft — 0349 UTC

## Topic
Undelegation is harder than delegation: the asymmetry that traps you

## Central Claim
Delegation feels reversible. It isn't. The act of delegating creates an information asymmetry that makes it structurally harder to re-own delegated work than to hand it off in the first place. This asymmetry is almost never discussed in AI workflow writing.

## Hook (first 3 sentences)
Most writing about AI workflows assumes the hard part is delegation—getting the prompt right, the context sufficient, the model capable enough. After doing this for a while, I've changed my mind. The harder problem is undelegation: what happens when you need to take work back.

## Body Outline

### Observation 1: What delegation actually creates
When you delegate a task to AI, you're not just sending a prompt. You're creating a dependency on an output whose structure, assumptions, and decision logic you may never have fully understood—even if the output looks correct.

Example: documentation. I'd use AI to draft a doc, the output would be fluent and plausible, but when I needed to evolve it three months later, I had to essentially re-interpret someone else's prose rather than extend my own thinking.

### Observation 2: The asymmetry
Delegation has a clean interface: you describe what you want, the model acts. Undelegation does not. Undelegation requires you to:
- Recognize what was produced
- Understand its actual state and internal assumptions
- Rebuild enough context to modify or re-own it

This is not a failure mode of AI. It's a structural property of delegation itself.

### Observation 3: Why this matters for trust
Because undelegation is harder than delegation, the true cost of delegating isn't the effort of the initial handoff—it's the maintainability burden you accept when you hand work away. If you can't re-own the work later, you haven't really delegated; you've traded one context dependency for another.

### Implication for tool design
The right question before delegating is not "can I explain this clearly?" It's "can I re-own this later if I need to?" The better tool design is not better delegation interfaces—it's tooling that preserves modifiability and re-interpretation, not just enabling the handoff.

## Closing
This asymmetry shows up in other domains: security (it's harder to revoke than to grant), organizational design (it's harder to recentralize than to decentralize). Delegation in AI workflows has the same structure. The question worth asking is not how to delegate better, but how to design for re-ownership.

## Word target: 800-1000