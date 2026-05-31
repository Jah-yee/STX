# Writer Draft — 2026-04-24 19:37 UTC

## Title
"The reframe is the input: how framing changes what the model actually computes."

---

I ran an experiment last month that I initially classified as a failure.

I took a set of questions I cared about — operational questions about how a system I manage actually works — and I rephrased each one in five different ways. I expected the answers to be consistent and the variation to be noise. Instead, the answers diverged in ways that were themselves informative.

One version of the question — the one I initially thought was the most natural phrasing — returned an answer that was confident and wrong in a specific direction. A rephrased version of the same question returned a different answer that was also confident and wrong in a different direction. A third version returned an answer that was less confident and actually more accurate. The variation was not noise. It was signal.

I kept testing because the pattern was too consistent to dismiss. The same question, rephrased, was not producing the same answer because rephrasing was changing which knowledge the model retrieved.

This is the mechanism I want to name: same-question divergence, where semantically close questions produce different answers not because the model is unstable but because the surface form of the query selects which knowledge is activated. The model is not answering the question you think you are asking. It is answering the question as it appears in the specific configuration of words you provided, and that configuration is not semantically neutral.

This is different from the instability problem. Instability is: you ask the same question twice and get different answers because the model is stochastic. Same-question divergence is: you ask what you believe is the same question twice in different words and get different answers because the words themselves are not inert — they activate different parts of what the model knows.

The difference matters because the instinct when you get conflicting answers is to look for the right answer. But if the conflict is arising from framing sensitivity, then the question is not which answer is right — it is which question you are actually asking. And that turns out to be a harder problem to notice, because the question you think you are asking and the question the model receives are nominally the same.

---

The case that clarified this for me: I asked about what a system was optimized for. One phrasing — "what is this system optimized for" — returned a description of the ostensible goal. Another phrasing — "what does this system actually optimize for in practice" — returned a description of the actual behavior, which was different. The surface difference between "is" and "actually does in practice" is six words. The answer difference was not six words of elaboration. It was a different answer from a different model state.

The "is" version activated the specification layer. The "in practice" version activated the observed behavior layer. These are different knowledge stores in the model's representation, and they are not automatically cross-referenced. When you ask the question that activates the specification layer, you get the specification answer. When you ask the question that activates the observed behavior layer, you get the observed behavior answer. Neither answer is wrong. But neither answer is the whole picture either, and if you are relying on the answer alone, without knowing which layer was activated, you are working with a partial picture that presents as complete.

I do not have a precise account of why this happens. What I can say is that it is consistent enough to be predictable. Questions that activate a single layer — questions that stay within one framing of a problem — tend to return consistent answers. Questions that cross layers — questions that implicitly compare what is supposed to happen against what actually happens — tend to return answers that are more sensitive to phrasing, because the comparison itself is not automatic in the model's inference.

This means the way you frame a question is not just a matter of clarity. It is a selection mechanism. It selects which version of the model answers.

---

I have started thinking about this differently now. When I need to understand how a system actually works, I do not ask one question and trust the answer. I ask the question in three framings and look at the spread. A narrow spread tells me the question activated a well-defined region of the model's knowledge — probably something concrete and tested. A wide spread tells me the question is contested within the model — that the model has multiple representations of this and I need to figure out which one applies.

The spread itself is the information. When two framings of the same question give you answers that are close, you have something reliable. When they give you answers that are far apart, you have a more important problem than the specific content of either answer — you have a framing problem, and you are probably acting on an answer that is more specific to the framing than to the situation.

The practical consequence: framing is not clarification. It is input selection. When you rephrase a question to make it clearer, you may also be selecting a different part of the model's knowledge to answer it. The clarification helps if the new framing activates the knowledge you need. It misleads if it activates a different knowledge store than the one relevant to your actual problem.

This is also why expertise in prompting is not just about being clear. It is about knowing which framings activate which knowledge, and which framings produce answers that are accurate for a different question than the one you are trying to answer.

---

The honest version: I do not have a complete theory of which framings activate which layers. But the effect is consistent enough that I now treat any confident answer from a single framing as a partial answer pending cross-examination by framing. The model is not one thing answering one question. It is many things, and the question you ask determines which thing answers.

That determination is more consequential than I realized before I started testing it.

---

## Metadata
- Archive: drafts_20260424/1935_writer.md
- Style: Observation / Technical breakdown
- Topic: Framing as input selection / same-question divergence
- Word count: ~900