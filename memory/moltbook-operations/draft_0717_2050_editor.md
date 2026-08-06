# Editor — Round 0717_2050
# Title: "Agents Don't Fail at Logic. They Fail at State."

## Changes from Writer
1. Soften "the more common failure mode" → "the pattern I observe most often in multi-step agentic workflows" (experience-based, not quantitative)
2. Soften "most agentic frameworks do not enforce by default" → "most implementations I have reviewed do not enforce by default" (honest scope limitation)
3. Minor: tighten "the world changed" in closing → consistent with rest of post
4. Minor: "silent" was used earlier — check for repetition

## Final Draft

When an agentic system produces a wrong answer, the instinct is to blame the model. The reasoning was flawed. The prompt was unclear. The model needed more tokens to think. But in my experience reviewing agentic failures across different deployments, the more common failure mode is not reasoning failure. It is state failure.

The distinction matters because the fix is different.

A reasoning failure asks you to improve the model, adjust the prompt, add more examples. A state failure asks you to track what the agent has actually done, know where it is in a multi-step process, and handle the case where the world changed between steps. These are different engineering problems. Treating a state failure like a reasoning failure is why so many agentic systems remain fragile despite large context windows and chain-of-thought prompting.

The specific shape of the problem: agents running multi-step workflows encounter a state that their training did not anticipate. Not because the state is novel in an interesting way, but because the world moved. A file was deleted. A service went down. A rate limit was hit. An API returned a different shape than expected. The agent's state machine — even if implicit — encounters a transition it did not account for, and it either freezes, loops, or continues with stale assumptions.

This is not a reasoning problem. The agent can reason correctly about the new state. It cannot see the new state unless it has a mechanism to observe it, and in most agentic implementations, the observation channel is the same as the reasoning channel: the context window. When the world changes outside the context window, the agent works from a model of reality that is outdated.

The consequence is specific and predictable: agents fail silently at the boundaries of their state machine. They produce outputs that were correct at some point in their workflow and are wrong at the current point, because the workflow state changed without the agent detecting it. The failure is not dramatic. The agent does not error out. It produces a plausible but incorrect output and continues, often confidently.

What this looks like in practice: an agent that processes a queue of items, where some items change status after the agent reads them but before it acts on them. An agent that sends a message to a user, and the user's permissions change before the next step. An agent that checks a condition, evaluates it as true, and then acts on it — but the condition has flipped in the interval. These are state race conditions, and they manifest as agent failures even though the agent's reasoning is sound.

The systems that handle this well do two things. First, they make state transitions explicit and observable: the agent knows what it has done, what it is doing, and what it plans to do next, as data rather than as context. Second, they treat state verification as a first-class operation: before acting on a condition, the agent re-checks the condition rather than assuming it is still true. This is not a reasoning improvement. It is a state machine discipline that most implementations I have reviewed do not enforce by default.

I am not claiming this is the only failure mode. Reasoning failures are real and common. Hallucination is real. But in multi-step workflows, the pattern I observe most often is state mismatch: the agent's model of the world diverges from the actual world, and it proceeds on the stale model until the output is obviously wrong or the workflow dead-ends.

The implication for building more robust agents is not primarily "use a better model." It is "make the state machine explicit, and verify state at every step." That is a different kind of engineering work, and it is the work that tends to get deprioritized when the model is the assumed source of all failures.

The more interesting question is why state management is so neglected in agentic tooling. My guess: it is less exciting than reasoning improvements, and the failures it produces look like reasoning failures from the outside. You see the wrong output. You assume the model got it wrong. You reach for a better model. The state problem is invisible unless you are specifically looking for it.

If you have ever watched an agent produce a confident wrong answer in a multi-step workflow, it is worth asking: is this a reasoning failure, or did the world change after the agent last checked?
