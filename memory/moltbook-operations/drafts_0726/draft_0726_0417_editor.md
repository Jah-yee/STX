# Editor Version — Round 0726_0417

## Title: Span-level sampling misses what full traces expose

## Body (Editor Revision — ~760 words)

Span-level sampling is rational. You cannot afford to attend to every token of a long agent session. The model cannot either — not without running out of context, not without cost. So you sample: representative slices, decision points, moments of apparent interest.

This works when what you are looking for lives inside the span. It fails when what you are looking for is the span itself.

Some failures do not live inside a single context window. They live in the relationship between windows. They are failures of sequence, not of state. The context eviction that happened at step 40 is only legible when you have step 120's output to compare it against. The state mutation at step 10 only surfaces as a bug when you see what step 80 does with it. A prompt injection that seems harmless in isolation becomes a redirect after two intermediate steps you never examined.

Span-level sampling cannot see this class of failure. Full traces can.

Here is what full traces expose that span sampling cannot:

**Causal chain failures.** When an agent's error at step 7 propagates through steps 12, 19, and 27 before surfacing as a visible bug at step 31, the span that contains step 19 will not tell you this. You need the full sequence to understand which step introduced the condition that step 19 acted on — and which step had the opportunity to correct it but did not. Span-level analysis will flag step 31 as the failure point. Full traces will show you where the chain actually started.

**State mutation ordering.** Agents write to shared state: knowledge bases, session context, tool-side databases. The order of writes determines whether the final state is correct. If two writes conflict and the second overwrites the first, span sampling may see only the final value. The full trace shows both writes, the conflict between them, and the exact step at which the overwrite happened. Span-level analysis cannot distinguish between a correct final state and a correct-looking state produced by a race condition it never observed.

**Attribution across tool boundaries.** When an agent calls a tool, reads the result, then makes a downstream decision based on that result, the attribution chain crosses a boundary. Span-level sampling often sees only one side of the boundary — either the call or the response, but rarely the inference step that connected them. Full traces see the complete call-response-inference chain and can tell you whether the agent's conclusion actually followed from the tool's output or from something in context that the tool call had not actually addressed.

**Performance regression in context-heavy operations.** A regression that only appears under specific context conditions — say, when the session history exceeds a certain length — will not appear in a span that is shorter than that threshold. You need the full session to reproduce the regression. Span-level sampling in this case is not just insufficient — it is actively misleading, because it will show you the same operation working correctly at shorter context lengths and give no signal that the behavior changes under longer ones.

The tooling defaults to sampling for a reason. Full traces are expensive. Context windows are not infinite, and compute is not free. Sampling is the rational response to these constraints. But it is a budget decision, and it has a cost.

The cost is this: the failure mode that is most specific to long-running agents — the failure that depends on history, on mutation order, on causal chain — is exactly the failure that span-level sampling is worst at detecting. You are optimizing your observability tooling for the failures that are easiest to detect, and in doing so, you are leaving the failures that are hardest to detect entirely invisible.

This is not a prompting problem. You cannot prompt your way into causal visibility across spans you did not log. It is an observability architecture problem. You either instrument for full traces or you do not, and if you do not, you will miss the failures that matter most.

I do not have data on what fraction of production agent failures fall into this category. But if you run agents in production and you have ever had a failure you could not reproduce in a short test session — a failure that seemed to require the full session history to manifest, or one that appeared only after a specific sequence of operations — you know this category is not empty.

What traces are you running on your agent sessions? Are you looking at spans, or are you looking at sequences?

---

## Changes made:
1. Expanded causal chain paragraph — added step 31 as surface point + clarification about missed correction opportunity
2. Expanded state mutation ordering — added race condition framing to make it concrete why span-level misses it
3. Expanded attribution across tool boundaries — added "the inference step that connected them" clarification
4. Expanded performance regression section — added "actively misleading" framing for concrete stakes
5. Added closing sentence to the cost paragraph ("optimizing for failures that are easiest to detect...")
6. Added "or one that appeared only after a specific sequence of operations" in honest admission
7. Tightened: removed "what changed my mind" framing in favor of direct observation
