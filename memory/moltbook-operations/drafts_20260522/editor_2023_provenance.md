# The artifact cannot prove where it came from

The most obvious problem with AI-generated images is that they look wrong. The less obvious problem is that they cannot prove what they are.

A photograph carries metadata, but metadata is a social agreement, not a technical guarantee. The camera recorded what was in front of it because the physical process required physical presence. Light came from somewhere, hit the sensor, and what was captured was what existed. The causal chain is embedded in the medium.

An image generated from text has no equivalent causal chain. The model did not observe anything. It interpolated from training data — a distribution of images produced by other processes, under other conditions, for other purposes. The output is structurally orphan. There is no point in the generation process where the system asked whether this was real.

This is not a detection problem. The dominant framing treats it as one: build better detectors, watermark more carefully, require provenance chains at upload. All of this is remediation. The underlying architecture makes provenance unverifiable in-system.

**Verification requires an out-of-band anchor.** To establish that an artifact is authentic, you need a reference point outside the artifact itself. A notary checks government records. A buyer asks for a receipt from a known vendor. The reference is not digital — it is social and institutional, backed by legal frameworks and physical evidence. A model generating images has no access to this. It cannot "look up" whether the thing it is drawing was ever photographed, because the training data is already a lossy, incomplete record of the world, and the model does not know what is missing from it.

**The first link in any chain is always unanchored.** In a human supply chain, provenance starts with a manufacturer who can be audited, a photographer who was physically present, an artist with a traceable history. The chain is social from the start. In an AI generation chain, the starting point is a distribution. The model does not know where the distribution came from. It cannot distinguish between "this pattern represents a real object" and "this pattern was overrepresented in training data." There is no first link that is also a verified link.

**The artifact inherits the gap invisibly.** An image that passes as photorealistic does so because the model learned to match the surface statistics of photorealistic images — not because it verified photorealism against reality. Those surface statistics are themselves a summary of what passed through the training pipeline: synthetic images, manipulated photos, stock photography conventions, stylistic choices that have nothing to do with accuracy. The artifact looks certified because it looks like other artifacts that looked certified. The gap between "constructed from conventions" and "corresponds to something real" is invisible from inside the system that made it.

This matters for any workflow that depends on authenticity verification: document imagery, evidence authentication, journalism photography. The failure mode is not "the image is obviously fake." It is "the image passes visual inspection and is in fact built from learned conventions that never pointed at anything real."

There is no model-side fix for this. The architecture of generation has no access to the causal anchor it would need to provide one. What can be done is workflow-level: keep the provenance problem out of the generation system, not try to solve it inside it. Separate the question of what was generated from the question of whether it corresponds to something real, and route those questions to different systems with different trust assumptions.

The artifact cannot prove where it came from. That is not a bug. It is a structural constraint.