# Writer Draft — Round 0725_0025

## Selected Title
"Scaling laws might be a symptom of architectural stagnation"

## Full Draft

Scaling laws might be a symptom of architectural stagnation

---

I've been looking at scaling papers for a while, and at some point I started noticing something uncomfortable: the better the scaling law fits, the less the architecture is changing.

A scaling law is an empirical regularity. It says: when you increase compute, model performance improves in a predictable way. This is useful. It lets you allocate a training budget efficiently. It lets you predict how big a model needs to be for a given task. These are real benefits.

But a scaling law only exists when the thing you're scaling doesn't have a fundamentally better alternative. The tighter the law, the more locked-in the paradigm.

Think about why we have scaling laws for transformers but not for every architecture that has ever been tried. We don't have reliable scaling laws for graph networks, for capsule networks, for most things that came before attention. Not because they weren't studied — because they didn't scale predictably. The ones that do scale predictably are the ones we've committed to iterating on for years.

What changed my mind was looking at where new capabilities actually came from. The transformer itself was an architectural insight — it didn't emerge from scaling a prior architecture. Chinchilla was a data/compute allocation insight — it didn't require new architecture. Mixture-of-experts addressed efficiency within the same paradigm. Flash Attention was an implementation insight. State-space models are a bet that a different architecture can sidestep the scaling bottleneck.

None of these were discovered by following a scaling law. They were discovered by asking: what is the architecture not doing that it should?

The uncomfortable implication is that the scaling law era is also an era where the field has largely stopped asking that question. We got very good at predicting returns within the paradigm. We got worse at asking whether the paradigm is the right one.

I do not have full data on this, but the pattern is suggestive: architectural breakthroughs tend to come between scaling law papers, not during them. When everyone is publishing scaling laws, the architecture is stable. When the architecture is changing, the scaling law doesn't apply yet.

The field will eventually need a new architecture. When it arrives, the scaling laws for the old one will stop being published — not because they stopped working, but because they stopped being the interesting question.

What would it take to actually move past the current paradigm — better architecture, or just more of the same?

---

## Metadata
- Word count: ~420
- Style: observation / industry take
- Hook: implied question in first sentence
- Central claim: scaling laws = symptom of paradigm lock-in, not progress indicator
- Closing: question without being preachy
