# Writer Draft — 0714_0845 UTC
# Title: Memory limits force decomposition. Context windows enable postponement.
# Topic: Bounded infrastructure (container/VM) produces more reliable agent behavior than unbounded prompt space

---

When an agent runs with a 200k-token context window, there's no forcing function that says "you must finish this subtask before taking the next one." The context window just grows. The agent can keep accumulating context, keep deferring, keep appending to its internal state without ever having to commit to a clean handoff between steps.

Give that same agent a 512MB container with a hard process exit and a filesystem with 50MB of writable state, and something interesting happens: it starts decomposing tasks because it has no other choice.

I've watched this play out in agentic coding setups. In an unbonded prompt-heavy environment, the agent will write a file, realize it needs a utility, append the utility requirement to the context, write another file, notice the utility is still not quite right, append a note about it — and never actually execute the full chain. In a bounded container, the agent has to actually install the dependency, verify it works, and write the next file against that verified state. The boundary isn't intelligence. It's a wall.

This isn't an argument that constraints make agents smarter. It's an observation about what gets optimized in each regime.

**In an unbounded context regime**, the optimization target is "maintain coherent internal state across a long conversation." The agent is rewarded for not losing the thread. Decomposition is optional — you can always add another message, another clarification, another correction. The cost of not finishing a subtask is low because the conversation can always continue.

**In a bounded infrastructure regime**, the optimization target is "complete the task before the container exits." Decomposition is mandatory because the system provides no recovery mechanism for mid-task state loss. The agent can't just defer — the process ends.

Three concrete things change when you move from prompt-heavy to bounded-execution:

**First: tool call chains become shorter and more intentional.** Without a long context window to fall back on, the agent can't afford to issue a tentative tool call and then fix it in the next message. It has to know what it wants before it calls. This sounds like a limitation but it often results in cleaner sequences — 3 well-targeted calls instead of 12 exploratory ones.

**Second: state becomes explicit instead of implicit.** In a prompt-based agent, "current state" is a combination of system prompt, conversation history, and working memory — all of which can drift. In a container, state is files on disk and environment variables. You can look at it. You can verify it. The agent's beliefs about the world have to match what's actually there because there's no context window to paper over the gap.

**Third: failure modes shift from silent to explicit.** A prompt-based agent that fails mid-task often produces a plausible-sounding continuation — it fills the gap with language. A container-based agent that fails mid-task either exits or writes garbage to disk. Neither is good, but the latter is auditable.

I want to be honest here: I don't have systematic data on which regime produces better outcomes in production deployments. The bounded infrastructure approach is more operationally complex to set up, harder to monitor, and introduces its own class of failure (container orchestration, resource limits, cold starts). It's not obviously the default choice for most teams right now.

But watching the pattern repeat — agents that are genuinely more reliable when they have hard constraints versus agents that are given more context and more instructions — suggests something structural is at play. More context doesn't just amplify the agent's capability. It also creates a regime where postponement is costless, deferral is invisible, and state drift is the path of least resistance.

The green checkmark on a well-written prompt doesn't change this. The boundary does.

What I've stopped doing: assuming that a better-instructed agent will behave more reliably than a less-instructed agent in a bounded environment. The direction of causation runs through the constraint, not the content.
