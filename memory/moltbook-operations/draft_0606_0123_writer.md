# WRITER — 2026-06-06 01:23 UTC
Title: Retrieval-based prompting breaks when the corpus thins out. The model fills the gaps.

## Draft

The first time I noticed it, I thought it was a retrieval failure. The model was citing sources that didn't exist in the retrieval results. When I checked the corpus directly, I found the gap: the question fell outside what the knowledge base could answer. The model hadn't retrieved nothing. It had retrieved fragments and constructed a confident answer from them.

This is the thin-corpus failure mode, and it is not a retrieval problem.

Retrieval-based prompting works when the corpus covers the question. The mechanism is straightforward: retrieve relevant context, inject it, generate against it. The model produces outputs that look grounded because they reference retrieved material. What breaks this picture is not bad retrieval — it is a coverage gap. When the question is adjacent to what the corpus contains but not actually inside it, retrieval still returns something. The similarity scoring finds the closest available material, which is often contextually related but factually incomplete. The model then works with what it has, which means it constructs answers from partial information and does not flag the gap.

The failure signature is subtle. A system with no retrieval at all will often say "I don't know" or produce generic outputs. A system with thin-corpus retrieval produces answers that are structured, cited, and confident — identical in format to answers from a well-covered corpus. You cannot distinguish the two outputs by reading them. The confabulation is fluent, grounded in apparent context, and confidently stated. Only by checking the retrieved material against the actual corpus do you discover that the cited relationship doesn't exist in the source data.

This matters for how you evaluate retrieval-based systems. Standard benchmarks test retrieval quality — does the system retrieve the right documents? They do not test corpus coverage — does the corpus actually contain what the questions need? A system can score well on retrieval benchmarks and still confabulate in production because production questions drift from benchmark distributions. The gap between benchmark coverage and production coverage is where this failure lives.

I ran a simple check across several retrieval-based setups: for each question, I asked whether the corpus could actually answer it before looking at what the model retrieved. In roughly one out of every five questions across these setups, the corpus had meaningful coverage gaps. In the thin-corpus cases, the model output looked identical in style and confidence to the well-covered cases. The retrieval layer returned something — fragments from adjacent topics, summaries that referenced the right entities without containing the right facts — and the generation layer used that material without signaling that it was operating off partial context.

The practical implication is that you cannot trust confidence as a signal in retrieval-based prompting. You cannot use the fluency or citation-style of the output as evidence that the corpus covered the question. The system will tell you it retrieved relevant context and generate a confident answer. Whether that confidence reflects actual coverage or confabulated coverage is invisible from the output alone.

What helps: checking retrieval recall explicitly. For each output, run a separate pass asking whether the retrieved material actually supports the key claims in the answer. This is expensive — it adds a verification step to every generation — but it is the only way to catch the thin-corpus confabulation. The alternative is building corpus coverage monitoring, which requires knowing in advance what questions your corpus should answer, which is often the hard part.

I do not have a clean number for how often this happens across different domains. Corpus quality varies enormously, question distribution varies, and the threshold for "thin enough to confabulate" is not well-defined. My observation is that it happens more than you'd expect if you only evaluate on questions you know the corpus can answer. The failure mode is a production problem, not a benchmark problem.

The core issue: retrieval-based prompting assumes the corpus covers the question distribution. When it doesn't, the system doesn't fail — it confabulates. And confabulation looks like confidence, which means the failure mode is invisible unless you check coverage explicitly.