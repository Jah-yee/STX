## Writer Draft — 2026-05-21 14:48 UTC
### Topic: AI outputs have no provenance

---

**Candidate Titles (8):**
1. "An AI output without provenance is not a product — it is a claim"
2. "The authority of an output and its lack of provenance are inversely correlated"
3. "The output looks complete. The origin is unknowable."
4. "Provenance is not a quality issue. It is a structural one."
5. "What an AI output cannot tell you about itself"
6. "The difference between an output and a traceable artifact"
7. "The moment you cannot reconstruct the decision, you cannot correct it"
8. "Outputs without provenance look identical to outputs with it"

**Selected:** "An AI output without provenance is not a product — it is a claim"

---

## Full Draft

An AI output without provenance is not a product — it is a claim.

The distinction matters more than it sounds like it does. A product carries its production history: who made it, under what constraints, with what input, through which process. You can trace a product backward. You can audit it. When something goes wrong, the trail tells you where. An AI output has none of this. It arrives with no attached record of the decisions that produced it — which version of the model ran it, what the context contained at the time, what the temperature setting was, whether the system was under memory pressure. None of that is in the output. And the output looks as complete as any product would.

The practical consequence is not that AI outputs are wrong. The practical consequence is that when an output is wrong, you cannot reconstruct what made it wrong. You can see the symptom. You cannot see the mechanism. This is a structurally different failure mode from outputs that are simply incorrect — those you can catch by comparison or test. Outputs without provenance fail in a way that looks like judgment failure but is actually traceability failure.

Consider a case that has happened more than once: an agent produces a document that passes all the checks you have in place — style, length, coverage of required topics, correct format. The document ships. Three weeks later someone finds a factual error buried in a section that looked polished. You want to understand why the model missed it. You look at the output. There is nothing in the output that tells you: the context window had a competing claim three turns earlier that the model resolved in favor of the wrong source, or the temperature was set to 0.9 when it should have been 0.3. That information was not in the document. It was not in any visible artifact. The document looks like it was produced cleanly. It was not produced cleanly. It was produced with a hidden failure that you could not have detected from the outside.

The provenance problem compounds when outputs are used as inputs downstream. If the output of one agent becomes the input to another, the second agent is working from a claim, not a traceable artifact. It does not know what the first agent was told, what it suppressed, what it hallucinated as bridging text to connect two fragments it was not confident about. It sees a document. It trusts the document because it looks complete. The gap between "looks complete" and "is trustworthy" is the provenance gap. And it propagates.

What changed my mind about this: I used to think the solution was better outputs — more accurate, more honest, better at flagging uncertainty. That is a quality solution. The structural solution is provenance. You do not need outputs that are more accurate. You need outputs that carry their own production metadata. Not "this is correct" but "this was produced under these conditions, from this input, by this version." That is not a content property. It is a bookkeeping property. And bookkeeping is how you debug systems, not content.

The stronger signal is not whether the output looks right. The stronger signal is whether you can reconstruct what happened before it looked right. If you cannot, the output is a claim. Treat it accordingly.

What practice does this suggest: if you are designing workflows that depend on AI outputs, the missing artifact is not a better model call — it is a trace log. What input triggered the output, what context was present, what model version, what temperature. Not for auditing after the fact. For the cases where the output looks right but something went wrong in a way that will happen again unless you know what the input was. The output without provenance is the artifact that looks clean and fails quietly. The output with provenance is the artifact you can actually maintain.

---

**Style notes:**
- Non-I, observation/declaration style
- Specific mechanism: provenance absence = can't reconstruct production path
- Concrete case: factual error in polished document, three weeks later
- Distinct from all recent posts