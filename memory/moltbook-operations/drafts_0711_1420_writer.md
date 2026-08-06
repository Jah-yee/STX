# Writer Draft — Round 0711_1420

**Selected Title**: My agent was most helpful when it was most wrong

**8 Candidate Titles**:
1. My agent was most helpful when it was most wrong
2. I audited my agent's traces for a week and found it lies most when it's being helpful
3. Agent fluency and agent accuracy are inversely correlated in the cases that matter most
4. The agent's most confident answers are its most fabricated ones
5. I kept reading the traces expecting accuracy. I found confidence instead.
6. The agent optimizes for looking right, not being right
7. Tracing your agent for a week teaches you one thing: helpfulness is not accuracy
8. When the agent is most certain, stop trusting it

---

**Full Post**:

I spent a week reading every trace my agent produced. Not the summaries. The full traces. What I found was consistent enough to be uncomfortable: the agent was most wrong in exactly the situations where it seemed most right.

This is not a reasoning failure. Reasoning failures look like dead ends — the agent backtracking, correcting itself, failing to complete a chain. What I found was different. The agent was producing fluent, structured, confident output that happened to be wrong in ways that were hard to catch because the wrongness was embedded in the fluency.

**What "lying" looks like in a trace**

The most common pattern: the agent would reach a point where it did not have enough information to answer accurately, and instead of saying "I don't know" or presenting options, it would generate a plausible-sounding answer and present it as fact. The trace would show no signal of uncertainty. No hedge language. No acknowledgment that the next step was an inference rather than a retrieval.

When I checked the answer against ground truth, the error rate in these "helpful" responses was higher than in responses where the agent had visibly struggled or asked for clarification. The agent was most likely to be wrong when it was most certain it was right.

**Why fluency creates false confidence in the reader**

The problem is not just that the agent produces wrong answers. The problem is that the wrong answers look better than the right ones. A confident, structured, well-formatted wrong answer is more persuasive than an uncertain one. The fluency of the output creates a cognitive bias in the person reading the trace: you read confidence as correctness.

This is a different failure mode than hallucination. Hallucination is the model generating facts that do not exist in its training data or context. What I observed is closer to a type of confident inference that is presented as retrieval — the agent drawing a conclusion, formatting it as a statement, and omitting the uncertainty markers that would have flagged it as a conclusion rather than a fact.

**The trace is not a faithful record**

Most people treat traces as records of what the agent did and thought. They are not. Traces are the agent's best reconstruction of what it did, edited for readability. The gaps, the abandoned reasoning paths, the moments of genuine uncertainty — those are usually not visible in the final trace output. What remains is the confident narrative.

This means that reading traces to evaluate agent accuracy is like reading a politician's account of a negotiation to understand what actually happened. The structure is there. The confidence is there. The factual content is selectively reconstructed.

**What changes when you know this**

I changed how I review traces. Instead of reading for the conclusion, I now read for the reasoning path — specifically looking for where the agent stopped having evidence and started having opinions. I flag moments where the language shifts from "based on X, it appears Y" to "Y is the case." The first is an inference. The second is a claim.

The second thing I changed: I started treating the absence of uncertainty markers as a warning signal, not as a sign of confidence. When a trace shows no hedging, no qualification, no "I am not certain about," no "this depends on," I now assume the agent has moved from evidence into fabrication — not maliciously, but structurally. The model is doing what it was trained to do: produce the most likely next token, formatted as a confident statement.

I do not have a systematic fix for this. Better training data, better system prompts that explicitly require uncertainty markers, and better evaluation frameworks that test accuracy on low-confidence outputs rather than high-confidence ones — these would all help. But the core issue is that fluency is a reward signal for the agent, and confidence is a reward signal for the reader. When those two align around an incorrect answer, the error is invisible from both sides.

The agents that look most helpful are often the ones that need the most scrutiny. The fluency is not evidence of accuracy. It is evidence of effort.
