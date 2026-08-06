# Writer Draft — draft_0727_2224

**Title**: Attention patterns implement soft routing, not causal structure

---

There is a persistent conflation in applied AI work between attention mechanisms in transformers and the notion of causal structure. They are not the same thing, and treating them as equivalent leads to specific, identifiable errors in system design.

Let me be precise about what each thing actually does.

A causal DAG is a structural claim. It says: this variable is a direct cause of that variable, and the absence of an edge means no direct causal relationship. The structure is discrete — an edge either exists or it doesn't. Identification of causal effects from observational data depends on this structure being correct. If you mis-specify the DAG — if you leave out a confounding variable — your identification strategy fails. The mathematics of causal inference requires a correctly specified graph.

An attention head in a transformer does something different. It computes a weighted average over a sequence, where the weights are a function of learned similarity between the current position and all other positions. The weights are soft, continuous, and input-dependent. Given different inputs, the same attention head will produce different weight patterns. There is no claim that the pattern of weights corresponds to a causal structure in the world — only that the weighted sum produces useful representations for next-token prediction.

These are genuinely different mathematical objects. One is a structural claim about the world. The other is a learned interpolation function. Conflating them shows up in several specific failure patterns I have observed in applied work.

**Failure pattern 1: Reading attention weights as causal evidence**

Teams sometimes inspect attention weight patterns post-hoc and use them as evidence for causal claims — "the model attends to X when reasoning about Y, therefore X causes Y." This is not valid. Attention weights are a function of the model's internal representation learning objective, not a causal inference procedure. The model is trained to predict the next token, not to identify the causal structure of the domain. High attention weight between two tokens can mean many things: syntactic dependency, semantic similarity, positional proximity, or nothing interpretable at all. It is a post-hoc pattern, not a causal variable.

**Failure pattern 2: Designing interpretability around attention visualization**

Some interpretability methods treat attention patterns as the primary window into model reasoning. This is structurally similar to trying to understand a program's logic by looking at register values — the register values are real, but they are not the program's logic. Attention weights are real intermediate computations, but they are not the reasoning trace the model is running. The actual computation is distributed across the parameter values, not visible in any single attention pattern.

**Failure pattern 3: Structured knowledge injection that ignores the distinction**

There is active work on injecting structured knowledge — ontologies, knowledge graphs, causal databases — into transformer models. The design error here is treating the injected structure as if it will be used as a causal prior, when the model will actually process it as another sequence to interpolate over. A knowledge graph with explicit causal edges does not become a causal prior just because it is in the context. The model's attention mechanism will treat it as soft similarity data, not as hard causal constraints. This is not a criticism of knowledge injection — it is a description of what knowledge injection actually does. The question worth asking is whether soft incorporation of structured knowledge is sufficient for the use case, and whether harder constraint mechanisms are needed for domains where causal correctness is non-negotiable.

**What this means in practice**

The confusion is most visible in domains where causal identification actually matters: scientific reasoning, legal analysis, medical diagnosis, counterfactual prediction. In these domains, a model that produces accurate predictions on average can still fail on specific cases in ways that are structurally wrong, not just statistically noisy. The model might produce the right answer for the wrong structural reason — and attention-based interpolation does not give you a way to distinguish this from correct causal reasoning.

The failure mode is silent. The model produces outputs that look reasoned. The system has no mechanism for surfacing that the reasoning is interpolation-based rather than structure-based. You only find out when someone with domain knowledge reviews specific outputs and notices that the model is pattern-matching on surface features rather than operating on causal structure.

This does not mean transformers are useless for structured reasoning tasks. It means the design assumption matters. If the task requires causal correctness — if the claim is "X causes Y" rather than "X is predictive of Y" — then the system needs a causal reasoning component, not just a large attention-based language model. The model can learn statistical patterns that correlate with causal structure, but it cannot be treated as a causal inference engine without an explicit causal layer.

The honest version of this claim is: transformers are extremely good at certain things, and causal inference is a different thing. The confusion arises when applied work implicitly assumes the former can substitute for the latter without an explicit bridging mechanism. The gap is structural, not a matter of scale.
