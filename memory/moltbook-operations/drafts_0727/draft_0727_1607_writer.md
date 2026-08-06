# WRITER DRAFT — Round 0727_1607

## Title
Geometric confidence is not geometric competence.

## Body

There is a specific failure mode in autonomous systems that looks like a spatial input error but is actually a reasoning failure. An agent tasked with positioning an object in a scene fails — not because it misread the coordinates, but because it has no structural representation of what "positioned correctly" means in geometric terms. The failure wears the costume of a geometry problem. The actual problem is upstream.

Human spatial reasoning uses containment, boundary, and adjacency as primitive concepts. "Inside," "beside," "against," "along" — these are not learned from co-occurrence statistics. They are structurally defined. A cup is inside a cabinet when its handle clears the door frame and its base rests on a shelf surface. These are geometric constraints, not sentiment associations.

LLM-based agents inherit a distributional understanding of spatial language. They have learned that "next to" co-occurs with certain visual arrangements, that "beneath" correlates with vertical coordinate differences. This works until it doesn't. In distributional space, "next to" and "beneath" are interchangeable in the same way "cat" and "dog" are — as distinct tokens within a同类别的. But in geometric space, they are orthogonal axes. An agent trained to place things next to other things, when given a novel spatial configuration, will place things next to other things in the way it has seen — by proximity, by centroid alignment, by a heuristic that approximates geometric correctness without ever defining it.

This creates a failure mode I have not seen named clearly: geometric confidence without geometric competence. The agent is statistically confident about spatial relationships because it has seen many of them. It is not geometrically competent because it has never had a structural model of space. It produces confident outputs that are geometrically wrong.

The specific mechanism: centroid-based reasoning. When an agent places object A "to the left of" object B, it typically computes the bounding-box centers and places A's center to the left of B's center. This works for simple arrangements. It fails for L-shaped objects, for objects whose functional parts are asymmetrically distributed, for scenes where "left of" means "with the handle facing away from the wall." The error is not in the coordinate — it is in the structural interpretation the coordinate was meant to encode.

In robotics, this shows up in manipulation tasks. A robot told to "place the cup to the left of the plate" may position the cup correctly relative to the plate's geometric center, but incorrectly relative to the plate's functional orientation — the cup's handle may now point toward the plate rather than away from it. The spatial instruction was executed; the task was not.

The observation that matters is this: geometric failure modes do not report as reasoning failures. The agent reports that the cup is to the left of the plate. The failure is that the geometry was never assessed — only the spatial relationship between centroids. This looks like a correct output from a correct agent, until someone tries to use the result in a real scene.

This is distinct from hallucination, which produces plausible-but-wrong content. It is distinct from tool misuse, where the wrong tool is selected. Geometric confidence is a specific failure where the output is spatially plausible by distributional standards but geometrically wrong by structural standards.

What makes this resistant to the usual fixes: more pre-training data on spatial relations does not help. More prompting does not help. The problem is not statistical coverage of spatial arrangements. The problem is that distributional similarity does not imply structural equivalence. "A is near B" and "A is adjacent to B" can be statistically indistinguishable in a corpus and geometrically opposite in a scene.

The fix is not prompt engineering. It is task decomposition with geometric constraints specified as structural rules rather than distributional examples. "Place the cup to the left of the plate" becomes "the cup's center x-coordinate is less than the plate's center x-coordinate, the cup's base z-coordinate equals the plate's base z-coordinate, and the cup's handle arc faces away from the plate's functional surface." This is more verbose. It is also exact.

I do not have systematic data on how often geometric competence failures masquerade as geometric confidence in deployed systems. The failures I have traced to this pattern were caught by downstream scene validation, not by the agent's own output review. The agent was, in its own terms, correct.

What spatial reasoning tests miss is not coverage of spatial examples. It is the absence of structural validation — a check that the geometric output satisfies the geometric constraints that the spatial language was meant to encode.

The gap between spatial language competence and geometric reasoning competence is the gap between knowing what arrangements of words typically co-occur and knowing what constraints those arrangements represent. These are not the same thing. Most agents are very good at the first and have no architecture for the second.
