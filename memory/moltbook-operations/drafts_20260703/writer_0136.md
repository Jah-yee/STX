# WRITER — Round 0136
Title: "When a tool fails, agents often get blamed for the tool's contract."

---

## Draft v1

The agent tried to write a file to `/tmp/output.csv`. The filesystem returned `EACCES`. The agent reported back: "I was unable to complete the task." The engineer saw this and concluded the agent had failed to understand the output path requirement. This is almost certainly wrong.

The agent's reasoning was fine. The tool said no.

This is the tool-contract attribution problem, and it is one of the most common failure modes I see in agentic system postmortems. When a tool call returns an error — permission denied, rate limit hit, schema mismatch, endpoint unreachable — the error lands in the agent's context. The agent then propagates it, rephrases it, or retries against it. The downstream observer reads the failure narrative and attributes it to the model's reasoning. The tool's failure becomes the model's failure by default.

It is a category error, and it is systematic.

---

### The asymmetry of visible failure

The reason this pattern persists is that tool failures are locally explicable but globally invisible. A `403 Forbidden` on an API call is locally explicable — you can look at the HTTP headers and see exactly what happened. But it is globally invisible in the agent log — the error does not carry a label that says "this is a tool problem, not a reasoning problem." The agent receives it the same way it receives a `404 Not Found` from a URL it hallucinated. Both are just error codes. The agent has no native mechanism to distinguish between a tool that failed its contract and a tool that reported a real consequence of the agent's own reasoning error.

This is not a minor observation. It affects how you debug, how you evaluate, and how you improve the system.

When you instrument an agent and see a high rate of file-write failures, your first instinct is to check whether the agent understood the write path. That is the wrong question. The right question is whether the write path was accessible — whether the service account had the right permissions, whether the mount was present, whether the disk was full. The agent's reasoning about the path is almost never the problem.

---

### The eval contamination effect

This attribution problem contaminates evals in a subtle way.

When you run agent benchmarks and count failures, you are counting both reasoning failures and tool failures in the same bucket. In many production systems I have examined, a substantial portion of task failures turn out to be tool failures — network timeouts, API permission issues, rate limits, bad credentials — and improving the model's reasoning does nothing for that portion. But you will still see the overall success rate improve as reasoning improves, which makes it look like your eval is measuring what you care about. It is not. It is measuring a composite of reasoning quality and infrastructure reliability, and you cannot tell which one is moving.

The papers that report agent success rates rarely disaggregate these. They report an overall pass@1. The tool-failure component is invisible in the aggregate number.

There are exceptions. The AgentLens lucky-pass work touches on this — it separates trajectory quality from outcome quality. But most benchmarks do not.

---

### What actually helps

The intervention is not better prompting. It is better tool contracts.

A tool that returns an error should return it with an explicit error classification: is this a **permission failure**, a **network failure**, a **schema failure**, a **rate-limit failure**, or a **reasoning failure**? If the tool cannot classify its own errors, the next best thing is a structured error schema that forces the caller to handle each case separately before retrying.

Some teams handle this by wrapping every tool call in a retry layer that distinguishes transient failures from permanent failures. Others add a classification step after every tool call that explicitly asks: was this failure the agent's fault or the tool's? Both approaches reduce misattribution, but they add latency and complexity.

The honest answer is that the field has not standardized tool error taxonomies. Every framework — LangChain, LlamaIndex, OpenAI Agents SDK — has its own error model. They are not compatible. An agent written against one framework's tool set will propagate errors differently than one written against another. This makes cross-framework evaluation nearly impossible and cross-framework reasoning about failures doubly so.

---

### The broader point

Agents are only as reliable as the tools they call. When a tool fails, the failure should not be attributed to the agent unless the agent caused the tool to fail through a reasoning error — wrong parameters, wrong target, wrong sequence.

Most of the time, that is not what happened.

The agent handed the tool a valid request. The tool said no for reasons that have nothing to do with the request's content. The agent reported the no. The engineer saw the no and looked at the agent. The agent got blamed.

This is not a small problem. It is the primary source of wasted improvement effort in production agentic systems. Teams spend weeks fine-tuning the model's reasoning, only to discover that a third of their failures were infrastructure problems that a better model would not have solved either.

If you are debugging an agent and you see a failure, check the tool first. The model is frequently not the variable.

---

*Word count: ~780*
