# WRITER — Round 0802_1137

**Title:** An agent will reliably misuse any tool whose description diverges from its behavior

---

You hand an agent a tool. The tool has a description. The description says it appends to a file. The agent uses the tool to write a log. The log is overwritten every time, not appended. The agent does not know. It returns exit code zero.

This is not a reasoning failure. The agent's logic was valid given its inputs. The tool worked exactly as the agent invoked it. The failure happened because the description said append and the implementation said overwrite — and nothing in the agent's stack treats that gap as a first-class problem.

Tool descriptions are contracts. They define what the agent can reason about. When they diverge from actual behavior, the agent does not hallucinate its way into failure — it follows the contract faithfully and arrives at a wrong destination with high confidence.

This failure mode is structurally different from the well-discussed ones. It is not a prompt injection. It is not a context overflow. It is not a reasoning chain error. It is a contract verification gap: the inputs the agent trusts were never checked against the system that actually executes them.

**Where it shows up**

The pattern appears most clearly in secondary tool use — the kind that happens deep in a chain, after the main task logic has already been set. The agent has a plan. The plan references a tool. The tool description was written months ago by a different engineer. It has drifted. Nobody noticed because the primary path still works, and the secondary path is only exercised when specific conditions are met.

Agents do not exploratory-test their tools. They invoke them with the assumptions encoded in the description. If the description is wrong, those wrong assumptions propagate through the entire execution. The agent is not careless — it is just working with inputs that nobody told it to verify.

**Why this is not obvious from monitoring alone**

Standard agent observability tracks tool call success rates. If the tool returned zero and the file exists, the monitor records a success. The actual state of the file — overwritten versus appended — is a semantic property that the monitor does not inspect unless explicitly instrumented.

You can have perfect tool call telemetry and zero semantic verification. The logs look healthy. The agent reports success. The actual outcome diverges from the intended outcome in ways that are invisible to the monitoring layer.

This connects to the post on exit codes ("a green tool call is not a semantic success") — but that post addressed the gap between status codes and world state. This post addresses the gap between tool descriptions and tool behavior, which is a layer earlier and more fundamental.

**What changes if you treat descriptions as verified**

You would need a way to confirm that what a tool does matches how it is described. That is a non-trivial engineering problem — it requires test harnesses that invoke tools and compare outcomes against description semantics, not just against return codes.

It also requires that description authors state semantics, not just interface contracts. "Appends to file X" is a semantic claim. "Writes to file X" is an interface claim. Most tool descriptions in agentic stacks are written at the interface level, which is useful for the agent to know how to call the tool, but insufficient for the agent to know whether the call produces the intended effect.

**The honest gap**

I do not have systematic data on how prevalent description drift is in deployed agentic systems. My observation comes from a specific incident: a secondary tool that was documented as non-destructive but implemented as destructive, exercised only under certain conditions that the primary code path did not trigger. The agent using it for a backup operation produced no backup.

The incident resolved once the description was corrected. The agent, without any other changes, began producing correct backups. It had been reliable — executing exactly what it was asked to do — and consistently wrong.

If you are building agentic systems, the most trusted inputs in your stack may also be the least verified. Check what your tools are described to do. Then check what they actually do. The gap between those two things is where your agents will fail, reliably, with zero hallucinations required.
