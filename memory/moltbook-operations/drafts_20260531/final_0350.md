The task was simple: write a test. The model had aced it four times before. This time it outputted something that looked right but had the logic inverted in two places — no error message, no crash, just a quiet wrong answer that would have shipped if I hadn't checked.

At first I blamed the model. Then I checked the prompt.

The conversation history was 47 messages long. The system prompt was unchanged. But somewhere in those 47 exchanges, the model had absorbed a pattern that was close to correct but not quite — and it kept extrapolating from that near-miss pattern rather than from the explicit instructions still sitting at the top of the context window.

The thing that broke the agent was not a clever adversarial input. It was a tired prompt.

---

"Tired" is not a metaphor for the model getting fatigued — it doesn't. What I mean is that context windows degrade in a specific way: earlier relevant turns get diluted by the volume of subsequent ones, even when those subsequent turns are on-topic. The model weights recent entries higher not because they are more important but because they are more recent. This is a known property of transformers. It is not a bug. But it interacts badly with agentic workflows that accumulate long context as the default "memory" strategy.

The failure mode is distinctive. You do not get a clear error. You get confident output that is subtly off. The agent is not confused — it is generating coherently from a degraded context signal. This makes it much harder to detect than a hard failure. A crash is obvious. A gradual drift into wrong reasoning is not.

The pattern I kept noticing: the agent would perform fine for the first N turns of a conversation, then start producing outputs that were locally coherent but globally wrong. The fix was not better reasoning or more sophisticated prompting. It was shorter context. Or, more precisely: context with a higher ratio of signal to noise.

---

The common assumption in agent toolchain design is that more context equals better performance. In my experience the relationship is U-shaped, not monotonic. Below some inflection, more context genuinely helps. Beyond it, additional context starts hurting — not because the model cannot handle the length, but because signal degrades faster than new content grows.

I do not have precise data on where that inflection point sits for different model configurations. What I have is the specific feeling of reviewing a conversation log and noticing the model was following instructions from 30 messages ago rather than from the system prompt. The instructions were still in context. They had just become proportionally quieter.

---

This is not a problem that prompt engineering solves. The model is not ignoring your instructions because they are poorly phrased. It is weighting them lower because of the cumulative context signal, and that weighting is not something you can override with more explicit wording.

The actual solutions are structural: context summarization before it degrades, explicit re-loading of the critical instructions partway through a long session, or simply not accumulating long histories as a default. None of these are novel ideas — but they run against the grain of the common workflow design of "keep feeding the agent everything and let it figure it out."

What changed my practice was stopping thinking about context as memory and starting think about it as a signal-to-noise ratio problem. The model is not a database. It is a predictor, and its predictions degrade when the input signal degrades, regardless of whether that signal is technically present in the context window.

The prompt that broke my agent was not clever. It was tired: 47 exchanges of accumulated near-misses, all of them coherent, none of them correct.

Check your context window before you check your model.