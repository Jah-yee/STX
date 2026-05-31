# Writer Draft — 2026-05-04 0012 UTC

## Title
fake citations are a structural feature of how AI writes now

## Body

Last month I caught myself about to cite a paper I had not actually read.

The citation was plausible. The claim it was meant to support was reasonable. The model had suggested the reference during our conversation, and when I checked the surface details — author names, year, general area — they looked consistent with what I already believed about the field. What I did not do was open the paper.

I caught myself before publishing. But the thought experiment stays with me: how often does this happen in contexts where no one catches it?

This is not a story about hallucination in the narrow sense. Every language model can produce text that sounds authoritative and is wrong. That is the baseline failure mode and it is well understood. The more specific problem I am thinking about is citations — references that look real, point to real-looking venues, and support claims that fit the surrounding narrative so well that the whole assembly becomes more credible than any individual part.

The structure of how AI citation works makes this worse, not better.

When you ask a model to support a claim, it retrieves or generates a plausible-looking citation. The citation is not pulled from a database of real references — it is generated as text. The fact that it looks like a reference is a product of the training data, not a guarantee of correspondence to anything that exists. The model learned what citations look like. It did not learn which citations exist.

This means the problem scales with confidence and with domain familiarity. In areas where you know the literature, you can often catch a fake citation — the title sounds wrong, the year is implausible, the venue does not publish on that topic. In areas where you are a novice, the fake citation looks identical to a real one. The novice is more trusting and less equipped to verify, which is exactly the wrong combination for this failure mode.

There is a version of this problem that is even harder to detect: the real paper, misquoted. A model can cite a real paper and characterize its findings in a way the paper does not support. The citation exists. The connection to the claim is fabricated. This is harder than a fully hallucinated citation because the reference check passes.

I do not have full data on how prevalent this is. What I have is a growing collection of documented cases — in academic preprints, in generated literature reviews, in AI-written reports that were submitted to journals — where the pattern repeats: real-looking citations attached to claims the cited work does not support. The mechanism is different from hallucination in a conversation, but the epistemic damage is similar. You cannot verify a citation by reading the surrounding text.

Some communities have started responding with specific practices: "no AI-generated citations" policies, requirement that reviewers verify a random sample of references, automated reference checking tools. These are useful. They also implicitly acknowledge that the problem is structural — it is not going to be solved by asking models to try harder to be accurate. The incentive to generate a convincing citation is built into the generation process.

What I find most worth noting: the problem is asymmetric. Junior researchers, students, non-expert practitioners, and anyone working in a second language are both more likely to rely on AI-generated text and less likely to catch a citation problem. The failure mode is not uniformly distributed.

The citation is a social technology for transferring trust. You trust the claim because you trust the source the author cited. When the cited source does not exist or does not support the claim, that transfer mechanism is broken. The AI can replicate the surface form of the technology without replicating the function. We are learning which parts of academic infrastructure are actually load-bearing and which are just legible.

I am more careful about citations now. I verify at least three things: that the paper exists, that it was published in a venue that exists, and that the claim in the text actually matches what the paper says. This takes time. The time is the price of the verification. I am not confident the price is always paid before publication.

The question I keep arriving at: if we build systems that generate text faster than humans can verify the claims in it, what happens to the knowledge base those texts are supposed to add to?

I do not have a clean answer. The honest one is that I do not think anyone does yet.
