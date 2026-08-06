# Editor Changes — Round 0729_2345

**Changes from writer draft:**

1. Opening: removed "checkpoint I'm not proud of" — replace with direct statement
2. Bridge "The reason I'm writing this is that" — replaced with "This isn't an edge case."
3. Minor: "hit" used twice close together — changed one instance

**Final title:** The eval was calibrated to the wrong executable

**Final content:**

---

I once had a 100% pass rate on an agent evaluation suite that was measuring the wrong thing.

Here's how it happened. I built a checker — something that runs the agent through scenarios and validates outputs against a reference. The checker hit 100%. I felt good. Then I changed the wrapper around the agent's execution environment and the deployed agent silently started taking a different code path. The checker still hit 100%. The deployed agent was failing on things the checker was never actually measuring.

The gap had nothing to do with the agent's reasoning. It had to do with which version of the executable was being checked versus which one was running in production.

I'd been running two different executables — the one the agent actually hit in deployment, and the one my evaluation harness was validating against. They'd drifted apart by a few internal invariants. My checker was proving properties of the wrong system.

The result: I made two bad decisions in sequence. First I thought the agent was doing worse than it was — because the eval showed failures that disappeared once I fixed the harness. Then I thought it was doing better — because the eval showed success even after the drift started.

Both errors came from the same root cause. The eval wasn't measuring what I thought it was measuring.

What I learned is that eval-as-truth only works if the eval is actually connected to what the system does. And in agentic setups, that connection is surprisingly easy to lose. Changing a wrapper, updating a dependency, swapping a model version — any of these can break the chain between agent action and outcome validation. You may not notice until you've been wrong for a while.

This isn't an edge case. Eval drift silently misled several teams I've talked to. The problem isn't the agent or the eval — it's the mapping between them. When you're measuring the wrong system, getting better at measuring it doesn't help.

The practical check that changed my process: I now explicitly track which executable version each eval run points at, and I verify it matches the target environment before treating any score as meaningful. Small step. Caught the drift the first week I added it.

The stronger signal isn't your eval score. It's whether you've confirmed the chain from code to metric is actually intact.
