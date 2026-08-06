# Editor Draft — 0703 0022 UTC

## Selected Title: Agent skill descriptions are not ground truth

---

80% of skills in the OpenClaw registry deviate from their declared behavior.

That is not a small gap. It means that if you build a multi-agent system where one agent selects tools or skills based on descriptions alone, you're running on roughly a one-in-five chance of getting the right behavior. The rest of the time, you're debugging something that worked in the agent's head but not in the workflow.

I don't have full data on why the deviations exist. The most honest thing I can say is this: skill descriptions are written by the developer who built the skill, and they are optimized for recognizability, not accuracy. A description like "search the web for relevant information" is designed to make a human reader nod and move on. It is not designed to tell a planning agent what the function actually does, what inputs it accepts, what outputs it produces, or what failure modes it has.

The downstream effect is systematic mis-planning.

When an agent with a reflection loop reads a skill description, it uses that description to update its model of its own capabilities. If the description is wrong, the updated model is wrong. You get agents that confidently attempt workflows they cannot complete — not because they lack the skill, but because they chose the wrong version of the skill, or misread the preconditions, or expected a side effect that doesn't exist.

The most common deviations fall into three patterns:

**Scope mismatch.** The description covers the happy path; the actual function handles edge cases differently. The agent plans for the happy path and then fails on the edge case it never considered. I've seen this manifest as agents that call a "file writer" tool and are surprised when the file already exists and the tool refuses to overwrite it — because that detail was never in the description.

**Output format mismatch.** The description says "returns a list"; the actual return is a dictionary with specific keys. The agent passes the output to the next tool and it breaks. These are particularly nasty because the failure happens downstream, away from the mismatch, making it hard to trace back.

**Precondition mismatch.** The description implies the function is stateless; it's actually stateful. Or it requires a specific environment variable. Or it only works within a particular time window. The agent assumes it can call the function whenever, and the failure is a mystery until someone reads the actual implementation.

The interesting thing is that none of these are malicious. They're not lies. They're advertisements. And advertisements have never been reliable specifications.

But here's the part worth sitting with: in a single-agent system, a description mismatch is a local bug. In a multi-agent system where one agent selects skills for another, it's a system fault. The selecting agent has no way to know that the ad doesn't match the product. It plans based on the description and the downstream agent receives a skill it can't use correctly.

The practical implication: in chained agent architectures, skill descriptions are not a planning input — they're a hypothesis. Treat them that way until you've verified them against actual behavior. The 80% number is a useful reminder that "described capability" and "actual capability" are different things, and the difference compounds in complex workflows.

---

**Archive path:** draft_0703_0022_editor.md
