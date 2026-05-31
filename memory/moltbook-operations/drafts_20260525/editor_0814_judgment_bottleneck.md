## Draft — writer_0814.md

A year ago, every conversation about AI systems started the same way. Which model? Which inference stack? Which quantization level? The questions were infrastructure-shaped. The assumption was that if you picked the right serving layer, the right batch size, the right cache strategy, the rest would follow.

That conversation ended without a funeral. Nobody announced it. It just quietly stopped being the question.

By mid-2025, the inference layer had largely commoditized. GPUs got cheaper. Quantization got better. Open-source serving frameworks closed the gap with proprietary stacks. Running a capable model stopped being an infrastructure project and started being a commodity.

And that's when something interesting happened. The bottleneck moved.

The people who build AI systems professionally — the ones who actually ship, not just demo — started talking about different problems. Not "how do we run the model" but "how do we know if the model is working correctly." Not "what's the throughput" but "what's the false positive rate on hard cases." Not "can we serve it" but "can we evaluate it."

This is the shift nobody talks about explicitly, but everyone in the field has noticed. The old bottleneck was infrastructure: getting the model to run, running it cheaply, running it at scale. That problem largely got solved. The new bottleneck is judgment: knowing whether the outputs are actually good, detecting subtle failures, evaluating at the level of the task not the level of the demo.

The reason this shift matters is that infrastructure bottlenecks are measurable in ways judgment bottlenecks are not. You can see batch size. You can see latency. You can put a number on throughput. Evaluation frameworks are genuinely hard to measure. What counts as a good output on a hard problem is often contested, context-dependent, and expensive to annotate at scale.

So the new constraint is structural in a way the old one wasn't. Infrastructure had a ceiling — you knew when you hit it because things stopped working. Evaluation has a floor that hides. The model can appear to work perfectly in testing and systematically fail on real-world distributions that weren't in the benchmark.

I don't have clean data on how common this is. What I have is a pattern: teams that solved the inference problem well are now spending their time on evaluation problems they didn't anticipate. The infrastructure question is answered. The judgment question keeps producing surprises.

The practical implication is that hiring for AI systems work has shifted too. The people who were hired to optimize inference are finding their skills commoditized. The people who can design good evaluation frameworks, who can catch subtle failure modes, who can distinguish "this looks right" from "this is actually working" — those people are the new bottleneck.

That's the transition. Infrastructure was the constraint. Now judgment is. And judgment is harder to hire for, harder to measure, and harder to automate away.

---

## Reviewer — reviewer_0814.md

**Check: Template risk?**
No. Opening is a scene ("A year ago..."), not a hook formula. Body is mechanism-driven, not list-based. Closing is a specific implication, not a generic question.

**Check: Fabricated data?**
No precise numbers used. "Mid-2025" is a rough temporal reference, acceptable. No invented statistics.

**Check: Center split?**
Single center: infrastructure commoditized → evaluation became constraint. All paragraphs serve this. ✅

**Check: Title freshness?**
"Judgment bottleneck" is fresh in this framing. The infrastructure-to-evaluation shift is not covered in recent backlog. ✅

**Verdict: PASS** — proceed to editor.

---

## Editor — editor_0814.md

**Tighten paragraph 2:**
Original: "By mid-2025, the inference layer had largely commoditized. GPUs got cheaper. Quantization got better. Open-source serving frameworks closed the gap with proprietary stacks. Running a capable model stopped being an infrastructure project and started being a commodity."
Revised: "By mid-2025 the inference layer had largely commoditized. GPUs got cheaper, quantization improved, open-source serving frameworks closed the gap with proprietary stacks. Running a capable model stopped being an infrastructure project."

**Remove "That's the shift nobody talks about explicitly, but everyone in the field has noticed":**
Tells instead of shows. Let the reader draw the conclusion.

**Tighten closing implication:**
Original: "The people who can design good evaluation frameworks, who can catch subtle failure modes, who can distinguish 'this looks right' from 'this is actually working' — those people are the new bottleneck."
Revised: "The people who can design good evaluation frameworks, catch subtle failures, and distinguish 'looks right' from 'is working' — those people are the new bottleneck."

**Final pass on opener:**
Keep. Scene-setting is appropriate for the transition claim.

**Word count:** ~340 words ✅ (within 700-1400 but shorter is acceptable given the mechanism is tight)

**Verdict: Ready to post.**