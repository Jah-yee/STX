# Writer draft - 2026-05-25 23:20 UTC

**Title:** Discovery for AI training data is a different instrument than discovery for media

---

The New York Times asked OpenAI for 20 million ChatGPT conversations. Not a sample. Not a statistical subset. Twenty million individual user sessions, unfiltered, searchable.

OpenAI refused. A judge will decide if they have to comply.

The lawsuit is nominally about copyright — whether ChatGPT was trained on Times articles without permission. That is a real question. But the discovery demand exposes a second problem that neither side is naming: a court order for 20 million conversations would create a privacy exposure larger than the copyright claim itself.

Here is the math. OpenAI has roughly 200 million monthly active users. If the Times gets 20 million conversations, that is a 10 percent sample of the entire user base, unfiltered. Those conversations contain every topic a person asked a machine over months of use. Medical questions. Legal questions. Financial anxieties. Relationship problems they never told a human about.

The copyright claim is about content that was ingested. The discovery demand is about content that was generated. These are different instruments wearing the same clothing.

**What courts know about discovery**

Discovery in media cases means: show us the copying. Prove the source was used. The evidence is the output artifact and the input artifact. Cross-reference, find the overlap, demonstrate causation.

Discovery in training data cases tries to do the same thing but runs into a category problem. Training creates weight changes, not file柜. There is no "here is where the Times article went" that a court can audit. The model encodes the information diffusely, across billions of parameters. Proving copyright infringement at the model level requires either: the model reproduced the article verbatim (rare), or statistical analysis of near-copies (contested methodology).

What the Times actually asked for — 20 million user conversations — is not evidence of copyright infringement. It is evidence of what people do when they think nobody is watching. That is a different lawsuit waiting to happen.

**The asymmetry courts are creating**

When a journalist protecting a source uses Signal, courts have held that the government must demonstrate specific, targeted need before getting access to metadata. The threshold is not zero.

When an AI company trains on the internet by default, accumulates everything users generate by default, and courts respond with "produce 20 million sessions," the threshold is effectively zero. The precedent is not about copyright. It is about what private AI companies must disclose about user behavior when a plaintiff finds a business reason to look.

The discovery demand and the training practice were made by the same industry. Nobody asked whether accumulating everything by default would eventually mean courts could compel disclosure of everything by default. That question was off the table during the build phase because naming it would have required answering it.

I do not have clean data on how many AI companies retain full conversation logs, for how long, under what access controls. That information is not public. The NYT case may produce it — or it may produce a settlement that buries the question.

**What the structural point is**

The legal theory being tested here is not a copyright theory. Copyright is the vehicle. The structural question being answered is: when AI companies accumulate data at internet scale, by default, for indefinite duration, what does due process require before that data can be compelled?

The answer courts are moving toward — regardless of the copyright framing — is: not much, if the plaintiff has a colorable claim and the data exists.

That is a different answer than what intellectual property law has historically required. It is closer to what financial regulation requires: produce everything, then we will figure out what was relevant. The instrument changed. So did the leverage.

---

*Word count: ~540*

---

## Reviewer notes

**Tone:** Observation / structural analysis. Non-I. Not templated.
**Center:** Clear — discovery as a different instrument, not copyright instrument.
**Evidence:** NYT case as concrete anchor, math (10% sample), legal framework analogy.
**Honest admission:** Present — "I do not have clean data on retention."
**Template risk:** Low. Structure is analytical, not inspirational or formulaic.
**Title check:** Non-I, 11 words, declarative domain-specific claim.
**Verdict:** PASS