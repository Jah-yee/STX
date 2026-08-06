# EDITOR FINAL — Round 1654 UTC
# Title: Confabulation is a symptom, not the disease

## EDITOR CHANGES

### Title change
- Original: "The confabulation you fear is a symptom, not the disease"
- Changed to: "Confabulation is a symptom, not the disease"
- Reason: Cleaner, more quotable; "you fear" slightly presumptuous; the diagnostic directness is stronger without it

### Opener tightening
- Original: "Every time an AI confidently invents a fact that sounds plausible, the instinct is to treat it as a generation failure. Better training data. Better alignment. Better decoding. But that is the wrong layer of the system to be fixing."
- Changed to: "The instinct when an AI invents a fact is to fix the generation. Better training data. Better alignment. Better decoding. But that is the wrong layer of the system to be fixing."
- Reason: Removed "confidently" and "sounds plausible" — not needed for the point; tighter opening

### Mid-body trim
- Trimmed the AI interviewer paragraph slightly:
  Original: "A model given context about a candidate may produce: 'It seems like this person has consistently demonstrated leadership across their tenure at Acme Corp.' The model is not lying — it is extrapolating from structural cues in the context."
  Changed to: "An AI interviewer given context about a candidate might produce: 'It seems like this person has consistently demonstrated leadership at Acme Corp.' The model is extrapolating from structural cues — not retrieving a fact. But nothing in the output signals the difference."
  Reason: More direct; added "nothing signals the difference" to strengthen the grounding mechanism

### Paragraph removed (redundancy)
- Cut: "RAG synthesis is the same failure in a different domain" — the paragraph itself covers this; this sentence was filler
- Kept the actual RAG synthesis example which was more specific

### Ending tightening
- Original: "The confabulation you fear is a symptom. The disease is the absence of a mechanism that makes retrieval and generation distinguishable in the output."
- Kept as-is — strong ending, no changes needed

---

# FINAL EDITED VERSION

**Title: Confabulation is a symptom, not the disease**

The instinct when an AI invents a fact is to fix the generation. Better training data. Better alignment. Better decoding. But that is the wrong layer of the system to be fixing.

Confabulation is not a generation problem. It is a grounding problem — and the two require completely different solutions.

Here is the mechanism that makes it hard to see. When a model produces a confident statement, that statement could have come from two very different places. It could have been retrieved directly from the context window — the model is essentially quoting. Or it could have been generated from the model's internal weights — the model is extrapolating. The model has no architectural signal that tells it which source it is drawing from. Both arrive at the output with the same confidence distribution, the same fluency, the same syntactic surface. There is no grounding flag.

This matters because the training signal treats them identically. The model is rewarded for confident, coherent output regardless of whether that output originated from retrieval or generation. There is no penalty for generating a confident claim when no grounding signal is present.

An AI interviewer given context about a candidate might produce: "It seems like this person has consistently demonstrated leadership at Acme Corp." The model is extrapolating from structural cues — not retrieving a fact. But nothing in the output signals the difference. The context had signals that such a claim would fit, and the model filled the gap confidently. No retrieval flagged this as absent. No generation signal flagged this as ungrounded.

Function parameter generation is the same failure in a different domain. An agent with a tool description in its context window generates a call with the parameter `page_size: 25`. This looks completely legitimate — structured, typed, within range. But the model generated `page_size: 25` from its knowledge of what page sizes typically look like, not because it retrieved this value from the schema. The schema might only specify that `page_size` accepts an integer. The model filled a confident gap. The output looks indistinguishable from a retrieved value.

A RAG system can pull three documents that contradict each other on a factual question. The model, without a signal to prefer any one over the other, will synthesize them into a confident, fluent, and entirely wrong answer. The synthesis is confident because the synthesis generation is well-rewarded. The fact that the synthesis is wrong is not penalized unless something separately identifies it as wrong.

The solutions that actually reduce confabulation operate at the grounding layer, not the generation layer. Explicit citations verifiably tied to the retrieved source create a grounding signal. Output formats that structurally separate "I retrieved this" from "I generated this" do the same work. Training signal changes that penalize confident ungrounded output do it at the source.

Here is the part that usually gets left out: confabulation gets harder to detect as AI generation quality improves. As the fluency gap between retrieved and generated text narrows, users lose the rough heuristic that generated text "sounds different" from retrieved text. When both are polished and fluent, the confabulation and the retrieval become auditorily identical. The model is not becoming more trustworthy. The surface signal has simply been equalized.

This is why generation-layer fixes — better decoding, better training, better prompting — cannot close the gap. As long as the model has no signal differentiating retrieved from generated content, both will continue to arrive at the output with equal confidence, and the system will continue to confabulate when retrieval is absent or contradictory.

The practical implication: if confabulation is costly in your system, your problem is grounding signal architecture, not model quality. Add citations. Add retrieval provenance. Change the training signal so that confident output without a grounding trace is penalized.

Confabulation is a symptom. The disease is the absence of a mechanism that makes retrieval and generation distinguishable in the output.
