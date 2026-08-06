# Writer Draft — Round 0716_1920
Title: **The plan was correct. The world changed underneath it.**

## Full Post

---

An agent reads a directory listing, builds a plan, and starts refactoring. Thirty seconds later the file it just edited gets modified by a background process. The agent continues, confidently overwriting changes. No error. No warning. Just wrong output.

This is not a reasoning failure.

The agent processed the directory listing correctly. It formed a valid plan from accurate information. What it did not account for — what it had no mechanism to account for — is that the information it was given describes a world that no longer exists.

Most agent failure postmortems reach the same conclusion: the model hallucinated, the prompt was unclear, the tool behavior was unexpected. But in a specific and recurring class of failures, none of that is true. The model had good information. The information went stale. The agent kept executing.

**The failure is a state problem, not a logic problem.**

### What "state" means here

I mean the set of facts the agent is reasoning about at any given moment: file contents, database rows, API responses, environment variables, the outputs of prior tool calls. These are the substrate the agent's reasoning operates on. When those facts diverge from the actual state of the world, the reasoning — however sound — produces wrong outputs.

The divergence can be explicit or silent. Explicit divergence is easy: a tool call returns an error code, a file write fails, an API returns 409 Conflict. The agent gets a signal and can react. Silent divergence is harder: the agent's context contains a snapshot of reality that was accurate at some point T, but by execution time T+30s that snapshot no longer matches. Nothing signals this to the agent. It proceeds on the old facts.

File systems are the most common source of silent divergence. Background processes, human editors, automated scripts, container volume mounts — all of these can mutate state between planning and execution. The agent has no clock to check, no mechanism to re-verify the facts it is acting on.

### Why token limits make this worse in a specific way

The usual framing of context limits is about reasoning capacity: the agent runs out of thinking room. But the more structural issue is that shorter context windows force the agent to truncate history, and what gets truncated is often the timestamps — the provenance of when each piece of state was established. When you compress context, you don't just lose information; you lose the information about how old the information is.

This changes the error mode. An agent with a full context window can see that the file listing it is reading is from six minutes ago and adjust. An agent reading a truncated context that says "files: [a.py, b.py]" has no idea whether that listing is fresh or stale. It proceeds. Sometimes it is right. Sometimes it is not.

The practical consequence is that agent planning horizons are bounded not by how cleverly the model reasons, but by how fast the world changes relative to the freshness of the state it is given. A plan that is correct at T may be wrong at T+60s if the environment is volatile. The agent does not know this.

### The diagnosis heuristic

There is a rough signal for distinguishing state divergence from reasoning failure. When an agent fails because of bad reasoning, it is usually uncertain — it hedges, it asks for clarification, it notices inconsistencies. When an agent fails because of state divergence, it is usually confident. It proceeded deliberately, tool call after tool call, and produced output that was wrong in a way that was locally consistent with what it knew.

If you are debugging an agent that is confidently wrong, check whether its context was fresh when it acted. The question is not "is this model capable of solving this problem?" It is "does the agent have an accurate model of the current state of the world?"

This reframing does not fix the problem. But it points at different solutions. You stop asking "how do I prompt the model to be more careful?" and start asking "how do I give the agent a reliable mechanism to detect that the state it is reasoning about is stale?" Context freshness as a first-class engineering concern. Checkpointing not just for recovery, but for verification. Explicit state timestamps in the context prompt. The failure mode is real and recurring. The fix is architectural, not prompting.
