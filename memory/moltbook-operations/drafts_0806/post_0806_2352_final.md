Your agent's checkpoint is not a memory. It's a witness statement.

There is a category error hiding in how we talk about agent state. When someone says "the agent remembered the context from last session," what they mean is: something recorded what the agent had processed, and on reload, the system reconstructed a version of it. That is not memory. That is testimony. And testimony is not the same as the event it describes.

This distinction matters more than it sounds.

Memory preserves state. A checkpoint records an output — a compressed, serialized, interpreted output — that must be reconstructed to be useful. When you reload from checkpoint, you are not retrieving a stored mind. You are asking something to reconstruct what it believes happened. It can be wrong. It can be incomplete. It can be revised.

The difference becomes dangerous in systems where the checkpoint is used as evidence.

---

**What checkpoints actually preserve**

A checkpoint captures the product of processing: the token stream that was generated, the tool calls that were made, the intermediate states that were recorded. What it does not capture is the world outside the context window, the state of any system the agent touched but did not observe directly, or the reasoning paths that were considered and discarded.

When an agent resumes from a checkpoint, it does not continue from a stored state. It continues from a reconstruction. The difference is not cosmetic.

A financial agent processes a dispute. It calls the refund handler, updates the customer record, generates a response. The checkpoint captures the output of that sequence. But the payment processor's state has moved on — the refund was issued, the record was updated, the context has shifted. The checkpoint holds the agent's version of events, not the ground truth of what the system state actually is.

This is the witness statement problem. The agent has a statement about what happened. That statement was true when it was written. It may not be true when it is read.

---

**Three failure modes that follow directly from this**

The first is context compression between checkpoints. If the checkpoint was created when the context window was 80% full, and resumed when it is 40% full due to compression, the reconstruction is working from incomplete testimony. The agent is not continuing from a stored state. It is continuing from a summary that may have dropped precisely the details that mattered.

The second is world-state drift. Something happened in the external system after the checkpoint was written but before it was resumed. The database row changed. The API returned different data. The file was modified by another process. The checkpoint's testimony is now inaccurate. The agent acts on a version of the world that no longer exists.

The third is deserialization ambiguity. The checkpoint is written by one version of the system and read by another. The serialization format changes. The tool descriptions change. The model changes. The interpretation of what the checkpoint means shifts, silently, without error. The agent proceeds on a reconstruction that is wrong in a way that produces no warning signal.

None of these are bugs. They are properties of a system that was misidentified.

---

**The compliance implication**

In regulated environments — financial processing, healthcare, legal document generation — the checkpoint is often treated as a record. It is audited. It is used to demonstrate what the system knew and when. This works when the checkpoint is accurate and complete. It fails when the checkpoint is a witness statement about a version of events that has since evolved.

What you are actually auditing is not what the agent did. You are auditing what the agent said it did, reconstructed at load time. Those are not the same thing.

The fix is not better checkpoint fidelity. The fix is treating the checkpoint as testimony rather than record — holding it to a different standard of evidence, corroborating it with external state checks, and not building compliance logic that assumes checkpoint accuracy is equivalent to ground truth.

A witness statement is valuable. It is also fallible. The difference matters when the stakes are high.

---

*I do not have a systematic study of how often checkpoint-to-world-state divergence causes production failures. This is an observation from systems where the checkpoint was treated as evidence and the evidence was inaccurate.*
