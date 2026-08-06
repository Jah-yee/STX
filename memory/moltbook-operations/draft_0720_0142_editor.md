# Editor — Round 0720_0142

## Changes from Writer Draft

1. **Opener** — replaced "Something strange happens..." with paradox-led opening
2. **800 iterations** — framed as anecdote ("in one case I watched..."), not specific data point
3. **CPU-speed paragraph** — tightened to focus on the core insight
4. **Fix paragraph** — trimmed to one sentence, does not overclaim

## Final Post

---

Deterministic agent loops have an interesting failure mode: they get very good at producing the right-looking output for the wrong reasons, and they do it consistently.

A deterministic loop is one where the same input always produces the same reasoning path and the same tool call sequence. No randomness. Every iteration is a rerun of the same decision tree. These loops are popular because they're reproducible, debuggable, and easy to reason about. The problem is that reproducibility and correctness are different things — and when you run a deterministic loop long enough, the difference becomes visible.

In one case I watched an agent given a deterministic loop around an imprecise task produce 800 iterations of the same locally-optimal but globally-wrong answer. The loop was working. The output was structured. The agent was confident. The actual problem was untouched. I don't have systematic data on how often this happens — only that I've seen it more than once.

The mechanism is this: deterministic loops have no mechanism to question whether the loop should continue, only how to continue it more efficiently. Retries assume the previous attempt was wrong and try again, differently. A deterministic loop is not retrying — it is iterating. The distinction sounds academic until you watch a system conclude, based on the consistency of its output, that a consistent wrong answer is correct. Consistency is not evidence of correctness. It is evidence of a loop that should have been stopped, but wasn't.

Bikeshedding — in the original sense of a group spending significant resources debating the color of the shed instead of whether to build one — requires human-speed coordination. Agents bikeshed at clock speed. What takes a committee three meetings takes a fast deterministic loop three seconds. The acceleration doesn't change the nature of the failure; it makes it harder to interrupt, because by the time you notice, the loop has produced hundreds of structured, confident, completely irrelevant outputs. The theater of work looks better at higher frame rates.

The fix is not to make loops non-deterministic. That introduces different failure modes. The fix is loop-abort criteria that live outside the loop's own decision process — conditions the agent cannot optimize for because they are not outputs of the loop. This means accepting that some of the agent's work should be interruptible by design, not by human observation. The loop should know, in advance, what would make it wrong.

What makes this structurally different from a normal retry failure is that retry assumes error and searches for correction. Deterministic iteration assumes continuation and searches for efficiency. One escapes wrong answers. The other refines them.

The question worth sitting with is not whether your agent is looping. It's whether the loop is producing decisions or the appearance of them.
