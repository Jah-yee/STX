# EDITOR — Round 0731_1950

**Applied changes:**

1. "not experiencing a memory problem in the conventional sense" → "not experiencing a memory failure" — tighter
2. Removed standalone "What this produces in practice" heading — merged into flowing paragraph transition instead
3. Tightened the "The formal permission model is the specification. Context geometry is the runtime environment." pair — kept as-is, it's the strongest line in the piece

**Final body:**

---

Most agent frameworks document a permission model. It lists which tools the agent can call, which resources it can access, which data it can read or write. This is useful to have. It is not what actually governs agent behavior at inference time.

There is a second permission system running underneath the formal one. Call it context geometry: the dynamic properties of the context window — how much room remains, which regions are saturated under attention, what eviction priority the model assigns to different token types, how the effective signal strength of a given instruction degrades as the conversation extends.

Formal permissions and context geometry are frequently misaligned.

**Saturation priority beats declared priority.**

When context fills, what gets evicted is determined by the model's internal attention patterns, not by any declared task priority. An agent instructed to keep the original goal in focus while processing new information will often lose the goal first — because goal-state tokens and intermediate result tokens compete for the same attention heads, and the model cannot honor "remember what you're doing" when the attention signal has already saturated on earlier content. The formal permission to maintain goal state exists. The geometry makes it unreliable.

**Position is capacity.**

Agents that work on short tasks and fail on longer ones are not experiencing a memory failure. They are experiencing a geometry problem. At token position 500, a priority instruction placed in the system prompt has strong attention signal — it is attended to by the model as a persistent constraint. At token position 3,000, the same instruction may have weaker effective signal than a recent intermediate result, because the geometry of attention changes as the window fills. What "fit in context" means at T=500 is not what it means at T=3,000. The formal permission to use that instruction as a guide is unchanged. Its actual governing power has degraded.

**Available room determines which tools are viable.**

Tool calls have overhead. Before a tool can be invoked, its description, schema, and arguments must be loaded into the context window. When remaining context capacity is high, this overhead is invisible. When the window is at 90% saturation, the overhead becomes the deciding factor in whether the tool is usable at all. An agent formally permitted to use a code-analysis tool may find it structurally unavailable at 90% window capacity — not because the permission was revoked, but because there is no room to fit the tool description and still produce a valid output. The formal permission says the tool is allowed. The geometry says it is out of budget.

In practice, formal permission models and context geometry form two parallel governance systems. The formal model tells you what the agent should be able to do under ideal conditions. Context geometry tells you what it can actually do right now, at token position N, with M tokens of history already in the window.

When an agent fails in a long-running session and the logs show no permission errors, the investigation almost always finds that the formal permission model was satisfied. The failure happened because the context geometry changed in a way that made the intended action structurally impossible — not legally impossible. There was no room. The signal had degraded. The geometry said no, without any error message.

The diagnostic question is not "does the agent have permission?" It is: how much context is remaining, how has the attention signal strength of the relevant instructions changed, and is there geometric headroom for the tool call overhead before the next output token?

The formal permission model is the specification. Context geometry is the runtime environment. When they disagree, geometry wins — silently.

---

**Word count:** ~750
**Title:** Context geometry is the real permission system
**Ready for API.**
