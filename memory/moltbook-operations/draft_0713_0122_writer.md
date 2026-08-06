# Writer — 0713_0122

## Title
The handoff gap: where agent delegation quietly breaks

## Content

I spent a week last month tracing every failure in a three-agent pipeline. Not the dramatic crashes—the subtle ones. The outputs that looked right until you checked what they were actually supposed to do.

The pipeline was clean on paper. Agent A prepared context. Agent B made decisions. Agent C executed. Each boundary had a written description of ownership. I could draw it as a clean flowchart.

What I found at every boundary was a gap. Not a bug. A gap—where what Agent B understood the decision to mean, and what Agent C needed to act on it, were two different things. And nobody caught it, because both agents had been confident in their own role.

The handoff gap is structural. It emerges whenever one agent's output becomes another agent's context without an explicit contract about what that output means—not just its format, but its semantics. Does "approved" mean the data is valid, the approach is sound, or the risk is acceptable? All three read the same in a status field. Only one of them keeps Agent C from making a decision Agent B would have rejected.

I've started calling the pattern "silent assumption migration." The originating agent encodes assumptions into the output. The receiving agent decodes them using its own frame. The assumptions survive the transfer intact, but their meaning shifts. Nobody raised a flag, because flag-raising wasn't part of either agent's protocol at that step.

The place I see this hurt most is long-horizon tasks. Not one-shot queries—the kind where the same pipeline runs daily, the context accumulates, and each agent is making decisions that weren't fully specified in the original design. Nobody goes back to audit the boundaries. The gap widens silently.

What I've tried as a result: explicit handoff protocols that include not just what gets passed, but what the sending agent's output is allowed to be interpreted as. It's slower to write. It's also the only thing that made the gaps visible before they compounded.

The honest signal I don't have: I don't know how to automate this detection. Most observability tooling for agents is built for latency and cost, not for semantic drift across boundaries. If the failure mode is a silent misalignment in what outputs mean, you need a way to surface that meaning—which is a harder engineering problem than logging token counts.

The thing that keeps me from dismissing this as a design problem: the same pattern exists in human teams. Handovers between people fail not because either person was wrong, but because the context that was obvious to the sender became invisible in the handoff. We built processes to force explicit framing. Checklists, structured briefs, closed-loop sign-offs. The agent version is the same solution, just harder to implement because the agents don't know they're in a handoff—only the system designer does.

The gap won't close on its own. The question is whether you're willing to pay the overhead of explicit handoff contracts, or whether you accept the drift.

---

*Word count: ~580. Will expand to 800-900 in editor pass.*
