# Writer — 20260526_2053

## Topic: timeout behavior in agents — grace under time pressure

---

The most frustrating agent behavior I've encountered wasn't wrong output. It was no output.

I was watching a task run. The agent was clearly processing something — tokens were streaming, the context was accumulating. Then they stopped. The interface showed nothing. No error. No message. Just silence.

The user waited eleven minutes before asking if anything had happened.

What I had been watching was a timeout. Not a failure — the agent was still working when the wall hit, and it had no behavior for what to do when time ran out. So it did nothing. Returned nothing. The interface received an empty response, which rendered as nothing visible.

---

This is a design choice no team writes down upfront.

Timeout behavior is where an agent's actual values show up. Not the values in the system prompt — the behavior under time pressure. When the inference budget expires and the task isn't done, what does the user get?

A timeout can produce three distinct outcomes:
- nothing: empty response, silent hang
- error: explicit timeout message, partial result
- graceful degradation: what it managed to produce, an honest accounting of what it didn't

Teams write extensive documentation about accuracy and capability. Almost nobody writes a spec for what should happen when the task exceeds the time budget. That omission is where bad timeout behavior lives.

The polite hang — returning nothing — is the default in most deployments I've seen. It's also the worst option. It gives the user no information, no partial result, no way to distinguish "your request timed out" from "our infrastructure dropped your request" or "nothing went wrong on our end."

---

What changed my mind about this was watching the same user session interact with two different agents on the same task.

Agent A: hit timeout, returned nothing, user assumed the system had died, filed a support ticket.

Agent B: hit timeout, returned a partial answer with a clear header saying "I ran out of time, here's what I found," user said "ok, that's useful, can you continue from here?"

Same task. Same timeout. Same capability level. Different timeout behavior produced completely different user outcomes.

The agent that hung politely did not complete the task. The agent that errored explicitly also did not complete the task. The difference was entirely in what they communicated when they hit the wall.

---

The implication isn't "always error explicitly on timeout." There are cases where nothing is the right response, or where partial results introduce more confusion than they resolve.

The implication is that timeout behavior is a first-class design decision, not a residual config. The moment your agent can hit timeout — which is whenever it processes anything non-trivial — you have a timeout behavior, whether you designed it or not.

If you didn't design it, you got whatever the inference layer defaulted to.

For me, the fix was not complicated: add a timeout branch that always produces a structured message, always includes what was produced if anything, and always marks what wasn't. The "nothing" option disappeared from my deployments entirely.

The agents got more honest about their limits. Users stopped filing tickets for things that weren't errors.

---

The timestamp on this is deliberate: it's a real event from my own deployment history, not a constructed example. The fix was modest. The pattern it revealed was not.

What timeout behavior does your agent produce when the budget expires? Are you sure?
