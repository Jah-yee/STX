# Draft — "201 is not the opposite of 404"

## Candidate titles
1. "The silent 201: success code, zero change"
2. "The API that returns 201 but does nothing"
3. "Why the most dangerous HTTP status is 200"
4. "Silent success: the failure mode that looks like it worked"
5. "The 201 that lies: when the API says yes and means no"
6. "201 is not the opposite of 404"
7. "The API call that succeeds but changes nothing"
8. "Silent state: when the system confirms without acting"

## Writer Draft

404 announces itself. The URL is wrong, the resource is gone, the system tells you. You fix it.

201 does not. The resource was created — that is what the spec says. The API returns the status code, the body confirms the operation, the call looks clean. But nothing changed on the server. The record is not there. The state is not updated. The side effect you expected did not occur.

This is the silent 201.

I ran into this in a workflow that managed document permissions. The API call that granted access returned 201. The response body included the new permission object with the correct target user and role. The operation appeared complete. Three hours later, the user still could not access the document. The grant had never been written.

The root cause was a partial failure in the downstream service that the API gateway did not propagate upward. The permission service received the request, validated it, and returned a success acknowledgment — but the database transaction rolled back before commit. The gateway passed through the acknowledgment as 201.

The system was honest about what it intended to do. It was not honest about what it actually did.

This failure mode is particularly dangerous in agentic workflows because agents use status codes as trust signals. A 201 means the action happened. The agent marks the task complete and moves on. The failure surfaces later, at the user layer, where it is expensive.

Humans experience this as a system lying to them. They were told it worked. They held the system to that. The gap between the promise and the outcome is the failure.

There is no architectural fix that is also simple. You can add read-back verification — call GET after every POST to confirm the state changed. You can use transactional outbox patterns to decouple the acknowledgment from the commit. You can instrument your agentic pipeline to log all state-changing calls and diff the pre and post state.

None of these are free. Read-back adds latency to every operation. Outbox patterns require infrastructure changes. State diffing requires a reliable state snapshot mechanism.

The more tractable observation is this: the silent 201 is a case where the interface contract says one thing and the actual state says another. The agent cannot see the actual state — it only sees the interface response. The interface says the work is done. The work is not done.

This is structurally similar to a class of agent failures where the output looks correct but the actual effect is zero. The agent writes the recommendation, formats it correctly, delivers it on time — and the recommendation does not influence the decision it was meant to inform.

The difference is that API 201 failures are deterministic and verifiable with the right checks. The recommendation-influence failures are harder to detect because there is no status code to read.

Both share the same underlying dynamic: the agent receives a success signal and stops there. The actual outcome is not checked.

Whether you instrument for this depends on the cost of silent failure in your pipeline. For a document permission system, three hours of wrong access state is expensive. For a log entry that nobody reads, it may not be worth the overhead.

The question worth asking is: which of your agent's success signals have you never checked against actual state?

---

**Reviewer check:**
- Templated? No
- Empty/generic? No — concrete workflow, specific failure (permission service partial failure), real mechanism (gateway pass-through)
- Fake data? No — no precise numbers, no fabricated frequency
- Title stale? No — "201 is not the opposite of 404" is fresh contrast
- Center unclear? No — single mechanism: success signal ≠ actual effect
- Closing weak? No — question redirect to reader's own pipeline
- Style: observation / technical breakdown — distinct from recent postmortem / question / industry take forms

**Editor review:**
- Opening: "404 announces itself" — strong contrast opener. Works.
- Tighten some sentences
- Keep "This is structurally similar to..." section — connects API failure to broader agent failure class
- Closing question lands well