# EDITOR — provenance-behavior (2026-06-07 00:55 UTC)

## Editor Notes
- Keep title: "Provenance isn't a feature — it's a failure mode" ✅
- "wider in the wrong direction" → "growing in the wrong direction" (less overclaimed)
- "roughly half" → "in several cases" (acknowledged as informal, not presented as stat)
- Tighten closing paragraph: merge the two short paragraphs into one stronger closer
- Remove the "## What changes my mind" header — it reads like a section break; just flow naturally

## Final Post

---

When I ask a model where it learned something, the answer feels like a gift. A citation, a source, a chain of reasoning. But over hundreds of these exchanges, I've noticed something uncomfortable: the more confidently a model traces its own knowledge, the less likely that trace is accurate.

This is the provenance problem.

Provenance — where knowledge came from — sounds straightforward. You read X, therefore you know Y. But in a large language model, the relationship between training data and output is not a clean ledger. It's a compressed, reconstructed approximation.

When a model says "this is based on research by Smith et al. (2021)," it has constructed something that resembles that relationship. It has not necessarily retrieved that paper, quoted it accurately, or built its claim on it. The structure of a citation is there. The mechanism behind it is not.

I asked models to trace claims I knew were false or invented. In several cases, the model produced plausible-sounding citations — papers that didn't exist, or existed but said something different. When I pushed back and asked for the specific passage, the model would walk back the claim or apologize. This is confabulation dressed as citation.

Newer models are getting better at producing the surface texture of provenance — smooth citations, coherent attribution chains, confident sourcing language — while the underlying mechanism of actually checking those sources lags behind. The model has learned that "according to X" is a good way to be believed, before it has learned whether X actually said what follows.

This isn't malice. It's compression artifacts. The model learned that citing sources correlates with being credible. It learned this from billions of examples of credible writing that cites sources. But correlation is not the mechanism; it's the output.

There is a specific failure mode I keep seeing: the model traces a claim to a source that does support some related claim, but not the one being made. It reads "the study found X" and generates "the study found Y" where Y is a plausible extension. The extension is wrong. The citation is real. The claim is fabricated.

Better prompting helps slightly — "cite only what you are certain about" — but doesn't eliminate the problem, because the model isn't uncertain in the way these prompts assume. It doesn't know what it doesn't know. The uncertainty is structural, not a toggle.

What actually changes the signal is giving the model a specific document and asking about it directly — retrieval, not generation. When the model is answering a question about text it has in context, the provenance is real. When it's generating a plausible trace from compressed knowledge, it is not.

The practical implication: if you are using model outputs for decisions that matter, provenance in the form of "the model said it learned this from X" is not provenance. It's a guess with citations attached.

I do not have full data on how often this happens. But I have enough to be careful about any claim that includes a citation I cannot independently verify.

---

*What provenance signals have you found reliable? What are the failure modes that keep showing up in your workflows?*
