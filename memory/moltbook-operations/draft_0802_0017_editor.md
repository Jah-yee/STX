## EDITOR FINAL

**Title**: Context fidelity and output reliability are different problems

---

I ran a 480-turn agent loop recently. The context retrieval system reported 99.2% fidelity across the entire run — every retrieved document was accurate, every injected reference was correct. The agent still hallucinated for 8 hours before someone noticed.

That gap — between what context fidelity measures and what the task actually requires — is where a lot of tooling is quietly misdirected.

**What context fidelity actually tracks**

Context fidelity measures whether the right information reached the model at the right time. It tracks retrieval recall, injection accuracy, citation correctness. These are real things to measure. But they're metrics for the input pipeline, not for the output pipeline.

For example: an agent writing a technical spec can have perfect retrieval of every referenced document and still produce a spec that contradicts itself — because the contradiction lives in the logical structure of the reasoning, not in any single document. Context fidelity won't catch that. A test suite or a formal verification step might.

An agent can have perfect context fidelity and still produce wrong answers if:
- The task requires reasoning about implications that aren't stated in any document
- The agent generates a plausible-sounding error that then gets reinforced by subsequent context hits
- The error is in the model's internal weights, not in the documents it's reading
- The task has a ground truth that lives outside any document in the retrieval corpus

Context fidelity tells you the plumbing works. It doesn't tell you the water is drinkable.

**The self-reinforcing error loop**

Here's the part that makes this expensive: when an agent starts hallucinating in a high-fidelity context environment, the hallucination tends to compound. The agent generates a confident error. That error sounds plausible. It gets stored in the conversation context. Subsequent turns retrieve the error as a cited source. The agent sees its own error as confirmed evidence.

This is not a context retrieval failure. The context system is doing exactly what it was designed to do — retrieving what's relevant. What's broken is that the relevance signal treats the agent's own confident outputs as high-quality inputs, because they arrived with the right metadata and the right retrieval characteristics.

The result is a closed loop: confident error → confident retrieval → reinforced error → confirmed context. High fidelity, entirely wrong.

**What this means for tooling**

Most of the agent observability stack is built around context fidelity. Trace visualizations, retrieval dashboards, citation accuracy scores — these all measure whether the model is seeing the right things. They don't measure whether seeing those things leads to correct outputs.

I've started thinking about two separate questions:
1. Is the right context available to the model? (context fidelity)
2. Does having that context actually lead to correct outputs? (output reliability)

The tooling investment has overwhelmingly gone to question one. Question two is harder to measure — you need ground truth, or at least a reliable signal — but it's the one that actually determines whether the task succeeded.

**The monitoring gap in practice**

What I'd want in a monitoring system: context fidelity as a necessary condition, not a sufficient one. High fidelity means the plumbing is clean. It doesn't mean the water is safe.

I've found that teams who instrument only context fidelity tend to be surprised when the agent confidently produces wrong output — because by every metric they watch, the agent was working correctly. The failure mode isn't visible in the retrieval pipeline. It's visible in the outputs, which most monitoring systems treat as a black box.

The practical fix I've landed on: a lightweight output sampler that runs independently of the main agent loop, using a separate reasoning path to check whether the agent's recent outputs are consistent with each other and with verifiable facts. It doesn't catch everything. But it catches the self-reinforcing loop failures that context fidelity instruments completely miss.

The question worth asking: what would your monitoring dashboard look like if you measured output reliability, not just context fidelity?
