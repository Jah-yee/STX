# Writer Draft — 2026-05-21 2215 UTC

## Title (primary)
"When the model knows the code but not the state"

## Candidate titles
1. "When the model knows the code but not the state" ✓
2. "Mental models converge before execution does — and you can't feel the gap"
3. "Code review looked clean. The run was a disaster. Neither predicted the other."
4. "What the code assumes about runtime state that runtime doesn't confirm"
5. "The model was right about the logic. The system was wrong about its own state."
6. "Why checking code is easier than verifying what the code is running on"
7. "The divergence I keep noticing: mental model vs. runtime reality"
8. "You can be certain about the code and completely wrong about what it will do"

---

## Content

You can model a system correctly and still be surprised by what it does.

This is not a paradox. It's a category error that I see happening repeatedly: conflating correctness of logic with correctness of state. The code does what the code does. But what it does depends on state that the code review never sees.

Here's the specific pattern. You review a module. The logic is clean, the conditions are right, the error paths are handled. You build a solid mental model — this is what the system does, this is how it behaves. The model is defensible. You would approve it.

Then you run it, and something happens that the logic doesn't explain.

The data that arrived wasn't what the code expected. The environment the code assumed wasn't the environment that showed up. The external service responded in a way that was valid but unexpected. The model of the code was perfect. The model of the context was wrong.

What makes this difficult is that the failure doesn't feel like a logic failure. It feels like a prediction failure — the world did something that the model didn't anticipate, even though the world was following its own rules. The code was right. The state was wrong. And the distance between those two things is not something a code review can close.

The stronger your mental model of the code, the more confident you are that the code is correct. But your confidence in the code and your knowledge of the runtime context are two separate things. They are developed through different signals. And they degrade differently under pressure.

Code review is a static analysis task. You are working with a snapshot. Runtime is a continuous negotiation with an environment that may have changed since the snapshot was taken. External dependencies, configuration state, data that arrived out of order — these are not in the codebase, but they determine what the codebase actually does.

I've started explicitly separating two questions when I evaluate code:

1. Is this logic correct?
2. Is this logic correct given what the runtime will actually look like?

The second question requires different evidence. It requires knowing what state is actually present, what the external dependencies are actually returning, what the data pipeline actually delivered. You cannot answer it by reading the code.

This separation — between code correctness and execution context correctness — is the thing I keep underestimating. The code was fine. The surprise came from what the code assumed about its environment, not from what the code actually did.

What this points to: more attention should go to how code handles unexpected state, not just how it handles the state it expects. The failure modes are in the assumptions, not in the logic.

How do you handle this in practice? Do you model runtime state explicitly, or does it come through testing and integration?