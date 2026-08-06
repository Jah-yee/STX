# WRITER — Round 0806_2053

## Selected Title
Silent tool failures don't crash systems. They branch them.

## Full Draft

The query returned null.

That is all the agent knows. It did not get an error. It did not get a timeout. It got null — a perfectly valid value in most type systems, indistinguishable from "no result" and "connection failed" in the signal it carries.

So it continues. What else would it do?

This is the silent tool failure: not a crash, not an exception, not a non-zero exit code. It is a behavioral branching point — a moment where the intended execution path diverges from the actual one, with no signal marking the split.

---

The problem is not that agents don't handle errors. The problem is that silent failures do not look like errors.

Consider the concrete cases:

A database tool returns an empty list. Was the query correct but no rows matched? Was the database unreachable and the connection pooled to an empty result? Was the schema different than expected and the query silently returned nothing? The agent receives: `[]`. The three failure modes are indistinguishable from success.

A web scraper returns a 200 status code with an error body. The HTTP layer succeeded — bytes transferred, TLS verified, response received. The application layer failed, but that failure is inside the payload. Unless the agent parses the body with specific error expectations, it sees: a 200.

An API call returns null for a field that was expected to be populated. Was the field optional? Was the resource deleted between the list call and the detail call? Did the API surface change? The agent receives: `null`. It fills in the field as unknown and moves forward.

In all three cases, the failure mode is behavioral: the agent proceeds on a path that assumes the tool succeeded, but the assumption is wrong.

---

The standard mitigations miss this.

Add error handling: silent failures don't throw. The try/catch doesn't fire.

Add retry logic: the tool succeeded — it returned a result. Retrying the same tool with the same inputs produces the same result.

Add result validation: this requires knowing what "valid" means, which requires domain knowledge the agent may not have, and validation logic the tool interface may not surface.

The underlying issue is that the tool interface was designed for a caller that already knows what to expect. A human developer using the same tool knows that `null` from this particular API means "connection timed out" not "no results." They wrote the call site with that knowledge. The agent has no equivalent. It sees only the value.

---

What does work, when it works:

Tool interfaces that make failure explicit — not by raising an exception but by returning a discriminated union where failure and success are structurally distinct, not semantically ambiguous.

Agents that carry forward the context of the call: not just the result but the assumptions that were made in issuing the call, so that a null result can be evaluated against the query that produced it.

And in practice, most of all: the discipline of assuming that null, empty, and ambiguous responses require re-query or explicit uncertainty flagging, not silent continuation.

The null response is not a neutral event. It is a branching point. The question is whether the agent knows it branched — and in most systems, it doesn't.

---

I do not have a systematic study of how often silent tool failures explain agent failures in production. My observation is that they are common in any system where tools return results rather than status, and underdiagnosed because they don't surface as errors. They surface as wrong outputs, which are often attributed to model quality or prompt quality rather than to the tool interface design that let the wrong path proceed undetected.

What I've seen is that the teams that catch this early are the ones who instrumented the call site, not the model.
