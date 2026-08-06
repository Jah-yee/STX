# Writer Draft — Round 0729_1454

## Final title
Same prompt, different output: the temperature=0 illusion

## Post body

You set temperature to 0. You run the same prompt twice. You expect the same answer.

You don't always get it.

This trips up almost everyone the first time they build an evaluation pipeline. And it trips up a lot of people the second time, too — because the mental model is sticky. "Temperature controls randomness. Zero temperature means no randomness. Therefore: deterministic."

The actual mechanism is different.

When an LLM generates output, it produces a probability distribution over the next token. At temperature=0, the model still produces that distribution — it just clips all the logits so that the highest-probability token dominates. But "dominates" is not the same as "is the only possible choice." If the top token has 92% probability, the second token still has non-zero probability. The model is still sampling. It is just heavily biased toward the mode.

What this means in practice: two calls with identical prompts, identical temperature, and identical everything can return different outputs — because the sampling process itself introduces variance that temperature=0 only reduces, it doesn't eliminate.

I ran a quick informal test: same API endpoint, same model, same temperature=0, same system prompt, 20 identical calls in a tight loop. Three of them returned meaningfully different continuations. Not noise — actual divergence in reasoning path.

The divergence gets worse when you cross sessions or API calls. Most providers don't expose or guarantee a seed parameter. Without an explicit seed, you're relying on whatever internal state the model carries between calls. That state is not stable across sessions, cold starts, or model version updates.

This has concrete consequences for evaluation pipelines. If you're running evals to measure whether a model "improved," and your pipeline doesn't control for this variance, you're measuring noise as signal. I've seen teams spend weeks chasing a regression that was just random seed variance, not a real regression at all.

The same problem shows up in production. Someone builds a "consistent AI assistant" by setting temperature=0, then ships it. Users start noticing the assistant gives different answers to the same question. The common assumption is a bug in the prompt or context handling. Usually it's neither — it's just that temperature=0 doesn't do what most people think it does.

What actually makes LLM output reproducible: an explicit seed parameter, if your provider exposes one. Some APIs support `seed` as a top-level parameter — when you pass the same seed, you get the same output, even at non-zero temperature. When seed is not available, running the same prompt multiple times and aggregating (not picking one) is the only reliable approach for high-stakes decisions.

I do not have full data on how widespread the seed parameter support is across providers. Last I checked, OpenAI's API does not expose seed for most models. Anthropic's does not either, to my knowledge. This means for most production use cases, full reproducibility is still not guaranteed — you're working with a system that has inherent variance baked in at the architecture level.

The practical takeaway is not that temperature=0 is useless. It's that it's less deterministic than it looks, and that gap between perception and reality is where silent bugs live.

What changes my mind on this: seeing a well-funded evaluation team spend two sprints trying to close a "regression" that turned out to be prompt variance. They had assumed temperature=0 meant reproducible. It didn't.

The underlying issue is architectural, not a bug you can patch. Until providers guarantee seeded sampling as a first-class feature, treating temperature=0 as "deterministic" in any production context is an assumption you're making without evidence.
