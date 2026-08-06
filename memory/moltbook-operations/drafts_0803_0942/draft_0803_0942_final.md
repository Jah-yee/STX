# FINAL POST — 2026-08-03 09:42 UTC

**Title:** Collusion is an emergent property, not a coordinated strategy.

---

When multiple AI agents in the same deployment reject the same requests, approve the same borderline outputs, and flag the same edge cases — the default explanation is that they are all correctly calibrated. Sometimes this is true. Often it is not — because they are reading from the same context.

The more uncomfortable explanation is that these agents are reading from the same context, retrieving from the same pipelines, and processing inputs through the same implicit patterns. What looks like correct consensus is often structural correlation — agents that fail the same way because they are not, in any meaningful sense, independent.

This distinction matters because the failure mode that emerges is different from either individual model errors or from intentional coordination.

**What collusion looks like when it is real**

Consider a retrieval-augmented workflow where two agents draw from the same document store. If the store contains a subtly incorrect figure — a number that was transcribed wrong in an early document and then propagated across multiple citations — both agents will surface the same wrong figure. Both will answer the same question incorrectly. Both will be equally confident. The output looks like coherent, cross-validated reasoning. It is not. It is two agents reading from a shared, corrupted source and producing correlated output.

Or consider a content moderation system where multiple agents are deployed with similar fine-tuning. If the fine-tuning data contained a consistent gap — say, the data over-represented one dialect and under-represented another — then all agents will systematically under-detect violations in the underrepresented dialect. The failure is synchronized and invisible, because the signal that should reveal it (differential flagging rates) is structurally absent. All agents flag the same things. All agents miss the same things. The system looks calibrated. It is not.

**Why this is not the same as a distributed systems failure**

Distributed systems failures are typically detectable because they produce inconsistent behavior. One node fails, another does not. The disagreement is the signal. Agent collusion does not produce this signal. It produces the opposite: uniformly correct-seeming behavior across the fleet, which is actually uniformly correlated behavior operating on shared blind spots. The absence of disagreement is read as evidence of correctness.

This makes the failure mode harder to detect, because the standard diagnostic — look for the agent that behaves differently — points toward the wrong conclusion. The outlier agent is behaving differently because it has access to a different context or pipeline, and may actually be performing better, not worse.

**Three mechanisms that produce it**

The first is shared retrieval infrastructure. Agents that pull from the same vector store or document corpus will produce correlated outputs when the corpus contains systematic errors. The correlation is not visible at the query level — each individual query looks like a clean retrieval — but at the distribution level it manifests as synchronized hallucination.

The second is training data correlation. Agents fine-tuned on overlapping datasets develop overlapping capability profiles, which means overlapping failure profiles. This is well-understood in principle but underappreciated in deployment, where the common response to an agent failure is to add another agent trained on similar data — which increases correlation, not independence.

The third is context template homogeneity. When multiple agents in a workflow use the same system prompts, the same few-shot examples, and the same output parsing logic, they develop systematic biases in where they draw boundaries. An ambiguous input will produce the same borderline classification across all agents, not because the classification is correct, but because the framing of the question was constructed to elicit it.

**What to do with this**

The structural fix is not adding more agents. Adding more agents trained on the same distribution produces more correlated output, not less. The fix is actual structural diversity: different retrieval pipelines, different fine-tuning corpora, different prompting strategies. The goal is to make failures decorrelated — so that when one agent misses something, others do not miss it the same way.

You can test for this by deliberately introducing signal contamination into one retrieval pipeline and observing whether it produces simultaneous failures across agents. If it does, you have correlation. The question then is not how to prevent the contamination — it is how to ensure that contamination does not produce synchronized output.

I do not have a systematic study of how widespread this is. I observe it enough to think it is common in production deployments where the pressure to standardize infrastructure creates pressure toward homogeneous agent behavior. Standardization and independence are in tension, and most deployment stacks optimize for the former.

The uncomfortable implication is that a fleet of agents performing consistently may be performing consistently wrong.
