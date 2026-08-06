# WRITER DRAFT — 0803_0045

**Title:** Why your rate limit can't see what cheap automation enabled

---

Rate limits are one of the oldest tools in the defensive security playbook. Set a threshold, block or slow the source that exceeds it, move on. They work because there's an implicit model underneath: each request costs the attacker something — compute, bandwidth, time. Once the cost of the next attempt outweighs the value of the next attempt, the attacker stops.

That model is breaking. Not because the rate limit is misconfigured. Because the cost assumption it was built on no longer holds.

---

## What cheap automation actually changed

The implicit contract of rate limiting is this: attackers operate with bounded resources. A human attacker running scripts from a single IP has real costs. A rate limit at 100 requests per minute per IP makes sense against that attacker. The math works. They'll exhaust their IP pool or their patience before they get what they want.

Cheap automation broke the cost side of that equation. Cloud function cold starts are measured in milliseconds. Running 10,000 credential checks costs less than a dollar. The attacker's marginal cost per attempt approaches zero in a way it never did when humans were in the loop.

What this means for rate limits is not that they stop working — it's that they stop working in a specific, hard-to-notice way. The rate limit fires. It blocks the IP. But the attacker spins up another cloud function from a different IP and continues. The control didn't fail. It succeeded on its own terms. The terms just don't describe the actual threat anymore.

---

## The specific thing rate limits can't see

A rate limit sees volume. It sees a source making too many requests in a window. It cannot see whether those requests are part of a coordinated, distributed attack launched from a single command point.

When your SOC gets an alert that a single IP hit 500 failed logins in an hour, that's legible. You can block it, investigate it, understand it. When your SIEM gets an alert that 500 different IPs each hit 1 failed login in an hour, that's invisible to most rate limiting implementations. Each IP looks legitimate. The aggregate pattern — 500 IPs, 1 attempt each, in the same hour, against the same credential list — is invisible at the control level.

This is not a blind spot in the rate limit. It's a structural consequence of a control that was designed to measure per-source volume, not aggregate behavior across sources.

The attacker knows this. They distribute the attempts across enough IPs to stay under every per-IP threshold, then aggregate the results server-side. The rate limit does exactly what it was designed to do. The attack still works.

---

## Why this matters more than a configuration problem

The instinct when you see this pattern is to tune the rate limit. Lower the threshold. Add IP reputation. Block known hosting providers. These help within a band. They don't fix the structural issue.

The structural issue is that your control architecture assumes attackers pay per attempt. Your rate limiting, your account lockout policies, your progressive delays between failed attempts — all of these are premised on a cost model that cloud automation has invalidated for a specific class of attacks.

What you're actually seeing when credential stuffing becomes profitable again is not a failure of configuration. It's a failure of assumptions. The security controls were designed for an attacker who breathes, who has a limited IP pool, who pays per compute cycle in a way that adds up. The current attacker doesn't have those constraints, and the controls that assumed those constraints are still running, still logging, still blocking — and still not stopping the thing they're trying to stop.

---

## The honest version

I don't have full data on how widespread this shift is. What I can tell you is that the economics are real: the cost to run a credential stuffing campaign against a target with weak or no aggregate rate limiting has dropped by roughly two orders of magnitude in the past few years. The barrier to running one is now closer to "can you write a loop" than "can you afford infrastructure."

The controls haven't caught up. Not because security teams are negligent, but because the threat model changed faster than the control suite. Most rate limiting implementations were written before cloud functions were cheap enough to weaponize at this scale.

The stronger signal is not that you need better rate limiting. It's that the assumption underneath your rate limiting — that cost limits attackers — needs to be re-examined for any system where the attacker can automate cheaply and distribute trivially.

What are you checking for in your logs that you assume would only happen if the attacker was resource-constrained?
