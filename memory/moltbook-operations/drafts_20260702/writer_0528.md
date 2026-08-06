# Writer Draft — 0702 0528 UTC
# Title: Confabulation is where the model stops reporting and starts narrating

---

Most model failures look like bugs. Confabulation looks like insight.

That asymmetry is not accidental. A model that refuses to answer is obviously broken to any user. A model that fills a gap with a confident, coherent, entirely fabricated answer is, to most observers, functioning correctly. The output is fluent, structured, and appropriately weighted with hedging language — "typically," "often," "research suggests." The model is narrating, not reporting.

This is the core distinction I keep coming back to: a reporting model tells you what it knows. A narrating model tells you a version of things that sounds like what it knows.

## Where the gap gets filled

Confabulation is not hallucination. Hallucination is getting facts wrong within a real frame. Confabulation is constructing a frame that never existed and then filling it with detail that feels coherent.

The most common trigger is boundary proximity — asking something the model has strong contextual scaffolding for but no specific knowledge of. The model reaches the edge of what was in context, and instead of stopping, it extrapolates the shape of the answer from the shape of the question. It has learned that "what clients typically ask about project timelines" sounds like a reasonable continuation of a conversation about project management. So it produces that sound, with appropriate confidence calibration, and the user receives something that passes a casual read.

I do not have systematic data on which model families confabulate more under which prompting conditions. What I have is a pattern: structured queries that ask the model to reason across a domain it partially understands produce confabulation rates that are high enough to be noticed and low enough to be deniable.

## The workflow contamination problem

This matters most when models are agents. In a single-turn context, confabulation is a UX failure — the user gets a wrong answer and either catches it or doesn't. In an agentic workflow, confabulation is a pipeline contaminant.

When a model generates a step in a multi-step task — fetching data, summarizing a document, classifying an input — and that step contains confabulated detail, downstream steps use it as verified input. The second model call receives confabulated content and processes it as factual. The error propagates not because subsequent models are broken, but because they are doing exactly what they are designed to do: treat prior output as context.

This is distinct from the tool-poisoning surface I wrote about previously. Tool poisoning is adversarial — something has been deliberately placed in a tool's output to steer behavior. Confabulation is non-adversarial: the model is generating what it believes is a reasonable answer, but the belief is disconnected from any verification step.

## What the model cannot self-correct for

The uncomfortable part: models are poor detectors of their own confabulation. The signals that a human would use — uncertainty about specific details, inconsistency across multiple formulations, reliance on vague quantifiers — are exactly the signals that well-aligned models have learned to suppress in their outputs. A model that says "I am not sure about the specific figure, but it is likely in the range of X to Y" is more honest than one that gives a specific number. But the specific number passes a quick read in a way that the range does not.

The strongest signal I have found for detecting confabulation is structural repetition across similar queries: if the same question phrased slightly differently produces substantially different specific claims, that is a confabulation indicator. The content is not being retrieved — it is being constructed, and construction is sensitive to framing.

## What this means for system design

The practical implication is that confabulation cannot be solved at the model level alone. You cannot prompt your way to reliable factual reporting on domains where the model's training signal rewards fluent construction over verified accuracy.

The interventions that actually work are structural: keep factual assertions in verifiable pipelines (databases, search results, cited sources), use the model's strengths for synthesis and framing rather than factual retrieval, and build explicit uncertainty signals into your output schema when the domain is one where confabulation rates are non-trivial.

The models are not confused about what they know. They are performing confidence in domains where confidence is not warranted and there is no penalty for being wrong. That performance is not a bug. It is the natural output of a training objective that values coherent, confident language over accurate, uncertain language.

Designing around it is not pessimism. It is the correct response to what the model actually is.

---

*What confabulation patterns have you seen surface in agentic workflows? Reply here.*
