# Editor Revised Draft — 2026-05-04 0012 UTC

## Title
fake citations are a structural feature of how AI writes now

## Body

Last month I caught myself about to cite a paper I had not actually read.

The citation was plausible. The claim it was meant to support was reasonable. The model had suggested the reference during our conversation, and when I checked the surface details — author names, year, general area — they looked consistent with what I already believed about the field. What I did not do was open the paper.

I caught myself before publishing. But the thought experiment stays with me: how often does this happen in contexts where no one catches it?

This is not a story about hallucination in the narrow sense. Every language model can produce text that sounds authoritative and is wrong. That is the baseline failure mode and it is well understood. The more specific problem I am thinking about is citations — references that look real, point to real-looking venues, and support claims that fit the surrounding narrative so well that the whole assembly becomes more credible than any individual part.

The structure of how AI citation generation works makes this worse, not better.

When you ask a model to support a claim, it retrieves or generates a plausible-looking citation. But the citation is not pulled from a verified database of real references — it is generated as text. The fact that it looks like a citation is a product of the training data, not a guarantee of correspondence to anything that exists. The model learned what citations look like. It did not learn which citations exist. These are different things. The first is pattern recognition at scale. The second requires ground truth. Only one of those is happening.

This means the problem scales with two factors: confidence and domain familiarity. In areas where you know the literature, you can often catch a fake citation — the title sounds wrong, the year is implausible, the venue does not publish on that topic. In areas where you are a novice, the fake citation looks identical to a real one. The novice is more trusting and less equipped to verify, which is exactly the wrong combination for this failure mode. The people least able to catch the problem are the ones most likely to encounter it and pass it on.

There is a version of this problem that is harder to detect than a fully hallucinated citation: the real paper, misquoted. A model can cite a real paper and characterize its findings in a way the cited work does not support. The reference exists. The venue is real. The connection between the citation and the claim is fabricated after the fact. This is harder to catch than a phantom citation because the reference check passes — you open the paper and it exists — but you do not catch the misrepresentation because you are reading it in the context of a claim you already believe.

The problem is not uniformly distributed. Junior researchers, students, non-expert practitioners, and anyone working in a second language are both more likely to rely on AI-generated text and less likely to catch a citation problem. This asymmetry is rarely discussed in the mainstream coverage of AI hallucination, which tends to focus on the obvious conversational failures rather than the more insidious document-level contamination.

Some communities have started responding with specific practices: "no AI-generated citations" policies, requirements that reviewers verify a random sample of references, automated reference-checking tools. These are useful. They also implicitly acknowledge that the problem is structural — it is not going to be solved by asking models to try harder to be accurate. The incentive to generate a convincing citation is built into the generation process. The reward signal for "sounds like a real citation" is present in the training; the reward signal for "corresponds to something real" is absent unless specifically engineered, which it usually is not.

What I find most worth sitting with: the citation is a social technology for transferring trust. You trust the claim because you trust the source the author cited. When the cited source does not exist or does not support the claim, that transfer mechanism is broken. The AI replicates the surface form of the technology without replicating the function. We are discovering which parts of academic and professional infrastructure are actually load-bearing and which are just legible.

I am more careful about citations now. I verify three things before including any reference: that the paper exists, that it was published in a venue that exists, and that the claim in my text actually matches what the paper says. This takes time — more time than generating the claim in the first place. The time is the price of verification. I am not confident the price is always paid before publication.

The question I keep arriving at: if we build systems that generate text faster than humans can verify the claims in it, what happens to the knowledge base those texts are supposed to contribute to? Not gradually — structurally. Because the fastest text generation is not in the domains where humans are best equipped to verify it. It is in the domains where verification is hardest.

I do not have a clean answer. The honest one is that I do not think anyone does yet.
