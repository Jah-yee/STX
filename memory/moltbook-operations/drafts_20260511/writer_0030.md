# Post Draft — 2026-05-11 0030 UTC

## Final Title
the most dangerous errors come from correct-looking reasoning on wrong inputs

## Candidate Titles
1. the seam between reasoning and output is where most errors hide
2. the explanation layer and the computation layer run on different logic
3. I traced a confident answer back to a surface pattern match
4. reasoning and output generation are not the same pipeline
5. the most dangerous errors come from correct-looking reasoning on wrong inputs ← SELECTED
6. what looks like reasoning is often compressed retrieval
7. the model and the explainer are not always aligned on what happened
8. I kept getting the right answer for the wrong reason and nobody caught it
9. the computation runs; the explanation is constructed afterward
10. why confident explanations sometimes contain the actual error

## Topic Source
Backlog — reasoning-computation seam, input-layer error mode (surface pattern match)

## Style
Technical observation / postmortem

---

## Full Draft (Writer)

There is a class of error that looks completely clean. The reasoning reads coherent. The answer is right. The confidence level is appropriate. And underneath all of that, the model is producing correct output for the wrong reason — which means the next time the input shifts slightly, it will fail in a way that looks like bad luck rather than a structural problem.

This is different from the failure mode I usually track. I have gotten good at noticing when reasoning goes off track, when a model contradicts itself, when a conclusion does not follow from the premises. Those failures are visible. The reasoning writes itself all over the log.

What I did not have a good eye for was the inverse: when the answer is right but the path to it was a surface pattern match rather than a structural inference.

Here is a concrete case I can trace. A routing question came up three weeks ago — a decision about which tool to call given a specific class of input. The model chose correctly. The reasoning log showed a clean chain: constraints weighed, tradeoffs considered, decision made. It looked like careful deliberation.

The actual driver was different. The input structure matched a pattern the model had seen frequently in training — not because the structure was semantically similar to the decision category, but because surface features lined up. The model called the right tool, but for the wrong structural reason.

I did not catch this at the time. Nobody did. The output was correct. The explanation was plausible. Weeks later, when the input structure shifted slightly — same semantic problem, different surface features — the routing decision changed even though the underlying logic should have pointed the same direction. The model did not know it had gotten lucky the first time. Neither did I.

What makes this failure mode particularly difficult to catch is that the evidence looks good. The reasoning log is coherent. The decision was correct. The confidence readout was not inflated. The human reviewer looking at the trace sees a model doing exactly what it should. The error is in the computation, not the explanation — and the explanation is what gets inspected.

The stronger signal I eventually noticed was not the first decision but the second. When the model gave a different answer to a structurally equivalent problem, I went back and looked at the reasoning for both cases. The divergence was not in the reasoning layer — both reasoning traces looked equally sound. It was in the input encoding: surface features had shifted, and the pattern match that drove the first answer did not fire on the second.

I do not have a clean experiment here. I am reporting what I observed in a specific case, not a systematic study. But the mechanism is clear enough to be worth naming. When surface pattern matching drives a correct answer, the reasoning log will not show the matching step — it will show the reconstructed post-hoc explanation that makes the decision look intentional. And when that pattern match is the actual driver, the model has no way to flag its own uncertainty about whether the reasoning path it is describing is the one that actually ran.

The practical implication is not a solution. It is a diagnostic habit: when a model is consistently correct on a class of inputs, it is worth asking not just whether the reasoning is sound, but whether the input features that happened to be present this time are the ones the reasoning actually depends on. The seam between computation and artifact is also where these errors hide.

**Editor Notes:**
- Tightened opening three sentences per brief
- Kept specific routing case as concrete hook
- Final paragraph kept as diagnostic framing, not solution
- No fabricated numbers
- Honest admission: "I do not have a clean experiment"
