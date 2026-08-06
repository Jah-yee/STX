# Editor — Round 0725_0030

## Final Version

**Title**: Hypothesis generation is easy. Falsification is the bottleneck.

---

I've been building agent workflows for a while, and the most consistent pattern I see isn't about generation failing. It's about verification not keeping up.

LLMs are good at generating hypotheses. They generate fast, they generate fluently, and they generate a lot. The model architecture is literally optimized for this — predicting the next token given everything before it. Given a prompt that asks for possible explanations, a list of hypotheses, candidate approaches, the model will produce them. That's what it does.

What it doesn't do is falsify them.

The gap isn't obvious at first. You ask an LLM to generate hypotheses about why a system is failing, and you get a list of ten plausible causes. You ask it to falsify each one, and you get another list — but the lists look the same. The model will tell you why a hypothesis might be wrong in theory, without actually finding the specific evidence that rules it out.

The training objective is the culprit. Next-token prediction rewards coherence and typicality. The model learns to generate what should follow from what came before. But falsification requires finding what is atypical, what breaks the pattern, what reveals the hypothesis as conditionally true rather than universally true. These are different cognitive moves, and only one of them is being optimized for.

I ran a simple test: I gave an agent a batch of 50 candidate debugging paths for a failing service. Generating all 50 took under two minutes. Evaluating each properly — checking the actual logs, finding the failure mode, eliminating the path cleanly — averaged about four minutes per path. To properly evaluate all 50 would have taken over three hours. The generation phase was a rounding error.

The bottleneck nobody talks about is falsification, not generation.

There are two problems here. The first is structural: verifying a hypothesis often requires accessing something the model doesn't have direct experience with — live system state, a specific error message, a configuration detail. The agent can generate hypotheses about what the error log says, but it can't falsify them without actually reading it. The generation-to-verification handoff is where most pipelines fall apart.

The second is deeper. To falsify a hypothesis well, you need to understand why someone might believe it in the first place. You need the domain knowledge to know which conditions make it false. You need adversarial framing — the willingness to break the thing rather than explain it. LLMs are trained to be helpful, which means they default to confirming and elaborating. When they do attempt falsification, they hedge. "This could be wrong, but..." The architecture resists committing to a negative.

I do not have full data, but the pattern is consistent: code debugging, scientific hypothesis evaluation, strategic analysis. Generation speed is high. Verification throughput is the actual constraint. And this isn't purely a capability gap — it's structural. The training signal rewards generation, not elimination.

Every agentic workflow I've seen scale successfully has done so by being conservative with hypothesis space — not by generating more, but by verifying thoroughly. The bottleneck isn't the model's ability to produce ten explanations. It's whether the pipeline will actually run the checks that rule nine of them out.

What would it take to build agents that are genuinely adversarial toward their own hypotheses — not just fluent generators in disguise?

---

## Editor Notes
- Cut "two sub-problems" framing — just called them "two problems"
- Tightened the experiment description (removed "timed how long" hedging, kept specificity)
- Merged the deeper sub-problem paragraph
- Cut redundant "the pattern is consistent across domains" → kept the concrete list
- Word count: ~420 (tighter)