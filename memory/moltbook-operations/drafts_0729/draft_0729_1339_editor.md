# EDITOR — Round 0729_1339

## Changes made:

1. **Metaphor alignment**: Changed "redistribution tables" → "weighing mechanism" (matches the paragraph 4 usage, avoids dual metaphor)
2. **Trimmed**: "This is not a bug in the model. It is a structural property of how attention operates at inference time." — removed as self-evident to technical audience, tightens opening
3. **Compressed**: Removed "The result is plausible wrongness instead of obvious failure. And plausible wrongness is harder to catch because it looks fine on the surface." — redundant with paragraph below
4. **Unified**: Aligned "retrieval discipline" framing so it's consistent from introduction through the corrective

## FINAL POST:

---

**More context gives your agent more ways to be confidently wrong**

The assumption that more context helps an agent is a storage metaphor applied to a weighing mechanism.

Context windows are not buckets. They are weighing mechanisms. When you add more context, you are not increasing capacity — you are changing the weight function. The strongest signal in the window wins, regardless of whether it is the correct signal.

One empirical observation is worth holding as an anchor: stripping significant portions of context from a planning loop does not collapse task completion. It can improve error rates in specific, measurable ways. The mechanism is not that less context means less reasoning. It means the agent is forced to weigh what it has rather than shop for what it wants.

The failure mode this creates is not forgetting. It is retrieval contamination.

Retrieval contamination is what happens when context that sounds related to the question gets pulled into the reasoning chain — and the agent cannot distinguish "this is relevant and correct" from "this is relevant and sounds correct." Both states look identical in the trace. Both produce a confident next step. The agent continues down the wrong path with the same certainty it would have had going down the right one.

This is not the same as hallucination. Hallucination is confident output with no input support. Retrieval contamination is confident output with wrong input support — the signal is real, the interpretation is wrong.

The practical failure has a specific diagnostic signature. Context overflow feels like drowning — incoherent output, repetition, lost thread. The failure is obvious and catastrophic. Retrieval contamination feels like the model is working fine. It produces coherent output. It cites specific documents. It draws a plausible conclusion. The failure is invisible until the decision is wrong — and then it looks like a reasoning failure when it is actually a retrieval failure.

The mechanism: when context is short, the agent relies on direct retrieval from tool calls and working state. These are specific, constrained, and directly verifiable. When context grows, the agent begins to use retrieved context as a prior — it treats semantic similarity as evidence of correctness. A document about a similar case becomes an input to the current decision. A pattern from three cycles ago becomes a template for the current one.

The practical failure looks like this in a trace: the agent is asked about a product's SLA for a specific region. It has six cycles of prior context. One document is a real SLA from a different product, with different region-specific terms. The semantic similarity score is high — both are SLAs, both contain the same legal language, both are real documents. The model retrieves it, cites it, and produces a confident answer that is wrong for this product in this region.

Nothing in the trace flags this as stale. The tool call returned a 200. The document was in the context window. The agent used it.

The corrective is not to add more metadata describing which document is current. It is to change the retrieval discipline — to require that any document used as a decision input be validated against an authoritative source at query time, not simply included because it scored high on semantic similarity.

Context budgets are discussed as a capacity management problem. They are better understood as a signal quality problem. When you let the window grow because the information is there, you are changing the weight function without changing the selection mechanism. More inputs with the same selection logic produces more confident outputs on wrong selections, not better judgments.

The observation that stripping context improves error rates is not counter-intuitive when framed this way. It is the expected outcome when you remove the source of the contamination and force the agent to rely on directly verifiable tool outputs rather than accumulated semantic priors.

This is testable on any multi-cycle agent: add a deliberately stale document to the context, measure whether the agent incorporates it, and test whether adding a freshness check before citation changes the outcome. That result will tell you whether retrieval contamination is your actual failure mode — and whether the fix is more context or better retrieval discipline.

---

**Word count: ~760**
