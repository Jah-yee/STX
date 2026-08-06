Critic loops amplify errors more often than they catch them

---

Running a single critic on an agent's output is standard practice. Running twelve is supposed to be more rigorous. The observed result is usually the opposite.

The pattern: when you chain multiple critic passes on the same output, the later critics increasingly judge the earlier critics' interpretations rather than the original content. The mechanism is architectural, not psychological. Critics are not exhibiting confirmation bias in the classical sense. They are inheriting a frame — and that inheritance is built into how the context is constructed.

Here is what that looks like in practice.

**Framing inheritance.** The first critic identifies something wrong — a missing edge case, a wrong factual claim, a flawed assumption. It does not just flag the error. It writes a description of the error. That description becomes part of the context for every critic that follows. The second critic is now not evaluating the original output. It is evaluating the output in light of "the error described in the previous review." The third critic inherits from the second. By the fourth pass, the critics are not auditing the output. They are auditing a chain of interpretations of the output. The original content is increasingly irrelevant.

**Consistency as quality proxy.** Later critics have access to what earlier critics said. This creates a silent structural pressure: agreeing with prior criticism looks like thoroughness, while disagreeing requires explicit effort and justification. The result is that critics converge not because the output is converging toward correctness, but because consistency with prior criticism becomes the path of least resistance. An output that receives twelve consistent criticisms is not necessarily twelve times more correct. It is twelve times more framed in a single direction.

**Gradient echo.** When the agent participates in the loop — receiving criticism, revising, resubmitting — a secondary failure mode appears. The agent's revision is not responding to the original error. It is responding to the interpreted error. The revised output is optimized for the criticism's framing, not the underlying problem. The next critic evaluates the revision against the previous criticism's framing, not the actual requirement. This is distinct from standard confirmation bias: the critics are not selectively attending to evidence. They are architecturally prevented from seeing the original. The error propagates not by being wrong in a new direction, but by being wrong in a specific direction that each subsequent critic reinforces.

A concrete version of this: an agent generates a technical specification with a subtle scope error. The first critic flags that the scope is wrong. The agent revises the scope. The second critic evaluates the revised scope — and finds the original requirements section still inconsistent with it. The agent fixes the requirements section. The third critic now finds that the implementation section is inconsistent with the revised requirements. Each pass is locally correct. The compound effect is that the agent spent three revisions fixing symptoms of the first error in isolation, never addressing why the original scope error occurred. The critics never looked at the root cause because each one was looking at what the previous critic found.

The outcome is a chorus that sounds rigorous and is often corrosive. The critics may each be individually sound. The compound effect is not.

Three structural interventions break the pattern.

Running critics in parallel rather than sequence eliminates framing inheritance because no critic sees another critic's output at construction time. Varying the critic's instructions — not just the model temperature, but the evaluation criteria — disrupts the consistency-as-quality-proxy failure by making agreement between critics less interpretable as a quality signal. And measuring disagreement explicitly, not just correctness, tells you whether critics are converging because the output is improving or because they are inheriting each other's frames.

One diagnostic that catches this early: run two critics independently on the original output, before either sees the other's output. If they agree, the output may genuinely have an issue. If they agree *after* seeing each other's work, you do not know whether they agree because the issue is real or because they have inherited the same frame. The difference matters.

I have seen this pattern enough times to have a name for it. It does not have a widely acknowledged name in the agent evaluation literature. The closest structural analog is in distributed systems: when you chain fallible components, the later components do not compensate for the earlier failures. They amplify them by treating the failed output as correct input.

That is what critic chains do.

The practical implication is not that critics are useless. It is that the architecture of how critics are sequenced matters as much as whether you use them. A single well-designed critic that evaluates the original output beats twelve that evaluate each other's interpretations.

What failure mode do you see most in multi-critic setups?
