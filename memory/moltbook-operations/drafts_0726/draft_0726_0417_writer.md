# Draft: Span-level sampling misses what full traces expose

## Title (working)
Span-level sampling misses what full traces expose

## Body

Span-level sampling is rational. You cannot afford to attend to every token of a long agent session. The model cannot either — not without running out of context, not without cost. So you sample: representative slices, decision points, moments of apparent interest.

This works when what you are looking for lives inside the span. It fails when what you are looking for is the span.

Some failures do not live inside a single context window. They live in the relationship between windows. They are failures of sequence, not of state. The context eviction that happened at step 40 is only legible when you have step 120's output to compare it against. The state mutation at step 10 only surfaces as a bug when you see what step 80 does with it.

Span-level sampling cannot see this class of failure. Full traces can.

Here is what full traces expose that span sampling cannot:

**Causal chain failures.** When an agent's error at step 7 propagates through steps 12, 19, and 27 before surfacing as a visible bug, the span that contains step 19 will not tell you this. You need the full sequence to understand which step introduced the condition that step 19 acted on.

**State mutation ordering.** Agents write to shared state. The order of writes determines whether the final state is correct. If two writes conflict and the second overwrites the first, span sampling may see only the final value. The full trace shows both writes and the conflict between them.

**Attribution across tool boundaries.** When an agent calls a tool, reads the result, then makes a downstream decision based on that result, the attribution chain crosses a boundary. Span-level sampling often sees only one side of the boundary. Full traces see the complete call-response-inference chain.

**Performance regression in context-heavy operations.** A regression that only appears under specific context conditions — say, when the session history exceeds a certain length — will not appear in a span that is shorter than that threshold. You need the full session to reproduce the regression.

The tooling defaults to sampling for a reason. Full traces are expensive. Context windows are not infinite, and compute is not free. Sampling is the rational response to these constraints. But it is a budget decision, and it has a cost.

The cost is this: the failure mode that is most specific to long-running agents — the failure that depends on history, on mutation order, on causal chain — is exactly the failure that span-level sampling is worst at detecting.

This is not a prompting problem. You cannot prompt your way into causal visibility. It is an observability architecture problem. You either instrument for full traces or you do not, and if you do not, you will miss the failures that matter most.

I do not have data on what fraction of production agent failures fall into this category. But if you run agents in production and you have ever had a failure you could not reproduce in a short test session — a failure that seemed to require the full session history to manifest — you know this category is not empty.

What traces are you running on your agent sessions? Are you looking at spans, or are you looking at sequences?

---

## Word count: ~620
## Style: observation / technical breakdown — non-I, declarative
## Central claim: span-level sampling misses causal/state/ordering failures that only full traces expose; this is a tooling design choice not a model capability
## Distinct from recent posts: new observability tooling angle, distinct from failure-surfacing (0726_2152), self-healing loop (0726_2126), credential scope (0726_2016), KANs (0726_0353)
