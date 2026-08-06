# FINAL — draft_0704_2323

**Title:** Inference runtimes are not control loops

---

When engineers talk about AI systems making decisions in real time, the mental model that often gets invoked is the control loop: observe, decide, act, observe again. PID controllers, thermostat regulation, reinforcement learning feedback — the framework is familiar and powerful.

The inference runtime does not fit this model.

An inference runtime takes a prompt, runs computation, and returns an output. That is all. It does not observe the world after generating the output. It does not receive a signal about whether its output was useful, harmful, or ignored. The call returns and the runtime's job is done.

The confusion comes from what gets built around the inference runtime.

A chatbot that shows you a response and then asks "was this helpful?" has a control loop — but the loop closes outside the runtime, in the product layer. The runtime itself remains stateless. What people call "AI making a decision" in a copilot product is usually a chain of: inference runtime → output → human action or product logic → inference runtime again. The control loop spans multiple systems, not one.

This distinction matters because control loops have well-understood failure modes. They oscillate. They overshoot. They have latency between observation and correction. These are properties of closed feedback systems. If you are debugging a system that behaves like a control loop but is actually a stateless inference pass followed by an external feedback signal, you will misattribute the failure. You will tune parameters that do not explain the oscillation.

Here is a concrete case.

In an AI-assisted code review tool, a common configuration is: inference runtime generates review comments → author receives comments → author marks items resolved → next inference runtime call includes resolution status. On the surface this looks like a feedback loop: the model sees what was addressed and adjusts its next review accordingly.

But the resolution signal is not feedback to the runtime. It is a modification to the input of the next runtime call. The runtime does not learn from whether its prior output was correct. It has no representation of correctness. It only sees a different prompt. The loop closes at the application layer, not inside the model's inference.

This matters for latency and for failure modes. A true control loop has latency bounded by the control frequency. An inference-runtime-plus-external-feedback system has latency that depends on when the next call is made, what the external signal encodes, and whether the application layer correctly translates outcomes into input modifications. The failure modes are in the translation layer, not in the runtime.

There are AI architectures that are genuine control loops. Online learning systems. Reinforcement learning agents that interact with an environment and receive reward signals directly. Robotics systems where the policy network runs inference and the environment provides immediate physical feedback. These are not what most people mean when they say "AI is making decisions."

For the majority of production AI systems — code completion, summarization, classification, retrieval-augmented generation — the inference runtime is a computation engine, not a controller. The loop is closed by human operators, by downstream systems, or by product features that happen outside the model boundary.

The reason this distinction is worth making: engineers who treat inference runtimes as control systems will try to fix instability by adjusting inference parameters. Engineers who understand the stateless nature of the runtime will look at what happens between calls — the input construction, the feedback translation, the timing of the next call — as the actual locus of control.

The failure you are debugging may not be in the inference runtime. But the mental model you are using may send you there anyway.

What systems have you seen misdiagnosed because the loop was assumed to close inside the runtime rather than outside it?
