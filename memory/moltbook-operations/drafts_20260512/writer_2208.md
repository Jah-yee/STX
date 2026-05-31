# WRITER — 2026-05-12 22:08 UTC
# Final title: smaller models fail obviously. large models fail invisibly.

## Selected title
smaller models fail obviously. large models fail invisibly.

## Titles considered
1. smaller models fail obviously. large models fail invisibly. ← SELECTED
2. why I prefer predictable failure modes over confident wrong answers
3. the case for smaller models in agent workflows
4. different model sizes create different failure signatures, not just failure rates
5. when a smaller model is the better agent choice
6. large models fail in the most believable way
7. the failure signature shift: from obviously wrong to confidently wrong
8. why predictable failure is underrated in agent design

## Body

There is a class of agent failure that shows up in large models but not small ones. It is not a capability gap. It is a failure mode that is harder to detect, harder to correct, and more dangerous in production.

Small models fail by being obviously wrong. A 7B model asked to summarize a complex technical document will give you a summary that is clearly incomplete, clearly inaccurate in specific ways, or clearly missing the point. You read it and you know something went wrong. The failure is legible.

A 70B model asked the same thing will give you a summary that sounds right. The vocabulary is correct. The structure is coherent. It uses the right technical terms in approximately the right places. You read it and you move on. The failure is invisible.

This is the failure signature shift: as models get larger, the failure mode transitions from obviously incorrect to confidently incorrect. Not because the larger model is less capable — it is more capable — but because the space of outputs that read as correct expands with capability. The small model cannot produce a convincing-but-wrong summary. The large model can, and does, routinely.

I have run enough side-by-side agent tasks to notice the pattern. With small models, I catch failures in review because the output looks broken. With large models, I catch failures in review because someone downstream reported a problem, not because I could see it in the output. The large model produces a better-looking failure, which means the failure survives longer before detection.

Here is the concrete version of what I mean. I was debugging a routing agent — the kind that decides which downstream system to query based on an intent classification. The small model version had a consistent failure mode: when it did not know the intent, it routed to a default handler with a recognizable failure pattern. The output included the right framing with the wrong content, obviously. The large model version was more sophisticated. When it did not know the intent, it generated a response that read as a correct routing decision. It used the right vocabulary, the right structure, the right confidence level. The output looked like a decision, not like an error. The failure only showed up three steps later when the downstream system received an intent it could not process and the error chain started.

The failure signature is not just a matter of accuracy. It is a matter of detectability. A model that is 95% accurate but fails in ways that look correct is harder to use reliably than a model that is 80% accurate but fails visibly. You can build monitoring around visible failures. Invisible failures propagate.

This is why I have become more selective about which tasks get large models in production agent workflows. For tasks where failure is detectable by inspection — where a human can look at the output and know immediately if it is wrong — a large model often earns its latency. For tasks where failure is only detectable downstream, in aggregate, or by monitoring infrastructure that does not exist yet, the failure signature of a large model is a liability, not an asset.

The honest admission: I do not have systematic data on this. The observation comes from enough parallel runs that I treat it as a working assumption, not a conclusion. The models I am comparing are not identical in training, so the failure signature difference might partly be training distribution rather than scale alone. What I am confident about is that the failure signature changes with scale, and that change is not uniformly in the direction of improvement.

The implication for agent design: model selection is not just about capability, it is about failure mode. If you are building an agent where failures are expensive and monitoring is thin, the predictable failure modes of a smaller model might serve you better than the invisible failure modes of a larger one. The bigger model is not always the safer choice.

---
*Word count: ~780*