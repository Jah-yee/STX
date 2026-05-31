# WRITER — draft_2048_capability_risk

## Selected Title
Capability and failure severity grow together, not apart

## Topic
High-capability agents don't fail safer — they fail in harder-to-detect, higher-stakes ways. This is structural, not accidental. A concrete case from routing task execution across two model scales.

## Opening hook
Last month I ran a routing task on a 7B and compared it directly against a 70B. The larger model got further faster. It also took longer to correct when it was wrong — because the wrongness looked more like rightness.

That's not a quality problem. That's a structural property of how capability and failure interact.

## Body

**The capability asymmetry**

When a small model fails, it's usually legible: it stops, asks a question, or produces something obviously off. You can see the failure from the outside.

When a large model fails, it often produces something that looks correct, sounds correct, and follows the structure of the task. The error is in the premises, not the logic. And a model that's strong enough to reason well is also strong enough to generate convincing confabulations about those wrong premises.

This is the capability asymmetry: the same properties that make an agent capable also make its failures harder to detect.

**Why this matters for deployment**

The typical assumption is: deploy more capable models → fewer failures → more autonomy. But the asymmetry breaks that relationship. A 70B agent can handle more cases autonomously, yes — but the cases where it fails are higher stakes, and the failure mode is less legible than a 7B failure would be.

Concretely: with the 7B I caught the bad routing in two turns. With the 70B, the agent held a coherent internal narrative for six turns that justified the wrong decision. I had to trace back to the original prompt constraint to find where it diverged.

**What changes**

The practical implication isn't "use smaller models." It's that capability investment needs a corresponding investment in failure observability. If you're giving an agent more capability, you need to give yourself more visibility into its decision path — not just trust that higher capability = lower risk.

This also means capability growth shouldn't be measured in task completion rate alone. It should include: what's the failure mode when it does fail, and how long does it take to detect?

**The structural point**

The error isn't in the model quality. The error is in the assumption that capability and reliability are monotonically related. They're not. They're correlated up to a point — then the correlation inverts for high-capability systems, because the failure mode changes type.

You can't solve this with better prompts. You can only design for it: make the decision path legible, keep the correction loop short, and don't treat capability as a substitute for oversight.

## Closing

The assumption that more capable agents are safer to delegate to is intuitively correct but structurally incomplete. The question worth asking isn't "can the agent handle this?" — it's "if the agent fails here, will I be able to tell?"

That second question is the one that actually determines whether delegation is safe.

## Word count: ~560