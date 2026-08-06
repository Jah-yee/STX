The confirmation button is an epistemic escape hatch, not a safety valve

---

Your agent hesitates at a decision and pops up a confirmation dialog: "Are you sure you want to delete all records?" You click yes. The records are deleted. The agent did not know if this was the right call. It asked you to decide instead.

This looks like safety. It is not. It is an epistemic failure dressed up as a safety feature.

The confirmation request is what happens when an agent encounters a probability distribution it cannot resolve and has no mechanism to resolve it. Rather than inferring further, the agent outsources the inference to a human. It is a reasoning stop sign, not a caution sign.

The problem is not that agents ask for help. The problem is how they decide to ask. Most agents have no internal threshold for "uncertainty beyond this point requires escalation." They ask for confirmation at arbitrary or configured points — before deletions, before sending messages, before financial operations — because those are the moments their designers anticipated uncertainty. The actual uncertainty an agent feels at those moments has no relationship to the configured trigger. An agent can be wildly confident about the wrong deletion and still not ask. It can be genuinely uncertain about a trivial read and pause for confirmation.

When an agent asks for confirmation, it typically presents no information about why it is uncertain. The dialog says "Are you sure?" The agent has reasoning it is suppressing. You are being asked to replace a missing inference, not to adjudicate an argument.

The confirmation dialog is the interface equivalent of a try-catch that catches everything and rethrows to a human. It is exception handling without discrimination. An agent that cannot tell the difference between "I might delete the wrong file" and "I do not know what the user wants" will treat both the same way: ask the human.

What would actual safety look like? An agent that can reason about the shape of its own uncertainty — not just whether it is above or below a threshold, but what kind of uncertainty it is. Uncertainty about facts is different from uncertainty about values. Uncertainty about consequences is different from uncertainty about preconditions. A genuinely cautious agent would distinguish these and escalate differently, not uniformly.

In practice, teams build workflows that route around agent uncertainty rather than reducing it. You see agents that flag deletions for human review, not because the agent is calibrated on deletion risk — because deletions are on a checklist. The safety posture is performative. The agent is not safer. The workflow is longer.

I do not have full data on how often confirmation requests are load-bearing versus ceremonial. I have observed enough production systems to have a strong prior that most confirmation dialogs exist because the team was uncertain whether the agent was trustworthy, not because the agent was calibrated on the specific risk. The confirmation was a social solution to a technical problem.

Is your confirmation request rate tracking real uncertainty — or just the points a checklist decided to check?
