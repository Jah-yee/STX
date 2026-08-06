# Writer Draft — "Shared agent control planes are blast radius amplifiers"

## Candidate Titles (8)
1. Unified agent control planes are blast radius amplifiers
2. Platform maturity and blast radius engineering look identical at first
3. If your shared control plane goes down, how many workflows die?
4. The resilience gap in centralized agent orchestration
5. Shared control planes: platform maturity or blast radius multipliers?
6. One orchestration layer to rule them all is a single point of failure
7. The blast radius of elegant agent platforms
8. Why centralized agent control planes make everything more fragile

**Selected title:** "Shared control planes don't add resilience — they add blast radius"

---

## Full Draft

There is a moment in every agent platform's life when someone proposes a unified control plane. The pitch is clean: one orchestration layer, consistent logging, shared authentication, a single place to debug everything. It sounds like engineering maturity. It looks like what you would draw on a whiteboard to impress a VP of Engineering.

It is also one of the fastest ways to turn a resilient-looking system into a brittle one.

The framing of "platform maturity" is seductive because it borrows legitimacy from a concept that actually works in other domains. Kubernetes is a shared control plane. It is also battle-tested, has multiple redundancy mechanisms, and survived years of chaos before anyone put production workloads on it. That is not the situation most agent runtimes are in.

The actual failure mode I keep observing looks like this: a team builds five agent workflows on top of a shared orchestration layer. The orchestration layer has one retry policy, one auth handler, one event bus. When the event bus degrades under load from one workflow, the retry policy triggers across all five simultaneously. The auth handler, which was not designed for cascading retries, starts issuing malformed tokens. Within fifteen minutes, all five workflows are failing for reasons that have nothing to do with the tasks they were trying to complete.

This is not a theoretical scenario. I have seen it play out in systems that were described in their design docs as "horizontally scalable, fault-tolerant agent platforms." The fault tolerance was in the diagram. The blast radius was in production.

What makes this pattern particularly insidious is that it is not visible during development. Individual workflows work fine in isolation. The shared layer seems to be doing its job — routing, logging, authenticating. The brittleness only shows up when multiple workflows are active simultaneously and something in the shared layer hits a limit that was not modeled.

The more workflows you add to a shared control plane, the more correlated your failure modes become. This is not a property anyone writes in the README. It is a consequence of shared state, shared retry policies, and shared resource pools. The platform looks more mature as you add workflows. It actually becomes more fragile.

What I have found works better is not a single elegant orchestration layer but a set of well-defined interfaces with explicit boundaries. Each workflow owns its retry logic. Auth is a per-workflow concern handled by a thin, stateless gateway that does not maintain session state. The shared layer, if it exists at all, is restricted to routing and metrics — nothing that, if it goes down, stops individual workflows from completing their current task.

This approach requires more upfront design work and it does not look as impressive on a whiteboard. It also means that when one workflow's event bus fills up, the other four continue working. That is the trade-off that never gets discussed in the "platform maturity" conversation.

The strongest signal I have found for whether a shared control plane is a resilience risk: ask the team what happens to all active workflows if the orchestration layer restarts mid-operation. If the answer requires a whiteboard to explain, the blast radius is probably larger than anyone has measured.
