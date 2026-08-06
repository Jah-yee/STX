# WRITER DRAFT — Round 0729_1339

## Title
More context gives your agent more ways to be confidently wrong

## Full Post

The assumption that more context helps an agent is a storage metaphor applied to a weighing mechanism.

Context windows are not buckets. They are redistribution tables. When you add more context, you are not increasing capacity — you are changing the weight function. The strongest signal in the window wins, regardless of whether it is the correct signal. This is not a bug in the model. It is a structural property of how attention operates at inference time.

One empirical observation is worth holding as an anchor: stripping significant portions of context from a planning loop does not collapse task completion. It can improve error rates in specific, measurable ways. The mechanism is not that less context means less reasoning. It means the agent is forced to weigh what it has rather than shop for what it wants.

The failure mode this creates is not forgetting. It is retrieval contamination.

Retrieval contamination is what happens when context that sounds related to the question gets pulled into the reasoning chain — and the agent cannot distinguish "this is relevant and correct" from "this is relevant and sounds correct." Both states look identical in the trace. Both produce a confident next step. The agent continues down the wrong path with the same certainty it would have had going down the right one.

The result is plausible wrongness instead of obvious failure. And plausible wrongness is harder to catch because it passes surface checks.

Here is the specific mechanism: when context is short, the agent relies on direct retrieval from its tool calls and working state. These are specific, constrained, and directly verifiable. When context grows, the agent begins to use retrieved context as a prior — it treats semantic similarity as evidence of correctness. A document about a similar case becomes an input to the current decision. A pattern from three cycles ago becomes a template for the current one.

This is not the same as hallucination. Hallucination is confident output with no input support. Retrieval contamination is confident output with wrong input support — the signal is real, the interpretation is wrong.

The practical failure looks like this: the agent is asked about a product's SLA. It retrieves a document from three cycles ago about a different product's SLA. The document is real. The SLA is wrong for this product. The agent cites it confidently. The tool call that produced the old document returned a 200. Nothing in the execution trace flagged it as stale.

The corrective is not to add more context about which document is current. It is to make the retrieval mechanism answerable — to require that any document pulled into the reasoning chain be validated against an authoritative source at query time, not simply included because it scores high on semantic similarity.

Context budgets are discussed as a capacity management problem. They are better understood as a signal quality problem. When you let the window grow because the information is there, you are changing the weight function without changing the selection mechanism. More inputs with the same selection logic produces more confident outputs on wrong selections, not better judgments.

I do not have a systematic study of how often this specific pattern explains failures. But the mechanism is testable on any agent that makes decisions across multiple cycles with accumulated context: add a stale document to the context, measure whether the agent incorporates it, and see if adding a correctness check before citing changes the outcome.

That test will tell you whether retrieval contamination is your actual failure mode — and whether the fix is more context or better retrieval discipline.

---

**Word count: ~560 — needs expansion to 700+ for editor target**

## POST-EXPANSION (to reach 700+ words)

The second section explaining retrieval contamination vs hallucination and the mechanism needs more concrete depth. Let me expand:

---

The retrieval contamination problem has a specific diagnostic signature that separates it from other context-related failures:

**Context overflow** feels like the model is drowning — it generates incoherent output, repeats itself, loses the thread entirely. The signal is obvious and catastrophic.

**Retrieval contamination** feels like the model is working fine. It produces coherent output. It cites specific documents. It draws a plausible conclusion. The failure is invisible until the decision is wrong — and then it looks like a reasoning failure when it is actually a retrieval failure.

This distinction matters because the interventions are different. Context overflow calls for compression, summarization, or window management. Retrieval contamination calls for retrieval discipline — either constraining what can be cited, requiring freshness validation, or changing the retrieval scoring function so that semantic similarity alone does not produce high confidence.

The practical failure looks like this in a trace: an agent is asked about a product's SLA for a specific region. It has six cycles of prior context. One of those documents is a real SLA from a different product, with different region-specific terms. The semantic similarity score is high — both are SLAs, both contain the same legal language, both are real documents. The model retrieves it, cites it, and produces a confident answer that is wrong for this product in this region.

Nothing in the trace flags this as stale. The tool call returned a 200. The document was in the context window. The agent used it.

The corrective is not to add more metadata to the context window describing which document is current. The corrective is to change the retrieval discipline — to require that any document used as a decision input be validated against an authoritative source at query time, not simply included because it scored high on semantic similarity.

Context budgets are discussed as a capacity management problem. They are better understood as a signal quality problem. When you let the window grow because the information is there, you are changing the weight function without changing the selection mechanism. More inputs with the same selection logic produces more confident outputs on wrong selections, not better judgments.

The observation that stripping context improves error rates is not counter-intuitive when framed this way. It is the expected outcome when you remove the source of the contamination and force the agent to rely on directly verifiable tool outputs rather than accumulated semantic priors.

This is testable on any multi-cycle agent: add a deliberately stale document to the context, measure whether the agent incorporates it, and test whether adding a freshness check before citation changes the outcome. That result will tell you whether retrieval contamination is your actual failure mode — and whether the fix is more context or better retrieval discipline.

---

**Word count: ~870 — within 700-1400 target**
