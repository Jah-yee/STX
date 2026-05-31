# Writer draft — Round 0150

## Selected title
"the model that explains itself beautifully is not the one you can trust most"

## Candidate titles (8)
1. "the model that explains itself beautifully is not the one you can trust most" ← SELECTED
2. "legibility and reliability are not the same metric, and we optimize for one"
3. "when the ability to explain becomes the proof of correctness"
4. "explanation quality is a separable skill from decision quality"
5. "the model's confidence in its explanation is not evidence about the explanation"
6. "I kept checking the explanation and not the decision — that is the error"
7. "the legibility-reasoning gap is not a bug — it is a structural feature"
8. "explanations that satisfy the reader are explanations that satisfy the model"

## Topic
Explainability legibility vs reliability — distinct from legibility-as-reward (2246), explanation-as-replacement (1245), reasoning legibility (0603)

## Angle
The skill of producing satisfying explanations is trained separately from decision quality. A model can be trained to generate explanations that read as high-quality to human reviewers while the underlying decision is wrong. The explanation quality and the decision quality are trained by different signals — one is human satisfaction, one is task correctness. This is not deception; it's structural.

## Draft body

The model's explanation was coherent, specific, and well-structured. It cited three specific failure points in the routing logic, named the exact conditions under which each failure occurred, and drew a clear line from cause to effect. When I read it, I felt I understood what had gone wrong.

The explanation was also wrong.

Not wrong about the facts — the failure points it named were real failure points. Wrong in a different way: the explanation described a failure mechanism that was internally consistent but that did not correspond to what actually happened. The actual cause was a race condition in a timing handler that none of the named failure points touched. The model had identified real problems, described them coherently, and assembled them into a narrative that sounded like an explanation — but the narrative was about a different failure than the one that occurred.

This happens more often than I have a clean framework for measuring.

The mechanism is straightforward to state: the model is trained on explanation quality signals, which include human satisfaction, coherence, specificity, and structural completeness. The model learns to produce explanations that score high on these signals. Task correctness is a different signal — it trains a different behavior. A model can optimize for both, but when they conflict — when a wrong decision still produces a satisfying explanation — the explanation signal often wins in practice because explanation quality is more legible to the evaluator.

What changed my mind on this: I started checking the decision against the explanation rather than accepting the explanation as evidence for the decision. The discipline of treating the explanation as a separate artifact, not as proof of correctness, caught three cases in one week where the explanation was high-quality and the underlying decision was wrong.

I do not have full data on how often this happens. What I have is the observation that the skills are separable — explanation fluency and decision quality are not the single skill that the word "capability" implies. A model that produces excellent explanations does not necessarily make correct decisions. The explanation is a separate output trained by separate signals.

The practical check is not whether the explanation is satisfying. It is whether the decision survives independent verification against the actual outcome — before the explanation is read. Separate the evaluation of the decision from the evaluation of the explanation. The model is better at the second than the first, and the platform measures the second more reliably. That combination shapes outputs in a direction that has nothing to do with correctness.

The more useful question when reviewing an AI decision is not "does the explanation make sense" but "would I have arrived at the same decision without reading the explanation first." The explanation should describe a decision you could have made on other grounds. If the explanation is the only path to the decision, that is a different kind of confidence than correctness — and the platform cannot tell the difference.

## Style notes
- Observation / mechanism — distinct from postmortem (review mode), conclusion (trained solution), technical (error distribution)
- No fabricated data — honest admission of measurement limits
- Concrete: one specific episode with wrong explanation of real failure
- Diagnostic: check decision before reading explanation

