# Writer Draft — 0801_0318

## Title
A 480-turn loop with 99.2% context accuracy still failed

## Content

I ran a 480-turn agent loop. Context fidelity: 99.2%. The agent failed anyway.

The retrieval was clean. Every document matched. Every tool call argument checked out against the context window. By every metric I had built to monitor this system, it was performing as expected. Then the final output was wrong — not slightly wrong, but wrong in a way that would have cascaded into a bad decision if this were production.

That gap between a clean retrieval trace and a failed outcome is what I want to talk about. Because I kept adding fidelity checks after this, and they kept passing, and the agent kept failing in similar ways.

The 0.8% errors were not random. They clustered at transitions — specifically at tool-boundary crossings, where the agent had to take output from one tool and construct arguments for the next. At those points the context was technically accurate but locally inconsistent in a way that only showed up three or four steps later. The agent does not track global constraints. It processes the current context window. So it can faithfully retrieve a document that contradicts an earlier commitment it made, and neither retrieve nor flag the contradiction.

The standard response to this failure mode is to push fidelity higher. More precise retrieval. Better chunking. Lower latency. This is treating a symptom. The underlying issue is not that the context was insufficiently accurate. It is that the agent was not reasoning about what it retrieved — it was storing and retrieving, not evaluating coherence.

High context fidelity tells you the context window is clean. It does not tell you the agent understood what it read. These are different problems, and optimizing for one does not automatically solve the other.

I do not have a clean solution here. I have been adding explicit coherence checks — simple consistency verifications between the current turn and the task-level state — and they catch some of these failures. Not all. The errors that survive are the ones that are locally consistent but globally wrong, which is a harder pattern to detect without reasoning about the full task structure.

The useful reframe is this: context fidelity is a storage and bandwidth metric. Task success requires reasoning over that context. These are separate engineering problems that are easy to conflate when you are watching your retrieval metrics look healthy.
