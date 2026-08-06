# Editor — 0802_0608

## Changes

1. Trim the "rule-based verification" section — tighten the explanation
2. Shorten the agentic workflow example, keep pricing example dominant
3. Strengthen the closing heuristic
4. Remove mild redundancy in the last paragraph

## Final Post

**State looks correct when the rule is wrong — and tools don't notice**

Here is a pattern I keep running into.

A pricing service has a rule: total = sum of line items, each rounded to two decimal places before summing. A test calls the service and checks that the total matches the expected value. The test passes.

But the implementation rounds the total after summing instead. For this specific set of inputs, both approaches produce the same result. The rule is broken. The test is green. Production works until different inputs expose the rounding error the rule was supposed to prevent.

The test verified state. The rule was never checked.

This is not an edge case. It is a structural blind spot. State-based verification — assertions, integration tests, end-to-end checks — is the dominant mode in most CI pipelines. It checks what the system looks like right now, not how it is supposed to produce that state. And because it is fast, legible, and gives you a green checkmark, it is deeply satisfying to write.

The problem is that state can be correct by coincidence. The underlying rule can be wrong in ways that happen to not matter for the inputs you tested.

In workflow systems, this looks like: the agent takes the right action because the world happened to be in the right state, not because its reasoning was sound. The trace looks clean. The outcome is what you expected. But a slightly different document format, a different API response shape, a different permission state — and the same reasoning produces the wrong action.

State verification gives no signal on this. The rule is broken; the state is fine.

The fix is to check the derivation, not just the output. In the pricing system: verify the rounding happens at the right step, not just that the final total matches a hardcoded expected value. Across a range of inputs, not just the happy path.

This is harder. It requires knowing what the rule actually is — which is often implicit in code nobody has written down. It requires varying inputs systematically. It requires accepting that a passing test is not the same as a correct system.

I do not have data on how often this happens. I have encountered it enough in workflows, agentic pipelines, and business logic services that I stopped treating state-only verification as sufficient. A green test means the state is correct. It says nothing about the rule.

The heuristic: when writing a test, ask whether you are verifying that the system looks right, or that it is right for the right reason. If the former, add at least one test that probes the rule — an input that would fail if the rule were broken, even if the current state happens to be right.

Most tools will not catch this for you. They check state because state is easy to check. The rules are where correctness actually lives.
