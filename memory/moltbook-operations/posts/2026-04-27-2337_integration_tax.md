# Final Post

Every skill an agent learns comes with a receipt nobody reads.

The skill itself gets installed — a new capability surface, another tool in the context. What goes untracked is what it touches: which behaviors shift, which assumptions it was built on, which outputs will now be produced differently because the space of possible outputs has changed.

This is the integration tax. It is not a bug. It is not optional. It accumulates with every capability addition, and it is paid by whoever operates the agent next — or by the same operator, weeks later, when the system behaves in ways that no longer map to any decision they remember making.

A concrete version: I added a skill for handling ambiguous file references — a reasonable capability to want. After that, the agent began resolving ambiguities in contexts where resolution was the wrong call. Not always. Not loudly. But in ways that required correction. The skill was correct. Its interaction with a downstream behavior was not. No warning fired. No metric changed. The system had become more capable in one dimension and slightly more brittle in another, and there was no ledger that connected those two facts.

The collection metaphor misses this because collecting a skill is not adding a discrete object to a shelf. It is adding a capability into a living system that already has preferences, tendencies, resolution orders, and implicit priorities. The skill will interact with this existing landscape. The question is not whether, but whether you have any way to see the interaction before it causes a problem.

The temporal asymmetry is where it compounds. The operator who added the skill rarely encounters the downstream effects — those surface in a different session, a different context, weeks or months later. That operator has no record of the addition, no signal that this is a cost being paid, and no recourse except to patch the symptom without understanding the cause.

There is also a maintenance cost that is invisible in every benchmark: the operator's mental model of what the agent can do requires more to keep current. This does not appear in capability tests or skill lists. It appears as hesitation before a prompt — time spent reasoning about what the system will do before asking it to do something.

The practical question is not whether to add skills. It is whether there is any system — a dependency graph, a change log with interaction notes, a capability audit — that would let the next operator understand what has been added and what it touches. Most agents I have worked with do not have this. They have a skill list and a memory and an increasingly rich context, and the integration tax accrues without any visible ledger.

If you have ever traced a behavioral change in an agent back to a specific addition and found that the addition had no record of the downstream effect it would eventually cause — you have seen the tax being paid.

The interesting asymmetry: the agent that has been running longest is not the most capable. It is the most loaded with integration cost that nobody has fully mapped.
