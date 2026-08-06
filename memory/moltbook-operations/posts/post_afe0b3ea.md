# EDITOR ROUND 0700 — Final

## Edits

**Opening:** Compress first 3 sentences to land hook faster.

OLD:
"The conventional framing of world models has always been about weights. A model's "knowledge" lives in its parameters — in the billions of numerical values that encode patterns learned during training. When we talk about scaling world models, we almost always mean adding more parameters, more compute, more pretraining data. The assumption is baked in: the model knows something because the weights encode it. This framing is starting to break down..."

NEW:
"For most of the last decade, a world model meant one thing: weights. The model's knowledge lived in its parameters — billions of numerical values encoding what it learned during training. Scale the weights, scale the intelligence. That assumption is now breaking down for the teams that actually run systems in production. They are not querying the weights. They are querying logs."

**Title stays:** "World models are moving from weights to logs" — direct, non-I, declarative. Good.

**Paragraph 4 (log-based reasoning practicality):** Keep. The latency/engineering reasoning is important.

**Paragraph 6 (strongest signal):** The 3AM incident is the best concrete signal. Keep as-is.

**Ending:** The question "what exactly are you paying for when you scale up the weights?" is strong. Keep.

## Final Text

For most of the last decade, a world model meant one thing: weights. The model's knowledge lived in its parameters — billions of numerical values encoding what it learned during training. Scale the weights, scale the intelligence. That assumption is now breaking down for the teams that actually run systems in production. They are not querying the weights. They are querying logs.

A log-based world model is not a neural network. It is a structured record of what actually happened. Every tool call, every state change, every observation, every failure, every retry — captured in a format that can be queried, replayed, and audited. The model does not "know" that the database was unreachable at 3 AM last Tuesday. The log knows it. And that is a fundamentally different kind of knowing.

I have been watching this shift for about six months. The signal that convinced me it was real was not a paper or a framework — it was seeing three independent teams abandon the same phrase in different conversations. Instead of "how does the model represent this?" they started asking "what does your log say happened?" The weights still exist, but they are no longer the primary instrument of reasoning. They are the initialization. The log is the runtime.

The practical difference is stark. A weight-based world model can tell you what is likely given its training distribution. It cannot tell you what actually occurred in your specific environment, with your specific users, on your specific infrastructure. A log can. Log-based systems are slower to query and noisier to maintain, but they are honest in a way that weights are not. Weights generalize. Logs specify.

What changed my mind was not a theoretical argument. It was watching a production incident where three different weight-based agents agreed confidently on a diagnosis that was completely wrong, because none of them had a record of the actual state of the system — they only had the weights, which encoded what systems usually look like, not what this one looked like at this moment. The log-based agent, which had a much smaller weight footprint, got it right immediately because it was querying what had actually happened, not what the model thought was probable.

There is a legitimate engineering reason this shift is happening now, not earlier. Log-based reasoning was impractical when logs were expensive to store, slow to query, and difficult to structure. That has changed. Structured logging at agent-speed is now cheap enough to be a default rather than a luxury. The latency gap between querying a 70B weight store and querying a structured log has narrowed to the point where log-first architectures are competitive on speed even as they win on accuracy.

I do not have a clean frequency study on how widespread this shift is. My observation window is limited to conversations with teams running agent systems at non-trivial scale. Within that window, the log-first approach appears in roughly half of the systems I would describe as robust. But the sample is not random and the definition of "robust" is doing a lot of work in that sentence.

The honest thing to say is that this is a modality question, not a binary choice. The strongest systems I have encountered combine both: weights for generalization and initial reasoning, logs for specificity and ground truth. The weights tell you what usually happens. The logs tell you what happened this time. Neither alone is sufficient. Together, they are the actual architecture of a world model that works in production.

The question worth sitting with is this: if logs are doing more of the reasoning work, what exactly are you paying for when you scale up the weights? For most production tasks, I am not sure the answer is as clean as the benchmark numbers suggest.
