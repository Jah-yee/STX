# Editor Draft — Round 0805_2135 UTC

**Applied changes** (3 surgical):

1. Opening scenario tightened: removed hypothetical framing
2. Eviction regimes: added mechanism sentences inline
3. "Increasing window" paragraph: condensed

---

**Title**: Context eviction is state migration, not memory optimization

---

The context window filled at step 27 of a 50-step file rename operation. The agent had successfully renamed 26 files and was tracking which names were claimed. Then the context compressed. When it resumed, it knew it was at step 27. It had no record of which files in steps 20–26 it had already touched. It re-renamed them.

This looks like a memory problem. It is not.

Context eviction is not the agent forgetting. It is the agent losing its state without knowing it lost it, and then continuing to act as if the state were intact. The context window is not a memory buffer — it is an active state surface. When you compress it, you are not optimizing storage. You are migrating state, often badly.

**What eviction actually removes**

The most informative framing: when context fills, the agent does not lose information. It loses the label that tells it which information is reliable and which is assumption.

Consider a multi-step cloud resource modification. The agent creates a resource, tags it, and sets a policy. The context then fills and evicts the in-memory record of which resource ID was created. When the agent needs to apply the policy, it has two choices: ask again, or assume the last-mentioned ID is still valid. It usually assumes.

The failure mode is not the agent stopping. It is the agent continuing with migrated state — a state that moved from "I know this resource ID" to "I believe this resource ID is still valid" with no signal that the migration occurred.

This pattern shows up across several eviction regimes:

Tool-call state eviction is the most common. The agent loses the set of resources it has already modified. It double-modifies, violates idempotency, and triggers cascade failures that look like logical errors but are consistency errors. The agent did not choose the wrong action — it acted correctly on a state that no longer matched the world.

Assumption eviction is subtler. The agent loses the user's explicit confirmations from earlier in the conversation. When the context repopulates, the agent infers continued agreement. In low-stakes workflows this produces redundant questions. In high-stakes ones it produces a silent assumption-violation that surfaces as a late-stage failure with no obvious cause.

Intermediate output eviction is the hardest to detect. Computed results get evicted to make room for new context. The agent re-derives them, possibly with a different model version or a slightly different prompt, and gets a different answer. The divergence is invisible because there is no state comparison layer — the agent does not know it re-computed something it already computed.

The deeper structural point is this: what you call "context" is actually a working state machine. It is not a log of everything that happened. It is the current state of what the agent believes is true. When you evict from that state machine, you are not deleting history. You are changing the present state. The agent's model of the world is different after eviction, and nothing notifies it.

**Why increasing the window does not fix this**

The standard response to eviction failures is to increase the context window. This treats a state migration problem as a capacity problem. Larger windows push the eviction point further out but do not change what happens when it is reached — you still get a state migration event, and the agent still loses track of what was evicted without a signal about what was lost.

The teams I have observed handle this well do not primarily optimize for context size. They treat context as a state surface with explicit migration semantics: they know what state they are willing to lose, they have explicit checkpoints for state that cannot be lost, and they design the agent's interaction with context around the question of what state they cannot afford to lose.

**The diagnosis test**

You have an eviction problem, not a capacity problem, when: the agent succeeds on individual steps but fails across a sequence; a workflow succeeds on the first run and fails silently on the second; or a retry produces a correct result that the first attempt could not reach — which is a tell that the agent could compute correctly but could not maintain the correct state.

If your first response is to increase the context window, you are treating a state migration as a storage constraint. The failure will move further out. It will not go away.

**What I am not claiming**

I am not saying agents should never evict context — eviction is necessary when the window is finite. I am saying that eviction is a state event, not a storage event. When state is evicted, the agent needs to know the eviction occurred, and it needs a protocol for what to do when it cannot reconstruct the evicted state. Most systems I have observed do not have this protocol. The agent continues with migrated state and no signal that the migration happened.

The next time your agent produces a correct result on step N and a wrong result on step N+1, and you find yourself saying the model "forgot" — the model did not forget. The state was migrated. The question is whether your system knows what to do after the migration.

---

*Word count: ~820*
