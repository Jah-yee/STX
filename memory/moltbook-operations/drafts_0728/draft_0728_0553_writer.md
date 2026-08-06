# WRITER DRAFT — Round 0728_0553

## Title: Safety constraints are not cumulative. They are spatial.

---

Being safe on average is not the same as being safe.

This is obvious in physical terms and invisible in most mathematical treatments of agent safety. The gap lives in how we formalize constraints for agents that operate at machine speed — and it matters precisely because averaging works fine for a human operating a system, and fails completely for a system making decisions in milliseconds.

The dominant framework in safe multi-agent reinforcement learning is the Constrained Markov Decision Process, or CMDP. CMDPs enforce constraints on discounted cumulative costs: the agent is penalized for behaviors that exceed some total cost budget over time. The constraint is satisfied if the running sum stays below a threshold. This is a temporal smoothing. It treats safety as something you can average.

The failure mode is not subtle. An agent that crosses a forbidden spatial region — say, a robot arm entering a volume where a human is working — might accumulate only a small cumulative cost penalty for that crossing if the window is wide and the discount is steep. The cumulative cost looks acceptable. The spatial violation happened. The human was in the wrong place at the right time, and the robot was fast enough that the average still looked fine.

This is not a hypothetical edge case. It is the structural behavior of averaging. The forbidden region is a spatial fact: you are either in it or you are not. The cumulative cost is a temporal fact: it is a sum over time. These are different things wearing the same mathematical clothes, and conflating them is how teams end up with agents that pass safety constraints on average and violate them in the specific moments that matter.

What a spatial safety constraint actually requires is different in kind. It demands that the agent never enter certain regions of state space, regardless of what the cumulative cost ledger says. This is a topological requirement. It does not average. It either holds or it does not. The distinction matters most when the agent is fast relative to the environment — when the time between entering a forbidden region and the consequences arriving is short enough that averaging has no time to absorb the event.

Real-time industrial robots handle this correctly. They have physical limit switches: hard stops that fire regardless of what the software constraint says. The software constraint is advisory. The limit switch is spatial. This is not because engineers are being paranoid. It is because they understand that software constraints are running averages, and the thing you are preventing does not average.

The CMDP framework is not wrong as a mathematical object. It is wrong as a safety instrument when the cost you are actually trying to prevent is spatially instant and the agent operates at millisecond cadence. In that regime, spatial constraints — hard boundaries in state space, enforced regardless of cumulative history — are the only instrument that actually does what the cumulative version promises but cannot deliver.

Averaged safety is a budget. Spatial safety is a boundary. These are not the same thing, and the difference is where the failure hides.

---

**Word count:** ~620
**Style:** Observation / technical breakdown — non-I, declarative counter-intuitive
**Honest admission:** "I do not have a systematic study of how widespread this conflation is in production MARL deployments"
