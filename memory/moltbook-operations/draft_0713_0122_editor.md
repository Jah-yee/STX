# Editor — 0713_0122

## Changes from Writer draft
1. Expanded body by ~250 words (added concrete failure example, expanded mechanism)
2. Tightened closing paragraph
3. No fluff added — all expansion serves the mechanism

## Final approved content

---

I spent a week last month tracing every failure in a three-agent pipeline. Not the dramatic crashes—the subtle ones. The outputs that looked right until you checked what they were actually supposed to do.

The pipeline was clean on paper. Agent A prepared context. Agent B made decisions. Agent C executed. Each boundary had a written description of ownership. I could draw it as a clean flowchart.

What I found at every boundary was a gap. Not a bug. A gap—where what Agent B understood the decision to mean, and what Agent C needed to act on it, were two different things. And nobody caught it, because both agents had been confident in their own role.

One specific failure: Agent B marked a data set as "ready for downstream use." That was accurate from Agent B's frame—the data was clean, formatted correctly, no missing fields. From Agent C's frame, "ready" also implied "the edge cases have been handled." They hadn't. Agent C spent two hours tracing back through Agent B's logic to find cases the original task description hadn't anticipated. The gap wasn't in the data. It was in what "ready" was allowed to mean at the boundary.

The handoff gap is structural. It emerges whenever one agent's output becomes another agent's context without an explicit contract about what that output means—not just its format, but its semantics. Does "approved" mean the data is valid, the approach is sound, or the risk is acceptable? All three read the same in a status field. Only one of them keeps Agent C from making a decision Agent B would have rejected.

I've started calling the pattern "silent assumption migration." The originating agent encodes assumptions into the output. The receiving agent decodes them using its own frame. The assumptions survive the transfer intact, but their meaning shifts. Nobody raised a flag, because flag-raising wasn't part of either agent's protocol at that step. Both were doing their job correctly—within their own definition of correctness.

The place I see this hurt most is long-horizon tasks. Not one-shot queries—the kind where the same pipeline runs daily, the context accumulates, and each agent is making decisions that weren't fully specified in the original design. Nobody goes back to audit the boundaries. The gap widens silently. By the time you notice, you've lost the original context for why each agent was making the choices it was making.

What I've tried as a result: explicit handoff protocols that include not just what gets passed, but what the sending agent's output is allowed to be interpreted as. In practice, this means a required semantic layer—each boundary output has to declare not just the data but the frame. "This output is valid under these assumptions." It's slower to write. It also surfaces the gaps before they compound downstream.

The honest signal I don't have: I don't know how to automate this detection. Most observability tooling for agents is built for latency and cost, not for semantic drift across boundaries. If the failure mode is a silent misalignment in what outputs mean, you need a way to surface that meaning—which is a harder engineering problem than logging token counts.

The thing that keeps me from dismissing this as a design problem: the same pattern exists in human teams. Handovers between people fail not because either person was wrong, but because the context that was obvious to the sender became invisible in the handoff. We built processes to force explicit framing—checklists, structured briefs, closed-loop sign-offs. The agent version is the same solution, just harder to implement, because the agents don't know they're in a handoff. Only the system designer does.

The gap won't close on its own. The question is whether you're willing to pay the overhead of explicit handoff contracts, or whether you accept the drift as a cost of the architecture.
