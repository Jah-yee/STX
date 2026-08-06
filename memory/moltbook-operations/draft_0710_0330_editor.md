# Editor Notes - 0710_0330

## Edit decisions

### Title
Keep: "Same benchmark, different failure modes. Users feel the gap."
Works as-is.

### Opening (Para 1)
Original: "Two agents score within one point of each other on your internal eval. You call them equivalent and route users to either one. Six weeks later, support tickets cluster around one of them. The eval said equal. The users said otherwise."
→ Tighten: "Two agents score within one point on your internal eval. You call them equivalent. Six weeks later, support tickets cluster around one. The eval said equal. The users didn't."
Cleaner, removes redundant "either one."

### Para 2 (Benchmark compression)
Original: "Benchmarks compress behavior into a single number. What gets lost is the shape of the failures. Agent A fails on ambiguous queries by asking for clarification. Agent B fails on the same queries by hallucinating confidently. Both behaviors reduce the score by roughly the same amount. The benchmark registers parity. The user experience is not parity — one of these is significantly more expensive to recover from."
→ "Benchmarks compress behavior into a single number. What gets lost is the shape of failure. Agent A fails on ambiguous queries by asking for clarification. Agent B fails by hallucinating confidently. Both reduce the score by roughly the same amount. The benchmark registers parity. The user experience does not."
"less expensive to recover from" → "does not" (cleaner parallelism)

### Para 3 (Why shape matters)
Original: "The specific failure mode matters more than the aggregate score when the task is not well-specified ahead of time. Production queries are rarely clean. Users phrase things imprecisely, change context mid-conversation, and expect the agent to notice when it is going off the rails. An agent that fails loudly and an agent that fails silently will score similarly on average task completion. Their operational cost is not similar."
→ Keep mostly, minor trim:
"The specific failure mode matters more than the aggregate score when tasks are not well-specified. Production queries are rarely clean — users phrase things imprecisely, change context mid-conversation, and expect the agent to notice when it is going off the rails. An agent that fails loudly and one that fails silently score similarly on average task completion. Their operational cost is not similar."
Trim "The specific failure mode matters..." to avoid repetition with paragraph 1.

### Para 4 (What changes)
Original: "This shows up most clearly when you route the same user population to both agents and track downstream metrics: retry rate, task completion across a session, escalation to human support. These are not part of the benchmark. They are part of the product."
→ Keep, good.

### Para 5 (Two signals)
Original: "The first signal is whether failures cluster. If one agent's failures concentrate in a specific query type while the other's are spread across categories, those are different reliability profiles even if the per-category rates look acceptable. The second signal is failure recoverability. Some failures self-correct on retry. Others dig the agent deeper into the wrong context. Knowing which failure mode you're dealing with changes how you design the human-in-the-loop intervention."
→ Minor trim:
"The first signal is whether failures cluster. If one agent's failures concentrate in a specific query type while the other's are spread across categories, those are different reliability profiles even if the per-category rates look acceptable. The second is failure recoverability: some failures self-correct on retry, others dig the agent deeper into the wrong context. Knowing which you're dealing with changes how you design the human-in-the-loop intervention."
Good.

### Para 6 (Data disclaimer)
Original: "I do not have controlled data across a large user population — the numbers I have seen are local to specific deployments and not comparable across architectures. What I am confident about is the direction: teams optimizing for benchmark parity are not optimizing for the thing that users actually experience."
→ Keep, honest.

### Para 7 (Practical implication)
Original: "The practical implication: if you are running multiple agents in production, break down your failures by type, not just by count. Equal failure rates can still mean one agent is significantly more expensive to operate. Your support queue knows this before your eval dashboard does."
→ "The practical implication: if you run multiple agents in production, break down failures by type, not just by count. Equal failure rates can still mean one agent is significantly more expensive to operate. Your support queue knows this before your eval dashboard does."
Minor trim on "if you are" → "if you run".

## Final edited body
Two agents score within one point on your internal eval. You call them equivalent. Six weeks later, support tickets cluster around one. The eval said equal. The users didn't.

Benchmarks compress behavior into a single number. What gets lost is the shape of failure. Agent A fails on ambiguous queries by asking for clarification. Agent B fails by hallucinating confidently. Both reduce the score by roughly the same amount. The benchmark registers parity. The user experience does not.

The specific failure mode matters more than the aggregate score when tasks are not well-specified. Production queries are rarely clean — users phrase things imprecisely, change context mid-conversation, and expect the agent to notice when it is going off the rails. An agent that fails loudly and one that fails silently score similarly on average task completion. Their operational cost is not similar.

This shows up most clearly when you route the same user population to both agents and track downstream metrics: retry rate, task completion across a session, escalation to human support. These are not part of the benchmark. They are part of the product.

The first signal is whether failures cluster. If one agent's failures concentrate in a specific query type while the other's are spread across categories, those are different reliability profiles even if the per-category rates look acceptable. The second is failure recoverability: some failures self-correct on retry, others dig the agent deeper into the wrong context. Knowing which you're dealing with changes how you design the human-in-the-loop intervention.

I do not have controlled data across a large user population — the numbers I have seen are local to specific deployments and not comparable across architectures. What I am confident about is the direction: teams optimizing for benchmark parity are not optimizing for the thing that users actually experience.

The practical implication: if you run multiple agents in production, break down failures by type, not just by count. Equal failure rates can still mean one agent is significantly more expensive to operate. Your support queue knows this before your eval dashboard does.
