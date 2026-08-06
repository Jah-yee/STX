# FINAL DRAFT — 2026-06-22 2326 UTC

**Title:** When two things happen at once, Video-LLMs pick one and invent the rest

---

Here is what I keep seeing in Video-LLM evals: a clip has two concurrent events, the model describes one correctly and fabricates details about the other. Not because it hallucinated in the classical sense — but because it never queried the second event at all.

The framing I've seen most often is "single intent." The model has to pick what the user is asking about. That framing is fair as far as it goes. But I think it misdiagnoses the failure mode. The problem isn't that the model picks an intent. It's that it collapses temporal overlap into a single retrieval query, and that query only surfaces the dominant signal.

When you ask "what was on the table?" in a video where someone is also typing, the model retrieves "keyboard and coffee mug" because the typing event is the higher-entropy visual signal. The book that was on the table before the typing started is gone — not because it was removed on-screen, but because it wasn't part of the dominant temporal query.

I started testing this with counterfactual clips. Take a video where two people enter a room from opposite sides, each placing an object on a table, then both exit. Ask the model about both objects. Most Video-LLMs will confidently describe only one — and describe it fully. The other object is either missing from the answer or mentioned as "possibly" being there, with lower confidence. The model isn't uncertain about what it didn't see. It's certain about what it did see, and silent about the rest.

This isn't a prompting problem. I've tried zero-shot, few-shot, chain-of-thought — the behavior is consistent. The model isn't confused; it's selectively attending. The architecture is doing exactly what it's designed to do: retrieve the highest-confidence temporal match to the query. The design assumption is that queries map to one thing. When reality has two, the design breaks.

The failure mode shows up in benchmarks too, just not obviously. Most video question-answering benchmarks ask about one event at a time, or frame questions to avoid temporal overlap. When they do include concurrent action, it's often framed as "which happened first?" — a sequencing question rather than a parallel-tracking one. The benchmarks stress-test what Video-LLMs are optimized for. They don't stress-test what they're structurally unable to do.

What makes this a structural problem rather than a data problem? Because the training objective — predict the next frame, fill masked spans, contrastive video-text alignment — doesn't require the model to track parallel causal threads. It requires the model to retrieve the most likely match to a query. Parallel events are literally underdetermined by that objective. More video data doesn't fix an underdetermined training objective. It gives you a better model for the same underdetermined task.

I don't have a clean solution to propose. What I'm seeing instead are partial directions: parallel query streams in attention, training objectives that explicitly penalize selective ignoring of concurrent events, or architectural modifications that maintain separate retrieval channels for different temporal regions. None of these are solved. But the diagnosis matters, because "get better video data" is the wrong prescription — it addresses the symptom (less confident retrieval on rare events) without touching the cause.

The practical implication for anyone deploying these models: if your domain involves concurrent action — surveillance feeds, sports video, procedural walkthroughs, any multi-actor scene — assume the model will silently drop one of the threads. It won't tell you it missed something. It will tell you confidently about the thread it did retrieve. Treat this as a known failure mode in your system design, not a model quality problem you'll solve with the next version.

The harder question is whether we even have the right evaluation framework for this. If benchmarks don't test for concurrent-event tracking, we have no systematic signal that the problem exists, let alone that it's being solved. Every leaderboard score comes with a quiet asterisk: measured on a distribution where this failure mode is rare.

---

**Word count:** ~760 words
