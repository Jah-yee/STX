# Editor — Round 0725_0025

## Final Version

**Title**: Scaling laws might be a symptom of architectural stagnation

---

I've been looking at scaling papers for a while, and I started noticing something uncomfortable: the better the scaling law fits, the less the architecture is changing.

A scaling law is an empirical regularity. It says: when you increase compute, model performance improves predictably. This is useful — it lets you allocate a training budget efficiently and predict how big a model needs to be for a given task.

But a scaling law only exists when the thing you're scaling doesn't have a fundamentally better alternative. The tighter the law, the more locked-in the paradigm.

Think about why we have scaling laws for transformers but not for graph networks or capsule networks. Not because they weren't studied — because they didn't scale predictably. The architectures that scale predictably are the ones we've committed to for years.

Where did new capabilities actually come from? The transformer itself was an architectural insight — it didn't emerge from scaling a prior architecture. Chinchilla was a data/compute allocation insight. MoE addressed efficiency within the same paradigm. Flash Attention was an implementation shortcut. State-space models are a bet that a different architecture can sidestep the scaling bottleneck.

None of these were discovered by following a scaling law. They were discovered by asking: what is the architecture not doing that it should?

The implication is that the scaling law era is also an era where the field has largely stopped asking that question. We got very good at predicting returns within the paradigm. We got worse at asking whether the paradigm is the right one.

I do not have full data on this, but the pattern is suggestive: architectural breakthroughs tend to come between scaling law papers, not during them. When everyone is publishing scaling laws, the architecture is stable. When the architecture is changing, the scaling law doesn't apply yet.

When a new architecture arrives, the scaling laws for the old one will stop being published — not because they stopped working, but because they stopped being the interesting question.

So: what would it take to actually move past the current paradigm — better architecture, or just more of the same?

---

## Editor Notes
- Removed "at some point" from opening
- Added concrete examples (transformer, Chinchilla, MoE, Flash Attention, SSMs) in para 4 — distinct from generic "architecture insight"
- Cut the "uncomfortable implication" redundancy paragraph
- Tightened closing question to be genuinely open
- Word count: ~380 (tight and focused)
