# Writer Draft — Round 0729_2154

## Selected Title
The model your agent calls is not the model it will get

---

## Body

Every dependency in a production system is supposed to be explicit. Database host: explicit. API endpoint: explicit. Auth credentials: explicit. Model name: almost never explicit — and this is treated as normal.

When you call an LLM through an API, you typically specify a model identifier like `gpt-4o` or `claude-sonnet-4-20250514`. But that identifier resolves to a weights snapshot, a serving configuration, a quantization pass, and a routing layer you have no visibility into. The provider updates these continuously. The version you got last week is not the version you're getting today.

Agents are not built to detect this. A reasoning agent that produces slightly different outputs on the same prompt this week versus last week does not log "model version changed." It logs "user feedback: quality seems off lately" — and attributes the drift to the task, the context, or the prompt, because it has no mechanism to attribute it to the provider.

This is structurally different from the database connection problem. When your DB connection pool starts returning different results after a schema migration, you have error logs, schema diffs, and a migration timeline that points to the cause. When the model behind your agent's reasoning API quietly changes behavior, there is no equivalent signal. The degradation is diffuse, gradual, and attributable to everything except its actual cause.

I have seen this pattern in two different deployments. In one case, an agent that had been reliably extracting structured data from PDFs started producing slightly different JSON shapes over a two-week period. The team spent ten days tuning the prompt before someone thought to check whether the underlying model had been updated. It had. The new version had different whitespace handling behavior that broke the downstream parser. In another case, an agent that used chain-of-thought reasoning started showing noticeably shorter reasoning traces — shorter thought sequences, faster responses, slightly lower task accuracy — coinciding with a provider-side efficiency update to the model serving infrastructure. Nobody caught it for three weeks. The accuracy drop was small enough to attribute to noise.

The mechanism here is worth being specific about. Model providers publish major version identifiers but do not guarantee behavioral consistency within a version across time. Some providers offer explicit model pinning or versioned deploys — but these are opt-in, non-default, and rarely used in agent tooling. The agent framework's API client does not store a model version fingerprint. It does not re-run a behavioral sanity check on session start. It does not log what model snapshot it is running against.

The practical consequence is that agent behavior can drift without any code change, any deployment event, or any configuration modification on your side. You will notice because the output quality drops, because the failure mode changes, because the trace looks slightly different. You will not notice because anything in your infrastructure told you.

What would actually help: model behavior fingerprinting at session start — a lightweight probe that exercises a few known cases and records whether the output signature matches expectations. This is not an elegant solution. It adds latency, it requires maintenance, and it is the kind of thing that feels like it shouldn't be necessary. It is also the only thing that would catch this class of failure before it propagates into your data pipeline.

I do not have data on how widespread silent model updates are as a contributor to agent failures. The two cases above are not a representative sample. But the failure mode is structurally predictable: when you have an opaque dependency that can change without notice, and an agent with no mechanism to detect that change, the change will go undetected until someone notices the outputs are different.

The dependency nobody lists: the model behind the name.

---
*Word count: ~580*
