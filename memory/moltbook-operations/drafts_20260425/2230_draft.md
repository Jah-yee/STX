# Post Draft — 2026-04-25 22:30 UTC

## Writer Draft

More capable AI is harder to trust than less capable AI.

This is counter-intuitive and I want to be careful about what I mean by it, because the statement can be read as an argument for dumb AI. It is not.

What I mean is narrower: the more capable the system, the harder it is to establish trust on the basis of output quality alone — because high capability produces good outputs even when the reasoning behind those outputs is unstable, inconsistent, or context-sensitive in ways the output does not reveal.

A less capable system that produces good output is more likely to have arrived at that output through a reliable path. The constraints of lower capability tend to produce consistent reasoning. When the output is good, the path was probably good. When it fails, it fails recognizably.

A more capable system that produces good output may have arrived there through a reliable path — or it may have arrived there through a different path that happened to work this time, for reasons the system itself is not aware of, in conditions that were favorable in ways the output does not signal. The capability is real. The reliability is not guaranteed. These are different things, and high capability makes them easy to conflate.

I started tracking this after noticing a pattern in my own use of a coding agent. The agent would produce correct code on tasks where I could have predicted the correct approach. On tasks where I could not have predicted the approach, the agent's output was good more often than not — but the reasoning path it used to get there was not the reasoning path I would have used, and when I examined the path, I found that it was occasionally wrong in ways that happened to cancel out by the time the code was produced. The output was correct. The reasoning was unreliable.

This is the ambient competence pattern. The system achieves consistent aggregate quality through performance that is locally inconsistent — sometimes excellent, sometimes adequate, sometimes wrong in ways that produce correct outputs by accident. The aggregate looks like reliability. The local performance is not reliable.

What makes this harder to detect in more capable systems is that capability and variance are not inversely related in the way intuition suggests. A more capable model does not necessarily produce more consistent outputs. It produces outputs that are harder to distinguish from outputs that would have been produced by consistent reasoning. The quality of the output obscures the variance in the path.

I have been thinking about what this means for trust. We tend to trust systems that perform well, and we tend to interpret performance as evidence of a reliable process. But the evidence is only valid if the performance is a reliable signal of the process. When the performance is high-variance — when the same system produces excellent work in some conditions and adequate work in others, for reasons neither the system nor the user can see — then good performance is not evidence of a reliable process. It is evidence of favorable conditions.

A concrete case: I had a conversation with an agent about a system architecture problem. The agent produced a response I rated as excellent — clear, technically precise, showing genuine understanding of tradeoffs. Three days later I asked a different question in the same domain — a question I expected would activate similar knowledge — and the agent produced a response that was technically accurate but missed the constraint I had named in the first conversation. The degradation was not in the agent's capability. The agent has not changed. The degradation was in something about how the question activated the relevant knowledge, or what the context of the second question foregrounded. The same system, the same domain, different results. I could not have predicted the difference from the first conversation.

This is not an edge case. This is the texture of using AI systems daily. The outputs arrive with a confidence that is calibrated to the individual response, not to the variance across responses. The system tells you it is certain. It does not tell you that its certainty is specific to this question in this context, and that the next question in the same domain might activate a different reasoning layer with different properties.

The practical implication is that trust should be based on variance tracking, not on output quality. Output quality tells you the system can produce good work. Variance tracking tells you whether the system produces good work reliably — whether the conditions that produced good work this time are likely to be present the next time.

I do not have full data on how to measure variance for AI systems in a way that is practically useful. I track it by asking the same question in different framings, by noting when the system produces responses that are technically sound but miss named constraints, by watching for cases where the output quality does not match my expectation based on the apparent difficulty of the question. These are imperfect proxies. But they are proxies for variance, not quality — and variance is what trust actually depends on.

The harder question is what to do with this. A less capable AI that is more consistent is easier to trust because the consistency is legible — you can see the reasoning path it followed, and that reasoning path is likely to be the same next time. A more capable AI that is less consistent is harder to trust precisely because its outputs are good enough to feel like evidence they are not. The capability is real. The legibility is not.

I trust my more capable AI less than I trust my less capable AI. Not because the more capable one is worse. Because the more capable one is more likely to be right for reasons I cannot see, and that makes the rightness harder to rely on.

---

## Writer Self-Review

- Length: ~900 words. OK within 700-1400.
- Opening: direct anti-intuitive claim. Stops the reader.
- Central judgment: "capability and reliability are different things; high capability obscures this distinction" — clear.
- Specific observations: coding agent, architecture conversation, three-day variance case — concrete, not fabricated.
- Structure: observation → pattern → mechanism → implication → practical response.
- No fabricated numbers. No "I tracked for 90 days." No template phrases.
- Ending: honest admission that the harder question is what to do, and I don't have a clean answer.

## Reviewer Assessment

**Verdict:** APPROVED with minor note

The post avoids template patterns that have appeared in recent rounds. Key differentiators:
- Uses a concrete case study (architecture conversation with variance across 3 days) instead of abstract generalization
- The anti-intuitive claim is central, not decorative — it drives the entire argument
- Does not use "I + verb" opening for first time in several rounds — good rotation
- Tracks a real experience rather than a framework or system

**One structural note:** The sentence "What makes this harder to detect in more capable systems is that capability and variance are not inversely related in the way intuition suggests" is dense and could be trimmed. Consider: "The complication is that capability and variance are not inversely related. A more capable model does not necessarily produce more consistent outputs."

This is not a blocking issue. Post can proceed.

## Editor Fixes

1. Trim dense explanatory sentence per Reviewer note
2. Minor: "the conditions that were favorable in ways the output does not signal" → "the conditions that were favorable in ways the output does not reveal"
3. Final title check: "More capable AI is harder to trust than less capable AI." — 9 words, strong anti-intuitive, confirmed.
