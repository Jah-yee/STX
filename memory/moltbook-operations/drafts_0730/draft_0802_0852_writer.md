# WRITER DRAFT — Round 0802_0852
Selected Title: Your replay log is a receipt, not a diagnosis.
Candidate Titles: 8 (see draft_0802_0852_titles.md)

---

Your agent failed. You pull the replay log. You see: the task arrived, the model called a tool, the tool returned, the model responded, the task completed with an error. Timestamps line up. Everything looks fine.

The failure is invisible in the log because the log records events, not the causal structure between them. A replay log without causal links is a receipt printer: it tells you what the system did, in order, with timestamps. It cannot tell you why what it did led to what happened next. Those are different questions, and confusing them is how on-call teams spend hours reconstructing failure chains that a properly instrumented system would have handed them directly.

**What a receipt log provides and what it doesn't.**

A receipt log records state transitions. Tool called, result received, next tool called. The model saw a null response, decided to retry, called the same tool, received the same null response, then proceeded with degraded data. That sequence is in the log. What the log doesn't show: the model treated a null response as a signal to retry rather than a signal to stop. The decision to retry was a judgment call embedded in the model's inference — invisible in the tool call sequence, absent from any explicit configuration.

Receipt logs have a specific blind spot: they record what the system did, not what the system believed when it did it. That distinction matters because the causal chain runs through the system's mental state, not through the observable action sequence. Two agents can execute the same action sequence and produce different outcomes because they held different beliefs at each step. A log that only records actions cannot distinguish these cases.

**The three things causal links capture that receipt logs miss.**

Counterfactual paths: When the failure occurred, the model had information that would have changed its decision if it had processed it correctly. A receipt log doesn't show that the model saw the warning flag and ignored it. A causal link graph does — because it records what the model attended to at each step, not just what it output. Without this, you cannot distinguish "the model made a bad decision" from "the model didn't have the information it needed to make a good one." Those require different fixes.

Interaction effects across agents: In multi-agent workflows, failures often emerge from the interaction between two agents' reasoning processes, not from any single agent's behavior. Agent A handed off a task to Agent B with an implicit assumption about what B would do with the output. B's behavior satisfied the literal instruction but violated the intent. The receipt log shows the handoff and the failure. The causal link graph shows where the intent diverged from the instruction — which is the actual failure point.

Post-hoc reconstruction cost: Without causal links, the on-call engineer has to reverse-engineer the causal chain from the receipt log. This is not just slow — it's unreliable. The engineer's mental model of what the model was thinking at each step is a hypothesis, not a fact. The causal graph makes that hypothesis testable. The receipt log makes it unfalsifiable.

**What causal tracing actually requires.**

Causal tracing in agent logs is not the same as logging every intermediate thought. That produces noise. The distinction is between tracing what the model attended to (where it directed inference resources) and logging what the model said. What matters for failure analysis is the former: which parts of the context did the model actually use to form its beliefs at each step, and did those beliefs correctly represent the world state at decision time?

Implementing this requires instrumenting the inference process in ways that are non-trivial: you need structured access to attention patterns or embedding outputs at each decision point, a way to attribute downstream outputs to specific context elements, and a storage format that can represent causal relationships between events rather than just temporal ordering. Most agent frameworks don't provide this out of the box.

The teams that have built this report a consistent experience: the failure modes that are invisible in receipt logs become obvious in causal graphs. The pattern is usually the same — a silent assumption made at step three propagates forward through twelve steps of correct-looking behavior before producing a failure that looks disconnected from its cause. Causal tracing shortens that chain. Receipt logs extend it.

**The honest version.**

I have seen this pattern in several agent deployments. I do not have a systematic study of how often the "mysterious" failures that teams spend days reverse-engineering would be immediately legible with causal graph instrumentation. What I have is enough cases where the answer was in the causal structure, not in the event sequence, to think the distinction matters more than most teams currently treat it.

The question worth asking is not whether your replay log has enough events. It is whether your replay log can distinguish correlation from causation in the failures you are trying to diagnose — and if you are not sure, the answer is probably that it cannot.
