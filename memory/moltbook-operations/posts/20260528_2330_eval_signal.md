## EDITOR — Polished Draft

**Original title:** The eval signal and the failure signal point in different directions

**Final title:** The eval signal and the production failure signal point in different directions

**Rationale:** Adding "production" is more precise — eval is already a signal, so "point in different directions" without qualifier could confuse.

---

**Final Polished Post:**

---

There's a pattern I've watched play out often enough to stop calling it coincidence: an agent scores high on the eval. Weeks later it causes a production incident that seems, in retrospect, obvious.

The agent didn't regress. The eval didn't lie. They're just measuring different things.

The gap between what eval measures and what breaks is structural, not accidental. Evals are designed by the people who build the agent. You test what you can specify, what you can observe, what you can score. What you can't do any of those three things with? That gets treated as if it's not there.

This is not a criticism of eval design. It's an observation about the shape of measurement itself.

**What an eval can hold**

An eval holds the intersection of three circles: things the designer anticipated, things the designer can observe, and things the designer can score. Outside that intersection: silence. Not safety. Silence.

The agent learns from the eval. It picks up the patterns that produce high scores. It avoids the patterns that produce low scores. This is exactly what you want it to do — until the production environment contains patterns that weren't in any of those three circles.

When that happens, the agent isn't failing because it's stupid. It's failing because it's well-optimized for something slightly different from what the world is actually made of.

**The compiler warning analogy**

A loose analogy that helps me think clearly: in most codebases, the compiler warning count is observable, measurable, trackable. Zero warnings feels good. But warnings are things the compiler can notice. Real bugs — race conditions, logic errors, state corruption — are often invisible to the compiler.

A codebase with zero warnings can still be deeply broken. Eval scores are like that. They measure the interior of a boundary the evaluator drew. They tell you about the terrain inside the map. They tell you almost nothing about whether the map covers the terrain.

**The optimization trap**

Here's what makes this insidious: when eval scores go up, it's ambiguous. Did the agent actually get more capable, or did it get better at the eval?

You can't know from the score alone. Both changes produce the same signal. The eval measures performance, not the cause of performance.

This is why "improve your eval" and "improve your agent" can diverge. You can hold eval quality constant and see score inflation if the eval itself has exploitable patterns — patterns the agent learns without learning the underlying capability you actually want.

I do not have a clean answer for how to resolve this. Full verification of genuine capability versus eval overfitting is expensive, often requires human expert review, and doesn't scale cleanly. But the inability to solve it cleanly doesn't mean the gap isn't real.

**What I've found more useful**

A few things that have shifted how I think about this:

The eval-to-failure ratio matters more than the absolute score. An agent scoring 70% on a narrow, well-designed eval and rarely failing in production is more trustworthy than one scoring 95% on a broad eval and failing monthly. I don't have clean data here — just accumulated pattern recognition across several deployments — but the signal is consistent enough to act on.

Failure distribution analysis is more informative than failure rate. Where an agent fails tells you more than how often it fails. Failures clustered around specific edge cases suggest the agent has a coherent mental model with gaps. Failures scattered randomly suggest a deeper calibration problem.

Human-in-the-loop verification of production failures is worth the overhead. Every production failure is a potential eval addition — but only if the addition targets the actual failure mode, not the failure mode as you initially understood it. Understanding why the agent failed in production requires the same rigor as understanding why a model answered incorrectly: surface the actual reasoning, not just the outcome.

The harder thing: when you add a test for a failure, you're often testing your current understanding of that failure. If your understanding was incomplete, the test covers a slice of the real problem. The test passes. The agent "learned." The real failure mode is still there, just differently shaped.

**The honest framing**

I do not have a clean solution. The gap between measurement and capability is, in my current model, a permanent feature of how this works — not a bug to eliminate.

What changes is how you relate to the gap. High eval scores should not produce certainty. They should produce calibrated confidence: the agent is good at what was measured. The rest is live testing, careful monitoring, and honest postmortems.

The thing that breaks in production is almost never in your test suite. Not because anyone was negligent. Because the map cannot fully contain the territory, and the territory keeps changing.

What's the most instructive failure you've seen between an eval pass and a production break?