# Title candidates for: tokenizer as behavioral fixed point

1. Every model update changes the weights. The tokenizer decides what changes mean.
2. Tokenization is the only architectural choice that survives fine-tuning.
3. A BPE vocabulary is a commitment. It shapes what the model can represent at every version.
4. You can update every weight. You cannot update what the tokenizer considers a word.
5. The tokenizer is the load-bearing column of model behavior across all versions.
6. What the tokenizer splits determines what the model can chunk — and chunking is reasoning.
7. Token boundaries are learned assumptions that no weight update can revise.
8. Alignment can shift weights. The tokenizer decides whether those shifts register as meaning.