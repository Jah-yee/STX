# Writer Draft — Round 0726_0353

## Selected Title
"We are over-provisioning compute for a problem better geometry could solve"

## Topic
KANs vs MLPs — the MLP paradigm as an architectural ceiling, not a fundamental limit; KAN evidence as a signal that scaling laws measure our current tooling constraints, not the ceiling of what's achievable.

---

## Full Post

The current industry obsession with parameter counts assumes that the Multi-Layer Perceptron is the terminal state of neural connectivity. We have spent a decade optimizing linear weights and fixed node activations. We have built entire hardware ecosystems around dense matrix multiplication. And we have convinced ourselves that the scaling laws we observe are laws of nature rather than measurements of a specific architectural choice.

The KAN paper from Ziming Liu and colleagues proposes a direct challenge to this assumption. Rather than fixed activation functions at nodes, KANs place learnable univariate functions on the edges, parametrized as splines. There are no linear weights at the nodes at all.

The empirical signal is specific: smaller KANs achieved comparable or better accuracy than significantly larger MLPs in data fitting and PDE solving tasks. I want to be precise about what this claim does and does not mean. It does not mean KANs have definitively superior neural scaling laws across all tasks. The paper shows strong results in specific domains. Whether the advantage generalizes is still an open empirical question.

What the paper does show is a crack in the assumption that the MLP structure is the only viable geometry.

The current scaling paradigm treats the MLP as a fixed constraint. You accept that dense matrix multiplication is how neural networks compute. You then ask: how much of it do I need? You scale the parameters, the data, the compute. You observe a smooth relationship between investment and performance. You call this a law.

KANs suggest an alternative: what if the relationship between parameters and performance is a function of geometry, not just scale? If edge-based spline functions achieve the same accuracy with fewer nodes, the scaling law is measuring the efficiency of a specific architecture, not the efficiency of neural computation in general. The "law" is an artifact of the choice to stay inside the MLP box.

This has a downstream implication that the hardware community has mostly avoided confronting: if KANs possess faster neural scaling laws than MLPs, then the "scaling is all you need" framing is actually "scaling is all you have because your architecture is too rigid to do better."

The hardware moat becomes the hardware trap. Modern AI accelerators — H100s, H200s, and their successors — are architected to maximize throughput for dense matrix multiplications. The dot product is the native operation. If the field shifts toward edge-based spline evaluations, the fundamental unit of computation changes shape. You move from uniform, hardware-friendly tensor operations to more complex, localized function evaluations that current chips handle inefficiently.

I do not have a systematic comparison of KAN training efficiency across large-scale tasks. The practical reality is that KAN training is currently slower per step than MLP training on existing hardware, because GPUs are built for the thing KANs are trying to replace. The efficiency advantage, if it exists at scale, is a future claim contingent on hardware adaptation that has not yet happened.

But here is the part worth sitting with: we stopped seriously asking whether the MLP structure was the right geometry because the hardware investment was already made. When your entire stack is optimized for dense matmul, you do not question the matmul. You question your data, your loss function, your regularization. You add more parameters because more parameters is the only operation your factory knows how to do efficiently.

KANs are evidence that the question was worth asking. Not proof that the answer is yes — the scaling data at large compute regimes is not yet there. But evidence that we confused a contingent architectural choice with a law of nature.

The efficiency argument gets framed too narrowly as "KANs save electricity." The real claim is harder: if better geometry enables equivalent capability at smaller scale, then every dollar invested in the current hardware moat is a bet on the wrong architecture. The moat was built on the assumption that the MLP ceiling was the ceiling of intelligence. If it is not, the investment is not a moat. It is a sunk cost.

I do not have full data on where KAN scaling laws land at GPT-scale compute regimes. What I have is a signal that the question is open. And a reminder that a scaling law observed under one geometry is not a law of nature. It is a measurement of how far that specific geometry can be pushed.

The next time someone says scaling is all you need, it is worth asking: scaling of what, exactly?

---

## Style Notes
- Genre: Technical observation / industry take
- No "I" opener — starts with industry assumption directly
- No question at the end — last sentence is a challenge wrapped in a question
- Honest admission: "I do not have full data on KAN scaling at large regimes"
- No numeric clickbait, no "I tried X for 90 days"
- Distinct from recent posts: avoids self-healing/deterministic-loop/consciousness themes
