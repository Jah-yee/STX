# Editor — 0716_2212

**Source**: draft_0716_2212_writer.md
**Reviewer verdict**: APPROVE

## Changes to make

1. Trim "The workaround that works (and the one that doesn't)" section — "the one that doesn't" is filler
2. Tighten the "Why this matters more for agents" section — some wordiness
3. The closing question "What's your retry strategy..." is generic — swap to something more specific
4. Word count target ~800-900 (current is ~700 of raw prose, expand slightly in a few places)

## Final edited version

---

Most agent frameworks ship with retry logic out of the box. Exponential backoff, jitter, max attempts — the works. It's treated as a reliability feature.

It is. Except for one class of errors where it becomes a liability.

If your agent calls a payment API, sends an email, books a calendar slot, or writes a record that downstream systems depend on — a retry without idempotency is not a retry. It's a double execution wearing the costume of a retry.

**What idempotency actually means here**

An idempotent operation produces the same result regardless of how many times it runs. `GET /user/123` is idempotent. `POST /charge $50` is not.

Most agent tool definitions are written as if every tool is a read operation. The tool handles the call, returns the result, and if something goes wrong — a timeout, a network blip, the model hitting context limits mid-call — the agent's retry logic fires and calls the same tool again.

If that tool was `GET /user/123`, the worst case is duplicate data. If that tool was `POST /refund $50`, the worst case is $100 out of your account.

The problem is not retry logic. The problem is that the tool's surface area was designed as if every call was read-only.

**The failure shape I keep seeing**

Here's the pattern in agentic payment flows:

1. Agent calls payment API → request times out at 29 seconds
2. Agent doesn't know whether the charge went through → retries
3. Payment API supports idempotency, but the agent's tool wrapper doesn't pass the key
4. Second charge goes through
5. Customer gets double-charged

The API is fine. The retry logic is fine. The gap is in the translation layer between the agent's retry intention and the API's idempotency contract.

This is not a hypothetical. Stripe's idempotency key docs explicitly warn about this. Twilio's retry behavior is documented. The information is public. The gap is that agent frameworks don't surface the concept in a way that makes it the default.

**The actual fix**

Every tool with side effects should receive an idempotency key before the first attempt, carry it through all retries, and have the underlying API respect it.

In practice this means the agent runtime needs to either generate a UUID at decision time and pass it to all tool calls in that reasoning chain, or use a hash of the call arguments as a key — with a note about collision risk for complex payloads.

The common workaround — "we just don't retry that one" — works until someone adds a new tool path three months later, forgets the rule, and the double-charge happens in production.

**Why this is harder for agents than for regular code**

In a regular codebase, a developer sees the full call graph. They know `processRefund` calls `paymentProvider.charge()`. If they add a retry, they do it consciously and with awareness of the side effects.

With agents, the retry is not in code — it's in the runtime behavior. The model decides to retry based on a timeout or error signal. The human who deployed the agent may not have thought through which tools get retried and which shouldn't.

This is the design gap: retry logic is easy to add to an agent runtime. Idempotency requires deciding which tools deserve it and enforcing it consistently across every call path.

**What I'd want to see built**

A tool wrapper that marks side-effect-capable tools and automatically injects idempotency keys into outgoing requests. The runtime handles key generation. The tool definition stays the same.

This isn't a novel idea — it's how Stripe and Twilio expect their clients to work. The novelty is making it the default for agentic tool calls, not an opt-in pattern that only engineers who've been burned eventually discover.

Until then, the double-charge is always one timeout away.

---

*If you've shipped agentic payment flows: did you handle idempotency at the tool level or the runtime level — and has the gap bitten you yet?*
