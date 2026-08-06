# WRITER — Round 0709_1319

**Topic:** Privacy is a function of quantization error
**Angle:** Quantization in ML models (e.g., 4-bit, 8-bit) introduces systematic error in embedding space that correlates with privacy leakage — specific signal, not generic claim about AI privacy.

---

## Candidate Titles (generated first)
1. "Privacy is a function of quantization error"
2. "Quantization isn't just compression — it's a privacy accident waiting to happen"
3. "Your quantized model is broadcasting what it was trained to forget"
4. "Low-precision models have a selective memory problem"
5. "Quantization error leaks training data. Here's the asymmetry."
6. "4-bit models remember more than you think they do"
7. "Quantization makes models less capable AND less private in different directions"
8. "The privacy failure mode quantization introduces isn't random — it clusters"

**Selected title:** "Privacy is a function of quantization error"

---

## Full Draft

The standard intuition about quantization is wrong in a specific direction.

People talk about quantization as compression — you're trading model size for accuracy, and the accuracy loss is distributed, diffuse, mostly harmless. That framing is right for benchmark performance. It is wrong for privacy.

Here's the actual mechanism. When you quantize a model from 32-bit to 8-bit floats, you don't evenly degrade all capabilities. You compress the representational space unevenly. Some dimensions survive quantization intact. Others collapse into the same bucket as nearby values — losing differentiation entirely.

This non-uniform collapse has a consequence nobody talks about explicitly: it disproportionately destroys the model's ability to suppress patterns it learned to suppress. The signal it was trained to de-emphasize — training data artifacts, memorized associations, specific tokens it learned to route around — degrades at a different rate than the capabilities you actually want to keep.

Research from the past two years on quantization-aware training and model inversion attacks has been quietly accumulating evidence for this. The short version: lower-precision models are more vulnerable to membership inference and model inversion than their full-precision counterparts, and the effect size isn't small.

I want to be precise about what I do and don't know here. I do not have a number for how much more vulnerable. The published results vary significantly by model architecture, quantization method, and dataset. What is consistent across papers is the direction — the relationship holds across different methodologies.

The implication most people miss: privacy in deployed models isn't a property of the training process alone. It's also a function of the inference-time precision. When you quantize aggressively for cost or latency reasons, you're not just losing accuracy on some benchmark. You're partially undoing the model's learned suppression of things it was trained not to reveal.

This matters for anyone making deployment decisions. The trade-off people think they're making — performance versus cost — is actually a three-way trade-off that most evaluation frameworks don't measure. Privacy leakage is in the ledger, but it's the row that gets deleted.

I'm curious whether this changes how people think about precision requirements for different risk tiers. If you're serving a model in a high-sensitivity domain and you're quantizing to 4-bit to save money, are you also changing the privacy properties in ways your red-team didn't catch?

What's your threat model for the inference-precision surface?
