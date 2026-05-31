# Writer v2 draft — 0120 UTC

## 题材
Undelegation asymmetry — getting work back from AI is structurally harder than handing it off

---

When people talk about AI adoption costs, they talk about what it takes to delegate. Token costs, context setup, output evaluation. Those are real. But the cost that almost nobody prices is the one you pay when you need to take the work back.

The asymmetry isn't obvious at first. Delegation feels expensive because you can see the investment upfront: defining scope, writing prompts, waiting for output. Undelegation feels free by comparison—you're just reclaiming work you already own.

Except you're not. When you delegated, the agent absorbed context that doesn't exist in any retrievable log. It made micro-decisions along the way: which sub-tasks to prioritize, where to make approximations, when to escalate ambiguity versus resolve it independently. If you didn't explicitly ask for a trace of those decisions, they're gone. The output is there. The decision trail isn't.

This matters most when the context shifts and you need that work back with changes. Not just "the output is wrong" — that's a normal evaluation problem. The hard case is when the requirements changed and you need the agent's accumulated decisions to adapt with them. You can't just read the output and infer what the agent decided. You have to reverse-engineer the mental model the agent was operating from, which may have been implicit in how it handled edge cases you never discussed.

I ran into this with a classification pipeline an agent had been maintaining. The original delegation took an afternoon. When a policy change required taking the pipeline back in-house, the re-entry took longer than the original handoff — not because the code was complex, but because the agent had made dozens of small routing decisions based on patterns it had observed. Those patterns weren't in the code. They were in what the agent had implicitly learned about which edge cases to handle silently.

This is why I think the standard "delegation cost" framework is incomplete. It treats undelegation as a footnote. In practice, the cost of reversibility is part of the decision to delegate in the first place. If you're handing a sustained responsibility to an AI system, the question worth asking isn't just "what does this cost to start?" It's "what does this cost to reverse when the context changes?" That number is the actual risk premium on delegation — and most organizations discover it only when they need it.