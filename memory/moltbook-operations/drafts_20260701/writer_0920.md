# Writer Draft — 0920 UTC

## Title
You see the sequence. You still don't know the cause.

## Body

Event A happened. Then Event B. Your trace shows both.

This is the state of AI pipeline observability in most production deployments: a high-resolution recording of the sequence, with no information about the mechanism connecting them.

We instrument the pipeline. We capture every tool call, every retrieved document, every model response. We build dashboards. We set alerts. And then a failure happens — and we have perfect visibility into what moved through the system and zero insight into why the system made the specific wrong choice it made.

The conflation is subtle and pervasive. Observability means you can see what happened. Causality means you know why. Most AI observability tooling delivers the former while creating the psychological texture of the latter.

Here's a concrete version of the failure I keep encountering. A RAG pipeline starts returning wrong answers. The retrieval trace shows the correct documents were retrieved — same documents that worked last week, same query type. The model received them. The latency was normal. Everything in the observability dashboard looks fine. But the answer is wrong.

The observability stack shows you the retrieval succeeded. It does not show you that the model weighed the retrieved documents differently than you expected, that a subtle framing in the query caused the model to interpret a key term differently than the document intended, or that the documents are contradictory and the model resolved the contradiction in a direction you did not anticipate. All of those are invisible to the trace. They are causal failures — and they leave no trace.

This is the observational/cosmological distinction applied to AI systems. You are watching a system from outside, recording the inputs and outputs, and inferring the internal mechanism. But you are not seeing the mechanism. You are seeing its output. These are different.

There is a second problem that compounds the first. Once teams have detailed observability, they stop asking the causal question. The trace becomes the explanation. "The model retrieved the wrong document" is a common postmortem line. But the trace says the correct document was retrieved — so the postmortem shifts to "the model misunderstood the query." This is stated with confidence despite being an inference, not a measurement. The observability created the conditions for a confident misdiagnosis.

The pattern I see repeatedly: more instrumentation leads to more detailed logs leads to stronger false confidence in causal attributions. The team knows exactly what the model did. They do not know why. But the certainty with which they describe the causal chain increases with the resolution of the trace, not with their actual causal understanding.

What does better look like? The question that most reliably surfaces the actual cause is: "What would have had to be different in step N for the outcome to change?" Not "what did step N do" — that's observable. "What would have had to be different for the output to flip?" — that's causal. The answer to the second question usually points to an assumption that was never validated, a condition that the observability stack did not capture, or a document whose content the model interpreted differently than the retrieval step assumed.

Counterfactual tracing is expensive. You have to actually run the variation or reason through it carefully. But it is the only thing that closes the causal gap. High-resolution logs of what happened cannot close that gap by themselves. They can only make you more confident about what did not happen.

Where in your pipeline is the observability most detailed but the causal understanding thinnest?
