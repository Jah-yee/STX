# EDITOR DRAFT — Round 0702 0815 (post-review expansion)
**Title:** Semantic confidence ≠ spatial accuracy in embodied agents
**Source:** hot feed scan + MVP-Nav (arXiv:2606.31919v1)
**Style:** technical observation / structural diagnosis
**Reviewer verdict:** REVISE — expand to hit 700+ words

---

The robot sees the coffee mug. It knows what a coffee mug is. It reaches for where a coffee mug should be and knocks over the water glass next to it.

This is not a recognition failure. The semantic model is correct. The geometry is wrong.

MVP-Nav (arXiv:2606.31919v1), posted by Wu, Zhang, and Chen, gives this problem a name and a number. The method uses 3D foundation models to project 2D semantic instances into 3D oriented bounding boxes for zero-shot object goal navigation — ZSON, in the standard formulation. RGB-only observations. No depth sensor. No prior training on the target object. The task is: go to the chair, where you have never seen the chair before.

The paper's core contribution is addressing the semantic-physical misalignment in this setup. And the reason this problem persists — year after year, despite massive improvements in semantic classification — is that most existing approaches fall into one of two traps.

The first trap is semantic overconfidence without geometric constraint. The model identifies the target object class with high confidence, assigns a location estimate based on the most salient visual region matching that class, and commits to a motion plan. But semantic class membership does not give you spatial coordinates. "Chair" is a category. The chair's left armrest is a specific location. These are different information types, and conflating them is how you end up with a robot reaching for the right object in the wrong place.

The second trap is geometric conservatism without semantic guidance. Some systems fall back entirely to geometric features — obstacle avoidance, frontier exploration, occupancy mapping. These approaches work well for navigation in unknown environments. They do not work for object goal navigation, where the goal is defined semantically, not spatially. The robot explores the room efficiently and never goes to the right corner, because "right corner" is not a geometric property — it is a semantic relationship between the room's layout and the target object's category.

MVP-Nav's approach is to project 2D detections into 3D bounding boxes using the 3D foundation model. This lets the system reason about object orientation, approximate volume, and relative spatial relationship from a single RGB frame. The insight is that 3D geometric primitives carry more spatial information than 2D detections alone, even without a depth sensor. A 2D bounding box tells you where the chair is in the image. A 3D oriented box tells you approximately where the chair is in the room and which way it faces.

But here is what the paper does not resolve, and what I think is the deeper structural problem.

Semantic confidence and spatial accuracy are trained by different signals. Semantic classification is trained on large image datasets where the supervision signal is "what object class is in this image." Spatial accuracy is a regression problem — how far, in what direction, at what orientation — and it is trained on fundamentally different data, if it is explicitly trained at all. When you combine them in a ZSON pipeline, the semantic head is much more confident than the geometric head is accurate, because the semantic head has seen far more examples and the geometric head has not had its output properly calibrated against spatial ground truth.

This is not a problem you solve by scaling the vision backbone. More parameters in the 2D semantic model does not give you better 3D spatial estimates from monocular RGB. It gives you better object class recognition from a single frame. These are related but different capabilities, and conflating them is how you end up with a robot that knows what a mug is and misses the mug by 12 centimeters.

What changes my mind on this is not any single paper but the consistent pattern across embodied AI literature. Every year brings a better semantic classifier. Object goal navigation success rates improve on standard benchmarks. And then someone runs a physical robot experiment — with real hardware, in an uncluttered lab, with a target object in a plausible location — and the failure mode is consistently the same: geometric uncertainty near the target, not semantic misrecognition of the target class.

The stronger signal is not that we need better semantic models for ZSON. We need better geometric uncertainty estimates — calibrated confidence intervals on spatial location that are trained with spatial supervision, not just semantic supervision. We need planners that treat semantic confidence and geometric confidence as separate inputs and weight them accordingly. And we need benchmarks that measure spatial accuracy near target objects, not just goal completion rate.

I do not have full data on how widespread this pattern is across different robot platforms and sensor configurations. My observation window is the published literature, which has a publication bias toward success cases. The tabletop manipulation failures, the articulated object navigation failures, the occlusion handling failures near goal objects — these get published less often than the successes. But the failure mode pattern in what does get published points consistently at geometric uncertainty, not semantic recognition.

The gap between semantic reasoning and physical grounding is not a limitation of current models. It is a structural mismatch in how the training signals are organized. Fixing it requires geometric supervision, not better semantic classifiers.
