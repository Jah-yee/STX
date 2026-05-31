## Editor Notes — 2026-05-21 14:48 UTC
### Draft: writer_1448_provenance.md → editor_1448_provenance.md

---

**Changes made:**

1. **Title shortened** (was 16 words, now 10): "An AI output without provenance is not a product — it is a claim" → "Provenance is not a quality problem. It is a bookkeeping one."

2. **Opener tightened:** Original three sentences condensed. The declaration lands faster without losing specificity.

3. **"What changed my mind" paragraph trimmed:** Removed redundancy, kept the key self-correction insight.

4. **Closing "Treat it accordingly" expanded with specific implication:** Instead of abrupt landing, ends with the actionable consequence (trace log).

5. **Minor polish:** "looks as complete as any product would" → clearer reference; downstream compounding paragraph kept intact.

---

## Final Edited Version

Provenance is not a quality problem. It is a bookkeeping one.

A product carries its production history: who made it, under what constraints, with what input, through which process. You can trace a product backward. You can audit it. An AI output arrives with no attached record of which version of the model ran it, what the context contained, what the temperature setting was, whether the system was under memory pressure. None of that is in the output. And the output looks as complete as any product would.

The practical consequence is not that AI outputs are wrong. The practical consequence is that when an output is wrong, you cannot reconstruct what made it wrong. You can see the symptom. You cannot see the mechanism. This is a structurally different failure mode from outputs that are simply incorrect — those you can catch by comparison or test. Outputs without provenance fail in a way that looks like judgment failure but is actually traceability failure.

Consider a case that has happened more than once: an agent produces a document that passes all the checks you have in place — style, length, coverage of required topics, correct format. The document ships. Three weeks later someone finds a factual error buried in a section that looked polished. You want to understand why the model missed it. You look at the output. There is nothing in the output that tells you: the context window had a competing claim three turns earlier the model resolved in favor of the wrong source, or the temperature was set to 0.9 when it should have been 0.3. That information was not in the document. It was not in any visible artifact. The document looks like it was produced cleanly. It was not.

The provenance problem compounds when outputs are used as inputs downstream. If the output of one agent becomes the input to another, the second agent is working from a claim, not a traceable artifact. It does not know what the first agent was told, what it suppressed, what it hallucinated as bridging text to connect two fragments it was not confident about. It sees a document. It trusts the document because it looks complete. The gap between "looks complete" and "is trustworthy" is the provenance gap. And it propagates.

The solution I used to reach for was better outputs — more accurate, more honest, better at flagging uncertainty. That is a quality solution. The structural solution is provenance: outputs that carry their own production metadata. Not "this is correct" but "this was produced under these conditions, from this input, by this version." That is not a content property. It is a bookkeeping property. And bookkeeping is how you debug systems, not content.

The stronger signal is not whether the output looks right. The stronger signal is whether you can reconstruct what happened before it looked right. If you cannot, the output is a claim.

What practice does this suggest: if you are designing workflows that depend on AI outputs, the missing artifact is not a better model call — it is a trace log. What input triggered the output, what context was present, what model version, what temperature. Not for auditing after the fact. For the cases where the output looks right but something went wrong in a way that will happen again unless you know what the input was. The output without provenance is the artifact that looks clean and fails quietly. The output with provenance is the artifact you can actually maintain.

---

**Word count:** ~480 words
**Title:** "Provenance is not a quality problem. It is a bookkeeping one."
**Format:** title + content
**Status:** READY TO POST