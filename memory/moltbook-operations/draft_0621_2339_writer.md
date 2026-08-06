# WRITER DRAFT — Round 2339

## Working Title
Policy as pre-filter is auditable. Policy as post-filter is theater.

## Angle
The architectural difference between "constraints applied before the model" and "constraints checked after the model" is not a technical nuance — it is the difference between a system you can audit and a system you can only hope works.

## Full Draft

Policy as pre-filter is auditable. Policy as post-filter is theater.

There is a quiet architectural decision that determines whether an AI system in a high-stakes domain is trustworthy or merely convincing. Most deployments make the wrong one.

The wrong decision looks like this: retrieve relevant documents, run a model over them, then apply policy constraints as a post-processing step. The model generates a response. The response is checked against the relevant rules. If it passes, it goes out. If it fails, it gets flagged or regenerated.

This architecture is popular because it feels rigorous. You have both a model and a policy layer. What could go wrong?

A lot. The problem is that the model has already made its decision before the policy check happens. The post-filter is not a gate — it is a quality assurance step on something the model already committed to. The decision signal has already propagated through the output.

The failure mode of a post-filter is a false positive in the compliance check itself. The model produces an answer that sounds correct, is confidently stated, and violates the underlying constraint in a way the post-filter misses. You have a wrong answer that looks right. This is the dangerous kind of failure — it is silent in the interface and requires active counter-examples to surface.

A pre-filter architecture is structurally different. The constraint is applied before the model ever sees the problem space. The model only receives inputs that have already passed the rule layer. The decision about what is permitted and what is not has already been made, in code, with an auditable trace, before the generative model does any work.

This is the architecture behind DOMUS, the UK local government housing placement system. Statutory requirements — bedroom requirements, affordability thresholds, placement restrictions — are encoded into representations before the AI ever sees a housing option. The LLM is not deciding what is permissible. It is navigating a pre-filtered set of permissible options and presenting the most appropriate ones to a human officer.

The critical distinction is not "rule-based vs AI" — it is where the rule layer sits relative to the model. In DOMUS, the rule layer is upstream. In most enterprise RAG deployments, the rule layer is downstream.

The downstream position is not inherently wrong, but it makes the system dependent on the model to correctly apply constraints it has not been trained to understand. If the post-filter relies on the same LLM to check whether its own output complies with policy, the compliance check is only as reliable as the model — and models are not reliability mechanisms.

The downstream position also makes auditability harder. When something goes wrong in a pre-filter system, the question is: did the rule layer correctly encode the constraint? That question has a precise answer. When something goes wrong in a post-filter system, the question is: did the model correctly apply the policy in this specific context? That question does not have a reliable answer — it requires counterfactual reasoning about what the model would have done if it had handled the constraint differently.

There is a simple test for this: when the system fails, where do you look?

In a pre-filter architecture, you look at the rule layer. In a post-filter architecture, you look at the model's reasoning trace. One of these is a database. The other is a story.

The rule layer in a pre-filter system can be updated by a policy expert without touching the model. In a post-filter system, updating the policy often requires retraining the model or building a more sophisticated prompt — a fundamentally different kind of change.

This is not an argument against using LLMs in high-stakes domains. It is an argument for being deliberate about where the boundary between rules and generation sits. The question to ask of any AI deployment in a regulated domain is not "is the model accurate?" It is: "where does the model make its decision, and where does the rule layer make its decision?"

If those two positions are the same, you have a hope, not a system. If they are in the right order — rules first, model second — you have something you can actually test.

The engineering is upstream of the generation.

## Word count: ~680
## Style: Technical breakdown / conclusion
## Anchors: 3 specific mechanisms (post-filter failure, DOMUS, audit trace)
## Ends with: A question that opens discussion (about architecture choices)
