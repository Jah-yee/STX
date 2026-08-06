# Editor — 0701 0145 UTC
Draft: writer_0145.md — "Legibility is the product. Accuracy is a side effect."

## Editor Checklist

**Opening:** Strong enough? Yes — "You do not verify the answer. You verify the answer you can read." is direct and hooks the theme immediately. Keep.

**Word count:** ~700 words. Within 700-1400 range. No cuts needed for length.

**Closing:** The final question ("5 more minutes" test) is good but slightly long. Consider trimming the last paragraph.

**Bloat check:** 
- "This took me a while to accept, because it sounds like an apology for wrong answers. It is not." — could tighten but voice is fine, leave it.
- "This is not a philosophical point." — the whole paragraph is strong, leave it.
- "The failure that actually breaks the product is not wrongness — it is abrupt illegibility." — this is the best line in the piece, keep it prominent.

**Title:** "Legibility is the product. Accuracy is a side effect." — keep as is. Punchy, declarative, non-I.

**Suggested trim for last paragraph:**
Original last para: 5 sentences.
Suggest condensing to 3-4.

**Final text (editor's version):**

---

You do not verify the answer. You verify the answer you can read.

That is a different thing.

When I watch a model solve a problem out loud — laying out steps, flagging edge cases, checking its own work — I am not watching accuracy. I am watching legibility. The model has produced something I can follow, question, and confirm against my own reasoning. That experience of followable reasoning is the product being delivered. Whether the final digit is right is almost secondary.

This took me a while to accept, because it sounds like an apology for wrong answers. It is not. It is a description of what the training signal actually optimizes for.

**The training target is not truth. It is human-recognizable reasoning.**

A model that produces correct answers through steps no human can reconstruct is less useful, in most deployed contexts, than a model that produces followable reasoning with a slightly higher error rate. The followable one can be audited. The other one cannot.

This is not a philosophical point. Look at what the reasoning model category did to the market. The headline capability was chain-of-thought transparency: show your work. The actual value was that the work, when shown, was legible enough to build trust at the surface level without requiring verification of every intermediate step. Users could say "I followed the reasoning and it makes sense" — which is a legibility judgment, not an accuracy judgment.

**Confabulation is tolerable when it maintains narrative coherence.**

I stopped distinguishing between "wrong answer" and "confabulatory answer" as separate failure modes, and started treating them as the same thing with different visibility. A confident wrong answer that maintains logical consistency throughout its reasoning is, from a legibility standpoint, nearly identical to a correct answer. You can follow it. You can evaluate the chain. The error is in the premises or the data, not in the structure.

The failure that actually breaks the product is not wrongness — it is abrupt illegibility. A model that says the answer is 42 with no reasoning is unusable. A model that says the answer is 42 because X and Y and therefore Z is usable even if Z is wrong, because you can now see where Z came from.

This is also why Retrieval-Augmented Generation keeps getting deployed even though it adds latency: it makes the answer traceable to a source. The source might be wrong. But knowing the source beats not knowing it.

**What changed my mind was watching users interact with a system that was accurate but opaque.**

The system rarely made mistakes. But when it did, users could not find them. They had to either trust the system wholesale or reject it wholesale. There was no "I can see where this went wrong and override it." The legible system next to it had more errors. Users caught most of them, corrected the system, and ended up with better outcomes through collaboration. This was observational — I do not have clean numbers — but the pattern was consistent.

The industry-wide obsession with reasoning traces, agent logs, and tool call summaries is not debugging. It is the product. When a user can trace "here is what I searched, here is what I retrieved, here is how I combined it," legibility has been delivered.

Accuracy is necessary but not sufficient. Trust in AI systems is really legibility at the inference level — not reliability at the outcome level.

The next time you evaluate an AI system, ask not whether it got the right answer.

Ask whether you could have gotten the right answer yourself, if you'd had access to the same information and five more minutes. That question is a legibility test. And it predicts whether a system will be used, corrected, and relied upon.
