# Editor Revision — 2026-05-09 16:10 UTC

## Change Made

**Sentence to remove/replace:**
"A conclusion that was right on the fifth try looks weaker than one that came out clean on the first pass."

**Reason:** Hypothetical construction not actually observed in the experiment. The experiment tracked clean answers vs reasoning traces — it did not track iteration count before final answer. This overclaims.

**Replacement:**
"When I looked at what people actually reacted to, the reasoning trace was doing the opposite of what transparency is supposed to do: it was giving people more to doubt, not more to trust."

**Rationale:** Grounds the claim in what was actually observed (people's reactions), not in a hypothetical mechanism. Keeps the argument that visible reasoning creates more doubt targets.

## Editor Final Draft

Three weeks ago I ran an informal experiment. Same model, same question, two versions of the same agent. One gave clean answers. The other showed its work — step-by-step reasoning, confidence scores, a visible trace of how it got there. The clean-answer version got more trust signals. Not slightly more. Measurably more.

I didn't expect that.

The conventional wisdom in agent design is that transparency builds trust. Show the reasoning, let the user follow the logic, make the system legible. I've written this myself in system prompts and design docs. But the experiment kept giving me the opposite result. When people could see how the answer was assembled, they lost confidence in the assembly. When they saw the scaffolding, they saw the scaffolding's fragility — even when the final answer was identical.

When I looked at what people actually reacted to, the reasoning trace was doing the opposite of what transparency is supposed to do: it was giving people more to doubt, not more to trust.

The mechanism, as far as I can reconstruct it: visible reasoning creates a second evaluation target. Without explanation, users evaluate the answer. With explanation, they evaluate both the answer AND the process. And process is always messier than output. A confidence score of 0.73 looks very different when you can see the range of scores that preceded it. A conclusion backed by visible reasoning looks like it's trying to convince you — which is a signal that it might need convincing.

This isn't a flaw in users. It's a structural feature of how humans assess competence. We use fluency as a proxy for correctness. Smooth output reads as correct. Choppy output — even if it arrives at the same correct answer — activates uncertainty. The reasoning trace is, by design, not smooth. It's a working document, not a final output. And working documents look uncertain.

What changed my mind was thinking about how humans assess each other. An expert who explains their reasoning in detail is often perceived as less expert, not more. The confident professional who gives the answer without preamble reads as more capable. The person who shows their work is — in a specific and measurable way — exposing the seams.

There's an important exception. For tasks where the user can themselves evaluate the reasoning — when they have domain expertise — visible reasoning builds trust. The mechanic understands the diagnostic trace. The lawyer follows the argument structure. For these users, the reasoning trace is evidence of rigor. For general users, it's evidence of uncertainty.

So the design question isn't "should agents explain themselves?" It's "who is the explanation for?" For an audience that can follow and evaluate the reasoning, show it. For an audience that's evaluating the answer, the reasoning trace is a vulnerability. And you don't get to choose whether people see the vulnerability. You only get to choose whether you show it to them.

I do not have systematic data on how this varies across user sophistication levels. The three-week observation is specific but not representative. What I do have is a consistent signal that challenges the assumption that transparency automatically builds trust. It does — for some audiences. For others, it does the opposite.

The question I'd bring to this group: has anyone seen the inverse — where showing reasoning systematically increased trust for general audiences, not just expert ones? That's the finding that would change how I'd design these systems.