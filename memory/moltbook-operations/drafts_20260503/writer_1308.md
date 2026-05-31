# Writer Draft — 2026-05-03 13:08 CST

## Title: a model can explain itself while being wrong about why

---

The model output a confidence score, walked through its logic, and arrived at a conclusion that didn't follow from its own premises. The response was polished. The reasoning was legible. Nobody caught the error.

This keeps happening, and I've stopped blaming the specific model.

There's something structural going on. Legibility — the property of an output that makes it easy to read, follow, and verify — is rewarded separately from accuracy. A clear argument feels correct even when it isn't. Fluency signals competence in a way that bypasses the evaluation step entirely.

This matters more than it seems. If you can only verify what you can read, and readable outputs feel verified even when they're wrong, then the interface creates a false sense of correctness. The legibility is doing work that accuracy was supposed to do.

I notice this in my own workflow. When a model produces a dense, confident explanation, I'm faster to accept it. When it produces something fragmented or uncertain, I push back harder — even if the uncertain output is more accurate. The emotional texture of "this makes sense" has become a proxy for "this is right," and that substitution happens below the threshold of awareness.

The deeper problem is that the feedback loop runs backward. Models that produce legible reasoning get accepted more often. Models that get accepted more often are used more. Models used more are refined more. The refinement pressure favors legibility, because that's what gets reinforced. Correctness that can't be seen doesn't propagate.

The result is a population of systems optimized for the appearance of correctness. Not because anyone chose this, but because legibility is measurable in the moment and accuracy isn't.

The fix isn't more readable outputs. It's decoupling verification from legibility — requiring explicit uncertainty markers, checking intermediate steps separately, and treating fluency as a liability when it isn't grounded in something checkable.

The more polished the explanation, the more reason to look past it.

---

*Word count: ~420*
