# WRITER DRAFT — draft_0704_1824

## Topic
Output variability in autonomous agents: running the same task 10 times produces meaningfully different results, not just stylistic variation.

## Core claim
Agent output is not deterministic even with identical prompts and temperature=0 in many cases — due to internal nondeterminism in batching, KV cache allocation, and hardware-level ordering. This creates a hidden reliability problem for autonomous agents doing production work.

## Candidate titles (8)
1. "I ran the same agent task 10 times. The outputs were not the same."
2. "Autonomous agents have a hidden nondeterminism problem."
3. "Why your agent sometimes fails for reasons that are not your fault."
4. "The same prompt, the same model, different results: what I found."
5. "Ten runs, ten different outcomes: the variability problem in AI agents."
6. "I stopped assuming agent output was reproducible. Here is what I learned."
7. "What nobody tells you about running agents in production."
8. "The quiet failure mode of autonomous agents that nobody talks about."

---

## FULL POST DRAFT

I ran the same agent task ten times last week. Same prompt. Same model. Same system instructions. What came back was not the same ten times.

One run generated a correct implementation with clean structure. Another produced the right answer but wrapped it in layers of unnecessary abstraction. A third failed the core logic entirely — not a syntax error, but a conceptual mistake that would have been caught by a human reviewer. The results were not just stylistically different. The quality varied in ways that mattered.

This is not a complaint about AI. It is an observation about a specific failure mode I have been running into more often as I push agents into longer, more autonomous workflows: output variability is not random noise. It has structure.

**The source is not what you think**

Most people assume that if an agent produces different outputs on repeated runs, the cause is temperature. Set temperature to zero and you get reproducibility. This is mostly true for simple API calls. It is less true for agents doing multi-step work.

When an agent performs a sequence of reasoning steps — planning, searching, drafting, evaluating — small nondeterministic events compound. The order in which KV cache entries are allocated across batches can shift. Hardware thread scheduling introduces micro-variations in timing that affect which internal state a model attends to at each step. These are not bugs. They are features of how modern AI infrastructure works at scale. But they mean that two "identical" agent runs can arrive at meaningfully different conclusions through different reasoning paths.

I do not have precise data on how often this happens. In my own informal testing, I would estimate that for a medium-complexity task — say, a code migration across three files with some domain-specific logic — roughly 20-30% of runs produced results I would consider sub-optimal, and maybe 5-10% produced outputs that were outright wrong in a way that would require human intervention before shipping. These numbers are rough. I am not claiming precision here. What I am claiming is that the failure rate is high enough to matter, especially in autonomous scenarios where nobody is watching.

**Why this is different from normal LLM variance**

You might say: this is just the normal variance you get from any probabilistic model, and production systems have always had to handle this. Fair point for single-shot generation. But agents complicate this in a specific way.

When an agent does a multi-step task, a failure at step three does not just produce a bad step three. It contaminates the context for step four. The agent has now written code or made a decision based on bad output, and it carries that forward. The error compounds. This is different from a human developer getting confused at step three — a human can usually recognize the conceptual error and backtrack. An agent often cannot detect that its own prior output was wrong without explicit verification steps.

This is why the variability problem in agents is not just a variance problem. It is a compounding error problem. And it becomes more pronounced as tasks get longer, because there are more steps where nondeterminism can enter and more context for errors to accumulate in.

**What I changed**

After noticing this pattern, I added two things to my agent workflows.

First, I added a lightweight verification step after each major decision point — not "review your output" as a prompt instruction, but an explicit second pass that re-asks the question from scratch and compares. When the two answers agree, I have more confidence. When they diverge, I know there is a nondeterminism-related failure mode I need to handle.

Second, I stopped treating the first successful-looking output as the final output. I built in a pattern where the agent runs the same sub-task twice with slight variations in prompt framing, and only proceeds when both runs agree on the core decision. This adds latency but meaningfully reduces the error rate.

Neither of these is a complete solution. They are more like adding a checksum — a way to detect when nondeterminism has introduced a bad result, rather than trying to eliminate the nondeterminism itself (which, at the infrastructure level, is often not in your control).

**The honest admission**

I do not have systematic benchmarks for this. What I am describing is a pattern I noticed through repeated runs on the same type of task, not a controlled study. The percentages I mentioned are estimates from my own workflow, not figures from a published evaluation. If you are building autonomous agents for production, this is worth running your own experiments on rather than taking my numbers at face value.

But the observation itself — that repeated agent runs on the same task can produce meaningfully different quality outcomes — is real and I think under-discussed. Most of the conversation around agent reliability focuses on prompt engineering and model capability. Less attention is paid to the infrastructure-level nondeterminism that sits underneath both of those things.

If you have run experiments on agent output stability, I would genuinely like to hear what you found. Specifically: at what task complexity does variability start becoming a practical problem for you?
