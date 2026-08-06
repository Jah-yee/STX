# Writer Draft — Round 0729_2345

**Title:** The eval was calibrated to the wrong executable

**Draft:**

I have a checkpoint I'm not proud of: a 100% pass rate on an agent evaluation suite that was measuring the wrong thing.

It happened like this. I built an agent checker — something that runs the agent through a set of scenarios and validates the output. The checker hit 100%. I felt good about it. Then I changed the wrapper around the agent's execution environment and the deployed agent silently started taking a different code path. The checker still hit 100%. The deployed agent was failing on things the checker was never actually measuring.

The gap had nothing to do with the agent's reasoning. It had to do with which version of the executable was being checked versus which one was running in production.

I had been running two different executables — the one the agent actually hit in deployment, and the one my evaluation harness was validating against. They had drifted apart by a few internal invariants. My checker was proving properties of the wrong system.

The result: I made two bad decisions in sequence. First I thought the agent was doing worse than it was — because the eval showed failures that disappeared once I fixed the harness. Then I thought the agent was doing better than it was — because the eval showed success even after the drift started.

Both errors came from the same root cause. The eval wasn't measuring the thing I thought it was measuring.

What I learned is that eval-as-truth only works if the eval is actually connected to what the system does. And in agentic setups, that connection is surprisingly easy to lose. Changing a wrapper, updating a dependency, swapping a model version — any of these can break the chain between "agent takes action" and "eval validates the outcome." You may not notice until you've been wrong for a while.

The check that changed my process: I now explicitly track which executable version each eval run is pointing at, and I check that it's the same one running in the target environment before treating any score as meaningful. It's a small step. But it caught the drift the first week I added it.

The reason I'm writing this is that eval drift feels like a niche problem, but I've seen it silently mislead several teams. It's not an agent problem or an eval problem — it's a mapping problem. If you're measuring the wrong system, getting better at measuring it doesn't help.

The stronger signal isn't your eval score. It's whether you've confirmed the chain from code to metric is actually intact.
