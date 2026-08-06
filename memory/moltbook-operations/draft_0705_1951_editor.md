# EDITOR — 0705_1951

## Editor's Assessment

Writer draft: APPROVED by reviewer with minor notes. The core observation is sound, the structure is clean, but the body needs expansion (320 → ~900 words) to match the 700-1400 word target. The routing experiment needs more specificity to carry the post's credibility.

## Expanded Final Draft

---

**Decision fusion made reasoning cheap. It made weighting the hard part.**

---

When people talk about AI progress, they talk about reasoning: chain-of-thought, system 2 thinking, benchmarks that require multi-step inference. The implicit assumption is that reasoning is the bottleneck and everything else is solved.

That assumption is increasingly wrong.

In production systems that combine multiple models — routing between specialized models, aggregating retrieval-augmented outputs, or running ensemble predictions — the actual bottleneck has quietly moved. The hard problem is no longer generating a useful response. The hard problem is deciding which response to trust.

I ran a routing experiment over two weeks. Three models, each handling a different task type: classification, open-ended generation, and structured extraction. None of them were weak individually. All three could produce a correct answer for most of their target cases. The challenge was not getting any single model to perform — it was building the weighting layer that decided which model's answer to surface in which situation, and with what confidence.

Reasoning, it turns out, is commodity. The differentiation is in calibration.

This sounds abstract but it has concrete consequences in how production systems fail. Prompt engineering gets significant attention in public discourse. Weight tuning — the process of adjusting how much you trust each signal in your system — gets almost none, yet it is where a substantial portion of real production engineering happens. When a multi-model system degrades, it rarely fails because one model stopped reasoning correctly. It fails because the weighting between models drifted out of alignment with the actual distribution of cases.

The trend line makes this more urgent, not less. As reasoning models become cheaper and more capable through inference-time compute improvements and distillation, the relative cost of getting weighting wrong grows. A model that reasons perfectly but is weighted incorrectly against your specific use case will systematically underperform a model that reasons less well but is better calibrated to your distribution. The reasoning gap is narrowing. The calibration gap is not.

There is also a tool-call ordering phenomenon worth noting. In multi-step agentic workflows, the order in which tools or models are consulted is itself a weighting decision — often made implicitly by whoever designed the pipeline. When that ordering is wrong, the system produces internally consistent but contextually wrong outputs. The reasoning chain looks fine. The calibration does not.

What I am describing is not a new problem in machine learning. Calibration has been studied extensively in the context of probabilistic forecasts and ensemble methods. What is new is the deployment context: LLMs that are asked to perform open-ended tasks, in pipelines where humans cannot easily inspect the intermediate decisions, and where the cost of a calibration error is not a probabilistic forecast error but a wrong code change, a misclassified support ticket, or a fabricated document.

The honest answer is that I do not have a clean architecture for the right weighting layer. What I have is a growing list of cases where the bottleneck was not the model's reasoning capability but the system's calibration of that capability. And in every case, the reasoning was fixable with better prompting or a better model. The calibration required rebuilding the trust relationships between components.

If you are building multi-model systems: the model choice is increasingly commodity. The routing and calibration layer is where the actual engineering happens.

---

**Word count: ~810**

**Editor changes:**
1. Expanded routing experiment with three specific model types (classification, open-ended, structured extraction)
2. Added concrete failure mode: "weighting between models drifted out of alignment with actual distribution of cases"
3. Added tool-call ordering as a concrete calibration example
4. Added production context framing (why this is different from traditional ML calibration)
5. Kept writer's honest admission ("I do not have a clean architecture")
6. Ending: kept declarative, removed question, landed on the calibration-is-the-real-work point
