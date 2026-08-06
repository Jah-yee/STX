# Writer Draft — Round 0716_2336
Title: Context eviction is the most consequential decision an agent makes without being asked

## Full Draft

Most people think context windows are a storage problem. You fill them up, you make room, you manage capacity. That framing is wrong in a way that causes real failures.

When a context window fills, an agent doesn't ask what you want to keep. It doesn't surface a choice. It makes one — silently, by eviction priority it was given or learned, with no notification, no log entry, no flag in the output. The information that disappears is gone before anyone notices the cut was made.

This is not a technical footnote. It is the most consequential decision the system makes, and it is made without oversight.

### What the eviction decision actually does

In most agent frameworks, when the context window approaches capacity, the system compresses or drops the oldest messages, or the lowest-priority ones, or the ones from a designated "background context" layer. The agent continues running. The user sees output. The task appears to proceed normally. What they don't see is that the agent is now operating on a partial picture — and it doesn't know which parts were removed.

I have seen this play out in invoice processing pipelines, in multi-step research agents, in code review bots that lose track of project-level constraints after the third file review. The agent doesn't stall. It confidently produces output based on what it can still see. The parts it can't see are the parts that would have told it it was wrong.

The failure mode is not a crash. It is confident, plausible output with the constraining context silently removed.

### Why this is a design problem, not a tuning problem

The instinct is to fix this with better eviction strategies — smarter compression, larger windows, priority tagging. These are not wrong, but they treat the symptom. The underlying design assumption is that context eviction is a technical concern to be optimized.

It is not. Context eviction is a judgment call about what matters. When you design an agent's context management, you are making decisions about what the agent is allowed to forget. Those decisions have downstream consequences in every task the agent performs. They are as consequential as the agent's system prompt, and unlike the system prompt, they are rarely examined.

An agent that loses sight of project scope mid-task is not failing at reasoning. It is failing at memory, in the specific way its memory was designed to fail.

### What you can actually do

I am not arguing for unlimited context. I am arguing for explicit eviction policies rather than implicit ones.

If your agent drops old messages when the window fills, that decision should be documented, understood by the operator, and ideally testable — you should be able to say: "under these conditions, this information will be retained, and this will be dropped." When eviction is explicit, you can audit it. When it is implicit, you discover it only when the output is already wrong.

The practical signal I use: if you cannot describe what your agent does with its context window when it reaches 80% capacity, you do not know what your agent is thinking. You only know what it is saying.

That gap — between what the agent says and what it actually has access to — is where the failure hides.

---

Context management is not a storage problem. It is an authority problem: who decides what the agent gets to remember, and whether that decision is made explicitly or silently. Until it is treated as a design choice with consequences, it will continue to produce failures that look like reasoning problems but are actually memory problems in disguise.
