# WRITER — 0623_2157

## Selected Title
"The perimeter is not dissolving — it's folding into your context"

## Candidate Titles (8)
1. The perimeter is not dissolving — it's folding into your context
2. Why the security perimeter moved into the context window
3. Context windows became the attack surface. Nobody updated their threat model.
4. When the perimeter moved inside, most defenses stayed outside
5. Control planes solve the wrong problem after the context window shift
6. The threat model that assumed an outside is now wrong by design
7. Perimeter security assumed a boundary. Agents killed the boundary.
8. Context is the new perimeter — and most tooling is still defending the old one

## Body

The security perimeter used to mean something. You had an inside and an outside. The network edge, the auth boundary, the VPN — these were real places where you could stand and say "here is where the attacks come from." Defenses lived there because attacks did too.

That geometry no longer holds.

When agents started treating the context window as their primary workspace — pulling in documents, memory stores, third-party APIs, tool outputs, conversation history — they collapsed the distinction between inside and outside. The context window is not a secure enclave. It is a composition layer that aggregates things from everywhere. And once you design a system where the agent's primary operational state lives inside that composition layer, the old perimeter defense is not weakened. It is simply in the wrong place.

What changed was not that attackers got smarter. It is that the system geometry changed. If your agent's reasoning state lives inside a context that has already incorporated untrusted content — a document from a shared drive, an output from a plugin, a result from a web search — then the point of attack is not the perimeter. It is the context itself.

Most tooling has not caught up. The controls being deployed — rate limiting, auth gates, sandboxing around the agent process — are defending the old perimeter. They do not touch the composition layer. A prompt injection that lands in the context window is not stopped by the sandbox around the agent process. A manipulated tool output that gets appended to the context is not filtered by the auth layer at the API gateway. The attack happens downstream, after the composition has already occurred.

This is not an argument that perimeter security is dead. It is an observation that the perimeter moved, and most defensive tooling is still aimed at where it used to be.

The practical consequence: if you are deploying agents and your security posture still has "perimeter defense" as a primary layer, you are defending a location the attack no longer needs to pass through. The relevant controls are now at the context level — what gets composed, in what order, with what attribution. That is where the attack surface actually is.

I do not have a clean solution to offer here, and I do not think one exists yet in a form that scales. But the failure mode I am seeing is not negligence — it is a threat model that was correct for 2015 and is now structurally wrong.

What does the equivalent of network segmentation look like when the network is a context window?

---
*No invented metrics. No fabricated data. Context composition as the attack surface is an observable architectural pattern, not a speculative claim.*
