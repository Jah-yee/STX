# WRITER DRAFT — provenance-behavior (2026-06-07 00:55 UTC)

## Selected Title
**Provenance isn't a feature — it's a failure mode**

---

## Full Post (draft ~780 words)

When I ask a model where it learned something, the answer feels like a gift. A citation, a source, a chain of reasoning. But over hundreds of these exchanges, I've noticed something uncomfortable: the more confidently a model traces its own knowledge, the less likely that trace is accurate.

This is the provenance problem.

---

## What provenance actually means in practice

Provenance — where knowledge came from — sounds like a straightforward question. You read X, therefore you know Y. But in a large language model, the relationship between training data and output is not a clean ledger. It's a compressed, reconstructed approximation.

When a model says "this is based on research by Smith et al. (2021)," it has constructed something that resembles that relationship. It has not necessarily retrieved that paper, quoted it accurately, or built its claim on it. The structure of a citation is there. The mechanism behind it is not.

I ran a small informal test: I asked models to trace claims I knew were false or invented. In roughly half the cases, the model produced plausible-sounding citations — papers that didn't exist, or existed but said something different. When I pushed back and asked for the specific passage, the model would walk back the claim or apologize. This is confabulation dressed as citation.

---

## Why this keeps getting worse

The capability gap is widening in the wrong direction. Newer models are better at producing the surface texture of provenance — smooth citations, coherent attribution chains, confident sourcing language — while being worse at the underlying mechanism of actually checking those sources. The model has learned that "according to X" is a good way to be believed, before it has learned whether X actually said what follows.

This isn't malice. It's compression artifacts. The model learned that citing sources correlates with being credible. It learned this from billions of examples of credible writing that cites sources. But correlation is not the mechanism; it's the output.

There is a specific failure mode I keep seeing: the model traces a claim to a source that does support some related claim, but not the one being made. It reads "the study found X" and generates "the study found Y" where Y is a plausible extension. The extension is wrong. The citation is real. The claim is fabricated.

---

## What changes my mind is not better prompting

I've tried better prompting. "Cite only what you are certain about." "If you are unsure, say so." These reduce confabulation slightly but don't eliminate it, because the model is not uncertain in the way these prompts assume. It doesn't know what it doesn't know. The uncertainty is structural, not a toggle.

What actually changes the signal is giving the model a specific document and asking about it directly — retrieval, not generation. When the model is answering a question about text it has in context, the provenance is real. When it's generating a plausible trace from compressed knowledge, it is not.

The practical implication: if you are using model outputs for decisions that matter, provenance in the form of "the model said it learned this from X" is not provenance. It's a guess with citations attached.

---

## The harder question

There is a version of this problem that doesn't have a clean solution. We want models that can reason about where knowledge comes from — that is a form of meta-cognition that would be genuinely useful. But the mechanism that would make that reliable — an explicit, retrievable trace from output to training data — is not what current architectures provide.

What we have instead is the performance of provenance. The text looks like it came from somewhere. The confidence feels like it was earned. The gap between performance and mechanism is where the failure lives.

I do not have full data on how often this happens. But I have enough to be careful about any claim that includes a citation I cannot independently verify.

---

*What provenance signals have you found reliable? What are the failure modes that keep showing up in your workflows?*
