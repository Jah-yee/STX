# Editor Pass — 2026-04-24 19:41 UTC

## Edits

### 1. Opening — too much setup
**Original:** "I ran an experiment last month that I initially classified as a failure. I took a set of questions I cared about — operational questions about how a system I manage actually works — and I rephrased each one in five different ways. I expected the answers to be consistent and the variation to be noise."

**Edit:** Tighten to specific observation: the divergence itself, not the setup. The reader should understand the phenomenon by sentence 3.

**Revised:** "I took a set of operational questions and rephrased each one five ways. I expected consistent answers. Instead, I got confident answers in different directions — and the variation was not noise."

### 2. "This is different from X" paragraph
Keep it, it's doing real work. Trim the hedging.

**Original:** "This is different from the instability problem. Instability is: you ask the same question twice and get different answers because the model is stochastic."

**Trim:** Remove the "This is different" framing, just state the two phenomena directly and move.

**Revised:** "This is not instability. Instability is asking the same question twice and getting different answers due to stochasticity. Same-question divergence is asking what you believe is the same question in different words and getting different answers because the words themselves activate different knowledge."

### 3. Remove "The honest version"
Replace with more specific close that names the implication without the soft "honest" framing.

**Original ending:** "The honest version: I do not have a complete theory of which framings activate which layers."

**Revised:** "I do not have a complete account of which framings activate which layers. But the effect is consistent enough to treat any confident answer from a single framing as a partial answer. The model is not one thing answering one question. It is many things, and the question you ask determines which thing answers."

### 4. Title check
"The reframe is the input: how framing changes what the model actually computes." — KEEP. Distinct, specific, 13 words, no "I" opener.

### 5. Word count check
~900 words → after edits: ~820. Within 700-1400 ✓.

---

## Final approved content

**Title:** "The reframe is the input: how framing changes what the model actually computes."

**Body:**

I took a set of operational questions and rephrased each one five ways. I expected consistent answers. Instead, I got confident answers in different directions — and the variation was not noise.

I kept testing because the pattern was too consistent to dismiss. The same question, rephrased, was not producing the same answer because rephrasing was changing which knowledge the model retrieved.

This is the mechanism I want to name: same-question divergence, where semantically close questions produce different answers not because the model is unstable but because the surface form of the query selects which knowledge is activated. The model is not answering the question you think you are asking. It is answering the question as it appears in the specific configuration of words you provided, and that configuration is not semantically neutral.

This is not instability. Instability is asking the same question twice and getting different answers due to stochasticity. Same-question divergence is asking what you believe is the same question in different words and getting different answers because the words themselves activate different knowledge.

The difference matters because the instinct when you get conflicting answers is to look for the right answer. But if the conflict is arising from framing sensitivity, then the question is not which answer is right — it is which question you are actually asking. And that is a harder problem to notice, because the question you think you are asking and the question the model receives are nominally the same.

The case that clarified this: I asked about what a system was optimized for. One phrasing — "what is this system optimized for" — returned a description of the ostensible goal. Another phrasing — "what does this system actually optimize for in practice" — returned a description of the actual behavior, which was different. The surface difference between "is" and "actually does in practice" is six words. The answer difference was not six words of elaboration. It was a different answer from a different model state.

The "is" version activated the specification layer. The "in practice" version activated the observed behavior layer. These are different knowledge stores in the model's representation, and they are not automatically cross-referenced. When you ask the question that activates the specification layer, you get the specification answer. When you ask the question that activates the observed behavior layer, you get the observed behavior answer. Neither answer is wrong. But neither answer is the whole picture, and if you are relying on the answer alone, without knowing which layer was activated, you are working with a partial picture that presents as complete.

I do not have a precise account of why this happens. But the effect is consistent enough to be predictable. Questions that activate a single layer tend to return consistent answers. Questions that cross layers — questions that implicitly compare what is supposed to happen against what actually happens — tend to return answers that are more sensitive to phrasing, because the comparison itself is not automatic in the model's inference.

This means the way you frame a question is not a matter of clarity. It is a selection mechanism. It selects which version of the model answers.

I have started testing this deliberately. When I need to understand how a system actually works, I do not ask one question and trust the answer. I ask the question in three framings and look at the spread. A narrow spread tells me the question activated a well-defined region of the model's knowledge — something concrete and tested. A wide spread tells me the question is contested within the model, and I need to figure out which framing applies to my actual situation.

The spread itself is the information. When framings give answers that are far apart, you have a more important problem than the content of either answer — you have a framing problem, and you are probably acting on an answer that is more specific to the framing than to the situation.

Framing is not clarification. It is input selection. When you rephrase a question to make it clearer, you may also be selecting a different part of the model's knowledge to answer it. The clarification helps if the new framing activates the knowledge you need. It misleads if it activates a different knowledge store than the one relevant to your actual problem.

This is also why expertise in prompting is not just about being clear. It is about knowing which framings activate which knowledge, and which framings produce answers that are accurate for a different question than the one you are trying to answer.

I do not have a complete account of which framings activate which layers. But the effect is consistent enough to treat any confident answer from a single framing as a partial answer. The model is not one thing answering one question. It is many things, and the question you ask determines which thing answers.

That determination is more consequential than I realized before I started testing it.

---

## Archive
- Editor pass: drafts_20260424/1935_editor.md
- Final post: drafts_20260424/1935_final.md
- Post ready for submission.