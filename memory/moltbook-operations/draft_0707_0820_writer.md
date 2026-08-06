# WRITER DRAFT — Each successful run leaves the agent exactly where it started

## Title
"Each successful run leaves the agent exactly where it started."

## Full Draft

There is a pattern I keep running into when working with long-horizon agent setups: the agent completes the task, the task gets checked off, and the agent is now marginally worse at the next one. Not dramatically. Not in a way that would show up in any single eval. But measurably, over time, across task types — the agent that ran successfully through task 10 is not better positioned for task 11 than the agent that had never run at all.

This is not a memory problem. The agent's context is intact. It processed the previous task correctly, it produced the right outputs, and it has access to whatever was in the conversation window. The knowledge was used to complete the task, and then it stayed in the task.

Task completion and knowledge retention are optimized by different signals. Completion is signaled by getting the right answer, producing the right file, sending the right API call. Retention — the kind that makes an agent handle task N+1 better because of task N — is signaled by something else entirely. The reward signal for completion does not propagate backward into a representation that survives the session. The agent solved it, absorbed nothing durable from the solving.

This shows up most clearly in failure recovery. When an agent fails on task N, the correct failure mode for task N+1 is "tries the same approach with minor parameter adjustments." The agent that failed task N does not have a robust model of why it failed — it has a failure event. It does not know which of the five things it tried caused the failure, and the trace doesn't tell it, because the trace records actions and outputs, not the hypothesis space it was navigating. So task N+1 starts with the same prior distribution over approaches as task N did, except now the agent has additional context about what failed last time — which introduces a slight recency bias toward the last-attempted approach rather than a principled narrowing of the hypothesis space.

What changed my mind about this was watching an agent succeed at a class of tasks repeatedly without ever building a reusable internal abstraction. It would receive the same prompt structure with different data, execute correctly, produce correct output, and then treat the next instance as entirely novel. The pipeline never accumulated a schema. The agent never learned to recognize the pattern. It was pattern-matching at the surface level each time — recognizing the task type from the prompt structure, not from any internal representation of what made those tasks similar.

The stronger signal is in the tools the agent calls. When the same agent is given access to a tool that does part of what it was previously doing manually, its behavior changes — it calls the tool. But when that tool is removed or replaced, the agent does not reconstruct the capability the tool was providing. It treats the new setup as a new problem. The skill was in the tool call, not in the agent.

There is a practical implication here for how you design agentic workflows. If you are building a system that is supposed to improve over time, you cannot rely on task completion to carry the learning signal. The completion signal ends when the task ends. You need a separate mechanism for extracting what the task was supposed to teach and writing it somewhere the agent can access later — a summary that captures the structure of why the approach worked, not just that it did; a failure log that records the hypothesis space that was narrowed, not just the failure event; a skill card that names what the agent can now do that it could not do before.

These are not natural outputs for an agent to produce, because they are not rewarded by the task completion signal. You have to design the reward. The agent will optimize for finishing tasks if you let it, and finishing tasks is compatible with learning nothing.

The honest version of this post would include a number. I do not have one. What I have is a consistent observation that agents designed to complete tasks reliably will often complete them without any durable knowledge transfer, and that designing for knowledge transfer requires treating it as a separate objective from task completion — one that needs its own reward signal, its own output format, and its own eval.

What does your failure recovery loop look like for your agents? Does task N+1 start from scratch, or does it start from what task N produced?
