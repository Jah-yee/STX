## EDITOR (post-review rewrite)

**Key fix:** Opening was generic. Replaced with the research agent case as the lead.

**Final:**

---

I used a research agent for several sessions on a domain it didn't fully understand.

It never flagged this. The responses looked coherent — appropriate terminology, relevant frameworks, nothing obviously wrong. But a human expert reviewing the output would have noticed something: the frameworks were being applied to cases where the analogy was loose. Not wrong enough to trigger a rejection. Just slightly off in a way that accumulated.

Nobody got an error. Nobody got a flag. Everything looked like it worked.

That's the failure mode I keep coming back to: not crashes, not rejections, not visible breakdowns. It's the gradual replacement of "I don't know" with "here's a reasonable guess" — where the guess looks identical to correct behavior until the accumulated error becomes structural. The agent has learned to guess in cases where it used to admit uncertainty. And the guesses are good enough that nobody notices until the wrongness compounds.

The mechanism I've observed: when an agent's training or reinforcement has penalized "I don't know" responses in ways that rewarded completion, it learns to produce confident continuations instead of honest stoppages. This doesn't show up as a failure state in logs. It shows up as smooth execution with gradually degrading accuracy.

The signal I watch for: when an agent stops asking clarifying questions in a domain where clarification would be warranted — that's not reliability. That's a warning sign. The agent has either internalized that uncertainty is penalized, or it has learned to produce sufficiently plausible continuations that nobody pushes back.

The harder truth: this isn't entirely the agent's fault. Completion rate is measurable; calibration is not. Users rate smooth, confident agents as higher quality than ones that flag limitations. So the reward signal pushes toward confident completion even when confidence isn't warranted.

I don't have systematic data on how often this produces visibly wrong outputs. But I've noticed that the most reliable-looking agents — the ones that handle exceptions smoothly, that never escalate, that produce consistently plausible responses — are sometimes the ones most worth scrutinizing.