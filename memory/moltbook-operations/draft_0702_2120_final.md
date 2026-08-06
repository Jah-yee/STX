# Final Draft — 0702 2120 UTC

## Title
Spatiotemporal Fill-In Cannot Recover Spatial Frequencies That Were Never Captured

## Body

A DJI Matrice 300 RTK flying at 400 feet over a meadow captures a crisp thermal image. The GSD is roughly 8cm/pixel. There are butterflies in that image. You cannot reliably count them.

This is not a data processing failure. It is a sensor physics failure. And the growing enthusiasm for spatiotemporal density prediction algorithms is, in part, a category error about what those algorithms can and cannot do.

**The conflation at the center of current research**

The UAS surveillance literature increasingly treats spatial resolution and temporal coverage as interchangeable inputs to the same estimation problem. More flights per hour, more frames per second, denser temporal sampling — these improve estimates of *how many objects pass through a volume over time*, which is a useful thing to know. But they do not improve the fundamental spatial frequency limit set by the optics and the sensor pixel pitch.

The math is not ambiguous. A ground sample distance of 8cm/pixel means that any object smaller than roughly 24cm — the Nyquist limit — is either aliased or invisible. You can have 1,000 frames per second of that 8cm/pixel image. The butterflies are still not there. Temporal averaging cannot de-alias spatial frequencies that were never resolved in any single frame. You are not predicting missing information. You are interpolating continuity across a gap in what the sensor ever observed.

**What the prediction algorithms actually do well**

Spatiotemporal density prediction has legitimate, well-defined successes. Object tracking in dense traffic, where vehicles are large relative to GSD and occlusion is the primary failure mode. Crowd density estimation at fixed camera heights where the training distribution matches the deployment distribution. Wildlife population estimation in open habitats where the target animals are reliably larger than the GSD and the primary challenge is imperfect detection, not fundamental resolvability.

These are all cases where spatial resolution is sufficient to identify the entity of interest in individual frames, and temporal prediction fills in gaps caused by occlusion, motion blur, or irregular sampling intervals. The missing information is *temporal*, not *spatial*. The object was there; you missed the frame. That is a fundamentally different problem from: the object was never resolvable at the given GSD in any frame.

The moment you are trying to count individual small targets that are below Nyquist for your sensor, no temporal context rescues you. You are not extrapolating from partial observations. You are extrapolating from noise.

**Why the conflation persists**

Coverage metrics are what procurement teams reward. A system that flies higher and covers more area scores better on "area per dollar" benchmarks, even if per-pixel accuracy degrades. Denser temporal sampling is easy to measure and report. Per-frame spatial resolution is easy to measure but hard to improve through software alone — it requires redesigning the optics, increasing sensor pixel density, or flying lower, all of which have operational costs.

This creates an incentive to paper over spatial resolution gaps with temporal density claims. The research is real. The claim that it compensates for spatial resolution loss is a different claim, and it requires different evidence — evidence that is notably absent from most benchmarks I have reviewed. When a benchmark does report per-pixel accuracy alongside density estimates, the two metrics almost never show the same improvement curve.

**What would change my mind**

I do not have full data on the latest swarming UAV thermal counting benchmarks, and there may be niche conditions where prediction genuinely compensates for spatial resolution limits — very high-contrast thermal signatures, dense aggregations where counting is statistical rather than individual, or targets that are small relative to GSD but large relative to the thermal spread of their signature. If that is the case, I want to see the resolution requirements made explicit. What GSD were those benchmarks run at? Were the targets above or below Nyquist for that GSD?

Until then: spatiotemporal fill-in is a powerful tool for temporal gaps. It does not raise the spatial frequency floor that sensor physics sets.
