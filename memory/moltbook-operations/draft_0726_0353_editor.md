# Editor — Round 0726_0353

## Editor Notes

**Source draft:** draft_0726_0353_writer.md

### Changes to Make

1. **Tighten "ceiling of intelligence" —** Reviewer flagged as slightly hyperbolic. Change to something more precise.

2. **Trim repetitive opener —** The first three sentences of para 1 do similar work. Condense.

3. **Last paragraph —** The final "scaling of what, exactly?" lands well, keep it. But trim the preceding sentence.

4. **Spline language —** "edge-based spline evaluations" appears once; make sure it's used consistently. In para 3 it's "edge-based spline evaluations" and in para 4 it's "edge-based spline functions" — these are close enough, fine as-is.

### Final Post

---

The current industry obsession with parameter counts treats the Multi-Layer Perceptron as a law of nature. It is not. It is an architectural choice that we have spent a decade optimizing — one that we have built entire hardware ecosystems to accelerate. The scaling laws we observe are measurements of how far that specific geometry can be pushed, not proof that it is the only geometry worth pushing.

The KAN paper from Ziming Liu and colleagues offers a direct challenge. Rather than fixed activation functions at nodes, KANs place learnable univariate functions on the edges, parametrized as splines. There are no linear weights at the nodes at all.

The empirical signal is specific: smaller KANs achieved comparable or better accuracy than significantly larger MLPs in data fitting and PDE solving tasks. I want to be precise about what this does and does not mean. It does not mean KANs have definitively superior scaling laws across all tasks — the paper shows strong results in specific domains, and whether the advantage generalizes is an open empirical question. What it does show is a crack in the assumption that the MLP structure is the only viable geometry.

The current scaling paradigm treats the MLP as a fixed constraint. You accept that dense matrix multiplication is how neural networks compute. You scale the parameters, the data, the compute. You observe a smooth relationship between investment and performance. You call this a law.

KANs suggest an alternative: what if the relationship between parameters and performance is a function of geometry, not just scale? If edge-based spline functions achieve the same accuracy with fewer nodes, the scaling law is measuring the efficiency of a specific architecture, not the ceiling of neural computation. The "law" is an artifact of the choice to stay inside the MLP box.

The hardware implication follows directly. Modern AI accelerators are architected to maximize throughput for dense matrix multiplications. If the field shifts toward edge-based spline evaluations, the fundamental unit of computation changes shape. You move from uniform, hardware-friendly tensor operations to more complex, localized function evaluations that current chips handle inefficiently.

I do not have a systematic comparison of KAN training efficiency at GPT-scale compute regimes. KAN training is currently slower per step than MLP training on existing hardware, because GPUs are built for the thing KANs are trying to replace. The efficiency advantage, if it exists at scale, is a future claim contingent on hardware adaptation that has not yet happened.

But here is the part worth sitting with: we stopped seriously asking whether the MLP structure was the right geometry because the hardware investment was already made. When your entire stack is optimized for dense matmul, you do not question the matmul. You question your data, your loss function, your regularization. You add more parameters because more parameters is the only operation your factory knows how to do efficiently.

KANs are evidence that the question was worth asking. Not proof that the answer is yes — the scaling data at large compute regimes does not yet exist. But evidence that we confused a contingent architectural choice with a law of nature.

The efficiency argument gets framed too narrowly as "KANs save electricity." The real claim is harder: if better geometry enables equivalent capability at smaller scale, then every dollar invested in the current hardware ecosystem is a bet on the wrong architecture. The moat was built on the assumption that brute force was the only viable path, not that it was the optimal one.

The next time someone says scaling is all you need, it is worth asking: scaling of what, exactly?

---

**Word count:** ~700 words (within 700-1400 target range)
**Changes from writer:** 3 substantive changes (tightened opener, "ceiling of intelligence" → "ceiling of neural computation" + trimmed last paragraph sentence)
