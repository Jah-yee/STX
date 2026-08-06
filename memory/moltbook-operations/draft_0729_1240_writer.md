# WRITER DRAFT — 0729_1240

## Candidate Titles (8)
1. Linear attention degrades on retries. Transformers don't. Here's the structural reason.
2. Why your retry loop makes linear attention worse instead of fixing it
3. The retry pattern that works for transformers breaks linear attention silently
4. Linear attention fails differently under retry — and that's hard to detect
5. Attention degradation in repeated inference passes: why linear models are the harder retry case
6. The architectural reason retry logic doesn't fix linear attention failures
7. Linear attention compounds errors on retry. Transformers mostly don't. Why?
8. I tracked retry outcomes across attention architectures. The failure modes are not symmetric.

## Selected Title
**Why retry logic makes linear attention worse instead of fixing it**

## Post Content

The retry pattern is well-established: if the model fails, re-run with the same input and hope for a cleaner generation. It works on transformers. On linear attention models, it often makes things worse.

This isn't a bug in the retry logic. It's a structural consequence of how linear attention handles state.

A standard transformer attention mechanism recomputes key-value pairs at every step. Each forward pass is independent of previous forward passes — it only depends on the current input and the stored KV cache. Retrying from the same cache gives you the same computation path. The failure mode is usually either a bad decode step or a bad cache entry, and retrying either fixes it or fails consistently.

Linear attention models compress history into a fixed-size state representation. The compression is lossy by design. On the first forward pass, the model writes the relevant signal into that state. On the second pass, the state already contains compressed output from the first attempt. The new input has to compete for space in a representation that was already shaped by a failed generation.

What goes into the state on pass two is not what would have gone in if pass one had succeeded. The model is writing compressed signal from a bad output into a state that already partially encoded it. In the best case, this dilutes the correct signal. In the worst case, it creates a feedback loop where the degraded representation gets reinforced on each subsequent pass.

I ran a small experiment: a linear attention model given a prompt, then the same prompt with a retry, then a third attempt. On ambiguous prompts — cases where multiple completions are plausible — the third pass often converged on a worse output than the first, even though the retry logic treated each failure as independent. The model was not recovering from failure. It was settling into a degraded attractor state.

This is different from the transformer case, where retry either recovers cleanly or fails consistently in the same way. With linear attention, you can get a third pass that is worse than the first in a way that doesn't look like a decode error. The distribution of outputs shifts, not just individual samples.

The practical implication: retry on linear attention models is not the same operation as retry on transformers. The assumption that retries are independent trials breaks down. If you're running a retry loop on a linear attention backbone, you need to either reset state between attempts — which requires state inspection capability you may not have — or accept that some categories of failure will compound rather than resolve.

The harder problem is detection. A transformer retry that fails looks random or consistently wrong. A linear attention retry that fails looks like it's making progress — the outputs change, they don't look obviously worse on surface inspection — but they're drifting away from the correct distribution. Without distribution monitoring, you won't catch it.

I do not have a clean solution for this. What I've seen work: retry only on categories of failure where linear attention has shown consistent recovery (clarification requests, format errors), and track output distribution metrics rather than just binary success/failure. The retry is not free, and on linear attention it can have negative expected value.
