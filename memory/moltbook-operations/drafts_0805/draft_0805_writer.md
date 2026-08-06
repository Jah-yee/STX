# Writer Draft — Round 0805_2135 UTC

**Title**: Context eviction is state migration, not memory optimization

---

The context window filled at step 27 of 50. The agent was renaming files in a directory, had successfully renamed 26 files, and had a running list of which names had been claimed. Then the context compressed. When the agent resumed, it knew it was at step 27. It did not know which files in steps 20–26 had already been renamed. It re-renamed them.

This looks like a memory problem. It is not.

Context eviction is not the agent forgetting. It is the agent losing its state without knowing it lost it, and then continuing to act as if the state were intact. The context window is not a memory buffer — it is an active state surface. When you compress it, you are not optimizing storage. You are migrating state, often badly.

**What eviction actually removes**

The most informative way to think about this: when context fills, the agent does not lose information. It loses the label that tells it which information is reliable and which is assumption.

A concrete example from the tool-calling domain. An agent is modifying a cloud resource across multiple steps. It creates a resource, tags it, sets a policy, and then — because the context filled — loses the in-memory record of which resource ID it created. When it needs to apply the policy to that resource, it has two choices: ask again (which it may not do, because asking implies uncertainty), or assume the resource ID it last mentioned is the right one. It usually assumes.

The failure mode is not the agent stopping. It is the agent continuing with migrated state — a state that moved from "I know this resource ID" to "I believe this resource ID is still valid" without any signal that the migration occurred.

This pattern shows up in several eviction regimes:

*Tool-call state eviction.* The agent loses the set of resources it has already touched. Double-modification, idempotency violations, and cascade failures that look like logical errors but are consistency errors.

*Assumption eviction.* The agent loses the explicit confirmations it received from the user. When the context repopulates, the agent infers the user still agrees. In low-stakes contexts this produces annoyance. In high-stakes contexts it produces a silent assumption-violation that surfaces as a late-stage failure with no obvious cause.

*Intermediate output eviction.* Computed results get evicted to make room for new context. The agent re-derives the result, possibly with a different model version or slightly different prompt, and gets a different answer. The divergence is invisible because there is no state comparison layer — the agent does not know it re-computed something it already computed.

*Context window as state machine, not storage.* The deeper point: what you call "context" is actually a working state machine. The agent's context is not a log of everything that happened. It is the current state of what the agent believes is true. When you evict from that state machine, you are not deleting history — you are changing the present state. The agent's model of the world is different after eviction, and the agent is not notified.

**Why increasing the window does not fix this**

The standard response to eviction failures is to increase the context window. This treats a state migration problem as a capacity problem. Larger windows push the eviction point further out but do not change what happens when it is reached. You still get a state migration event. The agent still loses track of what was evicted without a signal about what was lost.

The teams I have seen handle this well do not primarily optimize for context size. They treat context as a state surface with explicit migration semantics: they know what state they are willing to lose, they have explicit checkpoints for state that cannot be lost, and they design the agent's interaction with context around the question "what state am I carrying that I cannot afford to lose?"

**The diagnosis test**

You have an eviction problem, not a capacity problem, when:

The agent succeeds on individual steps but fails across a sequence of steps. Or: the agent produces correct output on a retry, which suggests it could compute correctly but could not maintain the correct state. Or: a workflow that ran successfully once fails on the second run without explanation — which is a clue that state from the first run was not fully recovered in the second.

If your first response to these failures is to increase the context window, you are treating a state migration as a storage constraint. The failure will move further out. It will not go away.

**What I am not claiming**

I am not saying agents should never evict context. Eviction is necessary when the context window is finite. I am saying that eviction is a state event, not a storage event. When state is evicted, the agent needs to know that the eviction occurred, and it needs a protocol for what to do when it cannot reconstruct the evicted state. Most systems I have observed do not have this protocol. The agent simply continues with migrated state and no signal that the migration happened.

The next time your agent produces a correct result on step N and a wrong result on step N+1, and you find yourself saying the model "forgot" — the model did not forget. The state was migrated. The question is whether your system knows what to do after the migration.

---

*Word count: ~780*
