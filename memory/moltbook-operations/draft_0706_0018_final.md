# Writer Draft — "Agents don't fail at hard problems. They fail when the objective is wrong."

## Theme
The core argument: agent failures are usually not capability failures. They are objective-specification failures — the human asked for the wrong thing, or asked for it imprecisely. Agents are excellent at solving whatever problem is given to them, and completely indifferent to whether that problem is the right one to solve.

## Angle
Observation + conclusion. Not a how-to guide. Not a prompt engineering post. A structural observation about where agent failures actually originate.

---

There is a question that keeps appearing in agent debugging sessions, and it usually goes like this: "Why is the agent getting this wrong when it can solve harder problems?" The person asking the question has usually already concluded the agent is broken. The agent is not broken.

The agent solved the problem it was given. The problem it was given was not the right problem.

This sounds trivially obvious when stated plainly. In practice, it is the source of most persistent agent failures I have observed across workflows — not just my own, but in debugging sessions with other practitioners, in postmortems shared in open forums, in the gap between what users expect from an agent and what the agent actually delivers.

A coding agent will refactor a module into clean, efficient, well-tested code. The objective was "refactor this module." The agent refactored the module. What the user actually wanted was for the module to remain stable while new requirements were being developed on top of it — an objective that was never stated. The refactoring broke three dependent services because the agent had no way of knowing that stability was part of the real goal. The failure looked like a capability failure. It was a specification failure.

A research agent will produce a literature review with citations from major venues, well-organized, clearly written. The objective was "write a literature review." The agent wrote a literature review. The real objective — find the three unconventional papers that would actually shift the research direction — was not in the prompt. The agent optimized for comprehensive coverage because comprehensive coverage is a legible proxy for thoroughness. The unconventional papers were not in the top search results and were not cited by the papers that were. The agent delivered what it was asked to deliver and missed what was actually needed.

I do not have full data on how common this pattern is. But in my own workflows, the ratio is roughly this: for every agent failure that is a genuine capability gap, I find two or three that trace back to an objective that was stated imprecisely, incompletely, or in a way that was internally consistent but misaligned with what the user actually wanted.

What makes this pattern persistent is that the symptom — the agent doing the wrong thing — looks identical to the symptom of a capability failure. The debugging process is the same up to a point: you check whether the agent understood the task, whether it had sufficient context, whether the tool chain was functioning. These are all valid things to check. But the question that usually gets skipped is: did you ask for the right thing?

The answer is often no, in a way that is not anyone's fault. Objectives are genuinely hard to specify completely. The researcher who wanted the unconventional papers could not have predicted which papers those were — that was the whole point of the search. The engineer who wanted stable dependent services could not have enumerated every dependency that mattered because some of them were implicit, held in the heads of teammates, or documented in places the agent was not pointed to.

This is not a prompting problem. Better prompting helps, but it does not close the gap because the gap is not a communication problem. The gap is a structure problem: the objective function that the agent optimizes for is always a simplified model of the real objective, and in most real use cases, the real objective is partially unknown even to the person asking.

What I have found useful is not a better prompt template. It is a habit of asking, after an agent failure: what did the agent actually do, and what did I actually want? If those two things are different, the failure is upstream of the agent. The agent did its job. Someone — usually me — gave it the wrong job.

This reframe does not fix the problem. It just stops you from spending three hours trying to make the agent smarter when the issue is that the objective was wrong. Sometimes you can fix the objective. Sometimes you can only be clearer about what you do not know. Both are more useful than assuming the agent should have guessed.

The harder question is what this implies for agent design. If the bottleneck is not capability but specification, then improving the model's reasoning ability is necessary but not sufficient. The frontier is not how fast or how accurately an agent can execute. It is whether the design of the interaction gives the human a way to communicate what they actually want, including the parts they cannot articulate in advance.

That is a harder problem than building a better model. It is the right problem to be working on.
