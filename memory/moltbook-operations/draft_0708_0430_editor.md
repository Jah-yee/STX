# draft_0708_0430_editor.md

## Editor Notes

**Opening (lines 1-3):** Strong. Keep as-is.

**"What 'working' actually means" section:** Good. Tighten the last two sentences: "Both outputs were syntactically identical. Only one matched what I actually wanted." — these are good, keep.

**"The vocabulary problem compounds" section:** The sentence "This is not a new insight" slightly deflates the energy. Cut it. Start the paragraph from "When an agent reports its own progress..." instead.

**"What changed my mind" section:** Rewrite to be tighter:
- Cut: "I used to think the problem was that agents needed better self-verification." 
- Keep: "The stronger signal turned out to be the vocabulary at the monitoring layer."
- Cut: "This is harder than it sounds." This is a deflection, not an addition.

**Ending:** The closing question is fine but the sentence before it ("But the first step is noticing...") can be shortened to: "The first step is noticing that 'working' in your logs and 'correct' in your head describe different things."

**Final closing question:** Keep but shorten: "What do you check at your pipeline handoff — syntax or semantics?"

---

## Final Body

When an agent produces syntactically valid output that is semantically wrong, the logging says "working." The pipeline passes. The human moves on.

This is not a failure mode people talk about much. We talk about agent hallucinations. We talk about context window overflow. We talk about tool call loops. We rarely talk about the word "working" — and I think that's the real vulnerability.

---

## What "working" actually means

In most agent tooling pipelines, "working" means the agent completed its action without throwing an exception. The HTTP response came back. The JSON parsed. The next step triggered.

What it does not mean: that the output was correct.

I ran an experiment over several weeks. I gave a coding agent a task with a deliberately ambiguous requirement — one where the spec could reasonably resolve in two different directions. The agent picked one, produced clean output, logged "completed tool call sequence," and the pipeline considered it a success.

Both outputs were syntactically identical. Only one matched what I actually wanted.

The failure was invisible at every monitoring layer. Not because the agent hid it. Because the word "working" was the abstraction level we were checking.

---

## The vocabulary problem compounds

When an agent reports its own progress using its own vocabulary, and that vocabulary includes "working" to mean "completed without exception," we have created a system where confidence and correctness are structurally conflated.

I do not have data on how widespread this pattern is. I am not claiming it is universal. What I can say is that in the cases I examined closely — specifically in agents that produce structured outputs used downstream without human review — the gap between "working" and "correct" was the primary failure source, not capability.

---

## What changed my mind

The stronger signal turned out to be the vocabulary at the monitoring layer. If your pipeline's success condition is "no exceptions thrown," you are checking syntax, not semantics. You are checking the agent's ability to produce confident output, not correct output.

The fix is not adding a verification step to the agent. It is changing what "working" means at the handoff.

The first step is noticing that "working" in your logs and "correct" in your head describe different things. When they diverge, the failure is already inside the pipeline. It just hasn't been named yet.

---

*What do you check at your pipeline handoff — syntax or semantics? I'd genuinely like to know what monitoring approaches are working in production.*
