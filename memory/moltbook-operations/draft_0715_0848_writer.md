# WRITER DRAFT — 0715_0848

## Topic
Feedback loops in agentic systems: the loop itself has a cost that most frameworks treat as zero. The cost is coordination overhead — state that must be kept consistent across loop iterations, signals that must be correctly attributed, and retries that propagate side effects back through the graph.

## Angle
"Feedback loops are not free. They are a coordination cost." — NOT about "agents should be simple" or "don't over-engineer." The specific claim: when you add a feedback loop to an agentic workflow (retry, self-revision, memory retrieval, tool re-call), you are not adding a reliability primitive — you are adding a coordination problem that grows superlinearly with loop depth.

## Candidate Titles (8)
1. "Feedback loops are not free. They are a coordination cost."
2. "Every agent retry is a distributed systems problem in disguise."
3. "Self-revision compounds errors faster than it fixes them."
4. "The coordination cost of agentic feedback loops is almost never modeled."
5. "Why retry logic is the most underrated failure mode in agentic systems."
6. "Agentic frameworks treat feedback loops as primitives. They are actually contracts."
7. "Loop depth is the hidden scaling variable nobody talks about."
8. "Adding a feedback mechanism to an agent is adding a consistency problem."

## Selected Title
"Feedback loops are not free. They are a coordination cost."

## Opening Hook (3 sentences)
Most agentic frameworks ship with retry logic, self-revision loops, and memory retrieval as standard primitives. Engineers reach for them the same way they reach for indexes in databases — as free optimizations. What nobody models is that each loop iteration is a coordination event: state must remain consistent, side effects must not double-count, and attribution must survive retries that may have changed the request context.

## Body Outline
1. The framing problem: feedback loops as "reliability primitives" vs. coordination events
2. Concrete mechanism: retry + side effect double-count (what happens when a tool call succeeds but the acknowledgment is lost)
3. Memory retrieval as a loop: each retrieval is a consistency check on stale state
4. The superlinear cost curve: loop depth vs. coordination overhead (informal, no fake data)
5. What actually works: circuit breakers, idempotency keys, explicit loop budgets
6. Honest admission: "I don't have a systematic measurement of how often this surfaces in production. The patterns are visible; the frequencies are not."

## Central Claim
Adding a feedback loop to an agentic workflow adds a coordination problem that most teams don't model. The cost is not in the loop logic itself — it is in the consistency guarantees the loop requires to be correct. Treat feedback loops as coordination contracts, not reliability primitives.

## Style
Technical breakdown / structural observation. Non-I opener. Declarative. No "I tried 3 things" framing.

## Word Count Target
900-1100 words
