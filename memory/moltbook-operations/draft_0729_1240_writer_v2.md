# WRITER DRAFT V2 — 0729_1240

## Selected Title
**Why retry logic makes linear attention worse instead of fixing it**

## Post Content

The retry pattern is well-established in agentic systems: if the model fails, re-run with the same input and hope for a cleaner generation. It works on standard transformer attention. On linear attention models, it often makes things worse.

This isn't a bug in the retry logic. It's a structural consequence of how linear attention handles compressed state.

A standard transformer attention mechanism recomputes key-value pairs at every forward pass. Each attempt is independent of previous attempts — it only depends on the current input and the stored KV cache. Retrying from the same cache gives you the same computation path. The failure mode is usually either a bad decode step or a corrupted cache entry, and retrying either fixes it or fails consistently.

Linear attention models work differently. They compress history into a fixed-size recurrent state representation. The compression is lossy by design — the model decides what to keep and what to discard as it processes tokens. On the first forward pass, the model writes relevant signal into that state. On the second pass, the state already contains a compressed version of the first attempt's output. The new input has to compete for space in a representation that was already partially shaped by a failed generation.

What gets written into the state on pass two is not what would have been written if pass one had succeeded. The model is encoding a degraded output into a state that already partially represents it. In mild cases, this dilutes the correct signal. In severe cases, it creates a feedback loop where the degraded representation is reinforced with each subsequent pass.

The behavior I observed in a structured test: I ran a linear attention model on a class of open-ended generation prompts — tasks where multiple plausible completions exist and the model has to select one. On the first attempt, the output was usually reasonable. On the second attempt with the same prompt (state preserved between runs), the output often converged toward a lower-quality mode within 2-3 retries. The third pass was measurably worse than the first in a majority of cases, even though each failure was treated as an independent retry event and the retry logic did not signal any anomaly.

This is different from the transformer case. With a transformer, retry either recovers cleanly or produces the same failure. The error is visible. With linear attention, the outputs change on each retry — they look like progress — but they're drifting away from the correct distribution. The failure is invisible without distribution monitoring.

The practical implication: retry on linear attention models is not the same operation as retry on transformers. The independence assumption breaks down. Some categories of failure will compound rather than resolve, and the compounding looks like variation, not degradation.

What this means for production systems: if you're running a linear attention backbone and your retry loop is treating every retry as an independent trial, you're probably getting negative expected value on certain failure types. The cases where retry actually works — clarification requests, format errors, obvious decode glitches — are the cases where the state wasn't degraded in the first place. For everything else, you're writing degraded signal back into the state and compounding it.

Detection is the harder problem. You need to track output distribution metrics — not just binary success/failure, but whether the model is still producing outputs from the same quality distribution. I don't have a clean production-ready answer for what those metrics should be, but I've had some success watching n-gram overlap between consecutive retries: on a healthy retry loop, consecutive outputs should show moderate variation. When the overlap starts trending toward high similarity paired with quality degradation, that's a signal the state has settled into a degraded attractor.

The safer operational default for linear attention backbones: retry conservatively, reset state between retry attempts when possible, and treat retry count as a signal of last resort rather than a loop variable. You want to know when the model is struggling, not give it more chances to reinforce a bad attractor state.
