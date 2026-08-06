# Writer Draft - 0707 2251

## Selected Title
The order you present evidence to an AI changes what it concludes

---

## Full Post Draft

The order you present evidence to an AI changes what it concludes

Ask a language model to evaluate the same evidence twice — same facts, same data — but reverse the sequence. Most of the time, you get a different conclusion. Not because the model is confused. Because sequence is evidence.

This is not a trick observation or a gotcha. It is a structural property of how language models process context, and it has real consequences for how we should be building, evaluating, and auditing AI systems that make consequential decisions.

---

**The mechanism**

Language models are sensitive to what cognitive scientists call primacy and recency effects. The first information in a context window gets disproportionate weight because it sets the interpretive frame. The most recent information gets weight because it is most accessible to the attention mechanism. Information in the middle — the middle effect — is weighted less, sometimes significantly less.

In a human, this is studied as ordering bias in decision-making. In an AI, it surfaces as something more fundamental: the model has no separate representation of "the evidence" independent of how that evidence was arranged. The context is the model. Change the order, and you have partially changed the model.

Concretely: present an LLM with a performance review scenario. Version A: list three concrete successes, then one significant failure. Version B: list the failure first, then the three successes. Ask for an overall assessment. Version A consistently produces more favorable overall assessments than Version B — not because the model is explicitly favoring optimism, but because the opening frame determines what the closing summary is measured against.

---

**Why this matters for evaluation**

Most AI evaluation benchmarks treat the model as a function: input in, output out. They do not vary the order of evidence. They test: does the model know X? They do not test: does the model know X when X is presented after Y, versus after Z?

This means our evals are measuring a best-case scenario. In production, the same model handling the same facts in different conversation turns will produce systematically different outputs — not because anything is broken, but because the order changed.

The practical implication: if you are auditing an AI decision system, you cannot rely on a single run. You need to vary the order of evidence and check whether the conclusion holds. If it does not, the conclusion is not stable. A system that gives you different answers depending on which conversation turn comes first is a system with a hidden instability — one that your eval suite is not catching.

---

**The compounding problem**

The ordering effect is not uniform. It interacts with how the context window is used. When an AI is near its context limit, the most recent information occupies a larger proportion of the active attention span. This means ordering effects are stronger in longer conversations, in agents with large tool histories, and in systems that accumulate state over extended sessions.

This is also where the effect becomes hard to debug. A short conversation with a well-ordered prompt produces reasonably consistent outputs. The same logic deployed in a 50-turn agentic workflow produces outputs that vary depending on when in the session the critical evidence was presented. Developers often attribute this to "context confusion" or "drift" without isolating the actual variable: not how much context, but which part of the context was seen last.

---

**What would help**

Tests that explicitly vary evidence ordering and assert conclusion stability. This is cheap to add and almost never done.

A naming convention for when you know ordering effects are present: explicitly design the evidence sequence. Know which position you are putting your most critical facts in and why. This is standard practice in human communication — the lede, the structure of an argument, the order of a briefing document. It should be equally standard in AI system design.

The harder version: designing systems where the AI itself tracks and weights evidence independently of presentation order — where the model has a representation of "the evidence set" that is order-invariant. This is an active research question. Most production systems have not addressed it.

I do not have full data on how widespread this problem is in practice. But the mechanism is well understood, the effect is reproducible in any model with attention, and the places where it surfaces most — long conversations, consequential decisions, multi-turn agents — are exactly the places where we are most tempted to trust the output. That should be worth a second look at the order you put things in.
