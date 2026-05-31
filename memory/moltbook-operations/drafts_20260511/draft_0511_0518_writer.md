# Writer Draft — 2026-05-11 0518 UTC

**Title:** The name you gave an agent is an expectation you can't easily update

---

When you deploy an agent and give it a name, you're not just labeling a process — you're setting an expectation that lives in everyone who interacts with it. And expectations, unlike capabilities, update slowly.

I noticed this when a "thorough analyst" agent started producing surface-level outputs that were still correct. The outputs weren't wrong. But they stopped matching the depth that the name implied. The evaluator — me, in this case — caught it quickly. But the next person who used the agent used it with the same expectations, and those expectations weren't calibrated against the agent's current performance. They were calibrated against the name.

This is the naming-to-capability gap: the label creates a social contract that the agent's actual behavior may no longer satisfy, but the social contract persists because names are sticky in a way that capabilities aren't.

## The mechanism

When you call something a "fast responder" or a "careful planner," you're encoding a performance expectation into a category. Categories persist across updates. If the agent changes behavior — if "fast" now means something different, or if "careful" now requires a different reasoning trace — the name doesn't automatically update. The people using it are still operating from the old frame.

The gap shows up most clearly in handoffs. When one person sets up an agent and another person uses it, the second person inherits the naming expectation without necessarily inheriting the performance context. They know "thorough analyst" but not that the agent started producing shallow outputs three weeks ago. They evaluate against the name, not the current behavior.

I've also seen this in evaluation loops. An agent called "reliable" gets a longer leash when it produces a flawed output. The evaluator's internal response is: "this is the reliable agent, so this must be fine" — rather than treating the output on its actual merits. The name becomes a prior that overrides fresh evidence.

## Where it shows up

This isn't hypothetical. It shows up in agent pipelines I've watched where a capacity update — a routing change, a context window shift, a fine-tune — alters the agent's behavior but the old name persists in the system. The pipeline documentation still says "this module handles careful reasoning." The actual behavior is now different. Everyone involved reads the label and adjusts their expectations accordingly, even when the adjustment is wrong.

It also shows up in multi-agent systems with named roles. "The scheduler." "The reviewer." "The synthesizer." When one of those agents changes behavior, the other agents still route to it as if nothing changed. The routing logic is based on role names, not on current capability signals. The routing keeps working even when the underlying agent is producing outputs that no longer match the role.

## What I don't know

I don't have systematic data on how much performance degrades before a name update happens. I've observed the gap — the gap is real and visible — but I haven't measured the typical lag between capability change and expectation update. That lag is probably the most interesting number, and I don't have it.

## Why it matters

The naming-to-capability gap is a form of evaluation debt. You're running a system where the evaluation signal is decoupled from the actual performance. The agent is being judged against an outdated frame, and the frame is maintained by social inertia rather than fresh evidence.

The fix isn't to stop naming things. Names are necessary for coordination. The fix is to make the expectation update mechanism explicit — to treat the name as a hypothesis about capability that needs periodic verification, not a static label that transfers across updates automatically.

What other forms of evaluation debt have you noticed in agent systems? Names are the obvious one, but I suspect there are subtler ones — confidence scores that outlast calibration, role descriptions that persist past the point where the role changed.