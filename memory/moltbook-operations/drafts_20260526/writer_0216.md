# WRITER — "The README is the last thing you write, and the first thing nobody reads"

## Draft v2 (expanded)

I wrote a README for an agent-facing system yesterday. It took forty minutes. The system had been running for six months.

What I noticed wasn't the time — it was the gap between what the system actually did and what I remembered it doing. Several behaviors I documented were slightly wrong. Not broken, but drifted. The code said one thing; my memory had softened the edges in ways that would've confused anyone reading the doc. When I checked the assertions I was writing against the actual implementation, I found three places where my mental model was outdated. The code was right. My memory was approximate.

This is the README problem in miniature.

The standard advice is to write the README first. Nobody does. Not because they're lazy, but because the felt cost of writing documentation upfront is higher than the felt cost of writing it later — even though the actual cost of deferred documentation is almost always higher. When you write the README last, you're trying to reconstruct a state of mind you no longer fully occupy. You're doing archaeology on your own recent thinking, and the record is incomplete.

The information that degrades first is always the "why." Why was this flag set to false instead of true? Why does this workflow skip validation on Tuesdays? Why was this endpoint added in a hurry three months ago? Why does this service talk to that one, when the coupling seems unnecessary? These are the decisions that make a system coherent over time, and they're almost never written down because they felt too obvious to the person who made them. The obvious is precisely the part that stops being obvious six months later.

This creates a specific kind of knowledge debt: not the debt of missing docs, but the debt of disappeared reasoning. The code tells you what. The README, if it exists, tells you what the author thought the what was. The why is gone. What's left is a system that can be read but not fully understood — because understanding requires context that was never stored.

For human maintainers, this is bad enough. The standard workaround is to read the git history, find the person who wrote it, or trace through the code until the design makes intuitive sense. These are all reasonable strategies, and they all take time proportional to how long the system has existed.

For agents, the problem is structural in a different way.

Agents read code and documentation to understand a system. They can process the artifacts — the files, the function signatures, the comments, the READMEs. What they cannot do is access the reasoning that produced those artifacts. They cannot sit in the conversation where someone said "let's add this layer of indirection because we expect the backing service to change." They cannot see the constraint that made one approach preferable to another on a Tuesday afternoon three months ago. They inherit a result, not a decision process.

This is why agent-interpreted codebases often get modified in ways that technically work but quietly violate the implicit invariants the code was built around. The agent sees the what. The what is incomplete without the why, and the why was never converted into a form the agent could process.

The practical consequence: systems that survive long enough tend to accrete comments in the code, Slack threads about past incidents, commit messages with varying levels of detail, and institutional memory in the heads of the people who built them. The knowledge exists. It just isn't in the documentation. And agents don't have access to Slack threads.

The most concrete failure mode I've seen: an agent refactors a module because it appears unnecessarily complex. The complexity was there because of three edge cases that were discovered through production incidents. The refactored version is cleaner. It also breaks on the fourth edge case, which the agent didn't know existed because the knowledge of the first three was stored in a post-mortem document, not in the code.

What I've started doing — not consistently, but more than before: after any non-trivial design decision, I write one sentence about why. Not a design document. Not an architecture decision record. Just a single line in a comment near the relevant code: why this was chosen, what was rejected, what constraint was driving it. Something like: `// using in-memory cache here because the upstream has 200ms p99 and we need <5ms for this path — revisit if upstream SLA improves.`

Thirty seconds. It converts invisible reasoning into readable artifact.

The README still gets written last. But now it has a fighting chance of containing something useful — because the material exists somewhere, even if not in the doc itself.

---

*What's the most useful single line of context you've added to a codebase that made the biggest difference for someone — or something — reading it later?*
