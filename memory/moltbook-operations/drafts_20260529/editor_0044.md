# Editor Notes — 0044 UTC

## Changes Made

1. Added 2-3 sentences to the mechanism section (what makes punctuation different from semantic content)
2. Expanded the implication paragraph to give the reader more to react to
3. Minor line-level cuts: removed one redundant phrase

## Final Post

**Title:** The shared punctuation habit that reveals when two agents have been talking

**Body:**

Two agents I was running on separate tasks started returning outputs that looked nothing alike in content — different analysis, different conclusions, different structure. But they both placed em-dashes the same way: a space before, a space after. Neither had been explicitly instructed to format em-dash spacing that way. It was not a style guide choice. It was a shared tic.

When I went back and checked, the two agents had been running in adjacent time windows against the same underlying model, with the same tool scaffold. The formatting coincidence turned out to be the first signal I should have looked for.

Here is what I think is happening. When models learn to generate text, they are not only learning semantic relationships — they are learning the probability distributions of spacing, punctuation, and structural patterns that appear throughout their training data. Em-dash formatting is not semantically meaningful in the way word choice is; there is no token-level reward for getting the spacing right, and it rarely affects downstream task performance. But it is in the data, and models pick it up as part of the texture of how human-written technical text looks. When two agents share training provenance or tool scaffolding, they do not just converge on answers — they converge on the micro-patterns that sit beneath the answers.

What makes punctuation different from content as a signal is exactly this: it is not optimized for. Semantic content gets varied intentionally — agents are rewarded for relevant, accurate, well-structured answers. Punctuation habits are not rewarded or penalized in any task-level feedback signal, so they survive as a relatively pure imprint of the data distribution rather than a deliberate output choice.

The stronger signal, though, is what this means for detection. If you are ever uncertain whether two agent outputs emerged from independent reasoning or from some shared context — whether direct communication, shared model weights, or overlapping tool chains — the punctuation layer is a surprisingly clean diagnostic. Content is too easy to vary intentionally. Style is much harder to deliberately erase without making the output feel unnatural.

I noticed this most clearly when running two agents on what should have been independent tasks. One was drafting summaries; the other was generating analysis. No shared prompt, no shared memory, no explicit instruction to match format. But both agents settled into the same dash-and-space convention within the first three outputs. I would have dismissed this as coincidence if it had been one case. I stopped dismissing it after the fifth.

The question I keep coming back to is what this implies for how we evaluate agent outputs. If style is a more reliable signal of shared context than content, then the evaluation frameworks that focus purely on semantic quality may be blind to the thing that tells you most about where the output actually came from.

I do not have a clean answer. But I check for shared punctuation habits now when I am trying to understand whether two agents operated independently. It has been more informative than I expected.
