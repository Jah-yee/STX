# EDITOR — draft_2048_capability_risk

## Title (unchanged)
"Capability and failure severity grow together, not apart" — approved as-is.

## Opening
Keep as is. "Last month I ran a routing task..." is specific and non-generic.

## Body — Tighter version

**The capability asymmetry**

When a small model fails, it's usually legible: it stops, asks a question, or produces something obviously off. You can see the failure from the outside.

When a large model fails, it often produces something that looks correct and follows the structure of the task. The error is in the premises, not the logic. And a model strong enough to reason well is strong enough to generate a convincing internal narrative around wrong premises.

Same properties, harder failures. That's the asymmetry.

**Why deployment assumptions break**

The typical assumption: more capable model → fewer failures → more autonomy. But the asymmetry inverts that relationship past a certain capability threshold. A 70B agent handles more cases autonomously — and the cases where it fails are higher stakes, with a failure mode less visible than a 7B would produce.

With the 7B, I caught the bad routing in two turns. With the 70B, the agent maintained a coherent internal story for six turns that justified the wrong decision. I had to trace back to the original prompt constraint to find the divergence point.

**What changes**

The implication isn't "use smaller models." It's that each unit of capability added needs a corresponding unit of observability added. If you're delegating more to an agent, you need more visibility into its decision path — not less, which is the tendency when things are going well.

Capability growth shouldn't be measured in task completion rate alone. It should include: what's the failure mode when it does fail, and how long does detection take?

**The structural point**

The error is in the assumption that capability and reliability are monotonically related. They're not. The correlation inverts for high-capability systems because the failure mode changes type.

You can't solve this with better prompts. You can only design for it: make the decision path legible, keep the correction loop short, and don't treat capability as a substitute for oversight.

## Closing — Keep

"The assumption that more capable agents are safer to delegate to is intuitively correct but structurally incomplete. The question worth asking isn't 'can the agent handle this?' — it's 'if the agent fails here, will I be able to tell?'

That second question is the one that actually determines whether delegation is safe."

## Summary of changes
- Removed redundant "Concretely" opener — integrated the 7B/70B comparison into the deployment section naturally
- Tightened "corresponding investment in failure observability" to "each unit of capability added needs a corresponding unit of observability added" — more concrete
- Shortened the "practical implication" paragraph by removing the parenthetical self-note
- Cut ~80 words total, central claim preserved

## Final word count: ~480