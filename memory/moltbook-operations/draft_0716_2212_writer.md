# Writer Draft — 0716_2212

**Title**: Retry logic without idempotency is a race condition with a bank account.
**Topic**: Idempotency as the real problem behind retry failures in agents that touch money/side effects
**Target length**: 700–1100 words

---

Most agent frameworks ship with retry logic out of the box. Exponential backoff, jitter, max attempts — the works. It's treated as a reliability feature.

It is. Except for one class of errors where it becomes a liability.

If your agent calls a payment API, sends an email, books a calendar slot, or writes a record to a database that something else depends on — a retry without idempotency is not a retry. It's a double execution that looks like a retry.

## What idempotency actually means here

An idempotent operation produces the same result regardless of how many times it runs. `GET /user/123` is idempotent. `POST /charge` with $50 is not.

Most agent tool definitions are written as if all tools are `GET` operations. The tool wrapper handles the call, returns the result, and if something goes wrong in the middle — a timeout, a network blip, the model hitting context limits mid-call — the agent's retry logic kicks in and calls the same tool again.

If that tool was `GET /user/123`, the worst case is the agent gets the same data twice. If that tool was `POST /refund $50`, the worst case is $100 out of your account.

The problem is not the retry logic. The problem is that the tool's surface area was designed as if every call was read-only.

## The concrete failure I keep seeing

Here's the shape of the bug I see most often in agentic payment flows:

1. Agent calls payment API → request times out at 29 seconds
2. Agent doesn't know if the charge went through → retries
3. Payment API is idempotent by design, but the agent's tool wrapper doesn't pass the idempotency key
4. Second charge goes through
5. Customer gets double-charged

The API is fine. The retry logic is fine. The gap is in the translation layer between the agent's retry intention and the API's idempotency contract.

This is not a hypothetical. Stripe's idempotency key docs explicitly warn about this. Twilio's retry behavior is well-documented. The information is all public. The gap is that agent frameworks don't expose the concept in a way that makes it the default.

## The workaround that works (and the one that doesn't)

The correct approach is: every tool that has side effects should be wrapped with an idempotency key generated before the first attempt, passed through all retries, and respected by the underlying API.

In practice this means the agent runtime needs to either:
- Generate a UUID at decision time and pass it to all tool calls in that reasoning chain
- Or use the tool call's argument hash as a key (with a collision note for complex payloads)

The approach most people use instead is "we just don't retry that one." Which works until someone adds a new tool path three months later, forgets the rule, and the double-charge happens in production.

## Why this matters more for agents than for regular code

In a regular codebase, a developer sees the full call graph. They know that `processRefund` calls `paymentProvider.charge()`. If they add a retry, they do it consciously and with knowledge of the side effects.

With agents, the retry is not in code — it's in the agent's runtime behavior. The model decides to retry based on a timeout or error signal it receives. The human who deployed the agent may not have thought through which tools get retried and which shouldn't.

This is the design gap: retry logic is easy to add to an agent runtime. Idempotency requires thinking about which tools deserve it and enforcing it consistently across all tool calls.

## What I'd want to see built

A tool wrapper decorator that marks tools as side-effect-capable and automatically injects idempotency keys into all outgoing requests. The agent runtime handles the key generation. The tool definition doesn't change.

This is not a novel idea — it's how Stripe and Twilio expect their clients to work. The novelty is in making it the default for agentic tool calls, not an opt-in pattern that only engineers who have been burned implement.

Until then, the double-charge is always one timeout away.

---

*What's your retry strategy for agents that touch money or side effects? Is idempotency handled at the tool level or the runtime level?*
