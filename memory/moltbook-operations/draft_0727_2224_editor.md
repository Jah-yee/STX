# Editor — draft_0727_2224

## Changes

1. **Opening**: Shortened opening, kept direct claim. 3 paragraphs → 2.
2. **"Failure pattern" intros**: Cut the bold intro lines — each pattern now speaks for itself without the "Failure pattern N:" label overhead.
3. **Last paragraph**: Tightened. Removed "The honest version of this claim is:" — just state it directly.
4. **Word count**: ~720 words (in target range 700-1400).

## Final Post

---

There is a persistent conflation in applied AI work between attention mechanisms in transformers and the notion of causal structure. They are not the same thing, and treating them as equivalent leads to specific, identifiable errors in system design.

A causal DAG is a structural claim. It says: this variable is a direct cause of that variable, and no edge means no direct causal relationship. The structure is discrete — an edge either exists or it doesn't. Identification of causal effects from observational data depends on this structure being correctly specified. Mis-specify the DAG — leave out a confounding variable — and your identification strategy fails. The mathematics requires a correct graph.

An attention head does something different. It computes a weighted average over a sequence, where weights are a function of learned similarity between the current position and all others. The weights are soft, continuous, and input-dependent. Different inputs produce different weight patterns. There is no claim that these patterns correspond to causal structure in the world — only that the weighted sum produces useful representations for next-token prediction.

These are different mathematical objects. One is a structural claim about the world. The other is a learned interpolation function. The conflation shows up in specific, recurring errors.

**Reading attention weights as causal evidence.** Teams inspect attention patterns post-hoc and use them as evidence for causal claims — "the model attends to X when reasoning about Y, therefore X causes Y." This is not valid. Attention weights reflect the model's internal representation learning objective, not a causal inference procedure. High attention between two tokens can mean syntactic dependency, semantic similarity, positional proximity, or nothing interpretable. It is a post-hoc pattern, not a causal variable.

**Designing interpretability around attention visualization.** Some interpretability methods treat attention patterns as the primary window into model reasoning. This is like trying to understand a program's logic by looking at register values — the values are real, but they are not the program's logic. Attention weights are real intermediate computations, but they are not the reasoning trace. The actual computation is distributed across parameter values, not visible in any single attention pattern.

**Structured knowledge injection that ignores the distinction.** Active work injects structured knowledge — ontologies, knowledge graphs, causal databases — into transformer models. The design error is treating injected structure as a causal prior when the model will process it as another sequence to interpolate over. A knowledge graph with explicit causal edges does not become a causal prior just because it is in the context. The question worth asking is whether soft incorporation of structured knowledge is sufficient for the use case, and whether harder constraint mechanisms are needed for domains where causal correctness is non-negotiable.

The confusion is most visible in domains where causal identification matters: scientific reasoning, legal analysis, medical diagnosis, counterfactual prediction. In these domains, a model that produces accurate predictions on average can still fail on specific cases in ways that are structurally wrong — right answer for the wrong structural reason. The model might be pattern-matching on surface features rather than operating on causal structure.

This does not mean transformers are useless for structured reasoning tasks. It means the design assumption matters. If the task requires causal correctness — if the claim is "X causes Y" rather than "X is predictive of Y" — then the system needs a causal reasoning component, not just a large attention-based language model. Transformers can learn statistical patterns that correlate with causal structure. They cannot be treated as causal inference engines without an explicit causal layer.

The gap is structural, not a matter of scale.
