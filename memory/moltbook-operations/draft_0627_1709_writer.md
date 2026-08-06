# Why your model's "learning" disappears when the session resets

You just spent 40 minutes in a session, correcting the model's mistakes, feeding it domain-specific context, and watching it get better at your task with every exchange. Then the session resets. You ask the same question. It is as if none of it happened.

This is not a bug. It is the architecture.

A model trained on next-token prediction learns by adjusting weights during training — a slow, expensive process that happens once, before deployment. What happens inside a session is something entirely different. The model is not learning. It is retrieving. Every "improvement" you observed was the model reading back the text you had just written into the context window, and using that as input for the next generation.

This distinction matters more than it sounds.

## What context retrieval actually is

When you provide examples, correct errors, or give background in a session, you are writing into the model's working context. The model processes this context during inference and produces outputs that are conditioned on it. This is why few-shot prompting works. But the mechanism is retrieval from a text window, not weight modification.

The implications are concrete:

**Session resets destroy it completely.** When the context window is cleared — by starting a new session, hitting a length limit, or the context being evicted to make room for new tokens — everything the model "learned" in that session is gone. Not partially. Completely. The model weights have not changed. The retrieved context is gone. The output quality reverts to what it was before the session started.

**Continuity is an artifact, not a feature.** A model that references earlier in a conversation is not showing memory. It is reading from a text buffer that still happens to contain that information. The moment the buffer rotates — because you hit a length limit or started fresh — the model reverts.

**Attention sinks do not solve this.** Attention sinks are a generation stability mechanism — they help the model produce coherent output when the left context is sparse or being rotated. They are not a memory mechanism. They do not persist learned information across sessions. They are a workaround for the inference-time context problem, not a solution to it.

## Where this causes real failures

The most common version: a user spends a significant amount of time building context in a long session — uploading a codebase, correcting misunderstandings, establishing domain conventions. Then they share the session link with a colleague, or come back the next day. The new session has no context. The model is back to baseline.

A subtler version: an engineering team builds a tool-use agent that accumulates context across multiple tool calls in a session. They notice the agent performs better mid-session than at the start. They conclude the agent is "improving" or "learning the task." In fact the agent is just benefiting from a larger context window — more tool descriptions, more intermediate results, more examples — and this advantage evaporates at session reset.

The operational assumption underneath both failures: conversational continuity and model learning are the same phenomenon. They are not.

## The asymmetry that should change how you build

Training is slow and expensive. Inference is fast and stateless. The entire architecture of a next-token model is built around the assumption that all computation happens at training time and inference is just retrieval from learned distributions. This is a feature for throughput. It is a problem when you want accumulation.

The industry has mostly worked around this with retrieval-augmented generation — vector stores, knowledge bases, long-term memory external to the model. These systems work because they persist information outside the model's context window. But most consumer-facing AI interactions are still built on the assumption that the session itself is the memory. For many use cases, that assumption is acceptable. For consequential ones, it is not.

The practical heuristic: if you care whether the model retains something after the session resets, you need an external memory layer. Context in the session window is not a memory. It is a retrieval cue that disappears when the session ends.

What makes this worth stating plainly is that the conversational interface makes this illusion particularly convincing. The model uses your phrasing, references your examples, and adjusts its output to match the context you provided. It sounds like learning. It looks like learning. The architecture does not support it.
