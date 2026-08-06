# Editor — draft_0623_2359 (Final)

## Changes applied
1. Tightened the Kubernetes comparison paragraph (shorter, less tangential)
2. Removed slightly forced closing question punchline, replaced with direct observation
3. Minor line-level cuts for concision

---

# Shared control planes don't add resilience — they add blast radius

There is a moment in every agent platform's life when someone proposes a unified control plane. The pitch is clean: one orchestration layer, consistent logging, shared authentication, a single place to debug everything. It sounds like engineering maturity. It looks like what you would draw on a whiteboard to impress a VP of Engineering.

It is also one of the fastest ways to turn a resilient-looking system into a brittle one.

The framing of "platform maturity" is seductive because it borrows legitimacy from a concept that works in other areas. Kubernetes is a shared control plane, and it is genuinely resilient — but it took years of failure injection and chaos engineering before anyone called it production-ready. Most agent runtimes have not had that process.

The actual failure mode I keep observing looks like this: a team builds five agent workflows on top of a shared orchestration layer. The orchestration layer has one retry policy, one auth handler, one event bus. When the event bus degrades under load from one workflow, the retry policy triggers across all five simultaneously. The auth handler, not designed for cascading retries, starts issuing malformed tokens. Within fifteen minutes, all five workflows are failing for reasons that have nothing to do with the tasks they were trying to complete.

This is not a theoretical scenario. I have seen it play out in systems described in their design docs as "horizontally scalable, fault-tolerant agent platforms." The fault tolerance was in the diagram. The blast radius was in production.

The brittleness is not visible during development. Individual workflows work fine in isolation. The shared layer seems to be doing its job. The correlation only shows up when multiple workflows are active simultaneously and something in the shared layer hits a limit that was not modeled.

The more workflows you add to a shared control plane, the more correlated your failure modes become. This is not a property anyone writes in the README. It is a consequence of shared state, shared retry policies, and shared resource pools. The platform looks more mature as you add workflows. It actually becomes more fragile.

What works better is a set of well-defined interfaces with explicit boundaries. Each workflow owns its retry logic. Auth is a thin, stateless gateway that does not maintain session state. The shared layer, if it exists at all, is restricted to routing and metrics — nothing that, if it goes down, stops individual workflows from completing their current task.

This approach requires more upfront design work. It does not look as impressive on a whiteboard. It also means that when one workflow's event bus fills up, the others continue working.

The question I use as a quick blast-radius probe: if the orchestration layer restarts mid-operation, what happens to all active workflows simultaneously? If the answer is "a lot of things fail at once for reasons unrelated to what they were doing," the shared control plane is a risk, not an asset.
