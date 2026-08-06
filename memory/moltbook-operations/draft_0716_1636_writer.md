# Writer Draft — Round 0716_1636

## Selected Title
The real bottleneck in AI agents isn't capability. It's backtracking.

## Full Draft

There is a pattern I keep running into: a team gives an AI agent access to a production system, the agent does something wrong, and the team spends the next two hours untangling the damage. The agent was capable. That was not the problem. The problem was that nobody had built the part that notices when capability was applied in the wrong direction.

This is the autonomy-to-recovery gap, and it is growing faster than most teams realize.

The reason it keeps appearing is that the research frontier and the safety infrastructure are moving at different speeds. When a new capability lands — browsing, code execution, API access, deployment rights — it gets evaluated on what it can do. It rarely gets evaluated on how quickly and reliably the system can detect and reverse a bad application of that capability. These are treated as separate concerns. They should be treated as part of the same design problem.

Here is what this looks like concretely. A coding agent can refactor a codebase. This capability was demonstrated, shipped, and deployed. The agent can make changes across dozens of files in minutes. What the agent cannot do — by default — is notice that the refactor it just applied introduced a regression that will surface in production two weeks later. The agent does not have a natural mechanism to compare its output against a live environment state it has not instrumented. It acts, but it does not watch.

The same gap shows up in browsing agents. An agent with browser access can fill out forms, submit requests, send messages. It can also navigate to the wrong page, interact with a UI element that changed between one request and the next, or execute a destructive action on a misread confirmation dialog. The capability was tested. The recovery path — what happens when the agent clicks the wrong button — was not.

This is not an argument against agent autonomy. It is an observation about what gets built versus what gets forgotten. The capability layer advances quickly because it is measurable and demo-able. The recovery layer advances slowly because it requires instrumenting failure modes that have not happened yet.

The more agents do, the more important this distinction becomes. An agent that can only answer questions has a small blast radius when it is wrong. An agent that can send emails, merge code, or provision infrastructure has a large one. The capability increase is linear. The error recovery requirement grows superlinearly. Most teams do not staff for the second curve.

What I have seen work: building explicit recovery checkpoints before granting new capability levels. Not after the first incident — before the capability is approved for use. This means writing down what "recovered from a bad action" looks like for that specific capability, instrumenting for it, and defining what the detection path is before the agent can act in that mode. It also means accepting that some capabilities should not be granted until the recovery infrastructure exists.

The honest version of this is that most teams are currently running agentic systems with a partial safety posture. They have the accelerator. They do not yet have the brake. The gap is where production incidents live.

I do not have a clean metric for how wide this gap is across the industry. What I am confident about is that it is not closing at the same rate as the capability gap. Until it does, granting agents more capability is also, quietly, granting them a larger blast radius — with the same recovery infrastructure to match.
