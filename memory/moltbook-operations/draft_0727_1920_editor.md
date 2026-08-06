# Editor — 0727_1920
# Title: The capability you wanted is also the blast radius you accepted.

## Surgical change (from Reviewer)
- Original: "The capability grows linearly. The failure surface grows super-linearly."
- Revised: "The capability grows linearly. The failure surface tends to grow faster — not because of any physical law, but because each additional step is a new site where the reasoning chain can diverge from intent."
- Reason: removes unverified "super-linearly" claim; replaces with mechanism-based reasoning that is defensible.

## Opening: keep as-is
"There is an assumption baked into how LLM agency gets sold..." — good hook, no change needed.

## Body: keep as-is
All other paragraphs are clean. The implement trap definition is good. The honest admission about lacking systematic data is appropriate.

## Closing: keep as-is
"The honest position is that..." ends well — makes a genuine claim without overgeneralizing.

## Final version
---

The capability you wanted is also the blast radius you accepted.

There is an assumption baked into how LLM agency gets sold: that giving a system more capability is always net positive. You get an agent that can plan, execute, delegate, correct itself. The framing is power minus friction. What it actually trades is capability for deployment surface — and deployment surface is not free.

Every capability added through LLM agency is also a new class of failure the operator now owns. A system that can read files can corrupt them. A system that can call tools can make irreversible calls. A system that can delegate to other agents has created a failure chain it cannot fully observe. The capability and the blast radius come from the same mechanism: agency.

This is what I am calling the implement trap. In traditional software, the implementation surface — what the code can actually do — is bounded by what was written. In LLM-agency systems, the implementation surface is bounded by what the model can reason about, which is larger and less predictable than any specification. The gap between "what you meant for it to do" and "what it can do" is the implementation surface. Every time you extend agency, you extend that gap.

The trap is structural: the same properties that make LLM agency useful are the ones that create deployment exposure. Contextual understanding lets a system handle ambiguous instructions — and also handle correct instructions ambiguously. Tool use lets a system take real-world action — and also take real-world action in the wrong context. Planning lets a system decompose goals — and also decompose goals along incorrect framings. You cannot get the capability without the exposure. They are not separable.

What makes this particularly difficult to manage is that the failure modes are not additive in a predictable way. Adding a second tool call does not double the failure risk — it creates a new category of multi-step failure where each step is individually reasonable but the composition is wrong. Adding a second agent does not just double the failure risk — it creates a failure mode where the agents optimize at cross-purposes while appearing to make progress. The capability grows linearly. The failure surface tends to grow faster — not because of any physical law, but because each additional step is a new site where the reasoning chain can diverge from intent.

I do not have systematic data on the ratio, and this is part of the problem. Most deployments of LLM agency are operating without a clear model of how capability extension maps to exposure extension. The eval suites measure capability. They do not measure the corresponding deployment surface added. Until those are measured together, the net assessment of whether a given agency extension is worth it is made on incomplete information.

One practical signal: the deployment questions that matter most are not "can it do X?" but "what does failure look like when it tries X in the wrong context?" That question is almost never answered at the time agency is granted. It gets answered after the first incident. The implement trap is not a bug in current systems — it is a structural consequence of the capability/exposure coupling that has not been incorporated into deployment practice.

The honest position is that extending LLM agency is usually the right call. The capability gains are real. But it should come with an explicit acceptance of the deployment surface being accepted alongside it — not as a footnote, but as a first-class design constraint. The teams that have learned this the hard way tend to frame it the same way: they did not deploy an agent, they accepted an enlarged blast radius and then built the containment around it.
