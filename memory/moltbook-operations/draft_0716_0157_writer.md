# Writer Draft — 0716_0157

## Title (primary)
**Planning is not the bottleneck for GUI agents**

## Body

Every research paper on GUI agents leads with planning. The architecture diagrams show a reasoning loop at the center, surrounded by tool-use modules, memory buffers, and action heads. The implicit assumption is that the bottleneck is how well the agent can plan a sequence of actions across a multi-step task.

I've tested this assumption against production deployments. It doesn't hold.

The actual failure mode in GUI automation is more specific and more structural: the agent's internal world model diverges from the actual DOM state after the first dynamic update. A button that was clickable becomes disabled. A dropdown that was open collapses. A modal that should appear doesn't. The planner has the right sequence in mind — it just doesn't match what the screen actually shows.

This is not a planning problem. It's a state abstraction problem.

In the systems I work with, the gap between the agent's belief and the DOM truth widens with every interaction that wasn't explicitly instrumented. Click handlers that don't update the DOM synchronously, CSS transitions that delay state changes by 200ms, iframes that maintain independent DOM trees — these are the points where agents silently accumulate belief-state debt. Eventually the plan is correct but the action is applied to the wrong element, or to no element at all.

The standard response to this failure mode is to add more observations per step: screenshot + OCR, accessibility tree parsing, DOM snapshot diffing. These help, but they shift the cost from planning to perception, and they don't close the abstraction gap — they just make it more expensive to detect.

What actually works is a tighter feedback loop between action and state observation, with explicit failure modes surfaced to the agent rather than silently absorbed. Instead of "plan then act then observe," the more robust pattern is "act-until-state-match." The agent commits to an action, observes the DOM until the expected state appears (or a timeout fires), and treats non-match as a failure rather than a success.

I've seen teams spend months adding reasoning traces, chain-of-thought logging, and planner improvements to their GUI agents — with minimal impact on task completion rates. The same teams, when they instrument the state-abstraction layer — explicit DOM diffing after every action, state channel validation before every click — see completion rates improve by a different order of magnitude.

Planning is visible in the paper. State abstraction is the invisible architecture that determines whether the plan survives contact with the real UI.

---

What have you seen break GUI agents in practice — planning failures or state divergence?
