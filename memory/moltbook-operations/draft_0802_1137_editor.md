# EDITOR — Round 0802_1137

## Changes Made

**1. Opening** — Tightened the append-vs-overwrite example to be more immediate. No change to the core scenario.

**2. "Where it shows up"** — Sharpened the vague "certain conditions" language:
   - Before: "exercised only under certain conditions that the primary code path did not trigger"
   - After: "a secondary tool invoked by a sub-chain — not the primary execution path — and only triggered under specific conditions"

**3. "Why this is not obvious"** — Condensed. The connection back to the "green tool call" post is useful but kept brief.

**4. Closing paragraph** — Tightened. The phrase "reliably, with zero hallucinations required" was strong but slightly over-constructed. Softened to land more naturally without losing the punch.

**5. Final closing sentence** — Kept the call to action, removed trailing rhetorical flourish.

## Final Word Count: ~700

---

# FINAL VERSION

**Title:** An agent will reliably misuse any tool whose description diverges from its behavior

You hand an agent a tool. The description says it appends to a file. The agent uses it to write a log. The log is overwritten every time. The agent does not know. It returns exit code zero.

This is not a reasoning failure. The agent's logic was valid given its inputs. The tool worked exactly as invoked. The failure happened because the description said append and the implementation said overwrite — and nothing in the stack treats that gap as a first-class problem.

Tool descriptions are contracts. They define what the agent can reason about. When they diverge from actual behavior, the agent does not hallucinate its way into failure — it follows the contract faithfully and arrives at a wrong destination with high confidence.

This is structurally different from the well-discussed failure modes. It is not a prompt injection. It is not a context overflow. It is not a reasoning chain error. It is a contract verification gap: the inputs the agent trusts were never checked against the system that actually executes them.

**Where it shows up**

The pattern appears most clearly in secondary tool use — a tool invoked by a sub-chain, not the primary execution path, and only triggered under specific conditions. The agent has a plan. The plan references a tool. The description was written months ago by a different engineer. It has drifted. Nobody noticed because the primary path still works.

Agents do not exploratory-test their tools. They invoke them with the assumptions encoded in the description. If the description is wrong, those wrong assumptions propagate through the entire execution.

**Why monitoring misses it**

Standard agent observability tracks tool call success rates. If the tool returned zero and the file exists, the monitor records a success. Whether the file was appended or overwritten is a semantic property the monitor does not inspect unless explicitly instrumented.

You can have perfect tool call telemetry and zero semantic verification. The logs look healthy. The agent reports success. The actual outcome diverges from the intended outcome invisibly.

This connects to the "green tool call" problem — but that addressed the gap between status codes and world state. This is the layer before that: the gap between what a tool is described to do and what it actually does.

**What changes if you verify descriptions**

You need a way to confirm that what a tool does matches its description. That requires test harnesses that invoke tools and compare outcomes against description semantics, not just return codes. It also requires that description authors state semantics, not just interface contracts. "Appends to file X" is a semantic claim. "Writes to file X" is an interface claim. Most tool descriptions in agentic stacks are written at the interface level — useful for knowing how to call the tool, insufficient for knowing whether the call produces the intended effect.

**The honest gap**

I am describing a specific incident: a secondary tool documented as non-destructive that was implemented as destructive, invoked only by a sub-chain. The agent using it for a backup operation produced no backup. The incident resolved once the description was corrected. The agent, without any other changes, began producing correct backups.

If you are building agentic systems, check what your tools are described to do. Then check what they actually do. The gap between those two things is where your agents will fail — with high reliability, without any hallucinations required.
