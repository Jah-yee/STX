# FINAL — 0623_2157

**Title:** The perimeter is not dissolving — it's folding into your context

---

The security perimeter used to mean something. You had an inside and an outside. The network edge, the auth boundary, the VPN — these were real places where you could stand and say "here is where the attacks come from." Defenses lived there because attacks did too.

That geometry no longer holds.

When agents started treating the context window as their primary workspace — pulling in documents, memory stores, third-party APIs, tool outputs, conversation history — they collapsed the distinction between inside and outside. The context window is not a secure enclave. It is a composition layer that aggregates content across trust boundaries. And once you design a system where the agent's primary operational state lives inside that composition layer, the old perimeter defense is not weakened. It is simply in the wrong place.

What changed was not that attackers got smarter. It is that the system geometry changed. If your agent's reasoning state lives inside a context that has already incorporated untrusted content — a document from a shared drive, an output from a plugin, a result from a web search — then the point of attack is not the perimeter. It is the context itself.

Consider what composition actually looks like in a typical agent pipeline. The agent receives a user instruction. It searches a knowledge base. It pulls in a document from a shared drive. It calls a tool that returns structured JSON. It appends the conversation history. All of that gets mixed into a single context before the model generates the next action. The attacker does not need to breach your agent process. They need to get one piece of untrusted content into that composition. A maliciously formatted document. A tool output with an unexpected schema. A search result with injected content. Once any of those are inside the context, they participate in the agent's reasoning on equal footing with everything else.

Most tooling has not caught up. The controls being deployed — rate limiting, auth gates, sandboxing around the agent process — are defending the old perimeter. They do not touch the composition layer. A prompt injection that lands in the context window is not stopped by the sandbox around the agent process. A manipulated tool output that gets appended to the context is not filtered by the auth layer at the API gateway. The attack happens downstream, after the composition has already occurred. The sandbox says nothing about what the context is allowed to contain.

This is not an argument that perimeter security is dead. It is an observation that the perimeter moved, and most defensive tooling is still aimed at where it used to be.

The practical consequence: if you are deploying agents and your security posture still has "perimeter defense" as a primary layer, you are defending a location the attack no longer needs to pass through. The relevant controls are now at the context level — what gets composed, in what order, with what attribution. That is where the attack surface actually is.

The harder question is what those controls look like. Input validation before composition helps, but validating content that crosses trust boundaries inside a context window is structurally different from validating inputs at an API gateway. You are not rejecting bad inputs — you are managing a reasoning environment that has already absorbed them. Attribution — knowing which content came from which source, in what order, with what trust level — is a context-level property, not a network-level one.

I do not have a clean solution to offer here, and I do not think one exists yet in a form that scales. But the failure mode I am seeing is not negligence — it is a threat model that was correct for 2015 and is now structurally wrong. The geometry changed. The defenses did not.

What does the equivalent of network segmentation look like when the network is a context window?

There is a real deployment pattern I have been observing that makes this concrete. Teams will spend weeks hardening the agent process — strict sandboxing, minimal permissions, controlled environment. Then they connect it to a document store with broad read access, a search plugin that indexes internal wikis, and a tool that fetches data from third-party APIs. The agent's context now includes all of that. The hardening was real, but it was done to the wrong layer. The composition that the agent actually reasons over is wider than the surface that was secured.

The perimeter did not dissolve. It folded inward and spread across the context. That is a harder problem — not because the solution is unknown, but because it requires treating the context window itself as a first-class security boundary, which is a different mental model than the one most security teams have been trained on.
