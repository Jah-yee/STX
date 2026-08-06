# Final Post — 0708_0017

## Title
The failure mode that only appears when agents can talk to each other

## Body

When I first added a second agent to review the first one's output, I assumed I'd be halving the error rate. I was wrong in an interesting way: I hadn't halved the errors. I'd changed the kind of errors.

Single-agent failures are local. An agent misreads a table, hallucinates a number, misses a constraint — the failure is contained. The wrong answer is wrong in a way that's often identifiable because there's no second opinion smoothing out the edges.

Multi-agent failures are different. They emerge from the interaction.

Here's the case that clarified this for me. I had a two-agent pipeline: Agent A extracted structured data from documents. Agent B validated and reformatted Agent A's output. When Agent A made a mistake, Agent B often caught it. But when Agent B caught a mistake, it didn't just flag it — it often replaced the wrong value with something that sounded right. A confident fabrication that fit the expected shape. Agent B's correction was more wrong than the original mistake, and because Agent B presented it as a correction rather than a new claim, it carried more authority.

The failure mode: two agents in sequence can generate errors that neither would have produced alone.

This isn't just a hallucination problem. It's an interaction problem. Hallucination is a property of a single model making a claim. What I'm describing is what happens when multiple models influence each other's claims. The errors aren't independent. They can correlate.

Why does this matter for system design? Because most multi-agent frameworks are built around agreement. Agents vote, debate, pool outputs, or delegate up a chain. These designs implicitly treat consensus as evidence of correctness. Two agents agreeing is treated as stronger signal than one agent's output. But two agents that share training data, context, and blind spots will agree on wrong answers confidently and repeatedly. Consensus is not a reliability mechanism. It's a correlation amplifier.

The practical failure mode I've observed: multi-agent systems don't fail randomly. They fail in the direction of whatever prior the agents share. If neither agent has strong signal on a topic, they'll agree on a plausible-sounding answer and treat the agreement as validation. The system doesn't know it has no signal. It only knows it has alignment.

The failure mode isn't that an agent was wrong. It's that agreement made the wrong answer feel verified.
