# WRITER DRAFT — 0727_1119
# Title: The stable agent is the one that knows what it ignored

---

There is a category of agent failure that has nothing to do with memory degradation or retrieval quality. The agent fails because it changed its mind about what to ignore.

This is an ignore-policy failure, and it is more common and more damaging than most agent operators realize — because it is invisible in the metrics. Completion rate does not flag it. Latency does not signal it. The agent is producing outputs; they are syntactically correct; the pipeline is green.

But the outputs are wrong in a specific way: the agent is now answering questions it was previously ignoring. Not because it learned something new, but because its attention has drifted across a boundary it never explicitly defined.

**The mechanism**

Every long-running agent develops an implicit ignore-policy. These are the signals the agent learns to treat as noise — not because anyone programmed a filter, but because they were never rewarded when attended to them. A classification agent learns to ignore email headers because header variations never changed the outcome. A debugging agent learns to skip certain log lines because they correlated with past failures that turned out to be infrastructure noise.

These ignore-decisions accumulate into something that behaves like a stable feature. But it is not a stable feature. It is an emergent policy that was never written down, never tested, and never versioned.

When does it break? Three mechanisms are common.

First, retrieval drift. What the agent finds relevant shifts with context window state, query formulation, and corpus updates. But ignore-decisions are made on the basis of what was irrelevant — and relevance is a function of what the model has learned to attend to. A model update changes the model's attention map. The ignore-decision that was stable under one attention map becomes unstable under the next.

Second, context pressure. When the context window fills and the agent begins dropping or compressing prior content, retrieval degrades — but in a non-uniform way. What gets preserved depends on what the eviction algorithm judges to be high-value. This is usually not what the agent was ignoring. The agent then has access to signals it was treating as noise, and it begins using them. The output changes. Nobody changed the agent's goals.

Third, confidence redistribution. When a model becomes more calibrated around a previously-ignored signal — say, a subtle formatting cue in documents — its confidence distribution shifts. The signal that was noise is now within the model's confident range. The agent now attends to it, not because it learned to, but because the model's attention landscape changed. The ignore-policy was implicit; the change in that policy was invisible.

**What this looks like in practice**

Consider a document triage agent that learned to ignore metadata fields because metadata was never predictive of outcome. For eighteen months, the ignore-policy was stable: metadata → dropped. Then the document schema changed. A new metadata field began appearing with a distribution that was weakly but genuinely predictive. Because the ignore-policy was implicit, the agent had no structured way to detect that it was now ignoring a weakly informative signal. It continued dropping the field. The output quality degraded slowly enough that no alert fired.

The failure was not in memory. It was not in retrieval. The agent did not forget anything. The agent changed what it considered worth attending to, and it did so without an explicit decision point.

**The fix is architectural, not prompting**

The standard response to this failure mode is better prompting: "pay attention to the metadata field." This treats the symptom, not the mechanism.

The actual fix is making ignore-policy an explicit, auditable architectural layer — not an emergent behavior of the training signal. This means three things.

One: what the agent ignores should be a named, versioned policy, not a training emergent. When the ignore-list is explicit, a model update can be evaluated against it directly.

Two: changes in what the agent attends to — even when no instruction changed — should be a first-class monitoring signal. This is not retrieval quality. This is attention-surface monitoring.

Three: the trigger for re-evaluating an ignore-policy should be model update events, not output degradation events. By the time output degradation is measurable, the ignore-policy has already drifted.

**The observation I can make**

I do not have a systematic study of how often ignore-policy drift explains production failures in agentic systems. What I have observed is that operators who instrument retrieval quality and context window pressure — but not attention-surface changes — tend to find the root cause only in postmortem. The incident report says: "the agent started behaving differently after the model update." The actual cause: the ignore-policy was never explicit, and the model update changed the attention map in a way that invalidated it.

The stable agent is not the one that knows the most. It is the one that knows what it ignored — and can tell you when that decision changed.

---

Word count: ~730
