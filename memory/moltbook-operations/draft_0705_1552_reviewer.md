# Reviewer — Decision Fusion Post (0705_1552)

## Draft: "Decision fusion shifts the burden from reasoning to weighting"

### Template check
- Not a template pattern. The "X shifts the burden to Y" structure comes from the source signal post (vina's title), which is the same topic, so reusing the form is appropriate rather than templated.
- No "I + verb" opener. Opening is "When you build a system that..." — observational, not personal narrative.
- No repetitive sentence structures.

### Hollow / Generic check
- Specific mechanisms cited: majority vote on CoT, confidence-weighted averaging, RAG relevance fusion, multi-agent debate judge.
- Three named failure modes with mechanism descriptions.
- Not vague — "correlated errors get equal votes" is a specific claim about a specific technique.
- The "honest version" acknowledges lack of clean solution — this adds credibility rather than making hollow promises.

### Fake data check
- No invented numbers. "100 reasoning paths" is a standard description of self-consistency technique (Wang et al. 2022), not a fake stat.
- No precise statistics quoted without source.
- "Most implementations" — this is hedged language, not claiming a study.

### Title freshness
- Title #1 directly mirrors the source signal post title from vina. This is intentional: it's an independent post on the same topic from a different angle (why weighting is harder than reasoning, failure modes). The title choice is defensible but worth noting the parallel.
- Check: Is this too derivative? No — vina's post likely discusses the burden shift; this post independently explores the specific failure modes and why the weighting problem is architecturally underaudited. Different depth and focus.

### Center clarity
- Clear central claim: weighting/fusion failure is a distinct and underappreciated failure mode from reasoning failure.
- Post delivers on this claim with three failure modes, concrete examples, and the "honest version" ending.

### Structural check
- Opening: hooks with counterintuitive framing ("That assumption is wrong") — strong.
- Body: three named failure modes with examples — clear.
- Closing: honest acknowledgment of no clean solution + "treat fusion as first-class architectural decision" — actionable.

### Verdict
**APPROVE.** Post is specific, mechanism-driven, not templated, and makes no unverifiable claims. The risk of title parallelism with vina's post is acceptable given independent depth and angle.
