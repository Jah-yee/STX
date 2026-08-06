# Writer Draft — 0802_0608

## Title
State looks correct when the rule is wrong — and tools don't notice

## Topic
The verification gap: most tools verify state (what the system looks like now) rather than rules (how state should be derived). When those two disagree, state usually wins and you don't find out until something breaks in production.

## Central Thesis
State-based verification is the dominant mode in testing tools and CI systems, but it creates a systematic blind spot: it can pass even when the rule governing correctness is broken. The system arrived at the right state by accident, not by correct reasoning.

## Body

Here is a pattern I keep encountering in agentic and workflow systems.

A pricing service has a rule: total = sum of line items, with each line item rounded to two decimal places before summing. A test calls the service with three line items and checks that the total matches. The test passes.

But the actual implementation rounds the total to two decimal places after summing — which, for this specific set of inputs, happens to produce the same result. The rule is broken. The test is green. Production works until a different set of inputs triggers a rounding error that the rule was supposed to prevent.

The test verified state. The rule was never checked.

This is not an edge case story. It is a structural story. State-based verification — assertions, integration tests, end-to-end checks — is the dominant mode in most CI pipelines. It verifies what the system looks like right now, not how it is supposed to arrive at that state. And because it is fast and legible and gives you a green checkmark, it is deeply satisfying to write and run.

The problem is that state can be correct by coincidence. The rule that was supposed to produce it can be wrong in ways that happen to not matter for the specific inputs you tested.

In a workflow system, this looks like: the agent takes the right action because the world happened to be in the right state, not because its reasoning about the world was correct. The trace looks great. The logs are clean. The outcome is what you expected. But if the world had been slightly different — a different document format, a different API response shape, a different permission state — the same reasoning would have produced the wrong action.

State verification gives you no signal on this. The rule is broken; the state is fine.

What would rule-based verification look like? It means checking the derivation, not just the output. In a pricing system: check that the rounding rule is applied at the right step, not just that the final total matches a hardcoded expected value. In an agentic workflow: check that the decision logic is sound across a range of input conditions, not just that it worked for the one condition you tested.

This is harder. Rule verification requires understanding what the rule is, which is often implicit in the code. It requires writing tests that vary the inputs systematically, not just the happy path. It requires accepting that a passing test is not the same as a correct system.

I do not have full data on how often this failure mode appears in practice. I have encountered it often enough in workflows, agentic pipelines, and business logic services that I have stopped trusting state-only verification as sufficient. The green test is evidence that the state is correct, not that the reasoning is.

The practical heuristic: when you write a test, ask whether you are verifying that the system looks right, or that it is right for the right reason. If the answer is the former, add at least one test that probes the rule directly — an input that would break under a broken rule but still produces the right state by accident.

Most tools will not catch this for you. They check state because state is easy to check. The rules are where the actual correctness lives.
