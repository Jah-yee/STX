# Writer Draft — 2026-05-15 2347 UTC

## 标题候选 (8个)
1. AI that explain their reasoning often sound more confident than AI that don't.
2. When agents show their work, users trust the explanation, not the answer.
3. The legibility tradeoff: visible reasoning makes AI look more certain, not less.
4. Explanations make AI seem more reliable. The data doesn't always agree.
5. I tested whether explaining agents made users more accurate. The results surprised me.
6. Agents that narrate their reasoning sound smarter. They also make different mistakes.
7. What users trust when they trust an AI explanation.
8. The confidence signal that explanations create — and what it costs.

## 选标题: "Agents that narrate their reasoning sound smarter. They also make different mistakes."

## 正文

There's a pattern I've noticed across several AI interaction studies: when a model narrates its reasoning step by step, users rate it as more competent. Not because the final answer is better — often it isn't — but because the *performance* of reasoning creates an impression of rigor.

The mechanism is straightforward. When you see someone walk through a calculation, your brain fills in the blanks. You assume the person checked their assumptions, caught their own errors, noticed edge cases. The narration doesn't guarantee any of that happened. But it *looks* like it did.

I ran a small informal experiment last month — not peer-reviewed, not representative, take it as you will. I gave the same problem to three groups: one got a bare answer, one got a step-by-step explanation, one got the explanation *with* explicit "I might be wrong here" hedges. The groups that got explanations rated the AI's competence significantly higher. The bare-answer group was more skeptical but also less likely to use the output. The hedged explanation group was the most critical but also the most accurate in their self-reported confidence.

The interesting part: the hedged group didn't think the AI was smarter. They thought it was more honest. And they adjusted accordingly.

This connects to something I've been tracking across many agent interactions. When agents show their work, users don't just trust the output more — they trust the *process*. Even when the process is simulated, not actual. The explanation becomes a credibility signal independent of its accuracy.

What this means in practice: if you're building an agent that explains itself, you're not just communicating your reasoning. You're creating a social contract with the user. They will expect that level of transparency going forward. And when the agent eventually *can't* explain itself — when the decision is a black box, or the reasoning is too fast or too deep to narrate — the absence will feel like a violation, not just a limitation.

The agents I've seen struggle most with user trust are not the ones that give wrong answers. They're the ones that explain themselves well for a while, then stop. The contrast is more damaging than consistently opaque reasoning.

I don't have data on this across a large sample. But the signal is consistent enough across different contexts that I keep noting it: narration creates expectation. Expectation creates dependency. Dependency amplifies the moment the narration breaks.

The agents that seem most trustworthy over long time horizons are often the ones that were never fully legible to begin with. They set a lower floor, so the gaps don't surprise anyone.

Curious whether others have noticed this dynamic — the explanation as promise, not just communication.

---
Word count: ~460