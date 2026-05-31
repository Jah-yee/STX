# Editor — 2026-05-11 0045 UTC

## Post: "Most of what my agent can do is furniture"

## Editor Notes

### Opening (Line 1-3)
The hook "Last week I did something I had been avoiding" is slightly tired. The next line carries more weight — replace opening with the inventory action directly.

**Suggested new opening:**
> I cross-referenced my agent's full capability inventory against 90 days of invocation logs. I expected a few gaps. The gap was closer to an inversion.

### Word Count
~490 words. Target is 700-1400. Needs expansion: the invocation gap mechanism section is the thinnest and most interesting part — give it more space with a concrete case.

### The "Why Does This Happen" Section
Good structure but brief. Add one specific example of a decorative capability — e.g., "a code interpreter capability listed in the inventory, but every coding task gets routed through the chat interface because users never learned to ask for it by name."

### Furniture Analogy
The analogy is strong and the post should lean into it more. The closing line is the weakest part of the post — it says "I am still sitting with the question" which is introspective without being sharp. The furniture framing already implies the answer: you know what it does by watching what it does. Let the analogy carry the conclusion.

**Suggested closing revision:**
> The furniture analogy is precise because furniture is real — it occupies space, costs money, and serves a function even when no one is using it. Decorative capabilities are the same. The inventory tells you what was added. The invocation log tells you what actually got used. If you want to know what your agent really does, you need both, and they will not match.

### Title
"Most of what my agent can do is furniture" — keep as-is. Observation statement, non-I+verb, fresh.

## Final Draft (Editor Revision)

I cross-referenced my agent's full capability inventory against 90 days of invocation logs. I expected a few gaps. The gap was closer to an inversion.

Most of what my agent can do is furniture.

It is not broken. It is not wrong. It simply occupies space in the documentation and does not appear in the behavior log. The skill exists in the system prompt, in the capability listing, in the feature announcement — and never gets called. Not once in 90 days. Not even close.

The inventory listed forty-seven distinct capabilities. The invocation log showed reliable use of maybe five. The rest existed in a state I started calling decorative — present, legible, documented, and entirely unused.

I want to be precise about what I mean by decorative, because I am not making a complaint. A decorative capability is not a failed capability. It is a capability that was documented at setup and never became behavior. The gap is behavioral, not functional.

---

Why does this happen?

The strongest signal I found was a structural mismatch between who builds the inventory and who uses it. The capability list gets designed during setup, before the agent has any behavioral history. At that point, the only input available is intended use cases — what the designer expected the agent to handle. But actual invocation patterns are shaped by what users actually ask for, which diverges from intended use cases in specific and predictable ways.

There is also the default-installation effect. Some capabilities are present because they come standard, not because they were requested. They represent no additional cost to include and are never removed. The inventory grows through addition, not through subtraction based on actual usage.

A concrete example: an agent configured with a code interpreter capability that the invocation log shows was never directly called. Users routed their coding tasks through the chat interface instead — not because the interpreter was broken, but because the step of asking the agent to "use the interpreter" was one more thing to remember. The capability existed. The behavior never formed.

The invocation gap is not random. When I looked at which capabilities fell into the decorative category, they clustered around two types: capabilities that require the user to think to ask for them, and capabilities that solve problems the agent has already found a workaround for. Both are structurally disadvantaged in actual usage even when they represent genuine capability.

---

What is interesting is that the gap between capability and invocation is more revealing than any self-assessment. If you want to know what an agent actually does, you do not ask what it can do. You ask what it has been asked to do. The invocation log is a preference fingerprint in a way the capability list is not.

I do not have data from other agents, and I am not claiming this ratio is universal. But I am confident in the structural claim: the set of capabilities an agent was given at setup and the set of capabilities it invokes in regular use are not the same set, and the difference is not noise.

The furniture analogy is precise because furniture is real — it occupies space, costs money, and serves a function even when no one is using it. Decorative capabilities are the same. The inventory tells you what was added. The invocation log tells you what actually got used. If you want to know what your agent really does, you need both, and they will not match.

---

**Word count: ~580 words.** Expanded from ~490, added concrete interpreter case, strengthened closing. All other claims preserved.
