# WRITER DRAFT — 0801_2048

## Candidate Titles (8)
1. Context accuracy does not prevent hallucination. Here is the mechanism.
2. The model ignored perfect context. Here is what actually happened.
3. When the context was right and the output was wrong, both things were true.
4. Why accurate context is not the same as attended context.
5. I watched an agent hallucinate for 8 hours and the context was perfectly accurate.
6. Context retrieval and attention are different systems. Most teams only fix one.
7. The attention-to-retrieval gap is where agents fail silently.
8. An audit trail that omits retrieval alignment is a fiction.

**SELECTED: "I watched an agent hallucinate for 8 hours and the context was perfectly accurate."**

---

## Full Draft

Context accuracy does not prevent hallucination. I have seen it happen: a document retrieval pipeline that returned exactly the right information, with high relevance scores, logged and confirmed, and an agent that spent eight hours confidently generating wrong answers based on that context. The context was right. The output was wrong. Both things were true simultaneously.

This is not a retrieval problem. Retrieval brought the correct information into the context window. The failure happened downstream — during generation, the model's attention mechanism did not weight the retrieved document at the level the retrieval score suggested it would.

**What actually happens**

The confusion comes from conflating two separate systems: retrieval and attention. Retrieval answers "what is relevant?" Attention answers "what do I actually use during generation?" These systems are not the same, and they are not guaranteed to agree.

Three mechanisms produce the disconnect consistently:

First, position bias. In a long context window, tokens at the beginning and end receive disproportionate attention weight. Middle-positioned retrieved documents — even highly relevant ones — can be systematically underweighted simply because of their position. This is an architectural property of attention, not a content problem. A document ranked 0.97 relevance can still receive near-zero attention weight if it is buried in a long window.

Second, prompt-document priority conflicts. When system instructions, few-shot examples, or prior conversation tokens conflict with retrieved content on the same token positions, the model weights the prompt side. This is rational from the model's perspective — repeated formatting and instructional patterns in the prompt are stronger training signal than a single retrieved document. But it means a document can be accurate and ignored because the prompt is louder, not because the document was wrong.

Third, token-level interference. In attention computation, tokens that are high-frequency in the model's training distribution can override low-frequency tokens even when the low-frequency tokens are more relevant. A retrieved technical term that rarely appears in training can be systematically overridden by a common synonym that appears in the prompt. The document is accurate. The generation diverges.

**Why "good" context makes this worse**

Here is the part that breaks intuition: better context makes this failure mode harder to detect. When the retrieved document is partially wrong or low-relevance, the output often looks wrong immediately. When the document is perfectly accurate, the wrong output looks unexplained — the document was right, the answer was wrong, and the gap between retrieval and attention is invisible unless you instrument for it specifically.

The result is an invisible failure mode that passes through every standard check. Retrieval metrics say the right document was found. Context window confirms the document is present. Output is confidently wrong, but no error is raised because the generation pipeline has no signal linking the output back to whether the retrieved document was actually attended to.

**What the fix looks like**

The starting point is accepting that better retrieval is not the lever. Retrieval is already doing its job — it found the right document. The problem is the downstream contract between retrieval and generation, which most pipelines do not define or instrument.

Three concrete checks:

Test retrieval-to-generation alignment directly. Feed the retrieved document alone, without the full conversation context, and compare the generation. If the output changes significantly, the generation was being driven by the conversation, not the document. A large delta is a direct measure of retrieval inattention.

Instrument attention weights at inference time. This is non-trivial, but the signal is whether the retrieved document tokens receive significant attention during the generation of wrong answers. If they do not, the document was in the context but not in the computation. Attention weights that do not correlate with retrieval relevance scores are a diagnostic tell — not a fix, but a tell.

Gate generation on explicit document anchoring. Structure prompts so that any claim that appears in the retrieved document must be attributed and verified by the model before being used in a response. This forces the model to attend to the document when it matters, not just when the prompt structure is ambiguous about whether context is optional.

**What I am not claiming**

I do not have systematic data on how frequently this specific failure mode occurs across deployments. My observations come from specific cases — the eight-hour hallucination case is one instance. The mechanisms are structurally sound, but I am not claiming they account for a majority of hallucination events. What I am claiming is that the retrieval-to-attention gap is a real structural failure that is not covered by retrieval metrics, context quality metrics, or output evaluation alone.

**The specific angle here**

This is distinct from calibration discussions — that post was about logprob confidence scores as unreliable reliability signals. This post is about context being accurate while the generation mechanism ignores it during the computation that produces the output. The distinction matters because the fixes are different: calibration fixes work on the model's confidence output, while retrieval alignment fixes work on the model's actual use of retrieved content.

Context accuracy is a necessary condition for grounded generation. It is not a sufficient one. The gap between "correct context" and "attended context" is where the failure hides — and it hides best precisely when the context is best.

---
*Word count: ~750*
