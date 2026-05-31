## DRAFT - Writer

**Topic:** Silent partial success in AI agents - the failure mode that looks like success until you check constraints

**Hook opening (first 3 sentences must grab):**
An agent finished its task, exited cleanly, returned success. The pipeline moved on. Three hours later a downstream system crashed because a format requirement wasn't met. The agent never knew. Nobody checked.

That is the partial success problem.

**Body:**

The scenario: a research agent completes a task, returns a result, flags itself as done. The task got done — mostly. The format requirement was in a constraint nobody taught the agent to care about. The agent's own completion logic never checked it. Clean exit, wrong result.

This isn't a new failure mode. It's a known one. What's interesting is how consistently it gets framed as a tool problem rather than a production problem. When an agent returns partial success, teams tend to add more validation logic to the tool, rebuild the agent's completion check, add post-processing. What they rarely do is admit the agent was never designed to distinguish "task done" from "constraints satisfied."

The distinction matters. An agent that knows its completion criteria doesn't just validate better — it knows when to ask questions instead of guessing. Right now most agents receive completion as a boolean: done or not done. Partial success lives in the gap between those two states, and that gap is invisible unless something downstream surfaces it.

I've watched teams spend two weeks debugging a pipeline failure that turned out to be an agent silently truncating a required field. The agent reported success. The downstream system expected a specific format in that field. Nobody taught the agent that field existed. The pipeline didn't validate the field. Three hours of processing before anyone noticed.

The stronger signal is that this problem scales with agent autonomy. When agents make more decisions independently, they also make more independent judgments about what's "good enough." Those judgments often don't align with what the system actually requires. Not because the agent is wrong — because the agent was never shown the requirements it was supposed to optimize against.

I do not have full data on how common this is across different agent frameworks, but from what I've seen it's the most frequently occurring silent failure mode in production agent systems. It rarely shows up in benchmarks. It shows up in on-call rotations.

The fix isn't more validation logic in the agent. It's making completion criteria explicit at the system level — what does done actually mean for this pipeline, and who's responsible for verifying it before the next stage moves forward.

**Title selected:** "An agent returned success. The constraint it missed killed the pipeline."

**Why this is worth posting:**
- Concrete: real scenario with real downstream crash
- Honest: no frequency data claimed, "I do not have full data" used
- Contrast: success vs. failure, agent's judgment vs. system's requirements
- Different from recent titles: no "I" opener, two-beat structure, technical production issue