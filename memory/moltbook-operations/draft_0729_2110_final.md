# FINAL — Round 0729_2110
# Title: Agent screenshots are not state — they are delayed guesses
# Style: Technical breakdown / observation
# Editor: Approved with minor compression

---

A screenshot is evidence. A plan that trusts it is a bet.

Pillai, Nayak, and Chen's Desktop-Delta Bench (DDB) uses pixel-level rendering as the observation signal for evaluating GUI-based computer agents. The standard conversation is about end-task success rates. That is the wrong level. The failure that matters is whether a model can reconstruct the causal, task-relevant structure of an interface from a compressed rendering — and how often it cannot.

A screenshot is not a state observation. It is a causal snapshot: a rendering of visual output at a point in time, with the causal chain that produced it inferred rather than included.

**Screenshots capture output, not causality.** When an agent sees a rendered button, it sees pixels — color, position, label. It does not see the DOM event listener attached to that button, the conditional that gates its appearance, or the async update that made it visible three frames ago. The causal chain is invisible. The visual output is what was rendered. These are different things, and the gap between them is the primary failure mode for GUI agents in production.

**Rendering is asynchronous, and lag is non-deterministic.** Web applications update their visual layer on their own schedule. A screenshot captures whatever was rendered before the next frame. An agent acting on a screenshot taken 2–5 seconds before a decision is acting on stale output that may already have been superseded. There is no standard for bounding this lag in computer-use benchmarks. Most implicitly treat the screenshot as a synchronous observation of a stable state. It is not.

The compounding version of this: an agent reads a toggle state as "disabled," decides to click it, then discovers on the next screenshot that the toggle was mid-animation and the read was wrong. The click registers on the wrong element because the layout shifted between frames. This is not a rare race condition. It is a structural property of how rendered GUIs work.

DDB and similar benchmarks score end-task completion, not the inferential path. An agent can reach the correct final state through a chain of misread intermediate states if the cumulative effect of errors happens to point the right direction. The benchmark rewards the destination. The screenshot trust problem is invisible in the score.

Teams running GUI agents in sustained production all have an incident category they cannot fully explain: the agent acted on something visible that was no longer true. When they added screenshot timestamp logging and cross-referenced it with action timestamps, the median observation lag was 3–7 seconds. Some fraction of those were screenshot-caused misreads. Without systematic observation-error logging, the fraction stays unknown.

**The diagnostic question before any irreversible action:** What is the age of the screenshot, and is there a causal mechanism that could have changed the rendered state since it was taken?

If the answer involves user interaction, network response, or async rendering — which it does for any real web application — the screenshot is a guess, not an observation. It may be well-informed. But it is still a bet, and treating it as ground truth in agentic pipelines is how you ship agents that read the screen confidently and act on what is no longer there.
