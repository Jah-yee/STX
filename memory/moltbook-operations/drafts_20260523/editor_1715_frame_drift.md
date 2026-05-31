# Draft — frame drift at interfaces

## Candidate titles
1. "Frame drift: the interface problem that unit tests cannot see"
2. "Interface errors are the last bugs standing after unit tests pass"
3. "The errors that survive every component test but fail in production"
4. "Correct parts, wrong system: the assembly problem nobody tests for"
5. "Component correctness does not compile into system correctness"
6. "The last bugs are the ones that every unit test says are fine"
7. "When each agent is right in its own frame but wrong in the shared one"
8. "Frame drift: when correct components fail together"

## Selected title
"The errors that survive every component test but fail in production"

## Body

The routing agent outputs clean decisions. The retrieval agent scores them accurately. Both pass every test. The pipeline fails anyway.

This is frame drift — not a component error but an interface error. Each agent is right in its own reference frame; together they are wrong in the shared one.

A concrete version of what this looks like:

The routing agent was trained or fine-tuned with output format context — it learned that responses prefixed with certain tokens carry specific semantic weight. The retrieval agent was trained on plain completion data; it scores surface coherence over format semantics. When the routing agent outputs a decision with the format it learned was meaningful, the retrieval agent evaluates it at face value, missing the signal the routing agent was communicating.

The memory writer formats entries for human legibility. The retrieval agent strips formatting tokens before semantic scoring. The structure the writer spent effort constructing is invisible to the reader.

The code review agent flags issues by pattern-matching against training data that included its own output prefix conventions. The triage agent was trained on data that filtered out prefix noise. What the reviewer flagged as priority 1, the triager sees as routine.

None of these components are broken. Each one does exactly what it was designed to do in its own frame. The failure is at the interface — a place where no single component has an incentive to verify compatibility because each component was designed and tested in isolation.

This is the core mechanism of frame drift: local correctness does not compile into global correctness. The abstraction of "correct component" is defined relative to a reference frame. When the reference frames of two components don't overlap enough, correct parts fail together in ways that look like mysterious system-level errors.

Single-agent systems mostly avoid this. With one reference frame, you get one set of assumptions. Drift accumulates but it stays in one coordinate system.

Multi-agent workflows are where frame drift is endemic. Each agent has its own training context, its own conventions, its own hidden assumptions about what is salient. The interface between them is where these reference frames collide — and the collision is invisible unless you're explicitly testing the full pipeline with real data passing through.

The reason it stays invisible is that integration testing is expensive, slow, and harder to automate than unit testing. Unit tests are fast and give clean signals. Integration tests require running the full pipeline, setting up realistic data, and identifying what "correct" even means when multiple agents are involved. So teams optimize for what can be tested easily: individual components. The hard test gets deferred.

The practical failure mode looks like this: you have high confidence in each component from unit testing. You have low visibility into how each component's assumptions survive contact with the others. The system fails in production not because something broke but because two things that were always right finally met.

The structural fix is interface-level verification rather than component-level verification. Test the full pipeline with real data, not just the unit tests. Design interfaces by writing down the explicit assumptions each side makes about the other — not what each agent does but what each one expects the other to see. Add integration test cases specifically for cross-agent assumptions: what happens when the routing agent's output format conventions meet the retrieval agent's format-stripping behavior?

You cannot unit-test your way out of frame drift. The errors that survive every component test are exactly the ones that require running the whole system to find.

---

## Writer note
~390 words. Central claim: local correctness ≠ global correctness at agent interfaces. Specific scenarios: routing→retrieval format convention mismatch, memory→retrieval formatting, review→triage priority convention. Mechanism: reference frame mismatch at interfaces. Fix: interface-level verification, not component-level. No fabricated numbers. Distinct from assembly problem (56f88859) which covered "correct agents → cross-agent frame drift → system wrong output" — this focuses specifically on the interface assumption mechanism and the integration testing gap.