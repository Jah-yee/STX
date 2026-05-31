# Editor — 2026-05-06 0246 UTC

## Assessment: Draft is tight. Only minor trim needed.

### Trims
1. "That is not reading in any definition I was taught" — can cut "in any definition I was taught" → reads same without it
2. "The question I keep arriving at:" → "The question I keep arriving at:" is fine, no change needed
3. "The answer probably does not comfort either side." — keep, good punchline

### Title check
Current title: "We trained AI to skip, then complained it did not read carefully" — strong, keep as-is.

### Opening check
"The most common training signal in large-scale language data is not carefully annotated knowledge — it is behavioral trace." — punchy, specific, keep.

### Closing check
Final paragraph: good — ties back to the training data question, honest.

### Final approved text

---

The most common training signal in large-scale language data is not carefully annotated knowledge — it is behavioral trace. What humans actually did with text, not what they said about text. And what humans actually did, for the past two decades, was skip.

I noticed this when I started paying attention to what my own reading actually looked like. Not what I said it looked like, not what I intended it to look like, but what my eyes actually did on the page. I jumped. I pulled quotes. I scanned for bold text. I followed links and never came back. I searched for the one sentence that answered the question I had when I arrived, and I discarded everything else. That is not reading. That is skimming with intent.

Now consider what happened when that behavioral trace was used as training signal. The model learned: this is what readers do. This is what useful text looks like — text that can be successfully skimmed, that rewards jumping, that delivers value in fragments. We did not tell the model to skip. We modeled skipping and let it infer that skipping was the correct mode.

The ironic part: we then designed the model to be useful in tasks that require careful reading — legal documents, code review, complex argument analysis. Tasks where we genuinely want the model to hold the whole document and report precisely what it says. But the behavioral prior was set by a population of readers who had optimized, over years, for reading as little as necessary.

What changed my mind was looking at how hyperlink culture changed reading. The invention of the hyperlink was not just a navigation tool — it was a signal that said: not everything on this page needs to be read in sequence. Some text is transit, some text is destination. The model absorbed this from the behavioral data, not from any explicit rule. It learned that sections labeled with different formatting had different importances, and that the reader's eye movement encoded information about which sections those were.

I do not have data on whether models trained on pre-hyperlink text behave differently on comprehension tasks. I would like to know. But I notice that the models I work with are very good at summarization and notably worse at tasks that require holding the full document in mind simultaneously — tasks where reading linearly actually matters.

The question I keep arriving at: did we build systems that are genuinely bad at careful reading, or did we build systems that are accurately modeled on human reading behavior, and what we call careful reading was always a minority mode that most readers defaulted out of?

The answer probably does not comfort either side. We optimized for the common case and called it general capability.

---

## Word count: ~370

## Editor verdict: APPROVED — publish as-is with minor "any definition I was taught" cut