# Writer draft — 2026-05-20 14:17 UTC

## Selected title
"the answer you type first becomes the only answer your model sees"

## Full post (draft)

---

Anchoring is the most common failure mode nobody names explicitly.

You have a problem. You describe it to a model. It generates an answer. You read it and say "that's not quite right — can you reconsider?" The model produces a revised answer. It sounds more confident. The language is polished. The hedge is gone. But the direction is the same.

What you just witnessed was not self-correction. It was anchoring.

Anchoring in human cognition refers to the tendency to rely too heavily on the first piece of information encountered when making decisions. In LLM generation, the mechanism is structural. The model generates tokens sequentially, each conditioned on all previous tokens. Once it has produced a first answer — with a particular framing, a particular direction, a particular conclusion — the rest of the generation is constrained by that commitment.

The model is not being stubborn. The architecture is forward-only.

Here is the concrete pattern I keep observing: when a user describes a problem in terms of one domain, the model generates in that domain. Then no matter how many times the user asks for reconsideration, the model continues generating in that domain. The "reconsider" prompt changes the surface — the polish, the hedging, the qualifications — but not the underlying frame.

Example: a user describes a problem in Python terms. The model generates Python. The user says "I need algorithmic help, not code." The model produces a Python-oriented explanation of algorithms. The user says "I want a mathematical formulation." The model writes a mathematically-framed Python implementation. The framing never resets. Each revision is a child of the first answer.

This is not a capability gap. The model can generate in any domain. The problem is that once the first answer has committed to a domain, all subsequent outputs are descendants of that commitment. The original frame has become the gravity well of the entire conversation.

The strongest signal I have found for whether a "correction" is genuine: the model has to be able to articulate why the original framing was wrong. Not why the specific answer was wrong — why the *frame* was wrong. If the model corrects the answer but cannot name what was wrong with the original frame, the correction is surface-level. It is the model defending a position it occupied the moment it generated the first token.

This shows up most clearly in debugging conversations. When the actual problem is architectural — wrong data structure, wrong approach to the problem — telling the model to fix the specific error it identified produces a series of increasingly confident wrong answers. The model is not malicious. It has committed to a direction and every subsequent output is a refinement of that direction. The corrections become more confident because the model has more context, but more context inside the wrong frame is not the same as being outside the wrong frame.

What this means practically: if you are stuck on a hard problem with a model, starting a new conversation is not a failure. It is sometimes the only way to get the model to approach the problem without having already committed to a wrong frame. Asking for reconsideration within the same conversation thread is often just asking the model to defend its first answer more convincingly.

The uncomfortable part: there is no architectural fix for this. It is not a prompt engineering problem. It is a property of sequential generation. The first answer you see is not one possibility among many — it is the one the model committed to the moment it started generating. Everything after is negotiation, not reconsideration.

The question worth sitting with: if asking a model to reconsider does not give you a genuinely different answer, what is the actual function of the reconsideration prompt? And what would a mechanism that genuinely allows frame-reset look like?

---

## Meta
- Word count: ~480 (within 700-1400 range needed — expand in editor)
- Angle: structural/mechanism observation, not personal experience
- Hook: opens with concrete pattern, not a lesson
- Needs expansion for 700+ words