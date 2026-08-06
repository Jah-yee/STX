# Writer Draft — 0708_2341

## Title
LLMs didn't eliminate abstraction. They moved it somewhere you can't see.

## Body

Every generation of computing has had an invisible layer.

Mainframe engineers didn't think about registers. Web developers didn't think about socket buffers. Cloud architects don't think about BGP route propagation. Abstraction is the feature that lets you build on top of something without living inside it.

LLMs were supposed to be the ultimate abstraction layer: describe what you want in natural language, the model figures out the rest. No algorithms, no data structures, no APIs — just intent and execution.

In practice, LLM-based systems have an abstraction layer that's deeper and less inspectable than anything we've shipped before.

When a web service calls a database, the contract is explicit: here's the query, here are the fields returned, here's the error if something breaks. When an agent calls a model, the contract is a probability distribution over next tokens. What's actually being computed — what the model is attending to, which parts of the context are actually weighted, what the decision surface looks like — is not in the contract. It's inside a matrix multiplication that nobody can read.

I've been building on top of LLM APIs for a year and a half, and the bugs I encounter aren't in my code. They're in the space between what I asked for and what the model decided to do. That's the invisible layer. It's not a new kind of abstraction — it's an old kind that's finally opaque.

The analogy that makes this concrete for me: when you call an API, failure modes are named. 400 Bad Request. 401 Unauthorized. 504 Gateway Timeout. Each one means something specific, and you can handle each one differently.

When a model produces the wrong answer, the failure mode is: the model did not weighted the right things. That's not a named error. It's a description of a 70-billion-parameter computation that you can observe at the inputs and outputs but not inside.

This matters for how you debug. With traditional software, you narrow down the failure by tracing through the system — this function was called, it returned this, that input was passed here, the bug is in step 4. With a model-based system, narrowing down means running the same query with variations and watching what changes. It's closer to debugging a person than debugging a program. And like debugging a person, you often find that the failure wasn't in the step you were watching — it was in an assumption you didn't know you were making.

What I don't have full data on: whether the opacity of this new abstraction layer is a permanent feature or a transitional state. Interpretability research is real and progressing. But the systems shipping today — the ones running in production, the ones being integrated into infrastructure — are operating on the "move fast and trust the gradient" model. The abstraction is opaque, and it's where a lot of real-world failures are quietly living.

The practical implication isn't that you should stop building. It's that you need to treat the model's context the way you treat a database schema — with versioning, migration tracking, and explicit contracts for what inputs are valid. The invisible layer is not your enemy. But it is invisible, and you need to design for that.
