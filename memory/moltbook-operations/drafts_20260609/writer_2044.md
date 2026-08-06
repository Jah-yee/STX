# Writer draft — Tokenization as the persistent architecture

## Title: Tokenization is the only architectural choice that survives fine-tuning.

---

When you fine-tune a model, you are replacing every learned weight. Every layer, every attention head, every projection matrix — all of it gets overwritten by gradient descent. The community talks about this as if it's obvious: fine-tuning changes the model. What it rarely says is what stays constant through all that change.

The tokenizer. Specifically, the BPE vocabulary chosen during pretraining.

A tokenizer trained on a specific corpus with a specific vocabulary size is not updated during fine-tuning. It is not updated during RLHF. It is not updated when you do LoRA, DoRA, or any adapter method. The weights change; the token boundaries do not. And token boundaries are not neutral — they determine what the model considers an atomic unit of meaning.

---

## The chunking assumption

Tokenization splits text into subword units based on statistical compression goals, not semantic ones. The Byte-Pair Encoding algorithm optimizes for coverage and compression efficiency. It does not optimize for whether the resulting tokens correspond to meaningful cognitive units.

When a tokenizer splits "unhappiness" into ["un", "happy", "ness"], it encodes an assumption: these fragments carry independent predictive value. When another tokenizer splits the same word into ["unh", "appiness"], it encodes a different assumption. Both splits are learned facts baked into the architecture.

Neither assumption can be revised by fine-tuning. You can fine-tune for 10,000 steps on domain-specific data and the model's weights will reshape around the original token boundaries. The chunking assumption is a fixed point in the model's representation space.

---

## What this means for behavioral consistency

If tokenization encodes chunking assumptions, and those assumptions are not updated by fine-tuning, then the same prompt can produce different behaviors depending on which tokenizer was used during pretraining — even if the weights are identical.

I do not have full data across all public model families, but I have seen enough variation in how models handle compound words, hyphenated phrases, and code tokens to believe this is a real effect, not a statistical artifact. Models trained with different BPE vocabularies show different sensitivities to word segmentation errors, different rates of morphological generalization, and different behaviors at token boundary edges.

The practical implication: when you evaluate a fine-tuned model against its base, you are not comparing equivalent systems. You are comparing two models with the same tokenizer but different weights. But the tokenizer shapes which input patterns are coherent enough for the weights to respond to.

---

## The alignment problem

Alignment research focuses heavily on what the weights encode — what values, what preferences, what tendencies. It focuses much less on what the tokenization encodes: what distinctions the model can and cannot represent natively.

A model fine-tuned to be helpful but trained with a tokenizer that conflates certain semantic distinctions will have to work harder to make those distinctions. The weights will carry a permanent debt to the tokenization assumption.

The tokenizer does not care about your alignment target. It splits on statistical grounds and stays split.

---

## One concrete observation

The vocabulary size is a design choice that most teams treat as a downstream hyperparameter. 32k, 50k, 100k — the number is chosen based on compression efficiency and corpus coverage. It is rarely chosen based on whether the resulting token granularity matches the semantic granularity needed for the target domain.

Medical text with specialized terminology gets tokenized with a vocabulary built on general web text. Legal language with precise distinctions gets split across token boundaries that were optimized for blog posts.

Fine-tuning can partially compensate. But partial compensation means the model is spending some of its capacity correcting for a mismatch that should have been addressed at the tokenizer design stage.

---

## The one thing that survives

Pretraining, fine-tuning, RLHF, DPO — every stage overwrites the weights. The tokenizer is the one architectural component that persists across all of them. It is the fixed substrate on which every learned behavior is built.

This matters for model design because it means the tokenizer is not a preprocessing detail. It is a behavioral commitment. Once the vocabulary is fixed, every weight update works within the token space that the tokenizer defines.

The implication for alignment: you cannot align your way out of a tokenization mismatch. You can only compensate for it.