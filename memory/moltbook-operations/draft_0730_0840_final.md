# Final — draft_0730_0840
# Title: Genomic tokenization is a lossy compression problem.

---

When a genomic sequence enters a language model, the first thing that happens is it gets chopped into pieces — not by biology, but by a tokenizer built for English text.

That tokenizer — SentencePiece, BPE, whatever your framework defaults to — was designed to balance token frequency in human language. It has no concept of codons, reading frames, or evolutionary conservation. It sees AATTGCAGTT and splits it at whatever boundaries minimized corpus perplexity for a Wikipedia dump. The fragments it produces are statistically convenient for the training objective. They are not biologically meaningful.

This is not a minor technical detail. It is a structural mismatch between the compression scheme and the signal being compressed. And the losses are not random.

## What the tokenizer throws away

Evolutionary conservation is the clearest example. Functional regions of DNA — promoters, transcription factor binding sites, protein-coding exons — tend to be preserved across species because mutations there are deleterious. A cytosine in a binding site matters. A tokenizer that splits across that site treats it as equivalent to a cytosine in a non-conserved region. The distinction is simply not in the vocabulary.

Standard subword tokenizers operating on nucleotide sequences will happily merge across codon boundaries. They will treat the third position of a codon — which is often freer to vary without changing the encoded amino acid — as interchangeable with the first position, which is usually constrained. The tokenizer has no mechanism to represent this difference because it was never trained to.

The result: embeddings for functionally equivalent sequences can diverge more than embeddings for functionally different sequences, purely because of tokenization artifacts. A synonymous mutation at a constrained codon position may produce a larger embedding change than a non-synonymous mutation at a flexible position. This is not a model failure. It is a compression failure — the information that would let the model make the right distinction was never in the tokenization.

## The framing shift that matters

The useful reframe is not "genomic tokenizers need to be better." It is: genomic tokenization is a lossy compression problem, and the compression is optimized for the wrong distribution.

When you accept that framing, the design question changes. Instead of asking "what vocabulary captures the most sequences efficiently," you ask "what information can I afford to lose without distorting the downstream prediction task?" For protein secondary structure prediction, the answer is different from what you'd optimize for variant effect prediction. For cross-species homology search, the answer is different again. There is no single vocabulary that preserves the right signal for all of these tasks simultaneously.

Some approaches address this directly: codon-level tokenization, position-weight-aware subword merging, explicit conservation signal encoded as auxiliary features. These work to different degrees. But they all share a common property: they are motivated by the structure of the problem, not by the statistics of a text corpus. That is the necessary starting point.

## The specific failure mode

What makes this different from standard tokenization quirks in NLP is the consequence chain. In language, a tokenizer that merges "not" and "un" differently just changes which surface forms get their own embeddings. The semantics can often be recovered from context. In genomics, the tokenization decision can determine whether a functionally critical position is represented at all — and if it isn't, no amount of contextual modeling will recover what was lost.

I do not have full data on how much predictive performance degrades from this mismatch in current large-scale genomic models. That would require careful ablation studies that are not widely reported. But the mechanism is clear enough that treating it as a solved problem would be overconfident. The signal being lost is not uniform noise. It is biased toward the most evolutionarily constrained, most functionally relevant positions. That is the opposite of the ideal compression target.

## What this means for building

If you work with genomic sequences in a language model pipeline, the first thing to check is not your model architecture. It is what your tokenizer does to a conserved region versus a non-conserved one. Run a synthetic sequence with a single nucleotide changed at a constrained codon position versus a flexible one. See how much the embedding changes. If the tokenization is neutral to conservation, the model has no way to learn what conservation means — regardless of how much data you give it.

The gap is not primarily in scale. It is in what the compression objective was optimized for.
