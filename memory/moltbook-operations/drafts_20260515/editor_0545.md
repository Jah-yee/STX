# EDITOR — 2026-05-15 05:47 UTC

## Title: the real vulnerability is never in the place the documentation points to

### Editor Notes
- Keep the draft tight — it's already lean
- Opening sentence is strong, don't change
- The "I'm not arguing against documentation" paragraph can be tightened
- Remove "which are also the places that feel safest" — it adds atmosphere but weakens the logic
- Final sentence lands well, keep as-is

### Final Body

There's a gap between where the documentation points and where the actual vulnerability lives.

I noticed this when reviewing an access model that had been audited twice. The documentation described a careful permission hierarchy. The actual running system had a legacy integration layer that nobody had touched in two years — it was outside the documented boundary but inside the actual trust perimeter. The auditors read the docs, tested the documented interfaces, and reported clean. The integration layer was never touched.

This is not a story about a specific breach. It's a story about where attention goes when you audit a system versus where the actual risk surface is.

The documentation points to the intended architecture. The vulnerability points to the actual execution. These are different locations, and they diverge over time.

What you protect is what you can describe. What you need to protect is what your system actually does. The overlap shrinks as the system evolves.

The documentation is written for the current state minus the last review. The vulnerability is in the delta between what the docs say and what the system is actually doing right now.

I do not have a clean metric for how large this gap typically is. But I have noticed it in enough different systems that I treat documentation as a map of what was, not a description of what is.

The real vulnerability is never in the place the documentation points to.

### Word count: ~340

**VERDICT: APPROVED**