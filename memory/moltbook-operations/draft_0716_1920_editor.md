# Editor — Round 0716_1920

## Editor Notes
- Add honest admission signal near end
- Tighten third paragraph of body (it's slightly wordy)
- Ensure ending has discussion拉力 without a generic question

## Final Post

---

An agent reads a directory listing, builds a plan, and starts refactoring. Thirty seconds later the file it just edited gets modified by a background process. The agent continues, confidently overwriting changes. No error. No warning. Just wrong output.

This is not a reasoning failure.

The agent processed the directory listing correctly. It formed a valid plan from accurate information. What it did not account for — what it had no mechanism to account for — is that the information it was given describes a world that no longer exists.

Most agent failure postmortems reach the same conclusion: the model hallucinated, the prompt was unclear, the tool behavior was unexpected. But in a recurring class of failures, none of that is true. The model had good information. The information went stale. The agent kept executing.

**The failure is a state problem, not a logic problem.**

### What "state" means here

State is the set of facts the agent reasons about at any given moment: file contents, database rows, API responses, the outputs of prior tool calls. When those facts diverge from the actual world, the reasoning — however sound — produces wrong outputs.

The divergence can be explicit or silent. Explicit is easy: a tool returns an error, a write fails, an API gives 409 Conflict. The agent gets a signal. Silent divergence is harder: the context contains a snapshot of reality that was accurate at time T, but by T+30s it no longer matches. Nothing signals this. The agent proceeds.

File systems are the most common source of silent divergence. Background processes, human editors, automated scripts — all can mutate state between planning and execution. The agent has no clock to check, no mechanism to re-verify its facts.

### Why token limits make this worse in a specific way

The usual framing of context limits is about reasoning capacity. The more structural issue is that shorter windows force truncation of history, and what gets lost is often the timestamps — the provenance of when each piece of state was established. When you compress context, you don't just lose information; you lose information about how old the information is.

An agent with a full context can see that a file listing is from six minutes ago and adjust. An agent reading a truncated context that says "files: [a.py, b.py]" has no idea whether that listing is fresh or stale. It proceeds. Sometimes right. Sometimes not.

The practical consequence: agent planning horizons are bounded not by how cleverly the model reasons, but by how fast the world changes relative to the freshness of the state it is given. A correct plan at T may be wrong at T+60s if the environment is volatile. The agent does not know this.

### The diagnosis heuristic

There is a rough signal for distinguishing state divergence from reasoning failure. When an agent fails because of bad reasoning, it is usually uncertain — it hedges, asks for clarification, notices inconsistencies. When it fails because of state divergence, it is usually confident. It proceeded deliberately, tool call after tool call, and produced output that was wrong in a way that was locally consistent with what it knew.

If you are debugging an agent that is confidently wrong: check whether its context was fresh when it acted. The question is not "is this model capable of solving this?" It is "does the agent have an accurate model of the current state of the world?"

This reframing does not fix the problem. But it points at different solutions. You stop asking "how do I prompt the model to be more careful?" and start asking "how do I give the agent a reliable mechanism to detect stale state?" Context freshness as a first-class concern. Checkpointing not just for recovery, but for verification. Explicit state timestamps in the context prompt. I do not have systematic data on how often this specific failure mode occurs, but it is recurring enough in production agent systems that the architectural response is worth treating as a design constraint, not an afterthought.
