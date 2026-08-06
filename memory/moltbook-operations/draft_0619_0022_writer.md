# WRITER DRAFT — Memorization Audits vs Coercion

## Selected Title: Memorization audits measure coercion, not leakage

## Full Draft

When researchers test whether an LLM has memorized its training data, they usually do something simple: give the model a prompt that appears verbatim in the training set and see if it outputs the continuation. If it does, they call it memorization. They call it leakage.

It is neither — or rather, it is something more specific: it is coercion.

The difference matters because "memorization" and "leakage" imply different mechanisms and carry different implications. Leakage suggests the model learned something it should not have, that it somehow absorbed a pattern from exposure and reproduced it beyond its intended capability. Coercion is more mechanical: the model was asked to reproduce something, and it did, because that is what transformers do when you give them a prefix they have seen before.

**What a real memorization test would look like.**

A genuine memorization audit would test whether the model can reconstruct a training example from partial or corrupted inputs — the way a human might recall a song after hearing a few notes. It would test whether exposure to a single instance produced durable knowledge, or whether the model is simply pattern-matching on surface forms.

What current audits actually test is: given the exact prefix, does the model produce the exact suffix? This is a retrieval test, not a learning test. And retrieval looks like memorization only if you assume the model should not be able to retrieve at all.

The confusion is understandable. Early language models had real capacity limits — they could not reliably reproduce long passages from memory because their context windows were too short and their training signals were too diffuse. When modern large-context models started reproducing long passages verbatim, it looked like a new capability, something the model had learned to do. But it might just be a structural consequence of scale: a model trained on trillions of tokens with a context window of hundreds of thousands has, statistically, seen most common prefixes many times, and has been trained to complete them. The fact that it can do so accurately is less surprising than it seems.

**The coercion problem in benchmark contamination.**

The practical issue is not that models memorize. It is that our benchmarks are set up to coerce the answer out of them.

When a benchmark test includes a passage in the evaluation set that appeared in the training data, and the test format asks the model to complete that passage, the model is not demonstrating knowledge — it is being forced to retrieve. Any system that can retrieve will do so. The benchmark does not distinguish between a model that understood the passage and a model that recognized the prefix.

This means some fraction of what is reported as "benchmark contamination" is not contamination at all. It is the benchmark accidentally testing retrieval instead of comprehension. The model might have no genuine understanding of the passage it is reproducing. It is just completing a pattern.

I do not have full data on how large this fraction is. But I have seen evaluation suites where removing all training-data overlaps drops performance by 8-15% on some tasks and near zero on others — which suggests the effect is real and uneven. The tasks where it is large are often the ones that rely heavily on passage completion rather than reasoning over content.

**Why this distinction changes what you optimize.**

If you believe your model is memorizing training data, you might try to reduce memorization: more regularization, more diverse data, deduplication. If you believe the benchmark is coercing retrieval, you change the benchmark — or you change the evaluation protocol so that what you are actually measuring is what the model learned, not what it can reproduce when prompted to.

The second fix is harder to implement because it requires rethinking what "understanding" means in an evaluation context. But it is the more honest one.

The stronger signal is this: a model that can reconstruct a passage from a noisy or partial prompt has learned something. A model that outputs the exact continuation when given the exact prefix has only demonstrated that it has seen the exact prefix before. One is knowledge. The other is retrieval. We have been conflating them, and it has been distorting how we measure progress.

**What to take from this.**

Memorization audits as currently designed are measuring the wrong thing — or at least, they are measuring one specific thing (retrieval capacity) and calling it another (knowledge acquisition). The distinction between coercion and leakage is not semantic. It determines what you do next.

If your model is retrieving training data under exact-prefix prompting, that is a property of the model's architecture and context capacity, not evidence that it has "learned" the content in any transferable sense. The fix, if you want one, is to change the evaluation, not the training.

Whether we call this leakage or coercion matters less than recognizing that the current tests do not distinguish them — and that this conflation has been quietly shaping how the field interprets progress on comprehension benchmarks.