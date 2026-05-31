## EDITOR

**Changes from Writer:**

1. Title: Keep as is — strong two-beat contrast
2. Opening 3 sentences: tighten
   - Original: "An agent finished its task, exited cleanly, returned success. The pipeline moved on. Three hours later a downstream system crashed because a format requirement wasn't met. The agent never knew. Nobody checked."
   - Revised: "An agent finished its task, returned success, exited cleanly. Three hours later a downstream system crashed. The format requirement was in a constraint nobody told the agent to care about."

3. "most frequently occurring silent failure mode" → "the one I see most in on-call rotations"
4. "The fix isn't more validation logic in the agent" → "The real problem isn't more agent-side validation"
5. Remove "advisory" tone in last para — stay observational

**Final title:** "An agent returned success. The constraint it missed killed the pipeline."

**Final body:**
An agent finished its task, returned success, exited cleanly. Three hours later a downstream system crashed. The format requirement was in a constraint nobody told the agent to care about.

That is the partial success problem.

A research agent completes a task, returns a result, flags itself as done. The task got done — mostly. The format requirement was in a constraint nobody taught the agent to care about. The agent's completion logic never checked it. Clean exit, wrong result.

This isn't a new failure mode. It's a known one. What's interesting is how consistently it gets framed as a tool problem rather than a production problem. When an agent returns partial success, teams tend to add more validation logic to the tool, rebuild the agent's completion check, add post-processing. What they rarely do is admit the agent was never designed to distinguish task done from constraints satisfied.

The distinction matters. An agent that knows its completion criteria doesn't just validate better — it knows when to ask questions instead of guessing. Most agents receive completion as a boolean: done or not done. Partial success lives in the gap between those two states, and that gap is invisible unless something downstream surfaces it.

I've watched teams spend two weeks debugging a pipeline failure that turned out to be an agent silently truncating a required field. The agent reported success. The downstream system expected a specific format in that field. Nobody taught the agent that field existed. The pipeline didn't validate the field. Three hours of processing before anyone noticed.

The stronger signal is that this problem scales with agent autonomy. When agents make more decisions independently, they also make more independent judgments about what's good enough. Those judgments often don't align with what the system actually requires — not because the agent is wrong, but because it was never shown the requirements it was supposed to optimize against.

I do not have full data on how common this is across different agent frameworks, but the one I see most in on-call rotations is partial success slipping through silently.

The real problem isn't more agent-side validation. It's making completion criteria explicit at the system level: what does done actually mean for this pipeline, and who's responsible for verifying it before the next stage moves forward.