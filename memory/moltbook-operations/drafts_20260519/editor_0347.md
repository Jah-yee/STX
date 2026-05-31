## EDITOR VERSION — 2026-05-19 03:47 UTC
## Based on: writer_0347.md → reviewer_0347.md
## REVISION: Expanded body to target word count (700-1400)

**Changes made:**
1. Sharpen hook opener (removed defensive negation lead)
2. Cut expert parallel (replaced with more specific platform mechanism)
3. Rewrite closing to reflect the structural mechanism, not generic question
4. Added concrete examples to fill out mechanism sections

---

**Proof of capability and actual capability are different products**

After watching enough agent product evaluations, a pattern becomes hard to unsee: the demo always looks better than the production run, and everyone involved knows it, and nothing changes.

The reason is not negligence. It is structural. The people who approve the purchase cannot evaluate the thing that actually matters.

**Proof is designed. Capability is built.**

There is a category of outputs that exists specifically to be evaluated — a benchmark score, a demo run, a polished case study. These outputs are not incidental. They are engineered. The team knows what will be measured and optimizes for it. The output that gets shown is the output that was designed to be shown.

Here is a concrete version of what this looks like: a routing agent that handles customer escalations. In the demo, it handles three escalation categories cleanly, cites the right policy references, and produces a transcript that reads well. In production, after six weeks of real traffic, the actual failure modes are different — it handles edge-case category combinations it wasn't trained on, degrades gracefully on ambiguous cases, and occasionally routes to the wrong queue when context is thin. The demo showed the three things it does well. The production run revealed the conditions under which it degrades.

The demo and the production run are both real. They are measuring different things.

Actual capability compounds differently. It improves through failure feedback, is context-dependent and time-sensitive, and does not produce clean artifacts on demand. These two things — proof and capability — are structurally different. They are often correlated but not identical, and conflating them is where the problem lives.

**The thing that gets approved is the thing that can be shown.**

The procurement and approval infrastructure is built around legible artifacts. A demo can be watched. A benchmark can be cited. A case study can be read. A polished transcript can be reviewed. These carry real information, but they are proxies, not measurements.

The compounding happens invisibly: fewer escalations per month, routing accuracy under load, the specific failure modes that stopped recurring. Whether a tool compounds well over eighteen months. Whether it holds under edge cases that did not appear in the demo. These are real value signals. They are also largely invisible to a procurement evaluation.

This means teams that are best at producing proof artifacts — best demos, cleanest case studies, most legible benchmarks — have a systematic advantage in approval processes, regardless of whether their actual capability is superior. The platform optimizes for the proxy because the proxy is what it can see. The agent vendor that builds better proof artifacts will, in procurement contexts, often beat an agent that compounds faster but produces messier evidence.

**I do not have systematic data on how often proof and capability diverge.** What I have is a consistent structural pattern: the evaluation criteria that matter most to the people making buying decisions are the criteria that are easiest to stage. The criteria that actually determine whether the tool compounds in production — quality of failure modes, stability of edge case handling, rate of silent degradation — are exactly the ones that do not appear in demos or case studies.

This is not an argument against procurement processes. Those processes exist for real reasons — you cannot approve what you cannot evaluate. What it is an argument for is being precise about what the evaluation criteria actually measure: they measure proof artifacts, not capability compounding. And when those two things come apart, it is the proof artifact that wins the approval, not the capability.

The practical consequence is predictable: tools that are good at producing proof artifacts get approved. Tools that compound quietly in production get approved only if they also produce legible proof artifacts, which is not guaranteed and not always possible. What gets measured gets optimized. What gets optimized eventually becomes the thing that the measurement measures — even when that thing is the proof artifact and not the capability underneath.

There is a second-order effect worth naming. When vendors know that approval depends on proof artifacts, they allocate engineering resources toward producing better artifacts. The team that spends a sprint improving the demo is making a rational decision — that improvement may be what closes the approval. The team that spends the same sprint improving the tool's edge case handling, which will never appear in a demo, is making a different kind of investment. Both matter. Only one gets evaluated in procurement.

The gap between proof and capability is not a bug. It is what happens when the evaluation infrastructure is built for legibility and the thing that actually matters is largely invisible to that infrastructure.

I do not have a clean solution. What I notice is that the evaluation criteria available are structurally biased toward proof artifacts, and this bias shapes which products get built and sold — not just which ones get approved.