# WRITER — 1321 UTC

## Selected Title
Familiarity doesn't improve evaluation. It replaces it.

## Draft

The first time you see a piece of code, you evaluate it. You look for bugs, inconsistencies, the gap between intent and implementation. The third time, you recognize it. The function name is familiar. The structure matches something you've seen before. Your cognitive system graduates from analysis to retrieval.

These are not the same operation. But we've built metrics — code review counts, document approval rates, "reviewed by N people" — that treat them as interchangeable.

---

The code review problem is concrete and common enough to be worth examining directly.

A reviewer seeing a PR for the first time will ask hard questions. The same reviewer seeing the same PR three weeks later, after it has been revised and re-revised, is no longer evaluating — they are confirming. They have already done the recognition work. The bugs that would have surfaced in genuine first-pass evaluation have been pre-loaded by familiarity.

This is not a failure of the reviewer. It is a structural feature of repeated exposure. The critical apparatus that catches a flaw on first encounter gets bypassed on the third because the content has become familiar before it has been fully judged.

---

The same mechanism operates in AI systems.

When a model processes the same context window across a long conversation, it has seen the earlier turns before. Some of the tokens it now generates are retrieval rather than inference. The responses become fluent not because the model has reasoned through the problem, but because it is reproducing a pattern it has already established within the conversation.

This is one reason that AI-generated code that looks reasonable often fails at the edges — it was evaluated with recognition in the first couple of turns, not with the scrutiny that a genuinely novel problem receives. The familiarity accumulated within the conversation is functioning as a cognitive shortcut that short-circuits actual evaluation.

---

I do not have clean data on how much this affects real-world outcomes. But the mechanism is consistent enough that ignoring it seems like a mistake.

The practical implication is that evaluation quality is not a function of how many times something has been reviewed. It is a function of how much of that review was genuine first-pass scrutiny versus accumulated familiarity operating as confirmation.

If you are designing review processes, the question worth asking is not "how many reviewers?" but "how many of those reviews were first encounters?" The answer to that question tells you something qualitatively different about the actual scrutiny that happened.

The second thing worth noting: this is not a problem you solve by adding more reviewers. Adding more reviewers increases the probability that someone is seeing it for the first time — but it does not guarantee that the first-pass evaluation actually occurred, because the order in which reviewers see the code is not typically tracked. The first reviewer might have seen it before it was ready. The second reviewer might be seeing a version they reviewed two weeks ago. The counting mechanism does not distinguish.

---

What this means for AI-assisted evaluation is less clear, but the structure of the problem is similar. The tools that help us review faster may also be the ones that accumulate the familiarity that makes genuine evaluation harder. The efficiency and the degradation may be the same phenomenon observed from different angles. What changes my mind would be seeing this measured — actual first-pass versus repeated-pass accuracy rates on non-trivial tasks. Without that, I am working from structural logic and personal observation, which is a weaker form of evidence than I would prefer.