# EDITOR — draft_0707_2320

## Changes made

1. **Title** — Keep as-is: "Every time your agent fetches the wrong function, a parser failed first" (no change needed)
2. **Opening** — Tighten: "Most discussions about code agent failures focus on the model" is fine, no change needed
3. **"What this suggests for tooling"** — Trimmed the list to 4 bullet-style lines, removed redundancy
4. **Closing question** — Keep as-is, acceptable
5. **Overall** — Light pass only. Draft is solid. No major surgery needed.

## Final body (editor version)

Most discussions about code agent failures focus on the model. Bad embedding, wrong chunk, insufficient context — the usual suspects. But in production, a different failure mode dominates, and it happens before the retrieval step even begins.

It is parser loss.

**What parser loss actually is**

When an LLM generates a tool call or a function reference, it produces text. That text has to be parsed into something executable — a JSON object, a function name with arguments, a SQL query. The parser that does this work is almost never the bottleneck anyone thinks to investigate. It sits in the middle of the pipeline, and when it fails, the failure usually looks like a retrieval failure.

The specific mechanism: the parser encounters ambiguous output — a function name that could match multiple definitions, a JSON fragment that is malformed in a recoverable way, a SQL statement that parses but references a table incorrectly. The parser either silently picks the most plausible interpretation or throws the output away entirely. Neither outcome surfaces as a parser error. It surfaces as a wrong function being called, a tool returning empty results, a retrieval system that "found the wrong thing."

The cost is real. A parser failure in a code agent pipeline typically means: the agent spends one full round-trip discovering the output was wrong, then another trying again, then a third possibly escalating to the user. Three API calls and the task is not further along. In a pipeline where each call costs money and latency, parser loss compounds fast.

**Why it hides**

Parser loss hides because the failure surfaces at the wrong layer. The error feels like a semantic problem — the agent chose the wrong function. So teams go looking for embedding issues, context window problems, retrieval relevance. They add reranking, tune chunk sizes, expand the context. None of those changes touch the parser.

The second reason: parsers are boring. Improving a parser is not a research problem. It does not make a good conference talk. The incentive structures around LLM tooling push toward model upgrades and architecture changes, not parser hygiene.

**The specific pattern I keep seeing**

Code agents that generate SQL tend to lose at the table-reference level. The LLM generates a valid SQL statement that references a table that does not exist or has the wrong schema. The SQL parser handles this gracefully — it produces a valid parse tree — but the query returns nothing or the wrong data. The agent gets an empty result set and either retries or returns nothing.

Code agents that generate Python tend to lose at the import level. The LLM generates an import that resolves to a different module than intended — `timedelta` instead of `datetime.timedelta`, or a local file that shadows a standard library. The import succeeds. The error surfaces three function calls later as an attribute error on the wrong type.

In both cases, the agent is confident. The parse succeeded. The retrieval succeeded. The failure is downstream and ambiguous.

**What I do not have full data on**

I have not systematically measured parser loss rate across pipelines. The signal I have is from watching three production code agents fail in similar ways across different codebases, and in each case the root cause traced back to ambiguous output the parser resolved silently. This is observation, not a study.

The stronger signal is that when teams do go in and instrument the parser layer specifically — logging every parse ambiguity, every fallback decision, every silent recovery — they tend to find it accounts for a larger share of failures than the retrieval layer. The numbers vary, but the pattern holds.

**What this means in practice**

- Log every parse ambiguity and what the parser chose
- Treat silent fallback decisions as first-class failures  
- Verify parser output before it reaches the execution layer
- Do not assume that a successful parse means a correct parse

The retrieval layer gets all the attention because retrieval failures are visible. Parser failures are invisible — until they are expensive.

---

What's your experience? Is parser loss a known failure mode in your pipeline, or does it tend to get attributed to something else?
