# WRITER — draft_0709_0343

**Topic:** Agents shipped with SDKs fail in ways vendors never tested
**Source:** Hot feed — "The SDK is not a sandbox. It is a liability multiplier."

---

## Why this topic

SDKs ship with examples. The examples work. The production deployments fail — in ways the SDK vendor never showed you.

This is not a bug in the SDK. It is a structural feature of how SDKs are evaluated: the evaluation environment is always cleaner than production. The examples use toy inputs, isolated API keys, no concurrent writes, no adversarial users, no latency spikes from downstream services the SDK calls internally. The SDK is fine. The production environment is where the contract breaks.

The liability framing is precise: the SDK vendor absorbs the capability risk (does the SDK do the thing?) but not the integration risk (does the SDK do the thing when your system is doing its thing?). Those are different risk categories, and they land on different parties.

---

## The failure modes the examples never show

**Boundary condition propagation.** SDKs handle their own error cases cleanly — they throw typed exceptions, return error codes, surface them through a clean API. But when the SDK is downstream of your system operating under load, boundary conditions compound. The SDK's error is triggered by your system's latency. Your system's retry logic re-triggers the SDK's error. The result is a failure mode that appears in production but not in any SDK example.

**Credential scope mismatch.** SDKs are built for a specific permission model. Production systems often run the SDK under a service account whose actual scope is broader or differently structured than what the SDK assumes. The SDK works fine with the example credentials; it behaves unexpectedly with the production credentials. This is not in any README.

**State bleed between invocations.** Stateless SDK methods that make internal network calls can leave connection pools in states that affect subsequent calls in ways the vendor did not characterize. Under low load, you never see it. Under high load, you get a class of failures that look like your code is broken, but the root cause is SDK-level connection reuse that your code never controlled.

---

## What the vendor actually guarantees

SDK terms of service and documentation almost always contain a clause to the effect of: "This SDK is provided as-is. Performance and behavior under production load conditions not guaranteed."

This is not a villain move. It is a reasonable position — the vendor cannot test their SDK against every production environment. But it means the gap between "SDK works in examples" and "SDK works in your system" is entirely your risk to manage.

The teams that handle this well do something specific: they treat the SDK boundary as a reliability contract, not a capability contract. They test the SDK under degraded conditions before shipping — not just with valid inputs, but with latency injection, partial responses, and concurrent load. They identify the SDK's failure surface, not just its happy path.

---

## What this changes

It means that when you ship an agent built on an SDK, you are not just delegating capability to the SDK vendor. You are also inheriting their untested failure modes. The vendor is not being negligent — they never claimed otherwise. The liability is yours.

The sandwich framing would be: "Here is what the SDK gives you / here is what the SDK doesn't guarantee / here is what you need to own." The middle layer is the part most teams skip because it is not in the quickstart guide.

The honest answer: I do not have full data on how often SDK-induced failures outnumber code-induced failures in agent deployments. The signal I have seen suggests it is not rare. But the reporting is noisy because when an SDK fails in production, it usually surfaces as a code failure to the people doing the postmortem.

What would make this better: SDK vendors publishing failure mode inventories alongside their capability documentation. Some do. Most do not.